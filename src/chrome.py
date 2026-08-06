# -*- coding: utf-8 -*-
"""
Shared page furniture: head, navigation, breadcrumbs, CTA and footer.

Everything that appears on every one of the generated pages lives here so a
brand change is a one-file edit rather than a six thousand file find-and-replace.
"""

import hashlib
import html
import json
import os

SITE = "https://www.consultusdigital.com"
BRAND = "Consultus Digital"


def _asset_version():
    """Content hash of the shared stylesheet, appended to its URL so a CSS change
    is picked up immediately instead of being served from cache."""
    css = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "css", "site.css")
    try:
        with open(css, "rb") as f:
            return hashlib.md5(f.read()).hexdigest()[:8]
    except OSError:
        return "dev"


CSS_V = _asset_version()


def esc(s):
    return html.escape(str(s), quote=True)


# --------------------------------------------------------------------------
# HEAD
# --------------------------------------------------------------------------

def head(title, description, path, *, noindex=False, jsonld=None, og_type="website"):
    canonical = SITE + path
    robots = ("noindex, follow" if noindex else
              "index, follow, max-image-preview:large, max-snippet:-1")
    blocks = ""
    for block in (jsonld or []):
        blocks += ('\n<script type="application/ld+json">'
                   + json.dumps(block, ensure_ascii=False, separators=(",", ":"))
                   + "</script>")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{esc(canonical)}">
<meta name="theme-color" content="#FAF8F3">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{esc(canonical)}">
<meta property="og:site_name" content="{BRAND}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/brand/consultus-mark.svg" type="image/svg+xml">
<link rel="preconnect" href="/assets/fonts/">
<link rel="stylesheet" href="/assets/fonts.css">
<link rel="stylesheet" href="/assets/css/site.css?v={CSS_V}">{blocks}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""


# --------------------------------------------------------------------------
# NAV
# --------------------------------------------------------------------------

def nav(divisions, capabilities, solutions, *, tag=None, tag_slug=None, icons=None):
    ic = icons or (lambda name, cls="": "")

    div_links = "".join(
        f'<a href="/{d["root"]}/">{ic(d["slug"], "mi")}'
        f'<span>{esc(d["label"])}<small>{esc(d["nav_blurb"])}</small></span></a>'
        for d in divisions)

    # Split the LIST into columns, never the joined HTML string. Slicing the
    # string cut an entry in half mid-element and split its blurb across both
    # columns, which is exactly what it looked like.
    cap_half = (len(capabilities) + 1) // 2

    def cap_col(items):
        return "".join(
            f'<a href="/capabilities/{c["slug"]}/">{ic(c["slug"], "mi")}'
            f'<span>{esc(c["name"])}<small>{esc(c["blurb"])}</small></span></a>'
            for c in items)

    half = (len(solutions) + 1) // 2

    def sol_col(items):
        return "".join(
            f'<a href="/growth-solutions/{s[0]}/">{ic(s[0], "mi")}'
            f'<span>{esc(s[1])}</span></a>' for s in items)

    tag_html = (f'<span class="nav-tag">{ic(tag_slug, "ico")}{esc(tag)}</span>'
                if tag else "")

    return f"""<div class="navwrap">
<nav class="pill" id="nav">
  <div class="nav-left">
    <a class="nav-logo" href="/" aria-label="{BRAND} home">
      <img src="/assets/brand/consultus-wordmark-dark.png" alt="{BRAND}" width="150" height="19">
    </a>{tag_html}
  </div>
  <ul class="nav-links">
    <li>
      <a class="top" href="/divisions/">Divisions
        <svg class="caret" viewBox="0 0 10 6" fill="none" aria-hidden="true"><path d="M1 1l4 4 4-4" stroke="currentColor" stroke-width="1.4"/></svg>
      </a>
      <div class="mega w2"><div class="mega-inner">
        <div class="mega-col"><h5>Industry practices</h5>{div_links}</div>
        <div class="mega-col"><h5>Start here</h5>
          <a href="/divisions/">All divisions<small>How the practices are organised</small></a>
          <a href="/work/">Case studies<small>Named clients and real numbers</small></a>
          <a href="/experts/">The team<small>Who does the work</small></a>
        </div>
      </div></div>
    </li>
    <li>
      <a class="top" href="/capabilities/">Capabilities
        <svg class="caret" viewBox="0 0 10 6" fill="none" aria-hidden="true"><path d="M1 1l4 4 4-4" stroke="currentColor" stroke-width="1.4"/></svg>
      </a>
      <div class="mega w2"><div class="mega-inner">
        <div class="mega-col"><h5>What we do</h5>{cap_col(capabilities[:cap_half])}</div>
        <div class="mega-col"><h5>&nbsp;</h5>{cap_col(capabilities[cap_half:])}</div>
      </div></div>
    </li>
    <li>
      <a class="top" href="/growth-solutions/">Solutions
        <svg class="caret" viewBox="0 0 10 6" fill="none" aria-hidden="true"><path d="M1 1l4 4 4-4" stroke="currentColor" stroke-width="1.4"/></svg>
      </a>
      <div class="mega w2"><div class="mega-inner">
        <div class="mega-col"><h5>Growth solutions</h5>{sol_col(solutions[:half])}</div>
        <div class="mega-col"><h5>&nbsp;</h5>{sol_col(solutions[half:])}</div>
      </div></div>
    </li>
    <li><a class="top" href="/work/">Work</a></li>
    <li><a class="top" href="/insights/">Insights</a></li>
    <li><a class="top" href="/about/">About</a></li>
  </ul>
  <div style="display:flex;gap:8px;align-items:center">
    <button class="nav-toggle" id="navToggle" aria-expanded="false" aria-controls="nav">Menu</button>
    <a class="btn primary sm" href="/book-a-strategy-call/">Book a strategy call</a>
  </div>
</nav>
</div>
"""


# --------------------------------------------------------------------------
# BREADCRUMBS
# --------------------------------------------------------------------------

def crumbs(trail, *, on_dark=False):
    """trail = [(label, href_or_None), ...] with the current page last."""
    items = []
    for i, (label, href) in enumerate(trail):
        last = i == len(trail) - 1
        if last or not href:
            items.append(f'<li><span aria-current="page">{esc(label)}</span></li>')
        else:
            items.append(f'<li><a href="{esc(href)}">{esc(label)}</a></li>')
    cls = "crumbs on-dark" if on_dark else "crumbs"
    return f'<nav class="{cls}" aria-label="Breadcrumb"><ol>{"".join(items)}</ol></nav>'


def crumb_jsonld(trail):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": label,
             **({"item": SITE + href} if href else {})}
            for i, (label, href) in enumerate(trail)
        ],
    }


# --------------------------------------------------------------------------
# CTA
# --------------------------------------------------------------------------

def cta(heading, sub, *, accent=None, primary=("Book a strategy call", "/book-a-strategy-call/"),
        secondary=("See the case studies", "/work/")):
    if accent:
        heading = heading.replace(accent, f'<span class="sem">{accent}</span>', 1)
    return f"""<section class="sec cta">
  <div class="sec-inner">
    <h2 class="rv">{heading}</h2>
    <p class="rv" style="--d:80ms">{esc(sub)}</p>
    <div class="btn-row rv" style="--d:160ms">
      <a class="btn primary on-dark" href="{esc(primary[1])}">{esc(primary[0])} <span class="arr">&rarr;</span></a>
      <a class="btn secondary on-dark" href="{esc(secondary[1])}">{esc(secondary[0])}</a>
    </div>
    <ul class="reassure rv" style="--d:220ms">
      <li>Thirty minutes</li><li>No charge, no obligation</li><li>You keep the findings</li>
    </ul>
  </div>
</section>
"""


# --------------------------------------------------------------------------
# FOOTER
# --------------------------------------------------------------------------

def footer(divisions, capabilities, solutions, icons=None):
    ic = icons or (lambda name, cls="": "")
    div_li = "".join(
        f'<li><a href="/{d["root"]}/">{ic(d["slug"], "fi")}{esc(d["label"])}</a></li>' for d in divisions)
    cap_li = "".join(
        f'<li><a href="/capabilities/{c["slug"]}/">{ic(c["slug"], "fi")}{esc(c["name"])}</a></li>'
        for c in capabilities)
    sol_li = "".join(
        f'<li><a href="/growth-solutions/{s[0]}/">{ic(s[0], "fi")}{esc(s[1])}</a></li>' for s in solutions)
    year = 2026
    return f"""<footer>
<div class="foot-in">
  <div class="foot-top">
    <div>
      <a class="foot-logo" href="/" aria-label="{BRAND} home">
        <img src="/assets/brand/consultus-wordmark-light.png" alt="{BRAND}" width="240" height="30">
      </a>
      <p class="foot-blurb">A performance marketing and sales enablement agency organised
      into four industry practices, measured on the outcome each one is actually judged by.</p>
    </div>
    <a class="btn primary on-dark" href="/book-a-strategy-call/">Book a strategy call <span class="arr">&rarr;</span></a>
  </div>
  <div class="foot-cols">
    <div><h4>Divisions</h4><ul>{div_li}</ul></div>
    <div><h4>Capabilities</h4><ul>{cap_li}</ul></div>
    <div><h4>Solutions</h4><ul>{sol_li}</ul></div>
    <div><h4>Company</h4><ul>
      <li><a href="/about/">About</a></li>
      <li><a href="/work/">Case studies</a></li>
      <li><a href="/insights/">Insights</a></li>
      <li><a href="/experts/">Experts</a></li>
      <li><a href="/contact/">Contact</a></li>
    </ul></div>
    <div><h4>Talk to us</h4><ul>
      <li><a href="/book-a-strategy-call/">Book a strategy call</a></li>
      <li><a href="/contact/">Send an enquiry</a></li>
    </ul></div>
  </div>
  <div class="foot-bottom">
    <span>&copy; {year} {BRAND}. All rights reserved.</span>
    <span>Toronto, Canada</span>
  </div>
</div>
</footer>
<div class="cta-rail" id="ctaRail">
  <span class="cr-note">Free 30-minute strategy call. You keep the findings.</span>
  <a class="btn primary sm" href="/book-a-strategy-call/">Book a strategy call <span class="arr">&rarr;</span></a>
</div>
<script>
(function(){{
  var t=document.getElementById('navToggle'),n=document.getElementById('nav');
  if(t&&n){{t.addEventListener('click',function(){{
    var o=n.classList.toggle('open');t.setAttribute('aria-expanded',o?'true':'false');
  }});}}
  var els=document.querySelectorAll('.rv');
  if(!('IntersectionObserver' in window)){{els.forEach(function(e){{e.classList.add('in');}});}}
  else{{
    var io=new IntersectionObserver(function(es){{
      es.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target);}}}});
    }},{{rootMargin:'0px 0px -8% 0px'}});
    els.forEach(function(e){{io.observe(e);}});
  }}
  requestAnimationFrame(function(){{document.body.classList.add('masks-in');}});
  // Reveal the conversion rail once the hero is behind you, hide it again at the
  // footer so it never covers the CTA it duplicates.
  // The hero is position:sticky, so it never stops intersecting and cannot be
  // used as the trigger. Scroll depth is measured instead.
  var rail=document.getElementById('ctaRail'), footEl=document.querySelector('footer');
  if(rail){{
    var atFoot=false, ticking=false;
    function sync(){{
      var past=(window.scrollY||window.pageYOffset)>window.innerHeight*0.9;
      rail.classList.toggle('show', past&&!atFoot);
      ticking=false;
    }}
    window.addEventListener('scroll',function(){{
      if(!ticking){{ ticking=true; requestAnimationFrame(sync); }}
    }},{{passive:true}});
    if(footEl&&'IntersectionObserver' in window){{
      new IntersectionObserver(function(es){{ atFoot=es[0].isIntersecting; sync(); }},
        {{threshold:0}}).observe(footEl);
    }}
    sync();
  }}
}})();
</script>
</body>
</html>
"""


def org_jsonld():
    return {
        "@context": "https://schema.org",
        "@type": "Organization",
        "@id": SITE + "/#organization",
        "name": BRAND,
        "url": SITE + "/",
        "logo": SITE + "/assets/brand/consultus-wordmark-dark.png",
        "description": ("Performance marketing and sales enablement agency organised into "
                        "healthcare, trades, DTC and professional services practices."),
        "address": {"@type": "PostalAddress", "addressLocality": "Toronto",
                    "addressRegion": "ON", "addressCountry": "CA"},
    }


def faq_jsonld(pairs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in pairs
        ],
    }


def service_jsonld(name, description, path, area=None):
    d = {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": name,
        "description": description,
        "url": SITE + path,
        "provider": {"@id": SITE + "/#organization"},
    }
    if area:
        d["serviceType"] = area
    return d


def faq_block(pairs, *, on_dark=False):
    if not pairs:
        return ""
    rows = "".join(
        f"<details><summary>{esc(q)}</summary><div>{a}</div></details>"
        for q, a in pairs)
    return f'<div class="faq">{rows}</div>'
