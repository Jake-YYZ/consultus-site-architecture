# -*- coding: utf-8 -*-
"""
Service modules, keyed by (division, url_slug).

Each entry supplies the substance for one service hub page and for every
service-by-industry page beneath it. Fields:

  name          display name from the architecture CSV
  verb          how the service reads in a sentence ("run paid search")
  blurb         one line, used in navigation and cards
  intro         two paragraphs of real explanation
  deliverables  five concrete things that ship
  metric        the number this service is judged on
  angles        three (heading, body) beats, written as decisions not features
  warning       the practical limitation, stated plainly
  decision      when to pick this service over the obvious alternative
  question      the FAQ question this service always gets asked
  answer        the honest answer, with {industry} substituted at build time
"""

S = {}

# ============================================================================
# HEALTHCARE
# ============================================================================

S[("Healthcare", "digital-marketing")] = {
    "name": "Digital Marketing Agency",
    "verb": "run the full digital program",
    "blurb": "The whole acquisition program, managed to booked appointments.",
    "intro": [
        "A full program means the channels stop being managed in isolation. Search "
        "captures the people already looking, social builds the demand that search "
        "later captures, and the website has to convert both without a handoff that loses people.",
        "We start with the measurement, because a program without a booked "
        "appointment number is four channels each claiming credit for the same patient.",
    ],
    "deliverables": [
        "Channel plan with a budget split by cost per booked appointment",
        "Search, social and organic managed against one shared target",
        "Landing pages and booking flow instrumented end to end",
        "CRM or practice management system connected to campaign data",
        "One monthly report showing spend, appointments and cost per appointment",
    ],
    "metric": "cost per booked appointment",
    "angles": [
        ("Start with intake, not ads",
         "We ask to listen to recorded calls before proposing a budget. On most "
         "audits, the gap between enquiries received and appointments booked is "
         "larger than anything a campaign change would deliver."),
        ("Split the budget by intent",
         "Someone searching for a specific procedure is worth a different bid than "
         "someone who saw a video and clicked. Merging them into one campaign "
         "hides which one pays."),
        ("Report to the schedule",
         "The monthly report leads with appointments booked and cost per "
         "appointment. Impressions and clicks sit underneath, available but not leading."),
    ],
    "warning": "A full program takes about ninety days to read properly. Search "
               "returns signal in weeks, organic in months. Judging the whole "
               "program on month one will point you at the wrong conclusion.",
    "decision": "Take the full program when more than two channels are already "
                "running and nobody can say which is working. If only one channel "
                "runs today, fix that one first.",
    "question": "How long before we can tell if this is working for our {industry_singular_lower}?",
    "answer": "Paid search gives a readable cost per appointment inside four to six "
              "weeks. Paid social takes longer because creative needs a testing "
              "cycle. Organic search moves in three to six months. We set the "
              "review at ninety days and share the leading indicators weekly until then.",
}

S[("Healthcare", "paid-search")] = {
    "name": "Paid Search and PPC",
    "verb": "run paid search",
    "blurb": "Google and Microsoft search campaigns bid to cost per appointment.",
    "intro": [
        "Search advertising reaches people who have already decided they need "
        "care and are choosing where to get it. That makes it the highest intent "
        "traffic available and usually the first channel worth funding.",
        "The work is mostly restraint. Tight match types, a maintained negative "
        "list and campaigns split so a high value procedure never shares a budget "
        "with a general enquiry term.",
    ],
    "deliverables": [
        "Campaigns split by procedure, urgency and patient value",
        "Negative keyword wall reviewed weekly against the search terms report",
        "Ad copy written to the regulator's standard and reviewed before launch",
        "Call tracking with recordings tied to the keyword that produced the call",
        "Bid strategy set against appointments, not form fills",
    ],
    "metric": "cost per booked appointment",
    "angles": [
        ("Bid on the procedure, not the category",
         "Category terms bring researchers. Procedure and condition terms bring "
         "people who are ready. The second group costs more per click and far less per appointment."),
        ("Watch the search terms report",
         "Automated bidding will find traffic wherever it is cheapest, which is "
         "rarely where it is most valuable. The negative list is the steering wheel."),
        ("Track the call, not just the form",
         "A large share of healthcare enquiries arrive by phone. Without call "
         "tracking, those campaigns look like they are failing and get cut."),
    ],
    "warning": "Google restricts advertising for some health conditions and "
               "treatments, and certain claims will get an ad disapproved or an "
               "account flagged. We check restrictions before building, not after a rejection.",
    "decision": "Fund paid search first when people already search for what you "
                "do. If the treatment is new or unfamiliar, demand has to be built "
                "on social before search has anything to capture.",
    "question": "What should we expect to pay per click for {industry_lower}?",
    "answer": "It depends far more on your market than your specialty. Competitive "
              "urban markets run several times the cost of regional ones for the "
              "same term. The number that matters is cost per booked appointment, "
              "and a higher cost per click often produces a lower one.",
}

S[("Healthcare", "seo")] = {
    "name": "SEO",
    "verb": "run search engine optimization",
    "blurb": "Organic rankings for the conditions, procedures and locations you serve.",
    "intro": [
        "Organic search compounds. A page that ranks keeps producing enquiries "
        "long after the work is paid for, which is the opposite of how paid media behaves.",
        "For healthcare, the work splits three ways: the technical health of the "
        "site, content that answers real patient questions properly, and local "
        "signals so the practice appears for searches near it.",
    ],
    "deliverables": [
        "Technical audit covering crawl, speed, indexation and structured data",
        "Condition and procedure pages that answer the question in the first paragraph",
        "Google Business Profile and local citation cleanup for every location",
        "Medical review with a named reviewer and review date on the page",
        "Internal linking from articles into the booking pages",
    ],
    "metric": "non-branded organic enquiries",
    "angles": [
        ("Answer first, context second",
         "A page about what a procedure costs should open with a price range. "
         "Search engines and readers both reward pages that lead with the answer."),
        ("One page per question",
         "Merging five patient questions into one long page means ranking for "
         "none of them well. Split them and link them together."),
        ("Local is a separate discipline",
         "Rankings in the map results depend on profile completeness, review "
         "velocity and proximity. Those levers barely overlap with the ones that move the standard results."),
    ],
    "warning": "SEO does not produce a readable return inside a quarter. If the "
               "practice needs appointments this month, fund paid search and treat "
               "organic as the twelve month investment it is.",
    "decision": "Prioritise organic when your cost per click is high and rising. "
                "The higher the paid cost in a market, the more an organic position is worth.",
    "question": "How long until we rank for {industry_lower} searches?",
    "answer": "Local and long-tail terms often move within two to three months. "
              "Competitive procedure terms in a major market take six to twelve. "
              "Sites with existing authority move faster than new domains, and no "
              "honest agency will promise a position or a date.",
}

S[("Healthcare", "ai-search")] = {
    "name": "AEO, GEO and AI Search",
    "verb": "build visibility in AI answers",
    "blurb": "Getting cited when patients ask an AI assistant instead of a search engine.",
    "intro": [
        "A growing share of health questions now get answered by an AI assistant "
        "that summarises several sources and may never send a click. Being one of "
        "those sources is a different job than ranking first.",
        "Models cite content they can parse confidently and attribute clearly. "
        "That rewards plain answers, clean structure, consistent entity information "
        "and pages that do not bury the fact being quoted.",
    ],
    "deliverables": [
        "Entity and organisation schema so machines can identify the practice",
        "Question-and-answer content structured for direct extraction",
        "Consistent name, address and credential data across the web",
        "Author and medical reviewer markup with real credentials",
        "Monitoring of which assistants cite you and for what questions",
    ],
    "metric": "citations in AI generated answers",
    "angles": [
        ("Write the sentence you want quoted",
         "Models lift clean, self-contained statements. A fact wrapped in three "
         "clauses of hedging does not survive summarisation."),
        ("Credentials are machine readable now",
         "Author markup with real credentials and a review date affects whether a "
         "model treats the page as reliable on a health topic."),
        ("Consistency beats volume",
         "Conflicting addresses, names or hours across directories make an entity "
         "ambiguous, and ambiguous entities do not get cited."),
    ],
    "warning": "This is the least mature measurement surface in search. Citation "
               "tracking is improving but still partial, and anyone quoting precise "
               "AI referral numbers is estimating.",
    "decision": "Worth funding once classic SEO fundamentals are in place. Chasing "
                "citations on a site that crawls badly is effort spent in the wrong order.",
    "question": "Does AI search actually send patients to {industry_lower}?",
    "answer": "It sends fewer clicks than classic search and the clicks it does "
              "send tend to convert well, because the reader has already been "
              "given context. Treat it as a share-of-answer play rather than a "
              "traffic channel, and do not move budget out of what is working to chase it.",
}

S[("Healthcare", "paid-social")] = {
    "name": "Paid Social",
    "verb": "run paid social",
    "blurb": "Meta and other social platforms used to create demand, not just capture it.",
    "intro": [
        "Social advertising reaches people before they start searching. For "
        "elective and self-pay services, that is where the demand gets built in "
        "the first place.",
        "Health targeting is restricted on most platforms, so the targeting job "
        "moves into the creative. The right message finds the right person when "
        "the audience settings cannot.",
    ],
    "deliverables": [
        "Creative families built around distinct patient motivations",
        "Compliant copy and imagery checked against platform health policy",
        "Landing pages matched to the specific ad angle that produced the click",
        "Lead quality fed back from the practice into campaign optimisation",
        "Retargeting sequenced by how far someone got in the booking flow",
    ],
    "metric": "cost per qualified enquiry",
    "angles": [
        ("Creative is the targeting",
         "Platforms restrict health interest targeting. An ad that opens by "
         "naming the problem it solves self-selects its audience more accurately "
         "than most targeting settings would."),
        ("Expect lower intent, plan for it",
         "Social enquiries need more nurturing than search enquiries. Budget for "
         "the follow up sequence when you budget for the ads."),
        ("Feed quality back into the algorithm",
         "Optimising toward form fills produces form fills. Optimising toward "
         "appointments that showed up produces appointments."),
    ],
    "warning": "Meta prohibits ads that imply knowledge of a person's medical "
               "condition. Copy written as direct address to a diagnosis gets "
               "rejected and repeated rejections put the ad account at risk.",
    "decision": "Fund paid social when the service is elective, self-pay or "
                "unfamiliar. For urgent care and established conditions, search captures demand more cheaply.",
    "question": "Can we advertise {industry_lower} on Meta at all?",
    "answer": "Usually yes, with constraints. You cannot imply you know the "
              "viewer has a condition, use before-and-after imagery in most health "
              "categories, or make outcome guarantees. Ads that describe the "
              "service and speak to a general audience clear review reliably.",
}

S[("Healthcare", "web-design")] = {
    "name": "Website Design and CRO",
    "verb": "build and optimise the website",
    "blurb": "Sites and booking flows built to turn visits into appointments.",
    "intro": [
        "The website is where every channel converts or fails. A practice can run "
        "excellent campaigns into a site that loses two thirds of the people who arrive.",
        "We measure before rebuilding. Sometimes the fix is a shorter form and a "
        "visible phone number, which ships in a week. Sometimes the site genuinely "
        "needs replacing.",
    ],
    "deliverables": [
        "Conversion audit of the pages carrying real traffic",
        "Booking flow rebuilt with the fewest steps the system allows",
        "Page speed work on the templates that matter most",
        "Accessible, mobile-first build that passes contrast and keyboard checks",
        "Test roadmap with a hypothesis and success metric per test",
    ],
    "metric": "visit to appointment conversion rate",
    "angles": [
        ("Shorten the form before redesigning the page",
         "Every field removed from a healthcare enquiry form tends to lift "
         "completion. Ask for what intake genuinely needs to make the first call."),
        ("Make the phone number a first class action",
         "Older patient populations and urgent enquiries still prefer to call. "
         "Hiding the number behind a contact page costs bookings."),
        ("Match the page to the ad",
         "Someone who clicked an ad about one procedure should land on that "
         "procedure, not the homepage. Message match is the cheapest conversion gain available."),
    ],
    "warning": "Below roughly a thousand conversions a month, A/B tests will not "
               "reach statistical significance in a useful timeframe. At that "
               "volume, fix the clear problems and skip the testing theatre.",
    "decision": "Rebuild when the site cannot be edited without a developer, "
                "fails accessibility, or loads slowly on mobile. Otherwise optimise what exists.",
    "question": "Should we rebuild the site or fix the one we have for {industry_lower}?",
    "answer": "Fix what you have if the platform lets your team edit pages, the "
              "site loads in under three seconds on mobile, and the booking flow "
              "works. Rebuild if any of those three fail. A rebuild is a "
              "three month project and a form fix is a three day one.",
}

S[("Healthcare", "crm-revops")] = {
    "name": "CRM and Revenue Operations",
    "verb": "build the CRM and intake systems",
    "blurb": "The path from enquiry to booked appointment, built and measured.",
    "intro": [
        "Most practices lose more revenue between the enquiry and the appointment "
        "than they would gain from any campaign improvement. Nobody owns that gap "
        "because it sits between marketing and the front desk.",
        "We build the routing, the follow up and the reporting that makes the gap "
        "visible, then stamp campaign data onto the record so the practice can see "
        "which ads produce patients who actually arrive.",
    ],
    "deliverables": [
        "Enquiry routing with a named owner and a response time target",
        "Automated follow up for the first hour, first day and first week",
        "Source, campaign and landing page written to every patient record",
        "Practice management or CRM integration so bookings flow back to the ad platforms",
        "No-show and reactivation sequences",
    ],
    "metric": "enquiry to booked appointment rate",
    "angles": [
        ("Response time is the whole game",
         "An enquiry answered within five minutes converts several times better "
         "than one answered the next morning. Nothing else in this list matters as much."),
        ("Reactivation is the cheapest growth available",
         "Patients who have already been treated are far cheaper to bring back "
         "than new ones are to acquire, and most practices have never once asked them to return."),
        ("Stamp the record at creation",
         "Attribution added later is guesswork. Written on at the moment the "
         "enquiry arrives, it is fact."),
    ],
    "warning": "This work only pays if somebody owns intake. Automation routes "
               "and reminds. It does not make the call.",
    "decision": "Do this before increasing ad spend if enquiry to appointment "
                "conversion is under about a third. Growth there is cheaper than growth in the ad account.",
    "question": "Do we need a new system for our {industry_singular_lower}?",
    "answer": "Usually not. Most practices already have a practice management "
              "system and a CRM that between them do the job, badly configured. "
              "Replacing systems is expensive and disruptive. We start by fixing "
              "the configuration and only recommend a change when the current tool genuinely cannot do it.",
}

S[("Healthcare", "content-marketing")] = {
    "name": "Content and Email Marketing",
    "verb": "run content and email",
    "blurb": "Patient education that ranks, and email that brings people back.",
    "intro": [
        "Patients research before they book, especially for anything elective or "
        "expensive. The practice that answers their questions honestly earns the "
        "appointment more often than the one that only advertises.",
        "Email does the other half. Most practices have a list of past patients "
        "they never contact, which is the cheapest appointment inventory they own.",
    ],
    "deliverables": [
        "Topic map built from real patient questions and search data",
        "Articles with a named clinical reviewer and a review date",
        "Recall and reactivation email sequences",
        "Pre-appointment education that reduces no-shows",
        "Internal links from every article to the relevant booking page",
    ],
    "metric": "organic enquiries and email attributed bookings",
    "angles": [
        ("Write what the front desk gets asked",
         "The questions staff answer on the phone twenty times a week are the "
         "ones the website should answer once, properly."),
        ("Review is a ranking signal and a trust signal",
         "A named clinician, their credentials and the date they reviewed the "
         "page affect both how readers judge it and how search engines treat it."),
        ("Email the list you already have",
         "Recall campaigns to past patients cost almost nothing and convert "
         "better than any acquisition channel."),
    ],
    "warning": "Content is a compounding investment with a slow start. Nothing "
               "here changes next month's numbers.",
    "decision": "Fund content when paid costs are climbing and you need an asset "
                "that keeps producing after the spend stops.",
    "question": "How much content does a {industry_singular_lower} actually need?",
    "answer": "Fewer pages than most agencies propose. Cover the conditions and "
              "procedures you want more of, the cost questions people are afraid "
              "to ask, and the practical logistics of a first visit. Twenty pages "
              "that fully answer a question beat a hundred that skim.",
}

S[("Healthcare", "ad-creative")] = {
    "name": "Ad Creative Production",
    "verb": "produce ad creative",
    "blurb": "Video and static ads produced in testable families, shot on site.",
    "intro": [
        "Creative decides most of a paid social account's performance. The "
        "targeting settings get the credit and the creative does the work.",
        "We shoot in the clinic with the actual practitioners where the category "
        "allows it. Real rooms and real faces outperform stock in every health "
        "account we have tested it in.",
    ],
    "deliverables": [
        "On-site production with practitioners and real facilities",
        "Creative families built around distinct patient motivations",
        "Compliant copy checked against platform health policy before shoot",
        "Static, video and vertical cuts delivered as matched sets",
        "Hook rate and cost per outcome reported per asset",
    ],
    "metric": "hook rate and cost per qualified enquiry",
    "angles": [
        ("Shoot the practitioner",
         "Health decisions are trust decisions. A clinician explaining something "
         "in their own words outperforms a produced brand film at a fraction of the cost."),
        ("One idea per family",
         "A family of six assets testing one motivation teaches you something "
         "when it loses. Six unrelated assets teach you nothing."),
        ("Compliance before the shoot",
         "Rewriting a script is cheap. Reshooting a day of footage because the "
         "claim will not clear review is not."),
    ],
    "warning": "Before-and-after imagery is prohibited or restricted in most "
               "health categories on Meta, which rules out the format many "
               "practices ask for first.",
    "decision": "Invest in production once a paid social account has enough spend "
                "to test properly. Below that, iterate on lower cost assets.",
    "question": "Do we need professional video for {industry_lower} ads?",
    "answer": "Not always. Clean phone footage of a practitioner answering a real "
              "patient question often outperforms polished production, because it "
              "reads as genuine. Invest in production for brand assets and "
              "anything you will run for a year.",
}

S[("Healthcare", "ecommerce-growth")] = {
    "name": "E-commerce Growth",
    "verb": "grow the online store",
    "blurb": "Online revenue for health brands selling products, not appointments.",
    "intro": [
        "Health and wellness brands selling physical product are running an "
        "ecommerce business with a regulatory overlay. The growth levers are the "
        "DTC ones, and the constraints are the health ones.",
        "We manage to blended efficiency across paid, email and marketplace, "
        "because a channel that reports a strong return while total revenue stays "
        "flat is claiming credit rather than creating it.",
    ],
    "deliverables": [
        "Paid social and search managed to blended marketing efficiency ratio",
        "Claims review so product copy clears both platform and regulator standards",
        "Email and SMS flows covering abandonment, replenishment and winback",
        "Subscription and repeat purchase economics built into the bidding",
        "Marketplace presence where the category supports it",
    ],
    "metric": "marketing efficiency ratio",
    "angles": [
        ("Manage to MER, not platform ROAS",
         "Every platform claims the same order. Marketing efficiency ratio is "
         "total revenue over total spend, and it cannot be double counted."),
        ("Repeat purchase changes the maths",
         "A supplement with a ninety day repurchase cycle can afford an "
         "acquisition cost that would sink a one-time purchase."),
        ("Claims are the constraint",
         "Health claims decide what you can say, which decides what creative can "
         "test. Get the claims list agreed before the creative brief."),
    ],
    "warning": "Health product claims are regulated separately from advertising "
               "policy. Clearing Meta review is not the same as being compliant "
               "with the regulator in your market.",
    "decision": "Treat this as DTC growth with a compliance layer. If the product "
                "also drives clinic visits, measure both or the channel looks worse than it is.",
    "question": "How do we grow {industry_lower} online without overstating claims?",
    "answer": "Sell the specifics instead of the outcome. Ingredients, sourcing, "
              "testing, what is in it and what is not. Brands that lead with "
              "verifiable detail clear review more reliably and hold up better "
              "when a regulator does look.",
}

# ============================================================================
# TRADES
# ============================================================================

S[("Trades", "digital-marketing")] = {
    "name": "Digital Marketing Agency",
    "verb": "run the full digital program",
    "blurb": "Every channel managed to one number: cost per booked job.",
    "intro": [
        "Trades marketing works when the channels stop being separate line items. "
        "Search catches the emergency, social builds recognition for the planned "
        "work, and the site converts both without making anyone hunt for a phone number.",
        "The program is judged on booked jobs and what each one cost to get. "
        "Everything else is diagnostic.",
    ],
    "deliverables": [
        "Channel plan with budget allocated by cost per booked job",
        "Service area built into the account structure, not the exclusion list",
        "Call tracking with recordings tied to campaign and keyword",
        "Job value fed back from the CRM into bidding",
        "One monthly report: spend, jobs, cost per job, by channel",
    ],
    "metric": "cost per booked job",
    "angles": [
        ("Geography is structure, not a filter",
         "Building the service area into how campaigns are organised is the "
         "difference between controlling where leads come from and filtering them after you paid."),
        ("Separate emergency from planned work",
         "An emergency call converts immediately at a high cost per click. A "
         "planned renovation takes weeks. Sharing a budget means the fast one starves the slow one."),
        ("Feed job value back",
         "Not all booked jobs are worth the same. Sending job value back into the "
         "ad platforms lets bidding chase the profitable ones."),
    ],
    "warning": "This only works if calls get answered. In most trades audits, "
               "missed calls during business hours cost more than the entire ad budget.",
    "decision": "Run the full program when several channels are live and "
                "unmeasured. If only Google Ads runs today, fix that account first.",
    "question": "How much should a {industry_singular_lower} spend to start?",
    "answer": "Enough to get about thirty conversions a month in your main "
              "service, or the bidding never learns. In most trades markets that "
              "is a few thousand a month. Below that, narrow to one service and "
              "one geography rather than spreading thin.",
}

S[("Trades", "google-ads")] = {
    "name": "Google Ads and PPC",
    "verb": "run Google Ads",
    "blurb": "Search and Local Services campaigns bid to cost per booked job.",
    "intro": [
        "Someone with a burst pipe is not browsing. They search, they call the "
        "first credible result, and the job is booked in four minutes. Search "
        "advertising is how you become that result.",
        "The account work is about precision. Service area, hours, match types "
        "and a negative list that keeps you out of auctions for work you do not want.",
    ],
    "deliverables": [
        "Campaigns split by service, urgency and geography",
        "Local Services Ads set up and managed alongside search where available",
        "Negative keyword wall reviewed weekly",
        "Call tracking with recordings scored for lead quality",
        "Ad scheduling matched to when your team can actually answer",
    ],
    "metric": "cost per booked job",
    "angles": [
        ("Bid by urgency",
         "Emergency terms convert on the first call and justify a high cost per "
         "click. Research terms need nurturing. Same budget, different jobs."),
        ("Local Services Ads sit above everything",
         "Where the category supports them, they appear above standard search "
         "results and charge per lead rather than per click. Different economics, run them separately."),
        ("Do not advertise outside your hours without a plan",
         "Paying for clicks at eleven at night when nobody answers is a "
         "measurable, avoidable loss. Either schedule around it or staff for it."),
    ],
    "warning": "Local Services Ads require licence and insurance verification "
               "that can take weeks. Start that process before you plan the launch date.",
    "decision": "Fund search first in almost every trade. Demand already exists "
                "and search is how it gets expressed.",
    "question": "What does a lead cost for {industry_lower}?",
    "answer": "It varies more by market than by trade. A competitive metro area "
              "can run several times a regional one for the same service. What "
              "matters is cost per booked job against average ticket. A lead cost "
              "that looks high can be cheap if the jobs are large.",
}

S[("Trades", "local-seo")] = {
    "name": "Local SEO",
    "verb": "run local SEO",
    "blurb": "Map pack visibility and rankings across every area you serve.",
    "intro": [
        "Most trades searches are local and a large share never leave the map "
        "results. Ranking there depends on proximity, profile completeness and "
        "review velocity, which is a different job from ranking in standard results.",
        "For businesses serving several areas, the work extends to location pages "
        "that are genuinely about those areas rather than the same page with the "
        "town name swapped.",
    ],
    "deliverables": [
        "Google Business Profile optimisation, categories, services and photos",
        "Review generation built into job completion",
        "Citation and directory cleanup for consistent business data",
        "Service area pages with real local substance",
        "Rank tracking by location rather than a single average position",
    ],
    "metric": "map pack visibility and calls from search",
    "angles": [
        ("Reviews are the lever",
         "Review count and recency move map rankings more than almost anything "
         "else you control. Ask at job completion, when satisfaction peaks."),
        ("Proximity is real and you cannot beat it everywhere",
         "You will not outrank a competitor located downtown for a downtown "
         "search. Target the areas you can genuinely win and be honest about the rest."),
        ("Thin location pages do more harm than good",
         "Twenty near-identical town pages get treated as low value. Fewer pages "
         "with real local detail work better."),
    ],
    "warning": "Fake reviews and keyword-stuffed business names get profiles "
               "suspended, and reinstatement is slow and uncertain. It is not a "
               "risk worth taking on the asset that produces your calls.",
    "decision": "Prioritise local SEO when you have a physical location or a "
                "tight service radius. For wide-area businesses, paid search covers ground faster.",
    "question": "How do we rank in more towns for {industry_lower}?",
    "answer": "Proximity limits how far a single location can rank. Real options "
              "are earning reviews that mention the work and the area, building "
              "location pages with genuine local content, and using paid search to "
              "cover the areas organic cannot reach.",
}

S[("Trades", "ai-search")] = {
    "name": "AEO, GEO and AI Search",
    "verb": "build visibility in AI answers",
    "blurb": "Being the contractor an AI assistant names when someone asks.",
    "intro": [
        "Homeowners now ask assistants who to call and what a job should cost. "
        "Those answers pull from sources the model trusts, and being one of them "
        "is a different exercise from ranking.",
        "Clear business data, straightforward answers to cost and process "
        "questions, and consistent information everywhere you appear.",
    ],
    "deliverables": [
        "Organisation and service schema so the business is machine readable",
        "Cost and process questions answered directly and specifically",
        "Consistent business data across directories and profiles",
        "Service area defined explicitly in structured data",
        "Monitoring of assistant answers for your main service questions",
    ],
    "metric": "citations in AI generated answers",
    "angles": [
        ("Answer the cost question honestly",
         "Pages that give a real range get quoted. Pages that say it depends and "
         "ask for a call get skipped by the model and the reader."),
        ("Structured data is how a machine reads you",
         "Service, area served and hours in schema removes the guesswork about "
         "what you do and where."),
        ("One version of your business everywhere",
         "Different phone numbers or addresses across directories make an entity "
         "ambiguous, and ambiguity loses citations."),
    ],
    "warning": "Measurement here is immature. Treat AI visibility as a hedge "
               "worth building, not a channel to forecast against.",
    "decision": "Do this after local SEO fundamentals are solid. Much of the same "
                "work feeds both, so the marginal cost is low once the base is in place.",
    "question": "Are people really using AI to find {industry_lower}?",
    "answer": "For research questions like what a job costs, what is involved and "
              "how to choose a contractor, yes and increasingly. For urgent work, "
              "people still search and call. Build for it, but do not move budget "
              "out of what is booking jobs today.",
}

S[("Trades", "paid-social")] = {
    "name": "Paid Social",
    "verb": "run paid social",
    "blurb": "Reaching homeowners before the project starts, not after.",
    "intro": [
        "Nobody searches for a kitchen renovation the day they decide to want "
        "one. The decision forms over months, and social is where it gets influenced.",
        "For planned and high-ticket work, social builds the demand that search "
        "later captures. For emergency work it rarely pays, and we will say so.",
    ],
    "deliverables": [
        "Creative built from real job footage, before and after",
        "Geographic and homeowner targeting matched to the service area",
        "Lead forms or landing pages with qualification built in",
        "Retargeting for people who viewed project pages",
        "Lead quality scored and fed back into optimisation",
    ],
    "metric": "cost per qualified enquiry",
    "angles": [
        ("Your job sites are the creative",
         "Before and after footage from real projects outperforms produced "
         "advertising in almost every trade we run. Film the work you are already doing."),
        ("Qualify in the ad, not after",
         "Naming the price range or project minimum in the creative reduces lead "
         "volume and raises the share worth calling."),
        ("Match the timeline",
         "Planned work has a long consideration window. Judging social on "
         "same-week bookings will make a working channel look broken."),
    ],
    "warning": "Lead form ads produce cheap leads of noticeably lower quality "
               "than landing page conversions. If your team's time is tight, the "
               "cheaper leads cost more.",
    "decision": "Fund social for planned, high-ticket and discretionary work. "
                "Skip it for emergency services where search does the job better.",
    "question": "Does paid social work for {industry_lower}?",
    "answer": "It works well for planned projects with a long decision window and "
              "a large ticket. It works poorly for urgent services people search "
              "for the moment they need them. If most of your revenue is "
              "emergency call-outs, put the budget in search.",
}

S[("Trades", "web-design")] = {
    "name": "Website Design and CRO",
    "verb": "build and optimise the website",
    "blurb": "Sites built so a homeowner can call you in two taps.",
    "intro": [
        "Trades websites fail in consistent ways. The phone number is not "
        "clickable on mobile, the service area is not stated, and there is no "
        "evidence the business has done the work before.",
        "Fixing those three things usually produces more booked jobs than a redesign would.",
    ],
    "deliverables": [
        "Click-to-call in the header on every page and every screen size",
        "Service area stated in plain text where people and machines can read it",
        "Project galleries with real photos from real jobs",
        "Quote request forms short enough to complete on a phone",
        "Page speed work so the site loads on a job site connection",
    ],
    "metric": "visit to enquiry conversion rate",
    "angles": [
        ("Mobile is the whole audience",
         "The overwhelming majority of trades traffic is on a phone, often "
         "outdoors on a weak signal. Design for that case first."),
        ("Show the work",
         "Photos of completed jobs, with the actual town named, do more for "
         "credibility than any amount of copy about quality and service."),
        ("Say where you work",
         "A visitor who cannot tell in five seconds whether you serve their area "
         "leaves. It is the most common conversion leak in the trades."),
    ],
    "warning": "A full redesign takes months during which nothing improves. If "
               "the current site works at all, fix the conversion basics first "
               "and decide about a rebuild afterwards.",
    "decision": "Rebuild when the site is not mobile-friendly or cannot be "
                "edited without a developer. Otherwise optimise.",
    "question": "What does a {industry_singular_lower} website actually need?",
    "answer": "A clickable phone number, the service area in plain text, photos "
              "of completed jobs, the services you offer on their own pages, and "
              "a short quote form. Everything beyond that is optional and most of it is decoration.",
}

S[("Trades", "crm-revops")] = {
    "name": "CRM and Revenue Operations",
    "verb": "build the CRM and follow-up systems",
    "blurb": "Making sure the leads you paid for actually get called back.",
    "intro": [
        "The most expensive problem in trades marketing is not lead cost. It is "
        "leads that arrive and never get called, because the office was busy and "
        "the email got buried.",
        "We build routing, alerts and follow up so an enquiry cannot go quiet, "
        "and stamp campaign data on the record so you can see which ads produce "
        "jobs rather than which produce leads.",
    ],
    "deliverables": [
        "Instant alerts to a named person, by text as well as email",
        "Missed call text-back so nobody who calls once is lost",
        "Automated follow up across the first hour, day and week",
        "Source, campaign and keyword written to every job record",
        "Quote follow up sequences for estimates that go quiet",
    ],
    "metric": "lead to booked job rate",
    "angles": [
        ("Missed call text-back pays for itself",
         "A large share of trades calls go unanswered during working hours. An "
         "automatic text within seconds recovers a meaningful portion of them."),
        ("Chase the quote",
         "Estimates that never get followed up are the single biggest source of "
         "lost revenue in most trades businesses. Two scheduled touches recover a real share."),
        ("Attribution at creation",
         "Writing the campaign onto the job record when the lead arrives is the "
         "only way to know later which ads produced profitable work."),
    ],
    "warning": "Automation reminds and routes. It does not sell. If nobody owns "
               "follow up, the system will document the leads you lose in more detail.",
    "decision": "Do this before increasing budget if lead to job conversion is "
                "under a third. It is cheaper than buying more leads.",
    "question": "We already have a CRM. Do we need another one for {industry_lower}?",
    "answer": "Almost certainly not. Most trades businesses have a capable system "
              "that is set up badly. Fixing routing, alerts and follow up in the "
              "tool you already pay for beats a migration that costs months and disrupts the office.",
}

S[("Trades", "content-marketing")] = {
    "name": "Content Marketing",
    "verb": "run content marketing",
    "blurb": "Answering the cost and process questions homeowners search for.",
    "intro": [
        "Homeowners research before they call, and they mostly research two "
        "things: what it costs and what is involved. Most trades websites answer neither.",
        "The business that publishes real numbers and a real process earns "
        "credibility before the first conversation, and gets called by people who "
        "already accept the price range.",
    ],
    "deliverables": [
        "Cost guides with real ranges and what moves the number",
        "Process explanations covering timeline, disruption and permits",
        "Comparison content between the options a homeowner is weighing",
        "Project case studies with photos, location and scope",
        "Internal links from every article to the relevant service page",
    ],
    "metric": "non-branded organic enquiries",
    "angles": [
        ("Publish the price range",
         "Most competitors will not. The ones who do get the call from people who "
         "have already accepted the number, which makes for better conversations and fewer wasted quotes."),
        ("Answer the permit and disruption questions",
         "How long will my kitchen be unusable is a real question that almost "
         "nobody answers in writing."),
        ("Local projects, named towns",
         "A case study that names the town and shows the work does more for local "
         "rankings than a generic service page."),
    ],
    "warning": "Content takes months to produce results. If the business needs "
               "work booked this month, fund search instead and start content alongside it.",
    "decision": "Invest here when paid costs are rising and you want an asset "
                "that keeps producing after the spend stops.",
    "question": "Should we publish prices for {industry_lower}?",
    "answer": "Publish a range with the factors that move it. It filters out "
              "people who were never going to proceed, it earns trust with people "
              "who were, and it is one of the strongest ranking and AI citation "
              "signals available in the trades.",
}

S[("Trades", "ad-creative")] = {
    "name": "Ad Creative Production",
    "verb": "produce ad creative",
    "blurb": "Job site footage cut into ads that test a specific idea.",
    "intro": [
        "The best trades creative is already happening on your job sites. It just "
        "needs someone to film it and cut it properly.",
        "We build creative in families, each testing one reason a homeowner "
        "chooses a contractor: the finish quality, the mess, the timeline, the price certainty.",
    ],
    "deliverables": [
        "Job site capture, before during and after",
        "Creative families each testing one buying motivation",
        "Vertical video cuts sized for every placement",
        "Crew and owner led pieces for credibility",
        "Hook rate and cost per enquiry reported per asset",
    ],
    "metric": "hook rate and cost per qualified enquiry",
    "angles": [
        ("Transformation is the hook",
         "Before and after holds attention in the trades better than any other "
         "format. It is also the easiest thing to capture on a job you are already doing."),
        ("The owner on camera works",
         "A crew lead explaining what they are about to do reads as real in a way "
         "produced advertising does not."),
        ("Film once, cut many",
         "One day on site produces months of assets if the capture is planned "
         "around the families you intend to test."),
    ],
    "warning": "Get customer permission in writing before filming a residential "
               "property. Retrofitting consent after the ad is running is a problem.",
    "decision": "Worth investing once paid social has enough budget to test "
                "properly. Below that, phone footage from the crew is enough.",
    "question": "Do we need a videographer for {industry_lower} ads?",
    "answer": "Not to start. Phone footage of real work, shot in landscape and "
              "vertical, tests the ideas at almost no cost. Bring in production "
              "once you know which angles work and want better versions of the winners.",
}

S[("Trades", "call-tracking")] = {
    "name": "Call Tracking and Attribution",
    "verb": "set up call tracking and attribution",
    "blurb": "Knowing which ad produced the call, and whether it became a job.",
    "intro": [
        "In the trades most enquiries arrive by phone, which means an account "
        "without call tracking is invisible where it matters most. Campaigns get "
        "cut for producing no form fills while they quietly produce the phone calls.",
        "We instrument calls at the keyword level, score them for quality, and "
        "tie the outcome back to the campaign that started it.",
    ],
    "deliverables": [
        "Dynamic number insertion so calls attribute to keyword and campaign",
        "Call recording with quality scoring against agreed criteria",
        "Conversion imported back into the ad platforms for bidding",
        "Missed call reporting by time of day and day of week",
        "Reporting that ties spend to booked jobs, not to calls",
    ],
    "metric": "cost per booked job",
    "angles": [
        ("Not every call is a lead",
         "Suppliers, wrong numbers and existing customers all ring the same "
         "number. Scoring calls before counting them keeps the reporting honest."),
        ("Feed booked jobs back into bidding",
         "Optimising to phone calls produces phone calls. Optimising to jobs that "
         "got booked produces jobs."),
        ("Missed call data is a management report",
         "Knowing you missed a share of calls between eleven and one, every day, "
         "is an operations finding worth more than most campaign optimisations."),
    ],
    "warning": "Call recording has consent requirements that vary by province and "
               "state. The announcement is not optional and we configure it correctly.",
    "decision": "Set this up before spending seriously on any channel that "
                "produces phone calls, which in the trades is all of them.",
    "question": "Do we really need call tracking for {industry_lower}?",
    "answer": "If most of your enquiries arrive by phone, yes, and it is not "
              "close. Without it you are optimising a phone-driven business on "
              "form fills, which means cutting the campaigns that work and funding the ones that do not.",
}

# ============================================================================
# DTC
# ============================================================================

S[("DTC", "performance-marketing")] = {
    "name": "Performance Marketing Agency",
    "verb": "run the full growth program",
    "blurb": "Paid, owned and marketplace managed to one blended efficiency number.",
    "intro": [
        "A DTC brand does not have a Meta problem or a Google problem. It has a "
        "contribution margin problem or it does not, and the channels are how you "
        "express the answer.",
        "We manage the whole mix to marketing efficiency ratio, then use channel "
        "detail to decide where the next dollar goes.",
    ],
    "deliverables": [
        "Blended MER target set from real contribution margin",
        "Paid social, search, shopping and marketplace run as one budget",
        "Email and SMS flows carrying the repeat purchase load",
        "Creative testing calendar with named hypotheses",
        "One report: revenue, spend, MER, new customer share",
    ],
    "metric": "marketing efficiency ratio",
    "angles": [
        ("Set the target from the margin",
         "The right MER is arithmetic, not ambition. Contribution margin after "
         "product, shipping and fees tells you what the business can afford to spend."),
        ("New customer share is the health metric",
         "A rising MER with a falling new customer share means you are "
         "harvesting the existing list. It looks like growth until the list runs out."),
        ("Email is not a channel, it is the margin",
         "Repeat purchase through owned channels is what makes the acquisition "
         "economics work. Treating it as an afterthought caps the whole program."),
    ],
    "warning": "If contribution margin after shipping and payment fees is under "
               "about thirty percent, no amount of media management fixes the "
               "business. The product economics have to change first.",
    "decision": "Take the full program when several channels run and platform "
                "numbers disagree with the bank account.",
    "question": "What MER should a {industry_singular_lower} brand target?",
    "answer": "Work backwards from contribution margin. If you keep thirty five "
              "cents on the dollar after product, shipping and fees, you break "
              "even around a MER of three and need meaningfully more than that to "
              "fund overhead and profit. Any target quoted without your margin is a guess.",
}

S[("DTC", "paid-social")] = {
    "name": "Paid Social",
    "verb": "run paid social",
    "blurb": "Meta, TikTok and Pinterest run as a creative testing operation.",
    "intro": [
        "Paid social for DTC is a creative business wearing a media buying "
        "costume. Account structure matters for a week and creative matters forever.",
        "We run consolidated campaigns, let the platform find the buyer, and "
        "spend the effort on producing enough distinct ideas to keep the account fed.",
    ],
    "deliverables": [
        "Consolidated campaign structure built for algorithmic learning",
        "Creative testing calendar with a named hypothesis per family",
        "Creator and user generated content pipeline",
        "Server side conversion tracking to survive signal loss",
        "Incrementality checks so the channel is not just claiming existing demand",
    ],
    "metric": "blended new customer acquisition cost",
    "angles": [
        ("Creative volume is the constraint",
         "Most accounts plateau because they run out of ideas, not because of "
         "targeting. Plan production capacity before you plan budget increases."),
        ("Creator content usually beats studio",
         "On one Consultus Digital account, creator video ran a 248 percent "
         "higher click-through rate than the equivalent static. It is not universal, but it is common."),
        ("Judge on blended, not platform reported",
         "Meta will report a return that assumes it caused every sale it touched. "
         "Check it against total revenue before believing it."),
    ],
    "warning": "Creative fatigue in a scaled account can arrive inside ten days. "
               "If production cannot keep pace, budget increases just buy the same "
               "ads shown more often to the same people.",
    "decision": "Lead with paid social when the product is visual, impulse-friendly "
                "or new to the market. Lead with search when people already know the category and search for it.",
    "question": "How much creative does {industry_lower} need per month?",
    "answer": "At modest spend, a handful of new concepts a month keeps an "
              "account healthy. Scaled accounts need several times that. The "
              "signal to watch is frequency and hook rate. When both move the "
              "wrong way at once, you are out of ideas rather than out of audience.",
}

S[("DTC", "paid-search-shopping")] = {
    "name": "Paid Search and Shopping",
    "verb": "run paid search and shopping",
    "blurb": "Search, Shopping and Performance Max built on a clean product feed.",
    "intro": [
        "Shopping performance is a feed problem before it is a bidding problem. "
        "Titles, attributes and image quality decide which auctions you enter at all.",
        "We rebuild the feed first, then structure campaigns so branded search is "
        "never credited with demand it did not create.",
    ],
    "deliverables": [
        "Product feed rebuilt with search-led titles and complete attributes",
        "Shopping and Performance Max structured by margin and intent",
        "Branded search separated so reporting stays honest",
        "Search term and placement exclusions maintained weekly",
        "Feed level margin data so bidding chases profit, not revenue",
    ],
    "metric": "return on ad spend at the product level",
    "angles": [
        ("Fix the feed first",
         "Titles that lead with the search phrase rather than the brand name "
         "change which auctions you enter. Nothing else in the channel moves as much."),
        ("Separate branded search",
         "Branded terms convert at a rate that flatters any campaign they sit in. "
         "Split them or you will keep over-crediting whichever campaign holds them."),
        ("Performance Max needs guardrails",
         "It will find cheap traffic wherever it exists, including your own "
         "branded searches. Exclusions and feed segmentation are how you keep it useful."),
    ],
    "warning": "Performance Max reporting is deliberately limited. If you need to "
               "know exactly where spend went, keep a portion of budget in "
               "standard Shopping and Search campaigns.",
    "decision": "Fund search and shopping when people already search for your "
                "product category by name. For a genuinely new product, build demand on social first.",
    "question": "Is Performance Max worth it for {industry_lower}?",
    "answer": "Usually yes, with guardrails. It performs well on a clean feed and "
              "a decent conversion volume. Run it alongside standard campaigns "
              "rather than replacing them, exclude branded search, and check that "
              "it is finding new customers rather than harvesting people who were already buying.",
}

S[("DTC", "seo")] = {
    "name": "E-commerce SEO",
    "verb": "run ecommerce SEO",
    "blurb": "Category and product pages built to rank, on a site structure that scales.",
    "intro": [
        "Ecommerce SEO lives and dies on site architecture. Category pages carry "
        "the commercial rankings, product pages carry the long tail, and faceted "
        "navigation quietly generates thousands of near-duplicate URLs if nobody controls it.",
        "The content job is making category pages worth ranking rather than a "
        "grid of products with a sentence above it.",
    ],
    "deliverables": [
        "Category page content built around how people actually search",
        "Faceted navigation and parameter handling so crawl budget is not wasted",
        "Product schema, review markup and availability data",
        "Internal linking from content into the commercial pages",
        "Technical work on speed, indexation and duplicate content",
    ],
    "metric": "non-branded organic revenue",
    "angles": [
        ("Category pages are the commercial asset",
         "They target the terms with buying intent and volume. A product page "
         "ranks for one thing. A well-built category page ranks for many."),
        ("Control the facets",
         "Filter combinations can generate tens of thousands of crawlable URLs. "
         "Left alone, they eat crawl budget and split ranking signals."),
        ("Content that survives a product going out of stock",
         "Build the ranking asset at category level so a discontinued product "
         "does not take a ranking with it."),
    ],
    "warning": "Ecommerce SEO takes six to twelve months to move revenue "
               "meaningfully. It is the right investment and the wrong answer to a quarter that is behind.",
    "decision": "Invest when paid acquisition costs are rising and you need "
                "revenue that does not stop when the budget does.",
    "question": "Can {industry_lower} rank against the big marketplaces?",
    "answer": "Not for broad category terms, usually. You can win specific, "
              "detailed and long-tail searches where a specialist page answers "
              "better than a marketplace listing. That is where the achievable revenue is.",
}

S[("DTC", "ai-search")] = {
    "name": "AEO, GEO and AI Search",
    "verb": "build visibility in AI answers",
    "blurb": "Being the product an assistant recommends when asked for one.",
    "intro": [
        "Shoppers are starting to ask assistants which product to buy and getting "
        "a shortlist back. Appearing on that shortlist depends on structured "
        "product data, third party corroboration and content a model can quote.",
        "It is early, the measurement is partial, and the underlying work "
        "overlaps heavily with SEO you should be doing anyway.",
    ],
    "deliverables": [
        "Product and organisation schema with complete attributes",
        "Comparison and buying guide content built for extraction",
        "Review and rating data exposed in machine readable form",
        "Consistent product information across marketplaces and retail partners",
        "Monitoring of assistant recommendations in your category",
    ],
    "metric": "share of assistant recommendations",
    "angles": [
        ("Third party corroboration matters",
         "Models weigh independent sources heavily. Reviews, press and retailer "
         "listings influence recommendations more than your own product copy does."),
        ("Structured attributes decide inclusion",
         "Material, size, compatibility, certification. The specifics a shopper "
         "filters on are the specifics a model matches on."),
        ("Write the comparison yourself",
         "Buying guides that fairly compare options, including alternatives to "
         "your own product, get cited more than pages that only sell."),
    ],
    "warning": "There is no reliable way to measure assistant-driven revenue "
               "today. Fund it from the SEO budget as an extension, not as a separate line with a forecast.",
    "decision": "Do it once product data and technical SEO are clean. Most of the "
                "work serves both, so the extra cost is small.",
    "question": "How do we get {industry_lower} recommended by AI assistants?",
    "answer": "Complete structured product data, genuine third party reviews, and "
              "content that compares options honestly. Models favour sources that "
              "read as independent and specific. There is no way to buy placement, which is the point.",
}

S[("DTC", "performance-creative")] = {
    "name": "Performance Creative",
    "verb": "produce performance creative",
    "blurb": "Creator, studio and motion assets produced to a testing calendar.",
    "intro": [
        "Creative is the largest performance variable in DTC and the one most "
        "brands under-resource. Accounts do not usually plateau on targeting. They "
        "plateau on ideas.",
        "We run production as an operation: a hypothesis backlog, a shoot "
        "calendar and a reporting loop that tells you which idea won, not just which file did.",
    ],
    "deliverables": [
        "Creator sourcing, briefing and rights management",
        "Studio and motion assets in matched families",
        "Hook, format and offer tested as separate variables",
        "Hook rate, hold rate and cost per acquisition per asset",
        "Winning angles pushed into email, landing pages and search copy",
    ],
    "metric": "hook rate and cost per acquisition",
    "angles": [
        ("Test the idea, not the file",
         "Changing the hook, the format and the offer at once produces a winner "
         "you cannot learn from. Isolate variables or the testing is theatre."),
        ("Creator content earns attention",
         "Content that looks like the feed it appears in holds attention longer "
         "than content that looks like an advertisement."),
        ("Winners go everywhere",
         "The hook that wins on paid social is the subject line that wins in "
         "email and the headline that wins on the landing page."),
    ],
    "warning": "Creator rights are usually time-limited. Running an asset past "
               "the licence term is a legal exposure that is easy to avoid and easy to forget.",
    "decision": "Scale production when hook rate declines while frequency rises. "
                "That combination means the account needs ideas, not budget.",
    "question": "How many creators does {industry_lower} need?",
    "answer": "Fewer than most brands assume, working more often. A handful of "
              "creators who understand the product and can turn around new angles "
              "monthly outperform a rotating cast producing one video each.",
}

S[("DTC", "shopify-cro")] = {
    "name": "Shopify Development and CRO",
    "verb": "build and optimise the store",
    "blurb": "Store builds and conversion work on Shopify and comparable platforms.",
    "intro": [
        "A store that converts at two percent instead of three needs fifty "
        "percent more traffic for the same revenue. Conversion work is the "
        "cheapest growth available to most brands and the least glamorous.",
        "We work on the pages that carry the traffic: product detail, cart and "
        "checkout. Homepage redesigns rarely move revenue.",
    ],
    "deliverables": [
        "Product page work on imagery, proof, options and delivery clarity",
        "Cart and checkout friction removal",
        "Site speed work including app audit and theme cleanup",
        "Test roadmap with hypothesis, metric and minimum sample size",
        "Post-purchase flow for repeat rate and average order value",
    ],
    "metric": "conversion rate and revenue per session",
    "angles": [
        ("Audit the apps",
         "Most established Shopify stores carry apps nobody uses that still load "
         "scripts on every page. Removing them is often the fastest speed win available."),
        ("Delivery clarity converts",
         "Shipping cost and delivery date shown on the product page, not "
         "discovered at checkout, is one of the most reliable conversion gains in ecommerce."),
        ("Test where the traffic is",
         "A winning test on a page with two percent of sessions is a rounding "
         "error. Run tests where the volume is."),
    ],
    "warning": "Under roughly a thousand monthly conversions, most tests will not "
               "reach significance in a reasonable window. Fix the obvious things "
               "and stop calling it testing.",
    "decision": "Prioritise CRO over more traffic when conversion rate sits below "
                "the category norm. Buying traffic into a leaking store is the expensive path.",
    "question": "What converts best on a {industry_singular_lower} product page?",
    "answer": "Clear pricing including shipping, a delivery estimate, imagery "
              "that shows scale and use, reviews near the buy button, and an "
              "obvious answer to the returns question. In that order, before anything else gets tested.",
}

S[("DTC", "email-sms")] = {
    "name": "Email and SMS",
    "verb": "run email and SMS",
    "blurb": "Owned channels carrying the repeat purchase that makes acquisition work.",
    "intro": [
        "Acquisition economics only work if customers come back. Email and SMS "
        "are how that happens, and they are the only channels where the audience "
        "cannot be taken away by a platform policy change.",
        "The flows do most of the work. Campaigns are the visible part and the "
        "smaller share of revenue in almost every account we audit.",
    ],
    "deliverables": [
        "Core flows: welcome, abandonment, post-purchase, replenishment, winback",
        "SMS for time sensitive moments, sized so it does not burn the list",
        "Segmentation by purchase behaviour rather than demographics",
        "List growth built into the site without wrecking conversion rate",
        "Revenue reported by flow and campaign against total revenue",
    ],
    "metric": "owned channel revenue share",
    "angles": [
        ("Flows beat campaigns",
         "Automated flows typically produce the majority of owned channel "
         "revenue while taking a fraction of the ongoing effort."),
        ("Replenishment timing is arithmetic",
         "If the product lasts sixty days, the reminder goes at forty five. Most "
         "brands guess this and leave revenue on the table."),
        ("SMS is a scarce resource",
         "Text messages get read and get unsubscribed. Save them for genuine "
         "urgency or the list degrades fast."),
    ],
    "warning": "Aggressive discounting through email trains a list to wait for "
               "the next sale. Short term revenue, long term margin problem.",
    "decision": "Build flows before campaigns, and before increasing acquisition "
                "spend. Sending more traffic to a brand with no retention is expensive.",
    "question": "What owned channel revenue share should {industry_lower} expect?",
    "answer": "For a brand with genuine repeat purchase, owned channels commonly "
              "carry somewhere between a fifth and a third of total revenue. Well "
              "under that usually means the flows are missing rather than the audience being wrong.",
}

S[("DTC", "analytics")] = {
    "name": "Analytics and Attribution",
    "verb": "build measurement and attribution",
    "blurb": "One number the whole business trusts, across platforms that disagree.",
    "intro": [
        "Add up what every platform reports and the total exceeds what the "
        "business actually sold. Budget decisions made on those numbers move money "
        "toward whichever channel reports most aggressively.",
        "We build to blended measurement, reconcile platform claims against real "
        "orders, and use incrementality testing where the stakes justify it.",
    ],
    "deliverables": [
        "Blended MER reporting across every channel and platform",
        "Server side tracking to reduce signal loss",
        "Reconciliation between platform reported and actual orders",
        "New versus returning customer split in every view",
        "Incrementality tests on the channels with the largest claims",
    ],
    "metric": "blended marketing efficiency ratio",
    "angles": [
        ("Blended first, channel second",
         "Set the budget on blended efficiency. Use channel detail to decide "
         "where the marginal dollar goes, not whether to spend it."),
        ("Test incrementality on branded search",
         "Branded search reports beautifully and often captures demand that "
         "would have converted anyway. A holdout test tells you how much."),
        ("New customer cost is the real number",
         "Blended acquisition cost across all customers hides the difference between "
         "growing and harvesting the existing base. Split it."),
    ],
    "warning": "Perfect attribution is not available any more. Aim for "
               "directionally correct and consistently measured, then stop "
               "arguing about last click.",
    "decision": "Do this before scaling spend. Scaling on numbers you do not "
                "trust just makes the mistake larger.",
    "question": "Why do our platform numbers not match our Shopify revenue for {industry_lower}?",
    "answer": "Because each platform counts every sale it touched, using "
              "different attribution windows, and several of them touched the same "
              "sale. The fix is not to reconcile them individually. Manage to "
              "blended efficiency and treat platform numbers as directional.",
}

S[("DTC", "marketplace-marketing")] = {
    "name": "Marketplace Marketing",
    "verb": "run marketplace marketing",
    "blurb": "Amazon and marketplace growth measured on ACOS, TACOS and total share.",
    "intro": [
        "Marketplaces are where a large share of product searches start, and "
        "where a brand can lose control of its own listing to a reseller.",
        "The work is listing quality, advertising structure and defending your "
        "own branded terms, measured on total advertising cost of sale rather than "
        "the ad account alone.",
    ],
    "deliverables": [
        "Listing optimisation: titles, bullets, imagery and backend terms",
        "Sponsored Products, Brands and Display campaign structure",
        "Brand registry, storefront and A+ content",
        "Defence of branded search against competitors and resellers",
        "TACOS reporting so ad spend is judged against total marketplace revenue",
    ],
    "metric": "total advertising cost of sale",
    "angles": [
        ("The listing is the conversion rate",
         "Marketplace advertising cannot fix a listing that does not convert. "
         "Images and bullets first, bids second."),
        ("Defend your brand terms",
         "Competitors bid on your brand name. Not defending it means paying "
         "later to win back customers who were already looking for you."),
        ("TACOS over ACOS",
         "Advertising cost of sale only measures the ads. Total advertising cost "
         "of sale measures the whole channel, including the organic sales the ads helped produce."),
    ],
    "warning": "Marketplace growth can cannibalise your own store, where margins "
               "are better. Worth doing, worth measuring across both.",
    "decision": "Sell on marketplaces when your category has real search volume "
                "there and your margins survive the fees. Otherwise it is revenue that costs more than it returns.",
    "question": "Should {industry_lower} sell on Amazon as well as our own store?",
    "answer": "If your category gets meaningful search volume there, usually yes, "
              "because customers will find your products listed by someone "
              "regardless. Owning the listing is better than a reseller owning it. "
              "Model the margin after fees and shipping before committing.",
}

# ============================================================================
# PROFESSIONAL SERVICES
# ============================================================================

S[("Professional Services", "digital-marketing")] = {
    "name": "Digital Marketing Agency",
    "verb": "run the full digital program",
    "blurb": "The whole program, measured to signed matters rather than enquiries.",
    "intro": [
        "Professional services firms rarely have a lead volume problem. They have "
        "a lead quality problem and a response time problem, and more advertising "
        "makes both more expensive.",
        "We build the program around the matter or mandate you actually want, "
        "then measure the cost of getting one signed.",
    ],
    "deliverables": [
        "Channel plan weighted to the matter types worth the most",
        "Intake process reviewed and instrumented before spend increases",
        "CRM configured so every enquiry carries its campaign source",
        "Content and search built around the questions clients ask before hiring",
        "Reporting to cost per signed matter, not cost per enquiry",
    ],
    "metric": "cost per signed matter",
    "angles": [
        ("Qualify before you scale",
         "Doubling enquiries in a firm that cannot triage them produces "
         "frustration and no revenue. Fix triage first."),
        ("Not all matters are worth the same",
         "Weighting the program toward the matter types with real value changes "
         "which keywords, which content and which campaigns get funded."),
        ("Response time beats everything",
         "An enquiry answered in five minutes converts several times better than "
         "one answered tomorrow. No campaign change competes with that."),
    ],
    "warning": "Professional services buying cycles are long. A program judged on "
               "thirty days will be cancelled just as the pipeline starts to fill.",
    "decision": "Take the full program when multiple channels run unmeasured, or "
                "when the firm is growing past what referrals can supply.",
    "question": "How long until we see signed matters from this for our {industry_singular_lower}?",
    "answer": "Enquiries arrive within weeks. Signed matters follow the length of "
              "your sales cycle, which in most professional services is one to six "
              "months. We report leading indicators weekly and set the real review at ninety days.",
}

S[("Professional Services", "paid-search")] = {
    "name": "Paid Search and PPC",
    "verb": "run paid search",
    "blurb": "High intent search campaigns bid to cost per qualified enquiry.",
    "intro": [
        "Search advertising in professional services is expensive and worth it, "
        "because the person searching has a problem they have decided to pay to solve.",
        "The discipline is in what you refuse to bid on. Broad category terms "
        "bring students, competitors and people looking for free advice.",
    ],
    "deliverables": [
        "Campaigns split by matter type and value",
        "Negative keyword wall against free advice and job seeker traffic",
        "Ad copy written to the standard your regulator applies",
        "Call tracking with recordings scored for matter quality",
        "Bidding against qualified enquiries, not raw form fills",
    ],
    "metric": "cost per qualified enquiry",
    "angles": [
        ("Bid on the problem, not the profession",
         "Someone searching for the profession is researching. Someone searching "
         "for their specific problem is ready to hire."),
        ("Build the negative list before launch",
         "Free, template, DIY, salary, jobs. In professional services the "
         "negative list is doing more work than the keyword list."),
        ("Score the calls",
         "Optimising to call volume in a category where half the calls are "
         "unqualified means paying to increase the half you do not want."),
    ],
    "warning": "Costs per click in competitive legal and financial categories are "
               "among the highest in advertising. Enter with a real budget or not "
               "at all, because a thin budget in a expensive auction buys nothing useful.",
    "decision": "Fund search when people actively search for the problem you "
                "solve. For relationship-led work with no search demand, content and reputation matter more.",
    "question": "Is paid search too expensive for {industry_lower}?",
    "answer": "Clicks are expensive and that is the wrong frame. If a signed "
              "matter is worth several thousand and you sign a reasonable share of "
              "qualified enquiries, an expensive click is still profitable. Model "
              "it on matter value before deciding.",
}

S[("Professional Services", "seo")] = {
    "name": "SEO",
    "verb": "run search engine optimization",
    "blurb": "Organic authority for the problems your best clients search.",
    "intro": [
        "In professional services, organic search is the channel that compounds "
        "and the one competitors cannot outbid you for. It is also the slowest.",
        "The work is authority: content that demonstrates expertise on the "
        "specific problems you handle, a technically sound site, and the trust "
        "signals that regulated categories are held to.",
    ],
    "deliverables": [
        "Technical audit covering crawl, speed, indexation and structured data",
        "Practice area pages built to rank rather than to describe",
        "Question-led content answering what clients ask before hiring",
        "Author markup with real credentials and professional qualifications",
        "Internal linking from content to the practice area pages",
    ],
    "metric": "non-branded organic enquiries",
    "angles": [
        ("Practice area pages carry the rankings",
         "They target the commercial terms. Articles support them and link into "
         "them. Firms that publish articles without strong practice area pages "
         "get traffic that does not convert."),
        ("Named authors, real credentials",
         "In categories where expertise and trust are assessed, a named "
         "professional with verifiable credentials on the page is a ranking factor and a conversion factor."),
        ("Write what clients ask",
         "The questions asked in the first ten minutes of a consultation are the "
         "content brief. They are also what people search."),
    ],
    "warning": "Organic results in competitive professional categories take six "
               "to twelve months. It is the right long term investment and the "
               "wrong answer to an urgent pipeline gap.",
    "decision": "Prioritise organic when paid costs are high, which in "
                "professional services is almost always.",
    "question": "Can a smaller firm rank for {industry_lower} terms?",
    "answer": "Not against national firms for the broadest terms. You can win "
              "specific problem searches, local variations and the detailed "
              "questions the large firms write about generically. That is usually "
              "where the better matters are anyway.",
}

S[("Professional Services", "ai-search")] = {
    "name": "AEO, GEO and AI Search",
    "verb": "build visibility in AI answers",
    "blurb": "Being cited when someone asks an assistant how to handle their problem.",
    "intro": [
        "People now describe their situation to an assistant and get an "
        "explanation with sources. For professional services, that is the research "
        "step that used to be several searches and a few articles.",
        "Being one of the cited sources depends on clear expertise signals, "
        "structured information and answers a model can quote without hedging.",
    ],
    "deliverables": [
        "Organisation and professional service schema",
        "Question-and-answer content structured for extraction",
        "Author markup carrying real professional credentials",
        "Consistent firm data across directories and professional listings",
        "Monitoring of assistant answers for your main practice areas",
    ],
    "metric": "citations in AI generated answers",
    "angles": [
        ("Credentials are the differentiator",
         "In regulated professions, verifiable qualifications on the page affect "
         "whether a model treats a source as authoritative."),
        ("Answer the process question",
         "How long does this take, what does it cost, what happens first. Direct "
         "answers get quoted. Invitations to call do not."),
        ("Jurisdiction matters and models know it",
         "Content that states which jurisdiction it applies to is more likely to "
         "be cited correctly and less likely to be cited wrongly."),
    ],
    "warning": "Assistants sometimes summarise regulated advice inaccurately. "
               "Writing clearly and stating jurisdiction reduces the chance of "
               "being cited in a way you would not stand behind.",
    "decision": "Build once core SEO is in place. The work overlaps, so the "
                "incremental cost is small.",
    "question": "Should {industry_lower} worry about AI answering client questions?",
    "answer": "The research step was already happening on search. What changes is "
              "that the answer is assembled rather than clicked. Firms cited in "
              "that answer still get the enquiry, and the people who arrive are "
              "better informed. Being absent from it is the risk.",
}

S[("Professional Services", "paid-social")] = {
    "name": "Paid Social",
    "verb": "run paid social",
    "blurb": "LinkedIn and Meta used for the matters people do not search for.",
    "intro": [
        "Some professional services problems get searched. Others get avoided "
        "until something forces the issue. Social advertising reaches the second group.",
        "It also reaches people by role and firm in a way search cannot, which "
        "matters for B2B mandates where you know exactly who the buyer is.",
    ],
    "deliverables": [
        "LinkedIn targeting by role, seniority, firm size and industry",
        "Meta campaigns for consumer-facing practice areas",
        "Creative that leads with the problem, not the firm",
        "Landing pages matched to the specific angle",
        "Lead quality scored and fed back into optimisation",
    ],
    "metric": "cost per qualified enquiry",
    "angles": [
        ("LinkedIn is expensive and precise",
         "Cost per click is high. When you can name the exact job title at the "
         "exact firm size, the precision can justify it. When you cannot, it rarely does."),
        ("Lead with the problem",
         "Creative that names a situation the viewer recognises outperforms "
         "creative about the firm's credentials."),
        ("Expect a longer path",
         "Social enquiries in professional services need nurturing. Budget for "
         "the follow up sequence, not just the ads."),
    ],
    "warning": "Regulated professions face restrictions on comparative claims, "
               "guarantees and testimonials in advertising. The rules come from "
               "your professional body, not the platform, and they are stricter.",
    "decision": "Use social for practice areas with no search demand, or B2B "
                "mandates with a definable buyer. For high-intent consumer matters, search is more efficient.",
    "question": "Does LinkedIn advertising work for {industry_lower}?",
    "answer": "It works when you can define the buyer precisely by role, firm "
              "size and industry, and the mandate is worth enough to absorb a high "
              "cost per click. For broad consumer-facing work it is usually the wrong platform.",
}

S[("Professional Services", "web-design")] = {
    "name": "Website Design and CRO",
    "verb": "build and optimise the website",
    "blurb": "Firm websites that turn research into a booked consultation.",
    "intro": [
        "Professional services websites are usually built to satisfy the "
        "partnership rather than the prospective client. The result is a site "
        "about the firm rather than about the problem the visitor arrived with.",
        "We build around the practice areas that matter commercially, with the "
        "proof and process a hesitant buyer needs before they will make contact.",
    ],
    "deliverables": [
        "Practice area pages structured around client problems",
        "Professional profiles with credentials, matters and real detail",
        "Consultation booking with the fewest steps possible",
        "Case results and testimonials within regulatory limits",
        "Speed, accessibility and mobile work on the templates that matter",
    ],
    "metric": "visit to consultation conversion rate",
    "angles": [
        ("Write for the client, not the partnership",
         "The visitor has a problem. A homepage about the firm's founding year "
         "does not address it."),
        ("Professional profiles convert",
         "In relationship-led categories, the individual profile is often the "
         "highest converting page on the site. Most firms treat it as a directory entry."),
        ("Explain the process and the cost",
         "The two things people most want to know before contacting a "
         "professional are what happens next and what it will cost. Answering both raises enquiry rates."),
    ],
    "warning": "Testimonials and case results are restricted for many regulated "
               "professions. What is permitted varies by jurisdiction and body, "
               "and we build to your specific rules.",
    "decision": "Rebuild when the site cannot be updated without a developer or "
                "fails on mobile. Otherwise fix the practice area pages and the booking flow first.",
    "question": "What matters most on a {industry_singular_lower} website?",
    "answer": "Practice area pages that describe the client's problem, "
              "professional profiles with real substance, a clear explanation of "
              "process and cost, and an easy way to book. Firm history and office "
              "photography matter far less than most firms assume.",
}

S[("Professional Services", "crm-revops")] = {
    "name": "CRM and Revenue Operations",
    "verb": "build the CRM and intake systems",
    "blurb": "Intake, routing and pipeline built so enquiries become signed matters.",
    "intro": [
        "Most firms lose more revenue in intake than they would gain from any "
        "campaign improvement. Enquiries land in a shared inbox, get picked up "
        "hours later, and the client has already engaged someone else.",
        "We build routing with named owners and response targets, then stamp "
        "campaign data on every record so the firm can finally see which marketing "
        "produces signed work.",
    ],
    "deliverables": [
        "Intake routing by matter type with a named owner and response target",
        "Conflict check and qualification built into the first touch",
        "Pipeline stages that match how the firm actually converts",
        "Source, campaign and landing page written to every record",
        "Reporting from first click through to signed matter",
    ],
    "metric": "enquiry to signed matter rate",
    "angles": [
        ("Somebody has to own intake",
         "A shared inbox is not an owner. The single highest return change in "
         "most firms is naming a person and a response time."),
        ("Qualify early and honestly",
         "Telling someone quickly that you are not the right firm protects "
         "everyone's time and produces referrals."),
        ("Attribution has to reach the matter",
         "Tracking that stops at the enquiry cannot tell you which campaigns "
         "produce the matters worth having."),
    ],
    "warning": "Conflict checks and privilege requirements constrain what can be "
               "stored and automated. We build inside those constraints rather than around them.",
    "decision": "Do this before increasing budget if enquiry to matter conversion "
                "is below what the partners expect. It is cheaper than buying more enquiries.",
    "question": "What CRM should a {industry_singular_lower} use?",
    "answer": "Usually the one you already have, configured properly. Practice "
              "management systems handle matters well and enquiries badly, so the "
              "gap is normally at the front. We fix the intake layer before "
              "recommending anyone replace a system the firm runs on.",
}

S[("Professional Services", "thought-leadership")] = {
    "name": "Thought Leadership and Content",
    "verb": "run thought leadership and content",
    "blurb": "Writing that demonstrates judgment instead of announcing expertise.",
    "intro": [
        "Every firm claims expertise. Very few demonstrate it in writing, which "
        "is why the ones that do get remembered and referred.",
        "Useful content in professional services takes a position. It says what "
        "the writer would do, what they would avoid and where the real risk sits.",
    ],
    "deliverables": [
        "Topic map built from client questions and regulatory change",
        "Articles that take a defensible position rather than surveying options",
        "Named authors with verifiable professional credentials",
        "Commentary on regulatory and legislative developments in your area",
        "Distribution through email and professional networks, not just publishing",
    ],
    "metric": "organic enquiries and referral influence",
    "angles": [
        ("Take a position",
         "Content that surveys every option helps nobody decide. The value is "
         "in the judgment about which option applies when."),
        ("Write about change",
         "Regulatory and legislative change creates urgent, searchable questions "
         "with a short window and very little competing content."),
        ("Distribution is half the work",
         "An article nobody sends anywhere is a page. An article that reaches the "
         "right hundred inboxes is a business development asset."),
    ],
    "warning": "Content that gives specific advice on a specific situation "
               "creates professional exposure. Write about principles and process, "
               "with the caveats your regulator expects.",
    "decision": "Invest here when the firm competes on expertise rather than "
                "price or convenience, which describes most professional services.",
    "question": "Who should write content for a {industry_singular_lower}?",
    "answer": "The professionals doing the work, edited by someone who can write. "
              "Ghostwritten content with a partner's name on it reads as generic "
              "because it is. A thirty minute recorded conversation with the "
              "practitioner produces better material than a brief ever will.",
}

S[("Professional Services", "ad-creative")] = {
    "name": "Ad Creative Production",
    "verb": "produce ad creative",
    "blurb": "Credible creative for categories where trust decides the enquiry.",
    "intro": [
        "Professional services creative has a narrower path than consumer "
        "advertising. It has to establish credibility fast without making claims "
        "the regulator will object to.",
        "What works is the professional explaining something useful. It is "
        "cheaper to produce than brand advertising and it performs better.",
    ],
    "deliverables": [
        "Practitioner-led video answering real client questions",
        "Creative families built around distinct client situations",
        "Copy reviewed against professional advertising standards before production",
        "Static and video assets sized for each placement",
        "Hook rate and enquiry quality reported per asset",
    ],
    "metric": "hook rate and cost per qualified enquiry",
    "angles": [
        ("Put the professional on camera",
         "Trust is the buying decision. A practitioner explaining something "
         "clearly does more than production value."),
        ("Answer a question, do not pitch",
         "Creative that teaches something useful in thirty seconds earns "
         "attention. Creative that lists credentials does not."),
        ("Compliance review before the shoot",
         "Rewriting a script costs nothing. Reshooting because a claim will not "
         "clear review costs a day."),
    ],
    "warning": "Testimonials, comparative claims and outcome references are "
               "restricted for most regulated professions and the rules differ by jurisdiction.",
    "decision": "Invest once paid social has enough budget to test. Below that, "
                "recorded video from a phone is sufficient to find the angle.",
    "question": "What creative works for {industry_lower}?",
    "answer": "A practitioner answering the question clients actually ask, filmed "
              "simply, with no claim about outcomes. It clears review, it "
              "establishes competence, and it consistently outperforms polished brand work in this category.",
}

S[("Professional Services", "analytics")] = {
    "name": "Pipeline Analytics and Attribution",
    "verb": "build pipeline analytics and attribution",
    "blurb": "Tracking from first click through to signed matter and matter value.",
    "intro": [
        "Firms measure enquiries because enquiries are easy to count. The "
        "question that matters is which marketing produced the matters worth having.",
        "That requires the CRM and the ad accounts to share a definition of what "
        "happened, which is a build rather than a report.",
    ],
    "deliverables": [
        "Event tracking tied to enquiry, consultation and signed matter",
        "Matter type and value written back against campaign source",
        "Server side conversion sending where platforms support it",
        "Long sales cycle attribution that survives a six month gap",
        "Reporting on cost per signed matter by channel and practice area",
    ],
    "metric": "cost per signed matter",
    "angles": [
        ("Measure the matter, not the enquiry",
         "Campaigns that produce many cheap enquiries and no signed work look "
         "excellent in a platform report and are losing money."),
        ("Long cycles break default attribution",
         "Standard conversion windows expire long before a professional services "
         "matter signs. The tracking has to be built for the real timeline."),
        ("Weight by value",
         "A campaign producing fewer, larger matters beats one producing more, "
         "smaller ones. Unweighted reporting says the opposite."),
    ],
    "warning": "Client confidentiality limits what can be passed to advertising "
               "platforms. We send conversion signals and values without "
               "transmitting anything identifying.",
    "decision": "Build this before scaling spend. Otherwise budget flows to "
                "whichever campaign produces the most enquiries, which is rarely the most revenue.",
    "question": "How do we attribute a matter that took six months for {industry_lower}?",
    "answer": "Stamp the original source on the record when the enquiry arrives "
              "and keep it there through the pipeline. Platform attribution "
              "windows will have expired, so the CRM becomes the source of truth "
              "and we report from it rather than from the ad accounts.",
}
