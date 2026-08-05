#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Consultus Digital site generator.

Reads the architecture CSV and writes every URL in it as a real folder with an
index.html, plus XML sitemaps and robots.txt.

    python3 build.py              # build the indexable set (Phase 1 + Phase 2)
    python3 build.py --all        # build all 6,532 URLs including Phase 3
    python3 build.py --phase 1    # build a single phase
    python3 build.py --lint       # build and fail on writing-standard violations

Phase 3 pages are marked "Index after content threshold" in the source data, so
they are generated with a noindex robots tag and kept out of the sitemaps until
real content is written for them. That is deliberate: shipping several thousand
thin pages into the index is how a site earns a doorway-page penalty.
"""

import argparse
import csv
import hashlib
import json
import os
import re
import shutil
import sys
from collections import defaultdict, OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "src"))

import chrome as C                                    # noqa: E402
from content.divisions import (                       # noqa: E402
    DIVISIONS, DIVISION_ORDER, CAPABILITIES, SHARED_SOLUTIONS)
from content.services import S as SERVICES            # noqa: E402
from content.sectors import SECTORS                    # noqa: E402
from content.industries import INDUSTRY_HOOKS          # noqa: E402
from content.solutions import DIVISION_SOLUTIONS       # noqa: E402
from content.corporate import CORPORATE                # noqa: E402

DATA = os.path.join(HERE, "data", "master_url_inventory.csv")
DIST = os.path.join(HERE, "dist")
SRC_ASSETS = os.path.join(HERE, "src", "assets")

DIVS = [DIVISIONS[d] for d in DIVISION_ORDER]

# ---------------------------------------------------------------------------
# Text helpers
# ---------------------------------------------------------------------------

_IRREGULAR = {
    "Doctors and physicians": "physician practice",
    "Healthcare generally": "healthcare organisation",
    "Clinics generally": "clinic",
    "Dental groups and DSOs": "dental group",
    "Opticians and eyewear retail": "optician",
    "Pharmacies": "pharmacy",
    "Denturists": "denturist",
    "Midwifery and doulas": "midwifery practice",
    "Orthotics and prosthetics": "orthotics provider",
    "Genetics and genomic testing": "genetic testing provider",
    "PPE and first aid": "PPE brand",
    "Scrubs and medical uniforms": "medical uniform brand",
    "Lab supplies and consumables": "lab supplies brand",
    "Home accessibility and mobility fit-outs": "accessibility fit-out business",
    "Acupuncture and TCM": "acupuncture clinic",
    "Sauna and float studios": "sauna studio",
    "Pet wellness and grooming": "pet grooming business",
    "Menstrual and period care": "period care brand",
    "Oral care and whitening products": "oral care brand",
    "Sports nutrition and protein": "sports nutrition brand",
    "Probiotics and gut health": "gut health brand",
    "Herbal and botanical remedies": "herbal remedy brand",
    "Medical foods and clinical nutrition": "clinical nutrition brand",
    "Infant formula and baby nutrition": "infant nutrition brand",
    "Maternity and baby health": "maternity health brand",
    "Home diagnostics and monitors": "home diagnostics brand",
    "Respiratory devices and nebulisers": "respiratory device brand",
    "Pain relief and TENS devices": "pain relief device brand",
    "Wound care and ostomy supplies": "wound care supplier",
    "Medical ID and safety products": "medical ID brand",
    "Sterilisation and infection control": "infection control supplier",
    "Compression and recovery wear": "compression wear brand",
    "Orthopedic braces and supports": "orthopedic brace brand",
    "Orthopedic footwear and insoles": "orthopedic footwear brand",
    "Contact lens and eyewear ecommerce": "eyewear ecommerce brand",
    "Veterinary supplies and pet pharmacy": "veterinary supplies brand",
    "Clinic furniture and equipment": "clinic equipment supplier",
    "Practice management and EMR": "practice management vendor",
    "Medical billing and RCM": "medical billing company",
    "Medical coding and credentialing": "medical coding company",
    "Healthcare staffing and recruiting": "healthcare staffing firm",
    "Medical answering and reception": "medical answering service",
    "Clinical trials and research sites": "clinical research site",
    "Health insurance and benefits": "health insurance provider",
    "Disability and injury management": "disability management provider",
    "Healthcare franchises and MSOs": "healthcare franchise",
    "Practice brokerage and transitions": "practice brokerage",
    "Medical education and training": "medical education provider",
    "Health tech and clinical software": "health tech company",
    "Patient engagement platforms": "patient engagement platform",
    "Medical transport and ambulance": "medical transport service",
    "Vaccination and travel clinics": "travel clinic",
    "Plasma and blood donation centres": "donation centre",
    "Mobile clinics and health units": "mobile clinic",
    "Medical centres and multi-site groups": "medical centre",
    "Caregiver and PSW agencies": "caregiver agency",
    "Adult day and respite programs": "respite program",
    "Assisted and independent living": "assisted living community",
    "Hospice and palliative care": "hospice",
    "Memory care": "memory care community",
    "Long-term care": "long-term care home",
    "Medical alert and monitoring": "medical alert provider",
    "Family medicine and primary care": "family practice",
    "Concierge and direct primary care": "concierge practice",
    "Endocrinology and diabetes care": "endocrinology practice",
    "OB-GYN and women's health": "women's health practice",
    "Fertility and IVF": "fertility clinic",
    "Pulmonology and respirology": "respirology practice",
    "ENT and otolaryngology": "ENT practice",
    "Allergy and immunology": "allergy practice",
    "CPAP and sleep apnea clinics": "sleep apnea clinic",
    "Bariatric and weight medicine": "bariatric practice",
    "Vein and vascular clinics": "vein clinic",
    "Hand and upper limb clinics": "hand clinic",
    "Plastic and cosmetic surgery": "cosmetic surgery practice",
    "Hyperbaric oxygen therapy": "hyperbaric therapy clinic",
    "Medico-legal and IME providers": "medico-legal provider",
    "Prenatal imaging and 3D ultrasound": "prenatal imaging studio",
    "Maternal and perinatal mental health": "perinatal mental health practice",
    "Lactation and postpartum support": "lactation support practice",
    "Pediatric centres and children's clinics": "pediatric clinic",
    "Child development and assessment centres": "child assessment centre",
    "Child and youth mental health": "youth mental health service",
    "Children's vision and optometry": "pediatric optometry practice",
    "Cosmetic dentistry and veneers": "cosmetic dental practice",
    "Orthodontics and aligners": "orthodontic practice",
    "Periodontics and implants": "periodontic practice",
    "Oral and maxillofacial surgery": "oral surgery practice",
    "Sedation and emergency dentistry": "emergency dental practice",
    "Dental sleep medicine": "dental sleep practice",
    "LASIK and refractive surgery": "refractive surgery practice",
    "Vision therapy and low vision": "vision therapy practice",
    "Audiology and hearing clinics": "hearing clinic",
    "Hearing aid retail groups": "hearing aid retailer",
    "Registered massage therapy": "massage therapy clinic",
    "Kinesiology and athletic therapy": "athletic therapy clinic",
    "Dietitians and clinical nutrition": "dietitian practice",
    "Podiatry and chiropody": "podiatry practice",
    "Multidisciplinary rehab clinics": "rehab clinic",
    "Counselling and therapy practices": "therapy practice",
    "Group and multi-clinician practices": "group practice",
    "Addiction and recovery centres": "recovery centre",
    "Eating disorder programs": "eating disorder program",
    "Ketamine and TMS clinics": "TMS clinic",
    "Autism services and ABA therapy": "ABA therapy provider",
    "Behavioural health networks": "behavioural health network",
    "Employee assistance providers": "employee assistance provider",
    "Telehealth and virtual care": "telehealth provider",
    "Digital mental health apps": "digital mental health brand",
    "Injectables and botox clinics": "injectables clinic",
    "Laser and skin clinics": "laser clinic",
    "Hair restoration and transplant": "hair restoration clinic",
    "Permanent makeup and lash studios": "permanent makeup studio",
    "Medical aesthetics training": "aesthetics training provider",
    "Hormone therapy and men's health": "hormone therapy clinic",
    "Menopause and midlife care": "menopause clinic",
    "Weight loss and GLP-1 programs": "weight loss program",
    "Preventative and longevity clinics": "longevity clinic",
    "Integrative and functional medicine": "functional medicine practice",
    "Cryotherapy and recovery studios": "recovery studio",
    "Animal hospitals and emergency vet": "emergency animal hospital",
    "Veterinary specialty and referral": "veterinary referral practice",
    "Mobile and house-call vets": "mobile veterinary practice",
    "Equine and large animal vets": "equine veterinary practice",
    "Exotic and avian vets": "exotic animal practice",
    "Specialty and infusion pharmacy": "specialty pharmacy",
    "Online and DTC pharmacy": "online pharmacy",
    "Diagnostic imaging and radiology": "imaging clinic",
    "Dental and medical labs": "medical lab",
    "At-home and consumer testing": "consumer testing brand",
    "Contract research organisations": "contract research organisation",
    "Healthcare non-profits": "healthcare non-profit",
    "Healthcare consulting firms": "healthcare consulting firm",
}

_ACRONYMS = {"HVAC", "EV", "DSO", "DSOs", "CPAP", "PPE", "IVF", "ENT", "TMS", "ABA",
             "IME", "EMR", "RCM", "PSW", "TCM", "GLP-1", "DIY", "CPA", "CFO",
             "HR", "IT", "ERP", "CRM", "AI", "B2B", "SaaS", "DTC", "MSO", "MSOs",
             "SEO", "PPC", "AEO", "GEO", "LASIK", "TENS", "OB-GYN"}


def singular(name):
    """Best-effort singular noun phrase for an industry, lowercase."""
    if name in _IRREGULAR:
        return _IRREGULAR[name]
    words = name.split()
    last = words[-1]
    if last.upper() in _ACRONYMS:
        # ends in an acronym ("Dental groups and DSOs"), so leave the noun alone
        return _lower_keep(name)
    if last.endswith("ies") and len(last) > 4:
        last = last[:-3] + "y"
    elif last.endswith(("sses", "shes", "ches", "xes")):
        last = last[:-2]
    elif last.endswith("s") and not last.endswith(("ss", "us", "is")):
        last = last[:-1]
    return _lower_keep(" ".join(words[:-1] + [last]))


def _lower_keep(name):
    """Lowercase a phrase but keep acronyms and proper nouns intact."""
    out = []
    for w in name.split():
        stripped = w.strip("(),.")
        if stripped.upper() in _ACRONYMS or (stripped.isupper() and len(stripped) > 1):
            out.append(w)
        else:
            out.append(w[0].lower() + w[1:] if w[:1].isupper() and not w[1:2].isupper() else w)
    return " ".join(out)


def lower_name(name):
    return _lower_keep(name)


def pick(seed, options):
    """Deterministic variant choice so sibling pages differ but rebuilds match."""
    h = int(hashlib.md5(seed.encode("utf-8")).hexdigest()[:8], 16)
    return options[h % len(options)]


def slugify(s):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s


def esc(s):
    return C.esc(s)


cta = C.cta

# Industry names that exist in more than one division ("Healthcare consulting
# firms" sits in both Healthcare and Professional Services). Filled by
# build_index; used to keep titles and descriptions unique across divisions.
AMBIGUOUS_INDUSTRIES = set()


def mk_title(core, division=None):
    """Brand suffix where it fits, division suffix where disambiguation is needed."""
    if division:
        return f"{core} | {division}"
    full = core + " | Consultus Digital"
    return full if len(full) <= 70 else core


def title_qualifier(p):
    """Returns the division label when this industry name is not unique, else None."""
    if p.entity in AMBIGUOUS_INDUSTRIES:
        return DIVISIONS[p.division]["label"]
    return None


# ---------------------------------------------------------------------------
# Load and normalise the architecture
# ---------------------------------------------------------------------------

class Page(dict):
    __getattr__ = dict.get


def load_pages():
    rows = list(csv.DictReader(open(DATA, encoding="utf-8-sig")))
    seen = set()
    pages = []
    dropped = []
    for r in rows:
        path = r["Path"]
        if path in seen:
            # "Architecture firms" is filed under two sectors in the source data,
            # which collides 11 URLs. Keep the first (Real estate and property,
            # alongside Engineering and Surveying firms) and drop the duplicate.
            dropped.append((path, r["Group / Sector"]))
            continue
        seen.add(path)
        pages.append(Page(
            path=path,
            url=r["URL"],
            division=r["Division"],
            sector=r["Group / Sector"],
            ptype=r["Page Type"],
            entity=r["Industry / Entity"],
            service=r["Service / Solution"],
            parent=r["Parent Hub"],
            indexation=r["Indexation"],
            phase=int(r["Launch Phase"].split()[-1]),
            intent=r["Primary Intent"],
            sitemap=r["XML Sitemap"],
        ))
    return pages, dropped


def build_index(pages):
    by_path = {p.path: p for p in pages}
    children = defaultdict(list)
    for p in pages:
        if p.parent and p.parent != p.path:
            children[p.parent].append(p)
    # sectors -> industries, divisions -> sectors, industry -> services
    sectors_of = defaultdict(OrderedDict)      # division -> sector -> [industry pages]
    services_of = defaultdict(list)            # industry agency path -> [service pages]
    divs_per_industry = defaultdict(set)
    for p in pages:
        if p.ptype == "Industry Marketing Agency Page":
            sectors_of[p.division].setdefault(p.sector, []).append(p)
            divs_per_industry[p.entity].add(p.division)
        elif p.ptype == "Service × Industry Landing Page":
            services_of[p.parent].append(p)
    AMBIGUOUS_INDUSTRIES.update(
        name for name, divs in divs_per_industry.items() if len(divs) > 1)
    return by_path, children, sectors_of, services_of


# ---------------------------------------------------------------------------
# Small render helpers
# ---------------------------------------------------------------------------

def sec_head(label, title, sub="", *, on_dark=False):
    lbl_cls = "section-lbl on-dark" if on_dark else "section-lbl"
    sub_html = f'<p class="sec-sub rv" style="--d:80ms">{sub}</p>' if sub else ""
    return f"""<div class="sec-head">
  <div class="lhs"><span class="{lbl_cls} rv">{esc(label)}</span>
    <h2 class="sec-title rv" style="--d:40ms">{title}</h2></div>
  <div>{sub_html}</div>
</div>"""


def ticks(items):
    return '<ul class="ticks">' + "".join(f"<li>{esc(i)}</li>" for i in items) + "</ul>"


def chips(items):
    """items = [(label, href)]"""
    return '<div class="chips">' + "".join(
        f'<a class="chip" href="{esc(h)}">{esc(l)}</a>' for l, h in items) + "</div>"


def stat_grid(stats, *, on_dark=False):
    out = []
    for i, (num, lbl, sub) in enumerate(stats):
        out.append(f'<div class="stat rv" style="--d:{i*70}ms"><div class="stat-num">{esc(num)}</div>'
                   f'<div class="stat-lbl">{esc(lbl)}</div><div class="stat-sub">{esc(sub)}</div></div>')
    return '<div class="stats">' + "".join(out) + "</div>"


def dir_group(title, count_label, items, more=None):
    links = "".join(f'<li><a href="{esc(h)}">{esc(l)}</a></li>' for l, h in items)
    more_html = f'<a class="more" href="{esc(more[1])}">{esc(more[0])} &rarr;</a>' if more else \
                f'<span class="count">{esc(count_label)}</span>'
    return f"""<div class="dir-group rv">
  <div class="dir-head"><h3>{esc(title)}</h3>{more_html}</div>
  <ul class="dir-list">{links}</ul>
</div>"""


def steps(items):
    out = []
    for h, b in items:
        out.append(f'<div class="step rv"><div><h3>{esc(h)}</h3><p>{esc(b)}</p></div></div>')
    return '<div class="steps">' + "".join(out) + "</div>"


def rail(items):
    """items = [(kicker, title, desc, href)]"""
    out = []
    for k, t, d, h in items:
        out.append(f'<a href="{esc(h)}"><span class="k">{esc(k)}</span>'
                   f'<span class="t">{esc(t)}</span><p class="d">{esc(d)}</p></a>')
    return '<div class="rail rv">' + "".join(out) + "</div>"


def prose(paras):
    return '<div class="prose">' + "".join(f"<p>{p}</p>" for p in paras) + "</div>"


def hero(kw_h1, display, accent, sub, facts=(), *, dark=False, trail=None, buttons=True):
    disp = esc(display)
    if accent:
        disp = disp.replace(esc(accent), f'<span class="sem">{esc(accent)}</span>', 1)
    # step the display type down as the line gets longer, so every hero fits a screen
    n = len(display)
    size_cls = " xlong" if n > 96 else (" long" if n > 52 else "")
    facts_html = ""
    if facts:
        facts_html = '<div class="hero-facts rv" style="--d:220ms">' + "".join(
            f'<span class="hero-fact">{esc(f)}</span>' for f in facts) + "</div>"
    btns = ""
    if buttons:
        btns = ('<div class="btn-row rv" style="--d:280ms">'
                '<a class="btn primary%s" href="/book-a-strategy-call/">Book a strategy call <span class="arr">&rarr;</span></a>'
                '<a class="btn secondary%s" href="/work/">See the case studies</a></div>'
                % ((" on-dark", " on-dark") if dark else ("", "")))
    crumb_html = ""
    if trail:
        crumb_html = f'<div class="hero-crumbs">{C.crumbs(trail, on_dark=dark)}</div>'
    return f"""<div class="hero-frame">
<section class="hero {'dark' if dark else 'light'}">
  <div class="hero-in">
    {crumb_html}
    <h1 class="hero-kw rv">{esc(kw_h1)}</h1>
    <p class="hero-display{size_cls} rv" style="--d:60ms">{disp}</p>
    <p class="hero-sub rv" style="--d:140ms">{esc(sub)}</p>
    {facts_html}
    {btns}
  </div>
</section>
</div>"""


def page_shell(title, desc, path, body, *, noindex=False, jsonld=None, tag=None):
    return (C.head(title, desc, path, noindex=noindex, jsonld=jsonld)
            + C.nav(DIVS, CAPABILITIES, SHARED_SOLUTIONS, tag=tag)
            + f'<main id="main">{body}</main>'
            + C.footer(DIVS, CAPABILITIES, SHARED_SOLUTIONS))


# ---------------------------------------------------------------------------
# Trail building
# ---------------------------------------------------------------------------

def trail_for(p, by_path):
    trail = []
    node = p
    guard = 0
    while node is not None and guard < 8:
        guard += 1
        trail.append((label_for(node), node.path))
        parent_path = node.parent
        if not parent_path or parent_path == node.path:
            break
        node = by_path.get(parent_path)
    trail.append(("Home", "/"))
    trail.reverse()
    # de-duplicate consecutive
    out = []
    for item in trail:
        if not out or out[-1][0] != item[0]:
            out.append(item)
    return out


def label_for(p):
    t = p.ptype
    if t == "Homepage":
        return "Home"
    if t == "Division Marketing Agency Hub":
        return DIVISIONS[p.division]["label"]
    if t == "Industry Directory":
        return "Industries"
    if t == "Division Service Hub":
        return "Services"
    if t == "Division Solution Hub":
        return "Solutions"
    if t == "Division Case Study Hub":
        return "Case studies"
    if t == "Division Insight Hub":
        return "Insights"
    if t == "Division Lead Strategist":
        return "Lead strategist"
    if t == "Division Assessment":
        return "Growth assessment"
    if t == "Sector Hub":
        return p.sector or p.entity
    if t == "Industry Marketing Agency Page":
        return p.entity
    if t == "Service × Industry Landing Page":
        svc = SERVICES.get((p.division, service_slug(p)), {})
        return svc.get("name", p.service)
    if t in ("Shared Capability", "Shared Solution", "Division Solution"):
        return p.entity
    return CORPORATE.get(p.path, {}).get("nav_label", p.entity or "Page")


def service_slug(p):
    seg = p.path.strip("/").split("/")[-1]
    return seg.split("-for-")[0]


SERVICE_TO_CAPABILITY = {
    "digital-marketing": "paid-media", "performance-marketing": "paid-media",
    "paid-search": "paid-media", "google-ads": "paid-media",
    "paid-search-shopping": "paid-media", "paid-social": "paid-media",
    "seo": "seo-ai-search", "local-seo": "seo-ai-search", "ai-search": "seo-ai-search",
    "web-design": "websites-cro", "shopify-cro": "websites-cro",
    "crm-revops": "crm-automation", "email-sms": "crm-automation",
    "content-marketing": "content-authority", "thought-leadership": "content-authority",
    "ad-creative": "performance-creative", "performance-creative": "performance-creative",
    "analytics": "analytics-intelligence", "call-tracking": "analytics-intelligence",
    "ecommerce-growth": "paid-media", "marketplace-marketing": "paid-media",
}
CAP_BY_SLUG = {c["slug"]: c for c in CAPABILITIES}
SOL_BY_SLUG = {s[0]: s for s in SHARED_SOLUTIONS}


def div_proof_stats(d):
    p = d["proof"]
    out = [(p["stat"], p["stat_label"], p["stat_sub"])]
    out.extend(p["support"])
    return out


def division_of(p):
    return DIVISIONS.get(p.division)


# ---------------------------------------------------------------------------
# CORPORATE TEMPLATES
# ---------------------------------------------------------------------------

def r_homepage(p, ix):
    c = CORPORATE["/"]
    by_path, children, sectors_of, services_of = ix
    div_cards = ""
    for d in DIVS:
        pr = d["proof"]
        div_cards += f"""<a class="card rv" href="/{d['root']}/">
          <span class="num">{esc(d['unit'])}</span>
          <h3>{esc(d['label'])}</h3>
          <p>{esc(d['nav_blurb'])}</p>
          <ul class="ticks"><li>{esc(pr['stat'])} {esc(pr['stat_label'])}, {esc(pr['client'])}</li></ul>
        </a>"""
    cap_items = [(c2["name"], f"/capabilities/{c2['slug']}/") for c2 in CAPABILITIES]
    sol_items = [(s[1], f"/growth-solutions/{s[0]}/") for s in SHARED_SOLUTIONS]

    body = f"""
{hero(c['kw'], c['display'], c['accent'], c['sub'], c['facts'])}

<section class="sec thesis dark-full"><div class="sec-inner">
  <p class="rv">{esc(c['thesis'])}</p>
</div></section>

<section class="sec">
  {sec_head("Divisions", "Four practices, four different definitions of a good month.",
            "A booked appointment, a booked job, a signed matter and a blended efficiency ratio. "
            "The channels overlap. Almost nothing else does.")}
  <div class="grid g4">{div_cards}</div>
</section>

<section class="sec bone-full"><div class="sec-inner">
  {sec_head("Capabilities", "Seven disciplines, applied to whichever outcome the division is judged on.",
            "These are the parts the programs are built from. Which ones lead depends entirely on "
            "the business and what is currently constraining it.")}
  <div class="grid g4">{''.join(
      f'<a class="card rv" style="--d:{i*40}ms" href="/capabilities/{c2["slug"]}/"><h3>{esc(c2["name"])}</h3><p>{esc(c2["blurb"])}</p></a>'
      for i, c2 in enumerate(CAPABILITIES))}</div>
</div></section>

<section class="sec dark-full"><div class="sec-inner">
  {sec_head("Proof", "Numbers our clients approved for publication.",
            "Every figure below came from a client account or a client report and is attributed "
            "to the named engagement. Where a result is not published, the case study says so.",
            on_dark=True)}
  {stat_grid([(DIVISIONS['Healthcare']['proof']['stat'], 'leads in month one', 'La Vie Executive Health'),
              (DIVISIONS['DTC']['proof']['stat'], 'marketing efficiency ratio', 'Dragonscale Supplies'),
              (DIVISIONS['Professional Services']['proof']['stat'], 'cost per lead on Meta', 'Zayouna Law Firm'),
              (DIVISIONS['Trades']['proof']['stat'], 'cost per lead', "Gordon's Downsizing")], on_dark=True)}
  <div class="mt40"><a class="btn primary on-dark" href="/work/">Read the case studies <span class="arr">&rarr;</span></a></div>
</div></section>

<section class="sec">
  {sec_head("Solutions", "Start from the situation, not the channel.",
            "Most agency conversations open with a channel. These open with what is actually "
            "going wrong, which often points somewhere else entirely.")}
  {chips(sol_items)}
</section>

{cta("Tell us what is not working.", "Thirty minutes, a review of what you are running now, and a straight answer on what to change first.", accent="not working")}
"""
    jl = [C.org_jsonld(), C.crumb_jsonld([("Home", "/")])]
    return page_shell(c["title"], c["desc"], "/", body, jsonld=jl)


def r_divisions_hub(p, ix):
    c = CORPORATE["/divisions/"]
    trail = [("Home", "/"), ("Divisions", "/divisions/")]
    cards = ""
    for d in DIVS:
        pr = d["proof"]
        cards += f"""<div class="svc-block rv">
          <div><span class="idx">{esc(d['unit'])}</span>
            <h3>{esc(d['label'])}</h3>
            <div class="prose"><p>{esc(d['lede'])}</p></div>
            <div class="btn-row mt24">
              <a class="btn secondary" href="/{d['root']}/">{esc(d['label'])} practice <span class="arr">&rarr;</span></a>
              <a class="btn secondary" href="{esc(d['industries_hub'])}">Industries</a>
            </div>
          </div>
          <div>
            <p class="lede">{esc(d['thesis'])}</p>
            {ticks([f"Measured on {d['unit']}", f"Buyers: {d['buyer']}", f"{pr['stat']} {pr['stat_label']} for {pr['client']}"])}
          </div>
        </div>"""
    body = f"""
{hero(c['kw'], c['display'], c['accent'], c['sub'], trail=trail)}
<section class="sec">
  <div class="prose rv" style="max-width:70ch">{''.join(f'<p>{esc(x)}</p>' for x in c['body'])}</div>
</section>
<section class="sec bone-full"><div class="sec-inner">{cards}</div></section>
{cta("Which practice fits your business?", "If you are not sure, describe the situation and we will point you at the right one, including when that is not us.", accent="fits your business?")}
"""
    jl = [C.crumb_jsonld(trail)]
    return page_shell(c["title"], c["desc"], p.path, body, jsonld=jl)


def r_capability_hub(p, ix):
    c = CORPORATE["/capabilities/"]
    trail = [("Home", "/"), ("Capabilities", "/capabilities/")]
    blocks = ""
    for i, cap in enumerate(CAPABILITIES):
        blocks += f"""<div class="svc-block rv">
          <div><span class="idx">0{i+1}</span><h3>{esc(cap['name'])}</h3>
            <div class="prose"><p>{esc(cap['lede'])}</p></div>
            <a class="btn secondary mt24" href="/capabilities/{cap['slug']}/">{esc(cap['name'])} <span class="arr">&rarr;</span></a>
          </div>
          <div>{ticks(cap['deliverables'][:4])}</div>
        </div>"""
    body = f"""
{hero(c['kw'], c['display'], c['accent'], c['sub'], trail=trail)}
<section class="sec">{blocks}</section>
{cta("Not sure which capability you need?", "Most businesses come asking for one channel and leave with a different first move. The call is free either way.", accent="which capability")}
"""
    return page_shell(c["title"], c["desc"], p.path, body, jsonld=[C.crumb_jsonld(trail)])


def r_solution_hub(p, ix):
    c = CORPORATE["/growth-solutions/"]
    trail = [("Home", "/"), ("Growth solutions", "/growth-solutions/")]
    cards = "".join(
        f'<a class="card rv" style="--d:{i*40}ms" href="/growth-solutions/{s[0]}/">'
        f'<h3>{esc(s[1])}</h3><p>{esc(s[2])}</p></a>'
        for i, s in enumerate(SHARED_SOLUTIONS))
    body = f"""
{hero(c['kw'], c['display'], c['accent'], c['sub'], trail=trail)}
<section class="sec"><div class="grid g3">{cards}</div></section>
<section class="sec bone-full"><div class="sec-inner">
  {sec_head("By division", "The same outcomes, framed for your industry.",
            "Each practice has its own version of these, with the metric and constraints that apply there.")}
  <div class="grid g4">{''.join(
      f'<a class="card rv" href="/{d["root"]}/solutions/"><h3>{esc(d["label"])}</h3>'
      f'<p>{esc(d["nav_blurb"])}</p></a>' for d in DIVS)}</div>
</div></section>
{cta("Start from the problem.", "Describe what is going wrong and we will tell you which of these it actually is.", accent="the problem")}
"""
    return page_shell(c["title"], c["desc"], p.path, body, jsonld=[C.crumb_jsonld(trail)])


def r_work_hub(p, ix):
    c = CORPORATE["/work/"]
    trail = [("Home", "/"), ("Work", "/work/")]
    cases = [
        ("La Vie Executive Health", "Healthcare", "512 leads in month one",
         "Executive health program launched across paid, organic and LinkedIn in nine weeks."),
        ("Dragonscale Supplies", "DTC", "13.23 marketing efficiency ratio",
         "A niche ecommerce brand managed to blended efficiency rather than platform ROAS."),
        ("Zayouna Law Firm", "Professional Services", "$72.70 cost per lead on Meta",
         "Personal injury acquisition rebuilt around signed files rather than enquiry volume."),
        ("Gordon's Downsizing", "Trades", "$164 cost per lead",
         "A 1958 family firm repositioned, 53 leads from a standing start."),
        ("BookSeats", "DTC", "8.10x return on ad spend",
         "Creator-led video against static, with a 248 percent higher click-through rate."),
        ("Eco Choice Windows", "Trades", "Program build",
         "Personas, creative, landing pages and CRM built as one system."),
    ]
    cards = "".join(
        f'<div class="card rv" style="--d:{i*40}ms"><span class="num">{esc(k)}</span>'
        f'<h3>{esc(n)}</h3><p>{esc(d)}</p>'
        f'<ul class="ticks"><li>{esc(s)}</li></ul></div>'
        for i, (n, k, s, d) in enumerate(cases))
    body = f"""
{hero(c['kw'], c['display'], c['accent'], c['sub'], trail=trail)}
<section class="sec"><div class="grid g3">{cards}</div>
  <p class="sec-sub mt40 rv">Case study pages for these engagements are published on the main
  Consultus Digital site. Figures shown here are the client-approved numbers.</p>
</section>
<section class="sec bone-full"><div class="sec-inner">
  {sec_head("By division", "Case studies grouped by practice.", "")}
  <div class="grid g4">{''.join(
      f'<a class="card rv" href="/{d["root"]}/case-studies/"><h3>{esc(d["label"])}</h3>'
      f'<p>{esc(d["nav_blurb"])}</p></a>' for d in DIVS)}</div>
</div></section>
{cta("Want numbers like these explained?", "We will walk through what produced them and whether the same approach applies to your business.", accent="explained?")}
"""
    return page_shell(c["title"], c["desc"], p.path, body, jsonld=[C.crumb_jsonld(trail)])


def r_insight_hub(p, ix):
    c = CORPORATE["/insights/"]
    trail = [("Home", "/"), ("Insights", "/insights/")]
    body = f"""
{hero(c['kw'], c['display'], c['accent'], c['sub'], trail=trail)}
<section class="sec">
  {sec_head("Insights", "Published when there is something worth saying.",
            "Articles are being migrated into this architecture. In the meantime, the division "
            "insight hubs below carry the writing relevant to each practice.")}
  <div class="grid g4">{''.join(
      f'<a class="card rv" href="/{d["root"]}/insights/"><h3>{esc(d["label"])}</h3>'
      f'<p>{esc(d["nav_blurb"])}</p></a>' for d in DIVS)}</div>
</section>
{cta("Rather just ask?", "A strategy call answers more than an article will, and it is specific to your account.", accent="just ask?")}
"""
    return page_shell(c["title"], c["desc"], p.path, body, jsonld=[C.crumb_jsonld(trail)])


def r_expert_hub(p, ix):
    c = CORPORATE["/experts/"]
    trail = [("Home", "/"), ("Experts", "/experts/")]
    body = f"""
{hero(c['kw'], c['display'], c['accent'], c['sub'], trail=trail)}
<section class="sec">
  {sec_head("Practice leads", "Each division has a named lead strategist.",
            "The person who sets the plan is the person you meet on the strategy call and the "
            "person accountable for the number afterwards.")}
  <div class="grid g4">{''.join(
      f'<a class="card rv" href="/{d["root"]}/lead-strategist/"><span class="num">{esc(d["unit"])}</span>'
      f'<h3>{esc(d["label"])} lead</h3><p>{esc(d["nav_blurb"])}</p></a>' for d in DIVS)}</div>
</section>
{cta("Meet the person who would run it.", "Strategy calls are taken by the practice lead, not by a salesperson.", accent="run it")}
"""
    return page_shell(c["title"], c["desc"], p.path, body, jsonld=[C.crumb_jsonld(trail)])


def r_about(p, ix):
    c = CORPORATE["/about/"]
    trail = [("Home", "/"), ("About", "/about/")]
    princ = "".join(
        f'<div class="card rv" style="--d:{i*50}ms"><span class="num">0{i+1}</span>'
        f'<h3>{esc(t)}</h3><p>{esc(b)}</p></div>'
        for i, (t, b) in enumerate(c["principles"]))
    body = f"""
{hero(c['kw'], c['display'], c['accent'], c['sub'], trail=trail)}
<section class="sec"><div class="prose rv" style="max-width:70ch">
  {''.join(f'<p>{esc(x)}</p>' for x in c['body'])}
</div></section>
<section class="sec bone-full"><div class="sec-inner">
  {sec_head("How we work", "Four things we hold to, including the ones that cost us revenue.", "")}
  <div class="grid g4">{princ}</div>
</div></section>
<section class="sec dark-full"><div class="sec-inner">
  {sec_head("The practices", "Four divisions, four metrics.", "", on_dark=True)}
  <div class="grid g4">{''.join(
      f'<a class="card rv" href="/{d["root"]}/"><span class="num">{esc(d["unit"])}</span>'
      f'<h3>{esc(d["label"])}</h3><p>{esc(d["nav_blurb"])}</p></a>' for d in DIVS)}</div>
</div></section>
{cta("Work with us, or do not.", "The strategy call includes the cases where the honest answer is that you do not need an agency yet.", accent="or do not")}
"""
    return page_shell(c["title"], c["desc"], p.path, body, jsonld=[C.org_jsonld(), C.crumb_jsonld(trail)])


def r_contact(p, ix):
    c = CORPORATE["/contact/"]
    trail = [("Home", "/"), ("Contact", "/contact/")]
    body = f"""
{hero(c['kw'], c['display'], c['accent'], c['sub'], trail=trail)}
<section class="sec">
  <div class="sec-head">
    <div class="lhs"><span class="section-lbl rv">Get in touch</span>
      <h2 class="sec-title rv">What to include so the first reply is useful.</h2></div>
    <div>{ticks([
      "What you sell and roughly what a customer is worth",
      "What you are running now and what it costs per month",
      "The number you are currently judging it on",
      "What made you start looking for help",
    ])}</div>
  </div>
  <div class="rail rv">
    <a href="/book-a-strategy-call/"><span class="k">Fastest</span><span class="t">Book a strategy call</span>
      <p class="d">Thirty minutes with the practice lead for your industry.</p></a>
    <a href="/divisions/"><span class="k">Not sure who to ask</span><span class="t">Find your division</span>
      <p class="d">Four practices, each with its own lead strategist.</p></a>
    <a href="/work/"><span class="k">Due diligence</span><span class="t">Read the case studies</span>
      <p class="d">Named clients, approved numbers and stated constraints.</p></a>
  </div>
</section>
{cta("Toronto based, working across North America.", "Send the situation rather than a brief. It gets you a more useful first answer.", accent="Toronto based")}
"""
    return page_shell(c["title"], c["desc"], p.path, body, jsonld=[C.org_jsonld(), C.crumb_jsonld(trail)])


def r_conversion(p, ix):
    c = CORPORATE["/book-a-strategy-call/"]
    trail = [("Home", "/"), ("Book a strategy call", p.path)]
    agenda = steps(c["agenda"])
    body = f"""
{hero(c['kw'], c['display'], c['accent'], c['sub'], trail=trail)}
<section class="sec">
  {sec_head("The call", "What the thirty minutes actually covers.",
            "It is a working session rather than a pitch. You will get the recommendation whether "
            "or not it involves hiring us.")}
  {agenda}
</section>
<section class="sec bone-full"><div class="sec-inner">
  {sec_head("Before you book", "Two things worth knowing.", "")}
  <div class="grid g2">
    <div class="card rv"><h3>You will meet the practice lead</h3>
      <p>The call is taken by the strategist who would run the account, not by a salesperson
      who hands you over afterwards.</p></div>
    <div class="card rv" style="--d:60ms"><h3>Sometimes the answer is no</h3>
      <p>If you are at capacity, if the unit economics do not support paid acquisition, or if the
      constraint is operational, we will say so on the call.</p></div>
  </div>
</div></section>
{cta("Book the call.", "Thirty minutes with the lead strategist for your industry.", accent="Book the call.",
     secondary=("See how the divisions work", "/divisions/"))}
"""
    return page_shell(c["title"], c["desc"], p.path, body, noindex=False, jsonld=[C.crumb_jsonld(trail)])


# ---------------------------------------------------------------------------
# SHARED CAPABILITY / SOLUTION
# ---------------------------------------------------------------------------

def r_shared_capability(p, ix):
    cap = CAP_BY_SLUG[p.path.strip("/").split("/")[-1]]
    trail = [("Home", "/"), ("Capabilities", "/capabilities/"), (cap["name"], p.path)]
    others = [(c2["name"], f"/capabilities/{c2['slug']}/") for c2 in CAPABILITIES if c2["slug"] != cap["slug"]]
    title = mk_title(f"{cap['name']}")
    desc = f"{cap['blurb']} Delivered across healthcare, trades, DTC and professional services."
    body = f"""
{hero(f"{cap['name']} Agency", cap['lede'], None, cap['blurb'], trail=trail)}
<section class="sec">
  <div class="sec-head">
    <div class="lhs"><span class="section-lbl rv">How it works</span>
      <h2 class="sec-title rv">{esc(cap['name'])}, in practice.</h2></div>
    <div class="prose rv">{''.join(f'<p>{esc(x)}</p>' for x in cap['body'])}</div>
  </div>
  <div class="grid g2">
    <div class="card rv"><h3>What ships</h3>{ticks(cap['deliverables'])}</div>
    <div class="card rv" style="--d:60ms"><h3>Where we would push back</h3>
      <p>{esc(cap['judgment'])}</p></div>
  </div>
</section>
<section class="sec bone-full"><div class="sec-inner">
  {sec_head("By division", "The same capability, four different jobs.",
            "What good looks like changes completely depending on the outcome the practice is measured on.")}
  <div class="grid g4">{''.join(
      f'<a class="card rv" href="/{d["root"]}/"><span class="num">{esc(d["unit"])}</span>'
      f'<h3>{esc(d["label"])}</h3><p>{esc(d["nav_blurb"])}</p></a>' for d in DIVS)}</div>
</div></section>
<section class="sec">
  {sec_head("Other capabilities", "Rarely bought alone.", "")}
  {chips(others)}
</section>
{cta(f"Is {lower_name(cap['name'])} your constraint?", "Often it is not. The strategy call starts with what is actually limiting growth rather than what you came to buy.", accent=lower_name(cap['name']))}
"""
    jl = [C.crumb_jsonld(trail), C.service_jsonld(cap["name"], cap["blurb"], p.path)]
    return page_shell(title, desc, p.path, body, jsonld=jl)


def r_shared_solution(p, ix):
    slug = p.path.strip("/").split("/")[-1]
    s = SOL_BY_SLUG[slug]
    name, blurb, context = s[1], s[2], s[3]
    trail = [("Home", "/"), ("Growth solutions", "/growth-solutions/"), (name, p.path)]
    div_versions = []
    for d in DIVS:
        for (dv, ds), sol in DIVISION_SOLUTIONS.items():
            if dv == d["label"] and (slug in ds or ds in slug):
                div_versions.append((d["label"], f"/{d['root']}/solutions/{ds}/"))
                break
    others = [(x[1], f"/growth-solutions/{x[0]}/") for x in SHARED_SOLUTIONS if x[0] != slug]
    body = f"""
{hero(name, blurb, None, context, trail=trail)}
<section class="sec">
  <div class="sec-head">
    <div class="lhs"><span class="section-lbl rv">The situation</span>
      <h2 class="sec-title rv">{esc(blurb)}</h2></div>
    <div class="prose rv"><p>{esc(context)}</p>
      <p>How this gets solved depends on the industry. Each practice has its own version of
      this work, with the metric and the constraints that apply there.</p></div>
  </div>
  {rail([("By practice", d["label"], d["nav_blurb"], f"/{d['root']}/solutions/") for d in DIVS[:3]])}
</section>
<section class="sec bone-full"><div class="sec-inner">
  {sec_head("Related solutions", "Problems that usually arrive together.", "")}
  {chips(others)}
</div></section>
{cta(f"Is {lower_name(name)} the actual problem?", "Sometimes the presenting problem is a symptom of a different one. The call sorts that out first.", accent=lower_name(name))}
"""
    jl = [C.crumb_jsonld(trail), C.service_jsonld(name, blurb, p.path)]
    return page_shell(f"{name} | Consultus Digital", blurb, p.path, body, jsonld=jl)


# ---------------------------------------------------------------------------
# DIVISION-LEVEL TEMPLATES
# ---------------------------------------------------------------------------

def division_services(division):
    return [(slug, mod) for (dv, slug), mod in SERVICES.items() if dv == division]


def r_division_hub(p, ix):
    by_path, children, sectors_of, services_of = ix
    d = division_of(p)
    trail = [("Home", "/"), ("Divisions", "/divisions/"), (d["label"], p.path)]
    svcs = division_services(p.division)
    sectors = sectors_of[p.division]
    sols = [(k[1], v) for k, v in DIVISION_SOLUTIONS.items() if k[0] == p.division]

    svc_blocks = ""
    for i, (slug, mod) in enumerate(svcs):
        svc_blocks += f"""<div class="svc-block rv">
          <div><span class="idx">0{i+1}</span><h3>{esc(mod['name'])}</h3>
            <div class="prose"><p>{esc(mod['intro'][0])}</p></div>
            <p class="mt16" style="font-family:var(--mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--charcoal)">
              Measured on {esc(mod['metric'])}</p>
          </div>
          <div>{ticks(mod['deliverables'][:4])}</div>
        </div>"""

    sector_items = [(s, f"/{d['industries_root']}/{slugify(s)}/") for s in sectors]
    title = mk_title(f"{d['label']} Marketing Agency")
    desc = f"{d['label']} marketing agency. {d['lede']}"
    pr = d["proof"]

    body = f"""
{hero(d['hero_kw'], d['display'], d['display_accent'], d['lede'],
      [f"Measured on {d['unit']}", f"{len(sectors)} sectors", f"{sum(len(v) for v in sectors.values())} industries"],
      trail=trail)}

<section class="sec thesis dark-full"><div class="sec-inner"><p class="rv">{esc(d['thesis'])}</p></div></section>

<section class="sec">
  {sec_head("The problem", "What usually brings a business here.",
            esc(d['judgment']))}
  <div class="grid g2">
    <div class="card rv"><h3>Signals we hear on the first call</h3>{ticks(d['signals'])}</div>
    <div class="card rv" style="--d:60ms"><h3>When this is not the right purchase</h3>
      <p>{esc(d['not_for'])}</p></div>
  </div>
</section>

<section class="sec bone-full"><div class="sec-inner">
  {sec_head("Services", f"Ten services, all measured on {d['unit']}.",
            "The mix depends on where the business currently loses money. It is rarely all ten.")}
  {svc_blocks}
  <div class="mt40"><a class="btn primary" href="/{d['services_root']}/">All {d['low']} services <span class="arr">&rarr;</span></a></div>
</div></section>

<section class="sec dark-full"><div class="sec-inner">
  {sec_head("Proof", f"{pr['client']}.", "Client-approved figures from the engagement.", on_dark=True)}
  {stat_grid(div_proof_stats(d), on_dark=True)}
  <div class="mt40"><a class="btn primary on-dark" href="/{d['root']}/case-studies/">
    {esc(d['label'])} case studies <span class="arr">&rarr;</span></a></div>
</div></section>

<section class="sec">
  {sec_head("Industries", f"{sum(len(v) for v in sectors.values())} industries across {len(sectors)} sectors.",
            "Each has its own page covering how acquisition actually works there.")}
  {chips(sector_items)}
  <div class="mt40"><a class="btn secondary" href="{esc(d['industries_hub'])}">Full industry directory <span class="arr">&rarr;</span></a></div>
</section>

<section class="sec bone-full"><div class="sec-inner">
  {sec_head("Solutions", "Start from the outcome.", "")}
  {chips([(v['name'], f"/{d['root']}/solutions/{k}/") for k, v in sols])}
</div></section>

<section class="sec">
  {sec_head("Rules of the category", "What constrains the work here.", "")}
  <div class="grid g2">
    <div class="card rv"><h3>Regulatory reality</h3><p>{esc(d['regulatory'])}</p></div>
    <div class="card rv" style="--d:60ms"><h3>Who decides</h3>
      <p>Programs here are bought by {esc(d['buyer'])}, and judged on {esc(d['unit'])}.</p>
      {ticks(d['units'])}</div>
  </div>
</section>

{rail_section(d)}
{cta(f"Book a {d['low']} strategy call.", f"Thirty minutes with the {d['low']} lead strategist and a straight answer on what to change first.", accent="strategy call", secondary=("Take the growth assessment", f"/{d['root']}/growth-assessment/"))}
"""
    jl = [C.crumb_jsonld(trail),
          C.service_jsonld(f"{d['label']} Marketing", d["lede"], p.path, area=d["label"])]
    return page_shell(title, desc, p.path, body, jsonld=jl, tag=d["label"])


def rail_section(d):
    return f"""<section class="sec tight">
  {rail([
    ("Next step", "Growth assessment", f"A structured review of the {d['low']} program you run today.", f"/{d['root']}/growth-assessment/"),
    ("The team", "Lead strategist", "The person who would set the plan and own the number.", f"/{d['root']}/lead-strategist/"),
    ("Reading", f"{d['label']} insights", "Practitioner writing from inside these accounts.", f"/{d['root']}/insights/"),
  ])}
</section>"""


def r_industry_directory(p, ix):
    by_path, children, sectors_of, services_of = ix
    d = division_of(p)
    trail = [("Home", "/"), ("Divisions", "/divisions/"), (d["label"], f"/{d['root']}/"), ("Industries", p.path)]
    sectors = sectors_of[p.division]
    total = sum(len(v) for v in sectors.values())
    groups = ""
    for sname, inds in sectors.items():
        prof = SECTORS.get(sname, {})
        items = [(i.entity, i.path) for i in sorted(inds, key=lambda x: x.entity)]
        groups += dir_group(sname, f"{len(items)} industries", items,
                            more=("Sector overview", f"/{d['industries_root']}/{slugify(sname)}/"))
    title = mk_title(f"{d['label']} Industries We Serve")
    desc = f"{total} {d['low']} industries across {len(sectors)} sectors, each with its own acquisition page."
    body = f"""
{hero(f"{d['label']} Marketing Agency Industries",
      f"{total} industries. Each one buys differently.",
      "Each one buys differently",
      f"The full {d['low']} directory, grouped into {len(sectors)} sectors. "
      f"Every industry has its own page covering how acquisition works there, what it is measured on and where it goes wrong.",
      trail=trail)}
<section class="sec">{groups}</section>
{cta("Cannot find yours?", "The list covers the industries we have run programs in. If yours is adjacent, the call will tell you whether the playbook transfers.", accent="Cannot find yours?", secondary=(f"{d['label']} practice", f"/{d['root']}/"))}
"""
    return page_shell(title, desc, p.path, body, jsonld=[C.crumb_jsonld(trail)], tag=d["label"])


def r_division_service_hub(p, ix):
    by_path, children, sectors_of, services_of = ix
    d = division_of(p)
    trail = [("Home", "/"), ("Divisions", "/divisions/"), (d["label"], f"/{d['root']}/"), ("Services", p.path)]
    svcs = division_services(p.division)
    blocks = ""
    for i, (slug, mod) in enumerate(svcs):
        cap = CAP_BY_SLUG.get(SERVICE_TO_CAPABILITY.get(slug, "paid-media"))
        blocks += f"""<div class="svc-block rv">
          <div><span class="idx">0{i+1} &middot; {esc(mod['metric'])}</span>
            <h3>{esc(mod['name'])}</h3>
            <div class="prose"><p>{esc(mod['intro'][0])}</p><p>{esc(mod['intro'][1])}</p></div>
            <div class="btn-row mt24">
              <a class="btn secondary" href="/capabilities/{cap['slug']}/">{esc(cap['name'])} capability</a>
            </div>
          </div>
          <div>{ticks(mod['deliverables'])}
            <div class="card mt24" style="background:var(--bone)"><h3>Where this stops working</h3>
              <p>{esc(mod['warning'])}</p></div>
          </div>
        </div>"""
    title = mk_title(f"{d['label']} Marketing Services")
    desc = (f"Ten {d['low']} marketing services from Consultus Digital, all measured on "
            f"{d['unit']} rather than impressions.")
    body = f"""
{hero(f"{d['label']} Marketing Services",
      f"Ten services. One number: {d['unit']}.", d['unit'],
      f"Every service below is judged on whether it moved {d['unit']}. "
      f"Which ones lead depends on where the business is currently losing money.",
      trail=trail)}
<section class="sec">{blocks}</section>
<section class="sec bone-full"><div class="sec-inner">
  {sec_head("By industry", "Every service, applied to a specific industry.",
            "The service pages below go industry by industry, because a paid search account for a "
            "hospital and one for a med spa share a platform and very little else.")}
  <div class="mt24"><a class="btn primary" href="{esc(d['industries_hub'])}">Browse industries <span class="arr">&rarr;</span></a></div>
</div></section>
{cta("Which of these do you actually need?", "Usually two or three, not ten. The strategy call narrows it before anyone quotes.", accent="actually need?")}
"""
    return page_shell(title, desc, p.path, body, jsonld=[C.crumb_jsonld(trail)], tag=d["label"])


def r_division_solution_hub(p, ix):
    d = division_of(p)
    trail = [("Home", "/"), ("Divisions", "/divisions/"), (d["label"], f"/{d['root']}/"), ("Solutions", p.path)]
    sols = [(k[1], v) for k, v in DIVISION_SOLUTIONS.items() if k[0] == p.division]
    cards = "".join(
        f'<a class="card rv" style="--d:{i*40}ms" href="/{d["root"]}/solutions/{slug}/">'
        f'<span class="num">{esc(v["measure"][:44])}</span><h3>{esc(v["name"])}</h3>'
        f'<p>{esc(v["problem"])}</p></a>'
        for i, (slug, v) in enumerate(sols))
    title = mk_title(f"{d['label']} Growth Solutions")
    desc = (f"Ten {d['low']} growth solutions from Consultus Digital, organised by the outcome "
            f"rather than the channel, and measured on {d['unit']}.")
    body = f"""
{hero(f"{d['label']} Growth Solutions", "Start from what is going wrong.", "what is going wrong",
      f"Ten situations {d['buyer']} bring us, and what we would actually do about each one.",
      trail=trail)}
<section class="sec"><div class="grid g3">{cards}</div></section>
<section class="sec bone-full"><div class="sec-inner">
  {sec_head("Across every division", "The same outcomes, framed for other industries.", "")}
  {chips([(s[1], f"/growth-solutions/{s[0]}/") for s in SHARED_SOLUTIONS])}
</div></section>
{cta("Not sure which one you have?", "Describe the situation. Often the presenting problem is a symptom of a different one.", accent="which one you have?")}
"""
    return page_shell(title, desc, p.path, body, jsonld=[C.crumb_jsonld(trail)], tag=d["label"])


def r_division_solution(p, ix):
    d = division_of(p)
    slug = p.path.strip("/").split("/")[-1]
    sol = DIVISION_SOLUTIONS[(p.division, slug)]
    trail = [("Home", "/"), ("Divisions", "/divisions/"), (d["label"], f"/{d['root']}/"),
             ("Solutions", f"/{d['root']}/solutions/"), (sol["name"], p.path)]
    approach = steps([(t, b) for t, b in sol["approach"]])
    others = [(v["name"], f"/{d['root']}/solutions/{k[1]}/")
              for k, v in DIVISION_SOLUTIONS.items() if k[0] == p.division and k[1] != slug]
    title = mk_title(f"{sol['name']} for {d['label']}")
    desc = f"{sol['lede']} {sol['problem']} Measured on {sol['measure']}."
    body = f"""
{hero(f"{d['label']} {sol['name']}", sol['problem'], None, sol['lede'], trail=trail)}
<section class="sec">
  {sec_head("What we do", "Three moves, in this order.", esc(sol['lede']))}
  {approach}
</section>
<section class="sec bone-full"><div class="sec-inner">
  <div class="grid g2">
    <div class="card rv"><h3>How we know it worked</h3><p>{esc(sol['measure'])}</p>
      <p class="mt16" style="font-size:14px;color:var(--charcoal)">Reported monthly against the
      baseline agreed before launch.</p></div>
    <div class="card rv" style="--d:60ms"><h3>When this is the wrong purchase</h3>
      <p>{esc(sol['caveat'])}</p></div>
  </div>
</div></section>
<section class="sec">
  {sec_head("Related", f"Other {d['low']} solutions.", "")}
  {chips(others)}
</section>
{cta(f"Is this your situation?", "If it is, the call goes straight to what we would change first. If it is not, we will say which one it actually is.", accent="your situation?")}
"""
    jl = [C.crumb_jsonld(trail), C.service_jsonld(sol["name"], sol["lede"], p.path, area=d["label"])]
    return page_shell(title, desc, p.path, body, jsonld=jl, tag=d["label"])


def r_division_case_hub(p, ix):
    d = division_of(p)
    trail = [("Home", "/"), ("Divisions", "/divisions/"), (d["label"], f"/{d['root']}/"), ("Case studies", p.path)]
    pr = d["proof"]
    title = mk_title(f"{d['label']} Case Studies")
    desc = (f"{d['label']} marketing case studies from Consultus Digital, with client-approved "
            f"numbers and the constraints stated.")
    body = f"""
{hero(f"{d['label']} Case Studies", f"{pr['client']}. {pr['stat']} {pr['stat_label']}.", pr['stat'],
      "Client-approved figures from the engagement. Where a number is not published, the case study says so "
      "rather than substituting a percentage that sounds better.", trail=trail)}
<section class="sec dark-full"><div class="sec-inner">
  {sec_head("The numbers", esc(pr['client']), esc(pr['stat_sub']), on_dark=True)}
  {stat_grid(div_proof_stats(d), on_dark=True)}
</div></section>
<section class="sec">
  {sec_head("More work", "Case studies across the other practices.", "")}
  {chips([(x["label"], f"/{x['root']}/case-studies/") for x in DIVS if x["label"] != d["label"]]
         + [("All case studies", "/work/")])}
</section>
{cta("Want this explained on a call?", "We will walk through what produced the number and whether the same approach applies to you.", accent="explained on a call?")}
"""
    return page_shell(title, desc, p.path, body, jsonld=[C.crumb_jsonld(trail)], tag=d["label"])


def r_division_insight_hub(p, ix):
    d = division_of(p)
    trail = [("Home", "/"), ("Divisions", "/divisions/"), (d["label"], f"/{d['root']}/"), ("Insights", p.path)]
    title = mk_title(f"{d['label']} Marketing Insights")
    desc = (f"Practitioner writing on {d['low']} marketing, measurement and growth, from the "
            f"team running the accounts.")
    body = f"""
{hero(f"{d['label']} Marketing Insights", "Writing from inside the accounts.", "inside the accounts",
      f"Notes on what actually happens in {d['low']} programs, including the parts that did not work.",
      trail=trail)}
<section class="sec">
  {sec_head("Start here", "The three things worth knowing about this category.", "")}
  <div class="grid g3">
    <div class="card rv"><h3>What it is measured on</h3><p>{esc(d['unit'].capitalize())}. Everything else is diagnostic.</p></div>
    <div class="card rv" style="--d:60ms"><h3>The constraint</h3><p>{esc(d['regulatory'])}</p></div>
    <div class="card rv" style="--d:120ms"><h3>The unpopular opinion</h3><p>{esc(d['judgment'])}</p></div>
  </div>
</section>
{rail_section(d)}
{cta("Rather just ask?", "A strategy call answers more than an article will, and it is specific to your account.", accent="just ask?")}
"""
    return page_shell(title, desc, p.path, body, jsonld=[C.crumb_jsonld(trail)], tag=d["label"])


def r_division_strategist(p, ix):
    d = division_of(p)
    trail = [("Home", "/"), ("Divisions", "/divisions/"), (d["label"], f"/{d['root']}/"), ("Lead strategist", p.path)]
    title = mk_title(f"{d['label']} Lead Strategist")
    desc = (f"The strategist who sets the {d['low']} plan and owns {d['unit']} at Consultus "
            f"Digital. They take the first call and the quarterly review.")
    body = f"""
{hero(f"{d['label']} Lead Strategist", "The person who sets the plan owns the number.", "owns the number",
      f"Every {d['low']} account has one strategist accountable for {d['unit']}. "
      f"They take the first call and they are still there at the quarterly review.", trail=trail)}
<section class="sec">
  {sec_head("What they do", "Four things, and only four.", "")}
  {steps([
    ("Set the target before launch",
     f"The program gets one number, agreed in writing. For {d['low']} that is {d['unit']}."),
    ("Decide the channel mix",
     "Based on where the business currently loses money, which is often not where the client thinks."),
    ("Say when to stop",
     f"Including the uncomfortable version. {d['not_for']}"),
    ("Own the review",
     "Monthly against the baseline, with variance explained rather than presented."),
  ])}
</section>
<section class="sec bone-full"><div class="sec-inner">
  <div class="grid g2">
    <div class="card rv"><h3>Who they work with</h3><p>{esc(d['buyer'].capitalize())}.</p>{ticks(d['signals'])}</div>
    <div class="card rv" style="--d:60ms"><h3>What they will tell you first</h3><p>{esc(d['judgment'])}</p></div>
  </div>
</div></section>
{cta("Talk to the strategist directly.", "Strategy calls are taken by the practice lead, not by a salesperson who hands you over afterwards.", accent="directly")}
"""
    return page_shell(title, desc, p.path, body, jsonld=[C.crumb_jsonld(trail)], tag=d["label"])


def r_division_assessment(p, ix):
    d = division_of(p)
    trail = [("Home", "/"), ("Divisions", "/divisions/"), (d["label"], f"/{d['root']}/"), ("Growth assessment", p.path)]
    title = mk_title(f"{d['label']} Growth Assessment")
    desc = f"A structured review of your {d['low']} marketing program, measured against {d['unit']}."
    body = f"""
{hero(f"{d['label']} Growth Assessment", "A review of what you run now, and what we would change.",
      "what we would change",
      f"We audit the program against {d['unit']} rather than against impressions, then hand back "
      f"the two or three changes with the largest effect. Whether or not they involve us.", trail=trail)}
<section class="sec">
  {sec_head("What gets reviewed", "Five areas, in this order.", esc(d['judgment']))}
  {steps([
    ("Intake and response time",
     "Recorded calls and enquiry timestamps. Most businesses lose more revenue in that gap than any campaign change would recover."),
    ("Account structure and waste",
     "Search terms, placements and geography. On most accounts we audit, a real share of spend is going somewhere nobody chose."),
    ("Measurement",
     f"Whether the business can see {d['unit']} at all, and whether the platforms and the books agree."),
    ("Creative and message match",
     "Whether the ad, the landing page and the offer say the same thing."),
    ("Capacity",
     f"Whether more demand is even useful right now. {d['not_for']}"),
  ])}
</section>
<section class="sec bone-full"><div class="sec-inner">
  <div class="grid g2">
    <div class="card rv"><h3>What you get back</h3>
      {ticks(["A written finding per area, with the evidence",
              f"A recommended first move, ranked by effect on {d['unit']}",
              "The things we would not spend money on yet",
              "An honest answer on whether you need an agency"])}</div>
    <div class="card rv" style="--d:60ms"><h3>What it costs</h3>
      <p>The assessment is part of the strategy call. There is no charge and no obligation to
      engage afterwards.</p>
      <p class="mt16" style="font-size:14px;color:var(--charcoal)">We do this because the
      businesses that are a genuine fit usually become clients, and the ones that are not
      would have been a bad engagement for both sides.</p></div>
  </div>
</div></section>
{cta(f"Book the {d['low']} assessment.", "Thirty minutes with the practice lead. You keep the findings either way.", accent="Book the")}
"""
    return page_shell(title, desc, p.path, body, jsonld=[C.crumb_jsonld(trail)], tag=d["label"])


# ---------------------------------------------------------------------------
# SECTOR HUB
# ---------------------------------------------------------------------------

def r_sector_hub(p, ix):
    by_path, children, sectors_of, services_of = ix
    d = division_of(p)
    sname = p.sector or p.entity
    prof = SECTORS[sname]
    inds = sorted(sectors_of[p.division].get(sname, []), key=lambda x: x.entity)
    trail = [("Home", "/"), ("Divisions", "/divisions/"), (d["label"], f"/{d['root']}/"),
             ("Industries", d["industries_hub"]), (sname, p.path)]
    title = mk_title(f"{sname} Marketing Agency")
    desc = f"{prof['lede']} Marketing for {lower_name(sname)} across {len(inds)} industries."
    faq = [
        (f"What is different about marketing {lower_name(sname)}?", esc(prof["lede"])),
        (f"Which channel should {lower_name(sname)} start with?", esc(prof["lead_ch"].capitalize()) + "."),
        (f"How long is the buying cycle in {lower_name(sname)}?", esc(prof["cycle"].capitalize()) + "."),
        ("What would you warn us about?", esc(prof["watch"])),
    ]
    body = f"""
{hero(f"{sname} Marketing Agency", prof['lede'], None,
      f"Consultus Digital runs acquisition programs across {len(inds)} industries in this sector, "
      f"measured on {d['unit']}.",
      [f"{len(inds)} industries", f"Buyer: {prof['buyer']}", f"Cycle: {prof['cycle']}"], trail=trail)}

<section class="sec">
  <div class="sec-head">
    <div class="lhs"><span class="section-lbl rv">The category</span>
      <h2 class="sec-title rv">How buying actually works here.</h2></div>
    <div class="prose rv">{''.join(f'<p>{esc(x)}</p>' for x in prof['context'])}</div>
  </div>
  <div class="grid g3">
    <div class="card rv"><span class="num">Who decides</span><h3>{esc(prof['buyer'].capitalize())}</h3></div>
    <div class="card rv" style="--d:60ms"><span class="num">How long it takes</span><h3>{esc(prof['cycle'].capitalize())}</h3></div>
    <div class="card rv" style="--d:120ms"><span class="num">Where to start</span><h3>{esc(prof['lead_ch'].capitalize())}</h3></div>
  </div>
</section>

<section class="sec bone-full"><div class="sec-inner">
  {sec_head("Reality check", "What goes wrong in this sector.", esc(prof['judgment']))}
  <div class="grid g2">
    <div class="card rv"><h3>The three recurring problems</h3>{ticks(prof['challenges'])}</div>
    <div class="card rv" style="--d:60ms"><h3>What we would warn you about</h3><p>{esc(prof['watch'])}</p></div>
  </div>
</div></section>

<section class="sec">
  {sec_head("Industries", f"{len(inds)} industries in this sector.",
            "Each has its own page covering how acquisition works there and what it costs.")}
  {dir_group(sname, f"{len(inds)} industries", [(i.entity, i.path) for i in inds])}
</section>

<section class="sec dark-full"><div class="sec-inner">
  {sec_head("Services", f"How we work with {lower_name(sname)}.",
            f"All ten are measured on {d['unit']}. Which ones lead depends on the business.", on_dark=True)}
  {chips([(m['name'], f"/{d['services_root']}/") for _, m in division_services(p.division)])}
</div></section>

<section class="sec">
  {sec_head("Questions", "Straight answers.", "")}
  {C.faq_block(faq)}
</section>

{cta(f"Working in {lower_name(sname)}?", f"Thirty minutes with the {d['low']} lead strategist and a straight answer on what to change first.", accent=lower_name(sname))}
"""
    jl = [C.crumb_jsonld(trail), C.faq_jsonld([(q, re.sub("<[^>]+>", "", a)) for q, a in faq]),
          C.service_jsonld(f"{sname} Marketing", prof["lede"], p.path, area=sname)]
    return page_shell(title, desc, p.path, body, jsonld=jl, tag=d["label"])


# ---------------------------------------------------------------------------
# INDUSTRY MARKETING AGENCY PAGE
# ---------------------------------------------------------------------------

def r_industry(p, ix):
    by_path, children, sectors_of, services_of = ix
    d = division_of(p)
    ind = p.entity
    sname = p.sector
    prof = SECTORS[sname]
    hook = INDUSTRY_HOOKS.get(ind, prof["lede"])
    low = lower_name(ind)
    sing = singular(ind)
    svc_pages = sorted(services_of.get(p.path, []), key=lambda x: x.path)
    siblings = [s for s in sectors_of[p.division].get(sname, []) if s.path != p.path]
    trail = [("Home", "/"), ("Divisions", "/divisions/"), (d["label"], f"/{d['root']}/"),
             ("Industries", d["industries_hub"]), (sname, f"/{d['industries_root']}/{slugify(sname)}/"),
             (ind, p.path)]

    svc_cards = ""
    for i, sp in enumerate(svc_pages):
        slug = service_slug(sp)
        mod = SERVICES.get((p.division, slug))
        if not mod:
            continue
        svc_cards += (f'<a class="card rv" style="--d:{min(i,6)*40}ms" href="{esc(sp.path)}">'
                      f'<span class="num">{esc(mod["metric"])}</span>'
                      f'<h3>{esc(mod["name"])} for {esc(low)}</h3>'
                      f'<p>{esc(mod["blurb"])}</p></a>')

    display = pick(p.path, [
        f"Marketing for {low}, measured on {d['unit']}.",
        f"{ind}: the number that matters is {d['unit']}.",
        f"Growth for {low}, judged at the {d['unit'].replace('cost per ', '')}.",
    ])
    accent = pick(p.path + "a", [d["unit"], low])

    faq = [
        (f"What makes marketing {low} different?", esc(hook)),
        (f"What should {low} be measured on?",
         f"{esc(d['unit'].capitalize())}. Enquiry counts and impressions are diagnostic, not the target."),
        (f"Which channel should {low} start with?",
         f"{esc(prof['lead_ch'].capitalize())}. That is the usual answer for this sector, and the "
         f"exception is when capacity, not demand, is the constraint."),
        (f"How long before {low} see results?",
         f"Paid channels give a readable number in four to six weeks. Organic search takes three to "
         f"six months. We set the real review at ninety days and report leading indicators weekly."),
        ("What would make you tell us not to spend?", esc(d["not_for"])),
        (f"What constrains advertising for {low}?", esc(prof["watch"])),
    ]
    qual = title_qualifier(p)
    title = mk_title(f"{ind} Marketing Agency", qual)
    desc = (f"{d['label']} marketing agency for {low}. {hook}" if qual
            else f"Marketing agency for {low}. {hook}")
    body = f"""
{hero(f"{ind} Marketing Agency", display, accent, hook,
      [f"Measured on {d['unit']}", sname, f"{len(svc_pages)} services"], trail=trail)}

<section class="sec">
  <div class="sec-head">
    <div class="lhs"><span class="section-lbl rv">The category</span>
      <h2 class="sec-title rv">What is actually different here.</h2></div>
    <div class="prose rv"><p>{esc(hook)}</p>{''.join(f'<p>{esc(x)}</p>' for x in prof['context'])}</div>
  </div>
  <div class="grid g3">
    <div class="card rv"><span class="num">Who decides</span><h3>{esc(prof['buyer'].capitalize())}</h3></div>
    <div class="card rv" style="--d:60ms"><span class="num">How long it takes</span><h3>{esc(prof['cycle'].capitalize())}</h3></div>
    <div class="card rv" style="--d:120ms"><span class="num">Judged on</span><h3>{esc(d['unit'].capitalize())}</h3></div>
  </div>
</section>

<section class="sec bone-full"><div class="sec-inner">
  {sec_head("Services", f"How we work with {low}.",
            f"Ten services, all measured on {d['unit']}. Most programs use two or three of them.")}
  <div class="grid g3">{svc_cards}</div>
</div></section>

<section class="sec">
  {sec_head("Reality check", "Where programs in this sector go wrong.", esc(prof['judgment']))}
  <div class="grid g2">
    <div class="card rv"><h3>Recurring problems</h3>{ticks(prof['challenges'])}</div>
    <div class="card rv" style="--d:60ms"><h3>When we would tell you not to spend</h3>
      <p>{esc(d['not_for'])}</p>
      <p class="mt16" style="font-size:14px;color:var(--charcoal)">{esc(prof['watch'])}</p></div>
  </div>
</section>

<section class="sec dark-full"><div class="sec-inner">
  {sec_head("Proof", f"{d['proof']['client']}.", "Client-approved figures from a "
            f"{d['low']} engagement.", on_dark=True)}
  {stat_grid(div_proof_stats(d), on_dark=True)}
  <div class="mt40"><a class="btn primary on-dark" href="/{d['root']}/case-studies/">
    {esc(d['label'])} case studies <span class="arr">&rarr;</span></a></div>
</div></section>

<section class="sec">
  {sec_head("Questions", f"What {low} ask before they engage.", "")}
  {C.faq_block(faq)}
</section>

{f'''<section class="sec bone-full"><div class="sec-inner">
  {sec_head("Related industries", f"Others in {lower_name(sname)}.", "")}
  {chips([(s.entity, s.path) for s in sorted(siblings, key=lambda x: x.entity)[:24]])}
  <div class="mt24"><a class="btn secondary" href="{esc(d['industries_hub'])}">All {d['low']} industries <span class="arr">&rarr;</span></a></div>
</div></section>''' if siblings else ''}

{cta(f"Run a {sing}?", f"Thirty minutes with the {d['low']} lead strategist, a review of what you run now, and a straight answer on what to change first.", accent=f"Run a {sing}?")}
"""
    jl = [C.crumb_jsonld(trail), C.faq_jsonld([(q, re.sub("<[^>]+>", "", a)) for q, a in faq]),
          C.service_jsonld(f"{ind} Marketing", hook, p.path, area=ind)]
    return page_shell(title, desc, p.path, body, noindex=(p.indexation != "Index"), jsonld=jl, tag=d["label"])


# ---------------------------------------------------------------------------
# SERVICE x INDUSTRY LANDING PAGE
# ---------------------------------------------------------------------------

def r_service_industry(p, ix):
    by_path, children, sectors_of, services_of = ix
    d = division_of(p)
    slug = service_slug(p)
    mod = SERVICES[(p.division, slug)]
    ind = p.entity
    sname = p.sector
    prof = SECTORS.get(sname, {})
    hook = INDUSTRY_HOOKS.get(ind, prof.get("lede", ""))
    low = lower_name(ind)
    sing = singular(ind)
    parent = by_path.get(p.parent)
    cap = CAP_BY_SLUG.get(SERVICE_TO_CAPABILITY.get(slug, "paid-media"))

    trail = [("Home", "/"), ("Divisions", "/divisions/"), (d["label"], f"/{d['root']}/"),
             ("Services", f"/{d['services_root']}/")]
    if parent:
        trail.append((ind, parent.path))
    trail.append((mod["name"], p.path))

    h1 = f"{mod['name']} for {ind}"
    kw = f"{mod['name']} for {ind}"
    display = pick(p.path, [
        f"{mod['name']} for {low}, measured on {mod['metric']}.",
        f"{mod['name']} that is judged on {mod['metric']}.",
        f"{mod['name']} for {low}. One number: {mod['metric']}.",
    ])

    siblings_svc = [s for s in sorted(services_of.get(p.parent, []), key=lambda x: x.path)
                    if s.path != p.path]
    same_svc_other_inds = []
    for other in sectors_of[p.division].get(sname, []):
        if other.path == (parent.path if parent else None):
            continue
        for sp in services_of.get(other.path, []):
            if service_slug(sp) == slug:
                same_svc_other_inds.append((other.entity, sp.path))
                break

    angles = "".join(
        f'<div class="card rv" style="--d:{i*60}ms"><span class="num">0{i+1}</span>'
        f'<h3>{esc(t)}</h3><p>{esc(b)}</p></div>'
        for i, (t, b) in enumerate(mod["angles"]))

    q1 = mod["question"].format(industry_lower=low, industry_singular_lower=sing, industry=ind)
    a1 = mod["answer"].format(industry_lower=low, industry_singular_lower=sing, industry=ind)
    faq = [
        (q1, esc(a1)),
        (f"What is different about {lower_name(mod['name'])} for {low}?", esc(hook)),
        (f"What is this measured on?", f"{esc(mod['metric'].capitalize())}, against a baseline agreed before launch."),
        (f"When is {lower_name(mod['name'])} the wrong choice for {low}?", esc(mod["decision"])),
    ]
    if prof.get("watch"):
        faq.append(("What should we watch out for?", esc(prof["watch"])))

    qual = title_qualifier(p)
    title = mk_title(f"{mod['name']} for {ind}", qual)
    desc = (f"{mod['name']} for {low} ({d['label']}), measured on {mod['metric']}. {mod['blurb']}"
            if qual else
            f"{mod['name']} for {low}, measured on {mod['metric']}. {mod['blurb']}")

    same_svc_block = ""
    if same_svc_other_inds:
        same_svc_head = sec_head("Same service, other industries",
                                 f"{mod['name']} across {lower_name(sname)}.", "")
        same_svc_block = ('<div class="mt40"></div>' + same_svc_head
                          + chips(sorted(same_svc_other_inds)[:24]))

    body = f"""
{hero(kw, display, mod['metric'], mod['blurb'],
      [f"Measured on {mod['metric']}", d['label'], sname], trail=trail)}

<section class="sec">
  <div class="sec-head">
    <div class="lhs"><span class="section-lbl rv">The approach</span>
      <h2 class="sec-title rv">{esc(mod['name'])} for {esc(low)}.</h2></div>
    <div class="prose rv">{''.join(f'<p>{esc(x)}</p>' for x in mod['intro'])}
      <p>{esc(hook)}</p></div>
  </div>
  <div class="grid g2">
    <div class="card rv"><h3>What ships</h3>{ticks(mod['deliverables'])}</div>
    <div class="card rv" style="--d:60ms"><h3>Where this stops working</h3>
      <p>{esc(mod['warning'])}</p>
      <p class="mt16" style="font-size:14px;color:var(--charcoal)">{esc(prof.get('watch',''))}</p></div>
  </div>
</section>

<section class="sec bone-full"><div class="sec-inner">
  {sec_head("How we think about it", "Three decisions that shape the account.", esc(mod['decision']))}
  <div class="grid g3">{angles}</div>
</div></section>

<section class="sec">
  {sec_head("Context", f"What {low} are working against.",
            esc(prof.get('judgment', '')))}
  <div class="grid g2">
    <div class="card rv"><h3>Recurring problems in {esc(lower_name(sname))}</h3>{ticks(prof.get('challenges', []))}</div>
    <div class="card rv" style="--d:60ms"><h3>Buying reality</h3>
      {ticks([f"Decided by {prof.get('buyer','the owner')}",
              f"Cycle: {prof.get('cycle','varies')}",
              f"Usually starts with {prof.get('lead_ch','search')}"])}</div>
  </div>
</section>

<section class="sec">
  {sec_head("Questions", "Straight answers.", "")}
  {C.faq_block(faq)}
</section>

<section class="sec bone-full"><div class="sec-inner">
  {sec_head("Related", f"Other services for {low}.", "")}
  {chips([(SERVICES[(p.division, service_slug(s))]['name'], s.path)
          for s in siblings_svc if (p.division, service_slug(s)) in SERVICES])}
  {same_svc_block}
  <div class="mt24"><a class="btn secondary" href="/capabilities/{cap['slug']}/">{esc(cap['name'])} capability <span class="arr">&rarr;</span></a></div>
</div></section>

{cta(f"Run a {sing}?", f"Thirty minutes with the {d['low']} lead strategist and a straight answer on whether {lower_name(mod['name'])} is your first move.", accent=f"Run a {sing}?")}
"""
    jl = [C.crumb_jsonld(trail), C.faq_jsonld([(q, re.sub("<[^>]+>", "", a)) for q, a in faq]),
          C.service_jsonld(h1, mod["blurb"], p.path, area=ind)]
    return page_shell(title, desc, p.path, body, noindex=(p.indexation != "Index"), jsonld=jl, tag=d["label"])


# ---------------------------------------------------------------------------
# WRITING STANDARD LINTER
# ---------------------------------------------------------------------------

BANNED_WORDS = [
    "innovative", "cutting-edge", "cutting edge", "best-in-class", "world-class",
    "industry-leading", "industry leading", "premium", "comprehensive", "personalized",
    "personalised", "results-driven", "state-of-the-art", "game-changing", "revolutionary",
    "synergy", "seamless", "holistic", "robust", "tailored", "bespoke", "unlock",
    "elevate", "empower", "leverage", "cookie-cutter", "best in class",
]
BANNED_PHRASES = [
    "it is not simply", "not just a", "whether you are", "whether you're",
    "in today's", "at its core", "the result?", "this is where",
    "it is important to note", "when it comes to", "ultimately,",
    "by combining", "this approach ensures", "it is worth noting",
    "that said,", "in addition,", "furthermore,", "moreover,",
    "in other words,", "at the end of the day", "as a result,",
    "with that being said", "click here", "learn more", "get started today",
    "begin your journey", "dynamic landscape", "sustainable transformation",
]
TAG_RE = re.compile(r"<[^>]+>")
WS_RE = re.compile(r"\s+")


def visible_text(html_str):
    txt = re.sub(r"<script.*?</script>", " ", html_str, flags=re.S | re.I)
    txt = re.sub(r"<style.*?</style>", " ", txt, flags=re.S | re.I)
    txt = TAG_RE.sub(" ", txt)
    txt = txt.replace("&amp;", "&").replace("&rarr;", " ").replace("&middot;", " ")
    txt = txt.replace("&nbsp;", " ").replace("&quot;", '"').replace("&#x27;", "'")
    return WS_RE.sub(" ", txt)


def lint_page(path, html_str, findings):
    """Group by rule plus the exact offending clause so one bad source string is
    reported once rather than once per page that inherits it."""
    txt = visible_text(html_str)
    low = txt.lower()

    def add(rule, snippet):
        # normalise to the clause around the hit so repeats collapse to one entry
        clause = WS_RE.sub(" ", snippet).strip()
        key = (rule, clause[:70])
        if key in findings:
            findings[key][1] += 1
        else:
            findings[key] = [path, 1, clause]
    for dash in ("—", "–"):
        if dash in txt:
            i = txt.index(dash)
            add("em/en dash", txt[max(0, i - 40):i + 40].strip())
    if "!" in txt.replace("!important", ""):
        i = txt.index("!")
        add("exclamation mark", txt[max(0, i - 40):i + 40].strip())
    for w in BANNED_WORDS:
        for m in re.finditer(r"\b" + re.escape(w) + r"\b", low):
            add("banned word: " + w, txt[max(0, m.start() - 45):m.start() + 45].strip())
            break
    for ph in BANNED_PHRASES:
        i = low.find(ph)
        if i >= 0:
            add("AI phrasing: " + ph, txt[max(0, i - 40):i + 60].strip())
    for m in re.finditer(r"\bConsultus\b(?!\s+Digital)", txt):
        add("bare 'Consultus'", txt[max(0, m.start() - 45):m.start() + 45].strip())
        break


# ---------------------------------------------------------------------------
# DISPATCH
# ---------------------------------------------------------------------------

RENDERERS = {
    "Homepage": r_homepage,
    "Division Hub": r_divisions_hub,
    "Capability Hub": r_capability_hub,
    "Solution Hub": r_solution_hub,
    "Case Study Hub": r_work_hub,
    "Insight Hub": r_insight_hub,
    "Expert Hub": r_expert_hub,
    "About": r_about,
    "Contact": r_contact,
    "Conversion": r_conversion,
    "Shared Capability": r_shared_capability,
    "Shared Solution": r_shared_solution,
    "Division Marketing Agency Hub": r_division_hub,
    "Industry Directory": r_industry_directory,
    "Division Service Hub": r_division_service_hub,
    "Division Solution Hub": r_division_solution_hub,
    "Division Solution": r_division_solution,
    "Division Case Study Hub": r_division_case_hub,
    "Division Insight Hub": r_division_insight_hub,
    "Division Lead Strategist": r_division_strategist,
    "Division Assessment": r_division_assessment,
    "Sector Hub": r_sector_hub,
    "Industry Marketing Agency Page": r_industry,
    "Service × Industry Landing Page": r_service_industry,
}


# ---------------------------------------------------------------------------
# SITEMAPS / ROBOTS
# ---------------------------------------------------------------------------

LASTMOD = "2026-08-05"

_BASE_ATTR = re.compile(r'((?:href|src|action|poster)=")/(?!/)')
_BASE_URL = re.compile(r'(url\()(["\']?)/(?!/)')


def apply_base(html_str, base):
    """Prefix root-relative URLs for hosting under a subdirectory.

    Canonical tags and JSON-LD carry absolute https URLs, so they are untouched.
    """
    html_str = _BASE_ATTR.sub(r"\1" + base + "/", html_str)
    return _BASE_URL.sub(r"\1\2" + base + "/", html_str)


def write_sitemaps(built):
    """Only pages marked Index go into a sitemap. Phase 3 stays out until it has content."""
    groups = defaultdict(list)
    for p in built:
        if p.indexation == "Index":
            groups[p.sitemap].append(p.path)
    names = []
    for name, paths in sorted(groups.items()):
        urls = "".join(
            f"<url><loc>{C.SITE}{path}</loc><lastmod>{LASTMOD}</lastmod></url>"
            for path in sorted(set(paths)))
        xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
               + urls + "\n</urlset>\n")
        open(os.path.join(DIST, name), "w", encoding="utf-8").write(xml)
        names.append(name)
    idx = "".join(f"<sitemap><loc>{C.SITE}/{n}</loc><lastmod>{LASTMOD}</lastmod></sitemap>"
                  for n in sorted(names))
    open(os.path.join(DIST, "sitemap_index.xml"), "w", encoding="utf-8").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + idx + "\n</sitemapindex>\n")
    return names, sum(len(set(v)) for v in groups.values())


def write_robots():
    open(os.path.join(DIST, "robots.txt"), "w", encoding="utf-8").write(
        "User-agent: *\n"
        "Allow: /\n\n"
        f"Sitemap: {C.SITE}/sitemap_index.xml\n")


def copy_assets(base=""):
    dest = os.path.join(DIST, "assets")
    if os.path.isdir(dest):
        shutil.rmtree(dest)
    shutil.copytree(SRC_ASSETS, dest)
    # fonts.css on disk references capitalised filenames; the files are lowercase,
    # which breaks on any case-sensitive host. Rewrite the references to match.
    fc = os.path.join(dest, "fonts.css")
    if os.path.isfile(fc):
        css = open(fc, encoding="utf-8").read()
        css = re.sub(r"(NuberNext[A-Za-z\-]*\.otf)", lambda m: m.group(1).lower(), css)
        open(fc, "w", encoding="utf-8").write(css)
    # A subdirectory-hosted build has to prefix url() inside the stylesheets too,
    # or the fonts 404 while every page looks fine.
    if base:
        for root, _dirs, files in os.walk(dest):
            for name in files:
                if not name.endswith(".css"):
                    continue
                fp = os.path.join(root, name)
                css = open(fp, encoding="utf-8").read()
                open(fp, "w", encoding="utf-8").write(_BASE_URL.sub(r"\1\2" + base + "/", css))


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true", help="include Phase 3 (all 6,532 URLs)")
    ap.add_argument("--phase", type=int, default=None, help="build one phase only")
    ap.add_argument("--lint", action="store_true", help="report writing-standard violations")
    ap.add_argument("--clean", action="store_true", help="wipe dist first")
    ap.add_argument("--base", default=os.environ.get("SITE_BASE", ""),
                    help="path prefix when hosting under a subdirectory, "
                         "e.g. --base /consultus-architecture for GitHub Pages")
    args = ap.parse_args()
    base = args.base.rstrip("/")

    pages, dropped = load_pages()
    ix = build_index(pages)

    if args.phase:
        selected = [p for p in pages if p.phase == args.phase]
    elif args.all:
        selected = pages
    else:
        selected = [p for p in pages if p.phase in (1, 2)]

    if args.clean and os.path.isdir(DIST):
        shutil.rmtree(DIST)
    os.makedirs(DIST, exist_ok=True)

    print(f"Architecture: {len(pages)} unique URLs ({len(dropped)} duplicates removed)")
    print(f"Building:     {len(selected)} pages")

    findings = {}
    counts = defaultdict(int)
    missing = defaultdict(int)
    built = []
    total_bytes = 0

    for p in selected:
        fn = RENDERERS.get(p.ptype)
        if fn is None:
            missing[p.ptype] += 1
            continue
        try:
            html_str = fn(p, ix)
        except Exception as e:
            print(f"  ERROR {p.path} [{p.ptype}]: {type(e).__name__}: {e}")
            raise
        if base:
            html_str = apply_base(html_str, base)
        outdir = os.path.join(DIST, p.path.strip("/"))
        os.makedirs(outdir, exist_ok=True)
        with open(os.path.join(outdir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_str)
        total_bytes += len(html_str.encode("utf-8"))
        counts[p.ptype] += 1
        built.append(p)
        if args.lint:
            lint_page(p.path, html_str, findings)

    copy_assets(base)
    names, n_urls = write_sitemaps(built)
    write_robots()

    # Record what this run actually built so qa.py can verify a partial build
    # against what was asked for rather than against the whole architecture.
    with open(os.path.join(DIST, ".build-manifest.json"), "w", encoding="utf-8") as f:
        json.dump({"paths": sorted(p.path for p in built),
                   "scope": "all" if args.all else (f"phase{args.phase}" if args.phase else "indexable"),
                   "base": base}, f)

    print("\nPages written by type:")
    for t, n in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"  {n:>6}  {t}")
    if missing:
        print("\nNO RENDERER (skipped):")
        for t, n in missing.items():
            print(f"  {n:>6}  {t}")
    print(f"\nTotal: {len(built)} pages, {total_bytes/1048576:.1f} MB "
          f"({total_bytes/max(len(built),1)/1024:.1f} KB average)")
    print(f"Sitemaps: {len(names)} files, {n_urls} indexable URLs")
    noindexed = sum(1 for p in built if p.indexation != "Index")
    if noindexed:
        print(f"Noindex:  {noindexed} pages (Phase 3, awaiting content threshold)")

    if args.lint:
        if findings:
            print(f"\nWRITING STANDARD: {len(findings)} distinct violations")
            for (rule, _), (path, n, clause) in sorted(
                    findings.items(), key=lambda kv: -kv[1][1]):
                print(f"  [{rule}]  x{n} pages")
                print(f"     ...{clause}...")
                print(f"     e.g. {path}")
            return 1
        print("\nWRITING STANDARD: clean")
    return 0


if __name__ == "__main__":
    sys.exit(main())
