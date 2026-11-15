"""Public Finance series (Butch 2026-11-11), "Inside the Local Treasury"; dates follow the daily blog rotation (Butch 2026-11-14).

Each post takes a typical treasury situation and explains it in plain words. Cases are composites:
no real taxpayer, employee, office or amount is named. Facts are checked against official sources
before each post is approved; per Butch, the posts themselves show no Sources section.
"""

TREASURY_POSTS = [
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
            "The honest answer is “sometimes, and only in the ways the law allows.” By the end of this post, you "
            "will know who can reduce or forgive real property tax, under what conditions, what the 2024 national "
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
            "Section 277 gives the President the power to condone or reduce the real property tax and its "
            "interest, for any year, in any province or city, or a municipality within Metro Manila, when the "
            "public interest requires it.",
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
            ("point", "Waiting for an amnesty", "Interest under Section 255 keeps running at 2% a month while "
             "you wait, and no relief is promised until an ordinance or law says so."),
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
            "with the property sold at public auction. By the end of this post, you will know how the unpaid "
            "tax grows, what each step from notice to auction means, how much time an owner has at each stage, "
            "and how to stop the process before it goes too far.",
            ("photo", "blog/finance-rpt-delinquency.jpg", "From unpaid tax to auction: the notice, the warrant of "
             "levy, the sale, and the one year to redeem. (Illustration: Butch Mahinay, aumahinay.dev)",
             "medium"),
            ("h", "The Tax Is Tied to the Land"),
            "Under Section 246 of the Code, the real property tax for a year falls due on January 1, and from that "
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
            "By the end of this post, you will know what the tax on transfer of real property ownership is, "
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
            "deadline, knowing what you are paying for, and bringing the right papers. By the end"
            " of this post, you will know the real deadline, what being late costs in pesos, what"
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
            " actually comes from. By the end of this post, you will be able to read the one "
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
