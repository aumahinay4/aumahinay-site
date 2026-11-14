"""Public Finance series (Butch 2026-11-11), "Inside the Local Treasury"; dates follow the daily blog rotation (Butch 2026-11-14).

Each post takes a typical treasury situation and explains it in plain words. Cases are composites:
no real taxpayer, employee, office or amount is named. Facts are checked against official sources
before each post is approved; per Butch, the posts themselves show no Sources section.
"""

TREASURY_POSTS = [
    {
        "title": "Inside the Local Treasury, Part 3: The Cedula, a Spanish-Era Tax That Never Left",
        "date": "December 30, 2026",
        "publish_on": "2026-12-30 21:00",  # blog rotation, one series a day (Butch 2026-11-14)
        "slug": "the-cedula-explained",
        "category": "finance",
        "summary": "The cedula began under Spain, was torn up by the Katipunan, and is still asked for at offices "
                   "today. Here is what it really is, why the clerk asks about your income, and where paying it "
                   "helps your barangay most.",
        "body": [
            "A young woman fresh out of college stood at the treasury window holding a list of "
            "requirements for her first job. Near the top was one word: cedula. The clerk asked "
            "for her name, address and birthday, then one more thing. “Magkano po ang kita "
            "ninyo?” How much do you earn? She looked puzzled. Why would a small piece of paper "
            "need her income?",
            "(As in every part of this series, the case is a composite. No real person or amount "
            "is described.)",
            "It is a fair question, and the answer goes back almost a century and a half. By the "
            "end of this post, you will know where the cedula came from, how to compute what you "
            "owe, where paying it helps your barangay most, and what it can and cannot prove.",
            ("h", "A Tax Older Than the Republic"),
            "Under Spain, Filipinos paid a head tax called the tribute. Historian Filomeno V. "
            "Aguilar Jr. writes that Spain abolished it in 1884 and introduced the cédula "
            "personal in 1885, a tax whose rate depended on a person’s economic capacity. The "
            "paper itself was the proof that you had paid.",
            "That is why it became a symbol. In the last week of August 1896, Andrés Bonifacio "
            "and members of the Katipunan tore up their cedulas as a sign of revolt against "
            "Spanish rule. The exact date and place are still debated, but the act itself is "
            "taught in every Philippine history class.",
            "More than a century later, the name has survived. The law now calls it the community"
            " tax, and the paper is the community tax certificate, but most of us still say "
            "cedula.",
            ("h", "What You Actually Pay"),
            "The community tax is levied by cities and municipalities under Sections 156 to 164 "
            "of the Local Government Code. For an individual, it has two parts: a basic tax of "
            "₱5, and an additional ₱1 for every ₱1,000 of income from salary, business, "
            "profession or property. The additional part is capped at ₱5,000.",
            "So our new graduate, if she expects to earn ₱300,000 in a year, pays ₱5 plus ₱300, "
            "or ₱305. My study note on the community tax covers the full rules, including "
            "corporations, exemptions and the deadlines for people who turn 18 during the year.",
            ("cta", "Read the study note: Community tax (cedula)", "/study-notes/community-tax-cedula/"),
            ("h", "Why the Clerk Asks About Your Income"),
            "Like Spain’s cédula personal, today’s community tax still grows with what a person "
            "earns or owns. That is the reason for the question at the window. The amount is "
            "based on what you declare, and the clerk does not check your payslip.",
            "That makes it tempting to say a smaller number. But a cedula is a tax receipt with "
            "your name on it, and for a worker earning ₱300,000 a year, the honest amount is only"
            " ₱305. Declaring it properly is a small, real way of doing your share for the town "
            "you live in.",
            ("h", "Where and When to Pay"),
            "You pay in the city or municipality where you live. The tax for the year falls due "
            "on January 1 and should be paid by the last day of February. After that, unpaid "
            "community tax earns interest of 24% a year.",
            "If you live in one town and work in another, the cedula is still paid where you "
            "live, not where your office or business is. A corporation is different: it pays "
            "where its principal office is. Paying early in the year also avoids the interest, "
            "which keeps running for as long as the tax stays unpaid.",
            "Here is a detail few people know. The city or municipal treasurer may deputize "
            "bonded barangay treasurers to collect the community tax. What is collected through "
            "the barangay is split 50-50 between the town and the barangay where it was paid. If "
            "your barangay collects it, getting your cedula there leaves half of what you pay in "
            "your own barangay.",
            ("h", "What the Cedula Is Not"),
            ("point",
             "It is not an ID",
             "It shows that the tax for the year was paid. It does not prove who you are, since "
             "anyone can buy one by giving a name."),
            ("point",
             "It is not a clearance",
             "It says nothing about your record. Offices that need that ask for a barangay or "
             "police clearance instead."),
            ("point",
             "It is not needed to vote",
             "The Code says plainly that no certificate may be required to register as a voter."),
            ("point",
             "It is not a national tax",
             "The money stays with the city or municipality, and with the barangay when it helps collect."),
            ("h", "A Few Quick Examples"),
            ("point", "A tricycle driver earning ₱150,000 a year", "₱5 basic plus ₱150 additional, or ₱155"),
            ("point",
             "A professional earning ₱6 million a year",
             "The additional tax would be ₱6,000, but the cap is ₱5,000, so the total is ₱5,005"),
            ("point",
             "A small corporation",
             "₱500 basic, plus ₱2 for every ₱5,000 of real property and ₱2 for every ₱5,000 of "
             "gross receipts last year, with the additional part capped at ₱10,000"),
            "For a married couple, the additional tax is based on the total property they own and"
            " the combined earnings of both. Only two groups are exempt: diplomatic and consular "
            "representatives, and visitors staying in the country for no more than three months.",
            ("h", "Turning 18, or Moving In, Midyear"),
            "The law has simple cut-off dates for people who become liable during the year. If "
            "you turn 18, or stop being exempt, on or before June 30, you pay for that year. If "
            "it happens on or before March 31, you have 20 days to pay before you become "
            "delinquent. If it happens on or after July 1, you pay nothing for that year and "
            "start the next January.",
            "There is also a grace period for the certificate itself. From January 1 to April 15,"
            " an office may still accept last year’s cedula, which helps when the January lines "
            "are long.",
            ("h", "For Treasury Workers"),
            "Behind the window, the cedula has its own rules. The national government prints the "
            "certificates and distributes them through the city and municipal treasurers. A small"
            " part of the proceeds goes to the national government to cover printing and "
            "distribution, and the treasurer remits it within 10 days after the end of each "
            "quarter. Everything the city or municipal treasurer collects directly goes to the "
            "general fund.",
            "Barangay treasurers can collect only when deputized, and only if they are bonded. "
            "Because these are accountable forms, each certificate issued, spoiled or still on "
            "hand must be reported, like any official receipt.",
            ("h", "Bring an ID Too"),
            "Because the cedula proves payment and not identity, it is rarely enough on its own. "
            "Under the Supreme Court’s 2004 Rules on Notarial Practice, a notary public must see "
            "competent evidence of identity, such as a current government ID with your photo and "
            "signature. So when an office or a notary asks for your cedula, bring a valid ID as "
            "well.",
            "At the treasury window, it also helps to know your expected income for the year "
            "before you line up. The clerk only needs a number, but having it ready keeps the "
            "line moving for everyone behind you, especially in January and February, before the "
            "end-of-February deadline.",
            ("h", "Should It Still Exist?"),
            "People have asked this for years. In 2013, the Commissioner of Internal Revenue said"
            " in a news report that the cedula was no longer needed and was ripe for reform. On "
            "the other side, the community tax is steady local income, and for many barangays "
            "their half of the collection is money they can count on every January.",
            "That debate belongs to Congress. Until the law changes, the cedula remains a tax. "
            "The Code still lets offices ask for it when you sign a notarized document, take an "
            "oath of office, get a permit or license, or receive money from public funds.",
            ("h", "Key Takeaways"),
            ("point",
             "It grows with income",
             "₱5 basic plus ₱1 for every ₱1,000 of income, with the additional part capped at ₱5,000."),
            ("point",
             "Pay where you live, by February",
             "Unpaid community tax earns interest of 24% a year after the last day of February."),
            ("point",
             "Your barangay can keep half",
             "When a deputized, bonded barangay treasurer collects it, half stays in that barangay."),
            ("point",
             "It proves payment, not identity",
             "Bring a valid ID as well, especially for a notary."),
            ("h", "The Question to Ask"),
            "Does your barangay treasurer collect the community tax, and do residents know that "
            "paying there keeps half of it in the barangay? If you work in a treasury, it is "
            "worth asking whether your barangay treasurers are deputized and bonded before the "
            "January rush begins.",
            ("cta",
             "Read: Inside the Local Treasury, Part 1: Where Your Town's Money Comes From",
             "/blog/where-your-towns-money-comes-from/"),
            ("cta",
             "Read: Inside the Local Treasury, Part 2: The January Rush and Your Business Permit",
             "/blog/january-rush-business-permit/"),
            ("cta", "Read: Your Data at the Treasury Counter", "/blog/your-data-at-the-treasury-counter/"),
            ("ask", "Do you still keep your old cedulas? I'd like to hear when you last needed one."),
        ],
    },
    {
        "title": "Inside the Local Treasury, Part 2: The January Rush and Your Business Permit",
        "date": "December 25, 2026",
        "publish_on": "2026-12-25 21:00",  # blog rotation, one series a day (Butch 2026-11-14)
        "slug": "january-rush-business-permit",
        "category": "finance",
        "summary": "Every January the line for business permits stretches out the door, and some owners still "
                   "miss the deadline by a day. Here is why the rush happens, what being late really costs, "
                   "and how to get through it in one visit.",
        "body": [
            "One morning in late January, the owner of a small bakery reached the treasury window"
            " with a folder of papers and a tired smile. She had been in line since seven. When "
            "the clerk computed her business tax, there was an extra line on the bill: a "
            "surcharge. Her deadline had passed two days earlier. “Akala ko katapusan pa ng "
            "Enero,” she said. She thought it was the end of the month.",
            "(As in every part of this series, the case is a composite. No real person, business "
            "or amount is described.)",
            "A late payment like this can be avoided with three things: knowing the real "
            "deadline, knowing what you are paying for, and bringing the right papers. By the end"
            " of this post, you will know the real deadline, what being late costs in pesos, what"
            " to bring, and what to do if you believe the bill is wrong.",
            ("h", "Why Everything Happens in January"),
            "The local business tax is a yearly tax, and under the Local Government Code it "
            "becomes due on the first day of the year. It is paid within the first 20 days of "
            "January. An owner who prefers to pay by quarter can do that too, with each "
            "installment due within the first 20 days of its quarter.",
            "So the real deadline is January 20, not January 31. Because almost every business in"
            " town renews at the same time, the line is longest in the last few days before the "
            "20th.",
            "The tax is computed on what the business sold the year before. That is why the "
            "treasury asks for last year’s gross sales or receipts at renewal. My study note on "
            "business tax and the mayor’s permit walks through the rates and rules in detail.",
            ("cta",
             "Read the study note: Business tax and the mayor's permit",
             "/study-notes/business-tax-and-mayors-permit/"),
            ("h", "Two Payments, One Visit"),
            "Renewal involves two different payments, and owners often mix them up:",
            ("point",
             "The business tax",
             "A tax on the privilege of doing business, based on gross sales. It goes to the "
             "town’s general fund like any other tax."),
            ("point",
             "The regulatory fees",
             "Fees for the mayor’s permit and the inspections behind it. The law says these must "
             "be reasonable and in line with the actual cost of regulating."),
            "The Ease of Doing Business Act (RA 11032) pushed towns to handle both in one place. "
            "It requires a single unified application form and a Business One Stop Shop, where "
            "the treasury, the permit office and other offices work side by side. The Bureau of "
            "Fire Protection is also meant to sit in the same area, and barangay clearances can "
            "now be issued at the city or municipal hall.",
            ("h", "What Being Late Really Costs"),
            "The Code allows the sanggunian to charge a surcharge of up to 25% of the unpaid tax,"
            " plus interest of up to 2% a month, for no more than 36 months. Your town’s revenue "
            "code sets the actual rates.",
            "In our bakery’s case, say its first-quarter installment was ₱2,000. At the maximum "
            "rate, paying two days late added a surcharge of ₱500, and interest was added on top."
            " That is money the owner could have kept just by coming a week earlier.",
            "The sanggunian may extend the deadline for a good reason, but by no more than six "
            "months. If your town announces an extension, it will be by ordinance or resolution, "
            "so check the town’s official page or the treasury before you rely on a rumor in the "
            "line.",
            ("h", "Declare Sales Honestly"),
            "It can be tempting to report lower sales to pay a lower tax. It is a poor bet. The "
            "treasurer may examine a business’s books once every tax period, and unpaid taxes can"
            " be assessed for up to five years after they fell due, or ten years when there was "
            "fraud. An underpayment found later comes back with surcharge and interest attached.",
            "Keeping simple records, such as your official receipts, sales book and bank "
            "deposits, also makes the declaration quick to prepare and easy to defend.",
            ("h", "What to Bring"),
            "Each town sets its own list, so check with your treasury or Business One Stop Shop. "
            "Expect to be asked for these:",
            ("point",
             "Last year’s permit and official receipts",
             "They show what you paid and help the clerk find your record."),
            ("point",
             "Your gross sales for last year",
             "Usually a written declaration, supported by your records or your filed tax returns."),
            ("point",
             "The unified application form",
             "Filled in, signed, and with any changes to your address, owner or line of business."),
            ("point",
             "Clearances your town requires",
             "Such as the barangay clearance and the fire safety inspection, which can often be "
             "handled at the same one-stop shop."),
            ("h", "Putting Numbers on It"),
            "Here is how the bakery’s bill could look, using the maximum rates in the Code. Your "
            "town’s revenue code may set lower ones.",
            ("point", "Last year’s gross sales", "₱400,000, taxed as a retailer at up to 2%"),
            ("point", "Business tax for the year", "₱400,000 × 2% = ₱8,000, or ₱2,000 a quarter"),
            ("point", "Surcharge for paying late", "₱2,000 × 25% = ₱500"),
            ("point",
             "Interest",
             "Up to 2% a month on ₱2,500 (the tax plus the surcharge), or up to ₱50 for each month"),
            "Paying on January 20 would have cost ₱2,000. Paying on January 22 cost at least "
            "₱2,500, and more once interest is added. On top of that, the regulatory fees for the"
            " mayor’s permit are paid as usual.",
            ("h", "If You Disagree With the Bill"),
            "Mistakes happen on both sides of the window. If the treasurer sends you a notice of "
            "assessment that you believe is wrong, you may file a written protest within 60 days "
            "of receiving it. The treasurer has 60 days to decide. If the protest is denied, or "
            "not acted on within those 60 days, you have 30 days to bring the case to court.",
            "If you paid more than you should have, you can ask the treasurer for a refund or a "
            "tax credit. File the claim in writing, and keep in mind that no case can be filed in"
            " court more than two years after the payment. Keep your official receipts; they are "
            "your best evidence.",
            ("h", "Closing or Moving the Business"),
            "A business that stops operating is not simply removed from the list. The owner files"
            " a sworn statement of gross sales for the year and pays any tax still due before the"
            " business is officially retired. Skipping this step can leave unpaid taxes, "
            "surcharges and interest piling up on a business that no longer exists.",
            "A branch or sales outlet that records its own sales pays the tax where it is "
            "located. If you open a second store in another town, that town is where its sales "
            "are taxed.",
            ("h", "How to Beat the Line"),
            "Go in the first two weeks of January, not the last three days before the 20th. Ask "
            "whether your town accepts applications online, since the law requires towns to "
            "automate the process. If cash is tight after the holidays, pay by quarter instead of"
            " risking a late annual payment. The law also sets processing times for government "
            "offices: three working days for a simple application and seven for a complex one.",
            ("h", "Before You Leave the Window"),
            "A few seconds of checking can save a second trip:",
            ("point",
             "Read the official receipt",
             "Your name, business name, address and the amount should be correct before you walk away."),
            ("point",
             "Keep it safe",
             "Store the receipt with your permit, and take a photo as a backup. Next January, it "
             "is the first thing the clerk will ask for."),
            ("point",
             "Mark the next due dates",
             "If you pay by quarter, the next installments are due within the first 20 days of "
             "April, July and October."),
            ("point",
             "Check the permit details",
             "The line of business and address on the permit should match what you actually do "
             "and where you do it."),
            ("h", "Key Takeaways"),
            ("point",
             "The deadline is January 20",
             "Business tax is due within the first 20 days of January, or of each quarter if you "
             "pay by installment."),
            ("point",
             "Late costs more than you think",
             "Your town may add a surcharge of up to 25% and interest of up to 2% a month."),
            ("point",
             "Declare sales honestly",
             "Underpayments can be assessed for up to five years, or ten when there was fraud."),
            ("point",
             "Know your remedies",
             "Protest an assessment in writing within 60 days, and claim a refund within two "
             "years of payment."),
            ("h", "The Question to Ask"),
            "When is your business tax actually due, and do you have last year’s sales ready "
            "today? If you work in a treasury, a good question for your office is this: does our "
            "town announce the January 20 deadline early and clearly, before the line forms?",
            ("cta",
             "Read: Inside the Local Treasury, Part 1: Where Your Town's Money Comes From",
             "/blog/where-your-towns-money-comes-from/"),
            ("cta", "Read: Inside the Local Treasury, Part 3: The Cedula", "/blog/the-cedula-explained/"),
            ("cta", "Read: Year-End in the Treasury", "/blog/year-end-in-the-treasury/"),
            ("ask",
             "Have you ever been caught by the January deadline? I'd be glad to hear how your "
             "town handles the rush."),
        ],
    },
    {
        "title": "Inside the Local Treasury, Part 1: Where Your Town's Money Comes From",
        "date": "December 20, 2026",
        "publish_on": "2026-12-20 21:00",  # blog rotation, one series a day (Butch 2026-11-14)
        "slug": "where-your-towns-money-comes-from",
        "category": "finance",
        "summary": "Taxes are collected at the town hall every day, yet the money never seems enough. The reason "
                   "is in one ratio most residents have never seen: how much of the town's income it raises "
                   "on its own.",
        "body": [
            "A few weeks after taking office, a new barangay council member came to the treasury "
            "with a simple question. The town collects taxes every working day, so why is there "
            "never enough money for the road in their barangay? It is a fair question, and it "
            "deserves a better answer than “walang pondo.” The answer starts with where the money"
            " actually comes from. By the end of this post, you will be able to read the one "
            "ratio that explains much of the answer, see why the national share can fall without "
            "warning, and know what actually raises a town's own income.",
            "(The cases in this series are composites of situations that come up in many treasury"
            " offices. Names, places and amounts are changed or left out.)",
            ("h", "Two Kinds of Money"),
            "Every local government has two broad kinds of income. The first is money it raises "
            "itself. The Bureau of Local Government Finance (BLGF) calls this locally sourced "
            "revenue. It includes real property tax, business tax, other local taxes, regulatory "
            "fees and service charges. It also includes income from economic enterprises, such as"
            " a public market or a slaughterhouse.",
            "The second is money that comes from outside. The biggest part is the town's share in"
            " national taxes, now called the National Tax Allotment (NTA). Smaller amounts may "
            "come from a share in national wealth, such as mining or energy found in the area, "
            "and from grants and transfers.",
            "If you want the legal details of who may tax what, my study note on sources of local"
            " revenue goes through them one by one. Here the question is simpler: how big is each"
            " part?",
            ("cta",
             "Read the study note: Sources of local revenue",
             "/study-notes/sources-of-local-revenue/"),
            ("h", "The One Ratio Worth Knowing"),
            "Take your town's total income for one year and ask what share of it came from the "
            "National Tax Allotment. BLGF has long called this dependency on the allotment. Here "
            "is a simple example, with round numbers for a made-up town:",
            ("point", "Total income for the year", "₱200 million"),
            ("point", "National Tax Allotment", "₱150 million"),
            ("point",
             "Locally sourced revenue",
             "₱45 million, from real property tax, business tax, fees and market income"),
            ("point", "Other receipts", "₱5 million, such as interest and miscellaneous income"),
            "In this example, the allotment is 75% of everything the town receives. Only about 23"
            " centavos of every peso comes from the town's own taxpayers. The numbers are "
            "invented, but the shape is familiar: for many municipalities, the allotment is the "
            "largest single source of income.",
            ("h", "Why the Allotment Can Fall"),
            "A town's allotment does not depend on how well the town collects. Under Section 284 "
            "of the Local Government Code, it is based on national tax collections in the third "
            "fiscal year before the current one. Since the Mandanas-Garcia ruling, that base "
            "covers all national taxes, and the bigger share has been released since fiscal year "
            "2022.",
            "The three-year lag matters. In June 2022, the Department of Budget and Management "
            "announced that the allotment for 2023 would be ₱820.27 billion, 14.47% lower than in"
            " 2022. The reason was simple: the 2023 share was computed from 2020 collections, the"
            " first year of the pandemic. The same memorandum urged local governments to make "
            "full use of their own powers to raise revenue.",
            "A town that relies on the allotment for three-quarters of its income feels a cut "
            "like that directly, and it arrives years after the cause, when everyone has already "
            "moved on.",
            ("h", "How the Allotment Is Divided"),
            "The national share is divided before it reaches any town hall. Under Section 285 of "
            "the Local Government Code, provinces as a group get 23%, cities 23%, municipalities "
            "34% and barangays 20%. Within each group, a province, city or municipality’s slice "
            "depends on three things: its population (50%), its land area (25%), and an equal "
            "share for everyone (25%).",
            "Barangays follow their own rule, set in the same section of the Code. Each barangay "
            "with at least 100 residents receives at least ₱80,000 a year. The rest of the "
            "barangay share is divided 60% by population and 40% equally.",
            "This is why two towns of similar size can receive very different amounts. Population"
            " counts for half of the formula, and it comes from the census. For 2023, DBM used "
            "the 2020 census for population and the 2001 master list of land area from the Land "
            "Management Bureau. A town that grows will see a bigger share only after a new census"
            " is used.",
            ("h", "The Year the Allotment Jumped"),
            "The Mandanas-Garcia ruling showed how much the base matters. In 2022, the first year"
            " of the wider base, the allotment for all local governments came to about ₱959 "
            "billion, and municipalities as a group shared ₱326.07 billion of it. The very next "
            "year, the total fell to about ₱820 billion because 2020 collections were low.",
            "Two years, two very different budgets, and neither change had anything to do with "
            "how well any single town collected its own taxes. For a treasurer preparing the "
            "income estimates, that is the lesson: the allotment can be planned for, but it "
            "cannot be controlled.",
            ("h", "Where the Road Project Went"),
            "Back to the question at the counter. Much of the town's income is already committed "
            "before the year begins. Employees must be paid. At least 20% of the allotment must "
            "go to development projects, a rule I wrote about in Principle 7 of the ALTOS "
            "Framework. The services the town now runs on its own, from health to agriculture, "
            "need their share too.",
            "What remains is small, and every barangay asks for part of it. Money collected at "
            "the window also does not go straight to a project. It is deposited in the right fund"
            " and can only be spent once the budget provides for it. A road waits for a place in "
            "the town's investment program and its annual budget, not for a good day of "
            "collections.",
            ("h", "What Actually Raises Local Income"),
            "Raising local income does not have to mean a new tax. Often it means doing the basics well:",
            ("point",
             "Records that match reality",
             "Tax declarations should show what is actually on the land, including new buildings "
             "and improvements."),
            ("point",
             "Collecting what is already owed",
             "Unpaid real property tax and business tax are income the town has already earned on paper."),
            ("point",
             "A complete list of businesses",
             "Every store that operates should hold a permit and pay its business tax, so honest "
             "payers do not carry the rest."),
            ("point",
             "A revenue code that is kept current",
             "Rates and fees should be reviewed from time to time, within the limits the Local "
             "Government Code allows."),
            ("point",
             "Paying made easy",
             "Clear schedules, short lines and simple requirements bring in more taxpayers on time."),
            "None of this is glamorous. But each peso the town raises on its own is a peso it can"
            " plan for, whatever happens to national collections three years from now.",
            ("h", "What Residents Can Do"),
            ("point",
             "Pay on time",
             "Real property tax and business tax paid on time are money the town can count on, "
             "unlike a share that moves with national collections."),
            ("point",
             "Be counted",
             "Population drives half of the allotment formula. Taking part in the census is one "
             "of the simplest ways to help your town’s share."),
            ("point",
             "Ask about the numbers",
             "Budget hearings and barangay assemblies are open to residents. Asking how much the "
             "town raised on its own is a fair and useful question."),
            ("h", "Where to See Your Town's Numbers"),
            "Local treasurers report their income and spending to BLGF through the Statement of "
            "Receipts and Expenditures (SRE). Quarterly reports are due by the 20th of the month "
            "after the quarter, followed by a year-end report. BLGF uses these reports to track "
            "how local governments are doing and publishes consolidated figures for the public.",
            ("h", "Key Takeaways"),
            ("point",
             "Know the ratio",
             "Divide the National Tax Allotment by total income to see how much of your town's "
             "money comes from outside."),
            ("point",
             "The allotment follows national collections",
             "It is based on taxes collected three years earlier, so it can fall even when your "
             "town collects well."),
            ("point",
             "Being counted matters",
             "Population is half of the formula, and it comes from the census."),
            ("point",
             "Local income is the part a town controls",
             "Accurate records, collecting what is owed and easy payment can raise it without a new tax."),
            ("h", "The Question to Ask"),
            "Of every peso your town received last year, how many centavos came from its own "
            "taxpayers? If you work in a treasury, you can answer that from your own SRE. If you "
            "are a resident, it is a good question to bring to a barangay assembly or a public "
            "budget hearing.",
            ("cta",
             "Read: Inside the Local Treasury, Part 2: The January Rush and Your Business Permit",
             "/blog/january-rush-business-permit/"),
            ("cta",
             "Read: ALTOS Principle 7, Keep Money in Its Fund",
             "/blog/altos-framework-keep-money-in-its-fund/"),
            ("cta", "Read: Year-End in the Treasury", "/blog/year-end-in-the-treasury/"),
            ("ask", "Did your town's ratio surprise you? I'd be glad to hear what you found."),
        ],
    },
]
