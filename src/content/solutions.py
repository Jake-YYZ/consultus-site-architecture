# -*- coding: utf-8 -*-
"""
Division solutions: 10 per division, expressed as the outcome a buyer wants
rather than the channel used to get there.

  problem   the situation as the client would describe it
  approach  three concrete moves, not capabilities
  measure   what tells you it worked
  caveat    when this is the wrong thing to buy
"""

DIVISION_SOLUTIONS = {}
D = DIVISION_SOLUTIONS

# ------------------------------ HEALTHCARE ------------------------------

D[("Healthcare", "patient-acquisition")] = {
    "name": "Patient acquisition",
    "problem": "The schedule has room and not enough new patients are finding the practice.",
    "lede": "New patient volume, measured at the booked appointment rather than the enquiry.",
    "approach": [
        ("Fund the intent that already exists",
         "Search captures people actively looking for the service. It is the fastest "
         "reliable volume and the first place we look before building demand from scratch."),
        ("Fix the booking path before raising spend",
         "Most practices lose a meaningful share of enquiries between the form and the "
         "confirmed appointment. That gap is cheaper to close than it is to out-spend."),
        ("Measure to the appointment",
         "Cost per lead flatters campaigns that produce enquiries nobody can convert. "
         "We connect the practice management system so the number is the booking."),
    ],
    "measure": "cost per booked appointment, and the share of appointments that show",
    "caveat": "If the practice is at capacity, this is the wrong purchase. Raising "
              "prices or adding clinical hours will do more for revenue than more demand.",
}

D[("Healthcare", "patient-reactivation")] = {
    "name": "Patient reactivation",
    "problem": "Thousands of past patients in the system and no process for bringing them back.",
    "lede": "The cheapest appointment volume most practices own and never use.",
    "approach": [
        ("Segment by last visit and treatment type",
         "A patient overdue for a routine recall needs a different message from one "
         "who stopped a course of treatment halfway through."),
        ("Run it as a sequence, not a blast",
         "Email, then text, then a call from the front desk for the higher value "
         "segments. Each step recovers a portion the previous one missed."),
        ("Make booking one tap",
         "Reactivation dies at friction. The message should land on a booking page "
         "with the patient already identified."),
    ],
    "measure": "appointments booked per thousand contacted, and the cost of the campaign against them",
    "caveat": "Contacting past patients is subject to consent rules. Anyone who has "
              "opted out stays out, and a list that has never been mailed needs a careful re-permission approach.",
}

D[("Healthcare", "appointment-conversion")] = {
    "name": "Appointment conversion",
    "problem": "Plenty of enquiries arriving, not enough of them turning into booked visits.",
    "lede": "Closing the gap between someone asking and someone attending.",
    "approach": [
        ("Time the first response in minutes",
         "Enquiries answered inside five minutes convert several times better than "
         "ones answered the next morning. This is the single largest lever."),
        ("Listen to the calls",
         "Recorded intake calls show exactly where bookings are lost. It is usually "
         "price handled badly, or availability offered without alternatives."),
        ("Reduce no-shows deliberately",
         "Confirmation, reminder and a simple reschedule link recover a meaningful "
         "share of appointments that would otherwise be empty slots."),
    ],
    "measure": "enquiry to booked appointment rate, and show rate against booked",
    "caveat": "This is an operations project as much as a marketing one. Without a "
              "named owner at the practice, the systems get built and then ignored.",
}

D[("Healthcare", "multi-location-growth")] = {
    "name": "Multi-location growth",
    "problem": "Several sites, one budget, and no way to tell which location actually needs demand.",
    "lede": "Growing a group without locations competing against each other for the same click.",
    "approach": [
        ("Separate the locations properly",
         "Geographic campaign structure, distinct landing pages and clean business "
         "profiles per site. Locations sharing campaigns bid against each other."),
        ("Allocate budget by capacity",
         "The location with the best cost per lead is often the one with the least "
         "room. Budget should follow open schedule, not reporting quality."),
        ("Report by site and in aggregate",
         "Head office needs both. Group-level numbers hide a location in trouble."),
    ],
    "measure": "cost per booked appointment by location, against each site's available capacity",
    "caveat": "If business data is inconsistent across directories, fix that first. "
              "Local visibility work has no foundation while three versions of the address are live.",
}

D[("Healthcare", "new-clinic-launch")] = {
    "name": "New clinic launch",
    "problem": "A new site opening with no patient base, no reviews and fixed costs starting on day one.",
    "lede": "Getting a new location to break even faster than the last one did.",
    "approach": [
        ("Start before the doors open",
         "Search presence, business profile and booking capability live several "
         "weeks ahead of opening, so week one has demand rather than a standing start."),
        ("Buy intent, build reputation",
         "Paid search covers the gap while reviews and local signals accumulate. "
         "The paid share drops as organic presence establishes."),
        ("Ask every early patient for a review",
         "The first fifty reviews do more for a new location's visibility than any "
         "other single action available."),
    ],
    "measure": "weeks to break even, and the paid share of bookings falling over time",
    "caveat": "Launch campaigns are expensive per booking at the start and should be. "
              "Judging month one against a mature location's cost per appointment gives the wrong answer.",
}

D[("Healthcare", "practitioner-recruitment")] = {
    "name": "Practitioner recruitment",
    "problem": "Demand the practice cannot serve because the clinical roles are unfilled.",
    "lede": "Recruitment run as performance marketing rather than job board spend.",
    "approach": [
        ("Build a real careers page",
         "Compensation range, schedule, patient load and who they would work with. "
         "Clinicians rule out vague postings immediately."),
        ("Target by credential and geography",
         "Paid social and search aimed at specific qualifications reaches people who "
         "are not actively browsing job boards."),
        ("Track the pipeline like a sales funnel",
         "Applications, screens, interviews and offers, with cost per hire at the end of it."),
    ],
    "measure": "cost per qualified applicant and cost per hire",
    "caveat": "Marketing fills the top of the funnel. If interviews take three weeks "
              "to schedule, candidates accept elsewhere and no campaign fixes that.",
}

D[("Healthcare", "referral-diversification")] = {
    "name": "Referral diversification",
    "problem": "Most referrals arrive from a handful of sources, any of which could stop.",
    "lede": "Reducing the concentration risk in where patients come from.",
    "approach": [
        ("Map the current sources honestly",
         "Most practices are more concentrated than they think. The first output is "
         "usually uncomfortable and useful."),
        ("Build direct patient demand alongside referrals",
         "Condition and procedure content that ranks gives the practice a source it "
         "controls, rather than one it is granted."),
        ("Support referrers properly",
         "Fast reporting back, an easy referral path and clear communication keep "
         "existing sources while new ones develop."),
    ],
    "measure": "share of new patients from the largest single source, tracked quarterly",
    "caveat": "Direct demand takes months to build. Start while the referral "
              "relationships are healthy, not after one has ended.",
}

D[("Healthcare", "patient-retention")] = {
    "name": "Patient retention",
    "problem": "New patients arrive, complete one visit and are never seen again.",
    "lede": "Keeping the patients acquisition already paid for.",
    "approach": [
        ("Measure the second visit",
         "Most practices track new patients and never look at the return rate. "
         "The second appointment is where the economics are decided."),
        ("Automate recall properly",
         "Scheduled recall by treatment type, sent before the patient has drifted "
         "rather than a year after."),
        ("Find where people stop",
         "Course-of-treatment drop-off usually clusters at a specific visit number. "
         "That is a fixable operational finding."),
    ],
    "measure": "return visit rate and revenue per patient over twelve months",
    "caveat": "Retention problems are usually clinical experience or scheduling "
              "problems. Marketing surfaces them and cannot solve them alone.",
}

D[("Healthcare", "healthcare-digital-transformation")] = {
    "name": "Healthcare digital transformation",
    "problem": "Paper forms, phone-only booking and systems that do not talk to each other.",
    "lede": "Replacing manual process with systems that hold up as volume grows.",
    "approach": [
        ("Start with the patient-facing path",
         "Online booking, digital intake forms and automated confirmations. The "
         "friction there costs revenue and consumes most of the front desk's day."),
        ("Connect the systems that matter",
         "Practice management, CRM and marketing platforms sharing data rather than "
         "staff retyping it."),
        ("Keep what works",
         "Replacing a functioning clinical system is disruptive and rarely the "
         "highest return move. Most of the gain is at the front."),
    ],
    "measure": "staff hours returned, and the share of bookings completed without a phone call",
    "caveat": "Patient data handling is regulated. Any system change has to satisfy "
              "privacy requirements before it satisfies convenience ones.",
}

D[("Healthcare", "healthcare-business-intelligence")] = {
    "name": "Healthcare business intelligence",
    "problem": "Reports from four systems that disagree, and no single view of what is working.",
    "lede": "One set of numbers the practice leadership actually trusts.",
    "approach": [
        ("Define the metrics once",
         "What counts as a new patient, a booked appointment and an attributed "
         "source. Most disagreement between reports is definitional."),
        ("Connect the practice management data",
         "Marketing platforms know about clicks. Only the clinical system knows "
         "about appointments that happened."),
        ("Build one dashboard, not five",
         "Spend, enquiries, appointments, show rate and cost per appointment, by "
         "location and service line."),
    ],
    "measure": "one reconciled monthly view, with variance explained rather than argued about",
    "caveat": "Reporting does not improve performance. It makes the decisions "
              "visible. Budget for acting on what it shows.",
}

# ------------------------------ TRADES ------------------------------

D[("Trades", "lead-generation")] = {
    "name": "Lead generation",
    "problem": "The crew has capacity and the phone is not ringing enough.",
    "lede": "Booked jobs at a cost the average ticket can carry.",
    "approach": [
        ("Buy the searches that convert today",
         "Service and emergency terms in the areas you actually serve, with the "
         "negative list doing as much work as the keyword list."),
        ("Build geography into the structure",
         "Service area as campaign architecture rather than a filter applied after "
         "you have paid for the click."),
        ("Track calls to the keyword",
         "Most trades enquiries are phone calls. Without call tracking, the "
         "campaigns that work look like the ones that do not."),
    ],
    "measure": "cost per booked job against average ticket",
    "caveat": "More leads into a business already booked eight weeks out produces "
              "cancellations and bad reviews. Check capacity before funding volume.",
}

D[("Trades", "estimate-conversion")] = {
    "name": "Estimate conversion",
    "problem": "Quotes go out and a large share of them are never heard from again.",
    "lede": "The revenue already sitting in estimates that nobody followed up.",
    "approach": [
        ("Follow up on a schedule",
         "Two scheduled touches after a quote recovers a real share of jobs. Most "
         "businesses do none because it feels like chasing."),
        ("Make the quote easier to say yes to",
         "Clear scope, financing options where relevant, and an obvious way to "
         "accept without another phone call."),
        ("Find where quotes stall",
         "Price, timeline or trust. The pattern is usually consistent and visible "
         "once quotes are tracked as pipeline rather than paperwork."),
    ],
    "measure": "quote to booked job rate, and revenue recovered from follow-up",
    "caveat": "If the close rate is already strong, the constraint is lead volume "
              "instead and this is the wrong project.",
}

D[("Trades", "call-conversion")] = {
    "name": "Call conversion",
    "problem": "Calls come in, and too many end without a booked job.",
    "lede": "Getting more of the phone calls you already pay for onto the schedule.",
    "approach": [
        ("Answer more of them",
         "Missed call reporting by hour usually shows a predictable window where "
         "nobody picks up. That is a staffing decision, not a marketing one."),
        ("Text back automatically",
         "An immediate text to any missed call recovers a meaningful portion of "
         "callers who would otherwise ring the next company."),
        ("Score the calls",
         "Recorded calls scored against agreed criteria show whether the problem is "
         "lead quality or call handling. They are different problems."),
    ],
    "measure": "answered call rate and call to booked job rate",
    "caveat": "If most calls are unqualified, this is a targeting problem "
              "upstream. Fix the campaigns before retraining the office.",
}

D[("Trades", "seasonal-demand-generation")] = {
    "name": "Seasonal demand generation",
    "problem": "Two months of chaos and four months of nothing.",
    "lede": "Smoothing the year instead of riding it.",
    "approach": [
        ("Advertise into the shoulder",
         "Costs fall sharply when competitors pause. The planned work that fills "
         "the next peak gets booked in the quiet weeks."),
        ("Sell the off-season service",
         "Maintenance agreements, inspections and planned replacement are the "
         "products that fill an empty calendar."),
        ("Build the list before the season",
         "Email and remarketing audiences assembled in the quiet months are what "
         "make the peak cheaper to fill."),
    ],
    "measure": "revenue in the off-peak months, and cost per job across the full year",
    "caveat": "Off-season demand is genuinely thinner. The goal is a flatter "
              "curve, not an identical one.",
}

D[("Trades", "geographic-expansion")] = {
    "name": "Geographic expansion",
    "problem": "The home market is saturated and the next town over is unfamiliar territory.",
    "lede": "Entering a new service area without the reputation you have at home.",
    "approach": [
        ("Buy visibility while reputation builds",
         "In a new area there are no reviews and no word of mouth. Paid search "
         "covers the gap on day one."),
        ("Build the local proof deliberately",
         "First jobs in a new area are reputation investments. Photograph them, ask "
         "for reviews that name the town, publish them."),
        ("Check the drive time honestly",
         "Expansion that adds ninety minutes of unpaid travel per job destroys "
         "margin quietly."),
    ],
    "measure": "cost per booked job in the new area against the home market, and margin after travel",
    "caveat": "Organic visibility in a new area takes months and is limited by "
              "physical proximity. Expect paid to carry it longer than at home.",
}

D[("Trades", "franchise-growth")] = {
    "name": "Franchise growth",
    "problem": "Two audiences, one marketing team: customers who need work done and people who might buy a territory.",
    "lede": "Recruiting franchisees and generating customer demand without one starving the other.",
    "approach": [
        ("Separate the programs completely",
         "Franchise recruitment and customer acquisition share nothing: different "
         "audience, different cycle, different creative, different budget."),
        ("Give franchisees a system that works",
         "Local campaign templates, landing pages and business profile setup that a "
         "new operator can run without becoming a marketer."),
        ("Stop territories bidding against each other",
         "Central structure and geographic discipline, or franchisees pay each "
         "other's costs up."),
    ],
    "measure": "cost per qualified franchise enquiry, and system-wide cost per booked job",
    "caveat": "Franchise earnings claims are regulated as a financial offering in "
              "most jurisdictions, with real disclosure requirements.",
}

D[("Trades", "technician-recruitment")] = {
    "name": "Technician recruitment",
    "problem": "Work turned down because there is nobody to send.",
    "lede": "Hiring skilled trades with the same rigour as demand generation.",
    "approach": [
        ("Publish the real terms",
         "Pay range, truck, schedule, on-call expectations. Technicians rule out "
         "vague postings in seconds."),
        ("Reach people who are not looking",
         "Paid social targeted by trade and geography reaches employed technicians "
         "that job boards never will."),
        ("Move fast once they apply",
         "Skilled trades applicants have options. A three week hiring process loses "
         "candidates the campaign paid for."),
    ],
    "measure": "cost per qualified applicant and time from application to offer",
    "caveat": "If retention is the real problem, recruiting harder just refills a "
              "leaking bucket at increasing cost.",
}

D[("Trades", "reputation-growth")] = {
    "name": "Reputation growth",
    "problem": "Good work, thin review profile, and competitors who look more established online.",
    "lede": "Building the review base that decides both rankings and phone calls.",
    "approach": [
        ("Ask at completion",
         "The moment the job is finished and the customer is pleased is the only "
         "reliable time to ask. Built into the process, not left to memory."),
        ("Respond to everything",
         "Every review, positive and negative. Response rate is visible to "
         "customers and factors into local visibility."),
        ("Handle the bad ones properly",
         "A measured, specific reply to a negative review does more good than the "
         "review did harm. Defensive replies do the opposite."),
    ],
    "measure": "review count, average rating and review recency across every location",
    "caveat": "Incentivised or fabricated reviews get profiles suspended. It is "
              "not worth risking the asset that produces the calls.",
}

D[("Trades", "multi-location-growth")] = {
    "name": "Multi-location growth",
    "problem": "Several branches, overlapping service areas and a budget nobody can allocate confidently.",
    "lede": "Running multiple branches without them competing for the same customer.",
    "approach": [
        ("Draw the boundaries in the account",
         "Explicit geographic structure per branch, so two locations never pay for "
         "the same click."),
        ("Standardise the business data",
         "Consistent name, address and phone across every directory and profile. "
         "It is unglamorous and it is the foundation."),
        ("Fund by capacity",
         "Budget follows the branch with open schedule, not the branch with the "
         "best-looking report."),
    ],
    "measure": "cost per booked job by branch, against each branch's available capacity",
    "caveat": "Overlapping service areas need a rule about who takes the "
              "boundary work. Marketing cannot resolve a territory dispute.",
}

D[("Trades", "sales-enablement")] = {
    "name": "Sales enablement",
    "problem": "The person quoting the job has no idea what the customer already read or clicked.",
    "lede": "Giving estimators the context marketing already collected.",
    "approach": [
        ("Pass the context through",
         "Which ad, which service page, which question they asked. It arrives with "
         "the lead or it is lost."),
        ("Standardise the quote",
         "A consistent, clear proposal format converts better than whatever each "
         "estimator builds from scratch."),
        ("Close the loop",
         "Won and lost outcomes written back against the campaign, so bidding "
         "chases profitable work rather than cheap leads."),
    ],
    "measure": "quote to booked job rate, and cost per booked job by campaign",
    "caveat": "This needs estimators to update records. Without that discipline "
              "the reporting is worse than none, because it looks authoritative.",
}

# ------------------------------ DTC ------------------------------

D[("DTC", "customer-acquisition")] = {
    "name": "Customer acquisition",
    "problem": "New customer cost climbing every quarter and margin going with it.",
    "lede": "Acquiring customers at a cost the contribution margin can actually carry.",
    "approach": [
        ("Set the target from the margin",
         "What you can pay for a customer is arithmetic: contribution margin after "
         "product, shipping and fees, adjusted for repeat purchase."),
        ("Feed the account ideas, not budget",
         "Scaled accounts plateau on creative, not targeting. Production capacity "
         "is the real constraint on spend."),
        ("Watch new customer share",
         "Efficiency that improves while new customer share falls is harvesting, "
         "not growth."),
    ],
    "measure": "new customer acquisition cost against contribution margin",
    "caveat": "If contribution margin is under about thirty percent, acquisition "
              "spend accelerates the loss. Fix pricing or fulfilment first.",
}

D[("DTC", "creative-testing")] = {
    "name": "Creative testing",
    "problem": "Assets get made, some do better than others, and nobody can say why.",
    "lede": "Testing that produces knowledge rather than only a winner.",
    "approach": [
        ("One hypothesis per family",
         "A family of assets testing a single idea teaches you something when it "
         "loses. Unrelated assets teach you nothing."),
        ("Isolate the variable",
         "Hook, format and offer tested separately. Change all three and the "
         "winner cannot be repeated."),
        ("Keep the losing record",
         "Documented failures stop the same idea being proposed again next quarter."),
    ],
    "measure": "hook rate, hold rate and cost per acquisition by asset and by hypothesis",
    "caveat": "Testing needs volume. Below meaningful daily spend, results are "
              "noise presented as insight.",
}

D[("DTC", "conversion-optimization")] = {
    "name": "Conversion optimization",
    "problem": "Traffic is fine, the conversion rate is not, and buying more traffic is the expensive answer.",
    "lede": "Getting more revenue from the sessions you already have.",
    "approach": [
        ("Work where the traffic is",
         "Product pages, cart and checkout. Homepage redesigns rarely move revenue."),
        ("Remove the delivery uncertainty",
         "Shipping cost and delivery date on the product page, not discovered at "
         "checkout. It is the most reliable gain in ecommerce."),
        ("Audit the apps",
         "Established stores accumulate apps nobody uses that still load on every "
         "page. Removing them is usually the fastest speed win available."),
    ],
    "measure": "conversion rate and revenue per session",
    "caveat": "Under roughly a thousand monthly conversions most tests never reach "
              "significance. Fix the obvious problems and stop calling it testing.",
}

D[("DTC", "product-launches")] = {
    "name": "Product launches",
    "problem": "A launch that sells well for a week and then goes quiet.",
    "lede": "Launches built to keep selling after the announcement.",
    "approach": [
        ("Warm the owned list first",
         "Email and SMS carry launch day. Paid amplifies what the list starts."),
        ("Have the second wave ready",
         "Launch creative fatigues fast. The assets for weeks two through six get "
         "made before launch, not after the drop-off."),
        ("Decide the success metric in advance",
         "Units, revenue or new customers. Launches judged on whichever number "
         "looked best afterwards teach nothing."),
    ],
    "measure": "revenue and new customers in the first ninety days, not the first week",
    "caveat": "Launch spikes are partly cannibalised demand from existing "
              "customers. Track new customer share or the launch will look better than it was.",
}

D[("DTC", "retention-and-lifecycle-growth")] = {
    "name": "Retention and lifecycle growth",
    "problem": "Customers buy once and are never seen again, so acquisition has to keep running to stand still.",
    "lede": "Making the second and third order happen reliably.",
    "approach": [
        ("Build the flows before the campaigns",
         "Welcome, abandonment, post-purchase, replenishment and winback typically "
         "produce most of the owned channel revenue for a fraction of the effort."),
        ("Time replenishment to consumption",
         "If the product lasts sixty days, the reminder goes at forty five. Most "
         "brands guess this."),
        ("Segment by behaviour, not demographics",
         "What someone bought and when tells you more than who they are."),
    ],
    "measure": "repeat purchase rate at ninety days and owned channel revenue share",
    "caveat": "Discount-led retention trains a list to wait for the next sale. "
              "Short term revenue, long term margin damage.",
}

D[("DTC", "profitability-and-attribution")] = {
    "name": "Profitability and attribution",
    "problem": "Every platform reports a strong return and the bank balance disagrees.",
    "lede": "One efficiency number the whole business can make decisions on.",
    "approach": [
        ("Manage to blended efficiency",
         "Total revenue over total spend cannot be double counted. Channel numbers "
         "decide where the marginal dollar goes, not whether to spend it."),
        ("Test incrementality where the claims are largest",
         "Branded search and retargeting report beautifully and often capture "
         "demand that would have converted anyway. A holdout tells you how much."),
        ("Reconcile to real orders",
         "Platform totals against actual orders, monthly, with the variance explained."),
    ],
    "measure": "blended marketing efficiency ratio and contribution margin after marketing",
    "caveat": "Perfect attribution no longer exists. Directionally correct and "
              "consistently measured beats precise and wrong.",
}

D[("DTC", "marketplace-expansion")] = {
    "name": "Marketplace expansion",
    "problem": "Customers are searching the marketplace and finding a competitor, or a reseller of your own product.",
    "lede": "Owning your listings before someone else does.",
    "approach": [
        ("Fix the listing before the bids",
         "Titles, images and bullets decide conversion. Advertising cannot rescue "
         "a listing that does not convert."),
        ("Defend the branded terms",
         "Competitors bid on your brand. Not defending it means paying later to "
         "win back customers who were already looking for you."),
        ("Measure total cost of sale",
         "Advertising cost of sale measures the ads. Total advertising cost of sale "
         "measures the channel, including the organic orders the ads produced."),
    ],
    "measure": "total advertising cost of sale, and marketplace share of category",
    "caveat": "Marketplace growth can cannibalise your own store where margins are "
              "better. Worth doing, worth measuring across both.",
}

D[("DTC", "international-growth")] = {
    "name": "International growth",
    "problem": "Orders arriving from another country and no proper offer for them.",
    "lede": "Entering a new market with the economics worked out first.",
    "approach": [
        ("Model the landed cost honestly",
         "Duty, shipping, returns and currency. Many international expansions are "
         "unprofitable before the first ad runs."),
        ("Localise more than the currency",
         "Delivery expectations, payment methods and return policy matter more "
         "than translated copy."),
        ("Start where the demand already shows",
         "Existing organic orders point at the market that will be cheapest to enter."),
    ],
    "measure": "contribution margin by market after landed cost and returns",
    "caveat": "Returns from international orders are frequently uneconomic. Decide "
              "the policy before you advertise, not after the first refund request.",
}

D[("DTC", "subscription-growth")] = {
    "name": "Subscription growth",
    "problem": "Subscriber numbers grow and revenue does not, because churn is eating the additions.",
    "lede": "Building subscription revenue that compounds rather than churns.",
    "approach": [
        ("Fix the second shipment",
         "Most subscription churn happens between order one and order three. That "
         "is where the intervention belongs."),
        ("Give control instead of friction",
         "Skip, delay and change are retention tools. Hard-to-cancel is a "
         "regulatory risk and it damages the brand."),
        ("Model on cohort, not on total",
         "Total subscriber count hides a cohort curve that is either improving or not."),
    ],
    "measure": "cohort retention at three and six months, and revenue per subscriber",
    "caveat": "Auto-renewal and cancellation rules are tightening in several "
              "markets. Cancellation has to be as easy as signing up.",
}

D[("DTC", "omnichannel-growth")] = {
    "name": "Omnichannel growth",
    "problem": "Retail, marketplace and direct all growing separately and occasionally against each other.",
    "lede": "Running direct and retail as one business rather than competing ones.",
    "approach": [
        ("Decide the pricing rules first",
         "Channel conflict is a pricing and promotion problem before it is a "
         "marketing one."),
        ("Measure the halo",
         "Direct advertising drives retail sales it never gets credit for. "
         "Geographic testing shows roughly how much."),
        ("Use direct for what retail cannot do",
         "New product testing, subscription and the customer relationship itself."),
    ],
    "measure": "total brand revenue and contribution margin across all channels",
    "caveat": "Retail partners react to direct discounting. Agree the rules with "
              "them before running the promotion.",
}

# ------------------------ PROFESSIONAL SERVICES ------------------------

D[("Professional Services", "high-value-lead-generation")] = {
    "name": "High-value lead generation",
    "problem": "Plenty of enquiries and very few of them the kind of matter the firm wants.",
    "lede": "Fewer enquiries, better matters, lower cost per signed file.",
    "approach": [
        ("Bid on the matter, not the profession",
         "Someone searching the profession is researching. Someone describing "
         "their specific problem is ready to hire."),
        ("Qualify in the advertising",
         "Naming the matter type and the situation reduces volume and raises the "
         "share worth a partner's time."),
        ("Measure to the signed matter",
         "Campaigns producing cheap enquiries that never sign look excellent in a "
         "platform report and lose money."),
    ],
    "measure": "cost per signed matter, and average value of matters by source",
    "caveat": "This will reduce lead volume. If the firm judges marketing on "
              "enquiry count, agree the change of metric before starting.",
}

D[("Professional Services", "authority-building")] = {
    "name": "Authority building",
    "problem": "The firm is genuinely expert and nothing online demonstrates it.",
    "lede": "Making expertise visible to people deciding who to hire.",
    "approach": [
        ("Publish judgment, not summaries",
         "Content that takes a position and explains when it applies. Surveys of "
         "every option help nobody decide."),
        ("Name the author properly",
         "Real credentials, real qualifications, a real biography. In regulated "
         "categories this affects both trust and search visibility."),
        ("Write about what just changed",
         "Regulatory and legislative change creates urgent, searchable questions "
         "with almost no competing content."),
    ],
    "measure": "non-branded organic enquiries and citations by other publications",
    "caveat": "Ghostwritten content with a partner's name on it reads generic "
              "because it is. The practitioner has to be genuinely involved.",
}

D[("Professional Services", "pipeline-growth")] = {
    "name": "Pipeline growth",
    "problem": "Revenue is fine this quarter and there is nothing visible behind it.",
    "lede": "Building a pipeline that is measurable before it closes.",
    "approach": [
        ("Define the stages honestly",
         "Enquiry, qualified, consultation, proposal, signed. Most firms have "
         "stages that describe hope rather than progress."),
        ("Instrument the long cycle",
         "Professional services cycles outlast platform attribution windows. The "
         "CRM has to become the source of truth."),
        ("Report leading indicators",
         "Consultations booked this month predicts revenue in four months. Revenue "
         "reported monthly predicts nothing."),
    ],
    "measure": "qualified pipeline value and consultation to signed matter rate",
    "caveat": "Pipeline reporting is only as good as partner discipline in "
              "updating it. That is a management problem, not a systems one.",
}

D[("Professional Services", "sales-enablement")] = {
    "name": "Sales enablement",
    "problem": "The partner taking the consultation knows nothing about how the client arrived.",
    "lede": "Arming the people who close with what marketing already knows.",
    "approach": [
        ("Pass the context to the consultation",
         "Which search, which page, which question. It changes how the first "
         "conversation opens."),
        ("Standardise the proposal",
         "A consistent format with clear scope and fees converts better than "
         "whatever each partner drafts."),
        ("Write outcomes back",
         "Signed and lost, with reasons, against the original source. That is how "
         "the marketing gets better."),
    ],
    "measure": "consultation to signed matter rate, and cost per signed matter by source",
    "caveat": "Conflict checks and privilege requirements constrain what can be "
              "stored and shared. The build works inside those rules.",
}

D[("Professional Services", "market-expansion")] = {
    "name": "Market expansion",
    "problem": "A new city or practice area where the firm has no reputation and no referral base.",
    "lede": "Entering a market where nobody has heard of you yet.",
    "approach": [
        ("Buy intent while authority builds",
         "Paid search covers the gap in a market with no branded demand and no "
         "referral flow."),
        ("Build local proof deliberately",
         "Local content, local people on the site, and matters that demonstrate "
         "the firm actually works there."),
        ("Check the regulatory position first",
         "Practising or advertising in a new jurisdiction may require licensing or "
         "different disclosure."),
    ],
    "measure": "cost per qualified enquiry in the new market against the established one",
    "caveat": "Organic authority in a new market takes six to twelve months. "
              "Budget for paid to carry it for longer than feels comfortable.",
}

D[("Professional Services", "multi-office-growth")] = {
    "name": "Multi-office growth",
    "problem": "Several offices with near-identical pages, competing for the same searches.",
    "lede": "Growing a multi-office firm without the offices cannibalising each other.",
    "approach": [
        ("Give every office a real page",
         "Its own people, practice areas and local matters. Duplicated pages with "
         "the city swapped rank badly and convert worse."),
        ("Separate the campaigns geographically",
         "Or offices bid against each other and the firm pays for the privilege."),
        ("Keep authority central",
         "Thought leadership belongs to the firm. Local pages carry the "
         "geographic and relationship signals."),
    ],
    "measure": "qualified enquiries by office, against each office's capacity",
    "caveat": "Firms operating across jurisdictions face different advertising "
              "rules in each. Content has to state which one it applies to.",
}

D[("Professional Services", "crm-adoption")] = {
    "name": "CRM adoption",
    "problem": "The firm bought a CRM and the fee earners do not use it.",
    "lede": "Getting a system used, which is a different problem from choosing one.",
    "approach": [
        ("Reduce what has to be entered",
         "Adoption fails on data entry burden. Automate what can be captured and "
         "ask for the minimum that is genuinely needed."),
        ("Make it useful to the person entering it",
         "If the only beneficiary is a management report, it will not get updated."),
        ("Fix intake first",
         "The enquiry layer is where the value is and where compliance is easiest. "
         "Matter management can follow."),
    ],
    "measure": "share of enquiries with a complete record, and time to first response",
    "caveat": "Replacing a system the firm runs on is expensive and disruptive. "
              "Most adoption problems are configuration and process, not the software.",
}

D[("Professional Services", "reputation-and-trust")] = {
    "name": "Reputation and trust",
    "problem": "Prospective clients research the firm and find very little, or the wrong thing.",
    "lede": "Managing what someone finds when they check you out before calling.",
    "approach": [
        ("Own the branded search result",
         "Firm name, partner names and directory profiles. This is the page every "
         "referral looks at before making contact."),
        ("Build reviews within the rules",
         "What is permitted varies by regulator. Where reviews are allowed, ask "
         "systematically. Where they are not, use the channels that are."),
        ("Respond to everything, carefully",
         "Confidentiality limits what can be said in reply. A measured response "
         "that does not disclose is still worth making."),
    ],
    "measure": "branded search result quality, review volume and rating where permitted",
    "caveat": "Responding to a client complaint publicly risks breaching "
              "confidentiality. Reply templates need professional review.",
}

D[("Professional Services", "partner-led-growth")] = {
    "name": "Partner-led growth",
    "problem": "Business development depends entirely on a few partners' personal networks.",
    "lede": "Turning individual reputation into firm-wide pipeline.",
    "approach": [
        ("Build the individual profiles",
         "Buyers search for people. Partner pages with real substance are often "
         "the highest converting pages on a professional services site."),
        ("Support the partners who will engage",
         "Content, speaking and outreach behind the people who actually want to do "
         "business development. Forcing the rest wastes everyone's time."),
        ("Connect personal brand back to the firm",
         "Individual authority that never links to the firm builds an asset the "
         "partner takes with them."),
    ],
    "measure": "enquiries attributable to named partners, and firm-level share of the pipeline",
    "caveat": "This concentrates dependency on individuals. Balance it with firm-level "
              "authority or the risk gets worse rather than better.",
}

D[("Professional Services", "digital-transformation")] = {
    "name": "Digital transformation",
    "problem": "Shared inboxes, spreadsheets and one person who knows how everything works.",
    "lede": "Replacing manual process before volume or a resignation forces the issue.",
    "approach": [
        ("Start at intake",
         "The enquiry layer is where the revenue leaks and where automation "
         "returns the most for the least disruption."),
        ("Document what only lives in someone's head",
         "The single-person dependency is the real risk. Writing the process down "
         "is most of the fix."),
        ("Keep the systems that work",
         "Practice and matter management usually functions. The gap is almost "
         "always at the front end."),
    ],
    "measure": "time to first response, and hours returned to fee-earning work",
    "caveat": "Client confidentiality and data residency requirements constrain "
              "which tools are permissible. Check before selecting, not after.",
}
