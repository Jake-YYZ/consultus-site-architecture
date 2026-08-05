# -*- coding: utf-8 -*-
"""
Sector profiles: 45 groups spanning 599 industries.

Every industry page and service-by-industry page inherits from its sector, so
this file carries the substance that stops those pages being interchangeable.

Fields per sector:
  lede        one sentence on what makes marketing this group different
  context     two paragraphs a practitioner would recognise as true
  buyer       who actually makes the decision
  cycle       how long the decision takes
  lead_ch     which channel usually leads, and why
  challenges  three real problems, concretely stated
  judgment    an opinion worth disagreeing with
  watch       the practical warning
"""

SECTORS = {}

# ============================== HEALTHCARE ==============================

SECTORS["Hospitals and facilities"] = {
    "division": "Healthcare",
    "lede": "Facilities compete on access and proximity more than reputation, and most of the demand is unplanned.",
    "context": [
        "People choose a facility under pressure, usually quickly and usually "
        "close to home. That makes proximity, wait times and whether the phone "
        "gets answered more decisive than any brand campaign.",
        "The marketing job splits between service lines that need volume and "
        "service lines that are already full. Advertising a department at "
        "capacity generates complaints rather than revenue, so the plan has to "
        "start from where the schedule actually has room.",
    ],
    "buyer": "marketing directors and service line leaders, with clinical sign-off",
    "cycle": "hours for urgent services, weeks for elective procedures",
    "lead_ch": "local search and map visibility, because most searches carry location intent",
    "challenges": [
        "Demand is uneven across departments while budget is set centrally",
        "Wait time and access questions go unanswered on the website",
        "Multiple locations competing for the same searches",
    ],
    "judgment": "Publish current wait times if you have them. It is the single "
                "most searched piece of information about an urgent care facility "
                "and almost nobody puts it on the page.",
    "watch": "Advertising a service line with no capacity converts marketing "
             "budget into patient complaints. Confirm schedule availability before funding volume.",
}

SECTORS["Senior and home care"] = {
    "division": "Healthcare",
    "lede": "The person searching is almost never the person receiving care.",
    "context": [
        "An adult child, usually mid-career and mid-crisis, is doing the "
        "research. They are comparing options, managing guilt and trying to work "
        "out cost, often within a few days of a hospital discharge.",
        "That changes the content entirely. Pricing, availability, what a day "
        "actually looks like and how quickly care can start matter more than "
        "philosophy of care statements.",
    ],
    "buyer": "adult children and family decision makers, often several at once",
    "cycle": "days when triggered by a health event, months when planned",
    "lead_ch": "search, because the trigger is a specific event that prompts an immediate search",
    "challenges": [
        "Emotional decision with several family members who disagree",
        "Cost is the first question and the last thing published",
        "Availability changes weekly and the website never reflects it",
    ],
    "judgment": "Put pricing on the site. Families rule out providers who hide "
                "it, and the enquiries you lose were never going to convert once they heard the number.",
    "watch": "Reviews carry unusual weight here and a single detailed negative "
             "review can outweigh twenty positive ones. Review response is part of the marketing job.",
}

SECTORS["Medical and surgical specialties"] = {
    "division": "Healthcare",
    "lede": "Referral flow and direct search both matter, and most practices only manage one of them.",
    "context": [
        "Specialist practices historically filled through referring physicians. "
        "Patients now research the specialist they were referred to, and "
        "increasingly search directly for a condition and choose without a referral.",
        "That means two audiences with different needs: referrers who want "
        "clinical detail and fast communication, patients who want to know what "
        "the condition means and what happens at the first appointment.",
    ],
    "buyer": "practice owners and physicians, sometimes a practice manager",
    "cycle": "days to weeks for symptomatic patients, longer for elective procedures",
    "lead_ch": "organic search on condition and procedure terms, supported by paid search for elective work",
    "challenges": [
        "Referral volume treated as fixed rather than something to grow",
        "Condition content written for colleagues instead of patients",
        "No visibility into whether referred patients actually booked",
    ],
    "judgment": "Write the condition pages for the patient, not the referrer. "
                "The referrer already knows. The patient deciding whether to "
                "attend the appointment does not, and they are the one who cancels.",
    "watch": "Some specialties face advertising restrictions on outcome claims. "
             "Check what your college permits before building creative around results.",
}

SECTORS["Maternal and newborn care"] = {
    "division": "Healthcare",
    "lede": "A fixed decision window, high emotional weight and heavy reliance on peer recommendation.",
    "context": [
        "The research window opens with a positive test and closes at delivery. "
        "It is one of the few healthcare categories with a genuinely predictable timeline.",
        "Decisions are made socially. Local parent groups, friends and online "
        "communities carry more weight than advertising, which makes reputation "
        "and word of mouth the real channel.",
    ],
    "buyer": "expectant parents, usually researching together",
    "cycle": "weeks to months, inside a fixed nine month window",
    "lead_ch": "organic search and community reputation, with paid social for awareness early in the window",
    "challenges": [
        "Reaching people early enough in the window to matter",
        "Competing with free hospital-provided services",
        "Reviews and community recommendation outweigh any paid message",
    ],
    "judgment": "Target the first trimester even though conversion happens later. "
                "By the second trimester most choices are already narrowed to two options.",
    "watch": "Birth outcome claims and imagery are sensitive and heavily "
             "scrutinised on social platforms. Keep creative focused on support and process.",
}

SECTORS["Pediatric and child health"] = {
    "division": "Healthcare",
    "lede": "Parents decide fast, under stress, and judge on how quickly they can be seen.",
    "context": [
        "A parent searching for pediatric care usually has a sick child and a "
        "wait they consider unacceptable. Speed of access beats almost every "
        "other consideration.",
        "For therapy and assessment services the pattern flips. Those decisions "
        "take months, involve schools and often hinge on waitlist length and "
        "whether the cost is covered.",
    ],
    "buyer": "parents, occasionally guided by a school or family physician",
    "cycle": "same day for urgent care, months for assessment and therapy services",
    "lead_ch": "local search for urgent services, organic and referral for therapy and assessment",
    "challenges": [
        "Wait times decide the choice and are rarely published",
        "Insurance and coverage questions go unanswered",
        "Assessment waitlists so long that enquiries go cold before intake",
    ],
    "judgment": "Publish your waitlist length even when it is bad. Parents "
                "calling six clinics will remember the one that told them the "
                "truth, and they come back when a space opens.",
    "watch": "Marketing to children is restricted on every major platform. All "
             "targeting and creative addresses the parent.",
}

SECTORS["Dental"] = {
    "division": "Healthcare",
    "lede": "One of the most competitive local advertising categories, split between routine care and elective work.",
    "context": [
        "Routine dentistry competes on proximity, insurance acceptance and "
        "availability. It is a local search fight and the map results decide most of it.",
        "Elective work behaves completely differently. Cosmetic treatment, "
        "implants and orthodontics are considered purchases with long research "
        "windows, financing questions and a real role for social advertising.",
    ],
    "buyer": "practice owners, and increasingly group or DSO marketing leads",
    "cycle": "days for routine and emergency, months for cosmetic and orthodontic work",
    "lead_ch": "local search and map visibility for routine care, paid social for elective treatment",
    "challenges": [
        "New patient offers have trained the market to shop on price",
        "Insurance questions unanswered on the site cost bookings",
        "Emergency searches happen outside opening hours",
    ],
    "judgment": "Discount new patient offers fill chairs with people who leave "
                "when the next offer appears. Competing on availability and "
                "insurance clarity builds a practice worth selling.",
    "watch": "Before and after imagery is restricted on Meta for most dental "
             "treatment, which removes the format cosmetic practices ask for first.",
}

SECTORS["Eye and vision"] = {
    "division": "Healthcare",
    "lede": "Routine exams are a local commodity and surgery is a considered, high value decision.",
    "context": [
        "Optometry competes locally on convenience, insurance and eyewear "
        "selection. It behaves like retail with a clinical component.",
        "Refractive and cataract surgery is a different business. Research runs "
        "for months, price and safety dominate the questions, and the surgeon's "
        "track record carries the decision.",
    ],
    "buyer": "practice owners, clinic managers and surgical practice marketing leads",
    "cycle": "days for exams, three to nine months for elective surgery",
    "lead_ch": "local search for optometry, paid search and social for surgical procedures",
    "challenges": [
        "Exams devalued by retail chains competing on price",
        "Surgery decisions stall on cost and safety concerns",
        "Eyewear revenue not connected to the exam booking journey",
    ],
    "judgment": "For elective surgery, publish the full price including "
                "follow-up. The category is full of headline prices that turn out "
                "to be per-eye or exclude aftercare, and buyers have learned to distrust the number.",
    "watch": "Vision correction outcome claims attract regulatory attention. "
             "Describe candidacy and process rather than promising results.",
}

SECTORS["Hearing"] = {
    "division": "Healthcare",
    "lede": "A long denial phase, then a fast decision once someone finally accepts they need help.",
    "context": [
        "The average person waits years between noticing hearing loss and doing "
        "something about it. Much of the marketing job is reaching them during "
        "that gap without making them defensive.",
        "Family members often start the search. Content that speaks to a spouse "
        "or adult child performs differently from content aimed at the person "
        "with the hearing loss.",
    ],
    "buyer": "clinic owners and retail group marketing leads",
    "cycle": "years of consideration, then weeks once the decision is made",
    "lead_ch": "search for people ready to act, paid social to reach family members earlier",
    "challenges": [
        "Long denial phase before anyone searches",
        "Price shock at the first quote",
        "Online and big box competition on device pricing",
    ],
    "judgment": "Lead with the free hearing test rather than the devices. The "
                "test is the low commitment step people will actually take, and "
                "the device conversation follows naturally.",
    "watch": "Device pricing is publicly compared and increasingly commoditised. "
             "Compete on the fitting, the follow-up and the audiologist, not the hardware.",
}

SECTORS["Allied health and rehab"] = {
    "division": "Healthcare",
    "lede": "High repeat visit volume, insurance coverage as the deciding factor, and heavy local competition.",
    "context": [
        "These practices live on repeat visits. A patient who books a course of "
        "treatment is worth many times a single appointment, which changes what "
        "an acquisition is worth.",
        "Coverage decides most bookings. Whether you direct bill, which insurers "
        "you work with and what the visit costs out of pocket are the questions "
        "that get asked on the first call.",
    ],
    "buyer": "clinic owners and multi-clinic operators",
    "cycle": "days, often triggered by injury or a physician recommendation",
    "lead_ch": "local search and map visibility, with referral relationships underneath",
    "challenges": [
        "Direct billing and coverage questions unanswered online",
        "High practitioner turnover disrupting patient continuity",
        "Retention after the first few visits rarely measured",
    ],
    "judgment": "Measure the course of treatment, not the first booking. A clinic "
                "with a strong first visit rate and poor retention is buying "
                "patients for competitors down the road.",
    "watch": "Injury and pain treatment claims are regulated by professional "
             "colleges. Describe the assessment and approach, not the outcome.",
}

SECTORS["Mental and behavioural health"] = {
    "division": "Healthcare",
    "lede": "Every major platform restricts the targeting, and the person searching is often in crisis.",
    "context": [
        "Meta and Google both limit how mental health services can target and "
        "what they can say. Interest targeting on conditions is largely "
        "unavailable, which pushes the whole job into the creative and the copy.",
        "Availability decides more bookings than approach does. Someone looking "
        "for help wants to know when they can be seen, whether it is covered, "
        "and whether sessions are virtual or in person.",
    ],
    "buyer": "practice owners, group practice directors and clinical leads",
    "cycle": "days when acute, weeks when planned",
    "lead_ch": "organic search and directory presence, with careful paid search where policy allows",
    "challenges": [
        "Platform restrictions on health condition targeting",
        "Waitlists longer than the enquiry stays warm",
        "Matching a client to the right clinician inside the practice",
    ],
    "judgment": "Publish availability by clinician and update it weekly. It "
                "converts better than any messaging about approach or modality, "
                "and it is the thing people are actually trying to find out.",
    "watch": "Ads that imply knowledge of someone's mental health condition are "
             "prohibited. Copy addresses a general audience or it gets rejected.",
}

SECTORS["Aesthetics and med spa"] = {
    "division": "Healthcare",
    "lede": "Visual, discretionary, price sensitive, and hemmed in by imagery restrictions on every platform.",
    "context": [
        "This is the most visual category in healthcare and the one most "
        "constrained in showing results. Before and after imagery, the obvious "
        "creative approach, is restricted or prohibited across the major platforms.",
        "Purchases are discretionary and repeatable. A client who commits to a "
        "treatment schedule is worth many times a single appointment, so "
        "retention economics justify a higher acquisition cost than first-visit maths suggests.",
    ],
    "buyer": "owners and marketing managers, frequently owner-operated",
    "cycle": "weeks for first treatment, then recurring",
    "lead_ch": "paid social for demand creation, search to capture treatment-specific intent",
    "challenges": [
        "Before and after imagery restricted on the platforms that matter most",
        "Constant discounting across the category",
        "Injector or practitioner departures taking clients with them",
    ],
    "judgment": "Sell the treatment plan, not the single session. The businesses "
                "that hold margin here are the ones that book the next appointment "
                "before the client leaves.",
    "watch": "Meta prohibits ads implying negative self-perception about "
             "appearance. Copy about fixing flaws gets rejected and repeat rejections risk the account.",
}

SECTORS["Wellness and longevity"] = {
    "division": "Healthcare",
    "lede": "Self-pay, high ticket, and constantly at risk of overstating what the science supports.",
    "context": [
        "Nothing here is covered by insurance, which means the buyer is paying "
        "directly and expects clarity about what they get for the money.",
        "The category attracts aggressive claims and regulators have noticed. "
        "The durable businesses describe the protocol, the testing and the "
        "physician oversight rather than promising outcomes.",
    ],
    "buyer": "clinic owners and program directors",
    "cycle": "weeks to months, with significant price consideration",
    "lead_ch": "paid social to build demand, search for people already looking for a named protocol",
    "challenges": [
        "Explaining value when nothing is covered",
        "Claims that will not survive regulatory review",
        "Programs that sound identical to every competitor",
    ],
    "judgment": "Publish what the program includes and what it costs. In a "
                "category where everyone gestures at optimisation, specificity is "
                "the entire differentiator.",
    "watch": "Hormone, peptide and weight management advertising is tightly "
             "restricted and enforcement is increasing. Get claims reviewed before production.",
}

SECTORS["Animal health"] = {
    "division": "Healthcare",
    "lede": "Emergency-driven, emotionally charged, and increasingly consolidated by corporate groups.",
    "context": [
        "Most veterinary searches happen when something is wrong. Proximity, "
        "whether the clinic is accepting new patients and whether they can be "
        "seen today decide the call.",
        "Many clinics are at capacity and struggling to hire, which means the "
        "marketing question is often about the right clients rather than more "
        "clients. Recruitment marketing frequently matters more than acquisition.",
    ],
    "buyer": "practice owners and corporate group marketing teams",
    "cycle": "same day for emergencies, weeks for wellness and elective services",
    "lead_ch": "local search and map visibility",
    "challenges": [
        "Clinics at capacity and closed to new patients",
        "Staffing shortages limiting how much demand can be served",
        "Price sensitivity colliding with rising care costs",
    ],
    "judgment": "If you are at capacity, spend the budget on recruitment instead "
                "of acquisition. More demand into a full clinic produces burnout and bad reviews.",
    "watch": "Pet loss and emergency care advertising needs care. Fear-based "
             "creative in this category damages trust badly.",
}

SECTORS["Pharmacy, labs and diagnostics"] = {
    "division": "Healthcare",
    "lede": "Convenience decides retail pharmacy, and clinical relationships decide everything else.",
    "context": [
        "Retail pharmacy competes on location, hours and wait time. It is a "
        "local convenience business with a clinical licence.",
        "Specialty pharmacy, labs and imaging sell to referrers and payers as "
        "much as to patients. Turnaround time and reporting quality carry more "
        "weight than consumer messaging.",
    ],
    "buyer": "owners, and business development leads for referral-driven services",
    "cycle": "immediate for retail, months for referral and contract relationships",
    "lead_ch": "local search for retail, direct and content-led for referral relationships",
    "challenges": [
        "Chain competition on price and hours",
        "Referral relationships built person to person and rarely supported by marketing",
        "Direct to consumer testing changing how patients access diagnostics",
    ],
    "judgment": "For referral-driven services, market to the referrer with the "
                "operational facts they care about: turnaround time, report "
                "clarity and how fast someone answers when there is a problem.",
    "watch": "Prescription and diagnostic advertising is restricted in most "
             "jurisdictions. Rules differ significantly between Canada and the United States.",
}

SECTORS["Healthcare business and tech"] = {
    "division": "Healthcare",
    "lede": "Selling to healthcare organisations, with long cycles and committees rather than individuals.",
    "context": [
        "The buyer is an organisation. Procurement, clinical leadership, IT and "
        "compliance all get a say, and any one of them can stop a deal.",
        "Marketing has to arm an internal champion with what they need to "
        "convince colleagues, because the person who fills in the form is rarely the person who signs.",
    ],
    "buyer": "practice administrators, clinical directors and procurement committees",
    "cycle": "three to eighteen months with multiple stakeholders",
    "lead_ch": "content and search for the research phase, with targeted outbound for named accounts",
    "challenges": [
        "Committee decisions where one objection stalls everything",
        "Long cycles that break default attribution windows",
        "Compliance and security review arriving late and killing deals",
    ],
    "judgment": "Publish your security and compliance documentation openly. In "
                "healthcare software it gets requested in every deal, and making "
                "buyers ask for it adds weeks to the cycle.",
    "watch": "Patient data claims get scrutinised. Anything implied about "
             "privacy or compliance has to be exactly true.",
}

SECTORS["Healthcare ecommerce and brands"] = {
    "division": "Healthcare",
    "lede": "Ecommerce economics with a regulatory layer that decides what the creative can say.",
    "context": [
        "These are DTC businesses. They live on contribution margin, repeat "
        "purchase and blended efficiency like any other consumer brand.",
        "The difference is claims. What the product does, who it is for and what "
        "results are implied all fall under advertising policy and health "
        "regulation, which constrains the creative before it is written.",
    ],
    "buyer": "founders, ecommerce directors and brand marketing leads",
    "cycle": "immediate for low ticket, weeks for devices and high value equipment",
    "lead_ch": "paid social for demand, search and marketplace for capture",
    "challenges": [
        "Health claims restricting what creative can test",
        "Marketplace competition on identical products",
        "Repeat purchase economics that are never modelled properly",
    ],
    "judgment": "Compete on specificity. Ingredients, testing, certifications and "
                "what the product does not do. It clears review more reliably and "
                "it is what buyers in this category actually compare.",
    "watch": "Clearing platform ad review is not the same as complying with "
             "Health Canada or the FDA. Both apply and only one of them sends warning letters.",
}

# ============================== TRADES ==============================

SECTORS["Mechanical and building systems"] = {
    "division": "Trades",
    "lede": "Sharply seasonal, split between emergency replacement and planned installation.",
    "context": [
        "Heating and cooling demand spikes with the weather and collapses "
        "between seasons. The emergency work is high margin and captured almost "
        "entirely through search, in the hour the system fails.",
        "Planned replacement and maintenance agreements are the stable half of "
        "the business, and they are won months earlier through reputation and follow-up.",
    ],
    "buyer": "homeowners in an emergency, property and facility managers for commercial work",
    "cycle": "hours for emergency replacement, weeks to months for planned installation",
    "lead_ch": "search for emergency demand, social and email for planned replacement",
    "challenges": [
        "Revenue collapsing between seasons",
        "Emergency calls arriving outside staffed hours",
        "Maintenance agreements sold once and never renewed",
    ],
    "judgment": "Do not go dark in the shoulder season. Costs per click fall "
                "sharply when competitors pause, and the planned replacement "
                "conversations that fill the next peak start there.",
    "watch": "Rebate and incentive programs change frequently. Advertising an "
             "expired rebate creates complaints and, in some jurisdictions, a compliance problem.",
}

SECTORS["Plumbing and water"] = {
    "division": "Trades",
    "lede": "The clearest emergency search category in the trades, decided by who answers first.",
    "context": [
        "A homeowner with water coming through the ceiling searches, calls the "
        "first credible result and books. The entire decision takes minutes and "
        "nobody compares three quotes.",
        "Planned work, water treatment and larger sewer and septic projects run "
        "on a different clock and need proof of prior work rather than speed.",
    ],
    "buyer": "homeowners, property managers and commercial facility teams",
    "cycle": "minutes for emergencies, weeks for planned work",
    "lead_ch": "search, and specifically Local Services Ads where the category supports them",
    "challenges": [
        "Emergency demand arriving overnight and at weekends",
        "Price shopping on routine jobs like drain clearing",
        "Larger projects requiring credibility a search ad cannot establish",
    ],
    "judgment": "If you advertise twenty four hour service, answer the phone at "
                "three in the morning. Paying for emergency clicks that go to "
                "voicemail is the most common avoidable waste in the category.",
    "watch": "Licensing and insurance verification is required for Local "
             "Services Ads and takes weeks. Start it before you plan the campaign launch.",
}

SECTORS["Electrical and energy"] = {
    "division": "Trades",
    "lede": "Traditional electrical work plus a fast-moving set of energy categories driven by incentives.",
    "context": [
        "Core electrical work behaves like the rest of the trades. Service "
        "calls, panel upgrades and commercial contracts, won through search and reputation.",
        "Solar, EV charging and efficiency work are incentive-driven markets. "
        "Demand moves when rebate programs change, and the businesses that track "
        "those changes closely get the volume.",
    ],
    "buyer": "homeowners for service and energy work, general contractors and facility managers for commercial",
    "cycle": "days for service calls, months for solar and energy projects",
    "lead_ch": "search for service work, paid social and content for energy projects",
    "challenges": [
        "Incentive programs changing the market with little notice",
        "Long consideration cycles on solar with high drop-off",
        "Commercial work won on relationships rather than advertising",
    ],
    "judgment": "In energy categories, publish the current incentive amounts and "
                "keep them accurate. It is the top search query, it changes often, "
                "and being the reliable source for it wins the enquiry.",
    "watch": "Savings and payback claims in solar attract regulatory attention "
             "in several markets. Use ranges tied to real conditions rather than headline figures.",
}

SECTORS["Exterior and structural"] = {
    "division": "Trades",
    "lede": "High ticket, weather-triggered, and crowded with storm-chasing competitors.",
    "context": [
        "Roofing and exterior demand spikes after weather events and stays flat "
        "otherwise. Storm periods bring out-of-area contractors who advertise "
        "aggressively and leave.",
        "The established local business competes on proof: real projects, real "
        "warranties and the fact that they will still exist when the warranty is called on.",
    ],
    "buyer": "homeowners, property managers and insurance adjusters",
    "cycle": "days after storm damage, weeks to months for planned replacement",
    "lead_ch": "search for damage-triggered demand, social for planned replacement and financing",
    "challenges": [
        "Storm chasers driving up ad costs and undercutting on price",
        "Insurance claim process confusing homeowners",
        "Long consideration cycles on large discretionary projects",
    ],
    "judgment": "Lead with how long you have been in the area and how the "
                "warranty works. Against transient competitors, permanence is the "
                "differentiator that actually matters to a homeowner.",
    "watch": "Insurance claim assistance is regulated in several jurisdictions "
             "and unlicensed claim handling carries real penalties.",
}

SECTORS["Interior renovation and finishing"] = {
    "division": "Trades",
    "lede": "Long consideration windows, visual decisions and buyers who are comparing three quotes.",
    "context": [
        "A kitchen or bathroom renovation is planned for months and researched "
        "visually. Buyers collect images long before they contact anyone.",
        "By the time they call, they are usually talking to three contractors "
        "and comparing on price, timeline and how much disruption to expect. "
        "The one who explains the process clearly wins more than the cheapest one.",
    ],
    "buyer": "homeowners, usually a couple deciding together",
    "cycle": "three to twelve months from first idea to signed contract",
    "lead_ch": "social and visual platforms for demand, search for capture near the decision",
    "challenges": [
        "Long research windows with many touchpoints and no attribution",
        "Quotes that go quiet and never get followed up",
        "Price comparison against contractors who quote low and change order later",
    ],
    "judgment": "Follow up quotes twice on a schedule. Unfollowed estimates are "
                "the single largest source of lost revenue in renovation, and "
                "nobody wants to do it because it feels like chasing.",
    "watch": "Portfolio images must be your own work. Using supplier or stock "
             "imagery as project photos is a credibility problem when a client visits a reference site.",
}

SECTORS["Construction and development"] = {
    "division": "Trades",
    "lede": "Business to business, relationship-led, with very long cycles and few buyers who matter.",
    "context": [
        "Commercial construction is won through relationships, bid lists and "
        "reputation. Advertising rarely produces a project directly.",
        "What marketing does is make the firm credible when it is being "
        "considered. A developer checking a bidder looks at completed projects, "
        "capability and whether the firm looks like it will still exist in three years.",
    ],
    "buyer": "developers, owners, architects and procurement teams",
    "cycle": "six months to several years",
    "lead_ch": "content, project portfolio and targeted outreach rather than broad advertising",
    "challenges": [
        "Very small number of buyers who genuinely matter",
        "Cycles far longer than any attribution window",
        "Recruitment as pressing as business development",
    ],
    "judgment": "Spend the marketing budget on the project portfolio and on "
                "recruitment. In commercial construction, the constraint is "
                "usually capacity to deliver rather than opportunities to bid.",
    "watch": "Publishing project details can breach client confidentiality "
             "clauses. Get written approval before a project goes on the website.",
}

SECTORS["Property services"] = {
    "division": "Trades",
    "lede": "Split between genuine emergencies and recurring contracts, with very different economics.",
    "context": [
        "Restoration and damage work is urgent, insurance-funded and won by "
        "whoever responds first. Availability around the clock is the product.",
        "Cleaning, landscaping and maintenance are recurring contract "
        "businesses. One signed contract is worth years of revenue, which "
        "justifies an acquisition cost that looks absurd against a single job.",
    ],
    "buyer": "homeowners, property managers, insurers and commercial facility teams",
    "cycle": "immediate for emergencies, weeks to months for recurring contracts",
    "lead_ch": "search for emergency work, direct and content-led for commercial contracts",
    "challenges": [
        "Emergency response competing on speed alone",
        "Insurance and adjuster relationships driving much of the volume",
        "Recurring contracts valued as single jobs in the ad account",
    ],
    "judgment": "Model contract value over its full term when setting an "
                "acquisition target. A commercial cleaning contract worth years of "
                "revenue can justify spending many times what a single job would.",
    "watch": "Mold and asbestos work is licensed and the claims you can make "
             "about remediation are constrained. Check your jurisdiction before writing copy.",
}

SECTORS["Specialty contractors"] = {
    "division": "Trades",
    "lede": "Narrow niches with low search volume, where being findable at all is the advantage.",
    "context": [
        "These trades have small addressable search volume and few competitors "
        "advertising properly. A well-built page can own a niche outright.",
        "Most work is business to business, from general contractors and "
        "facility managers who need a specific capability on a specific project.",
    ],
    "buyer": "general contractors, developers and facility managers",
    "cycle": "days to weeks, driven by an active project",
    "lead_ch": "search, because the buyer is looking for a specific capability by name",
    "challenges": [
        "Low search volume making paid campaigns hard to scale",
        "Buyers who need proof of capability and certification",
        "Project-driven demand that cannot be forecast",
    ],
    "judgment": "Build one strong page per capability and certification. In "
                "narrow trades, the specific term with fifty monthly searches "
                "converts better than any broad category term.",
    "watch": "Certification and licensing claims get verified by commercial "
             "buyers. Only list what is current.",
}

SECTORS["Networks and business models"] = {
    "division": "Trades",
    "lede": "Multi-location and franchise operators, where the hard problem is coordination rather than demand.",
    "context": [
        "Once a trades business runs several locations, the marketing problem "
        "changes shape. Locations compete for the same searches, budget flows to "
        "whoever tracks best rather than whoever has capacity, and head office "
        "cannot see the real picture.",
        "Franchise systems add a second audience. The same marketing team is "
        "recruiting franchisees and generating customer demand, and those need different programs.",
    ],
    "buyer": "regional marketing directors, franchise development leads and operations executives",
    "cycle": "immediate for customer demand, six to eighteen months for franchise recruitment",
    "lead_ch": "structured local search per location, with paid social for franchise recruitment",
    "challenges": [
        "Locations bidding against each other for the same clicks",
        "Inconsistent business data across dozens of profiles",
        "Budget allocated by tracking quality rather than by capacity",
    ],
    "judgment": "Allocate budget by capacity, not by performance. The location "
                "with the best cost per lead is often the one with the least room "
                "to take more work.",
    "watch": "Franchise recruitment advertising is regulated as a financial "
             "offering in many jurisdictions. Earnings claims carry disclosure requirements.",
}

# ============================== DTC ==============================

SECTORS["Beauty and personal care"] = {
    "division": "DTC",
    "lede": "Creative-led, heavily reviewed, and constrained on what results you can show.",
    "context": [
        "Beauty buyers research through creators and reviews before they buy. "
        "The brand's own advertising matters less than what someone they trust said about it.",
        "Results imagery is restricted on the platforms that drive the category, "
        "so the creative has to sell texture, ingredients, routine and identity instead.",
    ],
    "buyer": "founders, brand directors and ecommerce leads",
    "cycle": "immediate for low ticket, weeks for higher priced devices and regimens",
    "lead_ch": "paid social and creator content, with search capturing branded and problem-led demand",
    "challenges": [
        "Before and after imagery restricted on the main platforms",
        "Crowded category with heavy discounting",
        "Repeat purchase assumed rather than measured",
    ],
    "judgment": "Build the replenishment flow before scaling acquisition. Beauty "
                "acquisition economics almost never work on the first order, and "
                "the second order is where the business is.",
    "watch": "Efficacy claims on skincare and cosmetics are regulated separately "
             "from ad policy. Clinical-sounding language invites scrutiny.",
}

SECTORS["Health and wellness"] = {
    "division": "DTC",
    "lede": "Strong repeat purchase economics, constant claims risk, and heavy platform restriction.",
    "context": [
        "Supplements and wellness products have genuine subscription economics. "
        "A customer on a replenishment cycle is worth many times the first order, "
        "which is what makes the acquisition maths work.",
        "The constraint is claims. What the product does, who it is for and what "
        "outcome is implied are all regulated, and platforms reject aggressively "
        "in this category.",
    ],
    "buyer": "founders and growth leads",
    "cycle": "immediate purchase, with a repeat cycle of thirty to ninety days",
    "lead_ch": "paid social for demand, search and marketplace for capture, email for the repeat",
    "challenges": [
        "Health claims restricting what creative can test",
        "Subscription churn after the second or third shipment",
        "Marketplace competition on identical formulations",
    ],
    "judgment": "Model the third order, not the first. If you do not know your "
                "repeat rate at ninety days, you do not know what you can afford to pay for a customer.",
    "watch": "Supplement claims are regulated by Health Canada and the FDA, and "
             "clearing Meta review says nothing about whether a regulator agrees.",
}

SECTORS["Food and beverage"] = {
    "division": "DTC",
    "lede": "Thin margins, heavy shipping costs, and a repeat cycle that has to be engineered.",
    "context": [
        "Shipping food is expensive and often refrigerated. Contribution margin "
        "after fulfilment is the number that decides whether the business can "
        "afford paid acquisition at all.",
        "Repeat purchase is the whole model. Consumable products with a "
        "predictable cycle can build real subscription revenue, and brands that "
        "do not build the replenishment flow are leaving the business on the table.",
    ],
    "buyer": "founders and ecommerce directors",
    "cycle": "immediate, with a repeat cycle tied to consumption rate",
    "lead_ch": "paid social for trial, email and SMS for repeat, retail as a parallel channel",
    "challenges": [
        "Shipping cost eating contribution margin",
        "Trial-to-repeat conversion assumed rather than measured",
        "Retail distribution competing with the direct channel",
    ],
    "judgment": "If contribution margin after shipping is under thirty percent, "
                "paid acquisition will not fix the business. Change the price, the "
                "pack size or the shipping model first.",
    "watch": "Nutrition and health claims on food are regulated and vary by "
             "market. Ingredient and sourcing claims get audited.",
}

SECTORS["Fashion and accessories"] = {
    "division": "DTC",
    "lede": "Returns and sizing quietly decide profitability more than acquisition cost does.",
    "context": [
        "Apparel return rates run high enough that reported revenue and actual "
        "revenue are meaningfully different numbers. Optimising to gross revenue "
        "produces decisions that lose money.",
        "Sizing confidence is the conversion lever. Detailed fit guidance, real "
        "measurements and reviews that mention fit reduce both returns and hesitation.",
    ],
    "buyer": "founders, ecommerce directors and brand leads",
    "cycle": "immediate for known brands, longer for higher ticket and considered purchases",
    "lead_ch": "paid social and creator content, with search on branded and category terms",
    "challenges": [
        "Return rates distorting reported performance",
        "Seasonal inventory pressure forcing discounting",
        "Sizing uncertainty suppressing conversion",
    ],
    "judgment": "Optimise to net revenue after returns. It is a real "
                "implementation job and it changes which campaigns look profitable.",
    "watch": "Sustainability claims are increasingly regulated. Vague "
             "environmental language is a growing enforcement target in several markets.",
}

SECTORS["Home and lifestyle"] = {
    "division": "DTC",
    "lede": "High ticket, long consideration, and shipping economics that shape the whole model.",
    "context": [
        "Furniture and large home goods are researched for weeks and shipped "
        "expensively. The decision involves measuring a room, comparing options "
        "and often a second person agreeing.",
        "That long window makes retargeting and email central rather than "
        "supplementary. Most of the revenue arrives well after the first visit.",
    ],
    "buyer": "founders, ecommerce directors and category managers",
    "cycle": "weeks to months for large items, days for small home goods",
    "lead_ch": "paid social for discovery, search for capture, email and retargeting for the long middle",
    "challenges": [
        "Freight and delivery cost on large items",
        "Long consideration cycles breaking attribution",
        "Returns that are expensive or impractical to accept",
    ],
    "judgment": "Show delivery cost and lead time on the product page. In "
                "furniture it is the number one abandonment cause and the easiest "
                "thing to fix that nobody wants to fix.",
    "watch": "Flammability, safety and materials standards apply to furniture "
             "and home textiles, and claims about them get checked.",
}

SECTORS["Baby kids and family"] = {
    "division": "DTC",
    "lede": "Safety-driven buying, intense review scrutiny, and a customer who ages out.",
    "context": [
        "Parents research safety obsessively and trust other parents far more "
        "than brands. Reviews, certifications and recall history carry the decision.",
        "The customer window is short. A brand serving newborns loses that "
        "customer within a couple of years, which makes the acquisition treadmill permanent unless the range extends.",
    ],
    "buyer": "founders and brand leads",
    "cycle": "days to weeks, with heavy review research",
    "lead_ch": "paid social and creator content, with search for safety and comparison queries",
    "challenges": [
        "Customers ageing out of the product range",
        "Safety certification questions dominating research",
        "Gifting demand that never becomes repeat purchase",
    ],
    "judgment": "Publish the safety testing and certifications prominently. It "
                "is what parents search for, it is what reviews discuss, and most "
                "brands bury it in a specifications tab.",
    "watch": "Children's product safety standards are strictly enforced and a "
             "recall in this category is existential. Claims must be exact.",
}

SECTORS["Pet and animal"] = {
    "division": "DTC",
    "lede": "Emotional buying, strong repeat purchase, and health claims that need care.",
    "context": [
        "Pet owners spend on their animals the way they spend on family, and "
        "they research food and supplements with real diligence.",
        "Consumables give the category genuine subscription economics. "
        "Accessories and hardware do not, and the two need different acquisition maths.",
    ],
    "buyer": "founders and ecommerce leads",
    "cycle": "immediate, with a repeat cycle for food and supplements",
    "lead_ch": "paid social and creator content, with search for problem-led queries",
    "challenges": [
        "Veterinary claims restricting what supplements can say",
        "Retail and marketplace competition on price",
        "Subscription churn after the trial period",
    ],
    "judgment": "Separate consumables from hardware in the reporting. Blending "
                "them produces an average acquisition cost that describes neither business.",
    "watch": "Health claims for animal products are regulated and veterinary "
             "language attracts scrutiny.",
}

SECTORS["Technology and electronics"] = {
    "division": "DTC",
    "lede": "Specification-driven comparison, high return rates, and short product lifecycles.",
    "context": [
        "Buyers compare specifications, read reviews and check compatibility "
        "before purchasing. The research is technical and the content has to match that.",
        "Product cycles are short. A range that was competitive eighteen months "
        "ago is being compared against newer hardware, and the marketing has to "
        "keep pace with the refresh.",
    ],
    "buyer": "founders, ecommerce directors and product marketing leads",
    "cycle": "days to weeks with heavy comparison research",
    "lead_ch": "search and marketplace for comparison intent, paid social for new product launches",
    "challenges": [
        "Compatibility questions blocking purchase",
        "Return rates on technical products",
        "Marketplace price competition on identical stock",
    ],
    "judgment": "Answer the compatibility question on the product page in plain "
                "language. It is the most common reason a technical purchase "
                "stalls and the easiest objection to remove.",
    "watch": "Performance claims, battery life and wireless certifications are "
             "all verifiable and all get challenged.",
}

SECTORS["Sports outdoor and hobby"] = {
    "division": "DTC",
    "lede": "Enthusiast buyers who know more than your marketing team does.",
    "context": [
        "These customers are deeply informed and quick to spot marketing that "
        "does not understand the activity. Credibility with the community is the "
        "entry requirement.",
        "Demand is often seasonal and event-driven, which concentrates the year "
        "into a few months and makes timing decisions expensive to get wrong.",
    ],
    "buyer": "founders and brand leads, frequently participants themselves",
    "cycle": "days to weeks, longer for high value equipment",
    "lead_ch": "community and creator content, with search for specific product and comparison queries",
    "challenges": [
        "Seasonal demand concentrating the year",
        "Enthusiast communities that reject inauthentic marketing",
        "Specialist retail competing on selection and expertise",
    ],
    "judgment": "Hire from the community or partner with people in it. In "
                "enthusiast categories, marketing that gets the details wrong does "
                "measurable damage to the brand.",
    "watch": "Safety equipment carries certification standards, and performance "
             "claims in sport get tested publicly by the community.",
}

SECTORS["Commerce models"] = {
    "division": "DTC",
    "lede": "Defined by how the business sells rather than what it sells.",
    "context": [
        "A subscription brand, a marketplace-first brand and a wholesale brand "
        "moving direct face different constraints even when the product is identical.",
        "The model decides the metrics. Subscription lives on churn and lifetime "
        "value, marketplace on fees and listing control, wholesale-to-direct on "
        "channel conflict with existing retail partners.",
    ],
    "buyer": "founders, growth leads and, in backed businesses, board-level stakeholders",
    "cycle": "varies entirely by model",
    "lead_ch": "depends on the model, which is the point",
    "challenges": [
        "Channel conflict between direct and existing retail partners",
        "Subscription churn hiding inside apparently healthy growth",
        "Marketplace dependency limiting control over the customer relationship",
    ],
    "judgment": "Pick the metric the model actually runs on and report it "
                "everywhere. Subscription businesses reporting revenue growth "
                "while churn climbs are describing a problem as an achievement.",
    "watch": "Subscription auto-renewal terms are increasingly regulated. "
             "Cancellation has to be as easy as signing up in a growing number of markets.",
}

# ============================== PROFESSIONAL SERVICES ==============================

SECTORS["Legal services"] = {
    "division": "Professional Services",
    "lede": "Among the most expensive advertising auctions anywhere, with matter value that justifies it.",
    "context": [
        "Legal search terms in competitive practice areas are among the most "
        "expensive in advertising. A single click can cost more than most "
        "businesses pay for a lead.",
        "It still works, because a signed matter can be worth thousands or far "
        "more. The discipline is refusing to bid on the terms that bring "
        "students, competitors and people seeking free advice.",
    ],
    "buyer": "managing partners and marketing directors",
    "cycle": "hours for urgent matters, months for corporate and estate work",
    "lead_ch": "paid search for urgent consumer matters, organic and referral for corporate work",
    "challenges": [
        "Extremely high cost per click in competitive practice areas",
        "Unqualified enquiries consuming intake capacity",
        "Response time deciding which firm gets the matter",
    ],
    "judgment": "Answer within five minutes during business hours or stop "
                "increasing the ad budget. In personal injury and family law the "
                "first firm to make contact signs a disproportionate share of matters.",
    "watch": "Law society advertising rules restrict comparative claims, "
             "guarantees, testimonials and specialisation language. Rules differ "
             "by province and state and they are enforced.",
}

SECTORS["Financial services"] = {
    "division": "Professional Services",
    "lede": "Trust-led, heavily regulated, and built on relationships that advertising can only start.",
    "context": [
        "People move money to people they trust. Advertising can create "
        "awareness and capture a moment of intent, but the decision usually "
        "involves a conversation and a referral.",
        "Compliance shapes everything. What can be claimed about performance, "
        "how risk must be disclosed and what requires review before publishing "
        "all constrain the marketing before it starts.",
    ],
    "buyer": "principals, marketing directors and compliance officers",
    "cycle": "three to twelve months for advisory relationships, faster for transactional products",
    "lead_ch": "content and organic search for trust building, paid search for transactional products",
    "challenges": [
        "Compliance review slowing everything down",
        "Long relationship cycles breaking attribution",
        "Differentiating from firms that all say the same thing",
    ],
    "judgment": "Publish the fee structure. In an industry where most firms "
                "obscure it, transparency about how you get paid is the most "
                "credible differentiator available.",
    "watch": "Performance claims, projections and testimonials are restricted by "
             "securities regulators. Marketing usually needs compliance sign-off before publishing.",
}

SECTORS["Insurance"] = {
    "division": "Professional Services",
    "lede": "Price comparison at the front, retention economics at the back.",
    "context": [
        "Personal lines shoppers compare quotes and choose on price, which makes "
        "acquisition expensive and loyalty thin.",
        "Commercial lines is a different business entirely. Longer cycles, "
        "relationship-led, larger accounts, and renewal revenue that makes the "
        "acquisition cost worthwhile over years rather than months.",
    ],
    "buyer": "brokerage principals and marketing leads",
    "cycle": "days for personal lines, months for commercial accounts",
    "lead_ch": "paid search for personal lines quotes, content and outbound for commercial",
    "challenges": [
        "Aggregators and direct writers dominating personal lines search",
        "Quote requests that shop and never convert",
        "Commercial accounts won through relationships advertising cannot reach",
    ],
    "judgment": "Model the renewal, not the first policy. An account retained "
                "for five years justifies an acquisition cost that looks "
                "indefensible against a single year's commission.",
    "watch": "Insurance advertising is regulated by provincial and state "
             "authorities, with rules on how coverage and pricing can be described.",
}

SECTORS["Accounting and tax"] = {
    "division": "Professional Services",
    "lede": "Sharply seasonal on the consumer side, steady and relationship-led on the business side.",
    "context": [
        "Personal tax work spikes into a few weeks and vanishes. Compressed "
        "demand, price sensitivity and heavy competition from software.",
        "Business advisory is the opposite: recurring, relationship-led and far "
        "more valuable. Most firms want more of the second and market as if they want the first.",
    ],
    "buyer": "partners and practice managers",
    "cycle": "days in tax season, months for advisory relationships",
    "lead_ch": "search during seasonal peaks, content and referral for advisory work",
    "challenges": [
        "Revenue concentrated into a short season",
        "Software competing at the low end of the market",
        "Advisory services marketed the same way as compliance work",
    ],
    "judgment": "Market the advisory work, not the tax return. Compliance is "
                "commoditised and getting worse. The firms growing are the ones "
                "selling ongoing advice to business owners.",
    "watch": "Professional body rules govern how accounting and audit services "
             "can be advertised, including what can be said about specialisation.",
}

SECTORS["Consulting and advisory"] = {
    "division": "Professional Services",
    "lede": "Expertise sold on credibility, where the individual matters more than the firm.",
    "context": [
        "Buyers hire a person more than an organisation. The named consultant's "
        "track record and thinking carry the decision, which makes personal "
        "authority the marketing asset.",
        "Engagements are large and infrequent. A firm might need a handful of "
        "new clients a year, which makes broad advertising a poor fit and "
        "targeted authority building a good one.",
    ],
    "buyer": "executives and boards",
    "cycle": "three to twelve months, often longer",
    "lede_note": "",
    "lead_ch": "thought leadership, speaking and targeted outreach rather than broad advertising",
    "challenges": [
        "Very small number of target buyers",
        "Differentiating from firms describing identical capabilities",
        "Cycles far longer than platform attribution windows",
    ],
    "judgment": "Build the individual consultants' profiles rather than the firm "
                "brand. Buyers search for people and their ideas, not for consultancies.",
    "watch": "Client confidentiality usually prevents naming engagements. Get "
             "written approval before a case study goes live.",
}

SECTORS["Technology and managed services"] = {
    "division": "Professional Services",
    "lede": "Recurring revenue, technical buyers and long procurement cycles with security review at the end.",
    "context": [
        "Managed services and B2B software both run on recurring revenue, which "
        "means the acquisition cost is judged against years of contract value "
        "rather than a first invoice.",
        "The buying process is technical and committee-driven. Security review, "
        "compliance documentation and integration questions arrive late and stall deals that looked closed.",
    ],
    "buyer": "IT directors, operations executives and procurement",
    "cycle": "three to eighteen months with multiple stakeholders",
    "lead_ch": "content and search for the research phase, targeted outbound for named accounts",
    "challenges": [
        "Security and compliance review arriving late in the cycle",
        "Committee buying where one objection stalls everything",
        "Contract value justifying spend that platform reporting cannot see",
    ],
    "judgment": "Publish security documentation, certifications and integration "
                "detail openly. It gets requested in every deal and making buyers "
                "ask adds weeks to the cycle.",
    "watch": "Security and compliance claims must be exactly accurate. "
             "Overstating a certification is a contractual and reputational problem.",
}

SECTORS["Real estate and property"] = {
    "division": "Professional Services",
    "lede": "Cyclical, local, and split between transaction businesses and recurring management contracts.",
    "context": [
        "Brokerage revenue moves with interest rates and inventory. The market "
        "decides volume and marketing decides share, which is a different "
        "conversation from the one most brokerages want to have.",
        "Property management is the stable counterweight. Recurring contracts, "
        "long relationships and acquisition economics that work over years.",
    ],
    "buyer": "brokerage owners, property management principals and firm leadership",
    "cycle": "weeks to months for transactions, months for management contracts",
    "lead_ch": "local search and social for transactions, direct and content for management contracts",
    "challenges": [
        "Market cycles driving volume more than marketing does",
        "Individual agents marketing against their own brokerage",
        "Recruitment competing with client acquisition for the same budget",
    ],
    "judgment": "In a slow market, spend on recruitment and retention rather "
                "than lead generation. Agents are the durable asset and they move "
                "when the market turns.",
    "watch": "Real estate advertising rules govern how listings, results and "
             "agent claims can be presented, and vary by regulator.",
}

SECTORS["Recruitment and people services"] = {
    "division": "Professional Services",
    "lede": "Two audiences at once, and most firms only market to one of them.",
    "context": [
        "Recruitment is a marketplace business. It needs employers with roles "
        "and candidates to fill them, and the constraint moves between the two "
        "depending on the labour market.",
        "Most firms market hard to employers and treat candidate attraction as "
        "job board spend, which is why they run short of candidates exactly when it matters.",
    ],
    "buyer": "agency owners, business development leads and talent directors",
    "cycle": "days for candidate response, months for employer relationships",
    "lead_ch": "paid social and job platforms for candidates, content and outbound for employers",
    "challenges": [
        "Balancing two audiences with one budget",
        "Candidate supply moving with the labour market",
        "Commoditisation and fee pressure from employers",
    ],
    "judgment": "Run candidate attraction as a performance marketing program, "
                "not as job board spend. Firms that build a candidate pipeline "
                "ahead of demand win the mandates their competitors cannot fill.",
    "watch": "Employment advertising is subject to human rights and equal "
             "opportunity rules on how roles can be described and targeted.",
}

SECTORS["Professional and regulated services"] = {
    "division": "Professional Services",
    "lede": "Technical credibility, certification requirements and buyers who verify everything.",
    "context": [
        "These firms are hired for certified technical capability. The buyer "
        "checks credentials, insurance and prior project experience before a "
        "conversation begins.",
        "Much of the work is project-driven and won through procurement, "
        "tenders and professional networks rather than through advertising.",
    ],
    "buyer": "project owners, developers, procurement teams and government departments",
    "cycle": "months, frequently through formal procurement",
    "lead_ch": "search on specific capability terms, supported by a credible project portfolio",
    "challenges": [
        "Procurement processes that advertising cannot influence",
        "Credentials and certifications requiring constant verification",
        "Narrow search volume for specific technical capabilities",
    ],
    "judgment": "Build a page for every certification and technical capability "
                "you hold. Buyers search the exact term, volume is low, and "
                "competition for it is almost nonexistent.",
    "watch": "Professional engineering, architecture and related titles are "
             "legally protected. Describing capability incorrectly is a regulatory issue, not a marketing one.",
}

SECTORS["Multi-location and network models"] = {
    "division": "Professional Services",
    "lede": "Several offices or partners under one brand, competing with each other by accident.",
    "context": [
        "Multi-office firms run into the same problems as multi-location "
        "retail: offices bidding against each other, inconsistent business data "
        "and no central view of which office actually needs work.",
        "Partner-led firms add a further complication. Individual partners "
        "build personal brands that may or may not point back to the firm.",
    ],
    "buyer": "firm-wide marketing directors, managing partners and network leadership",
    "cycle": "varies by practice, typically months",
    "lead_ch": "structured local search per office, with firm-level content and authority above it",
    "challenges": [
        "Offices competing for the same searches",
        "Inconsistent business data across locations and directories",
        "Partner personal brands disconnected from the firm",
    ],
    "judgment": "Give each office a real page with its own people, practice "
                "areas and local proof. Duplicated pages with the city swapped "
                "rank badly and convert worse.",
    "watch": "Multi-jurisdiction firms face different advertising rules in each "
             "one. Content has to state which jurisdiction it applies to.",
}
