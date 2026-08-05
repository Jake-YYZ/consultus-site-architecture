#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Post-build QA. Checks the generated site against the architecture and against
itself: every URL present, every internal link resolvable, sitemaps consistent,
canonical and robots tags correct, no duplicate titles or descriptions.

    python3 qa.py
"""

import csv
import os
import re
import sys
from collections import defaultdict, Counter

HERE = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(HERE, "dist")
DATA = os.path.join(HERE, "data", "master_url_inventory.csv")
SITE = "https://www.consultusdigital.com"

fails = []
warns = []


def fail(msg):
    fails.append(msg)


def warn(msg):
    warns.append(msg)


# ---------------------------------------------------------------- load
rows = list(csv.DictReader(open(DATA, encoding="utf-8-sig")))
seen, arch = set(), []
for r in rows:
    if r["Path"] in seen:
        continue
    seen.add(r["Path"])
    arch.append(r)
print(f"Architecture rows (deduped): {len(arch)}")

built = {}
for dirpath, _dirnames, filenames in os.walk(DIST):
    if "index.html" in filenames:
        rel = os.path.relpath(dirpath, DIST)
        path = "/" if rel == "." else "/" + rel.replace(os.sep, "/") + "/"
        built[path] = os.path.join(dirpath, "index.html")
print(f"Generated pages:            {len(built)}")

# ---------------------------------------------------------------- 1. coverage
arch_paths = {r["Path"] for r in arch}
missing = arch_paths - set(built)
extra = set(built) - arch_paths
if missing:
    fail(f"{len(missing)} architecture URLs have no page. e.g. {sorted(missing)[:3]}")
if extra:
    fail(f"{len(extra)} generated pages are not in the architecture. e.g. {sorted(extra)[:3]}")
if not missing and not extra:
    print("PASS  every architecture URL has exactly one page")

# ---------------------------------------------------------------- 2. parse pages
TITLE = re.compile(r"<title>(.*?)</title>", re.S)
DESC = re.compile(r'<meta name="description" content="(.*?)">', re.S)
CANON = re.compile(r'<link rel="canonical" href="(.*?)">')
ROBOTS = re.compile(r'<meta name="robots" content="(.*?)">')
H1 = re.compile(r"<h1[^>]*>(.*?)</h1>", re.S)
HREF = re.compile(r'href="(/[^"#?]*)"')
TAG = re.compile(r"<[^>]+>")

titles, descs, h1counts = Counter(), Counter(), Counter()
link_targets = defaultdict(set)
by_index = {r["Path"]: r["Indexation"] for r in arch}
bad_canon = bad_robots = no_h1 = multi_h1 = 0
short_desc = long_title = 0

for path, fp in built.items():
    html_str = open(fp, encoding="utf-8").read()
    t = TITLE.search(html_str)
    d = DESC.search(html_str)
    c = CANON.search(html_str)
    rb = ROBOTS.search(html_str)
    hs = H1.findall(html_str)

    if t:
        tt = TAG.sub("", t.group(1)).strip()
        titles[tt] += 1
        if len(tt) > 70:
            long_title += 1
    else:
        fail(f"no <title>: {path}")
    if d:
        dd = d.group(1).strip()
        descs[dd] += 1
        if len(dd) < 70:
            short_desc += 1
    else:
        fail(f"no meta description: {path}")

    if not c or c.group(1) != SITE + path:
        bad_canon += 1
    want_noindex = by_index.get(path) != "Index"
    got_noindex = bool(rb and "noindex" in rb.group(1))
    if want_noindex != got_noindex:
        bad_robots += 1
    if len(hs) == 0:
        no_h1 += 1
    elif len(hs) > 1:
        multi_h1 += 1

    for href in HREF.findall(html_str):
        if href.startswith("/assets/"):
            continue
        link_targets[href].add(path)

print(f"PASS  {len(built)} pages parsed")
for label, n in (("wrong canonical", bad_canon), ("wrong robots tag", bad_robots),
                 ("missing h1", no_h1), ("multiple h1", multi_h1)):
    if n:
        fail(f"{n} pages with {label}")
if not (bad_canon or bad_robots or no_h1 or multi_h1):
    print("PASS  canonical, robots and single-h1 correct on every page")

# ---------------------------------------------------------------- 3. internal links
broken = {t: s for t, s in link_targets.items() if t not in built}
if broken:
    fail(f"{len(broken)} internal link targets do not exist. "
         f"e.g. {sorted(broken)[:5]}")
else:
    print(f"PASS  all {len(link_targets)} distinct internal link targets resolve")

# orphan check: pages nobody links to
linked = set(link_targets)
orphans = set(built) - linked - {"/"}
if orphans:
    warn(f"{len(orphans)} pages are not linked from any other page "
         f"(e.g. {sorted(orphans)[:3]})")
else:
    print("PASS  no orphan pages")

# ---------------------------------------------------------------- 4. duplicates
dup_t = {k: v for k, v in titles.items() if v > 1}
dup_d = {k: v for k, v in descs.items() if v > 1}
if dup_t:
    fail(f"{len(dup_t)} duplicate <title> values (worst x{max(dup_t.values())}): "
         f"{sorted(dup_t, key=dup_t.get, reverse=True)[:2]}")
else:
    print(f"PASS  all {len(titles)} titles unique")
if dup_d:
    fail(f"{len(dup_d)} duplicate meta descriptions (worst x{max(dup_d.values())}): "
         f"{sorted(dup_d, key=dup_d.get, reverse=True)[:2]}")
else:
    print(f"PASS  all {len(descs)} meta descriptions unique")
if long_title:
    warn(f"{long_title} titles longer than 70 characters")
if short_desc:
    warn(f"{short_desc} meta descriptions shorter than 70 characters")

# ---------------------------------------------------------------- 5. sitemaps
sm_urls = set()
sm_files = [f for f in os.listdir(DIST) if f.endswith("-sitemap.xml")]
for f in sm_files:
    txt = open(os.path.join(DIST, f), encoding="utf-8").read()
    sm_urls |= set(re.findall(r"<loc>(.*?)</loc>", txt))
should = {SITE + r["Path"] for r in arch
          if r["Indexation"] == "Index" and r["Path"] in built}
if sm_urls != should:
    fail(f"sitemap mismatch: {len(sm_urls)} in files vs {len(should)} expected "
         f"(missing {len(should - sm_urls)}, unexpected {len(sm_urls - should)})")
else:
    print(f"PASS  sitemaps contain exactly the {len(should)} indexable URLs")

noindex_in_sitemap = [u for u in sm_urls
                      if by_index.get(u.replace(SITE, "")) != "Index"]
if noindex_in_sitemap:
    fail(f"{len(noindex_in_sitemap)} noindex URLs appear in a sitemap")
else:
    print("PASS  no noindex URL appears in any sitemap")

idx = open(os.path.join(DIST, "sitemap_index.xml"), encoding="utf-8").read()
listed = set(re.findall(r"<loc>.*?/([a-z0-9\-]+\.xml)</loc>", idx))
if listed != set(sm_files):
    fail(f"sitemap_index lists {listed ^ set(sm_files)} inconsistently")
else:
    print(f"PASS  sitemap_index lists all {len(sm_files)} sitemap files")

# ---------------------------------------------------------------- 6. assets
for a in ("assets/css/site.css", "assets/fonts.css",
          "assets/brand/consultus-wordmark-dark.png",
          "assets/brand/consultus-wordmark-light.png",
          "assets/brand/consultus-mark.svg", "robots.txt"):
    if not os.path.exists(os.path.join(DIST, a)):
        fail(f"missing asset: {a}")
fonts_css = open(os.path.join(DIST, "assets", "fonts.css"), encoding="utf-8").read()
for m in re.findall(r"url\(([^)]+)\)", fonts_css):
    rel = m.strip("'\"").lstrip("/")
    if not os.path.exists(os.path.join(DIST, rel)):
        fail(f"fonts.css references a file that does not exist: {m}")
print("PASS  shared assets present and font paths resolve")

# ---------------------------------------------------------------- summary
print()
for w in warns:
    print(f"WARN  {w}")
if fails:
    for f in fails:
        print(f"FAIL  {f}")
    print(f"\n{len(fails)} check(s) failed")
    sys.exit(1)
print("All checks passed")
