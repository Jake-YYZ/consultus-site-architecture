# Consultus Digital — Site Architecture

The full 6,532-page architecture from the V2 CSV and sitemap packages, built as a
real website. Separate repo, so nothing here touches the existing prototype site.

## The short version

You do not edit 6,532 HTML files. You edit a handful of content files, run one
command, and every page that uses that content updates at once.

```bash
python3 build.py --all
```

That writes the whole site into `dist/` in about twenty seconds.

To look at it, double-click **Preview Site.command** in Finder. It builds the
site and opens it at <http://localhost:8099/>.

## What got built

| | |
|---|---|
| URLs in the architecture | 6,543 in the CSV, **6,532 unique** |
| Pages generated | 6,532 |
| Live and indexable now | **965** (Phase 1 + Phase 2) |
| Held back as `noindex` | 5,567 (Phase 3) |
| Page types | 24 distinct templates |
| Average page weight | 23 KB |

### The hierarchy

```
/                                    homepage
├── /divisions/                      4 industry practices
│   └── /healthcare-marketing-agency/          division home
│       ├── /healthcare-specialties/           industry directory
│       │   ├── /healthcare-specialties/dental/            sector hub (45 of these)
│       │   └── .../general-dentistry-marketing-agency/    industry page (598)
│       ├── /healthcare-marketing-services/    service hub
│       │   └── .../seo-for-general-dentistry/ service × industry (5,792)
│       ├── /healthcare-marketing-agency/solutions/        10 per division
│       ├── /healthcare-marketing-agency/case-studies/
│       ├── /healthcare-marketing-agency/insights/
│       ├── /healthcare-marketing-agency/lead-strategist/
│       └── /healthcare-marketing-agency/growth-assessment/
├── /capabilities/                   7 shared capabilities
├── /growth-solutions/               8 shared solutions
└── /work/  /insights/  /experts/  /about/  /contact/  /book-a-strategy-call/
```

## Three decisions worth knowing about

**1. Only 965 pages are set to be indexed.**
The source data marks 5,577 URLs as *"Index after content threshold"*. Those pages
are generated and browsable, but they carry a `noindex` tag and stay out of the XML
sitemaps until real content is written for them. Publishing several thousand thin
pages at once is how a site earns a doorway-page penalty from Google. The 965
indexable pages match the supplied sitemaps exactly.

To promote Phase 3 pages later: change their `Indexation` value to `Index` in
`data/master_url_inventory.csv` and rebuild. The sitemaps update themselves.

**2. Eleven duplicate URLs were removed.**
"Architecture firms" was filed under two sectors at once, which generated the same
11 URLs twice. It now sits under *Real estate and property*, alongside Engineering
firms and Surveying firms. 6,543 rows becomes 6,532 unique pages.

**3. Shared CSS instead of a copy per page.**
The prototype site inlines the whole stylesheet and a base64 logo into every file,
which makes each page around 400 KB. At this scale that would be a 2.6 GB website.
Here the design system is one file that every page links, so pages are 23 KB and a
brand change is a one-file edit. The existing prototype repo is untouched.

## Editing content

Everything readable lives in `src/content/`. Change a line, rerun the build.

| File | What it controls | Reach |
|---|---|---|
| `divisions.py` | The four practices: positioning, proof numbers, what each is measured on | Every page in that division |
| `services.py` | 40 service modules (10 per division) | The 5,792 service pages |
| `sectors.py` | 45 sector profiles: how buying works, what goes wrong | Every industry and service page in that sector |
| `industries_*.py` | One concrete line per industry, 597 of them | That industry's pages |
| `solutions.py` | 40 division solutions | The solution pages |
| `corporate.py` | Homepage, About, Contact, hub pages | Those pages |
| `chrome.py` | Nav, footer, breadcrumbs, schema markup | Every page |
| `assets/css/site.css` | The whole design system | Every page |

Proof numbers in `divisions.py` are the real client-approved figures: La Vie 512
leads, Dragonscale 13.23 MER, Zayouna $72.70 CPL, Gordon's $164 CPL. Nothing is
invented. If a number is not verified, the page says so rather than substituting
something vaguer.

## The two checks

**Writing standard.** Your human-led copy rules are enforced by the build:

```bash
python3 build.py --all --lint
```

It fails on em dashes, exclamation marks, banned adjectives (comprehensive,
seamless, tailored, world-class, leverage and the rest), AI sentence rhythms
("this is where", "whether you are", "it is worth noting"), and any bare
"Consultus" that should read "Consultus Digital". It currently reports clean.

**Structure.** Everything a broken site would get wrong:

```bash
python3 qa.py
```

Checks every architecture URL has exactly one page, every internal link resolves,
no orphan pages, unique titles and descriptions on all 6,532 pages, correct
canonical and robots tags, and that no `noindex` page has leaked into a sitemap.
All checks currently pass.

## Commands

```bash
python3 build.py                  # the 965 indexable pages only
python3 build.py --all            # all 6,532
python3 build.py --phase 1        # just the 392 core pages, fastest
python3 build.py --all --lint     # build and check the writing standard
python3 qa.py                     # structural checks
python3 serve.py                  # preview at localhost:8099
```

## Deploying

Pushing to `main` builds the site in GitHub Actions and publishes it to GitHub
Pages. The repo stores the generator, not the 145 MB of generated HTML, so a copy
change is a one-line diff.

The preview deploy is set to `noindex` site-wide so it can never compete with
consultusdigital.com. For the real launch, remove the "Keep the preview out of
search engines" step in `.github/workflows/deploy-pages.yml`.

## Still to do before this replaces the live site

- **Redirects.** These URLs are new. Old URLs need 301s to their new homes, which
  needs a mapping of the current site's URLs against this architecture.
- **Case study pages.** `/work/` lists the six engagements and links to the
  division hubs. The full case study pages still live on the prototype site and
  need porting into this structure.
- **Insights.** `/insights/` and the four division insight hubs are built but
  carry no articles yet. The blog is going to WordPress, so these need to point
  at it or pull from it.
- **Team.** `/experts/` links to the four lead strategist pages. Those pages
  describe the role rather than naming a person, because I did not have the names.
- **Phase 3 content.** The 5,567 held-back pages need real content before their
  `Indexation` flag is flipped. They are genuinely useful as-is for internal
  linking and for browsing, but they are not ready to be indexed.
