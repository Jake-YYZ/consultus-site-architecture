# -*- coding: utf-8 -*-
"""
Division profiles: the four industry practices plus the corporate voice.

Every proof number in this file is real and attributable to a named Consultus
Digital client engagement. Nothing here is invented. If a division has no
verified number for a claim, the claim is written qualitatively instead.
"""

DIVISIONS = {
    "Healthcare": {
        "low": "healthcare",
        "slug": "healthcare",
        "root": "healthcare-marketing-agency",
        "industries_root": "healthcare-specialties",
        "services_root": "healthcare-marketing-services",
        "industries_hub": "/healthcare-specialties/",
        "label": "Healthcare",
        "noun": "healthcare organizations",
        "short": "Healthcare",
        "nav_blurb": "Clinics, hospitals, specialty practices and health brands.",
        "hero_kw": "Healthcare Marketing Agency",
        "display": "Marketing that fills the schedule, not just the funnel.",
        "display_accent": "fills the schedule",
        "lede": (
            "A healthcare lead is not a booked appointment. Consultus Digital builds "
            "acquisition programs where the measurement stops at the confirmed visit, "
            "so you can tell which campaigns actually put people in chairs."
        ),
        "thesis": (
            "Most healthcare marketing reports stop at form fills. The number that "
            "pays for staff is the appointment that shows up."
        ),
        "buyer": "practice owners, marketing directors and clinic operators",
        "unit": "cost per booked appointment",
        "units": ["cost per booked appointment", "appointment show rate", "patient lifetime value"],
        "proof": {
            "client": "La Vie Executive Health",
            "url": "/work/la-vie-executive-health/",
            "stat": "512",
            "stat_label": "leads in month one",
            "stat_sub": "Executive health program launch, Oakville",
            "support": [
                ("$89.53", "Meta cost per lead", "Month one, La Vie Executive Health"),
                ("23", "keywords in the top three", "Nine weeks from launch"),
                ("9 wks", "launch to full channel mix", "Paid, organic and LinkedIn live"),
            ],
        },
        "regulatory": (
            "Healthcare advertising sits inside real rules. Google restricts some "
            "health claims, Meta limits how you can target health interests, and "
            "regulated professions answer to their college or board for how they "
            "advertise. We build campaigns that pass review the first time."
        ),
        "judgment": (
            "If your front desk cannot answer the phone inside two rings during "
            "business hours, fix that before you raise ad budget. Paid media makes "
            "an intake problem more expensive, not less."
        ),
        "not_for": (
            "Practices at full capacity with a six week waitlist. If you cannot "
            "see more patients, the honest recommendation is to raise prices or "
            "add clinical hours before spending on acquisition."
        ),
        "signals": [
            "Appointment volume flat while ad spend climbs",
            "No line of sight from ad click to booked visit",
            "Front desk taking calls the website should have handled",
            "Competitors outranking you for your own specialty",
        ],
    },

    "Trades": {
        "low": "trades",
        "slug": "trades",
        "root": "trades-marketing-agency",
        "industries_root": "trades-industries",
        "services_root": "trades-marketing-services",
        "industries_hub": "/trades-industries/",
        "label": "Trades",
        "noun": "trades and home services businesses",
        "short": "Trades",
        "nav_blurb": "Contractors, home services, construction and property trades.",
        "hero_kw": "Trades Marketing Agency",
        "display": "The phone rings or the marketing did not work.",
        "display_accent": "The phone rings",
        "lede": (
            "Trades marketing is judged on booked jobs and cost per job, not "
            "impressions. Consultus Digital runs call tracking from the first "
            "click through to the signed quote so you know which channel paid for itself."
        ),
        "thesis": (
            "In the trades, the scoreboard is simple. Booked jobs, average ticket, "
            "and what you paid to get them."
        ),
        "buyer": "owners, general managers and service managers",
        "unit": "cost per booked job",
        "units": ["cost per booked job", "booked job rate", "average ticket"],
        "proof": {
            "client": "Gordon's Downsizing",
            "url": "/work/gordons-downsizing/",
            "stat": "$164",
            "stat_label": "cost per lead",
            "stat_sub": "Gordon's Downsizing, 53 leads from a standing start",
            "support": [
                ("53", "leads from a standing start", "Gordon's Downsizing"),
                ("4.30%", "Google click-through rate", "Against a 2% category norm"),
                ("3.22%", "Meta click-through rate", "Two persona-led creative families"),
            ],
        },
        "regulatory": (
            "Trades campaigns live or die on service area accuracy. A campaign "
            "that pulls calls from ninety minutes outside your radius burns budget "
            "and staff patience. We build geography into the account structure, not "
            "the exclusion list."
        ),
        "judgment": (
            "Seasonality is not a reason to pause. The cheapest leads in most "
            "trades come in the shoulder weeks either side of peak, when the "
            "auction empties out and your competitors have gone dark."
        ),
        "not_for": (
            "Businesses booked solid eight weeks out with no crew capacity to add. "
            "More leads at that point become cancelled appointments and bad reviews."
        ),
        "signals": [
            "Leads arriving from outside the service area",
            "No idea which campaign produced last month's best jobs",
            "Missed calls going straight to voicemail",
            "Paying for clicks on jobs you do not want",
        ],
    },

    "DTC": {
        "low": "DTC",
        "slug": "dtc",
        "root": "dtc-marketing-agency",
        "industries_root": "dtc-industries",
        "services_root": "dtc-marketing-services",
        "industries_hub": "/dtc-industries/",
        "label": "DTC",
        "noun": "direct-to-consumer and ecommerce brands",
        "short": "DTC",
        "nav_blurb": "Ecommerce, subscription and consumer product brands.",
        "hero_kw": "DTC Marketing Agency",
        "display": "Managed to blended return, not platform-reported return.",
        "display_accent": "blended return",
        "lede": (
            "Every ad platform claims the same sale. Consultus Digital manages DTC "
            "brands to marketing efficiency ratio, the number that ties total revenue "
            "to total spend and cannot be double counted."
        ),
        "thesis": (
            "Platform ROAS is a story each channel tells about itself. MER is the "
            "only number the bank account agrees with."
        ),
        "buyer": "founders, ecommerce directors and growth leads",
        "unit": "marketing efficiency ratio",
        "units": ["marketing efficiency ratio", "contribution margin", "new customer cost"],
        "proof": {
            "client": "Dragonscale Supplies",
            "url": "/work/dragonscale-supplies/",
            "stat": "13.23",
            "stat_label": "marketing efficiency ratio",
            "stat_sub": "Dragonscale Supplies, up from 9.0",
            "support": [
                ("8.10x", "return on ad spend", "BookSeats, month one"),
                ("+27%", "against the previous record month", "Dragonscale Supplies"),
                ("+248%", "click-through rate, creator video over static", "BookSeats"),
            ],
        },
        "regulatory": (
            "Consumer advertising rules bite hardest on claims and pricing. "
            "Strikethrough pricing, subscription terms and health or performance "
            "claims all get reviewed. We keep creative inside the lines so accounts "
            "do not get restricted mid-flight."
        ),
        "judgment": (
            "If contribution margin after shipping and payment fees is under thirty "
            "percent, paid acquisition will not fix the business. Fix the unit "
            "economics or the higher the spend, the faster the loss."
        ),
        "not_for": (
            "Brands with one product, no repeat purchase and no email list. "
            "Acquisition economics only work when a customer is worth more than "
            "the first order."
        ),
        "signals": [
            "Platform ROAS looks fine while the bank balance does not",
            "Creative fatigue inside ten days of a launch",
            "New customer cost climbing every quarter",
            "Email and SMS treated as an afterthought",
        ],
    },

    "Professional Services": {
        "low": "professional services",
        "slug": "professional-services",
        "root": "professional-services-marketing-agency",
        "industries_root": "professional-services-industries",
        "services_root": "professional-services-marketing-services",
        "industries_hub": "/professional-services-industries/",
        "label": "Professional Services",
        "noun": "professional services firms",
        "short": "Professional Services",
        "nav_blurb": "Legal, financial, insurance, accounting, consulting and B2B.",
        "hero_kw": "Professional Services Marketing Agency",
        "display": "The metric is signed clients, not enquiries.",
        "display_accent": "signed clients",
        "lede": (
            "A professional services firm can drown in enquiries and still sign "
            "nothing worth having. Consultus Digital measures to the matter, the "
            "mandate or the retainer, which means intake and CRM are part of the build."
        ),
        "thesis": (
            "Lead volume flatters a report. The firm only grows when the right "
            "matters get signed."
        ),
        "buyer": "managing partners, marketing directors and business development leads",
        "unit": "cost per signed matter",
        "units": ["cost per signed matter", "qualified enquiry rate", "matter value"],
        "proof": {
            "client": "Zayouna Law Firm",
            "url": "/work/zayouna-law-firm/",
            "stat": "$72.70",
            "stat_label": "cost per lead on Meta",
            "stat_sub": "Zayouna Law, against a $200 to $250 category benchmark",
            "support": [
                ("$190", "cost per personal injury lead on Google", "Against a $442 benchmark"),
                ("74", "leads in the measured window", "Zayouna Law Firm"),
                ("-42%", "cost per lead, week over week", "After intake and targeting rebuild"),
            ],
        },
        "regulatory": (
            "Regulated professions advertise under rules set by their law society, "
            "securities regulator or professional body. Comparative claims, "
            "guarantees and testimonials are the usual tripwires. We write to the "
            "standard your regulator applies."
        ),
        "judgment": (
            "Most firms do not have a lead problem. They have a response time "
            "problem. An enquiry answered in five minutes is worth several times "
            "one answered the next morning, and no amount of ad budget closes that gap."
        ),
        "not_for": (
            "Firms with no intake owner. If enquiries land in a shared inbox that "
            "nobody is accountable for, marketing spend leaks out the bottom."
        ),
        "signals": [
            "Plenty of enquiries, few of them the right matter type",
            "No attribution from first click to signed file",
            "Referral pipeline flat and nothing built to replace it",
            "Partners fielding enquiries intake should handle",
        ],
    },
}

DIVISION_ORDER = ["Healthcare", "Trades", "DTC", "Professional Services"]

# The seven shared capabilities, delivered across every division.
CAPABILITIES = [
    {
        "slug": "paid-media",
        "name": "Paid Media",
        "blurb": "Search, social, shopping and marketplace buying managed to cost per outcome.",
        "lede": (
            "Paid media is the fastest way to test whether a market wants what you "
            "sell. It is also the fastest way to spend money proving it does not."
        ),
        "body": [
            "We run search, paid social, shopping and marketplace campaigns as one "
            "budget rather than four disconnected accounts. Structure comes first: "
            "campaigns split by intent and margin, not by whatever the platform "
            "wizard suggested.",
            "Every account we take over gets a search terms audit in the first week. "
            "On most accounts inheriting a broad match setup, a meaningful share of "
            "spend is going to terms the business would never bid on deliberately.",
        ],
        "deliverables": [
            "Account structure split by intent, margin and geography",
            "Negative keyword and audience exclusion wall, maintained weekly",
            "Creative testing calendar with named hypotheses",
            "Budget pacing against cost per outcome, not impression share",
            "Weekly search terms and placement review",
        ],
        "judgment": (
            "Broad match with a smart bidding strategy works when you have "
            "conversion volume to feed it. Under roughly thirty conversions a "
            "month, it mostly learns noise. Start tighter and loosen as data arrives."
        ),
    },
    {
        "slug": "performance-creative",
        "name": "Performance Creative",
        "blurb": "Ad creative built as hypotheses, tested against hook rate and cost per outcome.",
        "lede": (
            "Creative is the biggest lever in a paid account and the one most "
            "agencies treat as decoration."
        ),
        "body": [
            "We build creative in families. Each family carries one hypothesis about "
            "why someone buys, and every asset in it is a variation on that idea. "
            "That way a losing test tells you something instead of just losing.",
            "Hook rate is the first read. If the first three seconds do not hold "
            "attention, nothing downstream matters, and no amount of budget fixes it.",
        ],
        "deliverables": [
            "Hook families mapped to buyer motivations",
            "Static, video and creator-led assets produced in matched sets",
            "Hook rate, hold rate and cost per outcome reported per asset",
            "Winning angles fed into landing page copy and search ad extensions",
            "Refresh cadence set by fatigue data, not by calendar",
        ],
        "judgment": (
            "Volume alone is not a creative strategy. Twenty assets testing one "
            "idea teach you less than six assets testing three."
        ),
    },
    {
        "slug": "seo-ai-search",
        "name": "SEO and AI Search",
        "blurb": "Organic visibility across classic search results and AI answer engines.",
        "lede": (
            "Search now has two front doors. One returns ten links. The other "
            "returns a written answer that may never send a click."
        ),
        "body": [
            "Classic SEO still pays. Rankings, technical health and internal linking "
            "decide what gets crawled and what earns position. That work has not "
            "changed and we still do it.",
            "What has changed is that a growing share of queries end in an AI "
            "generated answer. Getting cited in those answers depends on clear "
            "entity signals, structured data and content a model can quote without "
            "guessing. We build for both, because both send buyers.",
        ],
        "deliverables": [
            "Technical audit covering crawl, index, speed and structured data",
            "Entity and schema build so machines can identify who you are",
            "Content mapped to real questions, answered in the first paragraph",
            "Internal link architecture connecting hubs to detail pages",
            "Visibility tracking across classic results and AI answer surfaces",
        ],
        "judgment": (
            "Chasing AI citations without fixing crawlability is backwards. If a "
            "model cannot reliably parse the page, it will not quote it either."
        ),
    },
    {
        "slug": "content-authority",
        "name": "Content and Authority",
        "blurb": "Writing that answers the question, earns the citation and holds up to review.",
        "lede": (
            "Most category content answers a question the reader did not ask, "
            "several paragraphs after they wanted the answer."
        ),
        "body": [
            "We write to search intent, which means the answer goes first and the "
            "context follows. A page about cost opens with a price range. A page "
            "about a procedure opens with what happens and how long it takes.",
            "In regulated categories the writing goes through review before it "
            "publishes, with a named reviewer and a review date on the page. That "
            "is a trust signal to readers and a quality signal to search engines.",
        ],
        "deliverables": [
            "Topic map built from real queries and sales conversations",
            "Briefs that specify the judgment, comparison and example each page owes",
            "Named expert review for regulated categories",
            "Refresh schedule for pages losing position",
            "Internal linking from every article back to the commercial page",
        ],
        "judgment": (
            "Publishing cadence is overrated. Ten pages that fully answer a "
            "question beat fifty that half answer one, and they are cheaper to maintain."
        ),
    },
    {
        "slug": "websites-cro",
        "name": "Websites and CRO",
        "blurb": "Sites and landing pages built to convert, then tested against a baseline.",
        "lede": (
            "A redesign that looks better and converts worse is a expensive way to "
            "lose revenue quietly."
        ),
        "body": [
            "We treat the site as a conversion system. Page speed, message match "
            "between ad and landing page, form length and proof placement all get "
            "measured rather than argued about.",
            "Testing runs against a named hypothesis with a defined success metric. "
            "A test that wins becomes the new baseline. A test that loses gets "
            "documented so nobody proposes it again in eight months.",
        ],
        "deliverables": [
            "Conversion audit across the paths that carry real traffic",
            "Message match between every campaign and its landing page",
            "Build in the platform you already run, or a rebuild if it is warranted",
            "Test roadmap with hypothesis, metric and minimum sample",
            "Form, booking and checkout instrumentation that survives tracking loss",
        ],
        "judgment": (
            "Below roughly a thousand conversions a month, most A/B tests will "
            "never reach significance. At that volume, fix the obvious problems "
            "and spend the effort on traffic quality instead."
        ),
    },
    {
        "slug": "crm-automation",
        "name": "CRM and Automation",
        "blurb": "The plumbing between a lead arriving and a person following up.",
        "lede": (
            "Marketing that ends at the form submission hands the business a "
            "problem instead of a customer."
        ),
        "body": [
            "We build the path from enquiry to owner: routing rules, response time "
            "targets, follow up sequences and the status fields that let you see "
            "where deals stall.",
            "Attribution is part of the same build. Source, campaign, creative and "
            "landing page get written onto the record so the sales pipeline and the "
            "ad account are finally telling the same story.",
        ],
        "deliverables": [
            "Lead routing with named owners and response time targets",
            "Pipeline stages that match how the business actually sells",
            "Automated follow up for the first hour, first day and first week",
            "Source, campaign and creative stamped on every record",
            "Reporting that ties closed revenue back to the campaign that started it",
        ],
        "judgment": (
            "Speed to first contact beats sequence sophistication. Five minutes "
            "with a plain phone call outperforms a beautifully written email sent the next day."
        ),
    },
    {
        "slug": "analytics-intelligence",
        "name": "Analytics and Intelligence",
        "blurb": "Measurement that survives cookie loss, iOS changes and platform self-reporting.",
        "lede": (
            "If two channels each claim the same conversion, at least one of them "
            "is wrong and your budget is being allocated on the difference."
        ),
        "body": [
            "We instrument the events that matter, send them server side where the "
            "platform supports it, and reconcile what the platforms report against "
            "what the business actually booked.",
            "The output is a single view: spend, leads, qualified leads, closed "
            "revenue and the efficiency ratio across everything. Channel level "
            "detail sits underneath it, not on top of it.",
        ],
        "deliverables": [
            "Event tracking plan tied to real business outcomes",
            "Server side conversion sending where the platform supports it",
            "Blended efficiency reporting across all channels",
            "Reconciliation between platform reported and CRM recorded conversions",
            "Dashboard the leadership team reads without a translator",
        ],
        "judgment": (
            "Perfect attribution does not exist any more. Aim for directionally "
            "correct and consistently measured, then make budget decisions on "
            "blended numbers rather than arguing about last click."
        ),
    },
]

# Eight solutions shared across divisions, expressed as outcomes rather than channels.
SHARED_SOLUTIONS = [
    ("multi-location-growth", "Multi-location Growth",
     "Growing several locations at once without them competing for the same click.",
     "Multi-location advertising fails in a predictable way. Locations bid against "
     "each other, budget flows to whichever site has the best tracking rather than "
     "the most capacity, and head office cannot see which location is actually short."),
    ("market-expansion", "Market Expansion",
     "Entering a new city or region where nobody knows the brand yet.",
     "A new market has no branded search volume, no reviews and no referral base. "
     "The playbook that works at home assumes all three."),
    ("new-location-launch", "New Location Launch",
     "Getting a new site to break even faster than the last one did.",
     "The window that decides a new location is the first ninety days. Demand has "
     "to arrive before the fixed costs do, which means the campaign has to start "
     "before the doors open."),
    ("lead-conversion", "Lead Conversion",
     "Turning the enquiries you already get into booked business.",
     "Most businesses looking to buy more leads are losing more than they would "
     "gain, somewhere between the form submission and the follow up call."),
    ("sales-enablement", "Sales Enablement",
     "Giving the people who close deals the context marketing already collected.",
     "The sales team is usually working blind. Marketing knows which ad, which "
     "page and which question brought the person in, and none of it reaches the "
     "person making the call."),
    ("marketing-attribution", "Marketing Attribution",
     "One version of the truth across platforms that all claim the same sale.",
     "Add up what every platform reports and you will find more conversions than "
     "the business recorded. Budget decisions made on those numbers move money "
     "toward whichever channel reports most aggressively."),
    ("digital-transformation", "Digital Transformation",
     "Replacing manual process with systems that hold up as volume grows.",
     "Spreadsheets, shared inboxes and one person who knows how everything works. "
     "It functions until volume doubles or that person leaves."),
    ("talent-acquisition", "Talent Acquisition",
     "Recruiting campaigns run with the same rigour as demand generation.",
     "Hiring campaigns get treated as HR admin and run as job board spend. Run as "
     "performance marketing, with landing pages, creative testing and a tracked "
     "pipeline, they cost less per hire."),
]
