"""Public Finance series (Butch 2026-11-11), "Inside the Local Treasury"; dates follow the daily blog rotation (Butch 2026-11-14).

Each post takes a typical treasury situation and explains it in plain words. Cases are composites:
no real taxpayer, employee, office or amount is named. Facts are checked against official sources
before each post is approved; per Butch, the posts themselves show no Sources section.
"""

TREASURY_POSTS = [
    {
        "title": "Inside the Local Treasury, Part 34: Raising a Tax Rate, the Once-in-Five-Years Rule",
        "slug": "adjusting-local-tax-rates",
        "category": "finance",
        "date": "May 31, 2027",
        "summary": "A local government cannot raise its tax rates whenever it wants. Section 191 of the Local "
                   "Government Code allows an adjustment not more than once every five years, and never more than "
                   "10 percent of the rates fixed in the Code. This part explains the rule, the publication steps "
                   "that follow, and the treasury’s work before and after a new rate takes effect.",
        "publish_on": "2027-05-31 21:00",
        "body": [
            "The draft ordinance raised the tax on one class of business by 15 percent. A council member had "
            "worked hard on it. The new revenue would pay for a second ambulance.",
            "The treasurer’s note on the draft was one line long: “Section 191 limits the adjustment to 10 "
            "percent, and the last adjustment was three years ago.” Both problems meant the draft could not pass "
            "as written.",
            "(The local government, the ordinance and the figures are invented for this post. The sections of "
            "the Local Government Code quoted below are real.)",
            "Part 33 looked at private partners who build public facilities. This part returns to a local "
            "government’s own taxing power and one of its limits. After this post, you will know what Section "
            "191 allows, how to compute the most a rate can rise, how often it can happen, what must be done "
            "after the ordinance passes, and what the treasury contributes at each step.",
            ("photo", "blog/finance-rate-adjust.jpg", "Adjusting a local tax rate: not more often than once in "
             "five years, never more than 10 percent of the rate fixed in the Code, and published before it "
             "takes effect. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "What Section 191 Says"),
            "Section 191 of the Local Government Code gives local governments “the authority to adjust the tax "
            "rates as prescribed herein not oftener than once every five (5) years, but in no case shall such "
            "adjustment exceed ten percent (10%) of the rates fixed under this Code.”",
            "Two limits are packed into that sentence.",
            ("point", "How often", "Not more than once every five years."),
            ("point", "How much", "The adjustment may not exceed 10 percent of the rate fixed in the Code."),
            ("h", "Working Out the Ceiling"),
            "The 10 percent is a share of the rate fixed in the Code, not ten percentage points. A small example "
            "shows the difference.",
            ("point", "Rate fixed in the Code", "Suppose it is 1 percent of gross receipts."),
            ("point", "Most the adjustment can be", "10 percent of 1 percent, which is 0.1 percentage point."),
            ("point", "Highest adjusted rate", "1.1 percent."),
            ("point", "What it is not", "11 percent, which would be adding ten percentage points."),
            "The draft in the story asked for 15 percent more than the current rate, which was already the rate in the Code. That was beyond the "
            "ceiling, before the five-year question was even asked.",
            ("h", "Counting the Five Years"),
            ("point", "Keep the history", "The treasury should keep a list of every tax ordinance, the rates it "
             "set and the date each took effect."),
            ("point", "Check before drafting", "Before a new adjustment is proposed, find the date of the last "
             "one for that tax."),
            ("point", "Write the date in the draft", "A whereas clause naming the last adjustment and its date "
             "saves the sanggunian from checking it again."),
            "In the story, the last adjustment had taken effect three years earlier. The earliest a new one could "
            "be considered was two years away.",
            ("photo", "blog/finance-rate-adjust-steps.jpg", "From draft to new rate: check the five-year date and "
             "the 10 percent ceiling, hold public hearings, approve, publish within ten days, and furnish copies "
             "to the treasurer. Figures are invented. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Public Hearings Come First"),
            "Any tax ordinance, including an adjustment, needs public hearings before it is enacted. Part 15 "
            "explained Section 187, which requires those hearings, and how an ordinance can be appealed. Part "
            "28 covered what local governments cannot tax at all.",
            ("h", "After Approval: Publication"),
            "Section 188 sets the next step. Within ten days after approval, certified true copies of tax "
            "ordinances and revenue measures “shall be published in full for three (3) consecutive days in a "
            "newspaper of local circulation.”",
            ("point", "No local newspaper?", "The same section allows posting “in at least two (2) conspicuous "
             "and publicly accessible places.”"),
            ("point", "Copies to the treasurer", "Section 189 says copies of all tax ordinances and revenue "
             "measures “shall be furnished the respective local treasurers for public dissemination.”"),
            "The treasurer is the official the Code names to help the public learn about the new rate. The "
            "counter is one of the first places taxpayers will hear about it.",
            ("h", "The Treasury’s Work Before the Vote"),
            ("point", "Estimate the revenue", "Apply the proposed rate to last year’s tax base, business by "
             "business if possible. Part 31 showed how estimates are built."),
            ("point", "Check the limits", "Five years and 10 percent, for every rate in the draft."),
            ("point", "Look at the burden", "Show how much more a typical small, medium and large taxpayer "
             "would pay in a year."),
            ("h", "The Treasury’s Work After Approval"),
            ("point", "Update the systems", "Change the rate tables in the billing system or spreadsheet, and "
             "test a few computations by hand."),
            ("point", "Update the forms and notices", "Assessment forms, the counter signboard and the "
             "office’s posted schedule of rates."),
            ("point", "Brief the counter staff", "One page with the old and new rates and the effective date."),
            ("point", "Record the date", "Add the new ordinance to the history list, so the next five-year "
             "check is easy."),
            ("h", "A Worked Estimate"),
            "Suppose one class of business is taxed at 1 percent of gross receipts, the rate in the Code, under the current ordinance.",
            ("point", "The tax base", "120 businesses with total gross receipts of ₱300,000,000 last year."),
            ("point", "At the current rate", "₱300,000,000 × 1 percent = ₱3,000,000."),
            ("point", "At the highest adjusted rate", "₱300,000,000 × 1.1 percent = ₱3,300,000, or ₱300,000 "
             "more a year."),
            ("point", "For a small business", "Gross receipts of ₱1,200,000 would pay ₱12,000 now and ₱13,200 "
             "after the adjustment, ₱1,200 more a year."),
            "Numbers like these let the sanggunian weigh the extra revenue against the extra burden in pesos, "
            "not in percentages that are easy to misread.",
            ("h", "Taxes, Not Fees"),
            "Section 191 speaks of tax rates. Fees and charges follow their own rules, including the "
            "requirement that regulatory fees be reasonable and in proportion to the cost of regulation, "
            "inspection and licensing, which Part 15 explained. Check which kind of "
            "revenue a draft changes before applying the five-year rule.",
            ("h", "Back to the Ambulance"),
            "The council member asked what was possible. The treasurer’s estimate showed that collecting the "
            "existing tax better, starting with the oldest delinquent accounts listed in Part 30’s action plan, "
            "could raise a similar amount within a year without any rate change.",
            "The draft was set aside, and the collection drive began that quarter. Two years later, when the five-year period had passed, a smaller "
            "adjustment within the 10 percent ceiling went through hearings, publication and the counter "
            "briefing without a single problem. By then, the second ambulance had already been bought from the better collections.",
            ("h", "Mistakes to Avoid"),
            ("point", "Confusing percent with percentage points", "10 percent of a 1 percent rate is 0.1 point."),
            ("point", "Forgetting the last adjustment", "Keep a dated history of every tax ordinance."),
            ("point", "Skipping publication", "An ordinance must be published or posted as Section 188 requires."),
            ("point", "Changing the rate but not the system", "Update the billing tables and test them."),
            ("h", "Key Takeaways"),
            ("point", "Once every five years", "At most, under Section 191."),
            ("point", "Ten percent of the Code’s rate", "A share of the rate, not ten points."),
            ("point", "Hearings, then publication", "Within ten days of approval, for three consecutive days."),
            ("point", "The treasurer disseminates", "Section 189 furnishes copies for public dissemination."),
            ("h", "Your Part 34 Action Plan"),
            ("point", "If you work in a treasury", "Build a dated list of every tax ordinance and the rates it "
             "set."),
            ("point", "If you sit in the sanggunian", "Ask for the date of the last adjustment and the 10 percent "
             "ceiling before debating any new rate."),
            ("point", "If you are a business owner", "Ask the treasurer’s office for the current schedule of "
             "rates and the ordinance that set them."),
            ("cta", "Read: Inside the Local Treasury, Part 28: What Local Governments Cannot Tax, the Limits in Section 133", "/blog/what-local-governments-cannot-tax/"),
            ("cta", "Read: Inside the Local Treasury, Part 15: Fee or Tax? Why the Difference Matters", "/blog/fee-or-tax/"),
            ("cta", "Read: Inside the Local Treasury, Part 31: Estimating Next Year’s Income, the Numbers Behind the Budget", "/blog/estimating-next-years-income/"),
            ("cta", "Read: Data Analytics Series, Part 30: Percent Change or Percentage Points? Reporting Growth Without Confusion", "/blog/data-analytics-part-30-percent-change/"),
            ("ask", "When did your local government last adjust its tax rates?"),
        ],
    },
    {
        "title": "Inside the Local Treasury, Part 33: When a Private Partner Builds, Local PPPs Under the 2023 Code",
        "slug": "local-public-private-partnerships",
        "category": "finance",
        "date": "May 28, 2027",
        "summary": "A local government can let a private company build and run a facility, such as a terminal or "
                   "a market, under a public-private partnership. Since the PPP Code of 2023, local projects are "
                   "confirmed by the local development council and approved by the sanggunian. This part explains "
                   "the basics and what the treasury should watch: promises the government makes, money it "
                   "receives, and records it must keep.",
        "publish_on": "2027-05-28 21:00",
        "body": [
            "The bus terminal had outgrown its lot ten years ago. A loan would take most of the local "
            "government’s borrowing room, as Part 29 explained. Then a private company offered to build a new "
            "terminal, run it for 25 years, and share the fees with the local government.",
            "The mayor liked the idea. The treasurer had questions: who collects the fees, how the share is "
            "checked, and what the local government promises to pay if the terminal earns less than expected.",
            "(The terminal, the company and the figures are invented for this post. The rules quoted below come "
            "from Republic Act No. 11966, the Public-Private Partnership Code of the Philippines.)",
            "Part 32 looked at a fund set aside by law. This part looks at a way to build public facilities with "
            "private money. By the end, you will know what a local PPP project is, who approves it, what a "
            "government undertaking is, and the questions a treasury should ask before and after the contract "
            "is signed.",
            ("photo", "blog/finance-ppp.jpg", "A local public-private partnership: a private partner builds and "
             "runs a facility, the local government approves and oversees it, and the treasury tracks every "
             "promise and every peso. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "A New Code Since 2023"),
            "Republic Act No. 11966 was approved on December 5, 2023. It brought the rules for public-private "
            "partnerships into one code. Its repealing clause lists Republic Act No. 6957, the old "
            "Build-Operate-and-Transfer Law, as amended by Republic Act No. 7718, among the laws repealed or "
            "modified.",
            "The Code also says that after it took effect, no other PPP guidelines, codes or ordinances may be "
            "used to enter into partnerships, except those made in accordance with the Code and its "
            "implementing rules. A local government that had its own PPP ordinance should check it against the "
            "Code.",
            ("h", "What Counts as a Local PPP Project"),
            "The Code defines a local PPP project as “a PPP Project that is undertaken by LGUs and LUCs,” "
            "meaning local governments and local universities and colleges. A PPP project, in turn, covers "
            "public infrastructure or development projects and services carried out under the Code.",
            ("point", "Examples", "A transport terminal, a public market, a water system or a waste facility, "
             "built or run by a private partner under a contract with the local government."),
            ("point", "Not a simple purchase", "Buying supplies or hiring a contractor to build a road the local "
             "government will run itself is ordinary procurement, not a PPP."),
            ("h", "Who Approves"),
            "Section 7 of the Code sets the approving bodies.",
            ("point", "The local development council confirms", "“Prior to approval, Local PPP Projects "
             "implemented by LGUs shall be confirmed by the respective local development councils.”"),
            ("point", "The sanggunian approves", "“Local PPP Projects shall be approved by the respective local "
             "Sanggunians in the case of LGUs.”"),
            ("point", "National funds need national review", "If national government funds are involved, the "
             "proposed government undertaking goes to the national review body named in the Code."),
            ("point", "Unsolicited proposals", "A proposal that comes from a private company, like the terminal "
             "offer, is submitted to the PPP Center to check that it is complete, under Section 10."),
            ("h", "Government Undertakings: The Promises"),
            "The Code defines government undertakings as “any form of contribution and/or support, which the "
            "government may extend to a Private Partner” for a PPP project. These are the part the treasury "
            "must watch most closely.",
            ("point", "Land or rights of way", "The local government provides the lot."),
            ("point", "Payments", "The local government pays the partner a fixed amount each year, for example "
             "for a facility the public uses for free."),
            ("point", "Guarantees", "The local government promises to cover a shortfall if fees fall below a "
             "set level."),
            "Each promise is a future claim on local money. A guarantee may cost nothing for years, then a great "
            "deal in a bad one.",
            ("photo", "blog/finance-ppp-checks.jpg", "What the treasury tracks in a local PPP: promises the "
             "local government made, money due to it, and the records that prove both. Figures are invented. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Questions the Treasury Should Ask Before Signing"),
            ("point", "What exactly do we promise to pay, and when?", "Each payment should appear in a schedule "
             "that the budget office can plan around, year by year."),
            ("point", "What could we owe in a bad year?", "Work out the worst case of any guarantee. Part 31 "
             "showed why estimates must be realistic."),
            ("point", "Who collects the fees?", "If the partner collects, how will the local government’s share "
             "be computed, paid and checked?"),
            ("point", "What records will we receive?", "Monthly reports, audited statements, ticket counts. The "
             "contract should name them and their deadlines."),
            ("point", "What happens at the end?", "Who owns the facility, and in what condition it must be "
             "handed over."),
            ("h", "After Signing: The Treasury’s Routine"),
            ("point", "Record the revenue share", "Issue official receipts for every payment received, as for "
             "any other local income."),
            ("point", "Check it against the reports", "Compare the share paid with the partner’s reported "
             "collections. Part 37 of the Business Intelligence Series showed how to find the few causes behind "
             "most of a gap."),
            ("point", "Keep a register of promises", "List every government undertaking, its amount, its "
             "trigger and its due date."),
            ("point", "Flag the triggers early", "If fees are trending toward a guarantee level, tell the budget "
             "office before the year’s budget is set."),
            ("h", "Back to the Terminal"),
            "The terminal offer included a guarantee: if annual fees fell below ₱12,000,000, the local "
            "government would pay the difference. The local government’s share was expected to be about "
            "₱1,800,000 a year. The treasurer worked out that if fees fell to ₱8,000,000 in a bad year, for "
            "example during a long road closure, the local government would owe the partner ₱4,000,000, more "
            "than two years of its expected share.",
            "The proposal went back for changes before reaching the development council. The final version "
            "replaced the guarantee with a longer term, and the treasury’s register of promises showed a single "
            "line: land provided, no payments due.",
            ("h", "Where to Get Help"),
            "Local governments do not have to work out a partnership alone.",
            ("point", "The PPP Center", "The national agency that receives unsolicited proposals under the Code "
             "also publishes guidelines for local projects on its website."),
            ("point", "Your own offices", "The planning office prepares the project, the legal office reviews "
             "the contract, the budget office plans the payments, and the treasury tracks what is promised and "
             "received. Part 20 described who does what in the treasurer’s office."),
            "A partnership touches every one of these offices for many years, so each should see the contract "
            "before it is signed.",
            ("h", "Mistakes to Avoid"),
            ("point", "Seeing only the free building", "Read every promise the local government makes in return."),
            ("point", "No worst case", "Price each guarantee before approval, not after the first bad year."),
            ("point", "Trusting reports without checking", "Compare the share paid with the partner’s numbers."),
            ("point", "Using an old local PPP ordinance", "Check it against the 2023 Code."),
            ("h", "Key Takeaways"),
            ("point", "One code since 2023", "Republic Act No. 11966 replaced the old BOT Law framework."),
            ("point", "Council confirms, sanggunian approves", "For local PPP projects of local governments."),
            ("point", "Government undertakings are promises", "Land, payments and guarantees, each a future "
             "claim on local money."),
            ("point", "The treasury tracks both sides", "What is promised and what is received."),
            ("h", "Your Part 33 Action Plan"),
            ("point", "If you work in a treasury", "Start a register of promises for every PPP or similar "
             "contract your local government has."),
            ("point", "If you sit in the sanggunian", "Before approving a PPP, ask for the worst-case cost of "
             "every guarantee, in pesos per year."),
            ("point", "If you are a resident", "Ask whether your local government has any PPP projects and how "
             "their fees are shared."),
            ("cta", "Read: Inside the Local Treasury, Part 29: When Local Governments Borrow, Loans, Bonds and the 20 Percent Limit", "/blog/when-local-governments-borrow/"),
            ("cta", "Read: Inside the Local Treasury, Part 19: The Public Market, a Business the Town Runs", "/blog/public-market-economic-enterprise/"),
            ("cta", "Read: Inside the Local Treasury, Part 31: Estimating Next Year’s Income, the Numbers Behind the Budget", "/blog/estimating-next-years-income/"),
            ("cta", "Read: Business Intelligence Series, Part 37: The Pareto Chart, Finding the Few Causes Behind Most of a Problem", "/blog/business-intelligence-part-37-pareto-chart/"),
            ("ask", "Does your local government have a facility built or run by a private partner?"),
        ],
    },
    {
        "title": "Inside the Local Treasury, Part 32: The Disaster Fund, Five Percent Set Aside Before the Storm",
        "slug": "local-disaster-risk-reduction-fund",
        "category": "finance",
        "date": "May 24, 2027",
        "summary": "Every local government must set aside at least 5 percent of its estimated regular revenue for "
                   "disaster risk reduction and management. Thirty percent of that is a quick response fund, and "
                   "what is not spent moves to a special trust fund for five years. This part explains the rules "
                   "in Section 21 of Republic Act No. 10121 and the treasury’s part in keeping the money ready.",
        "publish_on": "2027-05-24 21:00",
        "body": [
            "The typhoon passed on a Tuesday night. By Wednesday morning, the evacuation center held 312 "
            "families, and the disaster office needed rice, water and sleeping mats before noon.",
            "The treasurer did not have to search for the money. It had been set aside in January, in a fund "
            "the law requires every local government to keep, for exactly this kind of morning.",
            "(The local government, the storm and the amounts are invented for this post. The rules quoted below "
            "come from Republic Act No. 10121, the Philippine Disaster Risk Reduction and Management Act of "
            "2010.)",
            "Part 31 showed how next year’s income is estimated. This part looks at one slice of the budget that "
            "is fixed by law as a share of that estimate. By the end, you will know how big the disaster fund "
            "must be, what it may pay for, what the quick response fund is, what happens to money left at "
            "year-end, and where the treasury fits in.",
            ("photo", "blog/finance-ldrrmf.jpg", "The disaster fund: at least 5 percent of estimated regular "
             "revenue, with 30 percent kept as a quick response fund and the unspent balance carried in a "
             "special trust fund. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "From Calamity Fund to Disaster Fund"),
            "Section 21 of Republic Act No. 10121 begins by renaming an older fund: “The present Local Calamity "
            "Fund shall henceforth be known as the Local Disaster Risk Reduction and Management Fund.” The "
            "law itself shortens it to LDRRMF.",
            "The new name matches what the law lets the money pay for: not only the day after a calamity, but "
            "also the months before one.",
            ("h", "How Much: At Least Five Percent"),
            "The law sets a floor: “Not less than five percent (5%) of the estimated revenue from regular "
            "sources shall be set aside as the LDRRMF.”",
            ("point", "Estimated revenue from regular sources", "₱150,000,000 in this example, taken from the "
             "budget’s income estimate described in Part 31."),
            ("point", "LDRRMF, at least 5 percent", "₱7,500,000."),
            ("point", "Quick response fund, 30 percent of that", "₱2,250,000."),
            ("point", "The rest, 70 percent", "₱5,250,000 for other disaster risk reduction activities."),
            "Five percent is the minimum. A local government that faces frequent storms or floods may set aside "
            "more.",
            ("h", "What the Fund May Pay For"),
            "Section 21 says the fund supports disaster risk management activities, “such as, but not limited "
            "to,” the following:",
            ("point", "Preparedness", "Pre-disaster preparedness programs, including training."),
            ("point", "Equipment and supplies", "Purchasing life-saving rescue equipment, supplies and "
             "medicines."),
            ("point", "After the event", "Post-disaster activities."),
            ("point", "Insurance", "Payment of premiums on calamity insurance."),
            "The law adds that the local disaster risk reduction and management council monitors and evaluates "
            "the use and disbursement of the fund, based on the local disaster risk reduction and management "
            "plan.",
            ("h", "The Quick Response Fund"),
            "The law states: “Of the amount appropriated for LDRRMF, thirty percent (30%) shall be allocated as "
            "Quick Response Fund (QRF).” It describes the QRF as a stand-by fund for relief and recovery "
            "programs, so that living conditions in stricken areas can be normalized as quickly as possible.",
            "That is the money the treasurer released on Wednesday morning. Because it was already appropriated "
            "and set aside, the disbursement followed the normal steps in Part 7, from obligation to check, "
            "without waiting for a new budget.",
            ("photo", "blog/finance-ldrrmf-flow.jpg", "How the fund moves in a year: set aside in the budget, "
             "spent on preparedness and response, and any balance carried to a special trust fund for up to five "
             "years. Figures are invented. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Money Left at Year-End"),
            "Disasters do not follow the calendar, so the law does not let unused money simply disappear into "
            "the general fund at year-end.",
            ("point", "First, a special trust fund", "Section 21 says unexpended LDRRMF “shall accrue to a "
             "special trust fund solely for the purpose of supporting” disaster risk reduction and management "
             "activities of the local council."),
            ("point", "Then, five years", "Money not used within five years after it went into the trust fund "
             "reverts to the general fund, where the sanggunian may use it for other social services."),
            "So a balance left at the end of this year can still buy rescue boats three years from now, but not "
            "seven.",
            ("h", "Where the Treasury Fits"),
            ("point", "Keep the balances apart", "Part 16 explained why the Special Education Fund is tracked "
             "separately. The disaster fund and its trust fund need the same care, so that every peso can be "
             "traced to its purpose."),
            ("point", "Track the year each balance came from", "The five-year limit runs from when the money "
             "went into the trust fund. A simple table by year shows which balances are closest to the limit."),
            ("point", "Keep cash ready", "The quick response fund is only useful if the cash is there when "
             "the disbursement voucher arrives. Part 13 covered deposits and bank accounts."),
            ("point", "Support the reports", "Part 10 listed the reports a local government must post, including "
             "the use of its disaster risk reduction and management fund."),
            ("h", "A Simple Monthly Report"),
            "The disaster office plans the spending. The treasury can make the balances easy to see with one "
            "short table each month.",
            ("point", "This year’s fund", "Appropriated, obligated, paid and remaining, shown separately for "
             "the quick response fund and the rest."),
            ("point", "The trust fund", "Each balance by the year it arrived, with the year it reaches the "
             "five-year limit."),
            ("point", "Cash on hand", "The bank balance available for the fund, so nobody assumes money that "
             "is not there."),
            "Shared with the disaster office and the local chief executive, the table answers the first "
            "question asked on any storm morning: how much can we spend today?",
            ("h", "Back to Wednesday Morning"),
            "By noon, the relief goods were at the evacuation center. Over the next month, the QRF paid for food, "
            "water, mats and repairs to the center’s roof, a total of ₱1,940,000.",
            "At year-end, ₱1,300,000 of the year’s fund remained, mostly from a training program that had been "
            "postponed. It moved to the special trust fund. The treasury recorded it under the year it arrived, "
            "and the next year’s disaster plan used part of it for two rescue boats and life vests.",
            ("h", "What Residents Can Check"),
            ("point", "The posted report", "Look for the use of the disaster fund among the reports your local "
             "government posts."),
            ("point", "The 5 percent", "Compare the fund with the estimated regular revenue in the budget."),
            ("point", "Preparedness, not only relief", "Ask how much went to training, equipment and warning "
             "systems before the season, not only to relief after it."),
            ("h", "Mistakes to Avoid"),
            ("point", "Treating 5 percent as a ceiling", "It is a floor."),
            ("point", "Spending only after disasters", "The law covers preparedness too."),
            ("point", "Mixing the balances", "Keep the fund and its trust fund separate from the general fund."),
            ("point", "Losing track of the five years", "Record each balance by the year it arrived."),
            ("h", "Key Takeaways"),
            ("point", "At least 5 percent", "Of estimated revenue from regular sources."),
            ("point", "30 percent is the QRF", "A stand-by fund for relief and recovery."),
            ("point", "Unspent money stays for disasters", "In a special trust fund for up to five years."),
            ("point", "The council monitors its use", "Based on the local disaster plan."),
            ("h", "Your Part 32 Action Plan"),
            ("point", "If you work in a treasury", "Build a table of trust fund balances by year of accrual and "
             "mark any that are four years old."),
            ("point", "If you sit in the sanggunian", "Ask how this year’s fund is split between preparedness "
             "and response."),
            ("point", "If you are a resident", "Find your local government’s posted report on the disaster fund "
             "and ask what it bought before the last storm season."),
            ("cta", "Read: Inside the Local Treasury, Part 31: Estimating Next Year’s Income, the Numbers Behind the Budget", "/blog/estimating-next-years-income/"),
            ("cta", "Read: Inside the Local Treasury, Part 16: The Special Education Fund, the School Money in Your Amilyar", "/blog/special-education-fund/"),
            ("cta", "Read: Inside the Local Treasury, Part 7: From Budget to Check, How a Town Pays Its Bills", "/blog/from-budget-to-check/"),
            ("cta", "Read: Inside the Local Treasury, Part 10: Where to See How Your Town Spends", "/blog/where-to-see-how-your-town-spends/"),
            ("ask", "Do you know what your local government’s disaster fund bought before the last storm?"),
        ],
    },
    {
        "title": "Inside the Local Treasury, Part 31: Estimating Next Year’s Income, the Numbers Behind the Budget",
        "slug": "estimating-next-years-income",
        "category": "finance",
        "date": "May 19, 2027",
        "summary": "Every local budget starts with a guess about how much money will come in. The treasury "
                   "supplies the actual collections and helps estimate the rest, and four officials certify "
                   "that the estimate is reasonably collectible. This part explains the form, the method and why "
                   "an estimate that is too hopeful causes trouble all year.",
        "publish_on": "2027-05-19 21:00",
        "body": [
            "In July, the budget officer sent the treasury a one-line request: “Please give us next year’s "
            "estimated receipts.” Three people had three different ideas. The planning coordinator wanted a "
            "higher figure to fit more projects. The accountant wanted last year’s actual. The treasurer wanted "
            "to look at what had changed first.",
            "All three had a point. Only one approach would hold up when the money had to be spent.",
            "(The local government, the people and the amounts are invented for this post. The budget form and "
            "its wording come from the cited memorandum of the Department of Budget and Management.)",
            "Part 30 covered collecting business taxes that are already overdue. This part looks forward, to "
            "the income a local government expects next year. By the end, you will know which form carries the "
            "estimate, what each column means, who certifies it, a simple method for building a realistic "
            "estimate, and what happens when the estimate is too high.",
            ("photo", "blog/finance-estimate.jpg", "Estimating next year’s income: start from what was actually "
             "collected, adjust for what has really changed, and certify only what can reasonably be "
             "collected. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "The Form That Carries the Estimate"),
            "The Department of Budget and Management issues a Local Budget Memorandum each year to guide local "
            "budget preparation. Local Budget Memorandum No. 90, dated June 13, 2024, includes the Budget of "
            "Expenditures and Sources of Financing, LBP Form No. 1, for the General Fund. Its columns:",
            ("point", "Past Year (Actual)", "What was actually received last year."),
            ("point", "Current Year, First Semester (Actual)", "What has been received from January to June."),
            ("point", "Current Year, Second Semester (Estimate)", "What is expected from July to December."),
            ("point", "Current Year, Total", "The two semesters added together."),
            ("point", "Budget Year (Proposed)", "The estimate for next year."),
            "Two of those columns are facts, not guesses. The memorandum notes that past-year and first-semester "
            "receipts are jointly certified by the local treasurer and the local accountant.",
            ("h", "Who Certifies the Estimate"),
            "The form is signed by the local budget officer, the local treasurer, the local planning and "
            "development coordinator and the local accountant, and approved by the local chief executive. Their "
            "certification includes this sentence:",
            ("quote", "“We further certify that the foregoing estimated receipts are reasonably projected as "
             "collectible for the Budget Year.”"),
            "Reasonably projected as collectible. Not hoped for, not needed to balance the projects. The "
            "treasurer’s signature puts the treasury’s judgment behind that phrase.",
            ("h", "A Simple Method for Local Sources"),
            "Take one source at a time, such as the business tax.",
            ("point", "Step 1: Start from actuals", "Past year: ₱18,000,000. First semester this year: "
             "₱12,600,000."),
            ("point", "Step 2: Estimate the rest of this year", "Use the office’s own records of past "
             "years to see what share of the year’s business tax the second semester has brought in, and "
             "apply it. Here: ₱6,200,000, for a current-year total of ₱18,800,000."),
            ("point", "Step 3: Adjust only for real changes", "A new market wing with 40 stalls opening in "
             "January, a revised tax ordinance already approved, a large business that has closed. Each "
             "change is written down with its amount."),
            ("point", "Step 4: Write the reasons", "One line per adjustment, kept with the working papers, so "
             "next year’s team knows why."),
            ("point", "Step 5: Check against history", "Compare the proposed figure with the growth the "
             "source has actually shown. A sudden jump with no written reason is a warning."),
            ("photo", "blog/finance-estimate-steps.jpg", "Building one line of the estimate: last year’s actual, "
             "this year’s first half, an estimate of the second half, then only documented changes. Figures "
             "are invented. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Back to the Business Tax"),
            "The treasurer’s working paper for the business tax had three lines.",
            ("point", "Current-year total", "₱18,800,000."),
            ("point", "Business closed in March", "Minus ₱300,000 a year, from its last assessment."),
            ("point", "Revised schedule approved for next year", "Plus ₱900,000, computed business by business "
             "from this year’s declared gross sales."),
            "Proposed for the budget year: ₱19,400,000. The planning coordinator had hoped for ₱22,000,000. "
            "The difference had no reason written beside it, so it stayed out.",
            ("h", "Fees and Charges: Count Times Rate"),
            "Fees behave differently from taxes. Their total depends on how many transactions the office "
            "handles and on the rate set in the local revenue code.",
            ("point", "Count the transactions", "Use the receipts issued last year for each fee, such as "
             "permits or certifications, and the count so far this year."),
            ("point", "Apply the rate in force", "Use the rate in the ordinance that will apply next year, "
             "not a rate still under discussion."),
            ("point", "Note any change in volume", "A new office opening, a service moved online or a "
             "program ending can raise or lower the count. Write the reason, as with taxes."),
            "For example, 2,400 certifications last year at ₱100 each gave ₱240,000. If the count so far "
            "this year points to about 2,500, the proposed figure is ₱250,000, with the reason written "
            "beside it.",
            ("h", "What the Sanggunian May Ask"),
            "When the budget reaches the local legislative body, members may ask why a source is projected to "
            "rise. A treasury that kept the working papers can answer in minutes: the actuals, each "
            "adjustment and its reason. That record also helps next year’s team start faster.",
            ("h", "Why Too High Is Worse Than Too Low"),
            ("point", "Spending runs ahead of cash", "Part 7 explained Section 337, which limits disbursements "
             "from a fund to actual collections plus half of the estimated revenue not yet collected. An "
             "inflated estimate makes that limit look roomier than the cash really is."),
            ("point", "Projects stall midyear", "Contracts are signed against money that never arrives."),
            ("point", "Trust is lost", "Next year, every figure the treasury signs is doubted."),
            "An estimate that turns out slightly low leaves room for a supplemental budget later, funded by "
            "income actually received.",
            ("h", "Shares From Outside"),
            "Not every source is estimated by the treasury. A local government’s share of national taxes, "
            "covered in Part 1, is based on the figures the national government announces. The treasury’s job "
            "there is to use the announced amount, not to round it up.",
            ("h", "Measuring Accuracy"),
            "At year-end, compare each source’s estimate with its actual collection.",
            ("point", "Within a few percent", "The method is working."),
            ("point", "Far above actual", "Find the adjustment that did not happen, and remember it."),
            ("point", "Far below actual", "Find the change that was missed."),
            "Part 10 listed the reports a local government must post, including its quarterly statement of receipts and expenditures. "
            "Residents can make the same comparison.",
            ("h", "Mistakes to Avoid"),
            ("point", "Estimating to fit the projects", "The projects should fit the estimate."),
            ("point", "Skipping the actuals", "Past year and first semester come first."),
            ("point", "Adjustments with no written reason", "If it cannot be explained, leave it out."),
            ("point", "Never checking last year’s estimate", "Accuracy improves only when it is measured."),
            ("h", "Key Takeaways"),
            ("point", "One form, five columns", "Past actual, first semester, second-semester estimate, total "
             "and budget year."),
            ("point", "Four signatures", "Budget officer, treasurer, planning coordinator and accountant."),
            ("point", "Reasonably collectible", "The standard the certification promises."),
            ("point", "Actuals plus documented changes", "A method anyone can check."),
            ("h", "Your Part 31 Action Plan"),
            ("point", "If you work in a treasury", "For your three largest local sources, write last year’s "
             "estimate beside last year’s actual and note the difference."),
            ("point", "If you sit in the sanggunian", "Ask for the written reasons behind any source projected "
             "to grow faster than it has in past years."),
            ("point", "If you are a resident", "Find your local government’s posted statement of receipts and expenditures and "
             "compare two years."),
            "The budget passed with the treasury’s figure. In December, the business tax came in at "
            "₱19,550,000, slightly above the estimate. The planning coordinator’s extra project went into a "
            "supplemental budget, paid for with money already in the bank.",
            ("cta", "Read: Inside the Local Treasury, Part 7: From Budget to Check, How a Town Pays Its Bills", "/blog/from-budget-to-check/"),
            ("cta", "Read: Inside the Local Treasury, Part 1: Where Your Town's Money Comes From", "/blog/where-your-towns-money-comes-from/"),
            ("cta", "Read: Inside the Local Treasury, Part 10: Where to See How Your Town Spends", "/blog/where-to-see-how-your-town-spends/"),
            ("cta", "Read: Inside the Local Treasury, Part 29: When Local Governments Borrow, Loans, Bonds and the 20 Percent Limit", "/blog/when-local-governments-borrow/"),
            ("ask", "Have you ever compared your local government’s estimated income with what it actually collected?"),
        ],
    },
    {
        "title": "Inside the Local Treasury, Part 30: Unpaid Business Taxes, Distraint, Levy and What Cannot Be Seized",
        "slug": "unpaid-business-taxes-distraint-and-levy",
        "category": "finance",
        "date": "May 14, 2027",
        "summary": "When business taxes stay unpaid, the Local Government Code lets the treasurer seize and sell "
                   "personal property, levy on real property, or go to court. This part explains the steps and "
                   "deadlines in Sections 173 to 185, the property that cannot be taken, and how a business "
                   "owner can stop the process by paying.",
        "publish_on": "2027-05-14 21:00",
        "body": [
            "The hardware store had not paid its business tax for two years. The first notice was ignored. So "
            "was the second. When the third letter arrived, it came with a draft warrant attached and a short "
            "line from the treasurer: “Please see me before Friday.”",
            "The owner came on Thursday, angry. “You cannot take my store.” The treasurer opened the Local "
            "Government Code and showed him exactly what the law allowed, what it did not, and how he could "
            "stop all of it.",
            "(The store, the owner and the amounts are invented for this post. The sections of the Local "
            "Government Code described below are real.)",
            "Part 5 followed unpaid real property tax from notice to auction. This part covers the other big "
            "source of local revenue, business taxes, which follow a separate set of rules in Sections 173 to "
            "185. By the end, you will know the remedies the law gives, the steps and deadlines for seizing "
            "personal property and levying on real property, what cannot be seized, and what a business owner "
            "can do at any point.",
            ("photo", "blog/finance-distraint.jpg", "Collecting unpaid business taxes: a lien on the property, "
             "distraint of personal property, levy on real property, or a court case. (Illustration: Butch "
             "Mahinay, aumahinay.dev)", "medium"),
            ("h", "The Lien Comes First"),
            "Section 173 makes local taxes, fees and charges a lien on the property subject to them. The lien "
            "is “superior to all liens, charges or encumbrances in favor of any person.” It ends only when the "
            "tax, with surcharges and interest, is fully paid.",
            ("h", "Three Remedies"),
            "Section 174 lists the civil remedies for collecting local taxes.",
            ("point", "Distraint of personal property", "Seizing movable property, such as goods or equipment, "
             "and selling it."),
            ("point", "Levy on real property", "Placing a hold on land or buildings, and selling them if the tax "
             "is not paid."),
            ("point", "Judicial action", "Filing a case in court."),
            "The section allows these remedies to be pursued at the same time or one after another, as the "
            "local government chooses.",
            ("h", "Distraint, Step by Step"),
            "Section 175 sets out the process.",
            ("point", "Seizure", "On failure to pay on time, the treasurer may seize enough personal property "
             "to cover the tax, upon written notice."),
            ("point", "Accounting", "The officer leaves a signed list of the goods seized with the owner, or "
             "at the home or place of business with someone of suitable age."),
            ("point", "Posting", "Notice of the sale is posted in at least three public and conspicuous places, "
             "one of them at the office of the local chief executive. The sale may not be held until at least "
             "20 days after notice to the owner and the posting."),
            ("point", "Release", "If the owner pays the full amount and charges before the sale, the goods are "
             "returned."),
            ("point", "Sale", "Otherwise the goods are sold at public auction. The treasurer reports the sale "
             "to the local chief executive in writing within five days."),
            ("h", "Levy on Real Property"),
            "Section 176 allows a levy before, together with or after distraint.",
            ("point", "Notice of levy", "A written notice goes to the assessor and to the Registrar of Deeds, who "
             "annotate the records of the property."),
            ("point", "When distraint is not enough", "If the personal property seized is not enough, the "
             "treasurer proceeds with a levy on real property within 30 days after the distraint."),
            ("point", "Advertisement", "Under Section 178, the treasurer advertises the sale within 30 days "
             "after the levy, for at least 30 days, by posting at the main entrance of the municipal or city "
             "building and in the barangay, and by publication once a week for three weeks."),
            ("point", "Redemption", "Section 179 gives the owner one year from the sale to redeem the property "
             "by paying the taxes, charges and interest of not more than 2 percent a month on the purchase "
             "price."),
            ("point", "No bidder", "Under Section 181, if nobody bids enough, the treasurer purchases the "
             "property for the local government, and the owner still has one year to redeem it."),
            ("photo", "blog/finance-distraint-steps.jpg", "The timeline for distraint and levy, with the day "
             "counts set by the Local Government Code. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "What Cannot Be Seized"),
            "Section 185 protects certain property from distraint or levy. Among the items it lists:",
            ("point", "Tools of the trade", "Tools and implements necessarily used by the taxpayer in his trade "
             "or employment."),
            ("point", "A work animal", "One draft animal necessarily used in the taxpayer’s occupation."),
            ("point", "Family needs", "Necessary clothing, and household furniture and utensils up to ₱10,000 "
             "in value."),
            ("point", "Food", "Provisions, including crops, for individual or family use, enough for four "
             "months."),
            ("point", "Professional libraries", "Of doctors, engineers, lawyers and judges."),
            ("point", "A fishing boat", "One fishing boat and net, up to ₱10,000 in value, used by a fisherman "
             "for his livelihood."),
            ("point", "Parts of a house", "Materials forming part of a house or improvement on real property."),
            "The list keeps collection from taking away a family’s means of living. When in doubt about an item, "
            "the treasurer should leave it and check.",
            ("h", "Distraint or Levy: Which Comes First?"),
            "The Code leaves the order to the local government, but each remedy fits a different case.",
            ("point", "Distraint suits a running business", "Goods on the shelves or equipment that is not a "
             "protected tool can cover a modest debt quickly, and the owner can get them back by paying "
             "before the sale."),
            ("point", "Levy suits a larger debt", "When the amount is large, or the business has closed and "
             "left little stock, a levy on land or a building secures the debt through the Registrar of "
             "Deeds."),
            ("point", "Court suits a disputed amount", "When the taxpayer disputes the amount and the "
             "documents are strong, a case may settle the matter. Section 183 allows the local government to "
             "sue in any court of competent jurisdiction."),
            "Section 184 adds that distraint or levy may be repeated until the full amount, including "
            "expenses, is collected.",
            ("h", "The Treasurer Must Act"),
            "The Code does not treat these powers as optional. Section 177 says a treasurer who fails to issue "
            "or execute a warrant on time, or who abuses the power, shall be dismissed after due notice and "
            "hearing, without prejudice to criminal prosecution.",
            ("quote", "The law asks the treasurer to collect firmly, and to stay inside the lines it draws."),
            ("h", "What the Owner Can Do"),
            ("point", "Pay before the sale", "Payment of the tax and charges stops a distraint or a sale of real "
             "property."),
            ("point", "Ask for the computation", "In writing, showing the tax, surcharge and interest. Part 2 "
             "covered how business taxes are assessed each January."),
            ("point", "Question the assessment properly", "Part 18 explained the protest and refund rules. A "
             "protest has its own deadlines."),
            ("point", "Close the business properly", "If the store has stopped operating, Part 14 explained how "
             "retirement is done, so taxes do not keep running."),
            ("h", "Back to the Hardware Store"),
            "The owner owed ₱86,400 including surcharges and interest. After seeing the computation, he "
            "came back the next Monday with the full amount, before the date set for the warrant. No goods were seized. The draft warrant went back into the folder, unsigned.",
            ("h", "Mistakes to Avoid"),
            ("point", "For offices: skipping the written notice", "Seizure follows written notice."),
            ("point", "For offices: seizing exempt items", "Check Section 185 first."),
            ("point", "For owners: ignoring the letters", "Every notice is a chance to pay before property is "
             "taken."),
            ("point", "For owners: waiting for the auction", "Paying earlier costs less."),
            ("h", "Key Takeaways"),
            ("point", "A superior lien", "Local taxes come before other claims on the property."),
            ("point", "Three remedies", "Distraint, levy and court, together or in turn."),
            ("point", "Fixed steps and deadlines", "Notice, posting, at least 20 days, then sale."),
            ("point", "Some property is protected", "Tools, food, clothing and other items in Section 185."),
            ("h", "Your Part 30 Action Plan"),
            ("point", "If you work in a treasury", "List delinquent business accounts by age, as Part 34 of the "
             "Business Intelligence Series did, and send written notices to the oldest first."),
            ("point", "If you own a business", "Check that your business tax for this year and last is paid, "
             "and keep the official receipts."),
            ("point", "If you sit in the sanggunian", "Ask the treasurer for a yearly report on distraint and "
             "levy actions and their results."),
            ("cta", "Read: Inside the Local Treasury, Part 5: Unpaid Amilyar, From Notice to Auction", "/blog/unpaid-amilyar-notice-to-auction/"),
            ("cta", "Read: Inside the Local Treasury, Part 2: The January Rush and Your Business Permit", "/blog/january-rush-business-permit/"),
            ("cta", "Read: Inside the Local Treasury, Part 14: Closing a Business the Right Way", "/blog/closing-a-business-the-right-way/"),
            ("cta", "Read: Inside the Local Treasury, Part 18: Paid Too Much? Refunds, Tax Credits and Protests", "/blog/local-tax-refunds-and-credits/"),
            ("ask", "Did you know which property the law protects from seizure for unpaid taxes?"),
        ],
    },
    {
        "title": "Inside the Local Treasury, Part 29: When Local Governments Borrow, Loans, Bonds and the 20 Percent Limit",
        "slug": "when-local-governments-borrow",
        "category": "finance",
        "date": "May 9, 2027",
        "summary": "Local governments may borrow to build roads, markets and water systems, but the law sets a "
                   "ceiling on how much of their income can go to paying debts. This part explains where a local government "
                   "can borrow, the 20 percent limit, the certificate and opinion a loan needs, and how to check "
                   "whether a loan fits.",
        "publish_on": "2027-05-09 21:00",
        "body": [
            "The new public market would cost ₱100 million. The municipality had ₱12 million saved for it. At the "
            "budget hearing, a councilor asked the question everyone was thinking: “Can we borrow the rest, "
            "and if we do, can we still pay salaries ten years from now?”",
            "The treasurer had a one-page answer ready. It started with a number: 20 percent.",
            "(The municipality, the market and every peso amount in this post are made up to show how the rules work. "
            "The laws, offices and requirements named below are real.)",
            "Part 19 showed how a local government runs its public market as a business. This part goes one step back, to "
            "how it may pay for building one. By the end of it, you will know where a local government may "
            "borrow, what the 20 percent debt service limit means, which papers a loan needs before the money "
            "is released, and how to test a loan against the limit with simple arithmetic.",
            ("photo", "blog/finance-borrow.jpg", "Borrowing for a project: the loan funds the building, and "
             "the yearly payments come back out of regular income for years. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "Why a Local Government Borrows at All"),
            "Some projects cost more than a local government collects in a year. A market, a slaughterhouse, a water system "
            "or a long farm-to-market road can take several years of savings. Borrowing lets it build now "
            "and pay over the years the project is in use.",
            "The Department of Finance (DOF) explains that Section 296 of the Local Government Code allows local "
            "government units to create indebtedness and avail of credit facilities to finance local "
            "infrastructure and other socio-economic development projects.",
            ("quote", "Borrowing does not create new money. It moves future income to the present, and the "
             "future has to pay it back."),
            ("h", "Where a Local Government May Borrow"),
            "The DOF page on LGU loans lists the main routes.",
            ("point", "Banks and lending institutions", "Local governments may obtain credit lines from "
             "government and private banks and lending institutions."),
            ("point", "Bonds", "A local government may raise money by selling bonds to investors."),
            ("point", "Help from the DOF", "The DOF says it is mandated to give LGUs technical assistance "
             "in availing of credit facilities and in the flotation of bonds."),
            "Whichever route is taken, the payments become a yearly obligation that the sanggunian must "
            "appropriate in the budget, the same budget process Part 7 walked through.",
            ("h", "The 20 Percent Limit"),
            "The DOF summarizes the key ceiling this way: under Section 324 of the Local Government Code, the "
            "appropriation for debt servicing shall not exceed 20 percent of the local government’s annual "
            "regular income.",
            ("point", "Debt service", "The yearly payments on all of the local government’s loans, principal and interest "
             "together."),
            ("point", "Regular income", "The base the law names is annual regular income, not every peso "
             "received. The BLGF certificate described below states what the ceiling works out to."),
            ("point", "What the limit protects", "Salaries, services and maintenance. If loan payments could "
             "take any share of income, a local government could borrow until it had nothing left to run on."),
            ("h", "The Papers a Loan Needs"),
            "Before a loan is released, two outside offices look at it.",
            ("point", "BLGF certificate", "The Bureau of Local Government Finance issues a Certificate of Net "
             "Debt Service Ceiling and Borrowing Capacity. It states how much room the local government has under the "
             "limit."),
            ("point", "Monetary Board opinion", "The DOF page says a favorable opinion of the Monetary Board of "
             "the Bangko Sentral ng Pilipinas is needed before the loan proceeds are released."),
            "The DOF also notes that Department Order No. 054-2016 cut the documents needed for the BLGF "
            "certificate from twelve to four.",
            ("photo", "blog/finance-borrow-limit.jpg", "Testing a loan against the 20 percent limit: income, "
             "the ceiling, existing payments, and the room left for a new loan. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "Testing the Market Loan"),
            "Here is the one-page answer the treasurer brought to the hearing, step by step.",
            ("point", "Step 1: Regular income", "₱120,000,000 a year."),
            ("point", "Step 2: The ceiling", "20 percent of ₱120,000,000 = ₱24,000,000 a year for all debt "
             "service."),
            ("point", "Step 3: Existing payments", "An older road loan already takes ₱9,000,000 a year."),
            ("point", "Step 4: Room left", "₱24,000,000 − ₱9,000,000 = ₱15,000,000 a year."),
            ("point", "Step 5: The new payment", "A ₱100,000,000 loan over 10 years at 6 percent a year, paid "
             "in equal yearly amounts, costs about ₱13,586,796 a year."),
            ("point", "Step 6: Does it fit?", "Yes. ₱13,586,796 is below the ₱15,000,000 room, with about "
             "₱1,413,204 to spare."),
            "In a spreadsheet, Step 5 is one formula: =PMT(6%, 10, -100000000). It returns the equal yearly "
            "payment for that rate, term and amount.",
            "The councilor’s second question was harder. Over ten years, the municipality would pay about ₱135.9 million "
            "in total, so roughly ₱35.9 million would be interest. The treasurer put that line on the same page, "
            "because a loan that fits under the ceiling can still be a poor deal if the project does not earn "
            "or save enough to justify it.",
            ("h", "What the Numbers Do Not Show"),
            ("point", "Income can fall", "If regular income drops in a bad year, the same payment takes a bigger "
             "share. A thin margin under the ceiling leaves little room for that."),
            ("point", "Other projects wait", "Room used by this loan is room no other loan can use until it is "
             "paid down."),
            ("point", "The project must work", "A market that stands half empty still has to be paid for. Part "
             "19 covered how market income and costs should be tracked."),
            ("h", "How Residents Can Follow Local Government Debt"),
            "Debt is not hidden from the public. Part 10 listed the documents a local government must post under "
            "full disclosure, and the statement of debt service is one of them, posted every quarter.",
            ("point", "Read the statement", "Look for the lender, the amount, and how much is paid each "
             "quarter."),
            ("point", "Compare it with income", "Divide the yearly debt service by the local government’s regular income to "
             "see how close it is to 20 percent."),
            ("point", "Ask at the hearing", "Budget hearings are the place to ask what a loan is for and how it "
             "will be repaid."),
            ("h", "What Each Office Does"),
            ("point", "Treasurer", "Prepares the computation of debt service and room left, and pays the "
             "installments on time."),
            ("point", "Budget officer", "Makes sure each year’s debt service is in the budget."),
            ("point", "Accountant", "Records the loan and every payment, so the balance owed is always known."),
            ("point", "Sanggunian", "Decides whether to borrow, and appropriates the payments every year."),
            ("h", "Mistakes to Avoid"),
            ("point", "Guessing the ceiling", "Use the figure on the BLGF certificate, not an estimate."),
            ("point", "Forgetting existing loans", "The 20 percent covers all debt service, old and new."),
            ("point", "Looking only at the yearly payment", "Show the total interest too."),
            ("point", "Borrowing with no room for a bad year", "Leave a margin below the ceiling."),
            ("h", "Key Takeaways"),
            ("point", "Local governments may borrow", "Section 296 allows credit for infrastructure and development "
             "projects."),
            ("point", "Twenty percent is the ceiling", "Debt service may not exceed 20 percent of annual regular "
             "income (Section 324)."),
            ("point", "Two clearances", "A BLGF certificate and a favorable Monetary Board opinion come before "
             "release."),
            ("point", "Debt is public", "The statement of debt service is posted every quarter."),
            ("h", "Your Part 29 Exercise"),
            "Try the test yourself. A municipality has regular income of ₱80,000,000 and existing debt service of "
            "₱11,000,000 a year. It wants a ₱50,000,000 loan over 10 years at 6 percent.",
            ("point", "Question 1", "What is the ceiling? (Answer: ₱16,000,000.)"),
            ("point", "Question 2", "How much room is left? (Answer: ₱5,000,000.)"),
            ("point", "Question 3", "Does the loan fit? (Answer: No. =PMT(6%, 10, -50000000) gives about "
             "₱6,793,398 a year, which is more than the ₱5,000,000 room.)"),
            "If your municipality, city or province posts its statement of debt service, try the same test with its real numbers.",
            ("cta", "Read: Inside the Local Treasury, Part 7: From Budget to Check, How a Town Pays Its Bills", "/blog/from-budget-to-check/"),
            ("cta", "Read: Inside the Local Treasury, Part 10: Where to See How Your Town Spends", "/blog/where-to-see-how-your-town-spends/"),
            ("cta", "Read: Inside the Local Treasury, Part 19: The Public Market, a Business the Town Runs", "/blog/public-market-economic-enterprise/"),
            ("cta", "Read: Inside the Local Treasury, Part 1: Where Your Town's Money Comes From", "/blog/where-your-towns-money-comes-from/"),
            ("ask", "Would you support your local government borrowing for a project, and which one?"),
        ],
    },
    {
        "title": "Inside the Local Treasury, Part 28: What Local Governments Cannot Tax, the Limits in Section 133",
        "slug": "what-local-governments-cannot-tax",
        "category": "finance",
        "date": "May 4, 2027",
        "summary": "The Local Government Code gives provinces, cities, municipalities and barangays the power to tax, but Section "
                   "133 lists what none of them may tax. This part walks through the fifteen limits in plain "
                   "words, with examples from the counter, and explains why a revenue code should be checked "
                   "against them.",
        "publish_on": "2027-05-04 21:00",
        "body": [
            "The farmer had two sacks of copra on the back of his tricycle. At the edge of the next municipality, a "
            "man with a logbook stopped him and asked for ₱20 a sack before he could pass to the buyer’s "
            "warehouse. The farmer paid, kept the slip, and brought it to the municipal treasury the following "
            "week. “Is this allowed?”",
            "The clerk read the slip, then reached for the Local Government Code. The answer was in Section "
            "133.",
            "(The farmer, the checkpoint and the amounts are invented for this post. The sections of the Local "
            "Government Code quoted below are real.)",
            "Part 27 covered a fee a municipality may charge at the market. This part covers the other side: what "
            "provinces, cities, municipalities and barangays may not tax at all. Stay with me to the end, and you will "
            "know what Section 133 says, the fifteen limits in plain words, which ones come up at a municipal "
            "counter, and what to do when a charge seems to cross the line.",
            ("photo", "blog/finance-limits.jpg", "Section 133 of the Local Government Code: fifteen things no "
             "province, city, municipality or barangay may tax, unless the Code itself says otherwise. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "What Section 133 Says"),
            "Section 133 is titled “Common Limitations on the Taxing Powers of Local Government Units.” It "
            "opens with the words “Unless otherwise provided herein,” and then lists what the taxing powers of "
            "provinces, cities, municipalities and barangays shall not extend to.",
            ("point", "Common", "The limits apply to every level of local government, not only to municipalities."),
            ("point", "Unless otherwise provided", "Some limits have exceptions written elsewhere in the Code. "
             "Those exceptions are the only way around them."),
            ("point", "Taxes, fees and charges", "Several items cover fees and charges too, so renaming a tax "
             "as a fee does not escape them. Part 15 explained the difference between the two."),
            ("h", "The Fifteen Limits, in Plain Words"),
            ("point", "(a) Income tax", "Except on banks and other financial institutions."),
            ("point", "(b) Documentary stamp tax", "A national tax."),
            ("point", "(c) Estate, inheritance and gift taxes", "Including transfers made in anticipation of "
             "death, except as the Code provides."),
            ("point", "(d) Customs duties and port charges", "Including wharfage, except on wharves the local "
             "government built and maintains."),
            ("point", "(e) Goods passing through", "Taxes, fees or charges on goods carried into, out of, or "
             "through the territory, whether called wharfage, bridge tolls “or otherwise.”"),
            ("point", "(f) Products of marginal farmers and fishers", "Taxes, fees or charges on agricultural "
             "and aquatic products when sold by marginal farmers or fishermen."),
            ("point", "(g) BOI-registered pioneer and non-pioneer firms", "For six and four years respectively "
             "from registration."),
            ("point", "(h) Excise taxes and petroleum", "Excise taxes on articles under the National Internal "
             "Revenue Code, and taxes, fees or charges on petroleum products."),
            ("point", "(i) Percentage tax and VAT", "On sales, barters or exchanges, except as the Code "
             "provides."),
            ("point", "(j) Carriers’ gross receipts", "Of transportation contractors and common carriers by "
             "air, land or water, except as the Code provides."),
            ("point", "(k) Reinsurance premiums", "Premiums paid by way of reinsurance or retrocession."),
            ("point", "(l) Vehicle registration and driver’s licenses", "Except for tricycles."),
            ("point", "(m) Exported products", "Philippine products actually exported, except as the Code "
             "provides."),
            ("point", "(n) Certain small enterprises and cooperatives", "Countryside and Barangay Business "
             "Enterprises registered under R.A. No. 6810, and cooperatives registered under R.A. No. 6938."),
            ("point", "(o) The government itself", "The National Government, its agencies and "
             "instrumentalities, and local government units."),
            "Read together, the list has a pattern. Items (a), (b), (c), (h) and (i) are taxes the national "
            "government collects under the National Internal Revenue Code, and item (d) covers customs. "
            "Items (e), (f) and (m) protect goods moving to market and abroad. Items (g) and (n) protect "
            "businesses the law wanted to encourage. Item (o) keeps one level of government from taxing "
            "another.",
            ("photo", "blog/finance-limits-check.jpg", "Checking a charge against Section 133: three questions "
             "before a fee or tax is collected. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Back to the Copra"),
            "Two items in the list fit the farmer’s slip.",
            ("point", "Item (e)", "A charge on goods simply passing through a locality, “in the guise of” a "
             "toll or any other name, is outside a local government’s taxing power."),
            ("point", "Item (f)", "Section 131 defines a marginal farmer or fisherman as an individual engaged "
             "in subsistence farming or fishing, limited to selling, bartering or exchanging products produced "
             "by himself and his immediate family. If the farmer fits that definition, a charge on his copra "
             "is also barred."),
            "The clerk advised the farmer to bring the slip to the treasurer of the municipality that issued it, and "
            "copied it for the municipal treasurer, who could raise it with that local government.",
            ("h", "Limits That Come Up at a Municipal Counter"),
            ("point", "Checkpoint fees on produce", "Item (e). A local government may regulate and charge for services it "
             "actually provides, such as the use of its market, under the rules in Part 19. It may not charge "
             "goods for crossing its land."),
            ("point", "Tricycles", "Item (l) bars local charges on vehicle registration and driver’s licenses, "
             "with one stated exception: tricycles."),
            ("point", "Cooperatives", "Item (n). A business that says it is a registered cooperative should "
             "show its registration. The office records it before deciding what applies."),
            ("point", "Government offices", "Item (o). A national agency’s office in the locality is not billed "
             "local taxes."),
            "Other items, such as income tax on banks or taxes on carriers, come up mostly at the city and "
            "province level, where the Code’s exceptions are written.",
            ("h", "Why the Revenue Code Must Be Checked"),
            "A tax ordinance that crosses Section 133 can be challenged. Part 15 described how an ordinance can "
            "be appealed to the Secretary of Justice under Section 187.",
            ("point", "For the sanggunian", "Before passing a new tax or fee, check the draft against all "
             "fifteen items."),
            ("point", "For the treasurer", "When a new ordinance arrives, read it with Section 133 open. If "
             "something looks doubtful, raise it in writing before collection starts."),
            ("point", "For collectors", "If a taxpayer asks why a charge applies, the answer should name the "
             "ordinance and its section, not only “that is the rule.”"),
            ("h", "What Each Person Should Check"),
            ("point", "Farmers and fishers", "Keep proof that you sell what your family produces, and keep "
             "every slip for a charge you think is wrong."),
            ("point", "Business owners", "If you are registered with the Board of Investments or as a "
             "cooperative, bring the registration when you apply for your permit."),
            ("point", "Treasury staff", "A short list of the Section 133 items most likely to arise, posted "
             "where assessments are made."),
            ("point", "The sanggunian", "A Section 133 review of every new revenue measure."),
            ("h", "Mistakes to Avoid"),
            ("point", "Renaming a barred tax as a fee", "Items (e) and (f) cover fees and charges too."),
            ("point", "Charging goods for passing through", "Only services the local government provides can be charged."),
            ("point", "Assuming every cooperative is exempt", "Check the registration first."),
            ("point", "Skipping the exceptions", "“Unless otherwise provided” sends you to other sections."),
            ("h", "Key Takeaways"),
            ("point", "Fifteen common limits", "Section 133 binds provinces, cities, municipalities and barangays."),
            ("point", "Fees count too", "Several items bar taxes, fees and charges alike."),
            ("point", "Goods passing through", "May not be charged for crossing a territory."),
            ("point", "Marginal farmers and fishers", "Their products may not be taxed when they sell them."),
            ("h", "Your Part 28 Action Plan"),
            ("point", "If you work in a treasury", "Read your revenue code’s list of fees and mark any that "
             "touch goods in transit or farm and fish products."),
            ("point", "If you sit in the sanggunian", "Ask for a one-page Section 133 check with every new "
             "revenue ordinance."),
            ("point", "If you farm or fish", "Keep every slip for a charge on your produce, and ask your "
             "treasury about it."),
            ("cta", "Read: Inside the Local Treasury, Part 15: Fee or Tax? Why the Difference Matters", "/blog/fee-or-tax/"),
            ("cta", "Read: Inside the Local Treasury, Part 1: Where Your Town's Money Comes From", "/blog/where-your-towns-money-comes-from/"),
            ("cta", "Read: Inside the Local Treasury, Part 19: The Public Market, a Business the Town Runs", "/blog/public-market-economic-enterprise/"),
            ("cta", "Read: Inside the Local Treasury, Part 27: Sealing the Market Scales, Fees for Weights and Measures", "/blog/weights-and-measures-fees/"),
            ("ask", "Have you ever been asked to pay a charge just to bring goods through another municipality or city?"),
        ],
    },
    {
        "title": "Inside the Local Treasury, Part 27: Sealing the Market Scales, Fees for Weights and Measures",
        "date": "April 29, 2027",
        "publish_on": "2027-04-29 21:00",  # blog rotation, one series a day (Butch 2026-11-14)
        "slug": "weights-and-measures-fees",
        "category": "finance",
        "summary": "A kilo at the market should be a kilo. This part explains how the Local Government Code "
                   "lets a town charge fees for sealing and licensing weights and measures, how the "
                   "sanggunian sets the rules and penalties, when the treasurer may settle a violation, and "
                   "how the Timbangan ng Bayan scales let buyers check for themselves.",
        "body": [
            "Aling Nena bought a kilo of galunggong at the public market and, on her way out, set the bag on "
            "the large scale near the market office. The needle stopped at 850 grams. She walked back to "
            "the stall. The vendor weighed it again on his own scale, and it showed exactly one kilo.",
            "One of the two scales was wrong. The question was which one, and whose job it was to find out.",
            "(Aling Nena, the market and the vendor are invented for this post. The law and the government "
            "programs described below are real and cited.)",
            "Part 26 covered a provincial tax on printing. This part stays in the town, at the public market "
            "that Part 19 described as a business the town runs. You will learn what the Local Government "
            "Code says about fees for sealing and licensing weights and measures, who sets the rules and "
            "penalties, when the municipal treasurer may settle a violation, how the public scales found in "
            "some markets work, and what vendors, buyers and treasury staff should each check.",
            ("photo", "blog/finance-scales.jpg", "Weights and measures: the town seals and licenses scales "
             "for a fee, the sanggunian sets rules and penalties, and buyers can check at a public scale. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "What the Code Says"),
            "Section 148 of the Local Government Code of 1991 covers fees for the sealing and licensing of "
            "weights and measures.",
            ("point", "Who levies the fee", "The municipality, at reasonable rates prescribed by the "
             "sangguniang bayan. Under Section 151, a city may also levy the fees a municipality may."),
            ("point", "The rules on use", "The sangguniang bayan prescribes the regulations for using weights "
             "and measures, subject to guidelines of the Department of Science and Technology."),
            ("point", "Penalties", "The sanggunian, by ordinance, penalizes fraudulent practices and the "
             "unlawful possession or use of instruments of weights and measures, and sets the criminal "
             "penalty in line with the Code."),
            ("point", "Settling a minor case", "The sanggunian may authorize the municipal treasurer to "
             "settle an offense not involving fraud, before a case is filed in court, upon payment of a "
             "compromise penalty of not less than ₱200."),
            ("h", "A Fee, Not a Tax"),
            "Part 15 explained the difference between a fee and a tax. The sealing fee is a regulatory fee. "
            "It pays for the work of checking the instruments, not for general revenue.",
            ("point", "Reasonable rates", "The Code uses those words. The fee should be reasonable for the "
             "work of testing and sealing, not set mainly to raise money."),
            ("point", "One instrument, one fee", "A revenue code can charge per scale, per balance or per "
             "measure, with different rates for different kinds. Check what yours says."),
            ("point", "A receipt and a seal", "The vendor pays the fee, receives an official receipt, and "
             "the instrument receives a seal showing it passed."),
            ("h", "What Sealing Means"),
            "Sealing is the act of testing an instrument against standard weights or measures and, if it is "
            "accurate enough, marking it as approved for use in trade.",
            ("point", "Test", "The inspector places known standard weights on the scale and compares the "
             "reading."),
            ("point", "Seal or reject", "An accurate scale is sealed. One that is off must be repaired or "
             "replaced before it is used."),
            ("point", "Repeat on schedule", "A seal is not forever. Scales drift and can be tampered with, so "
             "the ordinance sets how often instruments are rechecked."),
            "In an August 2018 report by PTV, the Department of Trade and Industry in Antique urged local "
            "governments to calibrate market scales. The report pointed to the Consumer Act of the "
            "Philippines, and a DTI engineer said vendors’ scales should be calibrated every six months by "
            "the treasurer’s office. She added that an ordinance on vendors’ scales would let the town "
            "collect an inspection fee.",
            ("photo", "blog/finance-scales-steps.jpg", "From a vendor’s scale to a sealed one, and what "
             "happens when a scale fails. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Timbangan ng Bayan: Letting Buyers Check"),
            "The large scale near the market office in the story is a real kind of program. Under Timbangan "
            "ng Bayan, the Department of Trade and Industry places public weighing scales in markets so "
            "buyers can check what they bought.",
            ("point", "A national partnership", "The Department of Science and Technology’s Industrial "
             "Technology Development Institute reported a memorandum of understanding signed on August 1, "
            "2024 for the Timbangan ng Bayan project, with DTI, DILG, DOST and a private bank."),
            ("point", "Accuracy of the public scale", "DOST-ITDI said its National Metrology Laboratory "
             "supports reliable scales through verification and re-verification against measurement "
             "standards."),
            ("point", "Use it", "A buyer who doubts a weight can check at the public scale and bring the "
             "difference to the market office."),
            ("h", "Back at the Market"),
            "The market supervisor tested both scales with the office’s standard weights. The public scale "
            "was accurate. The vendor’s scale read 150 grams heavy at one kilo. Its seal was more than a year "
            "old.",
            ("point", "If it was not fraud", "A worn spring, no sign of tampering. Under the ordinance, the "
             "treasurer may settle the case with a compromise penalty, if the sanggunian has authorized "
             "it, and the vendor repairs the scale before using it again."),
            ("point", "If it was fraud", "A tampered scale is not settled at the counter. The ordinance’s "
             "penalties apply, and the case can go to court."),
            "Either way, Aling Nena got her missing 150 grams of galunggong.",
            ("h", "Why a Few Grams Matter"),
            "A short weight looks small on one purchase. It adds up over a day of sales. Take the scale in "
            "the story, which read 150 grams heavy at one kilo. If that scale showed 40 kilos of fish sold in "
            "a day, buyers would have received about 6 kilos less than they paid for. At ₱200 a "
            "kilo, that is roughly ₱1,200 of fish paid for and never handed over, in one day, at one stall.",
            "(These numbers are for illustration only. They show the arithmetic, not the size of any real "
            "loss.)",
            ("point", "For buyers", "Each short kilo is money lost on food, and a household that buys "
             "every day pays the difference every day."),
            ("point", "For honest vendors", "A vendor with an accurate scale competes with one who gives "
             "less for the same price. Sealing protects the honest seller too."),
            ("point", "For the town", "The market is a business the town runs. Buyers who stop trusting "
             "its scales can take their shopping elsewhere."),
            ("h", "Keeping the Register"),
            "Sealing is only as good as the record behind it. A simple register, kept in a spreadsheet or a "
            "logbook, can hold one row per instrument.",
            ("point", "Columns to keep", "Stall number, vendor, kind of instrument, its capacity, the date "
             "sealed, the official receipt number for the fee, the result (passed or rejected) and the "
             "date of the next check."),
            ("point", "A monthly look", "Sort by the next-check date. Any row with a date already past is "
             "an instrument due for a visit."),
            ("point", "Rejected instruments", "Keep the row, note the defect, and record the date it was "
             "repaired and passed. The history shows which stalls have repeat problems."),
            ("h", "What Each Person Should Check"),
            ("point", "Vendors", "That each scale has a current seal and a receipt for the fee, and that it "
             "reads zero with nothing on it."),
            ("point", "Buyers", "That the scale reads zero before your goods go on it, and that you can see "
             "the display. When in doubt, use the public scale."),
            ("point", "Treasury and market staff", "A register of sealed instruments with the date of the "
             "next check, and standard weights that are themselves checked."),
            ("point", "The sanggunian", "That the ordinance sets the fee, the schedule, the penalties and, "
             "if desired, the treasurer’s authority to settle non-fraud cases."),
            ("h", "Mistakes to Avoid"),
            ("point", "Treating the fee as a money-maker", "It is a regulatory fee at reasonable rates."),
            ("point", "Sealing once and forgetting", "Set and follow a recheck schedule."),
            ("point", "Settling a fraud case at the counter", "Only non-fraud offenses may be compromised."),
            ("point", "Ignoring the public scale", "It is there so buyers can check."),
            ("h", "Key Takeaways"),
            ("point", "A municipal fee", "Section 148, at reasonable rates set by the sangguniang bayan."),
            ("point", "Rules follow DOST guidelines", "The sanggunian writes them."),
            ("point", "Compromise only without fraud", "Not less than ₱200, if authorized, before a court case."),
            ("point", "Buyers can check", "Timbangan ng Bayan scales in markets."),
            ("h", "Your Part 27 Action Plan"),
            ("point", "If you work in a treasury", "Find the weights and measures section of your revenue "
             "code and check when instruments were last sealed."),
            ("point", "If you sell at the market", "Look at your seal date, and ask when the next check is."),
            ("point", "If you shop at the market", "Find the public scale, and use it once to see how it works."),
            ("cta", "Read: Inside the Local Treasury, Part 19: The Public Market, a Business the Town Runs", "/blog/public-market-economic-enterprise/"),
            ("cta", "Read: Inside the Local Treasury, Part 15: Fee or Tax? Why the Difference Matters", "/blog/fee-or-tax/"),
            ("cta", "Read: Inside the Local Treasury, Part 26: The Printing and Publication Tax, What the Print Shop Pays the Province", "/blog/printing-and-publication-tax/"),
            ("cta", "Read: Inside the Local Treasury, Part 6: Can the Town Forgive a Tax?", "/blog/can-the-town-forgive-a-tax/"),
            ("ask", "Have you ever checked your purchase on the public scale at your market?"),
        ],
    },
    {
        "title": "Inside the Local Treasury, Part 26: The Printing and Publication Tax, What the Print Shop Pays the Province",
        "date": "April 24, 2027",
        "publish_on": "2027-04-24 21:00",  # blog rotation, one series a day (Butch 2026-11-14)
        "slug": "printing-and-publication-tax",
        "category": "finance",
        "summary": "A print shop or a publisher can owe a business tax to the province, not to the town. This "
                   "part explains what the Local Government Code covers under the printing and publication "
                   "tax, the rate ceiling, the rule for a shop in its first year, the exemption for school "
                   "texts, and how it fits with the town’s permit fees.",
        "body": [
            "The print shop beside the town plaza had been busy for a year. It printed wedding invitations, "
            "certificates for the elementary school, receipts for the stores on the main road, and posters "
            "for every fiesta. In January, the owner went to renew his business permit and asked the clerk "
            "at the municipal treasury a question he had been saving: why had a letter from the provincial "
            "treasurer arrived about a tax on his printing?",
            "The clerk smiled. It was a question she heard about once a year, usually from someone who had "
            "just paid the town and assumed that settled everything.",
            "(The print shop, its owner and the figures are invented for this post. The sections of the Local "
            "Government Code described below are real and are cited.)",
            "Part 25 covered the idle land tax. This part returns to taxes on business, and to one that the "
            "Local Government Code gives to the province rather than the town: the tax on the business of "
            "printing and publication. You will learn what it covers, who may levy it and at what rate, how "
            "a shop in its first year is taxed, what is exempt, and how it fits with the fees the town "
            "collects.",
            ("photo", "blog/finance-printing.jpg", "The printing and publication tax: levied by the province "
             "or city, up to half of one percent of last year’s gross receipts, with school texts exempt. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "What It Covers"),
            "Section 136 of the Local Government Code of 1991 allows the province to tax the business of "
            "persons engaged in printing or publication.",
            ("point", "What is printed or published", "Books, cards, posters, leaflets, handbills, "
             "certificates, receipts, pamphlets and others of a similar nature."),
            ("point", "Printers and publishers", "The section covers both: the shop that prints for "
             "customers, and the business that publishes its own materials."),
            "Part 24 showed that the franchise tax in Section 137 has almost the same structure. Both are "
            "provincial taxes on a particular kind of business, measured by gross receipts.",
            ("h", "Who May Levy It, and How Much"),
            ("point", "Who levies it", "The province. Under Section 151, a city may also levy the taxes a "
             "province may, with rates up to 50 percent higher than the provincial maximum."),
            ("point", "The base", "The gross annual receipts for the preceding calendar year."),
            ("point", "The ceiling", "Not more than 50 percent of 1 percent, which is half of one percent, "
             "or 0.5 percent."),
            ("point", "A business in its first year", "Not more than one-twentieth of 1 percent of the "
             "capital investment, or 0.05 percent."),
            ("point", "From the second year", "The tax is based on the gross receipts for the preceding "
             "calendar year, regardless of when the business started to operate."),
            "As always, the provincial or city revenue code sets the actual rate within the ceiling. Read "
            "it before quoting a number.",
            ("h", "The Exemption for School Texts"),
            "Section 136 exempts receipts from the printing or publishing of books or other reading materials "
            "prescribed by the Department of Education, Culture and Sports as school texts or references. "
            "Republic Act No. 9155, the Governance of Basic Education Act of 2001, renamed that department the "
            "Department of Education, so today the question is whether DepEd prescribes the material.",
            ("point", "What it covers", "Receipts from printing or publishing those prescribed materials, not "
             "all of the shop’s receipts."),
            ("point", "Keep the proof", "A shop claiming the exemption should keep the contract or order and "
             "the document showing the materials are prescribed, and record those receipts separately."),
            ("point", "Certificates are not school texts", "The school certificates the plaza shop printed "
             "are printing for a school, but they are not books or reading materials prescribed as texts. "
             "Those receipts remain taxable."),
            ("h", "A Worked Example"),
            "The numbers below are invented to show the arithmetic. They are not any province’s actual rate.",
            ("point", "Gross receipts, 2026", "₱2,000,000 in total. Of this, ₱400,000 came from printing "
             "reading materials prescribed as school references, with the documents to prove it."),
            ("point", "Taxable receipts", "₱2,000,000 − ₱400,000 = ₱1,600,000."),
            ("point", "The tax for 2027", "If the provincial ordinance uses the full 0.5 percent: "
             "₱1,600,000 × 0.5% = ₱8,000."),
            ("point", "The same shop in a city", "A city may go up to 50 percent above the provincial "
             "ceiling under Section 151. At 0.75 percent, the tax on ₱1,600,000 would be ₱12,000."),
            ("point", "A new shop", "A shop that opens in 2027 with a capital investment of ₱600,000 owes "
             "not more than 0.05 percent, or ₱300, for its first year. In 2028 it is taxed on its 2027 "
             "receipts."),
            ("photo", "blog/finance-printing-steps.jpg", "Computing the printing and publication tax: "
             "remove the exempt school-text receipts, then apply the rate. Figures are invented. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Where the Town Comes In"),
            "This is the part of the owner’s question that needs the most care.",
            ("point", "The tax goes to the province", "Section 142 lets a municipality levy taxes, fees and "
             "charges “not otherwise levied by provinces.” Since Section 136 gives this tax to the province, "
             "the town does not levy its own tax on the same printing business."),
            ("point", "The town still issues the permit", "Section 147 lets a municipality impose reasonable "
             "fees and charges on business, such as the mayor’s permit fee. Those regulatory fees are "
             "separate from the provincial tax."),
            ("point", "Check your own codes", "How the provincial and municipal revenue codes divide the "
             "work can differ. The provincial treasurer’s office can confirm what the shop owes to each."),
            "When to pay follows the general rules covered in Part 24: a calendar-year tax, payable in "
            "quarterly installments within the first 20 days of each quarter under Sections 165 and 167, "
            "with surcharges and interest for late payment under Section 168.",
            ("h", "What Each Person Should Check"),
            ("point", "Print shop owners", "Whether the province or city has a printing and publication "
             "tax, its rate, and whether any receipts qualify for the school-text exemption."),
            ("point", "The provincial treasury", "A list of printers and publishers in each town, built "
             "with the municipal permit records."),
            ("point", "The municipal treasury", "That the town’s permit fees are charged, and that no "
             "municipal tax is billed on the printing itself."),
            ("point", "Customers who order printing", "Nothing to file. The tax falls on the printer’s "
             "gross receipts, not on the person who orders the invitations, though a shop may consider it "
             "when it sets its prices."),
            ("h", "Mistakes to Avoid"),
            ("point", "Assuming the town collects it", "Section 136 gives it to the province, and to cities."),
            ("point", "Exempting everything printed for a school", "Only prescribed school texts and references."),
            ("point", "Using this year’s receipts", "The base is the preceding calendar year."),
            ("point", "No proof for the exemption", "Keep the order and the document that prescribes the material."),
            ("h", "Key Takeaways"),
            ("point", "A provincial and city tax", "Section 136, with Section 151 for cities."),
            ("point", "Half of one percent at most", "Of the preceding year’s gross receipts."),
            ("point", "First year: capital investment", "Not more than one-twentieth of 1 percent."),
            ("point", "School texts are exempt", "Receipts from prescribed texts and references."),
            ("h", "Your Part 26 Action Plan"),
            ("point", "If you run a print shop", "Ask the provincial treasurer’s office whether you are "
             "listed, and what records to bring."),
            ("point", "If you work in a provincial treasury", "Compare your list of printers with the "
             "towns’ business permit records."),
            ("point", "If you work in a municipal treasury", "Check that your revenue code does not tax a "
             "business the province already taxes."),
            "The clerk walked the print shop owner through it: the permit fee to the town, the printing tax "
            "to the province, and the school readers he had printed for the district office, which he could "
            "claim as exempt if he had the papers. He went home to look for the purchase order.",
            ("cta", "Read: Inside the Local Treasury, Part 24: The Franchise Tax, What Power and Telecom Companies Pay the Province or City", "/blog/franchise-tax/"),
            ("cta", "Read: Inside the Local Treasury, Part 2: The January Rush and Your Business Permit", "/blog/january-rush-business-permit/"),
            ("cta", "Read: Inside the Local Treasury, Part 15: Fee or Tax? Why the Difference Matters", "/blog/fee-or-tax/"),
            ("cta", "Read: Inside the Local Treasury, Part 1: Where Your Town's Money Comes From", "/blog/where-your-towns-money-comes-from/"),
            ("ask", "Does your province tax the printing business, and did you know the town does not?"),
        ],
    },
    {
        "title": "Inside the Local Treasury, Part 25: The Idle Land Tax, When an Empty Lot Costs More Than the Amilyar",
        "date": "April 19, 2027",
        "publish_on": "2027-04-19 21:00",  # blog rotation, one series a day (Butch 2026-11-14)
        "slug": "idle-land-tax",
        "category": "finance",
        "summary": "A large lot left empty, or a farm left mostly uncultivated, can carry a tax on top of the "
                   "amilyar. This part explains who may levy the idle land tax, the 5 percent ceiling, which "
                   "lands count as idle and which do not, how the assessor lists them and the treasurer "
                   "gives notice, and when an owner may be exempted.",
        "body": [
            "The letter arrived in March. It was from the provincial treasurer, and it said that a lot in the "
            "town center had been listed as idle land and would be charged an additional tax. The owner, a "
            "nurse working abroad, called her brother at home. “Idle?” she said. “I’m saving to build on it. "
            "Isn’t paying the amilyar enough?”",
            "Her brother went to the assessor’s office the next morning to find out what “idle” meant, and "
            "whether it could be undone.",
            "(The letter, the lot and the family are invented for this post. The sections of the Local "
            "Government Code described below are real and are cited.)",
            "Part 24 covered a tax on businesses holding a franchise. This part returns to real property, the "
            "source of the amilyar, and covers a levy that sits on top of it. You will learn who may levy the "
            "idle land tax and at what rate, which lands the Code treats as idle and which it does not, how "
            "the assessor and the treasurer share the work, when an owner may be exempted, and what owners and "
            "treasury workers should each check.",
            ("photo", "blog/finance-idle.jpg", "The idle land tax: up to 5 percent of assessed value on top "
             "of the basic tax, on large lots and farms left mostly unused, listed by the assessor and "
             "noticed by the treasurer. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Who May Levy It, and How Much"),
            "Section 236 of the Local Government Code of 1991 allows a province, a city, or a municipality "
            "within Metropolitan Manila to levy an annual tax on idle lands.",
            ("point", "The rate", "Not more than 5 percent of the assessed value of the property."),
            ("point", "On top of the basic tax", "The idle land tax is in addition to the basic real "
             "property tax. The Code groups it with the special levies on real property, alongside the "
             "Special Education Fund tax in Section 235."),
            ("point", "Who levies it outside Metro Manila", "For land in a municipality outside Metro Manila, "
             "it is the province that may levy the tax, through its own ordinance."),
            "As with other local taxes, the levy exists only if the sanggunian passes an ordinance. The rate in "
            "that ordinance can be lower than 5 percent. Before telling an owner a number, read the current "
            "revenue code of the province or city.",
            ("h", "Which Lands Count as Idle"),
            "Section 237 sets the coverage. It has three parts.",
            ("point", "Agricultural land", "More than one hectare in area, suitable for cultivation, dairying, "
             "inland fishery or other agricultural uses, half or more of which remains uncultivated or "
             "unimproved by the owner or the person having legal interest in it."),
            ("point", "Other land in a city or municipality", "More than 1,000 square meters in area, half or "
             "more of which remains unutilized or unimproved by the owner or the person having legal interest."),
            ("point", "Subdivision lots, regardless of area", "Residential lots in subdivisions approved by "
             "the proper authorities, once ownership has passed to individual owners, who become liable for the "
             "tax. Lots not yet transferred to a buyer are treated as part of the subdivision, and the "
             "subdivision owner or operator pays."),
            ("h", "What the Code Says Is Not Idle"),
            "Section 237 also lists two kinds of agricultural land that are not idle, even if they look "
            "quiet.",
            ("point", "Permanent or perennial crops", "Land planted to permanent or perennial crops with at "
             "least 50 trees to a hectare. A coconut farm or a mango orchard at that density is not idle land."),
            ("point", "Grazing land", "Land actually used for grazing is not idle either."),
            "The word “actually” matters. An assessor looks at the use of the land on the ground, the same "
            "rule Section 217 applies to classification in general: property is assessed by its actual use.",
            ("photo", "blog/finance-idle-check.jpg", "Is the land idle? Check the size, how much is unused, "
             "and the exceptions, then whether the owner was prevented from using it. (Illustration: Butch "
             "Mahinay, aumahinay.dev)", "medium"),
            ("h", "When an Owner May Be Exempted"),
            "Section 238 allows the province, city or Metro Manila municipality to exempt idle land from the "
            "additional levy when the owner, or the person having legal interest, is prevented from using, "
            "improving or cultivating it. The Code lists force majeure, civil disturbance and natural "
            "calamity, and adds any cause or circumstance that physically or legally prevents the owner.",
            ("point", "It is a may, not a must", "Section 238 gives the local government the power to exempt. "
             "The revenue code is the place to look for how an owner applies and what proof is needed."),
            ("point", "Keep the proof", "A certification of a calamity, a court order that stops "
             "construction, or a document showing why the land could not be used. An exemption has to be "
             "shown, not assumed."),
            ("h", "How the Assessor and the Treasurer Share the Work"),
            "Section 239 divides the job between two offices.",
            ("point", "The assessor lists", "The provincial, city or municipal assessor makes and keeps an "
             "updated record of all idle lands in the area."),
            ("point", "The treasurer gives notice", "For collection, the assessor gives a copy of the record "
             "to the provincial or city treasurer, who notifies the owner or person having legal interest "
             "that the additional tax is being imposed."),
            "The list is only as good as its last update. A lot that has been built on since the last "
            "inspection should come off it, and the owner can help by asking the assessor for a new look.",
            ("h", "A Worked Example"),
            "The numbers below are invented to show the arithmetic. They are not any province’s actual "
            "values or rates.",
            ("point", "The lot", "A 1,500 square meter commercial lot in the town center, completely vacant. "
             "It is more than 1,000 square meters, and more than half is unused, so it is covered."),
            ("point", "The assessed value", "Suppose the market value is ₱4,500,000 and the assessment level "
             "for commercial land is 50 percent. The assessed value is ₱2,250,000."),
            ("point", "The idle land tax", "If the provincial ordinance uses the full 5 percent, the "
             "additional tax is ₱112,500 a year. That is on top of the basic tax and the Special Education "
             "Fund tax."),
            ("point", "After building", "If the owner builds on more than half of the lot, it no longer meets "
             "the definition, and the additional tax should stop once the assessor’s record is updated."),
            "The guide to the RPT Calculator on this site explains how the market value and the assessment "
            "level turn into an assessed value. The idle land tax uses the same assessed value.",
            ("h", "Penalties and the 2024 Amnesty"),
            "An unpaid idle land tax is part of the unpaid real property tax. Part 6 described Republic Act "
            "No. 12001, whose Section 30 granted an amnesty on penalties, surcharges and interest on unpaid real "
            "property taxes, naming the idle land tax among them. That window closed in July 2026. Unpaid "
            "amounts now follow the ordinary rules, which Part 5 covered.",
            ("h", "What Each Person Should Check"),
            ("point", "Owners of large lots or farms", "The current revenue code, whether the land is on the "
             "idle land list, and the date of the last inspection."),
            ("point", "The assessor’s office", "That the list is updated after inspections, and that "
             "exceptions for perennial crops and grazing are applied."),
            ("point", "The treasury", "That notices go out based on the latest list, and that the "
             "exemption procedure in the ordinance is clear at the counter."),
            ("h", "Mistakes to Avoid"),
            ("point", "Thinking the amilyar covers it", "The idle land tax is an additional levy."),
            ("point", "Assuming a planted farm is idle", "Perennial crops at 50 trees a hectare, or "
             "actual grazing, are excluded."),
            ("point", "Waiting for the list to update itself", "Ask the assessor to inspect once the land "
             "is used or built on."),
            ("point", "Claiming an exemption without proof", "Section 238 requires a cause that prevented use."),
            ("h", "Key Takeaways"),
            ("point", "Up to 5 percent of assessed value", "Section 236, on top of the basic tax."),
            ("point", "Size and use decide coverage", "Over 1 hectare for farms, over 1,000 square meters for "
             "other land, half or more unused."),
            ("point", "Exceptions exist", "Perennial crops, grazing, and causes that prevent use."),
            ("point", "Assessor lists, treasurer notifies", "Section 239."),
            ("h", "Your Part 25 Action Plan"),
            ("point", "If you own land", "Measure how much of it is actually used, and compare it with "
             "Section 237."),
            ("point", "If you work in a treasury", "Find out whether your province or city levies the tax, "
             "and at what rate."),
            ("point", "If you work in an assessor’s office", "Check when the idle land record was last updated."),
            "At the assessor’s office, the brother learned that the lot had been listed after an inspection "
            "two years earlier. He brought the building permit his sister had secured that January, and the "
            "photos of the foundation being poured. The assessor scheduled a new inspection for the following "
            "month.",
            ("cta", "Read: Inside the Local Treasury, Part 24: The Franchise Tax, What Power and Telecom Companies Pay the Province or City", "/blog/franchise-tax/"),
            ("cta", "Read: How to Use the RPT Calculator: Know Your Amilyar Before You Pay", "/blog/how-to-use-the-rpt-calculator/"),
            ("cta", "Read: Inside the Local Treasury, Part 5: Unpaid Amilyar, From Notice to Auction", "/blog/unpaid-amilyar-notice-to-auction/"),
            ("cta", "Read: Inside the Local Treasury, Part 6: Can the Town Forgive a Tax?", "/blog/can-the-town-forgive-a-tax/"),
            ("ask", "Is there a large empty lot in your town center, and do you know whether it is on the idle land list?"),
        ],
    },
    {
        "title": "Inside the Local Treasury, Part 24: The Franchise Tax, What Power and Telecom Companies Pay the Province or City",
        "date": "April 14, 2027",
        "publish_on": "2027-04-14 21:00",  # blog rotation, one series a day (Butch 2026-11-14)
        "slug": "franchise-tax",
        "category": "finance",
        "summary": "A business that holds a franchise from the government can owe a franchise tax to the "
                   "province or city where it earns. This part explains who may levy it, the rate ceiling, "
                   "how a newly started franchise is taxed, when payment is due, and what the Supreme Court "
                   "said about the words “in lieu of all taxes.”",
        "body": [
            "A young staff member at a provincial treasury was sorting the January payments when she found "
            "a check from a telephone company that served the province. The memo line said “franchise tax.” She "
            "turned to the senior examiner beside her. The company already had a business permit "
            "from the town, so why was it paying the province as well?",
            "The examiner pulled out the provincial revenue code and opened it to a page with a paper clip "
            "on it. “Because the company holds something most businesses don’t,” he said. “A franchise.”",
            "(The treasury, the telephone company and the check are illustrations for this post. The law and the "
            "court cases described below are real and are cited.)",
            "Part 23 covered a provincial tax on sand and gravel. This part covers another tax that the Local "
            "Government Code gives to provinces and cities: the tax on businesses that enjoy a franchise. "
            "You will learn what a franchise is, who may levy the tax and at what rate, how a business in "
            "its first year is taxed, when the tax is due, what the Supreme Court has said about franchise "
            "holders who claimed they were exempt, and what treasury workers and franchise holders should "
            "each check.",
            ("photo", "blog/finance-franchise.jpg", "The franchise tax: levied by the province or city, up "
             "to half of one percent of last year’s gross receipts, with a separate rule for a business in "
             "its first year. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "What a Franchise Is"),
            "A franchise, in this sense, is not a fast-food brand. It is a right or privilege that the "
            "government grants to operate a business affecting the public, through a law passed by "
            "Congress or a grant by an authorized agency. Examples include electric distribution, "
            "telecommunications, and radio and television broadcasting.",
            "In National Power Corporation v. City of Cabanatuan, G.R. No. 149110, decided April 9, 2003, "
            "the Supreme Court described a franchise tax as “a tax on the privilege of transacting business "
            "in the state and exercising corporate franchises granted by the state.” The Court added that "
            "the tax falls on the corporation that exercises the franchise, not on its stockholders.",
            ("h", "Who May Levy It, and How Much"),
            "Section 137 of the Local Government Code of 1991 opens with strong words: “Notwithstanding any "
            "exemption granted by any law or other special law, the province may impose a tax on businesses "
            "enjoying a franchise.” The section then sets the ceilings.",
            ("point", "Who levies it", "The province. Under Section 151, a city may also levy the taxes "
             "that a province may, and its rates may exceed the provincial maximum by not more than 50 "
             "percent. A municipality does not levy this tax."),
            ("point", "The base", "The gross annual receipts for the preceding calendar year, based on the "
             "incoming receipt, or realized, within the province’s territorial jurisdiction."),
            ("point", "The ceiling", "Not more than 50 percent of 1 percent of those gross receipts. In "
             "plainer terms, half of one percent, or 0.5 percent."),
            ("point", "A business in its first year", "For a newly started business, the tax may not exceed "
             "one-twentieth of 1 percent of the capital investment. That is 0.05 percent."),
            ("point", "From the second year", "Regardless of when the business started to operate, the tax "
             "is based on the gross receipts for the preceding calendar year, or any fraction of it."),
            "The provincial or city revenue code sets the actual rate within those ceilings. Read your own "
            "code before quoting a number, because the ordinance can be lower than the maximum.",
            ("h", "A Worked Example"),
            "The numbers below are invented to show the arithmetic. They are not any company’s actual "
            "receipts or any province’s actual rate.",
            ("point", "An established franchise", "A telephone company realized ₱40,000,000 in gross receipts "
             "within the province during 2026. If the provincial ordinance uses the full 0.5 percent, the "
             "2027 franchise tax is ₱200,000."),
            ("point", "The same company in a city", "If the receipts had been realized in a city whose code "
             "uses the full 50 percent allowance, the rate could reach 0.75 percent, or ₱300,000."),
            ("point", "A new franchise", "A new radio station starts operating under its franchise in 2027, with a capital investment "
             "of ₱10,000,000. Its first-year tax may not exceed 0.05 percent, or ₱5,000. In 2028 it is taxed "
             "on its 2027 gross receipts, even if it operated for only a few months."),
            ("photo", "blog/finance-franchise-steps.jpg", "How the franchise tax is computed: last year’s "
             "gross receipts for an established franchise, the capital investment for a new one. Figures are "
             "invented. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "When It Is Due"),
            "The Code also has general rules for paying local taxes. Under Section "
            "165, the tax period is the calendar year, and the tax may be paid in quarterly installments. "
            "Under Section 167, unless the Code provides otherwise, local taxes are paid within the first 20 "
            "days of January or of each following quarter.",
            "Late payment has a cost. Section 168 allows a surcharge of up to 25 percent of the unpaid amount "
            "and interest of up to 2 percent a month on the unpaid amount, including the surcharge, for no "
            "more than 36 months. Part 2 explained the same rules for the business permit, and they work "
            "the same way here.",
            ("h", "“In Lieu of All Taxes” and the Courts"),
            "Some legislative franchises say that the franchise holder pays a national franchise tax “in "
            "lieu of all taxes.” Franchise holders have argued that those words free them from local taxes. "
            "The Supreme Court has rejected that argument in several cases.",
            ("point", "City Government of San Pablo v. Reyes", "G.R. No. 127708, March 25, 1999. Manila "
             "Electric Company paid the city’s franchise tax under protest for 1994 to 1996, citing its "
             "older franchise. The Court held that the “magic words” of the clause must give way to Section "
             "193 of the Code, which withdrew tax exemptions upon its effectivity, except those it listed."),
            ("point", "National Power Corporation v. City of Cabanatuan", "The city assessed the government "
             "power company ₱808,606.41 based on its 1992 gross receipts. The Court held the company liable: "
             "it exercised a franchise, its activities were proprietary, and its old exemption had been "
             "withdrawn."),
            ("point", "Smart Communications v. City of Davao", "G.R. No. 155491, September 16, 2008. "
             "Smart’s franchise was granted after the Code took effect, so the Section 193 withdrawal did "
             "not reach it. The Court still ruled for the city. It read the “in lieu of all taxes” clause as "
             "covering national taxes only, and said tax exemptions “are strictly construed against the "
             "taxpayer.” The Court denied Smart’s motion for reconsideration on July 21, 2009."),
            "The lesson is not that every franchise holder must pay. A later franchise can grant a clear "
            "exemption from local taxes, and the Court in Smart noted that another company’s franchise did. "
            "The lesson is to read the exact words of the franchise. An exemption has to be clear; it is not "
            "presumed.",
            ("h", "What Each Office Should Check"),
            ("point", "Provincial or city treasury", "A list of franchise holders operating in the area, "
             "the franchise law of each, and whether each one has filed its gross receipts for the year."),
            ("point", "The examiner", "That the declared receipts are those realized within the province or "
             "city, and that they match the financial statements filed."),
            ("point", "The franchise holder", "The rate in the current revenue code, the deadline, and any "
             "exemption in its own franchise, read word for word, not summarized."),
            ("point", "Municipal treasury", "That the town does not issue a bill for this tax by mistake, "
             "since the Code gives it to the province and to cities."),
            ("h", "Mistakes to Avoid"),
            ("point", "Assuming “in lieu of all taxes” covers local taxes", "The Supreme Court ruled "
             "otherwise in San Pablo and in Smart."),
            ("point", "Charging more than the ceiling", "0.5 percent for a province, with the Section 151 "
             "allowance only for a city."),
            ("point", "Using this year’s receipts", "The base is the preceding calendar year."),
            ("point", "Forgetting the first-year rule", "A new franchise is taxed on its capital investment, "
             "not on receipts it has not earned yet."),
            ("h", "Key Takeaways"),
            ("point", "A provincial and city tax", "Section 137, with Section 151 for cities."),
            ("point", "Half of one percent at most", "Of the preceding year’s gross receipts realized in the area."),
            ("point", "First year: capital investment", "Not more than one-twentieth of 1 percent."),
            ("point", "Exemptions must be clear", "G.R. Nos. 127708, 149110 and 155491."),
            ("h", "Your Part 24 Action Plan"),
            ("point", "If you work in a treasury", "Open the franchise tax section of your revenue code and "
             "check the rate and base against Section 137."),
            ("point", "If you manage a franchise holder", "Ask your accountant how the receipts realized in "
             "each province or city are separated, and keep that breakdown with the return."),
            ("point", "If you are studying local taxation", "Read the three cases above in order and note how "
             "the Court treated an older franchise and a newer one."),
            "Back at the treasury, the young staff member asked one more question. How did they know the "
            "telephone company’s receipts were complete? The examiner handed her the company’s financial "
            "statements. “You compare,” he said. By noon she had found that the figures matched.",
            ("cta", "Read: Inside the Local Treasury, Part 23: The Sand and Gravel Tax, and Why the Barangay Gets the Biggest Share", "/blog/sand-and-gravel-tax/"),
            ("cta", "Read: Inside the Local Treasury, Part 2: The January Rush and Your Business Permit", "/blog/january-rush-business-permit/"),
            ("cta", "Read: Inside the Local Treasury, Part 6: Can the Town Forgive a Tax?", "/blog/can-the-town-forgive-a-tax/"),
            ("cta", "Read: Inside the Local Treasury, Part 18: Paid Too Much? Refunds, Tax Credits and Protests", "/blog/local-tax-refunds-and-credits/"),
            ("ask", "Which franchise holders operate in your province or city, and do you know which office collects their tax?"),
        ],
    },
    {
        "title": "Inside the Local Treasury, Part 23: The Sand and Gravel Tax, and Why the Barangay Gets the Biggest Share",
        "date": "April 9, 2027",
        "publish_on": "2027-04-09 21:00",  # blog rotation, one series a day (Butch 2026-11-14)
        "slug": "sand-and-gravel-tax",
        "category": "finance",
        "summary": "Every truckload of sand taken from a river can carry a tax for the province, the town "
                   "and the barangay. This part explains who may levy the tax on sand, gravel and other "
                   "quarry resources, the 10 percent ceiling, who issues the permit, how the money is "
                   "shared 30, 30 and 40, and what the Supreme Court said about quarrying for one’s own use.",
        "body": [
            "Every dry season, the trucks lined up at the riverbank below a small barangay. They came "
            "empty in the morning and left heavy with sand and gravel for a road project two towns away. "
            "At the barangay assembly, a farmer stood up with a question for the barangay treasurer. The "
            "trucks were wearing down the barangay road and taking the barangay’s river sand. Did the "
            "barangay get anything from it?",
            "The treasurer had the answer in a folder. The barangay got the largest share of all.",
            "(The barangay, the river and the trucks are illustrations for this post. The law and the court "
            "case described below are real and are cited.)",
            "Part 22 covered a tax on tickets to shows. This part covers a tax on what is taken out of the "
            "ground and the riverbed. You will learn who may levy the tax on sand, gravel and other quarry "
            "resources and on what, the ceiling on the rate, who issues the permit to extract, how the money "
            "is divided among the province, the town and the barangay, what the Supreme Court said about a "
            "company that quarried for its own use, and what treasury workers, contractors and barangay "
            "officials should each check.",
            ("photo", "blog/finance-quarry.jpg", "The sand and gravel tax: levied by the province, up to "
             "10 percent of the local market value, with a permit from the governor, shared 30, 30 and 40. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Who May Levy It, and on What"),
            "Section 138 of the Local Government Code of 1991 gives this tax to the province. Under Section "
            "151, a city may also levy the taxes that a province may.",
            ("point", "What is taxed", "Ordinary stones, sand, gravel, earth and other quarry resources, as "
             "defined under the National Internal Revenue Code."),
            ("point", "From where", "Resources extracted from public lands, or from the beds of seas, lakes, "
             "rivers, streams, creeks and other public waters within the province."),
            ("point", "How much", "Not more than 10 percent of the fair market value in the locality, per "
             "cubic meter. The provincial ordinance sets the actual rate within that ceiling."),
            ("point", "Who issues the permit", "Section 138 says the permit to extract shall be issued "
             "exclusively by the provincial governor, under the ordinance of the sangguniang panlalawigan."),
            ("h", "Where the Mining Act Comes In"),
            "The Philippine Mining Act of 1995, Republic Act No. 7942, also deals with quarrying. It sets "
            "the rules for the permits themselves.",
            ("point", "Quarry permit", "Under Section 43, applications go to the provincial or city mining "
             "regulatory board, and the provincial governor grants the permit once the requirements are met. "
             "The area is limited to five hectares, for a term of five years, renewable up to a total of "
             "25 years."),
            ("point", "Commercial sand and gravel permit", "Under Section 46, the provincial governor may "
             "grant a permit to extract and remove sand and gravel from an area of not more than five "
             "hectares."),
            ("point", "Fees and taxes", "Section 44 requires the permittee to pay a quarry fee and the "
             "excise tax provided by pertinent laws."),
            "In short, the permit allows the digging, and the provincial tax is paid on what is dug. One "
            "does not replace the other.",
            ("h", "How the Money Is Shared"),
            "Section 138 sets the division of the proceeds. Unlike the amusement tax in Part 22, which is "
            "split between two levels, this one is split among three.",
            ("point", "Province", "30 percent."),
            ("point", "Component city or municipality where the resources are extracted", "30 percent."),
            ("point", "Barangay where the resources are extracted", "40 percent."),
            "The barangay’s share is the largest because the barangay lives with the effects: the trucks, "
            "the dust, the riverbanks and the roads. The law does not state that reason in Section 138, so "
            "treat it as a reading of the numbers, not as a quoted rule.",
            ("h", "A Worked Example"),
            "The numbers below are invented to show the arithmetic. They are not any province’s actual "
            "values.",
            ("point", "The value", "Suppose the provincial ordinance values river sand at ₱500 per cubic "
             "meter in the locality and sets the rate at 10 percent. The tax is ₱50 per cubic meter."),
            ("point", "The volume", "A contractor hauls 2,000 cubic meters during the month. The tax is "
             "2,000 times ₱50, or ₱100,000."),
            ("point", "The shares", "Province ₱30,000. Municipality ₱30,000. Barangay ₱40,000."),
            ("photo", "blog/finance-quarry-split.jpg", "The worked example as a picture: ₱100,000 of quarry tax "
             "shared 30, 30 and 40 percent under Section 138. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            "₱40,000 a month is a meaningful amount for a small barangay. It is one reason barangay "
            "officials should know the volume being extracted in their area.",
            ("h", "Quarrying for One’s Own Use Is Still Taxed"),
            "In Lepanto Consolidated Mining Co. v. Ambanloc, G.R. No. 180639, decided June 29, 2010, a "
            "mining company had taken sand, gravel and earth from its own mining claim in Benguet from 1997 "
            "to 2000. It used them to backfill mined areas and to build and maintain its tailings dam, "
            "roads and offices. None of it was sold. The provincial treasurer assessed sand and gravel tax, "
            "and the company protested.",
            ("point", "The company’s argument", "The tax covered only commercial extraction, and its "
             "national mining lease already allowed it to extract."),
            ("point", "The Court’s answer", "The provincial revenue code exempted only gratuitous permits, "
             "so use for its own operations was not exempt. The lease showed the national government’s "
             "consent, but “an exemption from the requirements of the provincial government should have a "
             "clear basis.”"),
            ("point", "The kind of tax", "The Court called it an excise tax on the privilege of extracting, "
             "and said provinces can levy it independently from the national government."),
            "The lesson for treasuries is to read the provincial revenue code closely. The outcome turned "
            "on what that code exempted, and on what it did not.",
            ("h", "What Each Office Should Check"),
            ("point", "Provincial treasury", "That the revenue code’s rate stays within 10 percent, that "
             "volumes are recorded per barangay, and that the 30 and 40 percent shares are released to "
             "the right municipality and barangay."),
            ("point", "Municipal treasury", "That the municipality’s 30 percent arrives, and that it "
             "matches the volumes extracted within the town."),
            ("point", "Barangay treasurer", "That the barangay’s 40 percent arrives, with a breakdown by "
             "period. Part 17 described how to follow up on the barangay’s share of the amilyar; the same "
             "habit applies here."),
            ("point", "Contractors and haulers", "That a permit covers the site, and that the tax is paid "
             "under the provincial procedure. Some provinces publish these steps in their Citizen’s Charter."),
            ("h", "Mistakes to Avoid"),
            ("point", "Thinking the permit covers the tax", "A permit allows extraction; the tax is separate."),
            ("point", "Assuming own use is exempt", "The Supreme Court ruled otherwise in Lepanto."),
            ("point", "Charging more than 10 percent", "Section 138 sets the ceiling."),
            ("point", "Forgetting the barangay’s 40 percent", "It is the largest share."),
            ("h", "Key Takeaways"),
            ("point", "A provincial tax", "Under Section 138, also open to cities under Section 151."),
            ("point", "Not more than 10 percent", "Of the fair market value in the locality, per cubic meter."),
            ("point", "Shared 30, 30 and 40", "Province, city or municipality, and barangay."),
            ("point", "Own use is not exempt", "G.R. No. 180639, June 29, 2010."),
            ("h", "Your Part 23 Action Plan"),
            ("point", "If you work in a treasury", "Find the quarry tax section of your provincial revenue "
             "code and check the rate, the valuation and the sharing against Section 138."),
            ("point", "If you are a barangay official", "Ask the provincial or municipal treasury for the "
             "volumes extracted in your barangay and the share released for the last year."),
            ("point", "If you hire trucks for a project", "Ask your supplier whether the sand comes from a "
             "permitted site and whether the tax was paid."),
            "The farmer at the assembly asked one more question: how much had the barangay actually "
            "received? The treasurer did not know offhand. She wrote to the provincial treasury the next "
            "week, asking for the volumes and the shares for the past year. When the reply came, she read "
            "it aloud at the next assembly.",
            ("cta", "Read: Inside the Local Treasury, Part 22: The Amusement Tax, Cinemas, Concerts and Why Resorts Are Not Covered", "/blog/amusement-tax/"),
            ("cta", "Read: Inside the Local Treasury, Part 17: The Barangay’s Share of the Amilyar, and When It Must Arrive", "/blog/barangay-share-of-real-property-tax/"),
            ("cta", "Read: Inside the Local Treasury, Part 15: Fee or Tax? Why the Difference Matters", "/blog/fee-or-tax/"),
            ("cta", "Read: Inside the Local Treasury, Part 1: Where Your Town's Money Comes From", "/blog/where-your-towns-money-comes-from/"),
            ("ask", "Is there a river or quarry near you, and do you know how much your barangay receives from it?"),
        ],
    },
    {
        "title": "Inside the Local Treasury, Part 22: The Amusement Tax, Cinemas, Concerts and Why Resorts Are Not Covered",
        "date": "April 4, 2027",
        "publish_on": "2027-04-04 21:00",  # blog rotation, one series a day (Butch 2026-11-14)
        "slug": "amusement-tax",
        "category": "finance",
        "summary": "Part of every cinema or concert ticket can go to the province and the town. This part "
                   "explains who may levy the amusement tax, the 10 percent ceiling set in 2009, which shows "
                   "are exempt, why the Supreme Court said resorts and swimming pools are not covered, and how "
                   "the money is shared.",
        "body": [
            "A businessman in a provincial town opened a small cinema beside the public market and, a few "
            "months later, a resort with two swimming pools on the edge of town. At the end of his first "
            "quarter, he came to the treasury with two questions. Did he owe amusement tax on the movie "
            "tickets? And did he owe it on the resort’s entrance fees too? A neighbor had told him that "
            "everything people pay for fun is taxed the same way.",
            "The neighbor was wrong on the second point, and the Supreme Court had said so.",
            "(The businessman, his cinema and his resort are illustrations, not a real case. The court "
            "decision discussed later is real and is named.)",
            "Part 21 covered a tax on professionals. This part covers a tax on entertainment. You will learn "
            "who may levy the amusement tax and on what, the current ceiling on the rate, which events the "
            "law exempts, why resorts, swimming pools and tourist spots fall outside it, how the tax is "
            "withheld and shared, and what treasury workers and business owners should each check.",
            ("photo", "blog/finance-amusement.jpg", "The amusement tax: on admission to shows, up to 10 percent, "
             "with exemptions for the arts, and not on resorts. (Illustration: Butch Mahinay, aumahinay.dev)",
             "medium"),
            ("h", "Who May Levy It, and on What"),
            "Section 140 of the Local Government Code lets the province levy an amusement tax, collected "
            "from the proprietors, lessees or operators of theaters, cinemas, concert halls, circuses, boxing "
            "stadia and other places of amusement. The tax is a percentage of the gross receipts from "
            "admission fees.",
            ("point", "Who pays", "The operator of the place, out of the admission fees collected. The tax "
             "is computed on ticket sales, not on food, drinks or other sales inside."),
            ("point", "What “amusement” means", "Section 131 defines amusement as a pleasurable diversion "
             "and entertainment, and amusement places as theaters, cinemas, concert halls, circuses and other "
             "places where one seeks admission to entertain oneself by seeing or viewing the show or "
             "performances."),
            ("point", "Cities too", "Section 151 lets a city levy the taxes a province may impose. Cities may "
             "set tax rates up to 50 percent above the provincial maximum, but Section 151 makes an "
             "exception for professional and amusement taxes, so the provincial ceiling also binds cities."),
            ("quote", "The amusement tax follows the ticket to a show, not every peso spent on a good time."),
            ("h", "The Rate: Ten Percent Since 2009"),
            "The Local Government Code of 1991 first set the ceiling at 30 percent of gross receipts from "
            "admission fees. Republic Act No. 9640, which lapsed into law on May 21, 2009, amended Section "
            "140(a) and lowered the ceiling to not more than 10 percent.",
            "Some older copies of the Code online still show 30 percent. When you read the law, check that "
            "you have the amended text, and read your provincial or city revenue code for the actual rate, "
            "which can be lower than the ceiling.",
            ("h", "A Worked Example"),
            "Say a cinema in a municipality sells ₱500,000 in tickets in a month, and the province’s revenue "
            "code sets the rate at the 10 percent maximum.",
            ("point", "The tax", "10 percent of ₱500,000 is ₱50,000."),
            ("point", "Withheld first", "Section 140(b) says that for theaters and cinemas, the tax is first "
             "deducted and withheld by the operator and paid to the provincial treasurer before the gross "
             "receipts are divided with the film distributors. So the ₱50,000 comes off the top, and the "
             "remaining ₱450,000 is what the cinema and the distributor share."),
            ("point", "Shared equally", "Section 140(e) says the proceeds are shared equally by the province "
             "and the municipality where the amusement place is located: ₱25,000 each."),
            ("point", "When and how", "Section 140(d) leaves the time, manner, terms and conditions of "
             "payment to the sangguniang panlalawigan, along with surcharges, interest and penalties for "
             "fraud or failure to pay."),
            ("h", "What the Law Exempts"),
            "Section 140(c) exempts the holding of operas, concerts, dramas, recitals, painting and art "
            "exhibitions, flower shows, musical programs, and literary and oratorical presentations, except "
            "pop, rock or similar concerts.",
            ("point", "A school recital or a town art exhibit", "Exempt."),
            ("point", "A rock concert in the plaza with paid tickets", "Not exempt. The law names pop, rock "
             "and similar concerts as the exception to the exemption."),
            ("point", "Films graded by the Film Development Council", "Republic Act No. 9167 of 2002, which "
             "created the Film Development Council of the Philippines, provides for an amusement tax refund "
             "on graded films: 100 percent for Grade A films and 65 percent for Grade B, with the remaining "
             "35 percent going to the Council, as summarized by the legal database Jur.ph. The rules for "
             "claiming it are with the Council."),
            ("h", "Why Resorts and Swimming Pools Are Not Covered"),
            "In Pelizloy Realty Corporation v. Province of Benguet, G.R. No. 183137, decided on April 10, "
            "2013, the Supreme Court looked at a provincial revenue code that charged amusement tax on "
            "admission fees to resorts, swimming pools, bath houses, hot springs and tourist spots.",
            ("point", "The question", "Were these “other places of amusement” under Section 140?"),
            ("point", "The answer", "No. The Court applied a rule of reading called ejusdem generis: general "
             "words that follow a list of specific things cover only things of the same kind. Theaters, "
             "cinemas, concert halls, circuses and boxing stadia are all places where shows or performances "
             "are staged to be watched. Resorts and swimming pools are not."),
            ("point", "The result", "The Court declared that part of the provincial revenue code void insofar "
             "as it imposed amusement tax on admission fees to resorts, swimming pools, bath houses, hot "
             "springs and tourist spots. The tax on admission to boxing was left standing."),
            "The Court also repeated a principle worth remembering at every treasury window: taxing powers "
            "are construed strictly, so a doubt about whether a tax applies is not resolved in favor of "
            "collecting it.",
            "A resort can still owe other local taxes and fees, such as the business tax on its gross "
            "receipts and its permit fees, under the local revenue code. It is the amusement tax on its "
            "entrance fees that the Court ruled out.",
            ("h", "For Treasury Workers"),
            ("point", "Read the amended Section 140", "Confirm that your local revenue code’s rate does not "
             "exceed 10 percent."),
            ("point", "Check the list of places", "If your code taxes resorts, pools or tourist spots under "
             "the amusement tax, raise it with your legal office in light of the Pelizloy decision."),
            ("point", "Ask for the ticket records", "Gross receipts from admissions are the base. Ticket "
             "stubs, sales reports and distributor statements support the return."),
            ("point", "Record the share", "Proceeds are shared equally with the municipality where the place "
             "is located. Keep the location on every collection, as with the barangay shares in Part 17."),
            ("h", "For Business Owners"),
            ("point", "Know your category", "A cinema or a ticketed rock concert is covered. A recital, an "
             "art exhibit or a resort entrance fee is not covered by the amusement tax."),
            ("point", "Keep admissions separate", "Record ticket sales apart from food and other sales, so "
             "the tax base is clear."),
            ("point", "Ask in writing", "If you are unsure whether an event is exempt, write to the treasurer "
             "before the event, and keep the reply. Part 18 explained the remedies if you pay too much."),
            ("h", "Mistakes to Avoid"),
            ("point", "Using the old 30 percent", "The ceiling has been 10 percent since 2009."),
            ("point", "Taxing resort entrance fees as amusement", "The Supreme Court ruled them out in 2013."),
            ("point", "Taxing a recital or art exhibit", "Section 140(c) exempts them."),
            ("point", "Forgetting the municipality’s half", "Proceeds are shared equally."),
            ("h", "Key Takeaways"),
            ("point", "Levied by the province or city", "On gross receipts from admission fees."),
            ("point", "Not more than 10 percent", "Under Republic Act No. 9640."),
            ("point", "Shows, not resorts", "Pelizloy, G.R. No. 183137, April 10, 2013."),
            ("point", "Half to the municipality", "Where the amusement place is located."),
            ("h", "Your Part 22 Action Plan"),
            ("point", "If you work in a treasury", "Find the amusement tax section of your revenue code and "
             "check the rate and the list of places against Section 140 and Pelizloy."),
            ("point", "If you run an event", "Check whether it falls under the exemptions before you print "
             "tickets."),
            ("point", "If you buy a ticket", "Know that part of it may fund your province and your town, "
             "half and half."),
            "The businessman left with two answers. The cinema owed amusement tax on its ticket sales, "
            "withheld before the split with the distributor. The resort’s entrance fees did not, though the "
            "resort still had its business tax to pay. He thanked the cashier, and asked for a copy of the "
            "court decision to show his neighbor.",
            ("cta", "Read: Inside the Local Treasury, Part 21: The Professional Tax, What Your PTR Number Means", "/blog/professional-tax-receipt/"),
            ("cta", "Read: Inside the Local Treasury, Part 15: Fee or Tax? Why the Difference Matters", "/blog/fee-or-tax/"),
            ("cta", "Read: Inside the Local Treasury, Part 18: Paid Too Much? Refunds, Tax Credits and Protests", "/blog/local-tax-refunds-and-credits/"),
            ("cta", "Read: Inside the Local Treasury, Part 17: The Barangay’s Share of the Amilyar, and When It Must Arrive", "/blog/barangay-share-of-real-property-tax/"),
            ("ask", "Have you ever paid an entrance fee and wondered which part of it was a tax?"),
        ],
    },
    {
        "title": "Inside the Local Treasury, Part 21: The Professional Tax, What Your PTR Number Means",
        "date": "March 30, 2027",
        "publish_on": "2027-03-30 21:00",  # blog rotation, one series a day (Butch 2026-11-14)
        "slug": "professional-tax-receipt",
        "category": "finance",
        "summary": "Engineers, nurses, accountants and other licensed professionals see a PTR number under "
                   "signatures on plans, reports and prescriptions. It is the receipt for a local tax. This "
                   "part explains who pays the professional tax, how much, where and when, who is exempt, "
                   "and why the receipt number must be written on documents.",
        "body": [
            "A young civil engineer passed the board exam, got her license, and in March was hired by a "
            "construction firm. On her first week, the project manager handed back the building plans she "
            "had signed. “Your PTR number is missing under your name. And the office needs a copy of the "
            "receipt before payroll.” She knew her license number by heart. She had never heard of a PTR.",
            "(The engineer, her firm and her first week are illustrations, not a real person or company.)",
            "Part 20 looked at who does what inside the treasurer’s office. This part looks at one tax "
            "that brings first-time professionals to a treasury window. Read on to learn what the "
            "professional tax is, who must pay it and how much, where and when it is paid, who is exempt, "
            "what happens when it is paid late, and why the official receipt number travels with a "
            "professional’s signature.",
            ("photo", "blog/finance-ptr.jpg", "The professional tax: who pays, how much, when it is due, and "
             "why the receipt number goes under the signature. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "What the Professional Tax Is"),
            "Section 139 of the Local Government Code allows the province to levy an annual professional "
            "tax on each person engaged in the exercise or practice of a profession that requires a "
            "government examination. The official receipt issued for it is what people call the PTR, the "
            "professional tax receipt.",
            ("point", "Who it covers", "People practicing a profession that requires a government "
             "examination, such as the board and bar examinations. The license comes from passing the "
             "exam; the professional tax is a separate local tax for practicing."),
            ("point", "How much", "Section 139(a) lets the sangguniang panlalawigan set the amount and "
             "reasonable classes, but it can in no case exceed ₱300 a year."),
            ("point", "Cities too", "Section 151 lets a city levy the taxes the province may impose. Cities "
             "may set tax rates up to 50% above the provincial maximum, but Section 151 makes an "
             "exception for professional and amusement taxes. So the ₱300 cap applies in cities as well."),
            ("quote", "The license says you may practice. The PTR says you paid the local tax for practicing "
             "this year."),
            ("h", "Where and When to Pay"),
            ("point", "Where", "Section 139(b) says to pay the province where you practice, or where you "
             "keep your principal office if you practice in several places. In a city that levies the tax, "
             "it goes to the city."),
            ("point", "When", "Section 139(d) says the tax is payable annually, on or before January 31."),
            ("point", "Starting later in the year", "The same paragraph says a person who first begins "
             "to practice after January must pay the full tax before starting. There is no half-year rate "
             "for starting in March."),
            ("point", "One payment, the whole country", "Section 139(b) adds that once the tax is paid, "
             "the professional may practice anywhere in the Philippines without being made to pay any "
             "other national or local tax, license or fee for practicing that profession."),
            ("point", "Ask the right office", "Section 170 lets treasurers collect through duly authorized "
             "deputies. If you are unsure where your PTR is issued, ask the provincial treasurer’s office, "
             "or the city treasurer’s office if you practice in a city."),
            ("h", "Who Is Exempt"),
            ("point", "Government employees", "Section 139(d) says professionals exclusively employed in the "
             "government are exempt."),
            ("point", "Exclusively is the key word", "A nurse employed only in a government hospital is "
             "exempt. If the same nurse also works shifts at a private clinic, the employment is no longer "
             "exclusively in government, and the tax applies."),
            ("point", "A second profession", "Section 139(d) also says a line of profession does not become "
             "exempt just because it is practiced together with another profession whose tax was paid. A "
             "person licensed and practicing as both a lawyer and an accountant pays for each."),
            ("h", "The Employer’s Duty"),
            "Section 139(c) puts a duty on the employer as well. Any individual or corporation employing "
            "a person subject to the professional tax must require that person to pay the tax before "
            "employment and every year after.",
            "That is why the engineer’s firm asked for a copy of her receipt. A firm that hires licensed "
            "professionals can keep a simple list: each employee, the PTR number, the date paid and the "
            "province or city, and check it every January.",
            ("h", "Why the Number Goes Under Your Signature"),
            "Section 139(e) says a person subject to the professional tax must write the number of the "
            "official receipt issued to him in deeds, receipts, prescriptions, reports, books of account, "
            "plans and designs, surveys and maps, as the case may be.",
            ("point", "For the professional", "Keep the receipt number, date and place of issue where you "
             "can find them. Each year’s payment has its own receipt, so documents signed in January of a new "
             "year should carry the new one."),
            ("point", "For the reader", "A PTR number on a plan or report shows that the signer paid the "
             "professional tax for that year, and where. It may appear beside the signer’s "
             "license number."),
            ("point", "Not a license", "The PTR does not prove the person is licensed. The license itself "
             "comes from passing the government examination."),
            ("h", "Paying Late"),
            "Section 168 lets the sanggunian impose a surcharge of up to 25% on taxes not paid on time, "
            "and interest of up to 2% a month on the unpaid amount, including the surcharge, until paid. "
            "Total interest cannot run for more than 36 months. The exact rates are in the local revenue "
            "code, not in the Local Government Code itself.",
            "Here is an example. Suppose a province sets the tax at ₱300, with the highest surcharge and "
            "interest the law allows, and a professional pays four months after the January 31 deadline.",
            ("point", "Surcharge", "25% of ₱300 is ₱75, making ₱375."),
            ("point", "Interest", "2% of ₱375 is ₱7.50 a month. Over four months, that is ₱30."),
            ("point", "Total", "₱300 tax, ₱75 surcharge and ₱30 interest, or ₱405. How months are counted, "
             "and the actual rates, depend on the local ordinance."),
            "The amounts are small. The bigger cost is a plan, report or prescription signed without a "
            "valid receipt number when the law asks for one.",
            ("h", "For Treasury Workers"),
            ("point", "Know your ordinance", "Have the local revenue code’s rate, classes, surcharge and "
             "interest ready at the window, with a printed copy for taxpayers who ask."),
            ("point", "Ask about government employment", "A taxpayer who says “I work in government” may "
             "be exempt, but only if the work is exclusively in government. Ask, and note the answer."),
            ("point", "One receipt per profession", "A person practicing two professions needs the tax for "
             "each, under Section 139(d)."),
            ("point", "January planning", "With a January 31 deadline, the professional tax falls in "
             "the same month as the January rush described in Part 2."),
            ("h", "For Professionals"),
            ("point", "Pay before you practice", "If you start work after January, pay the full year before "
             "you sign anything."),
            ("point", "Pay in the right place", "Where you practice, or your principal office if you "
             "practice in several places."),
            ("point", "Write the number", "On every document the law lists, and update it each new year."),
            ("h", "Mistakes to Avoid"),
            ("point", "Confusing the license with the PTR", "The license lets you practice; the PTR is a yearly local tax."),
            ("point", "Assuming every government worker is exempt", "Only those exclusively employed in government."),
            ("point", "Waiting until next January", "A late starter pays before beginning to practice."),
            ("point", "Reusing last year’s number", "A new year means a new receipt."),
            ("h", "Key Takeaways"),
            ("point", "Up to ₱300 a year", "Set by the province or city, and capped by Section 139."),
            ("point", "Due January 31", "Or before practice begins, for those who start later."),
            ("point", "Paid once, valid nationwide", "For practicing that profession that year."),
            ("point", "The number goes on documents", "Plans, reports, prescriptions and the others in Section 139(e)."),
            ("h", "Your Part 21 Action Plan"),
            ("point", "If you are a professional", "Find this year’s receipt. Check that its number is on "
             "the documents you signed this year."),
            ("point", "If you employ professionals", "List each one with their PTR number and date, as "
             "Section 139(c) expects you to require the payment."),
            ("point", "If you work in a treasury", "Read the professional tax section of your local "
             "revenue code and confirm the rate, the classes and the late-payment charges."),
            "The engineer paid her professional tax that afternoon, wrote the receipt number under her "
            "signature on the plans, and gave the firm a copy. Next January, she will be the one reminding "
            "the new hires.",
            ("cta", "Read: Inside the Local Treasury, Part 20: Who Does What in the Treasurer’s Office", "/blog/inside-the-treasurers-office/"),
            ("cta", "Read: Inside the Local Treasury, Part 3: The Cedula, a Spanish-Era Tax That Never Left", "/blog/the-cedula-explained/"),
            ("cta", "Read: Inside the Local Treasury, Part 2: The January Rush and Your Business Permit", "/blog/january-rush-business-permit/"),
            ("cta", "Read: Inside the Local Treasury, Part 15: Fee or Tax? Why the Difference Matters", "/blog/fee-or-tax/"),
            ("ask", "If you are a licensed professional, did anyone explain the PTR to you before your first job?"),
        ],
    },
    {
        "title": "Inside the Local Treasury, Part 20: Who Does What in the Treasurer’s Office",
        "date": "March 25, 2027",
        "publish_on": "2027-03-25 21:00",  # blog rotation, one series a day (Butch 2026-11-14)
        "slug": "inside-the-treasurers-office",
        "category": "finance",
        "summary": "The treasurer’s office collects taxes, keeps the town’s money and pays its bills, but it "
                   "does not assess property, keep the books or prepare the budget. Here is what the Local "
                   "Government Code assigns to the treasurer, who supervises the office, and which office to "
                   "visit for what.",
        "body": [
            "A new employee on her first day at the town hall was given a simple task: deliver a taxpayer’s "
            "letter “to the treasury.” The letter asked why her property’s assessed value had gone up. The "
            "cashier read it, smiled, and sent her to another office down the hall. “We collect the tax,” he "
            "said, “but we don’t set the value.” By lunchtime she had visited three offices and learned more "
            "about local government than in her whole orientation.",
            "(The employee, the letter and the town hall are fictional, made up to explain the offices.)",
            "Part 19 looked at the public market as a business the town runs. This part steps back to look "
            "at the office that handles the town’s money. Read to the end, and you will know what the Local "
            "Government Code gives the treasurer to do, who appoints and supervises the treasurer, how the "
            "treasurer’s work differs from the assessor’s, the accountant’s and the budget officer’s, and "
            "which office a taxpayer should visit for which question.",
            ("photo", "blog/finance-office.jpg", "The treasurer’s office: advise on funds, keep custody, take "
             "charge of disbursements, inspect for tax compliance and keep the tax records. (Illustration: "
             "Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "What the Code Assigns to the Treasurer"),
            "Section 470 of the Local Government Code sets out the treasurer’s functions. In plain words, "
            "the treasurer:",
            ("point", "Advises on funds", "Advises the governor or mayor and the council on the disposition of local government funds."),
            ("point", "Keeps custody", "Takes custody of and properly manages the funds of the local "
             "government."),
            ("point", "Takes charge of disbursement", "Takes charge of the disbursement of local government "
             "funds, the last step of the payment process in Part 7."),
            ("point", "Inspects establishments", "Inspects private commercial and industrial establishments "
             "within the locality, in connection with the tax ordinances."),
            ("point", "Keeps the tax information", "Maintains and updates the local government’s tax "
             "information system."),
            ("point", "Administers oaths", "On notices to delinquent real property taxpayers, as in Part 5."),
            "The Code adds other duties as provided by law or ordinance. Much of this series, from the "
            "receipts in Part 11 to the deposits in Part 13, is these functions at work.",
            ("quote", "The treasurer keeps the money. Other offices decide the value, the budget and the "
             "books."),
            ("h", "Who Appoints and Who Supervises"),
            "Section 470 provides that the treasurer is appointed by the Secretary of Finance, from a list of at least three eligible recommendees of the governor or mayor. A House bill filed in the 19th Congress proposed moving the appointment to local chief executives. Its explanatory note describes the current arrangement: appointment by the Secretary of Finance, with the governor or mayor exercising administrative supervision. Until a change becomes law, the Code’s rule stands.",
            "So the appointment comes from the national Department of Finance, while the day-to-day supervision of the office sits with the local chief executive, to whom the treasurer reports on the work of the office.",
            ("h", "Four Offices, Four Jobs"),
            "The new employee’s morning makes sense once the offices are laid side by side.",
            ("point", "The assessor", "Appraises and assesses real property. A question about the assessed "
             "value of a lot goes here, not to the treasury."),
            ("point", "The treasurer", "Collects taxes, fees and charges, keeps the money, and pays out "
             "approved disbursements."),
            ("point", "The accountant", "Keeps the books, records every transaction in the accounts, and "
             "prepares the financial reports. The treasurer’s collections and deposits are recorded here."),
            ("point", "The budget officer", "Prepares the budget with the local chief executive and checks "
             "that funds are available for each expense."),
            "The separation builds in checks. The assessor sets a value the treasurer did not choose; the "
            "accountant records money the treasurer did not count alone; the budget officer confirms the "
            "funds the treasurer pays out. Part 7 followed a single payment through all of them.",
            ("h", "Inside the Treasury"),
            "Offices organize the treasurer’s work in different ways, depending on their size. One way an "
            "office might divide it:",
            ("point", "Collection", "The cashiers at the windows and the collectors in the field, issuing "
             "official receipts from accountable forms."),
            ("point", "Real property tax", "The records of each declared property, its payments and arrears, "
             "and the notices in Part 5."),
            ("point", "Business taxes and licenses", "The computations from gross sales declarations, done "
             "with the business permit process in Part 2."),
            ("point", "Cash and disbursement", "Deposits, bank accounts, checks and the cash book."),
            ("point", "Examination and inspection", "Visits to establishments and checks on declarations."),
            ("h", "The Records the Office Keeps"),
            "Much of the treasurer’s work leaves a paper trail that other offices and the auditors rely on. Earlier parts of this series described several of these records.",
            ("point", "Official receipts and accountable forms", "Issued, used and returned under the RAAF, as Part 11 explained."),
            ("point", "Collection and deposit records", "Each day’s collections and the deposits that match them, as in Part 13."),
            ("point", "Real property tax records", "Payments and arrears for each property, which feed the barangay shares in Part 17."),
            ("point", "Claims and protests", "The log of refund claims and protests with their deadlines, from Part 18."),
            "When COA audits the office, as Part 9 described, these are the records that show whether the money was handled as the rules require.",
            ("h", "Which Window for Which Question?"),
            ("point", "“How much do I owe?”", "The treasurer’s office, from its records."),
            ("point", "“Why did my assessed value go up?”", "The assessor’s office."),
            ("point", "“When will my supplier payment be released?”", "The treasurer’s office for the check, "
             "after the accountant and budget officer have processed the voucher."),
            ("point", "“Was my payment recorded?”", "The treasurer’s office first, with your official receipt "
             "in hand."),
            ("point", "“I paid too much.”", "A written claim to the local treasurer, as in Part 18."),
            ("h", "For New Treasury Workers"),
            ("point", "Learn the neighbors", "Know what the assessor, accountant and budget officer do, so you "
             "can send taxpayers to the right door the first time."),
            ("point", "Know your accountability", "If you handle cash or accountable forms, you answer for "
             "them, as Parts 11 and 12 showed."),
            ("point", "Ask before you answer", "If a question is outside the treasury’s work, say so and walk "
             "the taxpayer to the right office."),
            ("point", "Protect what you see", "Treasury records hold names, addresses, property and income details. Share them only as the office’s rules and the Data Privacy Act allow, and never discuss a taxpayer’s account with someone who is not entitled to it."),
            ("h", "Mistakes to Avoid"),
            ("point", "Arguing assessed values at the cashier’s window", "That is the assessor’s work."),
            ("point", "Assuming the mayor appoints the treasurer", "Under current law, the Secretary of "
             "Finance does."),
            ("point", "Treating the four offices as one", "Each checks the others."),
            ("point", "Leaving taxpayers to find the door", "Point them to the right office."),
            ("h", "Key Takeaways"),
            ("point", "Section 470 lists the duties", "Advise, keep custody, disburse, inspect, keep tax "
             "records."),
            ("point", "Appointed by the Secretary of Finance", "Under the mayor’s or governor’s "
             "administrative supervision."),
            ("point", "Four offices, four jobs", "Assessor values, treasurer collects and pays, accountant "
             "records, budget officer plans."),
            ("point", "Built-in checks", "No single office handles money from start to finish."),
            ("h", "Your Part 20 Action Plan"),
            ("point", "If you pay local taxes", "Before your next visit, write your question and decide "
             "which office it belongs to."),
            ("point", "If you are new to a treasury", "Visit the assessor, accountant and budget officer and "
             "ask each what they need from you."),
            ("point", "If you follow local government", "Find who your town’s treasurer is, and where the "
             "office posts its reports."),
            "The new employee delivered the letter to the assessor’s office just before noon. On her way "
            "back, she drew a small map of the four offices on the back of her orientation sheet. A week "
            "later, she was the one giving directions.",
            ("cta", "Read: Inside the Local Treasury, Part 19: The Public Market, a Business the Town Runs", "/blog/public-market-economic-enterprise/"),
            ("cta", "Read: Inside the Local Treasury, Part 7: From Budget to Check, How a Town Pays Its Bills", "/blog/from-budget-to-check/"),
            ("cta", "Read: Inside the Local Treasury, Part 1: Where Your Town's Money Comes From", "/blog/where-your-towns-money-comes-from/"),
            ("cta", "Read: Inside the Local Treasury, Part 12: The Surprise Cash Count, and What a Shortage Means", "/blog/cash-counts-and-shortages/"),
            ("ask", "Have you ever been sent from one town hall office to another? Which question was it?"),
        ],
    },
    {
        "title": "Inside the Local Treasury, Part 19: The Public Market, a Business the Town Runs",
        "date": "March 20, 2027",
        "publish_on": "2027-03-20 21:00",  # blog rotation, one series a day (Butch 2026-11-14)
        "slug": "public-market-economic-enterprise",
        "category": "finance",
        "summary": "Stall rentals, slaughterhouse fees and terminal charges come from businesses the town "
                   "itself runs. Here is what the law and the DBM’s manual call these enterprises, how their "
                   "money is kept separate, how to tell whether one pays for itself, and what happens to any "
                   "excess.",
        "body": [
            "A vendor who had sold vegetables in the public market for twenty years asked the market "
            "collector a question one morning. “I pay my stall rent every day. Where does it go? The roof "
            "still leaks over my stall.” The collector did not know. Neither did the vendors beside her. "
            "The answer starts with an idea that surprises some taxpayers: the public market is a business, "
            "and the town is its owner.",
            "(The vendor, the market and every number here are invented to explain the rules. No real "
            "market or person is described.)",
            "Part 18 looked at money the treasury must return. This part looks at money the town earns, not "
            "from taxes, but from running an enterprise. By the end, you will know what a local economic "
            "enterprise is, why its money is kept in a special account, how to measure whether it pays for "
            "itself, what happens to any excess, and what vendors, treasury staff and councils can each "
            "check.",
            ("photo", "blog/finance-market.jpg", "The public market as an economic enterprise: its own account, "
             "its own budget, a self-sufficiency ratio, and excess income that returns to the general fund. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "A Service and a Business"),
            "Section 17 of the Local Government Code lists public markets, slaughterhouses and other "
            "municipal enterprises among the basic services and facilities a municipality provides. The same "
            "section says costs may be charged for the delivery of these services.",
            "The Department of Budget and Management’s Manual on the Setting Up and Operation of Local "
            "Economic Enterprises, issued with Local Budget Circular No. 111 on June 10, 2016, describes "
            "these as ventures wholly or partially owned by local governments that earn income by selling "
            "goods and services.",
            ("point", "Public utilities", "The manual lists examples such as water supply, power, "
             "sanitation, and transport terminals, including bus and jeepney terminals, parking and piers."),
            ("point", "Other economic enterprises", "Public markets, slaughterhouses, cold storage, "
             "commercial spaces and local hospitals."),
            ("quote", "A market stall’s rent is not a tax. It is the price of a service the town sells."),
            ("h", "Where the Charges Come From"),
            "The Code gives local governments the power to charge for these services. Section 153 allows "
            "reasonable fees and charges for services rendered. Section 154 lets them fix the rates for "
            "public utilities they own and operate. Section 155 lets the council set toll fees for the use "
            "of public roads, piers or wharves. The amounts themselves are set in local ordinances, which is "
            "why stall rents and slaughter fees differ from town to town. Part 15 explained why a fee for a "
            "service follows different rules from a tax.",
            ("h", "Its Own Account"),
            "The manual cites Section 313 of the Code, which requires special accounts in the general fund "
            "for public utilities and other economic enterprises. It says each enterprise should have its own "
            "special account and its own annual operating budget.",
            ("point", "Income in", "Stall rentals, entrance fees, slaughter fees and similar collections for "
             "that enterprise."),
            ("point", "Costs out", "The manual counts personnel services, maintenance and other operating "
             "expenses, and finance charges as operating costs."),
            ("point", "Kept apart", "So the town can see whether the market earns its keep, instead of the "
             "figures disappearing into the general fund."),
            ("h", "Does It Pay for Itself?"),
            "The manual defines a simple test. An enterprise is self-sufficient if it recovers 100 percent of "
            "its operating costs. The self-sufficiency ratio is total income divided by total expenses, times "
            "100.",
            ("point", "Example", "A market earns ₱3,600,000 in a year from rentals and fees and spends "
             "₱4,500,000 to run. ₱3,600,000 ÷ ₱4,500,000 × 100 = 80 percent."),
            ("point", "What 80 percent means", "The market covered four-fifths of its costs. The other "
             "₱900,000 came from somewhere else, such as support from the general fund."),
            "Arrears change the picture. If the same market had ₱300,000 in unpaid stall rent and collected it, income would be ₱3,900,000, and the ratio would rise to about 86.7 percent, without raising a single rate. Before asking for a higher rent, a council can ask how much of the current rent is actually being collected.",
            "The manual describes transfers from the general fund to an enterprise as subsidies or "
            "advances. A subsidy is not wrong in itself; a town may decide the market is worth supporting. "
            "But it should be a decision, made with the number in view.",
            ("h", "Where Any Excess Goes"),
            "When an enterprise earns more than it spends, the manual, citing Section 313, sets an order. "
            "Income first covers improvement, repair and related costs of the enterprise. Next it repays "
            "advances from the general fund. Any excess then becomes part of the general fund of the local "
            "government.",
            "The manual also notes that, unlike a private corporation, an enterprise cannot keep its "
            "current-year earnings for itself. For the vendor’s question, this is the key: stall rent can pay "
            "for the market’s roof, but only if the repair is budgeted in the market’s account.",
            ("h", "Reviewing an Enterprise"),
            "The manual calls for a review every five years of whether each enterprise should continue. If "
            "an enterprise does not reach self-sufficiency, the local government may audit its facilities and "
            "then decide to continue it, restructure it or exit it.",
            ("h", "For Treasury Workers"),
            ("point", "Record collections by enterprise", "Each receipt for stall rent or slaughter fees should "
             "be coded to the right enterprise, so its income can be totaled."),
            ("point", "Track arrears by stall", "Unpaid rentals reduce the ratio as surely as higher costs. A "
             "list of overdue stalls, by amount and age, belongs in every monthly report."),
            ("point", "Deposit on time", "Market collections follow the same deposit rules as any other "
             "collection, as Part 13 explained."),
            ("point", "Use accountable forms", "Daily stall tickets or receipts are accountable forms, issued "
             "and returned as described in Part 11."),
            ("point", "Report the ratio", "Give the council the year-to-date income, expenses and self-sufficiency ratio of each enterprise every quarter, not only at budget time."),
            ("h", "For Vendors and Councils"),
            ("point", "Vendors", "Ask to see the market’s operating budget. Repairs you want should appear "
             "there."),
            ("point", "Councils", "Ask for the self-sufficiency ratio each year, and decide the subsidy "
             "openly."),
            ("point", "Everyone", "Compare this year’s ratio with last year’s. The direction says more than a "
             "single number."),
            ("h", "Mistakes to Avoid"),
            ("point", "Mixing market money into the general fund", "It needs its own special account."),
            ("point", "Ignoring rental arrears", "They lower income as much as a rate cut would."),
            ("point", "Hiding the subsidy", "Show it as a decision, with the ratio."),
            ("point", "Unbudgeted repairs", "If it is not in the enterprise budget, the rent cannot pay for it."),
            ("h", "Key Takeaways"),
            ("point", "The market is an enterprise", "Run by the town, with income from fees and rentals."),
            ("point", "Its own account and budget", "Under Section 313, as the DBM manual explains."),
            ("point", "Self-sufficiency ratio", "Income divided by expenses, times 100; 100 percent pays "
             "for itself."),
            ("point", "Excess has an order", "Repairs and improvements, then advances, then the general "
             "fund."),
            ("h", "Your Part 19 Action Plan"),
            ("point", "If you rent a stall", "Ask the market office what repairs are in this year’s budget."),
            ("point", "If you work in a treasury", "Total last year’s collections by enterprise, and set them "
             "beside the enterprise’s expenses."),
            ("point", "If you follow your council", "Look for the market subsidy in the budget and ask what "
             "ratio it supports."),
            "The collector carried the vendor’s question to the market supervisor, who showed her the "
            "market’s operating budget. The roof repair was there, scheduled before the rainy season. The "
            "vendor went back to her stall with a date, and, for the first time, a reason to keep her rent "
            "receipts in order.",
            ("cta", "Read: Inside the Local Treasury, Part 15: Fee or Tax? Why the Difference Matters", "/blog/fee-or-tax/"),
            ("cta", "Read: Inside the Local Treasury, Part 13: From the Cash Box to the Bank, Why Deposits Cannot Wait", "/blog/deposits-cash-box-to-bank/"),
            ("cta", "Read: Inside the Local Treasury, Part 11: The Blank Receipt Problem, Accountable Forms and the RAAF", "/blog/accountable-forms-blank-receipts/"),
            ("cta", "Read: Inside the Local Treasury, Part 18: Paid Too Much? Refunds, Tax Credits and Protests", "/blog/local-tax-refunds-and-credits/"),
            ("ask", "Does your town’s public market pay for itself? Have you ever seen its budget?"),
        ],
    },
    {
        "title": "Inside the Local Treasury, Part 18: Paid Too Much? Refunds, Tax Credits and Protests",
        "date": "March 15, 2027",
        "publish_on": "2027-03-15 21:00",  # blog rotation, one series a day (Butch 2026-11-14)
        "slug": "local-tax-refunds-and-credits",
        "category": "finance",
        "summary": "Local taxes can be paid in error, or assessed wrongly. The Local Government Code gives "
                   "taxpayers written remedies with firm deadlines: a claim for refund or credit, a protest "
                   "of assessment, and payment under protest for real property tax. Here is how each works.",
        "body": [
            "In February, a hardware store owner sat down with her accountant to close the books and found "
            "a problem. The business tax she paid in January had been computed on the wrong gross sales "
            "figure, a number from another store’s declaration typed into her record. She had paid ₱6,000 "
            "more than she owed. Her first question was whether the money was gone. Her second was how to "
            "ask for it back.",
            "(The store owner, the figures and the mix-up are illustrations, not a real case.)",
            "Part 17 followed money from the town to its barangays. This part follows money back to the "
            "taxpayer. It explains what the law calls an erroneous or illegal collection, the difference "
            "between a refund and a tax credit, how to file a claim and by when, how a protest of assessment "
            "differs from a refund claim, and the separate rules for real property tax.",
            ("photo", "blog/finance-refund.jpg", "Refunds, tax credits and protests: put it in writing, file "
             "within the deadline, and keep the receipt. (Illustration: Butch Mahinay, aumahinay.dev)",
             "medium"),
            ("h", "Erroneous or Illegal Collection"),
            "Section 196 of the Local Government Code speaks of any tax, fee or charge erroneously or "
            "illegally collected. Two kinds of cases fit.",
            ("point", "Erroneous", "The tax is valid, but the amount was wrong: a typing error, a wrong "
             "rate applied, or a payment made twice."),
            ("point", "Illegal", "The tax itself should not have been collected, for example a charge with "
             "no valid basis in an ordinance, as Part 15 discussed."),
            ("quote", "A refund starts with a letter, not with an argument at the window."),
            ("h", "Refund or Credit"),
            ("point", "A refund", "The amount is paid back to the taxpayer."),
            ("point", "A tax credit", "The amount is applied against the taxpayer’s current or future tax, "
             "so the next payment is smaller."),
            "Section 196 covers both and asks for a written claim for refund or credit. For a business that "
            "will pay again next quarter, a credit can be the simpler result. A taxpayer who has closed the "
            "business, as in Part 14, would ask for a refund.",
            ("h", "Step 1: File a Written Claim, Early"),
            "Section 196 sets two rules. First, no case can be brought in court to recover a tax, fee or "
            "charge erroneously or illegally collected until a written claim for refund or credit has been "
            "filed with the local treasurer. Second, no court case is allowed after two years from the date "
            "of payment, or from the date the taxpayer became entitled to a refund or credit. Because the claim must come before any court case, and any case must be filed within those two years, file the claim early.",
            ("point", "Write to the local treasurer", "A short letter: who you are, what you paid, when, "
             "why it was wrong, and whether you ask for a refund or a credit."),
            ("point", "Attach the proof", "A copy of the official receipt, the assessment or computation, "
             "and the document that shows the right figure, such as the correct sales declaration."),
            ("point", "Get it received", "Ask for a received stamp with the date on your copy. That date is "
             "your evidence that you filed in time."),
            "For the store owner, the payment was made on January 15. Two years from that date is January "
            "15, 2029. She filed in February, with almost all of that time still ahead of her, which is "
            "the safer way to use a deadline.",
            ("h", "A Protest Is Different"),
            "A refund claim is for money already paid. A protest of assessment, under Section 195, is for a "
            "notice of assessment that says you owe more.",
            ("point", "The notice", "When the treasurer finds that the correct tax was not paid, the law "
             "requires a notice of assessment stating the tax, the deficiency, and the surcharges, interest "
             "and penalties."),
            ("point", "Sixty days to protest", "The taxpayer may file a written protest within 60 days from "
             "receipt of the notice. Otherwise the assessment becomes final and executory."),
            ("point", "Sixty days to decide", "The treasurer must decide the protest within 60 days from "
             "filing, canceling the assessment wholly or partly, or denying it wholly or partly."),
            ("point", "Thirty days to appeal", "From receipt of the denial, or from the end of the 60-day "
             "period without a decision, the taxpayer has 30 days to appeal to the proper court. Otherwise "
             "the assessment becomes conclusive and unappealable."),
            ("h", "Real Property Tax: Pay First, Then Protest"),
            "Real property tax has its own rules in the part of the Code on real property taxation.",
            ("point", "Pay first", "Section 252 says no protest is entertained unless the taxpayer first pays "
             "the tax, and the receipt is marked “paid under protest.”"),
            ("point", "Protest within 30 days", "The written protest goes to the provincial or city "
             "treasurer, or the municipal treasurer within Metropolitan Manila, within 30 days from "
             "payment."),
            ("point", "Held in trust", "The amount paid under protest is held in trust by the treasurer, and "
             "the treasurer decides within 60 days of receiving the protest."),
            ("point", "If the taxpayer wins", "The amount is refunded or applied as a credit against current "
             "or future real property tax."),
            "Section 253 adds a separate claim for repayment when a real property tax is found illegal or "
            "erroneous and is reduced or adjusted. The taxpayer files a written claim with the provincial or "
            "city treasurer within two years from the date the taxpayer is entitled to the reduction, and "
            "the treasurer decides within 60 days.",
            ("h", "For Treasury Workers"),
            ("point", "Keep a claims log", "Date received, taxpayer, amount, type of claim, deadline to "
             "decide, decision and date released."),
            ("point", "Check the computation, not the person", "Recompute from the documents. If the error is "
             "the office’s, say so in the reply."),
            ("point", "Decide in writing, on time", "The 60-day periods in Sections 195, 252 and 253 run "
             "whether or not anyone remembers them."),
            ("point", "Record credits where the cashier will see them", "A credit that is not on the "
             "taxpayer’s record at the next payment is a promise that will be broken."),
            "A cash refund is money leaving the treasury, so it follows the payment steps described in Part 7, "
            "with the claim, the decision and the receipts as supporting documents.",
            ("h", "For Taxpayers"),
            ("point", "Read the computation before paying", "An error caught at the window can be fixed before it becomes a claim."),
            ("point", "Keep every receipt", "A claim without the receipt is hard to prove."),
            ("point", "Watch the dates", "Thirty days, sixty days and two years are different deadlines for "
             "different remedies."),
            ("h", "Mistakes to Avoid"),
            ("point", "Asking only at the window", "Without a written claim, there is no claim."),
            ("point", "Missing the two-year limit", "File early, and keep the received copy."),
            ("point", "Confusing a protest with a refund", "One answers an assessment; the other recovers a "
             "payment."),
            ("point", "Forgetting to apply a credit", "Mark it on the taxpayer’s record right away."),
            ("h", "Key Takeaways"),
            ("point", "Written claim first", "Section 196 requires it before any court case."),
            ("point", "Two years", "From payment, or from the date of entitlement."),
            ("point", "Protest of assessment", "Sixty days to protest, sixty to decide, thirty to appeal."),
            ("point", "Real property tax", "Pay under protest, protest within 30 days, decision in 60."),
            ("h", "Your Part 18 Action Plan"),
            ("point", "If you pay local taxes", "Check your last receipt against your declaration. If they "
             "differ, write to the treasurer this month."),
            ("point", "If you work in a treasury", "Start a claims log with a column for the decision "
             "deadline."),
            ("point", "If you own property", "Learn the words “paid under protest” before you need them."),
            "The store owner’s letter was received on a Tuesday. The treasurer’s office rechecked the "
            "declaration, found the typed figure, and wrote back within the month: ₱6,000 would be credited "
            "to her next quarterly payment. In April, her receipt showed the credit, and the amount due was "
            "₱6,000 smaller.",
            ("cta", "Read: Inside the Local Treasury, Part 15: Fee or Tax? Why the Difference Matters", "/blog/fee-or-tax/"),
            ("cta", "Read: Inside the Local Treasury, Part 7: From Budget to Check, How a Town Pays Its Bills", "/blog/from-budget-to-check/"),
            ("cta", "Read: Inside the Local Treasury, Part 2: The January Rush and Your Business Permit", "/blog/january-rush-business-permit/"),
            ("cta", "Read: Inside the Local Treasury, Part 17: The Barangay’s Share of the Amilyar, and When It Must Arrive", "/blog/barangay-share-of-real-property-tax/"),
            ("ask", "Have you ever paid a local tax twice or by mistake? How did you get it back?"),
        ],
    },
    {
        "title": "Inside the Local Treasury, Part 17: The Barangay’s Share of the Amilyar, and When It Must Arrive",
        "date": "March 10, 2027",
        "publish_on": "2027-03-10 21:00",  # blog rotation, one series a day (Butch 2026-11-14)
        "slug": "barangay-share-of-real-property-tax",
        "category": "finance",
        "summary": "Part of every basic real property tax payment belongs to the barangay where the property "
                   "stands. Here is how the Local Government Code splits the tax, how the share is computed, "
                   "when it must be released, and why a missing report can hold back millions.",
        "body": [
            "The barangay treasurer arrived at the municipal treasury with a folder and a calculator. Her "
            "barangay council was preparing its budget, and the captain had asked a simple question: how "
            "much of the amilyar paid in their barangay last quarter would come back to them, and when? "
            "The answer, it turned out, was written in one section of the law. Getting the number right "
            "took a report that showed every payment by barangay.",
            "(The treasurer, her barangay and the figures in this story are invented. A real case, reported "
            "in the news, appears later and is named as such.)",
            "Part 16 followed the Special Education Fund to the schools. This part follows the other half "
            "of the real property tax receipt, the basic tax, as it is shared out. You will learn how "
            "Section 271 of the Local Government Code divides it, how to compute a barangay’s share, when "
            "the share must be released, what a recent audit found when it was not, and what treasurers and "
            "barangay officials can each check.",
            ("photo", "blog/finance-brgy-share.jpg", "The barangay share of real property tax: split by "
             "law, computed by location, released every quarter, free of any holdback. (Illustration: Butch "
             "Mahinay, aumahinay.dev)", "medium"),
            ("h", "What Is Shared"),
            "Section 271 covers the proceeds of the basic real property tax, including the interest on it, "
            "and the proceeds from the use, lease, disposition, sale or redemption of property acquired at a public auction under the real property tax rules, the last step described in Part 5.",
            "The Special Education Fund is not part of this split. As Part 16 explained, Section 235 says "
            "the additional one percent tax accrues exclusively to the SEF.",
            ("quote", "The barangay’s share is not a gift from the town hall. It is set by law."),
            ("h", "The Split, by Type of Local Government"),
            ("point", "In a province", "35 percent to the province’s general fund, 40 percent to the "
             "general fund of the municipality where the property is located, and 25 percent to the "
             "barangay where the property is located."),
            ("point", "In a city", "70 percent to the city’s general fund and 30 percent to its barangays. "
             "Half of that 30 percent goes to the barangay where the property is located, and the other "
             "half is divided equally among all the city’s barangays."),
            ("point", "In a Metro Manila municipality", "35 percent to the Metropolitan Manila Authority, "
             "35 percent to the municipality’s general fund, and 30 percent to the barangays, shared the "
             "same way as in a city."),
            ("h", "Worked Example: A Municipality in a Province"),
            "Say a municipality collects ₱1,200,000 in basic real property tax and interest in one quarter.",
            ("point", "Province, 35 percent", "₱420,000."),
            ("point", "Municipality, 40 percent", "₱480,000."),
            ("point", "Barangays, 25 percent", "₱300,000 in all, but not divided equally. Each barangay "
             "gets 25 percent of what was paid on property located in it."),
            "If property in Poblacion paid ₱500,000, San Isidro ₱400,000 and San Roque ₱300,000, the shares "
            "are ₱125,000, ₱100,000 and ₱75,000. Together they make ₱300,000, and the three parts add back "
            "up to ₱1,200,000.",
            ("h", "Worked Example: A City"),
            "Say a city with ten barangays collects ₱6,000,000 in one quarter.",
            ("point", "City, 70 percent", "₱4,200,000."),
            ("point", "Barangays, 30 percent", "₱1,800,000, split in two halves of ₱900,000."),
            ("point", "Location half", "Each barangay gets 15 percent, half of 30, of what was paid on "
             "property in it. A barangay whose properties paid ₱1,000,000 gets ₱150,000."),
            ("point", "Equal half", "₱900,000 divided by ten barangays is ₱90,000 each."),
            "That barangay’s total for the quarter is ₱150,000 plus ₱90,000, or ₱240,000.",
            ("h", "When the Share Must Arrive"),
            "Section 271 is specific about timing. The share of each barangay is released, without need of "
            "any further action, directly to the barangay treasurer, every quarter, within five days after "
            "the end of the quarter. The law adds that the share is not subject to any lien or holdback for "
            "whatever purpose.",
            ("point", "No request needed", "The barangay does not have to apply or follow up for its share."),
            ("point", "Directly to the barangay treasurer", "Not through another office, and not held as "
             "a credit against something else."),
            ("point", "Five days after the quarter", "For January to March, that is by April 5."),
            ("h", "A Real Case: When the Report Is Missing"),
            "In July 2026, SunStar Cebu reported on the Commission on Audit’s 2025 audit report on Cebu "
            "City. According to the report, the city had not distributed ₱280.75 million in barangay shares "
            "of advance real property tax collections for 2020 to 2025, owed to its 80 barangays.",
            ("point", "What COA found", "The amounts sat in a deferred real property tax account instead of "
             "being recorded as owed to the barangays, which COA said violated Section 271."),
            ("point", "Why, according to the city", "Its tax software could not produce the detailed reports "
             "needed to compute each barangay’s share, and monthly reports did not match the accounting "
             "records."),
            ("point", "What COA recommended", "Finish the reconciliation within a firm timeframe, set a "
             "distribution schedule, record the amounts as liabilities, and resume quarterly releases."),
            "The lesson for any treasury is in the city’s explanation. The share depends on knowing where "
            "each paid property is located. If the collection records cannot be sorted by barangay, the law "
            "is clear but the number cannot be computed.",
            ("h", "For Treasury Workers"),
            ("point", "Record the barangay on every payment", "Each receipt and each collection report "
             "should carry the property’s barangay, taken from the tax declaration."),
            ("point", "Separate basic tax, interest and SEF", "Only basic tax, its interest and proceeds from auctioned property go into the split."),
            ("point", "Run the report before the quarter closes", "A total by barangay, reconciled with "
             "accounting, ready by the first day of the new quarter."),
            ("point", "Watch advance payments", "Payments made ahead for a future year still have a barangay "
             "share. Record it as owed, as COA advised, so it is not forgotten."),
            "Section 247 also lets the city or municipal treasurer deputize a barangay treasurer, if "
            "properly bonded, to collect real property tax on property located in the barangay. That "
            "changes who issues the receipt, but not the shares.",
            ("h", "For Barangay Officials"),
            ("point", "Ask for the computation", "Not only the amount, but the barangay’s collections it was "
             "based on."),
            ("point", "Check the calendar", "Note the date each quarterly share arrives, and ask if one is "
             "late."),
            ("point", "Put it in the budget carefully", "The share follows actual collections, so it moves "
             "from quarter to quarter."),
            ("h", "Mistakes to Avoid"),
            ("point", "Dividing equally in a province", "There, each barangay’s 25 percent follows its own "
             "collections."),
            ("point", "Including the SEF in the split", "It goes entirely to the SEF."),
            ("point", "Holding the share against a debt", "The law forbids any lien or holdback."),
            ("point", "Collecting without recording the barangay", "Then the share cannot be computed."),
            ("h", "Key Takeaways"),
            ("point", "Set by Section 271", "25 percent in a province, 30 percent in a city."),
            ("point", "Computed by location", "From what was paid on property in each barangay."),
            ("point", "Released every quarter", "Within five days, directly to the barangay treasurer."),
            ("point", "No holdback", "The share cannot be held for any purpose."),
            ("h", "Your Part 17 Action Plan"),
            ("point", "If you work in a treasury", "Check whether last quarter’s collection report can be "
             "sorted by barangay without retyping anything."),
            ("point", "If you serve in a barangay", "Ask for last quarter’s computation and the date the "
             "share was released."),
            ("point", "If you pay amilyar", "Look at the barangay printed on your tax declaration. That is "
             "where a part of your payment goes."),
            "The barangay treasurer left with a one-page computation and a date. The captain read it at the "
            "next session: their share for the quarter, the collections it came from, and the day it would "
            "arrive. For the first time, the line in their budget had a number behind it.",
            ("cta", "Read: Inside the Local Treasury, Part 16: The Special Education Fund, the School Money in Your Amilyar", "/blog/special-education-fund/"),
            ("cta", "Read: Inside the Local Treasury, Part 5: Unpaid Amilyar, From Notice to Auction", "/blog/unpaid-amilyar-notice-to-auction/"),
            ("cta", "Read: Inside the Local Treasury, Part 1: Where Your Town's Money Comes From", "/blog/where-your-towns-money-comes-from/"),
            ("cta", "Read the study note: Real property tax basics", "/study-notes/real-property-tax-basics/"),
            ("ask", "Does your barangay know how much of last quarter’s amilyar came back to it?"),
        ],
    },
    {
        "title": "Inside the Local Treasury, Part 16: The Special Education Fund, the School Money in Your Amilyar",
        "date": "March 5, 2027",
        "publish_on": "2027-03-05 21:00",  # blog rotation, one series a day (Butch 2026-11-14)
        "slug": "special-education-fund",
        "category": "finance",
        "summary": "Part of every real property tax payment goes to local public schools. Here is where the "
                   "Special Education Fund comes from, how it is shared, who decides how it is spent, what it "
                   "may pay for under the 2025 omnibus guidelines, and how you can see where it went.",
        "body": [
            "A father paying his real property tax looked closely at the official receipt for the first "
            "time. There were two amounts: one for the basic tax, and a second, labeled SEF. He asked the collector what the second one was. “Special Education Fund,” the collector said. “That part goes to the "
            "public schools.” He thought of his daughter’s classroom, the one with the leaking roof, and "
            "asked the next question: who decides what that money is spent on?",
            "(The story is made up for teaching, and so are its office, people and figures.)",
            "The Special Education Fund, or SEF, is a local fund that the law ties to a single purpose: public education. After this post, you will know where the SEF comes from, how it is "
            "collected and shared, who decides how it is spent, what it may pay for under the current "
            "guidelines, and where to look to see how your town used it.",
            ("photo", "blog/finance-sef.jpg", "The Special Education Fund: 1 percent on real property, "
             "released to the local school board, spent on public schools, and reported to the public. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Where the SEF Comes From"),
            "Section 235 of the Local Government Code allows a province or city, or a municipality within "
            "Metropolitan Manila, to levy and collect an annual tax of one percent on the assessed value of "
            "real property, in addition to the basic real property tax. The law says the proceeds accrue "
            "exclusively to the Special Education Fund.",
            "The SEF itself is older than the Code. It was created by Republic Act No. 5447, which the 2025 "
            "guidelines list among their legal bases.",
            ("quote", "Every amilyar receipt carries a small payment toward a classroom."),
            ("h", "How It Is Collected"),
            "The SEF tax is paid together with the basic real property tax, on the same schedule and with "
            "the same incentives.",
            ("point", "Notice by January 31", "Section 249 requires the city or municipal treasurer to post "
             "and publish, by January 31, the dates when the basic tax and the SEF tax may be paid without "
             "interest."),
            ("point", "Four installments", "Under Section 250, both may be paid without interest in four "
             "equal installments, due by March 31, June 30, September 30 and December 31."),
            ("point", "Discount for paying early", "Section 251 allows the sanggunian to grant a discount "
             "of up to 20 percent of the annual tax for advance payment of the basic and SEF taxes."),
            "Here is a simple example. A house and lot with an assessed value of ₱200,000 owes an SEF tax "
            "of 1 percent, or ₱2,000 a year, on top of the basic tax. Paid in four installments, that is "
            "₱500 a quarter for the schools.",
            ("h", "How It Is Shared"),
            "The newest rules are in DepEd, DBM, DILG and DOF Joint Circular No. 01, series of 2025, the "
            "Omnibus Guidelines on the Use of the Special Education Fund. It revises the earlier joint "
            "circulars of 2017 and 2020.",
            ("point", "Released to the school boards", "SEF proceeds are automatically released to the "
             "local school boards."),
            ("point", "Provinces share with municipalities", "Collections in a province are shared equally "
             "by the province and the municipalities within it."),
            ("point", "Cities keep their own", "A city keeps all of its SEF collections."),
            "So if you live in a municipality within a province, the SEF you pay is split between two "
            "school boards: the one in your town and the one at the provincial capitol. Both answer for "
            "how their share is used.",
            ("h", "Who Decides How It Is Spent"),
            "The local school board decides. Under the guidelines, the school board budget is prepared by "
            "the schools division superintendent, city superintendent or district supervisor, supported by "
            "the board’s programs, projects and activities. The SEF budget is approved through a local "
            "school board resolution signed by the chair and co-chair and approved by a majority of all "
            "members. The guidelines also widen the board’s membership to include, among others, "
            "implementers of the Alternative Learning System and parents of children with disabilities.",
            "The local treasurer’s role is to collect and keep the money, release it according to the "
            "approved budget, and keep its accounts separate from the General Fund. Under the guidelines, "
            "the treasurer, the budget officer and the accountant each receive a copy of the approved SEF "
            "budget within seven days of its approval.",
            ("h", "What the SEF May Pay For"),
            "The 2025 guidelines list allowable expenses. Among them:",
            ("point", "Operation and maintenance of public schools", "Including utilities and certain school "
             "health costs."),
            ("point", "School buildings and facilities", "Construction and repair."),
            ("point", "Equipment", "Including information and communication technology, following DepEd "
             "specifications."),
            ("point", "Early childhood and feeding programs", "Support for early childhood care and "
             "development, and for the National Feeding Program."),
            ("point", "Alternative and inclusive learning", "The Alternative Learning System, and support "
             "services for learners with disabilities."),
            ("point", "Books, research and sports", "Library books and periodicals, educational research "
             "and sports development."),
            "There is an important condition. Only items that are not adequately funded by DepEd or other "
            "national agencies may be charged to the SEF. The fund fills gaps; it does not replace the "
            "national budget for schools.",
            ("h", "How the Public Can See It"),
            "The guidelines require a detailed report on how the SEF was used to be posted on the local "
            "government’s website, in at least three conspicuous public places, or both, under the DILG’s "
            "Full Disclosure Policy. Part 10 of this series explained where to find these postings. The "
            "guidelines also require quarterly and year-end SEF reports to the Bureau of Local Government "
            "Finance: the first three quarterly reports by the 15th day of the month after each quarter, "
            "and the year-end report by February 28.",
            ("h", "Important Dates in the SEF Year"),
            ("point", "January 31", "Treasurer’s notice of the real property tax and SEF payment dates."),
            ("point", "Quarterly", "Installments due by March 31, June 30, September 30 and December 31, "
             "and quarterly reports to the Bureau of Local Government Finance."),
            ("point", "October 31", "Deadline for the local school board to approve the SEF budget for the "
             "coming year."),
            ("point", "February 28", "Year-end SEF report due."),
            ("h", "For Treasury Workers"),
            "Record the basic tax and the SEF tax separately on every receipt and in every report, and "
            "deposit them to the right accounts. A peso of SEF collected but recorded as basic tax ends up "
            "in the wrong fund. When the school board asks how much it has to work with, the treasury’s "
            "figures should be ready and match the bank.",
            ("h", "Mistakes to Avoid"),
            ("point", "Mixing SEF with the General Fund", "The SEF is a special fund, with its own accounts."),
            ("point", "Spending on items already funded by DepEd", "The SEF fills gaps only."),
            ("point", "Skipping the public posting", "The utilization report must be posted."),
            ("point", "Assuming residents cannot ask", "The reports are public, and residents can read "
             "them."),
            ("h", "Key Takeaways"),
            ("point", "One percent for schools", "An additional tax on assessed value (Section 235)."),
            ("point", "Paid with the amilyar", "Same installments, same early-payment discount."),
            ("point", "The local school board decides", "Under Joint Circular No. 01, series of 2025."),
            ("point", "Posted for the public", "Under the Full Disclosure Policy."),
            ("h", "Your Part 16 Action Plan"),
            ("point", "If you own property", "Look at your last real property tax receipt and find the SEF "
             "line."),
            ("point", "If you are a parent", "Ask your school head what the local school board funded for "
             "your school this year."),
            ("point", "If you work in a treasury", "Check that SEF and basic tax collections go to separate "
             "accounts, every day."),
            "The father asked the collector who sat on the school board. She told him which office at the town hall handles the school board’s papers and showed him where the town posts its SEF reports. That evening he "
            "found the report, and on it, a line for the repair of school roofs. His daughter’s school was "
            "on the list, scheduled for the summer break.",
            ("cta", "Read the study note: Real property tax basics", "/study-notes/real-property-tax-basics/"),
            ("cta", "Read: Inside the Local Treasury, Part 5: Unpaid Amilyar, From Notice to Auction", "/blog/unpaid-amilyar-notice-to-auction/"),
            ("cta", "Read: Inside the Local Treasury, Part 10: Where to See How Your Town Spends", "/blog/where-to-see-how-your-town-spends/"),
            ("cta", "Read: Inside the Local Treasury, Part 13: From the Cash Box to the Bank, Why Deposits Cannot Wait", "/blog/deposits-cash-box-to-bank/"),
            ("ask", "Have you ever seen how your town’s school board spends the SEF? What would you want it to fund?"),
        ],
    },
    {
        "title": "Inside the Local Treasury, Part 15: Fee or Tax? Why the Difference Matters",
        "date": "February 28, 2027",
        "publish_on": "2027-02-28 21:00",  # blog rotation, one series a day (Butch 2026-11-14)
        "slug": "fee-or-tax",
        "category": "finance",
        "summary": "A fee and a tax both come out of your pocket, but the law treats them differently. Here "
                   "is what the Local Government Code says about each, the test the Supreme Court uses to "
                   "tell them apart, the limits on both, and what you can do if a charge seems wrong.",
        "body": [
            "A woman opening a small eatery looked at her assessment from the town hall and frowned. There "
            "was the business tax, which she expected. Below it were a mayor’s permit fee, a sanitary "
            "inspection fee, a garbage fee and a fee for her signboard. “These are all just taxes with "
            "different names,” she told the clerk. The clerk smiled. “Not quite,” the clerk said, “and the "
            "difference is written in the law.”",
            "(This is a teaching case: the office, its staff and its figures are fictional.)",
            "To the person paying, a peso is a peso. To the law, a fee and a tax are different things, with "
            "different purposes and different limits. When you finish reading, you will know how the Local "
            "Government Code defines fees and charges, the test the Supreme Court uses to tell a fee from a "
            "tax, the limits that apply to each, how these charges are created, and what a taxpayer can do "
            "when one seems wrong.",
            ("photo", "blog/finance-fee-or-tax.jpg", "Fee or tax: a fee pays for regulation or a service, a "
             "tax raises revenue, and both need an ordinance and an official receipt. (Illustration: Butch "
             "Mahinay, aumahinay.dev)", "medium"),
            ("h", "What the Code Says"),
            "Section 131 of the Local Government Code defines the terms used in local taxation. Two of them "
            "matter here.",
            ("point", "Fee", "A charge fixed by law or ordinance for the regulation or inspection of a "
             "business or activity."),
            ("point", "Charges", "Pecuniary liability, such as rents or fees, against persons or property."),
            "A tax, by contrast, is imposed mainly to raise revenue for the government’s general needs. The "
            "business tax and the real property tax are examples. The money goes into the treasury to fund "
            "public services in general, not to pay for one particular service to the person who paid.",
            ("quote", "A tax pays for government. A fee pays for a specific job government does."),
            ("h", "The Supreme Court’s Test: What Is the Main Purpose?"),
            "In Progressive Development Corporation v. Quezon City, decided on April 24, 1989, the Supreme "
            "Court looked at a 5 percent charge on the gross receipts from stall rentals in a privately owned "
            "public market. The owner argued that it was a tax on income. The Court disagreed.",
            "The Court explained that if generating revenue is the primary purpose and regulation is merely "
            "incidental, the charge is a tax. If regulation is the primary purpose, the charge does not "
            "become a tax just because it also brings in money. The Court held that the 5 percent charge was "
            "a license fee for regulating the market, imposed under the city’s police power, and upheld it.",
            "So the label on a charge does not decide what it is. Its main purpose does.",
            ("h", "Who Can Create a Tax or a Fee"),
            "Section 132 gives the power to impose taxes, fees and charges to the sanggunian of the local "
            "government, exercised through an ordinance. A treasurer, a mayor or a department head cannot "
            "create a new charge on their own. If there is no ordinance, there is no basis to collect.",
            ("h", "The Limits on Fees"),
            "For fees that municipalities impose on businesses and occupations, Section 147 allows reasonable fees commensurate with "
            "the cost of regulation, inspection and licensing. In plain words, a regulatory fee should be "
            "in proportion to what it costs the town to inspect, regulate and license.",
            ("point", "Reasonable", "Not out of proportion to the work done."),
            ("point", "Tied to a purpose", "Inspection, regulation or a service, such as garbage "
             "collection."),
            ("point", "Set by ordinance", "With the amount written down, not decided at the window."),
            ("h", "The Limits on New Taxes and Charges"),
            "Section 186 lets a local government levy taxes, fees or charges on bases not already listed in "
            "the Code, but only if they are not unjust, excessive, oppressive, confiscatory or contrary to "
            "declared national policy, and only after a public hearing.",
            ("h", "Public Hearings Come First"),
            "Section 187 requires public hearings before any tax ordinance is enacted. This is where "
            "residents and business owners can speak for or against a proposed charge, and where a town "
            "should explain what each fee pays for.",
            "If you think an ordinance is illegal or unconstitutional, Section 187 also gives a remedy. You "
            "may appeal to the Secretary of Justice within thirty days from the ordinance’s effectivity, and "
            "the Secretary must decide within sixty days of receiving the appeal. The appeal does not stop "
            "the ordinance from taking effect, and it does not stop collection while the appeal is pending.",
            ("h", "Why the Difference Matters"),
            ("point", "To the taxpayer", "A fee should be explainable: you can ask what the inspection or "
             "the service involves and why it costs what it costs."),
            ("point", "To the town", "A regulatory fee that is far higher than the cost of regulation can be questioned as a tax in disguise."),
            ("point", "To the treasury", "Fees and taxes are recorded under different accounts, and some "
             "fees support a specific service. Knowing which is which keeps the books and the reports "
             "correct."),
            ("h", "Reading Your Assessment"),
            "On an assessment for a business permit, you will see two kinds of lines. The first is "
            "the business tax, computed from gross sales or receipts. The second is a group of regulatory "
            "fees and service charges, such as the mayor’s permit fee, sanitary and other inspection fees, "
            "garbage fees and signboard fees. Each line should trace back to an ordinance. If you want to "
            "see the basis, ask the treasurer’s office which ordinance and which section sets it. That is a "
            "fair question, and it deserves a clear answer.",
            ("h", "Every Peso Gets an Official Receipt"),
            "Whether it is a tax, a fee or a charge, every payment to the treasury gets an official receipt. "
            "Part 11 explained why that receipt matters. A fee paid without one is a fee the treasury may "
            "never see.",
            ("h", "For Treasury Workers"),
            "Keep a copy of the tax ordinance and the schedule of fees at the window, and know the section "
            "number for each line on an assessment. When a fee has not been reviewed in years, raise it "
            "with the office head so the sanggunian can check whether it still matches the cost of the "
            "service. And when a taxpayer asks for the legal basis of a charge, treat it as a fair "
            "question, not as a complaint.",
            ("h", "Mistakes to Avoid"),
            ("point", "Assuming every charge is a tax", "Some are fees for regulation or services, with "
             "different rules."),
            ("point", "Collecting a charge with no ordinance", "No ordinance, no basis to collect."),
            ("point", "Setting fees far above cost", "Fees should be commensurate with the cost of "
             "regulation."),
            ("point", "Missing the 30-day appeal window", "Challenges to an ordinance have a deadline."),
            ("h", "Key Takeaways"),
            ("point", "Purpose decides", "Revenue first means a tax; regulation first means a fee."),
            ("point", "Only an ordinance can create either", "Through the sanggunian (Section 132)."),
            ("point", "Fees follow cost", "Commensurate with the cost of regulation, inspection and "
             "licensing (Section 147)."),
            ("point", "Public hearings and appeals exist", "Speak up before enactment, or appeal within 30 "
             "days (Section 187)."),
            ("h", "Your Part 15 Action Plan"),
            ("point", "If you run a business", "Look at your last assessment and sort each line into tax "
             "or fee."),
            ("point", "If you work in a treasury", "Check that every line on your assessment form names its "
             "ordinance and section."),
            ("point", "If you care about your town", "Watch for notices of public hearings on tax "
             "ordinances, and attend one."),
            "The eatery owner asked the clerk which ordinance set the signboard fee. The clerk found it in "
            "the town’s revenue code and showed her the section, the amount and what it covered. The owner "
            "paid, kept her receipts and, a few months later, attended her first public hearing on a "
            "proposed change to the fee schedule.",
            ("cta", "Read the study note: Fees and charges", "/study-notes/fees-and-charges/"),
            ("cta", "Read: Inside the Local Treasury, Part 2: The January Rush and Your Business Permit", "/blog/january-rush-business-permit/"),
            ("cta", "Read: Inside the Local Treasury, Part 11: The Blank Receipt Problem, Accountable Forms and the RAAF", "/blog/accountable-forms-blank-receipts/"),
            ("cta", "Read: Inside the Local Treasury, Part 14: Closing a Business the Right Way", "/blog/closing-a-business-the-right-way/"),
            ("ask", "Which line on your business permit assessment have you wondered about?"),
        ],
    },
    {
        "title": "Inside the Local Treasury, Part 14: Closing a Business the Right Way",
        "date": "February 23, 2027",
        "publish_on": "2027-02-23 21:00",  # blog rotation, one series a day (Butch 2026-11-14)
        "slug": "closing-a-business-the-right-way",
        "category": "finance",
        "summary": "Shutting the door is not the same as closing a business. Here is why the town hall asks "
                   "for this year’s sales when you retire, what Section 145 of the Local Government Code "
                   "requires, the papers for the barangay, the BIR and the DTI, and the mistakes that keep a "
                   "closed business owing taxes.",
        "body": [
            "A couple ran a small bakery for six years. Last August, with rent rising and their eldest "
            "starting college, they sold the oven, returned the keys and put a sign on the door: “Thank you, "
            "suki!” They thought that was the end of it. The next January, a letter arrived from the "
            "municipal treasurer’s office. The bakery was still on the list of businesses due for renewal.",
            "(The bakery and the couple are invented, and so are the figures.)",
            "Closing a business has its own paperwork, just as opening one does. Stay with me to the end, "
            "and you will know why a business must be formally retired, why the treasurer asks for this "
            "year’s sales, what the barangay, the town hall, the BIR and the DTI each need, and the "
            "mistakes that keep a closed business owing taxes.",
            ("photo", "blog/finance-closing-business.jpg", "Closing a business: tell the barangay, retire "
             "the permit at the town hall, close the BIR registration, and cancel the business name. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Why “Retire” and Not Just “Close”"),
            "To the treasury, a business exists as long as its records say it does. If no one tells the "
            "town hall that the business has stopped, the records still show an active business, and the "
            "treasury still expects the tax and the renewal. Retiring a business is how the owner tells the "
            "government, officially, that the business has ended and on what date.",
            ("quote", "A business opens with papers, and it has to close with papers too."),
            ("h", "Why the Treasurer Asks for This Year’s Sales"),
            "This part can surprise business owners. Under Section 143 of the Local Government Code, the local "
            "business tax is computed on the gross sales or receipts for the preceding calendar year. So the "
            "tax a business pays in 2027 is based on what it sold in 2026.",
            "When a business ends, that pattern breaks: there is no next year to pay on this year’s sales. "
            "Section 145 handles it. A business that ends must submit a sworn statement of its gross sales "
            "or receipts for the current year. If the tax paid during the year is less than the tax due on "
            "those current-year sales, the difference must be paid before the business is considered "
            "officially retired.",
            ("h", "A Worked Example"),
            ("point", "Tax paid in January", "The bakery paid ₱9,000 in business tax for the year, based on "
             "last year’s sales."),
            ("point", "Sworn statement on closing", "From January to August, the bakery sold more than the "
             "year before. Using the town’s ordinance rates, the tax due on those sales comes to ₱10,500."),
            ("point", "The difference", "₱10,500 minus ₱9,000 equals ₱1,500, which must be paid before the "
             "bakery is officially retired."),
            "The rates themselves come from the local tax ordinance, within the limits in Section 143, so "
            "the figures differ from town to town. The treasurer’s office computes the final amount.",
            ("h", "Step 1: The Barangay"),
            "The town hall will want proof from the barangay that the business has stopped. In Quezon City, for example, this is a barangay certificate stating the exact closure date. Ask the barangay hall where the business operated what it issues and what it needs.",
            ("h", "Step 2: The Town Hall"),
            "Each local government sets its own list of requirements, so check with your business permits "
            "and licensing office. Quezon City, for example, asks for a notarized affidavit of closure "
            "stating the exact closure date, a barangay certificate with the closure date, the BIR "
            "certificate of registration, and sales records, among others. After the assessment is paid, "
            "the city issues a business retirement certificate.",
            ("point", "Affidavit of closure", "States the reason for closing and the exact date."),
            ("point", "Sworn statement of gross sales", "For the current year, up to the closing date."),
            ("point", "Latest permit and receipts", "Proof of what has already been paid."),
            ("point", "Payment of the assessment", "Including any difference under Section 145."),
            ("h", "Step 3: The BIR"),
            "The Bureau of Internal Revenue has its own closure process. Revenue Memorandum Circular No. "
            "47-2026, dated May 19, 2026, sets the current procedure.",
            ("point", "File BIR Form 1905", "This is the form used to cancel a registration."),
            ("point", "File the final returns", "Returns for every registered tax type, up to the closing "
             "date, with any tax due paid."),
            ("point", "Surrender unused invoices and permits", "Unused invoices, receipts and other "
             "accounting forms are submitted, along with the original BIR permits."),
            ("point", "Micro taxpayers", "Under the circular, micro taxpayers are no longer subject to a "
             "mandatory audit for closing a business."),
            ("h", "Step 4: The DTI, and Your Workers"),
            "A sole proprietor registered the business name with the Department of Trade and Industry, so "
            "the name must be cancelled there too. The DTI’s guide on closing a business lists a signed "
            "application form, a valid ID and a sworn declaration that the closure will not defraud "
            "creditors.",
            "If the business has employees, the DTI’s guide also points to the labor rules: written notice "
            "to the employees and to the Department of Labor and Employment at least one month before the "
            "closing date, and separation pay of at least one month’s pay or half a month’s pay for every "
            "year of service, whichever is higher.",
            ("h", "What Happens If You Do Not Retire"),
            "A business that stops without retiring can stay on the treasury’s list as an active "
            "business. Unpaid local business taxes can draw a surcharge of up to 25 percent and interest of "
            "up to 2 percent a month, for a maximum of 36 months, at rates set by the local ordinance "
            "(Section 168). The longer the owner waits, the harder it is to prove when the business really "
            "stopped.",
            ("h", "Keep the Closing Papers"),
            "Once everything is done, put the papers in one folder and keep it: the affidavit of closure, "
            "the barangay certificate, the retirement certificate from the town hall, the official receipt "
            "for the final payment, the BIR filing and clearance papers, and the DTI cancellation. If a "
            "letter or a bill arrives years later, that folder answers it in minutes. Keep a photo or scan "
            "of each one as well, in case the paper copies are lost.",
            ("h", "For Treasury Workers"),
            "A clear retirement process helps the treasury too. It keeps the list of active businesses "
            "honest, so collection targets and delinquency lists are real. Post the requirements at the "
            "window and on the town’s page, and give each retiring owner a written list. When a business "
            "has clearly closed but never retired, a letter explaining the steps does more good than a "
            "growing bill.",
            ("h", "Mistakes to Avoid"),
            ("point", "Closing the door and telling no one", "Retire the business at the town hall."),
            ("point", "Waiting until the next January", "Retire it soon after closing, while the records "
             "are fresh."),
            ("point", "Forgetting the BIR", "The local permit and the BIR registration are closed "
             "separately."),
            ("point", "Throwing away unused invoices", "They are surrendered to the BIR."),
            ("h", "Key Takeaways"),
            ("point", "Retire, do not just close", "The records must show the business has ended."),
            ("point", "This year’s sales matter", "Section 145 asks for a sworn statement and payment of "
             "any difference."),
            ("point", "Four offices, four steps", "Barangay, town hall, BIR and, for sole proprietors, "
             "the DTI."),
            ("point", "Delay costs money", "Unpaid taxes can draw surcharges and interest."),
            ("h", "Your Part 14 Action Plan"),
            ("point", "If you are closing a business", "Write down the closing date today, and keep your "
             "sales records up to that date."),
            ("point", "If you run a business", "Keep a folder with your permit, receipts and BIR "
             "registration, so closing, if it ever comes, is simple."),
            ("point", "If you work in a treasury", "Check whether your office has a written list of "
             "retirement requirements that owners can take home."),
            "The couple went to the town hall with the letter. The treasurer’s office explained the steps, "
            "and within a few weeks the bakery was officially retired. They paid the small difference, got "
            "their certificate, and framed the last receipt next to a photo of their first loaf.",
            ("cta", "Read the study note: Business tax and the mayor’s permit", "/study-notes/business-tax-and-mayors-permit/"),
            ("cta", "Read: Inside the Local Treasury, Part 2: The January Rush and Your Business Permit", "/blog/january-rush-business-permit/"),
            ("cta", "Read: Inside the Local Treasury, Part 6: Can the Town Forgive a Tax?", "/blog/can-the-town-forgive-a-tax/"),
            ("cta", "Read: Inside the Local Treasury, Part 13: From the Cash Box to the Bank, Why Deposits Cannot Wait", "/blog/deposits-cash-box-to-bank/"),
            ("ask", "Have you ever closed a business, or helped someone close one? Which step took the longest?"),
        ],
    },
    {
        "title": "Inside the Local Treasury, Part 13: From the Cash Box to the Bank, Why Deposits Cannot Wait",
        "date": "February 18, 2027",
        "publish_on": "2027-02-18 21:00",  # blog rotation, one series a day (Butch 2026-11-14)
        "slug": "deposits-cash-box-to-bank",
        "category": "finance",
        "summary": "Collecting the money is only half the job. Here is how a day’s collections travel from the "
                   "window to the bank, what “deposit intact” means, which banks may hold a town’s money, and "
                   "why a late deposit is a finding even when every peso is there.",
        "body": [
            "It was a Friday afternoon, and the market collector was having a good day. By four o’clock her cash box "
            "held more than ₱60,000. The bank was a forty-minute ride away, and it would close before she got "
            "there. So she locked the box in the office cabinet and went home, planning to deposit on "
            "Monday. Over the weekend, she kept thinking about that cabinet.",
            "(Like every case in this series, this one is invented, from the office down to the last peso.)",
            "Every peso a treasury collects has to reach the bank, whole and on time. Read to the end and "
            "you will know how collections travel from the window to the bank, what it means to deposit "
            "intact, which banks may hold a local government’s money, what the deposit papers prove, and "
            "how a collector far from a bank can stay inside the rules.",
            ("photo", "blog/finance-deposits.jpg", "From the cash box to the bank: deposit intact, deposit "
             "on time, keep the papers, and keep the funds apart. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "Why Deposits Matter"),
            "Cash in a drawer can be lost, stolen, borrowed or simply miscounted. Cash in a government bank "
            "account is recorded by someone outside the office, the bank, and can be checked against the "
            "treasury’s own books. A deposit turns money that depends on one person’s care into money that "
            "leaves a trail.",
            ("quote", "Money in the bank answers for itself. Money in a drawer needs someone to answer for it."),
            ("h", "Rule One: Deposit Intact"),
            "The Government Auditing Code, Presidential Decree No. 1445, says that officers who collect "
            "public money must remit or deposit intact the full amounts they receive and collect (Section "
            "69). Intact means exactly what was collected.",
            ("point", "No deductions", "Expenses are not paid out of collections, even small ones like "
             "fare or snacks for an event."),
            ("point", "No loans", "Not to a co-worker, not to yourself, and not “just until payday.”"),
            ("point", "No swapping", "Personal checks are not cashed from the cash box, and the collector’s "
             "own bills are not exchanged with the day’s collections."),
            "If the receipts for the day add up to ₱61,240, the deposit is ₱61,240. Anything less is a "
            "shortage, and Part 12 explained how seriously the law treats one.",
            ("h", "Rule Two: Deposit on Time"),
            "Collections are meant to reach the bank daily, or by the next banking day when they come in "
            "after the bank has closed. The Bureau of the Treasury’s Department Order No. 52-96, from May "
            "1996, sets this rhythm for national collections handled by local treasurers: deposit daily, "
            "and deposit collections received after banking hours on the next banking day.",
            "Audit reports test the same rhythm for local collections. For example, SunStar reported that "
            "the Commission on Audit’s 2025 annual audit report on Cebu City flagged collections "
            "that were not deposited each day or by the next banking day, and some that were not deposited "
            "intact.",
            "A late deposit can be a finding even when every peso is present, because the risk was there "
            "the whole time the money sat outside the bank.",
            ("h", "How Collections Travel"),
            ("point", "At the window", "Each payment gets an official receipt, issued in serial order."),
            ("point", "At the end of the day", "The collector counts the cash and checks, compares them with "
             "the receipts, and prepares a Report of Collections and Deposits, which lists the receipts and "
             "what was remitted or deposited."),
            ("point", "To the treasurer or the bank", "The collections go either to the treasurer or "
             "cashier, who signs for them, or straight to the bank."),
            ("point", "Back to the books", "The validated deposit slip comes back to the office and is "
             "attached to the report, so the books, the report and the bank all show the same amount."),
            ("h", "Which Banks May Hold a Town’s Money"),
            "A local government cannot open accounts wherever it likes. The Department of Finance’s "
            "Department Circular No. 001-2015, dated June 1, 2015, sets the rules for authorized government "
            "depository banks.",
            ("point", "Government banks first", "Local governments deposit with government financial "
             "institutions that hold a universal bank license and a CAMELS rating of at least 3."),
            ("point", "Collection banks", "Another bank may be used only to collect payments, for a fee, "
             "and the collections must move to the government bank on the next banking day."),
            ("point", "Other banks, by exception", "A non-government bank account is allowed only under conditions the circular lists. Among them are the lack of an accessible government bank or collection facility within a twenty-kilometer radius, and security reasons backed by a police certification. Even then, the account may hold only operating funds, and the balance is "
             "capped at three months of operating expenses or the deposit insurance limit, whichever is lower. That limit was ₱500,000 when the circular was issued."),
            ("h", "Keep the Funds Apart"),
            "A treasury does not pour everything into one account. Collections for the General Fund, the "
            "Special Education Fund and trust funds are reported and deposited separately, so that money "
            "set aside by law for one purpose is not spent on another. A deposit slip should show which "
            "fund it belongs to, and the report should match it fund by fund.",
            ("h", "When the Bank Is Far Away"),
            "Our collector’s problem is real in towns where the nearest bank branch is a long trip away. "
            "The rules do not disappear, so the office plans around them.",
            ("point", "Schedule the trip", "Set the deposit run early enough in the day to reach the bank "
             "before it closes."),
            ("point", "Use a collection facility", "Where the government bank has an authorized collection "
             "partner closer to the office, ask the treasurer whether it can be used."),
            ("point", "Remit to the treasurer", "A collector who cannot reach the bank can turn over the "
             "collections to the treasurer or cashier the same day, with the report, so the money moves "
             "out of one person’s hands."),
            ("point", "Secure what must stay overnight", "If cash must stay in the office, it goes in the "
             "vault or safe, is recorded, and is deposited first thing on the next banking day."),
            ("h", "What the Papers Prove"),
            "The Report of Collections and Deposits proves what was collected. The validated deposit slip "
            "proves what reached the bank. When the two match, the collector is clear. When an auditor "
            "compares the receipts, the report and the bank statement and finds a gap in time or in amount, "
            "the papers point to exactly where it happened. Keep them complete and filed by date.",
            ("h", "For Taxpayers"),
            "Pay only at an official window or through an official channel, and keep your official "
            "receipt. If a treasury offers payment through a bank or an online channel, the money goes "
            "straight into the government’s account and you get a record of your own.",
            ("h", "Mistakes to Avoid"),
            ("point", "Keeping collections for several days", "Deposit daily, or on the next banking day."),
            ("point", "Paying small expenses from collections", "Deposit intact, always."),
            ("point", "Mixing funds in one deposit", "Keep each fund on its own slip and report."),
            ("point", "Losing the validated deposit slip", "It is your proof. File it with the report."),
            ("h", "Key Takeaways"),
            ("point", "Deposit intact", "The full amount collected, with nothing taken out (PD 1445, "
             "Section 69)."),
            ("point", "Deposit on time", "Daily, or on the next banking day for late collections."),
            ("point", "Use the right bank", "Government banks first, under DOF Department Circular No. "
             "001-2015."),
            ("point", "Let the papers match", "Receipts, report and deposit slip should tell one story."),
            ("h", "Your Part 13 Action Plan"),
            ("point", "If you collect", "Check your last five deposit slips against your reports. Do the "
             "dates and amounts match?"),
            ("point", "If you supervise collectors", "List who deposits late and why, and fix the cause, "
             "whether it is distance, schedule or staffing."),
            ("point", "If you pay taxes or fees", "Keep your next official receipt, and ask whether your "
             "town offers payment through a bank."),
            "On Monday morning, the collector deposited the ₱60,000 the moment the bank opened. Every peso "
            "was there. Still, her supervisor changed the routine that week: on market days, the collector "
            "now turns over her collections to the cashier at three o’clock, and the cashier makes one "
            "deposit run for the whole office. The cabinet has been empty on weekends ever since.",
            ("cta", "Read the study note: Collection and deposit", "/study-notes/collection-and-deposit/"),
            ("cta", "Read: Inside the Local Treasury, Part 12: The Surprise Cash Count, and What a Shortage Means", "/blog/cash-counts-and-shortages/"),
            ("cta", "Read: Inside the Local Treasury, Part 11: The Blank Receipt Problem, Accountable Forms and the RAAF", "/blog/accountable-forms-blank-receipts/"),
            ("cta", "Read: Inside the Local Treasury, Part 7: From Budget to Check, How a Town Pays Its Bills", "/blog/from-budget-to-check/"),
            ("ask", "How far is the nearest bank from your town hall? How does your treasury handle the trip?"),
        ],
    },
    {
        "title": "Inside the Local Treasury, Part 12: The Surprise Cash Count, and What a Shortage Means",
        "date": "February 13, 2027",
        "publish_on": "2027-02-13 21:00",  # blog rotation, one series a day (Butch 2026-11-14)
        "slug": "cash-counts-and-shortages",
        "category": "finance",
        "summary": "An auditor can walk in and count a collector’s cash at any time. Here is how a cash count "
                   "works, how a shortage is computed, why the law treats a missing peso so seriously, and the "
                   "habits that keep an honest collector safe.",
        "body": [
            "At three in the afternoon, two people from the audit team walked up to a collector’s window and "
            "asked her to stop accepting payments. They were there for a cash count. She had not been told "
            "in advance, and that was the point. She closed her drawer, brought out her booklet of receipts "
            "and her cash box, and waited. She was nervous, though she had no reason to be. Or so she hoped.",
            "(The collector, the auditors and the office are invented for teaching, and so are the figures.)",
            "A cash count is one of the simplest controls in public finance. When you "
            "finish reading, you will know who answers for public money, how a cash count is done, how a "
            "shortage is computed, what the law says when cash is short or lost, and the daily habits that "
            "make a surprise count a non-event.",
            ("photo", "blog/finance-cash-count.jpg", "The cash count: list the receipts, count the cash, "
             "compare the two, and explain any difference at once. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "Who Answers for Public Money"),
            "Under the Government Auditing Code, Presidential Decree No. 1445, any officer whose duties "
            "permit or require the possession or custody of government funds or property is accountable for "
            "them and for their safekeeping (Section 101). In a local treasury, that includes the treasurer, "
            "cashiers, collectors and disbursing officers. The same section requires these officers to be "
            "bonded.",
            ("point", "The bond", "A fidelity bond, processed through the Bureau of the Treasury, protects the government, not the officer. It is there to make the government whole if public money is lost, and it does not clear the officer of liability."),
            ("point", "The head of the office", "The head of each agency is immediately and primarily "
             "responsible for all its funds and property, and those under the head answer to the head "
             "(Section 102)."),
            ("point", "Supervision", "A head who fails to supervise accountable officers with due care can "
             "be held jointly and solidarily liable with the officer who is primarily accountable (Section "
             "104)."),
            ("quote", "A collector holds the public’s money for a few hours. The law expects it back in full."),
            ("h", "How a Cash Count Works"),
            "A cash count compares two things: what the records say the collector should have, and what the "
            "collector actually has. The idea is simple enough to do on a single sheet of paper.",
            ("point", "Stop the transactions", "No payments are accepted while the count is going on, so "
             "the figures stay still."),
            ("point", "List the receipts", "Find the last receipt covered by the most recent deposit. Every "
             "receipt issued after it is money the collector should still be holding."),
            ("point", "Add up the accountability", "Total the amounts on those receipts."),
            ("point", "Count the cash and checks", "Bills and coins are counted by denomination. Checks are "
             "listed one by one and checked against the receipts they paid for."),
            ("point", "Compare and sign", "If the two totals match, the count is clean. If they do not, the "
             "difference is recorded, and the collector is asked to explain it."),
            ("h", "Computing a Shortage: A Worked Example"),
            "Here is the count at our collector’s window, step by step.",
            ("point", "Last deposit", "Covered receipts up to number 7820."),
            ("point", "Receipts issued since", "Numbers 7821 to 7864, which total ₱38,450. That is her "
             "accountability for undeposited collections."),
            ("point", "Cash counted", "₱37,950 in bills and coins."),
            ("point", "Checks on hand", "One check for ₱300, payable to the municipality and matching a "
             "receipt in the series."),
            ("point", "Total on hand", "₱37,950 plus ₱300 equals ₱38,250."),
            ("point", "Shortage", "₱38,450 minus ₱38,250 equals ₱200."),
            "Two hundred pesos. She looked at the figure twice. Then she remembered: a taxpayer had paid "
            "₱200 that morning, and she had written the receipt, but had she put the money in the box? A "
            "small shortage still has to be explained and restored right away. The size of the amount does "
            "not change the duty.",
            ("h", "Why a Missing Peso Is Serious"),
            "A shortage is more than an accounting problem. Article 217 of the Revised Penal Code, on "
            "malversation of public funds, says that when a public officer fails to have public funds or "
            "property duly forthcoming upon demand by a duly authorized officer, that failure is prima facie "
            "evidence that the officer put the missing funds or property to personal use.",
            "Prima facie means that the law presumes it until the officer proves otherwise. That is why an "
            "honest collector with a sloppy cash box is still in danger. The presumption does not ask "
            "whether the officer is a good person. It asks whether the money is there.",
            ("point", "Liability for funds", "An officer accountable for funds is liable for all losses that "
             "result from their unlawful deposit, use or application, and for losses caused by negligence "
             "in keeping them (PD 1445, Section 105)."),
            ("point", "Orders from above", "Acting on a superior’s instruction does not relieve an "
             "accountable officer of liability, unless the officer notified the superior in writing that "
             "the payment was illegal (PD 1445, Section 106)."),
            ("h", "When the Treasurer Is Found Short"),
            "The Government Auditing Code has a rule for the most serious case. When an examination of a "
            "local treasurer’s accounts shows a shortage in the cash that should be on hand, the examining "
            "officer takes full possession of the office and its contents, notifies the Commission on Audit "
            "and the local chief executive, closes the treasurer’s accounts up to the date of possession, "
            "and carries on the office’s public business for the time being (PD 1445, Section 46).",
            ("h", "Losses That Are Not the Officer’s Fault"),
            "Robbery, fire and flood happen. The law gives an honest officer a way to be cleared. When "
            "government funds or property are lost in transit, or through fire, theft or another casualty, "
            "the officer must notify the Commission on Audit or the auditor at once, and file an "
            "application for relief, with the available evidence, within thirty days of the loss, unless a "
            "longer period is allowed in a particular case (PD 1445, Section 73).",
            "Missing that deadline can cost the officer the relief. If you are ever robbed while carrying "
            "collections, the police report is only the first paper. The application for relief is the one "
            "that protects you.",
            ("h", "Habits That Make a Surprise Count a Non-Event"),
            ("point", "Count your own cash every day", "Before the end of the day, total your receipts and "
             "count your box. A gap you find at four o’clock is easier to explain than one an auditor finds "
             "the next morning."),
            ("point", "Deposit intact and on time", "The Government Auditing Code requires collecting "
             "officers to deposit the full amounts they collect (PD 1445, Section 69). Do not pay expenses "
             "out of collections."),
            ("point", "Never mix your own money with public money", "Keep your personal wallet away from the "
             "cash box, and never lend from collections, even for an hour."),
            ("point", "Keep checks matched to receipts", "Each check should point to the receipt it paid."),
            ("point", "Keep your bond current", "Know when it expires and what amount it covers."),
            ("point", "Object in writing", "If you are told to release money in a way you believe is "
             "illegal, put your objection on paper before you act."),
            ("h", "For Taxpayers"),
            "Always ask for an official receipt, and check that its amount matches what you paid. The "
            "receipt is your proof of payment, and it is also what lets an auditor find any money that did "
            "not reach the treasury. Every receipt you insist on helps keep a collector honest and helps "
            "clear an honest one.",
            ("h", "Mistakes to Avoid"),
            ("point", "Leaving collections undeposited for days", "Money in a box is exposed to loss and to "
             "suspicion."),
            ("point", "Using the cash box for change from your own wallet", "It blurs whose money is whose."),
            ("point", "Waiting to explain a shortage", "Explain and restore it at once."),
            ("point", "Forgetting the 30-day deadline after a robbery", "File the application for relief "
             "on time."),
            ("h", "Key Takeaways"),
            ("point", "Accountable officers answer for public money", "And they must be bonded (PD 1445, "
             "Section 101)."),
            ("point", "A cash count compares records with cash", "Receipts since the last deposit against "
             "what is in the box."),
            ("point", "Failure to produce funds on demand is serious", "Under Article 217, it is prima facie "
             "evidence of malversation."),
            ("point", "Honest losses can be relieved", "Notify at once and file within 30 days."),
            ("h", "Your Part 12 Action Plan"),
            ("point", "If you handle collections", "Do your own cash count before closing today, using the "
             "steps above."),
            ("point", "If you supervise collectors", "Hold one unannounced count this month, and treat a "
             "clean result as good news, not as wasted time."),
            ("point", "If you pay taxes or fees", "Check the next official receipt you receive before you "
             "leave the window."),
            "The ₱200 turned up in the collector’s own wallet. While making change that morning, she had slipped the taxpayer’s bills in with her own money by mistake. She restored "
            "it on the spot, the auditors noted the explanation, and the next morning she bought a separate "
            "coin purse for her own money. She has not mixed the two since.",
            ("cta", "Read the study note: Accountability: bonds, cash counts and shortages", "/study-notes/accountability-bonds-cash-counts-shortages/"),
            ("cta", "Read: Inside the Local Treasury, Part 11: The Blank Receipt Problem, Accountable Forms and the RAAF", "/blog/accountable-forms-blank-receipts/"),
            ("cta", "Read: Inside the Local Treasury, Part 9: When COA Writes, From Audit Memo to Disallowance", "/blog/when-coa-writes/"),
            ("cta", "Read: Inside the Local Treasury, Part 8: Cash Advances, the Money You Must Account For Later", "/blog/cash-advances-explained/"),
            ("ask", "Have you ever been part of a surprise cash count, on either side of the window? What did it teach you?"),
        ],
    },
    {
        "title": "Inside the Local Treasury, Part 11: The Blank Receipt Problem, Accountable Forms and the RAAF",
        "date": "February 8, 2027",
        "publish_on": "2027-02-08 21:00",  # blog rotation, one series a day (Butch 2026-11-14)
        "slug": "accountable-forms-blank-receipts",
        "category": "finance",
        "summary": "A blank official receipt has no value, yet losing one can cause more trouble than losing "
                   "cash. Here is why receipts are counted by serial number, how a booklet moves through a "
                   "treasury, what the RAAF report shows, and what to do when a form goes missing.",
        "body": [
            "A collector at a public market finished her day, counted her cash and balanced her report. "
            "Everything matched, except one thing. In her booklet of official receipts, number 4517 was "
            "missing. Not used, not cancelled, just gone. The cash was complete, so she wondered whether it "
            "mattered. Her supervisor told her it mattered more than she thought.",
            "(The collector and the market are a composite. No real person, office or form is described.)",
            "A missing receipt is a door left open. Anyone holding a blank official receipt could collect money "
            "that never reaches the treasury, and the taxpayer would walk away believing they had paid. "
            "Stay with me to the end, and you will know what accountable forms are, how a booklet moves "
            "from the supplier to the collector and back, how the RAAF report keeps every serial number in "
            "view, and the habits that keep a collector safe.",
            ("photo", "blog/finance-accountable-forms.jpg", "Accountable forms: counted by serial number, "
             "issued in order, reported in the RAAF, and reported at once when lost. (Illustration: Butch "
             "Mahinay, aumahinay.dev)", "medium"),
            ("h", "What Makes a Form Accountable"),
            "Some printed forms are worth nothing until they are used, but become proof of payment once they "
            "are. Official receipts, community tax certificates and cash tickets are examples. Because of "
            "that, the officer who holds them answers for every one, by serial number, until it is used, "
            "cancelled or returned.",
            ("point", "Official receipts for general collections", "Accountable Form No. 51 is an official "
             "receipt used for taxes, fees and charges."),
            ("point", "Official receipts for real property tax", "Accountable Form No. 56 shows the "
             "property, its assessed value, and the basic tax and Special Education Fund separately."),
            ("point", "Community tax certificates", "The cedula from Part 3, for individuals and "
             "corporations."),
            ("point", "Cash tickets", "Forms with a printed money value, such as those sold at markets. For "
             "these, a missing piece can mean a liability for its face value."),
            ("quote", "A blank receipt is worth nothing until someone uses it. That is exactly why it must be "
             "counted."),
            ("h", "The Life of a Booklet"),
            ("point", "Supply", "The treasurer obtains forms from the provincial treasurer’s office or "
             "directly from the National Printing Office."),
            ("point", "Custody", "The stock is kept in a safe place, and every booklet received is recorded "
             "by form number and serial numbers."),
            ("point", "Issue", "Booklets are issued to collectors in serial order, and the collector signs "
             "for them. From that moment, the collector answers for every receipt inside."),
            ("point", "Use", "Receipts are used in serial order, one per payment. A spoiled receipt is marked "
             "“Cancelled,” with all its copies left in the booklet."),
            ("point", "Return", "A finished booklet, with its copies, goes back to the treasurer and is kept "
             "for audit."),
            ("h", "The RAAF: Four Numbers That Must Agree"),
            "The Report of Accountability for Accountable Forms, or RAAF, is how a collector reports the "
            "forms in their care. For each kind of form, it shows the quantity and the first and last serial "
            "numbers in four columns:",
            ("point", "Beginning balance", "Forms on hand at the start of the period."),
            ("point", "Receipts", "Forms received during the period."),
            ("point", "Issued", "Forms used, including cancelled ones, or issued to others."),
            ("point", "Ending balance", "Forms still on hand at the end of the period."),
            "The arithmetic must hold: beginning balance plus receipts, minus issued, equals ending balance. "
            "Each collector prepares a RAAF every month. The liquidating officer combines them into a "
            "Consolidated RAAF, or CRAAF, submitted on or before the 5th day of the following month.",
            ("h", "A Worked Example"),
            ("point", "June 1", "A collector holds two booklets, serial numbers 12401 to 12500: 100 "
             "receipts."),
            ("point", "June 10", "She receives five more booklets, 12501 to 12750: 250 receipts."),
            ("point", "During June", "She uses 12401 to 12580, including two cancelled: 180 receipts."),
            ("point", "Ending balance", "100 + 250 − 180 = 170 receipts, serial numbers 12581 to 12750. "
             "Check: 12750 − 12581 + 1 = 170."),
            "When the count and the serial numbers agree, the RAAF tells a clean story. When they do not, "
            "the gap is where the questions start.",
            ("h", "What Auditors Look For"),
            "COA auditors match the serial numbers on the RAAF against the receipts, the reports of "
            "collections and deposits, and the deposits themselves. A gap or a repeated number stands out. "
            "If receipt 4517 appears in no report and is not marked cancelled, someone must explain where it "
            "went.",
            "That is why the collector’s complete cash did not settle the matter. The cash proved what she "
            "collected with the receipts she used. It said nothing about a receipt someone else might use.",
            ("h", "When a Form Goes Missing"),
            ("point", "Report it at once", "Tell the treasurer and the COA auditor the same day. A late "
             "report looks worse than an early one."),
            ("point", "Apply for relief when the law allows", "Under Section 73 of PD 1445, when government "
             "funds or property are lost through fire, theft or other casualty, the accountable officer "
             "notifies COA immediately and files an application for relief, with evidence, within 30 days."),
            ("point", "Expect a question about care", "Relief is given only when the evidence shows the "
             "loss was not due to the officer’s negligence."),
            ("h", "Habits That Keep a Collector Safe"),
            ("point", "Never pre-sign or pre-fill receipts", "A signed blank receipt is a gift to anyone who "
             "finds it."),
            ("point", "Never lend a booklet", "Not even for a few minutes. The collector who signed for it "
             "answers for it."),
            ("point", "Never use another collector’s booklet", "Every receipt must come from your own "
             "issued series."),
            ("point", "Count at the start and end of the day", "And lock unused booklets away."),
            ("h", "What Taxpayers Can Do"),
            "Always ask for an official receipt, and look at it before you leave the window. Check that it "
            "has a serial number, the correct amount and the date. A handwritten note, an acknowledgment slip "
            "or a receipt from a booklet that looks different from the usual is worth a polite question. Your receipt is your proof, and the treasury’s record that the money arrived. For real property tax, the receipt should also show the property, and the basic tax and the Special Education Fund as separate amounts. Keep these receipts with the tax declaration, as Part 5 advised.",
            ("h", "For Treasury Workers"),
            ("point", "Issue in order, record every booklet", "Keep the stock record current, by serial "
             "number."),
            ("point", "Check the RAAF arithmetic monthly", "Do not wait for the auditor to find a gap."),
            ("point", "Explain why it matters", "New collectors follow rules better when they understand "
             "the blank receipt problem."),
            ("h", "Mistakes to Avoid"),
            ("point", "Thinking complete cash closes the matter", "A missing blank receipt is a separate "
             "risk."),
            ("point", "Throwing away a spoiled receipt", "Mark it cancelled and keep every copy."),
            ("point", "Lending a booklet", "Accountability does not transfer."),
            ("point", "Reporting a loss days later", "Report it the same day."),
            ("h", "The Collector’s Receipt"),
            "The supervisor helped her search the stall area and the collection bag. Receipt 4517 turned up "
            "between the pages of her cash notebook, torn out by accident and still blank. She marked it "
            "cancelled, kept it with the booklet, and noted it in her report. From then on, she counted her "
            "receipts at the end of every day, not just her cash.",
            ("h", "Key Takeaways"),
            ("point", "Blank forms carry risk", "That is why they are counted by serial number."),
            ("point", "Beginning plus receipts minus issued equals ending", "The RAAF must always balance."),
            ("point", "CRAAF by the 5th", "Collectors’ reports are consolidated monthly."),
            ("point", "Report losses at once", "PD 1445, Section 73, sets 30 days for relief."),
            ("h", "The Question to Ask"),
            "Do you check the serial number on your official receipt? If you work in a treasury, ask your "
            "office: when did we last reconcile every booklet issued with every receipt reported?",
            ("cta", "Read the study note: Accountable forms and the RAAF", "/study-notes/accountable-forms-and-raaf/"),
            ("cta", "Read: Inside the Local Treasury, Part 3: The Cedula", "/blog/the-cedula-explained/"),
            ("cta", "Read: Inside the Local Treasury, Part 9: When COA Writes", "/blog/when-coa-writes/"),
            ("cta", "Read: Inside the Local Treasury, Part 10: Where to See How Your Town Spends", "/blog/where-to-see-how-your-town-spends/"),
            ("ask", "Have you ever been given a receipt that did not look right? What did you do?"),
        ],
    },
    {
        "title": "Inside the Local Treasury, Part 10: Where to See How Your Town Spends",
        "date": "February 3, 2027",
        "publish_on": "2027-02-03 21:00",  # blog rotation, one series a day (Butch 2026-11-14)
        "slug": "where-to-see-how-your-town-spends",
        "category": "finance",
        "summary": "Your town’s budget, its cash flows, its bids and its audit findings are meant to be public. "
                   "Here is what the law and the Full Disclosure Policy require towns to post, where to find "
                   "it, and how to read the first few numbers.",
        "body": [
            "A group of senior high school students had a class project: find out how their town spent its "
            "money last year. Their teacher expected them to come back with nothing. Instead, they came back "
            "with photos of a bulletin board at the municipal hall, a printout of a cash flow statement, and "
            "a question for their teacher: “Why is the money for the new market still unspent?”",
            "(The students and their town are a composite. No real town, school or amount is described.)",
            "A town’s finances are not supposed to be a secret, and the law says so. This post explains what "
            "towns are required to post, where to look for it, which documents to read first, and what "
            "questions a resident, a student or a treasury worker can fairly ask after reading them.",
            ("photo", "blog/finance-full-disclosure.jpg", "Where to see how your town spends: the bulletin "
             "board, the website, the audit report and the procurement notices. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "The Law: Section 352"),
            "Section 352 of the Local Government Code requires the local treasurer to post, within 30 days "
            "after the end of each year, a summary of all revenues collected and funds received, and of the "
            "appropriations and disbursements, in at least three publicly accessible and conspicuous places. "
            "Part 7 mentioned it as the last step in the trail of a payment.",
            "Section 352 sets the minimum. A national policy built on it asks for much more.",
            ("quote", "Public money leaves a public trail. You only have to know where to look."),
            ("h", "The Full Disclosure Policy"),
            "In 2010, the Department of the Interior and Local Government (DILG) issued Memorandum Circular "
            "No. 2010-83, known as the Full Disclosure Policy. According to the DILG, it requires local "
            "officials of provinces, cities and municipalities to fully disclose particular financial "
            "transactions, so that residents know how the budget is managed, disbursed and used.",
            "The circular was challenged in court as an intrusion on local autonomy. In Villafuerte v. "
            "Robredo, decided in December 2014, the Supreme Court upheld it. The Court called its posting "
            "requirements “mere transparency measures” and said the documents it requires are “well-within "
            "the contemplation of Section 352” of the Code.",
            ("h", "What Towns Must Post"),
            "The DILG’s Full Disclosure Policy page lists the reports in three groups:",
            ("point", "Budget reports", "The annual budget report, every year. The statement of debt service, the statement of receipts and expenditures and the statement of cash flow, every quarter."),
            ("point", "Procurement reports", "The annual procurement plan or procurement list, and any "
             "supplemental plan. Items to bid, bid results and abstracts of bids, every quarter."),
            ("point", "Special purpose fund reports", "Special Education Fund estimates and utilization, the "
             "Gender and Development accomplishment report, the use of the 20% development fund from the "
             "national tax allotment, and the use of the disaster risk reduction and management fund."),
            ("h", "Where to Look"),
            ("point", "Bulletin boards", "The policy calls for posting in at least three conspicuous places, "
             "such as the municipal or city hall, the provincial capitol, barangay halls, public markets, "
             "hospitals and schools."),
            ("point", "The town’s website", "The Supreme Court’s decision describes posting on websites as "
             "well as in public buildings and print media."),
            ("point", "The DILG’s Full Disclosure Policy portal", "The DILG runs an online portal for these "
             "reports, at fdpp.dilg.gov.ph."),
            ("point", "COA’s audit reports", "Part 9 explained that annual audit reports on local governments "
             "are public, and COA posts audit reports on its website."),
            ("h", "Reading the First Three Documents"),
            "The full set can be long. Start with three, and look for one thing in each.",
            ("point", "The annual budget report", "Find the total budget, then the three largest items. Ask "
             "whether they match what the town says its priorities are."),
            ("point", "The statement of receipts and expenditures", "Compare what was collected with what was estimated. A large gap is worth a question."),
            ("point", "The 20% development fund report", "Look for projects listed as not started or not "
             "completed. That is where the students found their unspent market money."),
            ("h", "Four Words That Unlock the Reports"),
            "The reports use the same few words again and again. Part 7 introduced most of them.",
            ("point", "Appropriation", "The amount the budget allows to be spent on an item. It is "
             "permission, not cash."),
            ("point", "Obligation", "Part of an appropriation set aside for a specific claim, such as a "
             "contract or a payroll."),
            ("point", "Disbursement", "Money actually paid out of the treasury."),
            ("point", "Balance", "What is left of an appropriation that has not been obligated or spent. A "
             "large balance late in the year is a fair thing to ask about."),
            "With these four words, a resident can follow an item from the budget to the payment, and see "
            "where it stopped.",
            ("h", "Questions You Can Fairly Ask"),
            "Reading the reports is the start. Asking about them is how they become useful. Good questions "
            "are specific and polite.",
            ("point", "Why was this project not started?", "There may be a good reason, such as a failed "
             "bidding or a land issue. Asking lets the office explain."),
            ("point", "Why did this revenue fall short?", "Part 1 showed how a town depends on local "
             "collections and transfers from the national government."),
            ("point", "Where can I see the bid results?", "The procurement reports should name the winning "
             "bidders and amounts."),
            ("point", "What did the auditor say?", "The audit report includes management’s comments on each "
             "finding."),
            ("h", "What Happens When a Town Does Not Post"),
            "According to the DILG, COA auditors were directed in 2010 to monitor compliance with the Full "
            "Disclosure Policy, and deviations may be raised in an audit observation memorandum and appear in "
            "the annual audit report. The DILG also cites Section 60 of the Local Government Code, which "
            "allows officials to be disciplined for gross negligence or dereliction of duty.",
            "For a resident, the practical step is simpler: if a report is missing from the board or the "
            "website, ask the town where it can be seen.",
            ("h", "For Treasury Workers"),
            ("point", "Post on time, every time", "The Section 352 summary is due within 30 days after the "
             "year ends. Put the date on the office calendar."),
            ("point", "Make the board readable", "A faded printout behind dusty glass is posted but not "
             "disclosed. Replace pages when they fade."),
            ("point", "Welcome the questions", "A resident who reads the cash flow statement is doing what "
             "the policy intends. A clear answer builds trust."),
            ("h", "Mistakes to Avoid"),
            ("point", "Assuming the numbers are secret", "The policy requires them to be posted."),
            ("point", "Reading only the totals", "The story is in the items and the unspent balances."),
            ("point", "Jumping to conclusions", "An unspent fund can have a lawful reason. Ask first."),
            ("point", "Forgetting the audit report", "It is the independent view of the same numbers."),
            ("h", "The Students’ Answer"),
            "The students wrote to the municipal planning office with their question. The reply explained "
            "that the market project’s first bidding had failed and a second was scheduled. They added the "
            "letter to their report, and their teacher posted the whole project on the school’s bulletin "
            "board, two blocks from the one at the municipal hall.",
            ("h", "Key Takeaways"),
            ("point", "Section 352 is the minimum", "A yearly summary posted within 30 days in three "
             "public places."),
            ("point", "The Full Disclosure Policy asks for more", "Budget, procurement and special fund "
             "reports, upheld by the Supreme Court in 2014."),
            ("point", "Look in four places", "Bulletin boards, the town website, the DILG portal and COA’s "
             "audit reports."),
            ("point", "Ask specific, polite questions", "The reports are meant to be read and asked about."),
            ("h", "The Question to Ask"),
            "When did you last look at your town’s bulletin board for its budget reports? If you work in a "
            "treasury, ask your office: are this quarter’s reports posted, and could a student read them?",
            ("cta", "Read: Inside the Local Treasury, Part 9: When COA Writes", "/blog/when-coa-writes/"),
            ("cta", "Read: Inside the Local Treasury, Part 1: Where Your Town's Money Comes From", "/blog/where-your-towns-money-comes-from/"),
            ("cta", "Read: Inside the Local Treasury, Part 7: From Budget to Check", "/blog/from-budget-to-check/"),
            ("cta", "Read: Year-End in the Treasury: What Really Happens in December", "/blog/year-end-in-the-treasury/"),
            ("ask", "Have you ever read your town’s budget or audit report? What surprised you?"),
        ],
    },
    {
        "title": "Inside the Local Treasury, Part 9: When COA Writes, From Audit Memo to Disallowance",
        "date": "January 29, 2027",
        "publish_on": "2027-01-29 21:00",  # blog rotation, one series a day (Butch 2026-11-14)
        "slug": "when-coa-writes",
        "category": "finance",
        "summary": "An audit memo, a notice of suspension, a notice of disallowance: each letter from the "
                   "Commission on Audit means something different. Here is what each one asks, the deadlines "
                   "the law sets, how an appeal works, and how to keep a memo from becoming a disallowance.",
        "body": [
            "The envelope was on the treasurer’s desk on a Monday morning, marked with the seal of the "
            "Commission on Audit. Inside was an audit observation memorandum about cash advances that were "
            "past their liquidation deadline. A new clerk, seeing the seal, asked in a whisper whether "
            "someone was in trouble. The treasurer smiled. “Not yet,” she said. “This is the letter that "
            "lets us fix it before anyone is.”",
            "(The treasurer and the clerk are made up for this post, as in every part of this series. No "
            "real office, person or amount is described.)",
            "A letter from the Commission on Audit, or COA, can cause panic in an office. It should cause "
            "action instead, and the right action depends on which letter it is. By the last section, you "
            "will know what COA does, the difference between an audit observation memorandum, a notice of "
            "suspension and a notice of disallowance, the deadlines the law sets, how an appeal works, and "
            "the habits that keep a memo from growing into a disallowance.",
            ("photo", "blog/finance-coa.jpg", "When COA writes: an observation, a suspension, a disallowance, "
             "and the way to settle each. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Who COA Is and Why It Writes"),
            "The Commission on Audit is the constitutional body that examines, audits and settles the "
            "accounts of government offices, local governments included. Its auditors check that money was "
            "collected, kept and spent according to law, and that every transaction has the documents to "
            "prove it.",
            "Auditors work from documents. That is why the earlier parts of this "
            "series kept returning to papers: the official receipt, the voucher, the liquidation report. "
            "When a paper is missing or a rule was not followed, the auditor writes.",
            ("quote", "An audit letter is a question. The answer is a document."),
            ("h", "Letter One: The Audit Observation Memorandum"),
            "An audit observation memorandum, or AOM, tells the office what the auditor noticed. It might "
            "point out cash advances past their deadline, collections deposited late, or records that are "
            "incomplete. It asks the office for its comments and the documents that explain or correct the "
            "finding.",
            "An AOM is the early warning. In our story, the treasurer’s office had a list of employees whose "
            "travel advances were overdue. The memo was the chance to collect their liquidation reports, as "
            "Part 8 described, before the finding hardened into something worse.",
            ("h", "Letter Two: The Notice of Suspension"),
            "A notice of suspension holds a transaction in place because something is missing or unclear, "
            "such as a voucher without the documents that support it. The transaction is not yet rejected. "
            "It is waiting for an explanation.",
            "The Government Auditing Code sets a clock on that wait. Section 82 of Presidential Decree No. "
            "1445 says a suspension “which is not satisfactorily explained within ninety days” after the "
            "accountable officer receives the notice “shall become a disallowance,” unless the auditor, in "
            "writing and for good cause, extends the time.",
            ("point", "What to do", "Submit the missing documents, or a written explanation, well before "
             "the 90 days end."),
            ("point", "What not to do", "Wait for a reminder. The deadline runs from receipt of the notice, "
             "not from the next letter."),
            ("h", "Letter Three: The Notice of Disallowance"),
            "A notice of disallowance, or ND, means the auditor has decided that a payment should not have "
            "been made, in whole or in part. It names the amount and the persons the auditor holds liable for "
            "it.",
            "This is where liability becomes personal. Section 103 of PD 1445 says spending of government "
            "funds in violation of law or regulations “shall be a personal liability of the official or "
            "employee found to be directly responsible therefor.” Part 7 explained why signatures carry "
            "weight. A disallowance is where that weight is measured in pesos.",
            "COA can also issue a notice of charge, for revenue that should have been collected in full but "
            "was not. For a treasury, that can mean a tax, fee or charge that was under-assessed or not "
            "collected.",
            ("h", "How an Appeal Works"),
            "A disallowance is not the last word if the office believes the auditor is wrong.",
            ("point", "Six months to appeal", "Section 48 of PD 1445 lets any person aggrieved by an "
             "auditor’s decision appeal in writing within six months from receipt of the decision."),
            ("point", "First stop: the Director", "Under COA’s 2009 Revised Rules of Procedure, Rule V, an "
             "aggrieved party appeals from the auditor to the Director, within six months after receiving "
             "the decision."),
            ("point", "Then the Commission Proper", "Rule VII allows a further appeal, but only within the "
             "time remaining of the same six-month period. Time spent on the first appeal counts against "
             "it."),
            ("point", "If no appeal is filed", "Section 51 of PD 1445 makes the decision final and "
             "executory."),
            "Because the six months are shared between stages, an office that waits until the fifth month to "
            "file its first appeal leaves itself very little time for the next one.",
            ("h", "How Each Letter Ends"),
            "When the documents are submitted, the amount is refunded, or an appeal succeeds, the matter is "
            "settled. The auditor then issues a notice of settlement of suspension, disallowance or charge, "
            "which allows the item to be removed from the books. Keep that notice. It is the proof that the "
            "matter is closed.",
            ("h", "What Residents Can Read"),
            "Audit findings are not secret. Annual audit reports on local governments are public documents. COA posts audit reports on its website, coa.gov.ph, and some towns post their own reports on their websites. A town’s report lists the auditor’s observations, "
            "the recommendations, and the management’s comments. Reading your town’s report is one of the "
            "clearest views of how its money was handled.",
            ("h", "For Treasury Workers"),
            ("point", "Log every letter on the day it arrives", "Write the date received and the deadline it "
             "starts. For a suspension, that is 90 days. For a disallowance, six months to appeal."),
            ("point", "Answer the AOM fully", "Attach documents, not just explanations. A finding fixed at "
             "the AOM stage does not reach the later letters."),
            ("point", "Fix the cause, not only the case", "If the AOM was about late liquidations, set up "
             "the tracking list from Part 8 so the next audit finds none."),
            ("point", "Get advice early on an ND", "A disallowance involves personal liability and strict "
             "deadlines. Consult your office’s legal officer before the time runs short."),
            ("h", "Mistakes to Avoid"),
            ("point", "Treating an AOM as routine paperwork", "It is the cheapest stage to fix a problem."),
            ("point", "Letting the 90 days pass", "Under Section 82, an unexplained suspension becomes a "
             "disallowance."),
            ("point", "Appealing late in the six months", "The same six months must cover every stage of "
             "appeal."),
            ("point", "Losing the settlement notice", "Without it, proving that the matter is closed is "
             "harder."),
            ("h", "The Treasurer’s Answer"),
            "The treasurer gave each employee named in the memo a written reminder with a date. Within two "
            "weeks, every overdue advance was liquidated or refunded, and the office replied to the AOM with "
            "copies of the reports and official receipts attached. The finding appeared in the audit report "
            "as an observation with the office’s action noted, and it went no further.",
            ("h", "Key Takeaways"),
            ("point", "Each letter means something different", "An AOM observes, a suspension waits, a "
             "disallowance decides."),
            ("point", "Ninety days for a suspension", "PD 1445, Section 82, turns an unexplained suspension "
             "into a disallowance."),
            ("point", "Six months to appeal, shared", "Section 48 and COA’s rules set one six-month period "
             "for all stages."),
            ("point", "Liability is personal", "Section 103 places it on the person directly responsible."),
            ("h", "The Question to Ask"),
            "Have you ever read your town’s annual audit report? If you work in a treasury, ask your office: "
            "how many audit observations from last year are still unanswered, and who owns each one?",
            ("cta", "Read: Inside the Local Treasury, Part 8: Cash Advances", "/blog/cash-advances-explained/"),
            ("cta", "Read: Inside the Local Treasury, Part 7: From Budget to Check", "/blog/from-budget-to-check/"),
            ("cta", "Read the study note: Disbursements, vouchers, checks and cash advances", "/study-notes/disbursements-vouchers-checks-cash-advances/"),
            ("cta", "Read: Year-End in the Treasury: What Really Happens in December", "/blog/year-end-in-the-treasury/"),
            ("ask", "What is the most useful thing you learned from an audit finding? I'd like to hear it."),
        ],
    },
    {
        "title": "Inside the Local Treasury, Part 8: Cash Advances, the Money You Must Account For Later",
        "date": "January 24, 2027",
        "publish_on": "2027-01-24 21:00",  # blog rotation, one series a day (Butch 2026-11-14)
        "slug": "cash-advances-explained",
        "category": "finance",
        "summary": "A cash advance looks like money in hand, but it is a debt to the town until it is "
                   "liquidated. Here is who may get one, what it may be used for, the deadlines to account for "
                   "it, and what happens when they are missed.",
        "body": [
            "Three weeks after a seminar in Manila, an employee found a note clipped to her payslip: “Please "
            "see the accountant re: unliquidated cash advance.” She had come home with receipts in her bag "
            "and every intention of filing them. Then work piled up. Now her next salary was at risk.",
            "(Like every story in this series, this one is a composite. No real employee, office or amount "
            "is described.)",
            "A cash advance is simple to receive and easy to forget. Read to the end and you will know what a "
            "cash advance is, who may receive one, the rules that keep it honest, the deadlines for "
            "accounting for it, what happens when they pass, and the habits that make liquidation painless.",
            ("photo", "blog/finance-cash-advance.jpg", "Cash advances: a specific purpose, one at a time, "
             "liquidated on time, and the balance refunded. (Illustration: Butch Mahinay, aumahinay.dev)",
             "medium"),
            ("h", "What a Cash Advance Is"),
            "Part 7 followed a normal payment: the goods or service come first, then the voucher, then the "
            "check. Some expenses cannot wait for that. An employee traveling to a seminar needs money for "
            "fares and meals before the trip, and a payroll paid in cash needs cash before payday.",
            "A cash advance solves that. Money is released before the expense, to an official or employee "
            "who becomes accountable for it. Until they show how it was spent and return what was not spent, "
            "the amount stays on the books as something they owe.",
            ("quote", "A cash advance is not an allowance. It is a loan from the town that is repaid with "
             "receipts."),
            ("h", "The Rules in the Law"),
            ("point", "Only under COA’s rules", "Section 339 of the Local Government Code says no cash "
             "advance may be granted to any local official or employee except under the rules of the "
             "Commission on Audit (COA)."),
            ("point", "Only for a specific purpose", "Section 89 of the Government Auditing Code, Presidential "
             "Decree No. 1445, allows a cash advance only for a legally authorized, specific purpose."),
            ("point", "One at a time", "The same section says no new cash advance is given until the "
             "previous one is settled."),
            "COA Circular No. 97-002 sets out the details that offices follow. The study note on "
            "disbursements lists them with the related sections.",
            ("cta", "Read the study note: Disbursements, vouchers, checks and cash advances", "/study-notes/disbursements-vouchers-checks-cash-advances/"),
            ("h", "Who May Receive One"),
            ("point", "Disbursing officers", "Under COA Circular No. 97-002, only permanently appointed "
             "officials may be designated disbursing officers, the people who hold cash advances for "
             "payrolls or petty expenses."),
            ("point", "Elected officials", "They may get cash advances only for official travel."),
            ("point", "No passing it along", "A cash advance may not be transferred from one accountable "
             "officer to another. The person who signed for it answers for it."),
            ("h", "The Deadlines"),
            "Each kind of advance has its own clock under COA Circular No. 97-002:",
            ("point", "Salaries and wages", "Liquidated within 5 days after the end of each pay period."),
            ("point", "Petty operating and field expenses", "Liquidated within 20 days after the end of the "
             "year."),
            ("point", "Local travel", "Within 30 days after returning to the official station."),
            ("point", "Foreign travel", "Within 60 days after returning to the Philippines."),
            ("point", "Year end", "All cash advances are liquidated by the end of the year, and unused "
             "balances are refunded."),
            "Our employee returned from her seminar on March 6. Thirty days later is April 5. The note on her "
            "payslip arrived after that date had passed.",
            ("h", "A Worked Example"),
            ("point", "The advance", "₱5,000 for a three-day seminar in another province."),
            ("point", "The spending", "Fares, meals and registration, supported by receipts, total "
             "₱4,200."),
            ("point", "The liquidation", "A liquidation report showing ₱4,200 in expenses, with the receipts "
             "attached."),
            ("point", "The refund", "The unused ₱800 is returned to the treasury, which issues an official "
             "receipt for it."),
            "The refund matters as much as the receipts. Keeping the balance, even by accident, leaves the "
            "advance open on the books.",
            ("h", "Petty Cash: Small Amounts, Same Discipline"),
            "An office may keep a petty cash fund for small, urgent purchases. Under COA Circular No. 97-002, a "
            "payment from petty cash is capped at ₱15,000 per transaction, and splitting one purchase into "
            "several smaller ones to stay under the cap is not allowed. The custodian replenishes the fund by "
            "accounting for what was spent.",
            ("h", "Why the Rules Are This Strict"),
            "Each rule closes a gap that would otherwise let public money drift.",
            ("point", "One advance at a time", "Without it, a new advance could quietly cover an old one, "
             "and the unaccounted amount would roll forward from trip to trip."),
            ("point", "No transfer between officers", "When the person who signed for the money is the only "
             "one who answers for it, it is clear who must explain a shortage."),
            ("point", "A specific purpose", "An advance “for expenses” cannot be checked. An advance “for "
             "the three-day seminar on March 3 to 5” can."),
            ("point", "Deadlines in days", "Thirty days is short enough that receipts are still in the bag "
             "and memories are fresh."),
            ("h", "What Happens When It Is Late"),
            "Under COA Circular No. 97-002, if a cash advance is not liquidated on time, the officer’s salary "
            "may be withheld, and the officer may face administrative and criminal charges. An unliquidated "
            "advance also blocks the next one, under the one-at-a-time rule.",
            "For the office, an unliquidated advance means money has left the treasury without proof of "
            "how it was used, which is what auditors look for. That brings us back to the payslip note. The "
            "accountant was not being harsh. The rule leaves no room to wait.",
            ("h", "Habits That Make Liquidation Easy"),
            ("point", "Keep one envelope per trip", "Put every receipt in it as you go, and write the date "
             "and purpose on the back of each."),
            ("point", "Ask what counts before you leave", "Ask the accountant which receipts and documents "
             "the liquidation will need, such as a certificate of appearance or attendance from the venue."),
            ("point", "Liquidate in your first week back", "The 30-day clock starts the day you return, "
             "not the day you remember."),
            ("point", "Refund the balance with an official receipt", "And keep a copy of that receipt."),
            ("h", "For Treasury Workers"),
            ("point", "Check before releasing", "Confirm that the person has no open advance, and that the "
             "purpose is specific and authorized."),
            ("point", "Track the due dates", "A simple list of open advances and their deadlines prevents "
             "surprises."),
            ("point", "Explain the clock at release", "Tell the employee the deadline in days and as a date, "
             "when you hand over the money."),
            ("h", "Mistakes to Avoid"),
            ("point", "Treating the advance as personal money", "It is public money until it is "
             "liquidated."),
            ("point", "Lending it to a co-worker", "The advance cannot be transferred, and you remain "
             "accountable for it."),
            ("point", "Losing receipts", "Without them, the expense cannot be supported."),
            ("point", "Forgetting the refund", "The unused balance is returned with an official receipt."),
            ("h", "The Employee’s Envelope"),
            "She found the receipts in her seminar bag, filled out the liquidation report that afternoon, and "
            "refunded ₱800 at the treasury window. Her salary was released on time. Before her next trip, she "
            "bought a box of brown envelopes and labeled the first one with the seminar’s name and the date "
            "30 days after her return.",
            ("h", "Key Takeaways"),
            ("point", "A cash advance is a debt", "It is cleared only by receipts and a refund of the "
             "balance."),
            ("point", "Specific purpose, one at a time", "PD 1445, Section 89, and COA’s rules."),
            ("point", "Know your clock", "Five days for payroll, 30 days after local travel, 60 after "
             "foreign travel."),
            ("point", "Late means consequences", "Salary may be withheld, and charges may follow."),
            ("h", "The Question to Ask"),
            "Do you have a cash advance open right now, and do you know its deadline as a date? If you work "
            "in a treasury, ask your office: how many advances are past due today, and who is following them "
            "up?",
            ("cta", "Read: Inside the Local Treasury, Part 7: From Budget to Check", "/blog/from-budget-to-check/"),
            ("cta", "Read: Inside the Local Treasury, Part 1: Where Your Town's Money Comes From", "/blog/where-your-towns-money-comes-from/"),
            ("cta", "Read: Year-End in the Treasury: What Really Happens in December", "/blog/year-end-in-the-treasury/"),
            ("ask", "What is your system for keeping receipts on an official trip? I'd like to hear what works."),
        ],
    },
    {
        "title": "Inside the Local Treasury, Part 7: From Budget to Check, How a Town Pays Its Bills",
        "date": "January 19, 2027",
        "publish_on": "2027-01-19 21:00",  # blog rotation, one series a day (Butch 2026-11-14)
        "slug": "from-budget-to-check",
        "category": "finance",
        "summary": "Why does a supplier wait weeks for a check after delivering the goods? Follow one payment "
                   "from the budget to the check, through three certifications, an approval and two "
                   "signatures, and see what each one protects.",
        "body": [
            "A supplier of office chairs stood at the treasury window with a delivery receipt in one hand and "
            "his phone in the other. “The chairs were delivered two weeks ago,” he said. “They are already "
            "being used. Why is there still no check?” The clerk opened a folder and showed him where his "
            "voucher was: on a desk two offices away, waiting for one more signature.",
            "(This case, like every case in this series, is a composite. No real supplier, office or amount is "
            "described.)",
            "To someone outside, the wait looks like red tape. Inside, every signature on that voucher answers "
            "a question the law requires someone to ask before public money leaves the treasury. This post "
            "explains each step from the budget to the check, who signs at each one, what the signature "
            "means, and what a supplier, an employee or a resident can do to keep a payment moving.",
            ("photo", "blog/finance-budget-to-check.jpg", "From budget to check: an appropriation, an "
             "obligation, a voucher, and a check with two signatures. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "Rule One: No Appropriation, No Payment"),
            "Section 305 of the Local Government Code sets the first principle: no money is paid out of the "
            "local treasury except under an appropriation ordinance or law. The annual budget, passed by the "
            "sanggunian, is that ordinance. It lists how much each office may spend, and on what.",
            "Section 336 adds that appropriated funds are used only for the purpose they were appropriated "
            "for. Money set aside for office equipment cannot quietly pay for a fiesta. If a need was not in "
            "the budget, the sanggunian has to act first.",
            ("quote", "The budget is not a wish list. It is the permission slip for every peso that leaves."),
            ("h", "Rule Two: Deliver First, Then Get Paid"),
            "Section 338 says no money is paid on a contract under which no services were rendered or goods "
            "delivered. The chairs had to arrive, and the office had to confirm they matched what was ordered, "
            "before any payment could begin.",
            "That is the reason for the delivery receipt in the supplier’s hand. It is the first document in "
            "his payment folder, not the last.",
            ("h", "Three Certifications and an Approval"),
            "Section 344 is the heart of the process. No money may be disbursed unless three officers have "
            "each certified their part:",
            ("point", "The budget officer", "Certifies that an appropriation exists for the purpose. "
             "Question answered: is this expense in the budget?"),
            ("point", "The accountant", "Obligates the appropriation, setting the amount aside so it cannot "
             "be spent twice. Question answered: is the money reserved for this claim?"),
            ("point", "The treasurer", "Certifies that funds are available. Question answered: is there "
             "cash to pay it?"),
            "Section 344 then requires the head of the office with control of the fund to certify the voucher "
            "or payroll as to the validity, propriety and legality of the claim. In the supplier’s case, that "
            "was the head of the office that ordered the chairs.",
            "Finally, the local chief executive approves the voucher. The same section exempts regularly "
            "recurring administrative expenses, such as payrolls for regular employees, light, water and "
            "telephone bills, and remittances to government creditors like the GSIS and SSS. Those do not need "
            "the mayor’s own signature on each voucher.",
            "The study note on disbursements lists these rules with their section numbers and a worked "
            "example.",
            ("cta", "Read the study note: Disbursements, vouchers, checks and cash advances", "/study-notes/disbursements-vouchers-checks-cash-advances/"),
            ("h", "Two Signatures on the Check"),
            "Under Section 345, checks are drawn by the local treasurer and countersigned by the local "
            "administrator. If either is temporarily absent or incapacitated, the duty passes to their "
            "immediate assistant.",
            "Two signatures mean no single person can both prepare and release a payment. The same idea runs "
            "through the whole process: the person who asks for the money, the person who checks the budget, "
            "the person who reserves it, the person who confirms the cash and the person who approves are meant to be different people.",
            ("h", "A Limit on Spending Ahead of Collections"),
            "A treasurer cannot pay everything in the budget just because it was approved. Section 337 limits "
            "total disbursements from a fund to its actual collections plus 50% of its estimated revenue not "
            "yet collected.",
            ("point", "An example", "A fund expects ₱100 million this year and has collected ₱60 million. "
             "The limit is ₱60 million + 50% × ₱40 million = ₱80 million."),
            ("point", "At year end", "Section 337 allows no cash overdraft in any fund at the end of the "
             "year."),
            "This is one reason payments are sometimes scheduled rather than released the day a voucher is "
            "complete. The treasurer’s certification of available funds has to be true when it is signed.",
            ("h", "Why Each Signature Is Taken Seriously"),
            "Signing is not a formality, because the law attaches liability to it. Under Section 342, an "
            "accountable officer who follows a superior’s order to make an illegal payment is not relieved of "
            "liability unless they object in writing, and the superior who gave the order is jointly and "
            "severally liable.",
            "So when a treasurer asks for a missing document, it is not stubbornness. It is the officer making "
            "sure that the certification they sign is true.",
            ("h", "Where Payments Get Stuck"),
            "The supplier’s voucher was not lost. It was waiting, and the reasons for waiting fall into a few "
            "kinds.",
            ("point", "A missing document", "A delivery receipt without the inspection report, or a "
             "contract without the purchase order."),
            ("point", "An absent signatory", "Section 345 lets an immediate assistant sign checks, and "
             "Section 344 has a rule for a department head’s next-in-rank, but someone still has to be there to sign."),
            ("point", "No obligation yet", "The accountant cannot obligate an amount that the budget officer "
             "has not certified."),
            ("point", "Cash timing", "The Section 337 limit, or simply waiting for collections to come in."),
            ("h", "What a Supplier or Employee Can Do"),
            ("point", "Submit complete papers", "Ask the ordering office for its list of required documents "
             "before delivery, not after."),
            ("point", "Ask where the voucher is", "A polite question at each office, such as “Which "
             "signature is still missing?”, moves a voucher faster than a complaint."),
            ("point", "Keep copies", "Keep the delivery receipt, the invoice and any acknowledgment of the "
             "documents you submitted."),
            ("h", "What a Resident Can Check"),
            "Payments are public money, and some of the trail is public too. Section 352 requires the treasurer "
            "to post, within 30 days after the year ends, a summary of all revenues collected and funds "
            "received, and of the appropriations and disbursements, in at least three public places. Ask your "
            "town where it is posted, and read it.",
            ("h", "For Treasury Workers"),
            ("point", "Check before you certify", "Your certification of available funds is a statement of "
             "fact. Confirm the balance, not just the paper."),
            ("point", "Put objections in writing", "Section 342 protects the officer who registers an "
             "objection in writing."),
            ("point", "Explain the step, not just the rule", "A supplier told “we need the inspection report "
             "from the requesting office” knows where to go. One told “incomplete” does not."),
            ("h", "Mistakes to Avoid"),
            ("point", "Delivering before the order is final", "Without an obligation, there is no money "
             "reserved for you."),
            ("point", "Assuming approval means cash", "An approved budget is permission, not money in the "
             "bank."),
            ("point", "Skipping a signature to save time", "A skipped step can become an audit finding later."),
            ("point", "Asking the treasurer to “just release it”", "The treasurer cannot certify what is "
             "not yet true."),
            ("h", "The Supplier’s Check"),
            "The missing signature was the head of the office that ordered the chairs, who had been on leave. "
            "The next-in-rank officer signed the next morning, and the check, signed by the treasurer and "
            "countersigned by the administrator, was ready three days later. The supplier left with a list of "
            "documents for his next delivery.",
            ("h", "Key Takeaways"),
            ("point", "No appropriation, no payment", "Section 305 ties every peso to the budget."),
            ("point", "Three certifications", "Budget officer, accountant and treasurer, then the head of "
             "office and the approving authority (Section 344)."),
            ("point", "Two signatures on the check", "Treasurer and administrator (Section 345)."),
            ("point", "Signatures carry liability", "That is why missing papers stop a payment."),
            ("h", "The Question to Ask"),
            "Have you ever waited for a check from your town? Which signature was missing? If you work in a "
            "treasury, ask your office: how long does a complete voucher take to become a check, and where "
            "does it wait the longest?",
            ("cta", "Read: Inside the Local Treasury, Part 1: Where Your Town's Money Comes From", "/blog/where-your-towns-money-comes-from/"),
            ("cta", "Read: Inside the Local Treasury, Part 6: Can the Town Forgive a Tax?", "/blog/can-the-town-forgive-a-tax/"),
            ("cta", "Read: Inside the Local Treasury, Part 5: Unpaid Amilyar, From Notice to Auction", "/blog/unpaid-amilyar-notice-to-auction/"),
            ("ask", "Have you ever waited for a government check? I'd like to hear what held it up."),
        ],
    },
    {
        "title": "Inside the Local Treasury, Part 6: Can the Town Forgive a Tax?",
        "date": "January 14, 2027",
        "publish_on": "2027-01-14 21:00",  # blog rotation, one series a day (Butch 2026-11-14)
        "slug": "can-the-town-forgive-a-tax",
        "category": "finance",
        "summary": "After a typhoon or a bad harvest, people ask whether the town can forgive their real property "
                   "tax. Here is what the law allows a sanggunian and the President to do, what the 2024 national "
                   "amnesty covered, and what it did not.",
        "body": [
            "Two weeks after a typhoon flattened the rice fields, a barangay captain sat across from the "
            "treasurer with a folded letter from his farmers. The typhoon had taken the harvest that paid their bills. “They are asking if the town can forgive this year’s amilyar,” he said. “Can it?”",
            "(As in every part of this series, the case is a composite. No real person, place or amount is "
            "described.)",
            "The honest answer is “sometimes, and only in the ways the law allows.” When you finish reading, you will know who can reduce or forgive real property tax, under what conditions, what the 2024 national "
            "amnesty under Republic Act No. 12001 covered and who it left out, and how to tell real relief from "
            "a rumor at the window.",
            ("photo", "blog/finance-tax-relief.jpg", "Four kinds of relief: calamity condonation, the President’s "
             "power, the 2024 amnesty, and the 6% cap. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Why a Treasurer Cannot Simply Say Yes"),
            "A treasurer collects what the law and the local revenue code say is due. The treasurer does not set "
            "taxes and cannot waive them on a kind heart. Forgiving a tax is a policy decision, and the Local "
            "Government Code gives that decision to specific people, with specific limits.",
            "That matters for taxpayers too. A discount promised verbally at the window, with no ordinance or law "
            "behind it, protects nobody. When auditors review the collections, any tax left uncollected has to rest on a legal basis.",
            ("quote", "Relief is real only when it is written in an ordinance or a law."),
            ("h", "The General Power: Section 192"),
            "Section 192 of the Code says local government units “may, through ordinances duly approved, grant "
            "tax exemptions, incentives or reliefs under such terms and conditions as they may deem necessary.”",
            "The key words are “through ordinances.” Relief comes from the sanggunian, passed and approved like "
            "any other ordinance, and it reaches only the taxes that local government levies.",
            ("h", "Relief After a Calamity: Section 276"),
            "For the real property tax, Section 276 is more specific. After a general failure of crops, a "
            "substantial drop in the prices of agricultural or agri-based products, or a calamity, the "
            "sanggunian may condone or reduce, wholly or partly, the tax and interest for the following year or "
            "years in the areas affected.",
            "Two details stand out:",
            ("point", "It must be done by ordinance", "The sanggunian acts, not the treasurer or the mayor "
             "alone."),
            ("point", "It must be passed before January 1", "The ordinance is passed before the first day of "
             "January of the year it covers. Relief is planned for the coming year, not granted retroactively "
             "at the window."),
            "For the barangay captain, this was the realistic path. If the council passed an ordinance before "
            "January 1, the farmers’ tax for the next year could be reduced or condoned. This year’s bill, "
            "already due, was a different matter.",
            ("h", "When the President Steps In: Section 277"),
            "Section 277 gives the President the power to condone or reduce the real property tax and its interest when the public interest requires it.",
            "This is a national power. It is not something a resident can apply for at the treasury, and "
            "an owner should not delay payment hoping for it.",
            ("h", "A Real Example of Local Relief"),
            "After Typhoon Santi in 2013, the Inquirer reported that Cabanatuan City’s council passed an ordinance "
            "condoning interest and penalties on unpaid real property tax for 2013 and earlier years. Public "
            "auctions of delinquent properties were halted for the period, and properties involved in court "
            "cases over the tax were not covered.",
            "Notice what was forgiven: the interest and penalties, not the tax itself. Owners still paid what "
            "they owed. That pattern repeats in the national amnesty below.",
            ("h", "The 2024 National Amnesty: RA 12001, Section 30"),
            "Republic Act No. 12001, the Real Property Valuation and Assessment Reform Act, was approved on June "
            "13, 2024. Its Section 30 granted a real property tax amnesty that “shall cover penalties, "
            "surcharges, and interests from all unpaid real property taxes, including Special Education Fund, "
            "idle land tax, and other special levy taxes, prior to the effectivity of this Act.”",
            ("point", "What owners still paid", "The tax itself. Section 30 allowed “one-time payment or "
             "installment payment of the delinquent real property taxes.”"),
            ("point", "The deadline", "The amnesty could “only be availed within a period of two (2) years "
             "after the effectivity of this Act.”"),
            ("point", "When the law took effect", "Section 39 made it effective 15 days after publication. "
             "The amnesty window ran from July 2024 and closed in July 2026."),
            "Section 30 also listed three kinds of property the amnesty did not cover:",
            ("point", "(a) Already auctioned", "“Delinquent real properties which have been disposed of at "
             "public auction to satisfy the real property tax delinquencies.”"),
            ("point", "(b) Under a compromise", "“Real properties with tax delinquencies which are being paid "
             "pursuant to a compromise agreement.”"),
            ("point", "(c) In court", "“Real properties subject of pending cases in court for real property "
             "tax delinquencies.”"),
            "An owner reading this in 2027 should treat Section 30 as history. Any relief today has to come "
            "from a newer law or a local ordinance, and the treasury can say whether one exists.",
            ("h", "A Different Kind of Relief: The 6% Cap"),
            "RA 12001 also requires local governments to update their schedules of market values, the basis of "
            "the real property tax. New values can mean higher bills. Section 29 softens the first step: for the "
            "first year a new schedule takes effect, “any increase in real property taxes shall be limited to a "
            "maximum of six percent (6%)” of the taxes assessed before the law took effect.",
            "The cap applies to each type of real property tax, including the Special Education Fund and idle "
            "land tax. For the years after, Section 29 adds that the local government “may enact an ordinance to "
            "impose a cap on the increase.” Whether your town did so is a question for your sanggunian.",
            ("point", "An example", "A lot taxed ₱2,400 a year before the law can be billed at most ₱2,544 in "
             "the first year of the new schedule, an increase of ₱144."),
            ("h", "Is Amnesty Fair?"),
            "Amnesties raise a fair question. The owner who paid on time, every year, gets nothing, while the one "
            "who waited is spared the interest. Supporters answer that an amnesty brings in money that might "
            "never be collected, and puts properties back on the paying rolls.",
            "Both points deserve weight. That is one reason the law sets limits, such as the deadline and the "
            "exclusions in Section 30. Relief is meant to be a door that opens once and closes, not a habit.",
            ("h", "Mistakes to Avoid"),
            ("point", "Waiting for an amnesty", "Interest under Section 255 keeps running at 2% a month, for up to 36 months, while you wait, and no relief is promised until an ordinance or law says so."),
            ("point", "Thinking amnesty erases the tax", "Under RA 12001, only penalties, surcharges and "
             "interest were forgiven. The tax was still paid."),
            ("point", "Trusting a verbal promise", "Ask for the ordinance number or the law. If there is none, "
             "there is no relief."),
            ("point", "Assuming auctioned land is covered", "Section 30 excluded properties already sold at "
             "auction for unpaid tax."),
            ("h", "An Action Plan"),
            ("point", "After a calamity", "Write to your barangay captain or councilor early, before "
             "December, since a Section 276 ordinance must pass before January 1."),
            ("point", "If you have arrears", "Ask the treasury for a statement of account and whether any "
             "ordinance currently grants relief, with its number."),
            ("point", "If your bill rose", "Ask whether a new schedule of market values took effect, and "
             "whether the 6% first-year cap was applied."),
            ("point", "Keep the papers", "Keep the official receipts and a copy of any ordinance you relied "
             "on."),
            ("h", "The Captain’s Letter"),
            "The treasurer explained the rules, and the captain took the letter to the sanggunian instead. In "
            "December, the council debated an ordinance reducing the next year’s tax in the barangays the "
            "typhoon hit. The farmers paid this year’s bill in installments, and the captain posted a copy of "
            "the ordinance on the barangay board when it passed.",
            ("h", "Key Takeaways"),
            ("point", "Only an ordinance or a law can forgive a tax", "Not the treasurer, and not a promise "
             "at the window."),
            ("point", "Section 276 is for calamities", "The sanggunian may condone or reduce the next year’s "
             "tax by an ordinance passed before January 1."),
            ("point", "RA 12001’s amnesty has closed", "It forgave penalties, surcharges and interest, not "
             "the tax, and it could be availed only until July 2026."),
            ("point", "The 6% cap still matters", "It limits the first-year increase when a new schedule of "
             "market values takes effect."),
            ("h", "The Question to Ask"),
            "Do you know whether your town has any tax relief ordinance in force today? If you work in a "
            "treasury, ask your office: when a calamity hits, who drafts the Section 276 ordinance, and by when?",
            ("cta", "Read: Inside the Local Treasury, Part 5: Unpaid Amilyar, From Notice to Auction", "/blog/unpaid-amilyar-notice-to-auction/"),
            ("cta", "Read the study note: Paying real property tax", "/study-notes/paying-real-property-tax/"),
            ("cta", "Read the study note: Real property tax basics", "/study-notes/real-property-tax-basics/"),
            ("cta", "Read: Inside the Local Treasury, Part 1: Where Your Town's Money Comes From", "/blog/where-your-towns-money-comes-from/"),
            ("ask", "Has your town ever granted tax relief after a calamity? I'd like to hear how it worked."),
        ],
    },
    {
        "title": "Inside the Local Treasury, Part 5: Unpaid Amilyar, From Notice to Auction",
        "date": "January 9, 2027",
        "publish_on": "2027-01-09 21:00",  # blog rotation, one series a day (Butch 2026-11-14)
        "slug": "unpaid-amilyar-notice-to-auction",
        "category": "finance",
        "summary": "Real property tax left unpaid does not simply disappear. Here is how interest grows, what a "
                   "notice of delinquency means, how a warrant of levy and an auction work, and the one year an "
                   "owner has to get the property back.",
        "body": [
            "A man home from work abroad walked into the treasury with his phone held out. On the screen was a "
            "photo his cousin had taken at the barangay hall: a list of names posted on the board, under the "
            "words “Notice of Delinquency.” His late father’s name was on it. “Papa paid the amilyar every year,” "
            "he said. “At least, I thought he did.”",
            "(As in every part of this series, the case is a composite. No real person, property or amount is "
            "described.)",
            "Amilyar is the everyday name for the real property tax on land and buildings. It is due every "
            "year, and when it goes unpaid, the Local Government Code lays out a series of steps that can end "
            "with the property sold at public auction. Read to the end and you will know how the unpaid "
            "tax grows, what each step from notice to auction means, how much time an owner has at each stage, "
            "and how to stop the process before it goes too far.",
            ("photo", "blog/finance-rpt-delinquency.jpg", "From unpaid tax to auction: the notice, the warrant of "
             "levy, the sale, and the one year to redeem. (Illustration: Butch Mahinay, aumahinay.dev)",
             "medium"),
            ("h", "The Tax Is Tied to the Land"),
            "Under Section 246 of the Code, the real property tax for a year accrues on January 1, and from that "
            "day it is a lien on the property. A lien is a legal claim. This one is superior to other liens and "
            "encumbrances, and it stays with the property until the tax is paid, even if the property changes "
            "hands.",
            "That is why the son’s problem did not die with his father. The unpaid tax stayed attached to the lot, "
            "and anyone who inherits or buys it inherits the problem with it.",
            ("quote", "The tax does not follow the owner. It stays with the land."),
            ("h", "How the Bill Grows"),
            "Section 250 lets owners pay the basic tax and the Special Education Fund in four installments, due "
            "by March 31, June 30, September 30 and December 31. An installment not paid on time earns interest "
            "under Section 255: 2% a month on the unpaid amount, until it is paid. The interest stops growing "
            "after 36 months, so the most it can reach is 72% of the unpaid tax.",
            "Here is what that looks like for a lot whose basic tax and Special Education Fund add up to ₱2,400 "
            "a year:",
            ("point", "One year’s tax, 12 months late", "2% × 12 = 24% interest, or ₱576. The bill becomes "
             "₱2,976."),
            ("point", "The same tax, 36 months or more late", "The cap of 72% applies, or ₱1,728. The bill "
             "becomes ₱4,128."),
            ("point", "Three years unpaid", "Each year’s tax carries its own interest, counted from its own due "
             "dates, so the arrears pile up year after year."),
            "Section 250 adds a rule that can surprise owners. A payment is applied first to the unpaid tax, "
            "interest and penalties of earlier years. An owner cannot choose to pay only this year’s tax and "
            "leave the old years for later.",
            "The study note on paying real property tax walks through quarterly payments, discounts and "
            "interest with worked examples.",
            ("cta", "Read the study note: Paying real property tax", "/study-notes/paying-real-property-tax/"),
            ("h", "Step 1: The Notice of Delinquency"),
            "When the tax becomes delinquent, Section 254 requires the treasurer to post a notice at the main "
            "entrance of the provincial capitol or the city or municipal hall, and in a public place in each "
            "barangay. The notice is also published once a week for two weeks in a newspaper of general "
            "circulation in the area.",
            "This is the list the son’s cousin had photographed. It is a public warning, and it is the clearest "
            "moment to act, because nothing has been levied yet and the owner can still settle at the window.",
            ("h", "Step 2: The Warrant of Levy"),
            "Section 256 gives the local government two remedies for unpaid real property tax: an administrative "
            "action through levy on the property, and a court case. It may use one or both.",
            "For the levy, Section 258 has the treasurer issue a warrant of levy, which has the force of a court "
            "order of execution. The warrant is mailed to or served on the owner, and the levy is annotated on the tax "
            "declaration and the title. From then on, anyone who checks the title sees it.",
            "The law also puts pressure on the treasurer. Under Section 259, a treasurer who fails to issue or "
            "execute the warrant within one year from the time the tax became delinquent may be dismissed from "
            "the service. Collecting unpaid real property tax is a duty, not a "
            "favor.",
            ("h", "Step 3: The Auction"),
            "Section 260 sets the timetable. Within 30 days after the warrant is served, the treasurer advertises "
            "the sale of the property. The notice is posted at the main entrance of the government building and "
            "in a public place in the barangay where the property is, and published once a week for two weeks.",
            "Even then, the owner can stop it. At any time before the date fixed for the sale, the owner may pay "
            "the delinquent tax, the interest and the expenses, and the sale does not go ahead.",
            "Section 263 covers the case where nobody bids, or the highest bid does not cover the tax, interest "
            "and expenses. The treasurer then buys the property for the local government. The owner can still "
            "redeem it within one year.",
            ("h", "Step 4: One Year to Redeem"),
            "A sale is not the end. Under Section 261, the owner has one year from the date of sale to redeem "
            "the property. To do so, the owner pays the delinquent tax with its interest, the expenses of the "
            "sale, and interest of up to 2% a month on the price the buyer paid, counted from the sale to the "
            "redemption.",
            "During that year, the owner keeps possession of the property and the right to its rent and "
            "other income. But the year is the limit the law sets. After it, the right to redeem under "
            "Section 261 is gone.",
            ("h", "Is There a Time Limit on Collection?"),
            "Yes. Section 270 says the tax must be collected within five years from the date it became due, or "
            "within ten years from discovery when there was fraud or intent to evade. The period stops running "
            "in some cases, such as when the owner is out of the country or cannot be located.",
            "That limit is not a reason to wait. The lien under Section 246 remains on the property, and an owner "
            "who wants to sell, mortgage or transfer it will still be asked to show that the tax is paid.",
            ("h", "What About the Amnesty?"),
            "Republic Act No. 12001, signed on June 13, 2024, included a one-time amnesty under Section 30. It "
            "covered “penalties, surcharges, and interests from all unpaid real property taxes” due before the "
            "law took effect, but only if availed “within a period of two (2) years after the effectivity of "
            "this Act.” The tax itself was still paid, either at once or by installment.",
            "Counting from the law’s effectivity in July 2024, that window closed in July 2026. An owner reading "
            "this today should ask the treasury whether any newer local relief applies, and should not assume "
            "one does.",
            ("h", "Mistakes to Avoid"),
            ("point", "Assuming someone else paid", "A tax declaration can stay in the name of a parent who "
             "has passed away. Ask for a statement of account instead of relying on memory."),
            ("point", "Paying only the current year", "Section 250 applies payments to older arrears first, so "
             "a payment meant for this year may go to past years."),
            ("point", "Ignoring the posted notice", "The notice of delinquency is the stage where settling is "
             "simplest. Later stages add expenses and annotations on the title."),
            ("point", "Treating the auction as final", "There is still a year to redeem under Section 261, "
             "but it is a firm limit."),
            ("h", "An Action Plan"),
            ("point", "This week", "Ask the treasury for a statement of account on every property in your "
             "family, by tax declaration number."),
            ("point", "If there are arrears", "Ask what the total is today, how it is computed, and whether "
             "payment by installment is allowed under your local revenue code."),
            ("point", "If you disagree with the amount", "Section 252 lets you pay under protest and file a "
             "written protest within 30 days of payment."),
            ("point", "Every year after", "Pay by March 31 if you can, and keep the official receipts together "
             "with the tax declaration."),
            ("h", "The Son’s Lot"),
            "The son asked for a statement of account, and the arrears covered all of the previous year. No warrant had been issued yet, so he paid in full at the window, then went to the assessor to start transferring the tax declaration to the "
            "heirs. On his way out, he took a photo of the receipt and sent it to his cousin. “Tell me if our name "
            "is ever on that board again,” he wrote.",
            ("h", "Key Takeaways"),
            ("point", "The tax is a lien", "It stays with the property until paid, even after the owner dies "
             "or the land is sold."),
            ("point", "Interest is 2% a month", "It is capped at 36 months, or 72% of the unpaid tax."),
            ("point", "Notice, levy, auction", "Each step is set by law, and the owner can stop the sale by "
             "paying before the auction date."),
            ("point", "One year to redeem", "After a sale, the owner keeps possession for a year and can get "
             "the property back by paying."),
            ("h", "The Question to Ask"),
            "When did you last see an official receipt for the amilyar on your family’s land? If you work in a "
            "treasury, ask your office: how long does it take us to move from a posted notice to a warrant?",
            ("cta", "Read the study note: Real property tax basics", "/study-notes/real-property-tax-basics/"),
            ("cta", "Read: Inside the Local Treasury, Part 4: Selling Land? Meet the Transfer Tax", "/blog/selling-land-transfer-tax/"),
            ("cta", "Read: Inside the Local Treasury, Part 1: Where Your Town's Money Comes From", "/blog/where-your-towns-money-comes-from/"),
            ("cta", "Read: Inside the Local Treasury, Part 2: The January Rush and Your Business Permit", "/blog/january-rush-business-permit/"),
            ("ask", "Has your family ever found an unpaid amilyar years after the fact? I'd like to hear how it was settled."),
        ],
    },
    {
        "title": "Inside the Local Treasury, Part 4: Selling Land? Meet the Transfer Tax",
        "date": "January 4, 2027",
        "publish_on": "2027-01-04 21:00",
        "slug": "selling-land-transfer-tax",
        "category": "finance",
        "summary": "Before a sale or donation of land can be registered, a local tax must be paid at the treasury. Here is what the tax on transfer of real property is, who must pay it, how "
                   "it is computed, the 60-day clock, and why the Register of Deeds will not move without "
                   "the receipt.",
        "body": [
            "A retired teacher came to the treasury window with a brown envelope and a question. Months "
            "earlier, she had sold a small lot to a neighbor. The deed was signed and notarized, the money "
            "was paid, and everyone shook hands. Now the buyer was at the Register of Deeds, and the clerk "
            "there had sent him back. “They need proof that the transfer tax was paid,” she said. “What "
            "transfer tax?”",
            "(As in every part of this series, the case is a composite. No real person, property or amount "
            "is described.)",
            "A land sale can be done in good faith, with a notarized deed, and still stall at this step: a local tax that one of the parties did not know about. "
            "Stay with me to the end, and you will know what the tax on transfer of real property ownership is, "
            "who the law says must pay it, how to compute it, how long you have, what being late costs, and "
            "what to bring to the window.",
            ("photo", "blog/finance-transfer-tax.jpg", "The transfer tax: who pays, how much, within 60 days, "
             "and the receipt the Register of Deeds needs. (Illustration: Butch Mahinay, aumahinay.dev)",
             "medium"),
            ("h", "What the Law Says"),
            "The tax comes from Section 135 of the Local Government Code. It allows a province to impose a "
            "tax on the sale, donation, barter or any other way of transferring ownership or title of real "
            "property.",
            ("point", "Who levies it", "It is a provincial tax. For land in a municipality, it belongs to "
             "the province. A city may levy it itself, and under Section 151 a city’s rate may be up to 50% "
             "higher than the provincial limit."),
            ("point", "The rate", "At most 50% of 1% of the total consideration, or of the fair market "
             "value when the money involved is not substantial, whichever is higher. In a city, the limit "
             "is up to 0.75%."),
            ("point", "The exemption", "Section 135 exempts transfers made under the Comprehensive Agrarian "
             "Reform Law, Republic Act No. 6657."),
            "Each province or city sets its actual rate in its own revenue code, so the limit in the Code is "
            "a ceiling, not a guarantee of what your bill will be.",
            ("h", "Who Must Pay"),
            "Section 135 names the person responsible: the seller, donor, transferor, executor or "
            "administrator. In our case, that is the retired teacher, not her neighbor.",
            "Buyers and sellers can agree between themselves that the buyer will shoulder the tax, and some "
            "deeds say so. That agreement settles who hands over the money. It does not change the fact that "
            "the title will not move until the tax is paid, which is why the buyer was the one sent back.",
            ("quote", "The deed changes hands in a day. The title changes hands only after the taxes are paid."),
            ("h", "How Much: Two Examples"),
            "Here is how the tax looks at the maximum provincial rate. Your province’s revenue code may set "
            "a lower one.",
            ("point", "A sale for ₱1,200,000", "The fair market value on the tax declaration is ₱1,000,000. "
             "The price is higher, so the tax is computed on the price: 0.5% × ₱1,200,000 = ₱6,000."),
            ("point", "A donation to a daughter", "No money changes hands, so the fair market value is used: "
             "0.5% × ₱1,000,000 = ₱5,000."),
            ("point", "The same sale in a city", "At the city limit of 0.75%, the tax on ₱1,200,000 could "
             "reach ₱9,000."),
            "The study note on sources of local revenue shows where this tax sits among the other taxes a "
            "province, city and municipality may levy.",
            ("cta", "Read the study note: Sources of local revenue", "/study-notes/sources-of-local-revenue/"),
            ("h", "The 60-Day Clock"),
            "Section 135 says the tax must be paid within 60 days from the date the deed was executed, or, "
            "when the transfer comes from a death, from the date of death.",
            "Sixty days is about two months, and it starts on the day the deed is signed, not on the day "
            "anyone remembers the tax. In our case, the teacher signed in early March and came to the window in October, about five months after the deadline.",
            ("h", "What Being Late Costs"),
            "Section 168 of the Code allows a surcharge of up to 25% of the unpaid tax, plus interest of up to "
            "2% a month on the unpaid tax and surcharge, for no more than 36 months. The province’s revenue "
            "code sets the actual rates.",
            ("point", "The tax", "₱6,000 on the ₱1,200,000 sale."),
            ("point", "The surcharge", "Up to 25% × ₱6,000 = ₱1,500."),
            ("point", "Interest", "Up to 2% a month on ₱7,500, or up to ₱150 for each month late."),
            "Five months late, the bill could reach ₱6,000 + ₱1,500 + ₱750 = ₱8,250 at the maximum rates. "
            "Paid on time, it would have been ₱6,000.",
            ("h", "Why the Register of Deeds Sent the Buyer Back"),
            "Section 135 makes payment a condition for the next steps. The Register of Deeds may not register "
            "the deed until the provincial or city treasurer has certified that the tax was paid. The "
            "assessor applies the same rule before cancelling the old tax declaration and issuing a new one "
            "in the buyer’s name.",
            "That is why an unpaid transfer tax quietly blocks everything. The buyer cannot get a title in "
            "his name, cannot declare the property for real property tax under his name, and may find it "
            "hard to sell or mortgage the land later.",
            ("h", "The Notary’s Part"),
            "The same section gives notaries public a duty too. A notary who notarizes a deed transferring "
            "real property must give a copy to the provincial treasurer, or the city treasurer, within 30 "
            "days. This lets the treasury know a transfer happened, even when the parties forget to come in.",
            ("h", "What to Bring"),
            "Each treasury sets its own list, so call first. Expect to be asked for these:",
            ("point", "The notarized deed", "The deed of sale, donation or exchange, with copies."),
            ("point", "The latest tax declaration", "It shows the property’s fair market value and the "
             "assessed owner."),
            ("point", "Proof that real property tax is paid", "Some offices ask for a certificate or the latest official receipt to show the property has no unpaid tax."),
            ("point", "IDs of the parties", "And, for an estate, the papers showing who represents it."),
            "National taxes are a separate track. The Bureau of Internal Revenue handles its own taxes on the "
            "transfer and issues a Certificate Authorizing Registration. Ask the BIR office that covers the "
            "property what it requires.",
            ("h", "For Treasury Workers"),
            "The transfer tax is easy to collect and easy to miss. Three habits help.",
            ("point", "Use the notaries’ copies", "Match the deeds notaries send in against the payments "
             "received. A deed with no payment after 60 days is a reminder letter waiting to be written."),
            ("point", "Check the base", "Compare the price in the deed with the fair market value on the tax "
             "declaration, and apply the rule in the revenue code consistently."),
            ("point", "Explain the deadline at the counter", "A taxpayer who learns about the 60 days on day "
             "59 is grateful. One who learns on day 150 is not."),
            ("h", "The Teacher’s Lot"),
            "The teacher paid the tax with the surcharge and interest, and the buyer finally registered the "
            "deed. On her way out, she asked the clerk to write the 60-day rule on the back of her receipt. "
            "“My brother is selling his lot next year,” she said. “He will not wait five months.”",
            ("h", "Key Takeaways"),
            ("point", "It is a provincial or city tax", "Up to 0.5% in a province, up to 0.75% in a city, on "
             "the higher of the price or fair market value."),
            ("point", "The law names the seller", "Or the donor, transferor, executor or administrator, whatever the parties agree between themselves."),
            ("point", "Sixty days", "From the signing of the deed, or from the date of death."),
            ("point", "No receipt, no transfer", "The Register of Deeds and the assessor need proof of "
             "payment first."),
            ("h", "The Question to Ask"),
            "If you have signed a deed in the last two months, has the transfer tax been paid? If you work in "
            "a treasury, ask your office: do we follow up the deeds the notaries send us?",
            ("cta", "Read: Inside the Local Treasury, Part 1: Where Your Town's Money Comes From", "/blog/where-your-towns-money-comes-from/"),
            ("cta", "Read: Inside the Local Treasury, Part 2: The January Rush and Your Business Permit", "/blog/january-rush-business-permit/"),
            ("cta", "Read: Inside the Local Treasury, Part 3: The Cedula", "/blog/the-cedula-explained/"),
            ("ask", "Have you ever had a land transfer stall at the Register of Deeds? I'd like to hear what held it up."),
        ],
    },
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
            "It is a fair question, and the answer goes back almost a century and a half. By the end of this post, you will know where the cedula came from, how to compute what you "
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
            " tax, and the paper is the community tax certificate, but people still call it the "
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
            "the other side, the community tax is steady local income, and a barangay's share of "
            "what is collected there is money it can count on every January.",
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
            "deadline, knowing what you are paying for, and bringing the right papers. When you finish reading, you will know the real deadline, what being late costs in pesos, what"
            " to bring, and what to do if you believe the bill is wrong.",
            ("h", "Why Everything Happens in January"),
            "The local business tax is a yearly tax, and under the Local Government Code it "
            "becomes due on the first day of the year. It is paid within the first 20 days of "
            "January. An owner who prefers to pay by quarter can do that too, with each "
            "installment due within the first 20 days of its quarter.",
            "So the real deadline is January 20, not January 31. Because renewals for the whole "
            "town fall due in the same twenty days, the line is longest in the last few days "
            "before the 20th.",
            "The tax is computed on what the business sold the year before. That is why the "
            "treasury asks for last year’s gross sales or receipts at renewal. My study note on "
            "business tax and the mayor’s permit walks through the rates and rules in detail.",
            ("cta",
             "Read the study note: Business tax and the mayor's permit",
             "/study-notes/business-tax-and-mayors-permit/"),
            ("h", "Two Payments, One Visit"),
            "Renewal involves two different payments, and it helps to keep them apart:",
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
            " actually comes from. After this post, you will be able to read the one "
            "ratio that explains much of the answer, see why the national share can fall without "
            "warning, and know what actually raises a town's own income.",
            "(The cases in this series are composites, not records of any real office. Names, "
            "places and amounts are changed or left out.)",
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
            "invented.",
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
            "Raising local income does not have to mean a new tax. It can come from doing the basics well:",
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
