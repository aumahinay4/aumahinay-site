"""Study Notes 2 to 10 (Butch asked 2026-11-10; outline approved earlier, see notes.OUTLINE).

One note every Friday at 9 pm Philippine time, November 13, 2026 to January 8, 2027.
Same shape as Note 1 in notes.py, plus "sources" (the laws and rules each note relies on).

Facts checked (November 2026) against the text of RA 7160 Book II (Butch's Drive copy, "lgu code Book II"),
RA 12001 (2024), RA 11032 (2018), PD 1445 (Government Auditing Code), COA Circular No. 97-002 (cash
advances) and Treasury Circular No. 02-2019 (fidelity bonds, as cited in OCA Circular No. 06-2024).
Worked examples and quiz answers were re-computed before publishing. No Wikipedia sources.
"""

NOTES_2_TO_10 = [
    # ------------------------------------------------------------------ Note 2
    {
        "number": 2,
        "slug": "real-property-tax-basics",
        "title": "Real property tax basics",
        "summary": "How land, buildings and machinery are valued and assessed, who may levy the real property "
                   "tax, the rates, what is exempt, and how the money is shared.",
        "publish_on": "2026-11-13 21:00",
        "body": [
            "Real property tax, or RPT, is the steadiest tax a local government has. Land does not move away, and "
            "the tax stays attached to it until it is paid. It is an ad valorem tax, which means the amount "
            "depends on the value of the property (Section 199). Title Two of Book II of the Local Government "
            "Code, Sections 197 to 283, governs it. In 2024 the Real Property Valuation and Assessment Reform Act "
            "(Republic Act No. 12001) changed the way property values are set, so both laws matter today.",
            ("h", "Who levies it and who collects it"),
            "Only a province, a city, or a municipality within Metro Manila may levy the real property tax "
            "(Section 232). In a municipality outside Metro Manila, the tax is levied by the province, but the "
            "municipal treasurer collects it and enforces the remedies against delinquent owners (Section 247). "
            "The municipal treasurer may deputize barangay treasurers to collect, as long as they are bonded and "
            "the municipality pays the premium.",
            ("h", "Five principles"),
            "Section 198 lists the principles behind every assessment:",
            ("list", [
                "Real property is appraised at its current and fair market value.",
                "It is classified for assessment according to its actual use.",
                "It is assessed on a uniform classification within each local government.",
                "Appraisal, assessment, levy and collection are never given to a private person.",
                "Appraisal and assessment must be equitable.",
            ]),
            ("h", "From market value to tax in three steps"),
            ("list", [
                "Market value. The assessor values the property at the market value in the locality "
                "(Section 201), using the schedule of market values. Under RA 12001, assessors prepare the "
                "schedule following the Philippine Valuation Standards, the Bureau of Local Government Finance "
                "(BLGF) reviews it, and the Secretary of Finance certifies it. It is updated every three years.",
                "Assessed value. The market value is multiplied by the assessment level, a percentage set by "
                "ordinance for each class (Section 199). The result is the assessed value, also called the "
                "taxable value.",
                "Tax. The assessed value is multiplied by the tax rate: up to 1% for a province, or up to 2% for "
                "a city or Metro Manila municipality (Section 233), plus 1% for the Special Education Fund, or "
                "SEF (Section 235).",
            ]),
            ("h", "Maximum assessment levels (Section 218)"),
            ("table", ["Kind of property", "Highest level the ordinance may set"], [
                ["Land", "Residential 20%, agricultural 40%, commercial 50%, industrial 50%, mineral 50%, "
                         "timberland 20%"],
                ["Buildings", "A sliding scale by market value. A residential building worth ₱175,000 or less "
                              "is assessed at 0%, and the level climbs by brackets to 60% for one worth more "
                              "than ₱10 million. Agricultural buildings run from 25% to 50%, and commercial and "
                              "industrial buildings from 30% to 80%."],
                ["Machinery", "Agricultural 40%, residential 50%, commercial 80%, industrial 80%"],
                ["Special classes", "Property used for hospitals, cultural or scientific purposes, and that of "
                                    "local water districts and government water or power corporations, at "
                                    "lower levels of 10% to 15% (Section 216)"],
            ]),
            ("tip", "These are ceilings, not the rates you will see on a tax bill. Each province or city sets its "
                    "own levels by ordinance, often much lower. Always read your local revenue code."),
            ("h", "Actual use, not the title"),
            "Section 217 says property is classified, valued and assessed by its actual use, regardless of "
            "where it is, who owns it, and who uses it. A lot titled as residential but used as a hardware store "
            "is assessed as commercial. When the use changes, the owner should expect a new assessment.",
            ("h", "Other levies on real property"),
            ("list", [
                "Idle land tax of up to 5% of assessed value (Section 236). It covers agricultural land of more "
                "than one hectare with half left uncultivated, and other land of more than 1,000 square meters "
                "with half unused (Section 237). Land planted to permanent or perennial crops with at least 50 trees "
                "a hectare, or used for grazing, is not idle.",
                "Special levy on land that gains from a public works project funded by the local government, up "
                "to 60% of the project cost, paid over five to ten years (Sections 240 and 241).",
            ]),
            ("h", "What is exempt (Section 234)"),
            ("list", [
                "Property of the Republic and of local governments, unless its beneficial use has been given to a "
                "taxable person",
                "Charitable institutions, churches and their parsonages or convents, mosques, non-profit or "
                "religious cemeteries, and property actually, directly and exclusively used for religious, "
                "charitable or educational purposes",
                "Machinery and equipment actually, directly and exclusively used by local water districts and "
                "government corporations that supply water or generate and transmit power",
                "Property owned by duly registered cooperatives",
                "Machinery and equipment used for pollution control and environmental protection",
            ]),
            "An owner who claims an exemption must file proof with the assessor within 30 days of declaring the "
            "property; otherwise it is listed as taxable (Section 206).",
            ("h", "How the money is shared"),
            "The basic tax collected in a province is split three ways: 35% to the province, 40% to the "
            "municipality and 25% to the barangay where the property is (Section 271). In a city, 70% goes to the "
            "city and 30% to the barangays: half of that to the barangay where the property is, and half equally "
            "to all barangays of the city. The barangay share must be released within five days after the end of "
            "each quarter, with no holdback. The SEF goes to the local school boards; in a province it is divided "
            "equally between the provincial and municipal school boards (Section 272).",
            ("h", "Declaring property and appealing an assessment"),
            "Owners declare their property to the assessor under oath (Section 202). A buyer, or an owner who "
            "builds an improvement, files a declaration within 60 days (Section 203). If an owner does not "
            "declare, the assessor declares the property for them (Section 204). An owner who disagrees with an "
            "assessment may appeal to the Local Board of Assessment Appeals within 60 days of receiving the "
            "notice (Section 226). The board decides within 120 days, and its decision may be appealed to the "
            "Central Board of Assessment Appeals within 30 days (Section 229). An appeal does not stop the "
            "collection of the tax (Section 231).",
            ("tip", "RA 12001 also protects owners from a sudden jump: in the first year a new schedule of market "
                    "values takes effect, the increase in real property tax is capped at 6% (Section 29)."),
        ],
        "example": (
            "Worked example: the tax on a house and lot",
            [
                "A family owns a residential lot with a market value of ₱500,000 and a house worth ₱1,200,000 in "
                "a municipality. Assume the province uses the maximum levels in Section 218.",
                "Lot: ₱500,000 × 20% = ₱100,000 assessed value.",
                "House: ₱1,200,000 falls in the bracket over ₱1,000,000 up to ₱2,000,000, so the level is 35%. "
                "₱1,200,000 × 35% = ₱420,000 assessed value.",
                "Total assessed value: ₱100,000 + ₱420,000 = ₱520,000.",
                "Basic tax at 1%: ₱5,200. SEF at 1%: ₱5,200. Total for the year: ₱10,400.",
                "Sharing of the basic tax: province 35% = ₱1,820; municipality 40% = ₱2,080; barangay 25% = "
                "₱1,300. The ₱5,200 SEF is split equally: ₱2,600 each to the provincial and municipal school "
                "boards.",
            ],
            "₱10,400 a year, payable in four installments of ₱2,600 each (see Note 3). With lower local "
            "assessment levels, the real bill would be smaller.",
        ),
        "practice": [
            ("Which of these may NOT levy the real property tax?",
             ["a province", "a city", "a municipality outside Metro Manila", "a municipality within Metro Manila"], 2,
             "Section 232: only provinces, cities and municipalities within Metro Manila may levy it. Outside "
             "Metro Manila, the province levies and the municipal treasurer collects."),
            ("The assessed value of real property is equal to ____.",
             ["market value × assessment level", "market value × tax rate", "assessed value × tax rate",
              "market value − depreciation"], 0,
             "Section 199: assessed value is the market value multiplied by the assessment level. It is the same "
             "as taxable value."),
            ("What is the highest assessment level a province may set for residential land?",
             ["10%", "20%", "40%", "50%"], 1,
             "Section 218: residential land 20%, agricultural 40%, commercial, industrial and mineral 50%, "
             "timberland 20%."),
            ("A residential lot is used as a hardware store. How is it assessed?",
             ["as residential, because of its title", "as commercial, because of its actual use",
              "as agricultural", "as special"], 1,
             "Section 217: real property is classified and assessed by its actual use, whoever owns or uses it."),
            ("What is the maximum idle land tax?",
             ["1% of assessed value", "2% of assessed value", "5% of assessed value", "10% of market value"], 2,
             "Section 236 allows an annual tax on idle lands of up to 5% of assessed value, on top of the basic "
             "tax."),
            ("Of the basic real property tax collected in a province, what share goes to the barangay where the "
             "property is?",
             ["20%", "25%", "35%", "40%"], 1,
             "Section 271(a): province 35%, municipality 40%, barangay 25%."),
            ("In a province, how is the Special Education Fund tax shared?",
             ["all to the provincial school board", "all to the municipal school board",
              "equally between the provincial and municipal school boards", "35/40/25 like the basic tax"], 2,
             "Section 272: in provinces, the SEF is divided equally between the provincial and municipal school "
             "boards."),
            ("Within how many days of receiving the notice of assessment may an owner appeal to the Local Board "
             "of Assessment Appeals?",
             ["15 days", "30 days", "60 days", "120 days"], 2,
             "Section 226: within 60 days from receipt of the written notice of assessment."),
            ("Which property is exempt from real property tax?",
             ["a private school's canteen leased to a concessionaire", "a church and its convent",
              "a government lot leased to a private company", "a farm owned by a corporation"], 1,
             "Section 234(b) exempts churches and their parsonages or convents. Government property whose "
             "beneficial use is given to a taxable person is taxable."),
            ("Under RA 12001, the increase in real property tax in the first year of a new schedule of market "
             "values is capped at ____.",
             ["3%", "6%", "10%", "20%"], 1,
             "Section 29 of RA 12001 caps the first-year increase at 6% of the taxes before the new schedule."),
        ],
        "sources": [
            "Republic Act No. 7160, Local Government Code of 1991, Book II, Sections 197 to 283",
            "Republic Act No. 12001, Real Property Valuation and Assessment Reform Act (approved June 13, 2024), "
            "Sections 15, 16, 19 and 29",
        ],
    },
    # ------------------------------------------------------------------ Note 3
    {
        "number": 3,
        "slug": "paying-real-property-tax",
        "title": "Paying real property tax: quarters, discounts and interest",
        "summary": "When real property tax falls due, how the quarterly installments, advance-payment discounts "
                   "and 2% monthly interest work, and what happens when the tax stays unpaid.",
        "publish_on": "2026-11-20 21:00",
        "body": [
            "Note 2 showed how the real property tax is computed. This note follows the tax bill from January to "
            "December: when it falls due, how to pay it in parts, how to earn a discount, how interest grows, and "
            "what the treasurer may do when it stays unpaid. Unless stated otherwise, the sections cited are from "
            "the Local Government Code (RA 7160).",
            ("h", "January 1: the tax is born"),
            "The tax for a year accrues on January 1, and from that day it is a lien on the property, superior to "
            "any mortgage or other claim (Section 246). The lien follows the land even if it is sold. The "
            "assessor gives the treasurer the assessment roll on or before December 31 (Section 248), and the "
            "treasurer posts a notice of the dates when the tax may be paid without interest on or before January "
            "31, and publishes it once a week for two weeks (Section 249).",
            ("h", "Four installments"),
            "The basic tax and the SEF may be paid in four equal installments without interest (Section 250):",
            ("table", ["Installment", "Due on or before"], [
                ["First quarter", "March 31"],
                ["Second quarter", "June 30"],
                ["Third quarter", "September 30"],
                ["Fourth quarter", "December 31"],
            ]),
            ("tip", "Section 250 also says payments go first to prior years' unpaid tax, interest and penalties. "
                    "An owner with old arrears cannot choose to pay only the current year."),
            ("h", "Discounts for paying early"),
            "If the basic tax and the SEF are paid in advance according to the schedule, the sanggunian may grant "
            "a discount of up to 20% of the annual tax (Section 251). The exact discount is set by the local "
            "revenue code. Many codes give a smaller discount for paying each quarter on time and a bigger one "
            "for paying the whole year, or several years, in advance. Discounts usually apply only to properties "
            "with no unpaid back taxes.",
            ("h", "Interest for paying late"),
            "An installment not paid by its due date earns interest of 2% a month on the unpaid amount until it is "
            "paid in full. The total interest can never exceed 36 months, so the most interest that can pile up "
            "is 72% (Section 255). Many local codes count a part of a month as a full month, so paying on the "
            "first day of a month instead of the last day of the month before costs a full 2%.",
            ("h", "When the tax stays unpaid"),
            ("list", [
                "Notice of delinquency. The treasurer posts it at the main entrance of the provincial capitol or "
                "city or municipal hall and in each barangay, and publishes it once a week for two weeks "
                "(Section 254).",
                "Remedies. The local government may levy on the real property, go to court, or do both "
                "(Section 256).",
                "Warrant of levy. It works like a court order of execution and is annotated on the tax "
                "declaration and the title (Section 258). A treasurer who fails to issue or execute the warrant "
                "within one year from delinquency may be dismissed from the service (Section 259).",
                "Auction. Within 30 days after the warrant is served, the treasurer advertises the sale for two "
                "weeks (Section 260). The owner may stop the sale at any time before the date by paying the tax, "
                "interest and expenses.",
                "Redemption. After the sale, the owner has one year to redeem the property by paying the "
                "delinquent tax, interest and expenses, plus up to 2% a month on the purchase price. The owner "
                "keeps possession and its income during that year (Section 261).",
                "No bidder. If nobody bids, the treasurer buys the property for the local government. The owner "
                "may still redeem it within one year (Section 263).",
            ]),
            "Collection has a time limit. The tax must be collected within five years from the date it became "
            "due, or within ten years from discovery if there was fraud or intent to evade (Section 270). The "
            "period stops running while the treasurer is legally prevented from collecting, while a "
            "reinvestigation requested with a written waiver is pending, or while the owner is out of the country "
            "or cannot be found.",
            ("h", "Paying under protest and asking for a refund"),
            "A taxpayer who thinks the tax is wrong must still pay it first. The receipt is marked \"paid under "
            "protest\", and the written protest is filed within 30 days of payment with the provincial or city "
            "treasurer (or the treasurer of a Metro Manila municipality), who decides within 60 days. The amount "
            "protested is held in trust. If the protest wins, the money is refunded or credited; if it is denied "
            "or not decided in 60 days, the taxpayer may go to the Local Board of Assessment Appeals "
            "(Section 252). A claim for refund of an excessive collection is filed within two years from the date "
            "the taxpayer becomes entitled to it (Section 253).",
            ("h", "Relief in hard times"),
            "After a general crop failure, a big drop in farm prices, or a calamity, the sanggunian may condone or "
            "reduce the tax and interest for the following year by an ordinance passed before January 1 "
            "(Section 276). The President may also condone or reduce the tax when the public interest requires it "
            "(Section 277).",
            ("tip", "A buyer should ask for proof that the real property tax is fully paid before closing a sale. "
                    "The Registry of Deeds will not register a transfer without it (Section 209)."),
        ],
        "example": (
            "Worked example: one bill, three ways to pay",
            [
                "A lot's basic tax is ₱1,200 and its SEF is ₱1,200, so the total is ₱2,400 a year, or ₱600 a "
                "quarter. The local code gives a 10% discount for paying the whole year by March 31, and counts "
                "a part of a month as a full month.",
                "Paid in full on March 20: ₱2,400 − 10% (₱240) = ₱2,160.",
                "Paid quarter by quarter on time: 4 × ₱600 = ₱2,400.",
                "First and second quarters paid together on August 10. The first quarter was due March 31, so "
                "April, May, June, July and part of August count: 5 months × 2% = 10%, or ₱60.",
                "The second quarter was due June 30, so July and part of August count: 2 months × 2% = 4%, or "
                "₱24.",
                "Paid on August 10: ₱600 + ₱60 + ₱600 + ₱24 = ₱1,284.",
            ],
            "Paying early costs ₱2,160 for the year; paying the first half late costs ₱84 more than paying on "
            "time. The RPT calculator on this site does the same arithmetic for any date.",
        ),
        "practice": [
            ("On what date does the real property tax for a year accrue?",
             ["January 1", "January 31", "March 31", "the date of the assessment"], 0,
             "Section 246: it accrues on January 1 and from then is a lien on the property."),
            ("When is the second-quarter installment due?",
             ["on or before April 20", "on or before June 30", "on or before July 20", "on or before September 30"], 1,
             "Section 250: March 31, June 30, September 30 and December 31."),
            ("What is the largest discount a sanggunian may give for advance payment?",
             ["10%", "15%", "20%", "25%"], 2,
             "Section 251: a discount not exceeding 20% of the annual tax due."),
            ("What is the most interest that can be charged on an unpaid installment?",
             ["24%", "36%", "50%", "72%"], 3,
             "Section 255: 2% a month for at most 36 months, or 72%."),
            ("An owner with unpaid tax for last year pays this year's first quarter. Where does the payment go "
             "first?",
             ["to the current quarter", "to last year's unpaid tax, interest and penalties",
              "to the SEF only", "the owner may choose"], 1,
             "Section 250: payments are applied first to prior years' delinquencies, interest and penalties."),
            ("A protest against the tax must be filed within ____ after paying the tax.",
             ["15 days", "30 days", "60 days", "one year"], 1,
             "Section 252: no protest is entertained unless the tax is paid first, and the written protest is "
             "filed within 30 days of payment."),
            ("After a tax auction, how long does the owner have to redeem the property?",
             ["30 days", "six months", "one year", "five years"], 2,
             "Section 261: one year from the date of sale, paying the tax, interest and expenses plus up to 2% "
             "a month on the purchase price."),
            ("Without fraud, within what period must the real property tax be collected?",
             ["three years from the date it became due", "five years from the date it became due",
              "ten years from the date it became due", "there is no limit"], 1,
             "Section 270: five years, or ten years from discovery when there is fraud or intent to evade."),
            ("If nobody bids at the auction of a delinquent property, what happens?",
             ["the sale is cancelled and the tax is forgiven", "the treasurer buys it for the local government",
              "the barangay takes it", "the owner gets a 50% discount"], 1,
             "Section 263: the treasurer purchases it for the local government; the owner may redeem it within "
             "one year."),
            ("A tax bill of ₱600 was due March 31 and is paid on May 5. The local code counts a part of a month "
             "as a month. What is the interest?",
             ["₱12", "₱24", "₱36", "₱48"], 1,
             "April and part of May are 2 months: 2 × 2% = 4% of ₱600 = ₱24."),
        ],
        "sources": [
            "Republic Act No. 7160, Local Government Code of 1991, Sections 209, 246 to 277",
        ],
        "link": ("Try the numbers yourself:", "Real Property Tax calculator", "/tools/rpt-calculator/"),
    },
    # ------------------------------------------------------------------ Note 4
    {
        "number": 4,
        "slug": "business-tax-and-mayors-permit",
        "title": "Business tax and the mayor's permit",
        "summary": "Who pays the local business tax, how it is computed from last year's gross sales, when it is "
                   "due, the penalties for paying late, and where the mayor's permit and the Business One Stop "
                   "Shop fit in.",
        "publish_on": "2026-11-27 21:00",
        "body": [
            "Every January, the line at the municipal hall grows long with business owners renewing their "
            "permits. Two different things are paid at that time: the business tax, which is a tax on doing "
            "business, and the regulatory fees for the mayor's permit. This note explains both, using the Local "
            "Government Code (RA 7160) and the Ease of Doing Business Act (RA 11032).",
            ("h", "Who may levy it"),
            "The business tax belongs to the municipality (Section 143). A city may levy the same taxes at rates "
            "up to 50% higher (Section 151), and so may municipalities in Metro Manila (Section 144). Barangays "
            "alone may tax small stores with gross sales of ₱50,000 or less in cities, or ₱30,000 or less in "
            "municipalities, at up to 1% (Section 152). The province has no general business tax, but it has its "
            "own taxes, such as those on printing and publication, franchises, amusement and delivery trucks "
            "(Note 1).",
            ("h", "The tax base: last year's gross sales"),
            "The tax for this year is based on gross sales or receipts of the preceding calendar year. Gross "
            "sales means the total money received for goods or services, excluding discounts known at the time "
            "of sale, sales returns, excise tax and value-added tax (Section 131).",
            ("h", "The rates in Section 143"),
            ("table", ["Kind of business", "Maximum rate"], [
                ["Manufacturers, assemblers, repackers, processors, brewers, distillers", "A fixed amount by "
                 "bracket of gross sales; ₱6.5 million or more: up to 37.5% of 1%"],
                ["Wholesalers, distributors, dealers", "A fixed amount by bracket; ₱2 million or more: up to 50% "
                 "of 1%"],
                ["Exporters, and sellers of essential goods", "Half the usual rates. Essential goods include rice "
                 "and corn, flour, meat, dairy, sugar, salt, cooking oil and gas, laundry soap, detergents, "
                 "medicine, farm inputs, feeds, school supplies and cement."],
                ["Retailers", "2% of gross sales of ₱400,000 or less; 1% if more"],
                ["Contractors", "A fixed amount by bracket; ₱2 million or more: up to 50% of 1%"],
                ["Banks and other financial institutions", "Up to 50% of 1% of gross receipts from interest, "
                 "commissions, discounts, leasing, dividends, rentals and similar"],
                ["Peddlers", "Up to ₱50 a year each"],
                ["Any other business", "A rate set by the sanggunian; no more than 2% for businesses subject to "
                 "VAT, excise or percentage tax"],
            ]),
            ("tip", "As with every local tax, these are ceilings. The municipality's revenue code sets the actual "
                    "schedule."),
            ("h", "Rules that trip people up"),
            ("list", [
                "Each establishment pays separately. One line of business does not become exempt because "
                "another line in the same place already pays (Section 146).",
                "Two businesses with the same rate are taxed on their combined gross sales; businesses with "
                "different rates report their sales separately.",
                "A branch or sales outlet records its own sales and pays where it is located (Section 150). For "
                "sales recorded in a principal office, 30% is taxed where the office is and 70% where the "
                "factory, plant, project office or plantation is.",
                "A business that closes must file a sworn statement of its gross sales for the year and pay any "
                "balance before it is officially retired (Section 145).",
            ]),
            ("h", "When to pay, and the penalties"),
            "The tax period is the calendar year, and the tax may be paid quarterly (Section 165). It accrues on "
            "January 1; a new tax or a new rate starts on the first day of the next quarter after the ordinance "
            "takes effect (Section 166). Payment is due within the first 20 days of January, or of each quarter "
            "for those paying by installment. The sanggunian may extend this for a good reason, but by no more "
            "than six months (Section 167). If paid late, the sanggunian may impose a surcharge of up to 25% and "
            "interest of up to 2% a month on the tax plus surcharge, for no more than 36 months (Section 168).",
            ("h", "The mayor's permit"),
            "Besides the tax, the municipality may charge reasonable fees for regulating, inspecting and licensing "
            "a business, but they must be commensurate with the cost of that work (Section 147). Before the "
            "permit is issued, the business needs a barangay clearance. The barangay must act on it within seven "
            "working days; if it does not, the city or municipality may issue the permit anyway "
            "(Section 152).",
            "RA 11032 requires local governments to use a single unified business application form, to set up a "
            "Business One Stop Shop (BOSS), and to automate the process. Barangay clearances may now be issued at "
            "the city or municipal BOSS. Government offices must act on applications within three working days "
            "for simple transactions, seven for complex ones and twenty for highly technical ones, and an "
            "application not acted on in time is deemed approved.",
            ("h", "Checking the books, and the taxpayer's remedies"),
            "The treasurer may examine a business's books once each tax period, during business hours, with a "
            "written authority if a deputy does it (Section 171). Unpaid taxes may be assessed within five years "
            "from the date they became due, or ten years from discovery of fraud (Section 194). A taxpayer who "
            "receives a notice of assessment may protest in writing within 60 days; the treasurer decides within "
            "60 days, and the taxpayer has 30 days after a denial to go to court (Section 195). A refund claim "
            "must be filed with the treasurer, and no court case may be brought after two years from payment "
            "(Section 196).",
        ],
        "example": (
            "Worked example: a sari-sari store that paid late",
            [
                "A store in a municipality had gross sales of ₱300,000 last year. It is a retailer with sales of "
                "₱400,000 or less, so the maximum rate is 2%.",
                "Annual business tax: ₱300,000 × 2% = ₱6,000, or ₱1,500 a quarter.",
                "The first-quarter installment was due January 20 but was paid on March 15.",
                "Surcharge at the maximum 25%: ₱1,500 × 25% = ₱375.",
                "Interest at 2% a month on the tax plus surcharge, for 2 months (January 21 to March 15, counting "
                "a part of a month as a month): (₱1,500 + ₱375) × 4% = ₱75.",
                "Amount due on March 15: ₱1,500 + ₱375 + ₱75 = ₱1,950.",
            ],
            "Paying less than two months late raised the installment from ₱1,500 to ₱1,950. A store with sales of only "
            "₱25,000 would instead pay the barangay, at up to 1%.",
        ),
        "practice": [
            ("What is the tax base of the municipal business tax?",
             ["the capital of the business", "the gross sales or receipts of the preceding calendar year",
              "the net income of the current year", "the assessed value of the store"], 1,
             "Section 143 bases the tax on gross sales or receipts of the preceding calendar year."),
            ("What is the maximum rate on a retailer with gross sales of ₱400,000 or less?",
             ["0.5%", "1%", "2%", "3%"], 2,
             "Section 143(d): 2% for ₱400,000 or less, 1% if more."),
            ("In a municipality, who may tax a store with gross sales of ₱25,000?",
             ["the province", "the municipality", "the barangay", "nobody"], 2,
             "Section 152: barangays alone may tax stores with sales of ₱30,000 or less in municipalities "
             "(₱50,000 or less in cities)."),
            ("Within what period must business taxes be paid?",
             ["the first 20 days of January or of each quarter", "the whole month of January",
              "on or before March 31", "within 30 days of the permit"], 0,
             "Section 167: within the first 20 days of January or of each subsequent quarter."),
            ("What is the highest surcharge a sanggunian may impose on late business tax?",
             ["10%", "20%", "25%", "50%"], 2,
             "Section 168: a surcharge of up to 25%, plus interest of up to 2% a month for at most 36 months."),
            ("A manufacturer records sales in its principal office in Makati but has its factory in a Quezon "
             "town. What share of those sales may the town tax?",
             ["30%", "50%", "60%", "70%"], 3,
             "Section 150(b): 30% to where the principal office is and 70% to where the factory is."),
            ("Regulatory fees for the mayor's permit must be ____.",
             ["equal to the business tax", "commensurate with the cost of regulation, inspection and licensing",
              "at least ₱1,000", "set by the BLGF"], 1,
             "Section 147: reasonable fees commensurate with the cost of regulation, inspection and licensing."),
            ("If a barangay does not act on a clearance application within seven working days, what may happen?",
             ["the application is denied", "the city or municipality may issue the permit anyway",
              "the business must reapply", "the punong barangay is fined"], 1,
             "Section 152(c): the city or municipality may issue the license or permit."),
            ("How long does a taxpayer have to protest a notice of assessment for local taxes?",
             ["15 days", "30 days", "60 days", "one year"], 2,
             "Section 195: a written protest within 60 days of receiving the notice; the treasurer decides "
             "within 60 days."),
            ("Under RA 11032, what is the processing time for a simple transaction?",
             ["one working day", "three working days", "seven working days", "twenty working days"], 1,
             "RA 11032: three working days for simple, seven for complex and twenty for highly technical "
             "applications."),
        ],
        "sources": [
            "Republic Act No. 7160, Local Government Code of 1991, Sections 131, 143 to 152 and 165 to 196",
            "Republic Act No. 11032, Ease of Doing Business and Efficient Government Service Delivery Act of 2018",
        ],
    },
    # ------------------------------------------------------------------ Note 5
    {
        "number": 5,
        "slug": "community-tax-cedula",
        "title": "Community tax (cedula)",
        "summary": "Who must pay the community tax, how the basic and additional tax are computed for individuals "
                   "and corporations, when it is due, and when the certificate must be shown.",
        "publish_on": "2026-12-04 21:00",
        "body": [
            "Most Filipinos still call it the cedula. Its legal name is the community tax, and the paper you get "
            "after paying is the community tax certificate, or CTC. It is one of the smallest taxes a person pays, "
            "but it is collected from more people than almost any other local tax. Article Six of Title One, Book "
            "II of the Local Government Code (Sections 156 to 164) governs it.",
            ("h", "Who levies it"),
            "Cities and municipalities may levy the community tax (Section 156). Provinces and barangays do not "
            "levy it, although barangay treasurers often collect it as deputies, as explained below.",
            ("h", "Individuals who must pay (Section 157)"),
            "Every inhabitant of the Philippines aged 18 or over must pay if any one of these is true:",
            ("list", [
                "They have been regularly employed on a wage or salary basis for at least 30 consecutive working "
                "days during the year.",
                "They are engaged in a business or occupation.",
                "They own real property with a total assessed value of ₱1,000 or more.",
                "They are required by law to file an income tax return.",
            ]),
            "The tax has two parts: a basic tax of ₱5.00, and an additional tax of ₱1.00 for every ₱1,000 of "
            "income, whether from business, the exercise of a profession, or property. The additional tax can "
            "never exceed ₱5,000. For a married couple, the additional tax is based on the total property they "
            "own and the total gross receipts or earnings of both.",
            ("h", "Corporations (Section 158)"),
            "Every corporation doing business in the Philippines, domestic or resident foreign, pays a basic tax "
            "of ₱500 and an additional tax of:",
            ("list", [
                "₱2.00 for every ₱5,000 worth of real property in the Philippines it owned during the preceding "
                "year, based on the value used for the real property tax; and",
                "₱2.00 for every ₱5,000 of gross receipts or earnings from its business in the Philippines during "
                "the preceding year. Dividends received from other corporations count as gross receipts.",
            ]),
            "The additional tax of a corporation can never exceed ₱10,000.",
            ("h", "Who is exempt"),
            "Only two groups: diplomatic and consular representatives, and transient visitors whose stay in the "
            "Philippines does not exceed three months (Section 159). A person who is not required to pay may "
            "still get a certificate for ₱1.00 (Section 162).",
            ("h", "Where and when to pay (Sections 160 and 161)"),
            ("list", [
                "An individual pays where they reside; a corporation pays where its principal office is.",
                "The tax accrues on January 1 and must be paid by the last day of February.",
                "A person who turns 18, or stops being exempt, on or before June 30 must pay for that year. If "
                "it happens on or before March 31, they have 20 days to pay without becoming delinquent.",
                "A person who turns 18, comes to reside in the Philippines, or stops being exempt on or after "
                "July 1 does not pay for that year. The same June 30 and July 1 cut-offs apply to new "
                "corporations.",
                "Unpaid tax earns interest of 24% a year from the due date until it is paid.",
            ]),
            ("h", "When the certificate must be shown (Section 163)"),
            "An individual who must pay the community tax may be asked to show the certificate when they:",
            ("list", [
                "acknowledge a document before a notary public",
                "take an oath of office for a government position",
                "receive a license, certificate or permit from a public authority",
                "pay any tax or fee, or receive money from public funds",
                "transact other official business, or receive a salary or wage",
            ]),
            "A corporation shows its certificate in the same kinds of transactions. From January to April 15, the "
            "previous year's certificate is still accepted. A certificate is never required to register as a "
            "voter.",
            ("tip", "The CTC is not an ID and does not prove identity. It proves only that the tax for the year has "
                    "been paid."),
            ("h", "Collection and sharing (Section 164)"),
            "The national government prints the certificates and distributes them through the city and municipal "
            "treasurers. A small part of the proceeds goes to the national government to cover printing and "
            "distribution, and the treasurer remits it within 10 days after the end of each quarter. The city or "
            "municipal treasurer deputizes barangay treasurers to collect the tax in their barangays, but only if "
            "they are bonded. What the city or municipal treasurer collects directly goes entirely to its general "
            "fund. What is collected through barangay treasurers is split 50% to the city or municipality and 50% "
            "to the barangay where it was collected.",
            ("tip", "For a barangay, deputized CTC collection is real income. A barangay treasurer who collects "
                    "early in the year, while most people need their cedula, keeps half of every peso for the "
                    "barangay."),
        ],
        "example": (
            "Worked example: an employee and a small corporation",
            [
                "Ana earns a salary of ₱360,000 a year. Basic tax: ₱5.00. Additional tax: ₱360,000 ÷ ₱1,000 × "
                "₱1.00 = ₱360.00. Total: ₱365.00.",
                "Her cousin, a professional earning ₱6,000,000 a year, would owe ₱6,000 in additional tax, but the "
                "cap is ₱5,000, so the total is ₱5,005.",
                "A corporation owned real property assessed at ₱2,000,000 and had gross receipts of ₱10,000,000 "
                "last year.",
                "Real property: ₱2,000,000 ÷ ₱5,000 × ₱2.00 = ₱800. Gross receipts: ₱10,000,000 ÷ ₱5,000 × ₱2.00 = "
                "₱4,000.",
                "Additional tax: ₱800 + ₱4,000 = ₱4,800, below the ₱10,000 cap. Total: ₱500 + ₱4,800 = ₱5,300.",
            ],
            "Ana pays ₱365, the professional ₱5,005, and the corporation ₱5,300. If Ana paid through her barangay "
            "treasurer, ₱182.50 would stay with the barangay.",
        ),
        "practice": [
            ("Which local governments may levy the community tax?",
             ["provinces only", "cities and municipalities", "barangays only", "all local governments"], 1,
             "Section 156: cities or municipalities may levy a community tax."),
            ("What is the basic community tax for an individual?",
             ["₱1.00", "₱5.00", "₱50.00", "₱500.00"], 1,
             "Section 157: an annual basic tax of ₱5.00, plus the additional tax."),
            ("What is the maximum additional community tax for an individual?",
             ["₱1,000", "₱2,000", "₱5,000", "₱10,000"], 2,
             "Section 157: ₱1.00 for every ₱1,000 of income, never more than ₱5,000."),
            ("A corporation pays an additional tax of ₱2.00 for every ____ of gross receipts.",
             ["₱1,000", "₱2,000", "₱5,000", "₱10,000"], 2,
             "Section 158: ₱2.00 for every ₱5,000 of real property and ₱2.00 for every ₱5,000 of gross receipts, "
             "up to ₱10,000."),
            ("By when must the community tax be paid?",
             ["January 20", "the last day of February", "March 31", "April 15"], 1,
             "Section 161: it accrues on January 1 and is paid not later than the last day of February."),
            ("Who is exempt from the community tax?",
             ["senior citizens", "government employees", "diplomatic and consular representatives",
              "students"], 2,
             "Section 159: only diplomatic and consular representatives, and transient visitors staying three "
             "months or less."),
            ("Maria turns 18 on August 15. Must she pay the community tax for that year?",
             ["yes, within 20 days", "yes, by December 31", "no, not for that year", "only if she is employed"], 2,
             "Section 161: a person who reaches 18 on or after July 1 is not subject to the tax for that year."),
            ("What interest applies to unpaid community tax?",
             ["2% a month up to 36 months", "24% a year", "25% surcharge only", "none"], 1,
             "Section 161: interest of 24% a year from the due date until paid."),
            ("For which of these is the community tax certificate NOT required?",
             ["acknowledging a deed before a notary", "receiving a business permit", "registering as a voter",
              "taking an oath of office"], 2,
             "Section 163: presentation of the certificate is not required for the registration of a voter."),
            ("Community tax collected by a deputized barangay treasurer is shared ____.",
             ["100% to the barangay", "50% city or municipality, 50% barangay", "70% city, 30% barangay",
              "all to the national government"], 1,
             "Section 164(c): 50% to the general fund of the city or municipality and 50% to the barangay where "
             "it was collected."),
        ],
        "sources": [
            "Republic Act No. 7160, Local Government Code of 1991, Sections 156 to 164",
        ],
    },
    # ------------------------------------------------------------------ Note 6
    {
        "number": 6,
        "slug": "fees-and-charges",
        "title": "Fees and charges",
        "summary": "How a fee differs from a tax, which fees and charges local governments may collect, and the "
                   "rules on amounts, ordinances, tolls and late payment.",
        "publish_on": "2026-12-11 21:00",
        "body": [
            "Taxes are only part of local revenue. A town also earns from permit fees, market stall rentals, "
            "slaughterhouse charges, burial fees, certifications and many other payments. Together these are "
            "called fees and charges. They follow their own rules, and knowing the difference between a fee and a "
            "tax helps a treasury worker defend a charge, or spot one that should not be there.",
            ("h", "Fee, charge, tax: the definitions"),
            ("list", [
                "A fee is a charge fixed by law or ordinance for the regulation or inspection of a business or "
                "activity (Section 131).",
                "Charges are pecuniary liabilities, such as rents or fees, against persons or property "
                "(Section 131).",
                "A tax is imposed to raise revenue for public purposes. It does not need to match any service "
                "the taxpayer receives.",
            ]),
            "This difference matters. A regulatory fee must be commensurate with the cost of regulation, "
            "inspection and licensing (Section 147). A \"fee\" set far above that cost is really a tax, and it "
            "must then meet every rule for taxes, including the limits on what local governments may tax.",
            ("h", "What may be charged"),
            ("table", ["Kind", "Legal basis (RA 7160)"], [
                ["Fees on business and occupation (the mayor's permit) and on the practice of a profession, "
                 "except the professional tax kept by the province", "Section 147"],
                ["Sealing and licensing of weights and measures", "Section 148"],
                ["Fishery rentals, fees and charges in municipal waters", "Section 149"],
                ["Barangay clearance, and barangay fees on cockpits, places of recreation with admission fees, "
                 "and billboards and signs", "Section 152"],
                ["Service fees and charges for services rendered", "Section 153"],
                ["Rates for public utilities the local government owns and runs, such as a water system or "
                 "public market", "Section 154"],
                ["Toll fees for roads, piers, bridges and ferries the local government built", "Section 155"],
                ["Any other fee or charge on a base not already enumerated or taxed by national law",
                 "Section 186"],
            ]),
            ("h", "Some built-in protections"),
            ("list", [
                "Marginal fishermen may gather fry and catch fish in municipal waters free of any rental, fee or "
                "charge (Section 149).",
                "Tolls may not be collected from soldiers and police officers on mission, postal workers "
                "delivering mail, physically handicapped persons, and disabled citizens aged 65 or older "
                "(Section 155).",
                "For a weights-and-measures offense that does not involve fraud, the sanggunian may let the "
                "treasurer settle the case before it reaches court, for a compromise penalty of at least ₱200 "
                "(Section 148).",
            ]),
            ("h", "How a fee becomes law"),
            "A fee or charge, like a tax, is imposed only by an ordinance of the sanggunian, and only after a "
            "public hearing (Sections 186 and 187). Within 10 days of approval, the ordinance is published in "
            "full for three consecutive days in a local newspaper; where there is none, it is posted in at least "
            "two conspicuous public places (Section 188). Copies go to the local treasurers for public "
            "information (Section 189). Anyone may question its legality before the Secretary of Justice within "
            "30 days of its effectivity, but the appeal does not stop the collection (Section 187). Enforcing an "
            "ordinance after notice that it was disapproved or suspended is a ground for administrative action "
            "(Section 190).",
            ("h", "Late payment and exemptions"),
            "For taxes, fees and charges not paid on time, the sanggunian may impose a surcharge of up to 25% and "
            "interest of up to 2% a month, for no more than 36 months (Section 168). For other revenue due the "
            "local government, such as rentals under a contract, interest of up to 2% a month for no more than 36 "
            "months may be collected from the due date (Section 169). The sanggunian may also grant exemptions or "
            "reliefs by ordinance (Section 192).",
            ("tip", "Fees and charges, like taxes, may never be collected by a private person (Section 130). Every "
                    "peso must pass through the treasurer or a duly authorized deputy, and every payment gets an "
                    "official receipt (see Note 7)."),
            ("h", "Where the money goes"),
            "Most fees go to the general fund. Income from a public utility or economic enterprise, such as a "
            "market or slaughterhouse, is recorded in a special account of the general fund; after costs, it "
            "first pays back the loans or advances made for it, and any excess becomes part of the general fund "
            "(Section 313). Money held for a specific purpose, such as a guaranty deposit, is a trust fund and "
            "may be used only for that purpose (Section 309).",
        ],
        "example": (
            "Worked example: is it a fee or a tax?",
            [
                "A town charges every sari-sari store a ₱3,000 \"sanitary inspection fee\" a year. The health "
                "office spends about ₱300 a year to inspect each store.",
                "A fee must be commensurate with the cost of regulation (Section 147). At ten times the cost, the "
                "charge looks like a tax, open to challenge before the Secretary of Justice within 30 days of the "
                "ordinance's effectivity (Section 187).",
                "Now a different case: a market stall rents for ₱1,500 a month, due on the 5th. A vendor pays the "
                "January rent three months late, and the ordinance sets interest at 2% a month (Section 169).",
                "Interest: ₱1,500 × 2% × 3 months = ₱90. Amount due: ₱1,500 + ₱90 = ₱1,590.",
            ],
            "A fee is tested against the cost of the service; a rental follows the contract or ordinance. The "
            "vendor owes ₱1,590.",
        ),
        "practice": [
            ("The Local Government Code defines a fee as a charge fixed by law or ordinance for ____.",
             ["raising general revenue", "the regulation or inspection of a business or activity",
              "the use of a public road only", "national government services"], 1,
             "Section 131: a fee is a charge fixed by law or ordinance for the regulation or inspection of a "
             "business or activity."),
            ("A regulatory fee for the mayor's permit must be ____.",
             ["at least equal to the business tax", "commensurate with the cost of regulation, inspection and "
              "licensing", "set by the Department of Finance", "the same in every town"], 1,
             "Section 147. A fee far above that cost is really a tax."),
            ("Which of these is exempt from toll fees under Section 155?",
             ["a jeepney operator", "a postal worker delivering mail", "a delivery truck",
              "any senior citizen"], 1,
             "Section 155 exempts soldiers and police officers on mission, postal personnel delivering mail, "
             "physically handicapped persons, and disabled citizens aged 65 or older."),
            ("Before an ordinance levying a new fee is enacted, what is required?",
             ["approval of the BLGF", "a public hearing", "a referendum", "approval of COA"], 1,
             "Sections 186 and 187: no tax ordinance or revenue measure without a prior public hearing."),
            ("Within how many days after approval must a revenue ordinance be published?",
             ["5 days", "10 days", "15 days", "30 days"], 1,
             "Section 188: within 10 days, in full for three consecutive days in a local newspaper, or posted in "
             "two public places."),
            ("A taxpayer questions the legality of a revenue ordinance. To whom, and within what period?",
             ["the Secretary of Justice, within 30 days of effectivity", "the COA, within 60 days",
              "the provincial treasurer, within 15 days", "the Ombudsman, any time"], 0,
             "Section 187: appeal to the Secretary of Justice within 30 days from effectivity; the appeal does "
             "not suspend collection."),
            ("May marginal fishermen be charged a fee for gathering bangus fry in municipal waters?",
             ["yes, at the rate set by ordinance", "no, it is free of any rental, fee or charge",
              "only during the closed season", "only if they use nets"], 1,
             "Section 149(b)(2): the privilege is granted to marginal fishermen free of any rental, fee or "
             "charge."),
            ("What is the maximum interest on unpaid rentals and other revenues under Section 169?",
             ["1% a month, up to 12 months", "2% a month, up to 36 months", "24% a year, no limit",
              "25% one-time surcharge"], 1,
             "Section 169: up to 2% a month from the due date, for no more than 36 months."),
            ("Who may collect local fees and charges?",
             ["a private agency paid by commission", "the treasurer or a duly authorized deputy",
              "any department head", "the barangay tanod"], 1,
             "Sections 130 and 170: collection is never let to a private person; it is done by the treasurer "
             "or authorized deputies."),
            ("A guaranty deposit received by the local government goes to which fund?",
             ["the general fund", "the Special Education Fund", "a trust fund", "the development fund"], 2,
             "Section 309(b): money received as a guaranty for an obligation is a trust fund, used only for its "
             "purpose."),
        ],
        "sources": [
            "Republic Act No. 7160, Local Government Code of 1991, Sections 130, 131, 147 to 155, 168, 169, 186 "
            "to 192, 309 and 313",
        ],
    },
    # ------------------------------------------------------------------ Note 7
    {
        "number": 7,
        "slug": "collection-and-deposit",
        "title": "Collection and deposit",
        "summary": "Who may collect local revenue, the rule that every payment gets an official receipt, how "
                   "collections are reported and deposited intact, and how local funds are kept apart.",
        "publish_on": "2026-12-18 21:00",
        "body": [
            "Notes 1 to 6 explained what a local government may collect. This note is about the act of collecting "
            "itself: the window where a taxpayer hands over money, and what must happen to that money before the "
            "day ends. Two laws set the rules: the Local Government Code (RA 7160) and the Government Auditing "
            "Code of the Philippines (Presidential Decree No. 1445). The Commission on Audit (COA) adds the forms "
            "and procedures in its Government Accounting Manual for local governments.",
            ("h", "Who may collect"),
            "All local taxes, fees and charges are collected by the provincial, city, municipal or barangay "
            "treasurer, or by their duly authorized deputies (Section 170). The treasurer may deputize the "
            "barangay treasurer; if a bond is needed, the province, city or municipality pays the premium. "
            "Collection is never given to a private person (Section 130).",
            ("h", "Rule one: every payment gets an official receipt"),
            "\"No payment of any nature shall be received by a collecting officer without immediately issuing an "
            "official receipt in acknowledgment thereof\" (PD 1445, Section 68). The Local Government Code says "
            "the same thing in its own words: local revenue comes only from sources authorized by law or "
            "ordinance, and its collection must always be acknowledged properly (Section 305).",
            ("list", [
                "Issue the receipt at the moment of payment, never later and never before.",
                "Use receipts in serial order, one receipt per payment.",
                "Write the payor, the date, the nature of the collection and the amount in words and figures.",
                "If a receipt is spoiled, mark it \"Cancelled\" and keep all copies in the booklet. Never tear "
                "one out.",
                "Never issue a handwritten note, acknowledgment slip or private receipt in place of an official "
                "receipt.",
            ]),
            ("h", "Rule two: remit and deposit intact"),
            "Collecting officers must \"remit or deposit intact the full amounts so received and collected\" "
            "(PD 1445, Section 69). Intact means exactly what was collected: no deductions for expenses, no loans "
            "to co-workers, no cashing of personal checks, and no \"borrowing\" until tomorrow. The Local "
            "Government Code adds that every officer authorized to collect must remit the full amount to the "
            "treasury, credited to the account where it belongs (Section 307), and that all money officially "
            "received is accounted for as local funds (Section 305). Collections are deposited in the government "
            "depository bank not later than the next banking day (PD 1445, Section 69).",
            ("h", "The end-of-day routine"),
            ("list", [
                "Count the cash and checks, and compare the total with the receipts issued.",
                "Prepare the Report of Collections and Deposits (RCD). It lists the receipts by serial number, "
                "payor, nature of collection and amount; the remittances or deposits made; the accountable forms "
                "received, used and left; and a summary of collections and deposits, with a certification by the "
                "collector and a verification by the person who receives the money.",
                "Remit the collections, with the RCD, to the treasurer or cashier, or deposit them in the bank "
                "and attach the validated deposit slip.",
                "Keep each fund apart: general fund collections, Special Education Fund collections and trust "
                "fund collections are reported and deposited separately.",
            ]),
            ("h", "Separate funds, separate accounts"),
            "Every local government keeps a General Fund for money not set aside by law for another purpose "
            "(Section 308). The Special Education Fund and trust funds are special funds (Section 309). The "
            "accountant keeps separate books and the treasurer separate bank accounts for each fund (Section 310). "
            "Within the General Fund, special accounts are kept for public utilities and economic enterprises, for "
            "loans and bond issues, and for development projects funded from the national tax allotment "
            "(Section 313).",
            "Depository accounts are kept in the name of the local government with banks, preferably "
            "government-owned, in or nearest to the area, and the interest earned stays with each account "
            "(Section 311). Treasurers and other accountable officers must keep their personal money separate from "
            "public funds and may not profit from public money (Section 312).",
            ("tip", "A collector's cash drawer should hold only the day's collections and, if the treasurer has set "
                    "one up, a fixed change fund. Personal money, wallets and other people's cash belong somewhere "
                    "else. In a surprise cash count, anything in the drawer is presumed to be public money."),
            ("h", "Who checks"),
            "The books, accounts, papers and cash of the treasurer and every accountable officer are open at all "
            "times to COA (Section 348). COA's auditors examine collections, compare the deposits with the bank, "
            "and look for gaps or repeats in receipt numbers. Note 8 explains how the receipts themselves are "
            "accounted for, and Note 10 what happens when cash is short.",
        ],
        "example": (
            "Worked example: closing a collector's day",
            [
                "A collector issued official receipts numbered 4501 to 4530 today. Receipt 4517 was spoiled and "
                "marked \"Cancelled\", so 29 receipts carry money.",
                "The 29 receipts add up to ₱48,750: ₱41,250 in cash and one check for ₱7,500 payable to the "
                "municipality.",
                "The count of the drawer shows exactly ₱41,250 in bills and coins, plus the check.",
                "The RCD lists receipts 4501 to 4530, with 4517 shown as cancelled, a total of ₱48,750, and the "
                "remittance of ₱48,750 to the municipal treasurer.",
                "The treasurer deposits the ₱48,750 intact the next banking day, keeping the general fund and "
                "any trust fund collections in their own accounts.",
            ],
            "Receipts, cash and deposit all agree at ₱48,750, and no receipt number is missing.",
        ),
        "practice": [
            ("Who may collect local taxes, fees and charges?",
             ["the treasurer or a duly authorized deputy", "any employee assigned by the mayor",
              "a private collection agency", "the COA auditor"], 0,
             "Section 170: the provincial, city, municipal or barangay treasurer, or their duly authorized "
             "deputies."),
            ("When must a collecting officer issue an official receipt?",
             ["at the end of the day", "immediately upon receiving the payment", "only if the payor asks for it",
              "when the money is deposited"], 1,
             "PD 1445, Section 68: no payment of any nature is received without immediately issuing an official "
             "receipt."),
            ("What does \"deposit intact\" mean?",
             ["deposit after deducting small expenses", "deposit the exact amount collected, without deductions",
              "deposit only the cash, keep the checks", "deposit once a week"], 1,
             "PD 1445, Section 69: remit or deposit intact the full amounts received and collected."),
            ("A receipt is spoiled while being filled out. What should the collector do?",
             ["tear it out and throw it away", "mark it \"Cancelled\" and keep all copies",
              "reuse it the next day", "give it to the taxpayer anyway"], 1,
             "A cancelled receipt stays in the booklet with all its copies so every serial number is accounted "
             "for."),
            ("Which report lists the day's receipts, the deposits and the accountable forms used?",
             ["the Statement of Cash Flows", "the Report of Collections and Deposits", "the Annual Budget",
              "the Disbursement Voucher"], 1,
             "The RCD shows collections by receipt, remittances or deposits, and the accountability for "
             "accountable forms."),
            ("According to Section 311, where should the treasurer keep the local government's money?",
             ["in a personal account of the treasurer", "in banks, preferably government-owned, in or nearest "
              "to the area", "in the office vault only", "with the provincial treasurer"], 1,
             "Section 311: depository accounts in the name of the local government with banks, preferably "
             "government-owned, in or nearest to the area."),
            ("The Special Education Fund and trust funds are ____.",
             ["parts of the General Fund", "special funds kept in separate books and accounts",
              "national government funds", "kept by the school principal"], 1,
             "Sections 309 and 310: special funds, with separate books and depository accounts for each fund."),
            ("Who earns the interest on a depository account of the local government?",
             ["the treasurer", "the bank", "that same account", "the national treasury"], 2,
             "Section 311: earnings of each depository account accrue exclusively to it."),
            ("Can a treasurer keep personal money mixed with public funds in the vault?",
             ["yes, if it is recorded", "no, personal money must be kept separate", "yes, up to ₱5,000",
              "only on weekends"], 1,
             "Section 312: personal money is kept separate and distinct from public funds."),
            ("Who may inspect the books, accounts and cash of a local treasurer at any time?",
             ["the Commission on Audit", "any councilor", "the BIR", "the barangay captain"], 0,
             "Section 348: they are open at all times to inspection by COA or its authorized representative."),
        ],
        "sources": [
            "Republic Act No. 7160, Local Government Code of 1991, Sections 130, 170, 305, 307 to 313 and 348",
            "Presidential Decree No. 1445, Government Auditing Code of the Philippines, Sections 68 and 69",
        ],
    },
    # ------------------------------------------------------------------ Note 8
    {
        "number": 8,
        "slug": "accountable-forms-and-raaf",
        "title": "Accountable forms and the RAAF",
        "summary": "What accountable forms are, how they move from the supplier to the collector and back, and "
                   "how the Report of Accountability for Accountable Forms keeps every serial number accounted "
                   "for.",
        "publish_on": "2026-12-25 21:00",
        "body": [
            "An official receipt is worth nothing blank, and yet a missing blank receipt can cause more trouble "
            "than missing cash. Anyone holding it could collect money that never reaches the treasury. That is why "
            "official receipts, community tax certificates and similar printed forms are called accountable forms: "
            "the officer who holds them answers for every one, by serial number, until it is used, cancelled or "
            "returned.",
            ("h", "What counts as an accountable form"),
            ("list", [
                "Official receipts for general collections. Accountable Form No. 51 is the official receipt most "
                "local treasuries use for taxes, fees and charges.",
                "Official receipts for real property tax, commonly Accountable Form No. 56, which show the "
                "property, the assessed value, and the basic tax and SEF separately.",
                "Community tax certificates for individuals and for corporations (Note 5).",
                "Cash tickets and other forms with a printed money value, such as those sold at markets or "
                "terminals.",
            ]),
            "Some forms carry a printed value, like a ₱5 cash ticket; most, like official receipts, do not. Both "
            "kinds are counted and reported by serial number. For a form with a printed value, a missing piece "
            "can mean a liability for its face value.",
            ("h", "The life of a booklet"),
            ("list", [
                "Supply. A municipal treasurer usually requests stocks from the provincial treasurer. One "
                "provincial office, for example, issues accountable forms on a Requisition and Issue Voucher "
                "with an Invoice and Receipt of Accountable Forms.",
                "Custody. The treasurer keeps the stock in a safe place and records every booklet received, by "
                "form number and serial numbers.",
                "Issue. Booklets are issued to collectors in serial order, and the collector signs for them. "
                "From that moment, the collector is accountable for every receipt in the booklet.",
                "Use. Receipts are used in serial order, one per payment. A spoiled receipt is marked "
                "\"Cancelled\" with all copies left in the booklet.",
                "Return. A finished booklet, with its duplicate and triplicate copies, is returned to the "
                "treasurer and kept for audit.",
            ]),
            ("h", "The RAAF"),
            "The Report of Accountability for Accountable Forms, or RAAF, is how a collector or the treasurer "
            "reports the forms in their care. For each kind of form, it shows four things, each with the quantity "
            "and the first and last serial numbers:",
            ("table", ["Column", "What it shows"], [
                ["Beginning balance", "Forms on hand at the start of the period"],
                ["Receipts", "Forms received during the period"],
                ["Issued", "Forms used (including cancelled ones) or issued to others during the period"],
                ["Ending balance", "Forms still on hand at the end of the period"],
            ]),
            "The arithmetic must always hold: beginning balance plus receipts, minus issued, equals ending "
            "balance. The RAAF is prepared monthly and goes to the accountant, who checks it against the "
            "collections recorded; the same section appears in each Report of Collections and Deposits (Note 7). "
            "COA auditors match the serial numbers on the RAAF against the receipts, the RCDs and the deposits.",
            ("tip", "Gaps and repeats are what auditors look for first. If receipt 4517 appears in no RCD and is "
                    "not marked cancelled, someone must explain where it went."),
            ("h", "When forms are lost"),
            "A lost booklet or receipt must be reported at once to the treasurer and to the COA auditor. When "
            "government funds or property are lost in transit or through fire, theft or other casualty, the "
            "accountable officer must notify COA immediately and file an application for relief, with "
            "supporting evidence, within 30 days (PD 1445, Section 73). Credit is given only when the evidence "
            "shows the loss was not due to the officer's negligence.",
            ("h", "Habits that keep a collector safe"),
            ("list", [
                "Never sign or pre-fill receipts in advance.",
                "Never lend a booklet to a co-worker, even for a few minutes. The collector who signed for it "
                "answers for it.",
                "Never use a receipt from a booklet issued to someone else.",
                "Lock unused booklets away at the end of the day, and count them when you start.",
                "Report a missing receipt the same day it is discovered.",
            ]),
        ],
        "example": (
            "Worked example: one month of a RAAF line",
            [
                "On June 1, a collector holds two booklets of Accountable Form No. 51, serial numbers 12401 to "
                "12500: 100 receipts.",
                "On June 10, the treasurer issues five more booklets, 12501 to 12750: 250 receipts.",
                "During June, the collector uses receipts 12401 to 12580, including two cancelled ones: 180 "
                "receipts.",
                "Ending balance: 100 + 250 − 180 = 170 receipts, serial numbers 12581 to 12750.",
                "Check: 12750 − 12581 + 1 = 170. The numbers agree.",
            ],
            "The June RAAF shows 100 + 250 − 180 = 170, and the serial numbers 12581 to 12750 confirm it.",
        ),
        "practice": [
            ("Why are official receipts called accountable forms?",
             ["because they cost money to print", "because the holder answers for every one by serial number",
              "because only accountants may use them", "because COA prints them"], 1,
             "Each form is accounted for by serial number until it is used, cancelled or returned."),
            ("What does RAAF stand for?",
             ["Report on Audit of Annual Finances", "Report of Accountability for Accountable Forms",
              "Record of Assessed and Appraised Forms", "Register of Accounts and Funds"], 1,
             "The Report of Accountability for Accountable Forms."),
            ("Which formula must always hold in a RAAF?",
             ["beginning + receipts − issued = ending", "beginning − receipts + issued = ending",
              "receipts − issued = beginning", "ending + issued = receipts"], 0,
             "Beginning balance plus receipts, minus issued, equals ending balance."),
            ("A collector has 40 receipts on hand, receives 50 and uses 65. How many are left?",
             ["15", "25", "35", "55"], 1,
             "40 + 50 − 65 = 25."),
            ("A receipt is spoiled. What happens to it in the RAAF?",
             ["it is left out", "it is reported among the forms issued, as cancelled",
              "it is added back to the ending balance", "it is reported as lost"], 1,
             "A cancelled receipt is used up; it is reported among the forms issued and kept in the booklet."),
            ("Which form is commonly used as the official receipt for real property tax?",
             ["Accountable Form No. 51", "Accountable Form No. 56", "the community tax certificate",
              "the cash ticket"], 1,
             "Accountable Form No. 56 shows the property, the assessed value, and the basic tax and SEF."),
            ("A collector's booklet is stolen. Within what period should the application for relief be filed "
             "with COA?",
             ["7 days", "15 days", "30 days", "one year"], 2,
             "PD 1445, Section 73: notify COA immediately and file the application for relief within 30 days."),
            ("A co-worker asks to borrow your receipt booklet for a few minutes. What should you do?",
             ["lend it and record the numbers", "refuse; the collector who signed for it answers for it",
              "lend it if the supervisor agrees verbally", "give the co-worker a few loose receipts"], 1,
             "Accountability follows the person who signed for the booklet; never lend it."),
            ("What do auditors look for first when checking receipts?",
             ["the color of the forms", "gaps and repeats in serial numbers", "the collector's handwriting",
              "the paper quality"], 1,
             "A missing or repeated number signals collections that may not have reached the treasury."),
            ("How often is the RAAF usually prepared?",
             ["daily", "monthly", "every six months", "once a year"], 1,
             "It is prepared monthly, and the same accountability section appears in each RCD."),
        ],
        "sources": [
            "Presidential Decree No. 1445, Government Auditing Code of the Philippines, Sections 68 and 73",
            "Commission on Audit, Government Accounting Manual for Local Government Units (forms and reports)",
        ],
    },
    # ------------------------------------------------------------------ Note 9
    {
        "number": 9,
        "slug": "disbursements-vouchers-checks-cash-advances",
        "title": "Disbursements: vouchers, checks and cash advances",
        "summary": "The certifications every payment needs, who signs the voucher and the check, the limit on "
                   "spending ahead of collections, and the rules for cash advances.",
        "publish_on": "2027-01-01 21:00",
        "body": [
            "Collecting money is half of treasury work. The other half is paying it out, and the law is stricter "
            "there. A collector who makes a mistake can usually correct it; an officer who approves an unlawful "
            "payment may have to pay it back personally (Section 351). This note covers the rules for paying out "
            "local funds under the Local Government Code (RA 7160), the Government Auditing Code (PD 1445) and "
            "COA's rules on cash advances.",
            ("h", "The first principles"),
            ("list", [
                "No money is paid out of the local treasury except under an appropriation ordinance or law "
                "(Section 305).",
                "Local funds are spent only for public purposes, and never for religious or private purposes "
                "(Sections 305 and 335).",
                "Trust funds are paid out only for the purpose of the trust (Section 305).",
                "Appropriated funds are used only for the purpose they were appropriated for (Section 336).",
                "No payment is made on a contract before the services are rendered or the goods delivered "
                "(Section 338).",
            ]),
            ("h", "Three certifications and an approval (Section 344)"),
            "No money may be disbursed unless:",
            ("list", [
                "the local budget officer certifies that an appropriation exists for the purpose;",
                "the local accountant has obligated that appropriation; and",
                "the local treasurer certifies that funds are available.",
            ]),
            "The head of the office with administrative control of the fund certifies the voucher or payroll as "
            "to the validity, propriety and legality of the claim. The local chief executive then approves the "
            "voucher, except for regularly recurring administrative expenses such as payrolls for regular "
            "employees; light, water and telephone bills; and remittances to government creditors such as the "
            "GSIS, SSS, Land Bank, DBP, the National Printing Office and the Procurement Service. For special or "
            "trust funds, the administrator of the fund approves. When a department head is temporarily absent, "
            "the next-in-rank officer performs the function and is fully responsible for it.",
            ("h", "Who signs the check"),
            "Checks are drawn by the local treasurer and countersigned by the local administrator. If either is "
            "temporarily absent or incapacitated, the duty passes to their immediate assistant (Section 345).",
            ("h", "Spending ahead of collections (Section 337)"),
            "Disbursements may come from any local fund in the treasurer's custody, but total disbursements from a "
            "fund may not exceed its actual collections plus 50% of its uncollected estimated revenue. There may "
            "be no cash overdraft in any fund at the end of the year. In a calamity, the sanggunian may let the "
            "treasurer go beyond this limit, but only for items in the approved budget, and any overdraft is "
            "covered by the first collections of the next year.",
            ("h", "Cash advances"),
            "No cash advance may be granted to any local official or employee except under COA's rules "
            "(Section 339). A cash advance is given only for a specific, legally authorized purpose, and no new "
            "advance is given until the previous one is settled (PD 1445, Section 89). COA Circular No. 97-002 "
            "sets the details:",
            ("list", [
                "Only permanently appointed officials may be designated disbursing officers. Elected officials "
                "may get cash advances only for official travel.",
                "A cash advance may not be transferred from one accountable officer to another.",
                "Payments from a petty cash fund are capped at ₱15,000 per transaction, and splitting a "
                "purchase to stay under the cap is not allowed.",
                "Salaries and wages are liquidated within 5 days after each pay period.",
                "Petty operating and field expenses are liquidated within 20 days after the end of the year.",
                "Local travel is liquidated within 30 days after returning to the official station; foreign "
                "travel within 60 days after returning to the Philippines.",
                "All cash advances are liquidated at year-end, and unused balances are refunded.",
                "If an advance is not liquidated on time, the officer's salary may be withheld, and the officer "
                "may face administrative and criminal charges.",
            ]),
            ("h", "Liability and transparency"),
            "The treasurer, accountant, budget officer or other accountable officer who acts on the order of a "
            "superior is not relieved of liability for an illegal use of funds unless they register their "
            "objection in writing; the superior who gave the order is jointly and severally liable "
            "(Section 342). Spending for entertainment or receptions is limited to authorized representation "
            "allowances and a few listed cases (Section 343). The accountant gives the sanggunian monthly "
            "financial statements within 30 days after each month, and the year-end statements within 60 days "
            "after December 31 (Section 346). Within 30 days after the year ends, a summary of all revenues "
            "collected and funds received, and the appropriations and disbursements, is posted in at least three "
            "public places (Section 352).",
        ],
        "example": (
            "Worked example: the 50% limit and a travel advance",
            [
                "A municipality's General Fund expects ₱100 million in revenue this year. By the end of August it "
                "has collected ₱60 million, so ₱40 million is still uncollected.",
                "Section 337 limit: ₱60 million + 50% × ₱40 million = ₱80 million. Total disbursements from the "
                "General Fund may not exceed ₱80 million at this point.",
                "Separately, an employee gets a ₱5,000 cash advance for a seminar in another province and "
                "returns to the office on March 6.",
                "Local travel must be liquidated within 30 days after return: March 6 + 30 days = April 5.",
                "If the employee spent ₱4,200, the liquidation report shows ₱4,200 in expenses and the ₱800 "
                "balance is refunded with an official receipt.",
            ],
            "The fund may disburse up to ₱80 million so far, and the travel advance is liquidated by April 5 "
            "with ₱800 returned.",
        ),
        "practice": [
            ("Which officer certifies that funds are available before a payment?",
             ["the local budget officer", "the local accountant", "the local treasurer", "the mayor"], 2,
             "Section 344: the budget officer certifies the appropriation, the accountant obligates it, and the "
             "treasurer certifies the availability of funds."),
            ("Who countersigns checks drawn by the local treasurer?",
             ["the local accountant", "the local administrator", "the vice mayor", "the COA auditor"], 1,
             "Section 345: checks are drawn by the treasurer and countersigned by the local administrator."),
            ("Which payment does NOT need the local chief executive's own approval on the voucher?",
             ["a contractor's progress billing", "a payroll for regular employees", "a purchase of equipment",
              "a cash advance for travel"], 1,
             "Section 344 exempts regularly recurring expenses such as payrolls for regular employees and "
             "utility bills."),
            ("A town has collected ₱30 million and expects ₱20 million more. What is the most its fund may "
             "disburse now?",
             ["₱30 million", "₱40 million", "₱50 million", "₱60 million"], 1,
             "Section 337: ₱30 million + 50% × ₱20 million = ₱40 million."),
            ("May a supplier be paid before delivering the goods?",
             ["yes, if the mayor approves", "no, advance payment is prohibited", "yes, up to 15%",
              "yes, for emergency purchases only"], 1,
             "Section 338: no money is paid on a contract under which no services were rendered or goods "
             "delivered."),
            ("Within what period must a cash advance for local travel be liquidated?",
             ["5 days after return", "20 days after return", "30 days after return", "60 days after return"], 2,
             "COA Circular No. 97-002: within 30 days after returning to the official station; 60 days for "
             "foreign travel."),
            ("An employee has an unliquidated cash advance and asks for a new one. What is the rule?",
             ["grant it if the amount is small", "no new advance until the previous one is settled",
              "grant it with the mayor's approval", "grant it and deduct the old one later"], 1,
             "PD 1445, Section 89, and COA Circular No. 97-002."),
            ("What is the cap per transaction for payments from a petty cash fund under COA Circular No. 97-002?",
             ["₱5,000", "₱10,000", "₱15,000", "₱50,000"], 2,
             "₱15,000 per transaction, and splitting purchases to avoid the cap is prohibited."),
            ("A treasurer releases funds illegally on the mayor's order without objecting in writing. Who is "
             "liable?",
             ["only the mayor", "only the treasurer", "both, jointly and severally", "nobody, it was an order"], 2,
             "Section 342: the treasurer is not relieved unless they object in writing, and the superior is "
             "jointly and severally liable."),
            ("Within how many days after the year ends must the summary of revenues and disbursements be "
             "posted?",
             ["15 days", "30 days", "60 days", "90 days"], 1,
             "Section 352: within 30 days, in at least three publicly accessible and conspicuous places."),
        ],
        "sources": [
            "Republic Act No. 7160, Local Government Code of 1991, Sections 305, 335 to 346, 351 and 352",
            "Presidential Decree No. 1445, Government Auditing Code of the Philippines, Section 89",
            "Commission on Audit Circular No. 97-002 (February 10, 1997), rules on cash advances",
        ],
    },
    # ------------------------------------------------------------------ Note 10
    {
        "number": 10,
        "slug": "accountability-bonds-cash-counts-shortages",
        "title": "Accountability: bonds, cash counts and shortages",
        "summary": "Who is an accountable officer, why they must be bonded, what happens during a cash count, "
                   "and what the law says when cash or property is short or lost.",
        "publish_on": "2027-01-08 21:00",
        "body": [
            "Every note in this series ends in the same place: someone must answer for public money. This last "
            "note is about that person, the accountable officer, and the rules that protect both the public and "
            "the officer: bonds, cash examinations, and the law on shortages and losses.",
            ("h", "Who is accountable"),
            "Any officer whose duties permit or require the possession or custody of local government funds is "
            "accountable for them and for their safekeeping (Section 340; PD 1445, Section 101). That covers "
            "treasurers, cashiers, collectors, disbursing officers, and deputized barangay treasurers. Other "
            "officers who are not accountable by the nature of their duties may still be held accountable through "
            "their participation in the use or application of the funds, for example by signing a voucher or "
            "approving a payment (Section 340).",
            ("h", "Bonds"),
            "Every officer whose duties permit or require the possession or custody of local funds must be "
            "properly bonded (Section 305; PD 1445, Section 101). The bond is a fidelity bond issued through the "
            "Bureau of the Treasury, now under Treasury Circular No. 02-2019, which treats any officer whose "
            "duties involve the possession, custody or control of public funds or property as a bondable officer. "
            "The amount of the bond is based on the officer's maximum accountability; for a collector, this is "
            "usually worked out from their average collections. When the city or municipal treasurer deputizes barangay treasurers to collect real "
            "property tax or the community tax, they must be bonded, and the city or municipality pays the premium "
            "(Sections 164, 170 and 247).",
            ("tip", "The bond protects the government, not the officer. If a bonded officer is found short, the "
                    "government may recover from the bond, and the officer remains liable for the full amount."),
            ("h", "Primary and secondary responsibility"),
            "The head of each agency is immediately and primarily responsible for all its government funds and "
            "property; those under the head who hold funds or property are responsible to the head (PD 1445, "
            "Section 102). Heads must supervise accountable officers with \"the diligence of a good father of a "
            "family\"; one who fails to do so may be jointly and solidarily liable for a loss, and local "
            "treasurers have the same duty over the accountable officers under them (PD 1445, Section 104).",
            ("h", "How much an officer must answer for"),
            "An officer accountable for funds is liable for all losses from their unlawful deposit, use or "
            "application, and for losses caused by negligence in keeping them (PD 1445, Section 105). An officer "
            "accountable for property is liable for its money value if it is misused, and for loss or damage "
            "from negligence, whether or not it was in their actual custody at the time. Acting on a superior's "
            "order is no excuse unless the officer objected in writing (Section 342; PD 1445, Section 106). "
            "Spending in violation of the law is the personal liability of the official responsible "
            "(Section 351).",
            ("h", "Cash counts"),
            "The books, accounts, papers and cash of the treasurer and every accountable officer are open to COA "
            "at all times (Section 348). In a cash examination, the auditor counts the cash and checks on hand, "
            "lists the official receipts issued since the last deposit, and compares the two. Cash on hand plus "
            "deposits not yet credited must equal the accountability shown by the records.",
            "If a local treasurer is found short, the law is strict (Section 348):",
            ("list", [
                "the examining officer takes over the office and its contents and notifies COA, the local chief "
                "executive and the local accountant;",
                "the office is turned over to the next-in-rank accountable officer in the treasury, unless that "
                "officer is also under investigation, in which case the auditor runs the office;",
                "the treasurer's accounts are closed on the date of turnover; and",
                "the treasurer or accountable officer found short is automatically suspended.",
            ]),
            "A shortage is also a criminal matter. Under Article 217 of the Revised Penal Code, the failure of a "
            "public officer to produce public funds or property on demand by an authorized officer is prima facie "
            "evidence that they used it for personal purposes. That is malversation, one of the most serious "
            "offenses a treasury worker can face.",
            ("h", "Losses that are not the officer's fault"),
            "Fire, theft, robbery, flood and other casualties happen. When public funds or property are lost in "
            "transit or through casualty or force majeure, the officer must notify COA immediately and file an "
            "application for relief, with the available evidence, within 30 days (PD 1445, Section 73; Section "
            "378 of the Code has the same rule for property). Credit is allowed only when the evidence shows the "
            "loss happened without the officer's fault or negligence. Missing the deadline can cost the officer "
            "the relief.",
            ("h", "Habits that keep an accountable officer safe"),
            ("list", [
                "Deposit intact and on time. Cash that stays in the vault longer than it should is exposed to "
                "loss and to suspicion.",
                "Never mix personal money with public funds (Section 312), and never lend public money, even "
                "for a day.",
                "Count your own cash every day and keep the records that prove each count.",
                "Keep your bond current and know your maximum accountability.",
                "Object in writing to any order you believe is illegal (Section 342).",
                "Report any loss at once, and file for relief within 30 days.",
            ]),
        ],
        "example": (
            "Worked example: a surprise cash count",
            [
                "An auditor arrives at 3 pm and counts a collector's cash. The last deposit covered receipts up "
                "to number 7820.",
                "Receipts 7821 to 7864 were issued today, totaling ₱38,450. That is the collector's "
                "accountability for undeposited collections.",
                "The count finds ₱37,950 in bills and coins and one check for ₱300 payable to the municipality: "
                "₱38,250 in all.",
                "Shortage: ₱38,450 − ₱38,250 = ₱200.",
                "The collector must explain and restore the ₱200 at once. An unexplained shortage, and a failure "
                "to produce the money on demand, is evidence of malversation.",
            ],
            "A ₱200 shortage. Small amounts still matter: the law looks at whether public money was produced on "
            "demand, not at its size.",
        ),
        "practice": [
            ("Who is an accountable officer?",
             ["anyone employed by the local government", "an officer whose duties permit or require custody "
              "of public funds", "only the local treasurer", "only elected officials"], 1,
             "Section 340 and PD 1445, Section 101: any officer whose duties permit or require the possession "
             "or custody of public funds."),
            ("Which law requires every accountable officer to be properly bonded?",
             ["RA 6713", "PD 1445, Section 101", "RA 9184", "RA 11032"], 1,
             "PD 1445, Section 101, and Section 305 of the Local Government Code."),
            ("Who pays the premium on the bond of a barangay treasurer deputized to collect real property tax?",
             ["the barangay treasurer", "the barangay", "the city or municipality", "the province"], 2,
             "Section 247: the premium is paid by the city or municipal government concerned."),
            ("Under PD 1445, who is immediately and primarily responsible for all government funds and property "
             "of an agency?",
             ["the COA auditor", "the head of the agency", "the cashier", "the accountant"], 1,
             "PD 1445, Section 102."),
            ("A cash examination finds a local treasurer short. What happens to the treasurer?",
             ["nothing until a court decides", "automatic suspension from office", "a warning",
              "transfer to another office"], 1,
             "Section 348: the treasurer or accountable officer found with a shortage is automatically "
             "suspended."),
            ("Under Article 217 of the Revised Penal Code, failure to produce public funds on demand is ____.",
             ["a minor violation", "prima facie evidence of malversation", "proof of negligence only",
              "not an offense"], 1,
             "It is prima facie evidence that the officer put the missing funds to personal use."),
            ("Public funds are stolen from a collector during a robbery. Within what period must the application "
             "for relief be filed?",
             ["7 days", "15 days", "30 days", "90 days"], 2,
             "PD 1445, Section 73: notify COA immediately, and apply for relief within 30 days."),
            ("A collector's records show ₱25,600 in undeposited collections. The count finds ₱25,150. What is "
             "the shortage?",
             ["₱350", "₱450", "₱550", "₱650"], 1,
             "₱25,600 − ₱25,150 = ₱450."),
            ("An accountable officer releases funds illegally on a superior's order. When is the officer "
             "relieved of liability?",
             ["always", "never", "only if the officer objected in writing", "only if the amount is small"], 2,
             "Section 342 and PD 1445, Section 106: unless the officer objected in writing."),
            ("What does a fidelity bond protect?",
             ["the officer from any liability", "the government against loss from the bonded officer",
              "the taxpayer's payments", "the bank"], 1,
             "The bond protects the government; the officer remains liable for any shortage."),
        ],
        "sources": [
            "Republic Act No. 7160, Local Government Code of 1991, Sections 164, 170, 247, 305, 312, 340, 342, "
            "348, 351 and 378",
            "Presidential Decree No. 1445, Government Auditing Code of the Philippines, Sections 73, 101 to 106",
            "Act No. 3815, Revised Penal Code, Article 217 (malversation)",
            "Bureau of the Treasury, Treasury Circular No. 02-2019 (fidelity bonds)",
        ],
    },
]


def _spread(practice):
    """Move the right answer around A to D so it is not usually B. Choices that are amounts or periods
    (they start with a digit or ₱) keep their order from smallest to largest."""
    targets = [0, 2, 3, 1]
    out = []
    for i, (q, choices, ans, why) in enumerate(practice):
        if not any(c[0].isdigit() or c[0] == "₱" for c in choices):
            right = choices[ans]
            others = [c for j, c in enumerate(choices) if j != ans]
            ans = targets[i % 4]
            choices = others[:ans] + [right] + others[ans:]
        out.append((q, choices, ans, why))
    return out


for _n in NOTES_2_TO_10:
    _n["practice"] = _spread(_n["practice"])
