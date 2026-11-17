"""Study Notes 11 to 15 (Butch said "Yes. Follow the same." 2026-11-18 PH: all five proposed topics,
Tuesdays and Fridays at 9 pm, December 11 to 25, 2026).

Same shape as Notes 2 to 10. Facts checked (November 2026) against:
- RA 7160 Book II text (Butch's Drive copy) and chanrobles.com for Section 245;
- NIRC as amended by RA 10963 (TRAIN), Sections 24(A)(2)(a), 32(B)(7)(e), 58(A), 114(C) (lawphil);
- RR No. 2-98 Section 2.57.2(J) as amended by RR No. 11-2018 (KPMG copy of the RR);
- BIR RMC No. 59-2023 (via PwC Tax Alert 20) on creditable VAT withholding since January 1, 2021;
- RA 6713 Sections 4, 5, 7, 8, 11 and RA 3019 Sections 3, 7, 9, 11, 13, 14 (lawphil), BP 195 (chanrobles),
  RA 10910 (lawphil);
- COA Memorandum No. 2013-004 (Revised Cash Examination Manual) and the contents of the Government
  Accounting Manual for LGUs, Volume II.
No Wikipedia sources. Worked examples and quiz answers recomputed.
"""

from notes_2_10 import _spread

NOTES_11_TO_15 = [
    # ------------------------------------------------------------------ Note 11
    {
        "number": 11,
        "slug": "taxes-withheld-for-the-bir",
        "title": "Taxes the treasury withholds for the BIR",
        "summary": "Why a local government deducts national taxes from what it pays suppliers and employees, "
                   "the rates on goods, services and VAT, and how the money reaches the BIR.",
        "publish_on": "2026-12-11 21:00",
        "body": [
            "Notes 1 to 10 were about money a local government collects for itself. This note is about money it "
            "holds for someone else. Every time a local government pays a supplier or an employee, part of the "
            "payment is a national tax that the law asks the payer to deduct and send to the Bureau of Internal "
            "Revenue (BIR). The payer is then called a withholding agent. Unless stated otherwise, the sections "
            "cited are from the National Internal Revenue Code (NIRC), as amended by the TRAIN Law (RA 10963).",
            ("h", "Why withhold at all"),
            "Withholding collects a tax at the moment income is paid, instead of waiting for the taxpayer to file. "
            "Section 57 allows the BIR to require it, and Revenue Regulations No. 2-98 lists who withholds and at "
            "what rate. The amount deducted is not the local government's money. It is held only until it is "
            "remitted to the BIR.",
            ("h", "What a local government withholds"),
            ("table", ["What is paid", "What is withheld"], [
                ["Purchases of goods from a local supplier",
                 "Expanded withholding tax of 1% of the price before VAT, except on a single purchase of "
                 "₱10,000 or less (RR 2-98, Section 2.57.2(J), as amended by RR 11-2018)"],
                ["Purchases of services from a local supplier",
                 "Expanded withholding tax of 2% of the price before VAT, with the same ₱10,000 exception"],
                ["Purchases from a VAT-registered supplier",
                 "VAT of 5% of the payment (Section 114(C)). Since January 1, 2021 this is creditable: the "
                 "supplier deducts it from the VAT it owes."],
                ["Salaries and wages of employees",
                 "Income tax on compensation, computed with the graduated table in Section 24(A)(2)(a)"],
            ]),
            "The rule in Section 2.57.2(J) covers income payments by \"a government office, national or local, "
            "including barangays\". A barangay that buys supplies above ₱10,000 withholds just as a province "
            "does.",
            ("tip", "Rates and forms change. Before applying a rate, check the BIR's latest revenue regulations "
                    "and tax calendar. This note gives the rules in force when it was written."),
            ("h", "The base: the price before VAT"),
            "The expanded withholding tax and the 5% VAT are both computed on the price before VAT, not on the "
            "total that includes VAT. If an invoice shows ₱100,000 plus ₱12,000 VAT, the base is ₱100,000.",
            ("h", "Tax on salaries"),
            "From January 1, 2023, the first ₱250,000 of taxable compensation a year is not taxed. The excess "
            "up to ₱400,000 is taxed at 15%, then ₱22,500 plus 20% of the excess over ₱400,000, and so on up to "
            "35% above ₱8 million (Section 24(A)(2)(a)). Thirteenth-month pay and other benefits are not "
            "taxable up to ₱90,000 a year (Section 32(B)(7)(e)). The employer withholds a share of the yearly "
            "tax from each pay.",
            ("h", "Sending the money to the BIR"),
            "For creditable withholding taxes, the return is filed and the tax paid not later than the last day "
            "of the month after the close of the quarter in which they were withheld (Section 58(A)). The BIR also sets "
            "monthly remittance forms and due dates in its regulations. The payee receives a certificate of the "
            "tax withheld: BIR Form No. 2307 for a supplier and BIR Form No. 2316 for an employee. The supplier "
            "or employee uses it to claim credit for the tax.",
            ("list", [
                "Deduct the tax before the payment is released.",
                "Keep each deduction recorded by payee, type and rate, so the quarterly return and the "
                "certificates agree.",
                "Remit the full amount. Withheld tax is never used to pay the local government's own bills.",
                "Give every supplier its certificate, so it can claim the credit.",
            ]),
        ],
        "example": (
            "Worked example: paying a VAT-registered supplier of goods",
            [
                "A municipality buys office supplies. The invoice shows ₱100,000 plus ₱12,000 VAT: ₱112,000 "
                "in all.",
                "Base for withholding: ₱100,000, the price before VAT.",
                "Expanded withholding tax on goods: 1% × ₱100,000 = ₱1,000.",
                "VAT withheld: 5% × ₱100,000 = ₱5,000.",
                "Check issued to the supplier: ₱112,000 − ₱1,000 − ₱5,000 = ₱106,000.",
                "The ₱6,000 is remitted to the BIR, and the supplier gets a BIR Form No. 2307 for it.",
                "Now an employee with taxable compensation of ₱360,000 a year: (₱360,000 − ₱250,000) × 15% = "
                "₱16,500 a year, or ₱1,375 a month.",
            ],
            "The supplier receives ₱106,000 and a certificate for ₱6,000. The employee has ₱1,375 withheld "
            "each month.",
        ),
        "practice": [
            ("When a local government deducts a national tax from a payment, it acts as a ____.",
             ["withholding agent", "tax assessor", "collecting bank", "revenue district office"], 0,
             "The payer who deducts and remits the tax is the withholding agent (Section 57)."),
            ("What rate of expanded withholding tax applies to a government purchase of goods above ₱10,000?",
             ["1%", "2%", "5%", "10%"], 0,
             "RR 2-98, Section 2.57.2(J), as amended: 1% on goods and 2% on services."),
            ("What rate of expanded withholding tax applies to a government payment for services?",
             ["1%", "2%", "5%", "15%"], 1,
             "RR 2-98, Section 2.57.2(J), as amended: 2% on services."),
            ("Which single purchase is NOT subject to the expanded withholding tax on government payments?",
             ["₱8,000", "₱12,000", "₱50,000", "₱150,000"], 0,
             "Section 2.57.2(J) excepts any single purchase of ₱10,000 and below."),
            ("How much VAT does a government office withhold on payments to a VAT-registered supplier?",
             ["1%", "3%", "5%", "12%"], 2,
             "Section 114(C): 5% of the payment."),
            ("Since January 1, 2021, the VAT withheld by government is ____.",
             ["creditable against the supplier's VAT", "a final tax", "refunded to the local government",
              "kept in the trust fund"], 0,
             "Section 114(C), as amended by the TRAIN Law, shifted the system from final to creditable."),
            ("An invoice shows ₱50,000 plus ₱6,000 VAT for services. How much expanded withholding tax is "
             "withheld?",
             ["₱500", "₱1,000", "₱1,120", "₱2,500"], 1,
             "2% of the price before VAT: 2% × ₱50,000 = ₱1,000."),
            ("Which certificate does a supplier receive for taxes withheld from its payment?",
             ["BIR Form No. 2307", "BIR Form No. 2316", "the official receipt", "the RAAF"], 0,
             "BIR Form No. 2307 is the certificate of creditable tax withheld; Form No. 2316 is for employees."),
            ("An employee's taxable compensation is ₱300,000 a year. What is the yearly tax?",
             ["₱0", "₱7,500", "₱15,000", "₱45,000"], 1,
             "(₱300,000 − ₱250,000) × 15% = ₱7,500 (Section 24(A)(2)(a))."),
            ("Up to how much of thirteenth-month pay and other benefits is excluded from taxable income each "
             "year?",
             ["₱30,000", "₱82,000", "₱90,000", "₱250,000"], 2,
             "Section 32(B)(7)(e): up to ₱90,000."),
        ],
        "sources": [
            "National Internal Revenue Code, as amended by Republic Act No. 10963 (TRAIN Law), Sections 24(A)(2)(a), "
            "32(B)(7)(e), 57, 58(A) and 114(C)",
            "Revenue Regulations No. 2-98, Section 2.57.2(J), as amended by Revenue Regulations No. 11-2018",
            "Revenue Memorandum Circular No. 59-2023 (creditable VAT withholding from January 1, 2021)",
        ],
    },
    # ------------------------------------------------------------------ Note 12
    {
        "number": 12,
        "slug": "special-levy-on-benefited-land",
        "title": "Special levy on land that gains from public works",
        "summary": "How a province, city or municipality can recover part of the cost of a road, drainage or "
                   "other project from the lands that gain the most from it.",
        "publish_on": "2026-12-15 21:00",
        "body": [
            "When a local government builds a road, a drainage canal or a flood wall, the lots beside it gain. "
            "They are easier to reach, safer from flooding, and worth more. The Local Government Code lets the "
            "local government ask those landowners to share part of the cost. This is the special levy, found in "
            "Sections 240 to 245 of RA 7160. Unless stated otherwise, the sections cited are from that Code.",
            ("h", "Who may impose it"),
            "A province, a city or a municipality may impose a special levy on lands within its territory that "
            "are specially benefited by public works projects or improvements it funded (Section 240). Note that "
            "a municipality outside Metro Manila has this power even though it does not levy the basic real "
            "property tax (Note 2). The "
            "project must be funded by the local government that imposes the levy.",
            ("h", "The limits"),
            ("list", [
                "The levy may not exceed 60% of the actual cost of the project, including the cost of acquiring "
                "land and other real property for it (Section 240).",
                "It does not apply to lands exempt from the basic real property tax (Section 240).",
                "It does not apply to the remainder of a land whose owner donated part of it to the local "
                "government for the project (Section 240).",
                "It is paid in annual installments, never fewer than five nor more than ten years (Section 241).",
            ]),
            ("h", "The ordinance"),
            "The levy is imposed by a tax ordinance. It must describe the nature, extent and location of the "
            "project, state the estimated cost, mark the benefited area by metes and bounds, and set the number "
            "of annual installments (Section 241). The sanggunian does not have to use one uniform rate for the "
            "whole district. It may set different rates for different parts, depending on how much each part "
            "gains (Section 241).",
            "Before the ordinance is passed, the sanggunian holds a public hearing and notifies the affected "
            "owners in writing of its date and place, so they can state their positions or objections "
            "(Section 242).",
            ("h", "How each lot's share is computed"),
            "The levy is apportioned according to the assessed value of the affected lands, as shown in the "
            "assessor's books. Once the ordinance takes effect, the assessor determines the annual amount for "
            "each parcel and sends each owner a written notice (Section 243). An owner who disagrees may use the "
            "same remedies as for an assessment of real property, starting with an appeal to the Local Board of "
            "Assessment Appeals (Section 244; see Note 2).",
            ("h", "When it is due, and the treasury's part"),
            "The special levy accrues on the first day of the quarter next following the effectivity of the "
            "ordinance (Section 245). It is levied under the same title of the Code as the real property tax, and "
            "several collection rules cover \"any other tax levied under this Title\": late payments earn "
            "interest of 2% a month for up to 36 months (Section 255), the local government may collect by "
            "levy on the property or by court action (Section 256), and the tax is a lien on the property "
            "(Section 257).",
            ("tip", "For the treasury, a special levy is a multi-year receivable tied to specific lots. Keep a "
                    "schedule by parcel and installment year, so each official receipt shows which year of the "
                    "levy it pays."),
        ],
        "example": (
            "Worked example: a drainage project",
            [
                "A municipality spends ₱10,000,000 on a drainage canal. The lots it protects have a combined "
                "assessed value of ₱40,000,000.",
                "Maximum levy: 60% × ₱10,000,000 = ₱6,000,000 (Section 240).",
                "The ordinance uses one rate for the whole area. A lot assessed at ₱200,000 carries "
                "₱200,000 ÷ ₱40,000,000 = 0.5% of the levy: 0.5% × ₱6,000,000 = ₱30,000.",
                "The ordinance sets ten annual installments, the most Section 241 allows: ₱30,000 ÷ 10 = "
                "₱3,000 a year.",
                "If one year's installment is paid three months late, interest at 2% a month for 3 months is "
                "6% × ₱3,000 = ₱180 (Section 255).",
            ],
            "The owner pays ₱3,000 a year for ten years, and ₱3,180 for a year paid three months late.",
        ),
        "practice": [
            ("Which local governments may impose a special levy?",
             ["provinces, cities and municipalities", "provinces only", "barangays only",
              "the national government only"], 0,
             "Section 240: a province, city or municipality, for projects it funded."),
            ("What is the most a special levy may recover?",
             ["25% of the project cost", "50% of the project cost", "60% of the project cost",
              "100% of the project cost"], 2,
             "Section 240: not more than 60% of the actual cost, including land acquisition."),
            ("Over how many years may the special levy be paid?",
             ["1 to 3 years", "3 to 5 years", "5 to 10 years", "10 to 20 years"], 2,
             "Section 241: not fewer than five nor more than ten annual installments."),
            ("A project cost ₱4,000,000. What is the largest total special levy?",
             ["₱1,000,000", "₱2,000,000", "₱2,400,000", "₱4,000,000"], 2,
             "60% × ₱4,000,000 = ₱2,400,000."),
            ("How is the special levy shared among the benefited lands?",
             ["according to the assessed value of each land", "equally per lot", "according to lot area only",
              "by lottery"], 0,
             "Section 243: apportioned according to the assessed valuation of the lands affected."),
            ("What must happen before the ordinance imposing a special levy is passed?",
             ["a public hearing with written notice to affected owners", "approval of the BIR",
              "a referendum in the barangay", "a court order"], 0,
             "Section 242: a public hearing, with written notice to the owners of the date and place."),
            ("Must the sanggunian use one uniform rate for the whole benefited district?",
             ["no, it may set different rates depending on the benefit", "yes, always",
              "yes, unless the President approves", "only for municipalities"], 0,
             "Section 241: it may fix different rates for different parts, depending on how much each gains."),
            ("An owner donated part of her land for the road. Is the rest of that land subject to the levy?",
             ["no, the remainder is not covered", "yes, at the full rate", "yes, at half the rate",
              "only if the road is paved"], 0,
             "Section 240: the levy does not apply to the remainder of land portions donated for the project."),
            ("When does the special levy accrue?",
             ["on the date the project starts", "on the first day of the quarter after the ordinance takes "
              "effect", "on January 1 of the next year", "when the project is finished"], 1,
             "Section 245: the first day of the quarter next following the effectivity of the ordinance."),
            ("A lot's share of the levy is ₱24,000, payable in eight annual installments. How much is each "
             "installment?",
             ["₱2,400", "₱3,000", "₱4,800", "₱8,000"], 1,
             "₱24,000 ÷ 8 = ₱3,000 a year."),
        ],
        "sources": [
            "Republic Act No. 7160, Local Government Code of 1991, Sections 240 to 245, 255, 256 and 257",
        ],
    },
    # ------------------------------------------------------------------ Note 13
    {
        "number": 13,
        "slug": "delivery-truck-and-van-tax",
        "title": "Tax on delivery trucks and vans",
        "summary": "The provincial tax on every vehicle used to deliver liquor, soft drinks, cigarettes and "
                   "similar products: who pays, how much, and when.",
        "publish_on": "2026-12-18 21:00",
        "body": [
            "Note 1 listed this tax in one line. It deserves a closer look, because it is easy to confuse with the municipal "
            "business tax. Unless stated otherwise, the sections cited are from the Local Government Code "
            "(RA 7160).",
            ("h", "What the law says"),
            "The province may levy an annual fixed tax for every truck, van or any vehicle used by manufacturers, "
            "producers, wholesalers, dealers or retailers in the delivery or distribution of distilled spirits, "
            "fermented liquors, soft drinks, cigars and cigarettes, and other products as the Sangguniang "
            "Panlalawigan may determine, to sales outlets or consumers within the province. The tax may not "
            "exceed ₱500 a year per vehicle (Section 141(a)).",
            ("h", "Reading it piece by piece"),
            ("table", ["Element", "What it means"], [
                ["Who levies it", "The province, through an ordinance of the Sangguniang Panlalawigan"],
                ["Who pays", "Manufacturers, producers, wholesalers, dealers and retailers who use the vehicle"],
                ["What is taxed", "Each vehicle used to deliver or distribute the listed products"],
                ["Which products", "Distilled spirits, fermented liquors, soft drinks, cigars and cigarettes, "
                 "and other products the Sangguniang Panlalawigan names"],
                ["Where", "Deliveries to sales outlets or consumers within the province, directly or "
                 "indirectly"],
                ["How much", "A fixed amount per vehicle per year, not more than ₱500"],
            ]),
            ("h", "A built-in exemption"),
            "The manufacturers, producers, wholesalers, dealers and retailers covered by this tax are exempt "
            "from the tax on peddlers found elsewhere in the Code (Section 141(b)). A delivery truck pays this "
            "tax, not the peddler's tax.",
            ("h", "Not the same as the business tax"),
            "This tax is on the vehicle, at a fixed amount. The municipal business tax under Section 143 is on "
            "the business, based on its gross sales (Note 4). A soft drink distributor may therefore pay the "
            "business tax to the municipality where it sells and the delivery truck tax to the province for "
            "each vehicle.",
            ("h", "In a city"),
            "A city may levy the taxes a province may levy, and its rates may exceed the provincial maximum by "
            "up to 50%, except the professional and amusement taxes (Section 151). For this tax, the city's "
            "ceiling works out to ₱500 × 150% = ₱750 per vehicle a year.",
            ("h", "Payment and penalties"),
            "Unless the Code provides otherwise, local taxes are paid within the first 20 days of January "
            "(Section 167). A late payment may carry a surcharge of up to 25% and interest of up to 2% a month "
            "on the unpaid tax including the surcharge, for no more than 36 months (Section 168). Like every "
            "local tax, it is collected by the treasurer or a duly authorized deputy (Section 170), and every "
            "payment gets an official receipt (Note 7).",
            ("tip", "A good list of the vehicles is half the work. Ask covered businesses for the plate numbers of "
                    "every delivery vehicle used in the province, so each receipt names the vehicles it covers."),
        ],
        "example": (
            "Worked example: a distributor with six trucks",
            [
                "A soft drink distributor uses six trucks to deliver to stores in the province. The provincial "
                "ordinance sets the tax at the ₱500 maximum.",
                "Annual tax: 6 × ₱500 = ₱3,000, due within the first 20 days of January (Section 167).",
                "The distributor pays on March 10. The ordinance sets the maximum 25% surcharge and 2% monthly "
                "interest, and counts a part of a month as a full month.",
                "Surcharge: 25% × ₱3,000 = ₱750.",
                "Interest from January 21 to March 10, two months: 4% × (₱3,000 + ₱750) = ₱150.",
                "Amount due on March 10: ₱3,000 + ₱750 + ₱150 = ₱3,900.",
            ],
            "Paying on time costs ₱3,000. Paying on March 10 costs ₱3,900.",
        ),
        "practice": [
            ("Which local government levies the tax on delivery trucks and vans under Section 141?",
             ["the province", "the barangay", "the municipality", "the national government"], 0,
             "Section 141(a): the province may levy it. A city may also levy it under Section 151."),
            ("What is the most a province may charge per delivery vehicle each year?",
             ["₱100", "₱300", "₱500", "₱1,000"], 2,
             "Section 141(a): not exceeding ₱500."),
            ("Which of these products is named in Section 141?",
             ["soft drinks", "rice", "school supplies", "medicine"], 0,
             "Distilled spirits, fermented liquors, soft drinks, cigars and cigarettes, and other products the "
             "Sangguniang Panlalawigan determines."),
            ("The tax is computed on ____.",
             ["each vehicle, at a fixed amount", "the gross sales of the business", "the value of the truck",
              "the number of deliveries"], 0,
             "Section 141(a): an annual fixed tax for every truck, van or vehicle."),
            ("Businesses that pay the delivery truck tax are exempt from which tax?",
             ["the tax on peddlers", "the business tax", "the real property tax", "the community tax"], 0,
             "Section 141(b): exempt from the tax on peddlers prescribed elsewhere in the Code."),
            ("A wholesaler uses four vans. The ordinance sets ₱400 per vehicle. What is the annual tax?",
             ["₱400", "₱1,200", "₱1,600", "₱2,000"], 2,
             "4 × ₱400 = ₱1,600."),
            ("What is the highest rate a city may set for this tax?",
             ["₱500", "₱600", "₱750", "₱1,000"], 2,
             "Section 151: up to 50% above the provincial maximum, so ₱500 × 150% = ₱750."),
            ("Unless the Code provides otherwise, when must the tax be paid?",
             ["within the first 20 days of January", "on or before March 31", "on the date of each delivery",
              "before the vehicle is registered"], 0,
             "Section 167: within the first 20 days of January or of each subsequent quarter."),
            ("A ₱2,000 tax is paid late. What is the largest surcharge?",
             ["₱200", "₱400", "₱500", "₱1,000"], 2,
             "Section 168: up to 25% × ₱2,000 = ₱500."),
            ("How does this tax differ from the municipal business tax?",
             ["it is a fixed amount per vehicle, not based on gross sales", "it is paid only once in a "
              "lifetime", "it replaces the business tax", "it is collected by the BIR"], 0,
             "Section 141 taxes each vehicle at a fixed amount; Section 143 taxes the business on its gross "
             "sales."),
        ],
        "sources": [
            "Republic Act No. 7160, Local Government Code of 1991, Sections 141, 143, 151, 167, 168 and 170",
        ],
    },
    # ------------------------------------------------------------------ Note 14
    {
        "number": 14,
        "slug": "ethics-at-the-collection-window",
        "title": "Ethics at the collection window",
        "summary": "What the Code of Conduct (RA 6713) and the Anti-Graft Law (RA 3019) mean for treasury "
                   "workers: gifts, conflicts of interest, prompt service and the SALN.",
        "publish_on": "2026-12-22 21:00",
        "body": [
            "A treasury worker handles public money and serves the public every day. Two laws set the standard "
            "for how they do it: the Code of Conduct and Ethical Standards for Public Officials and Employees "
            "(RA 6713, 1989) and the Anti-Graft and Corrupt Practices Act (RA 3019, 1960). This note reads both "
            "with the collection window in mind.",
            ("h", "Eight norms of conduct (RA 6713, Section 4)"),
            ("list", [
                "Commitment to public interest",
                "Professionalism",
                "Justness and sincerity",
                "Political neutrality",
                "Responsiveness to the public",
                "Nationalism and patriotism",
                "Commitment to democracy",
                "Simple living",
            ]),
            ("h", "Duties that apply every day (RA 6713, Section 5)"),
            "Letters and other communications from the public must be answered within 15 working days from "
            "receipt (Section 5(a)). Officials and employees must attend to anyone who seeks the services of "
            "their office and act promptly and expeditiously (Section 5(d)).",
            ("h", "What RA 6713 prohibits (Section 7)"),
            ("list", [
                "Having a financial or material interest in any transaction that requires the approval of "
                "one's office (Section 7(a)).",
                "Owning, controlling or working for a private business regulated by one's office, unless the law "
                "allows it (Section 7(b)).",
                "Using or disclosing confidential information to advance private interests or give anyone an "
                "undue advantage (Section 7(c)).",
                "Soliciting or accepting, directly or indirectly, any gift, gratuity, favor, entertainment or "
                "loan from any person in the course of one's official duties or in connection with any "
                "transaction that may be affected by one's office (Section 7(d)).",
            ]),
            ("h", "The SALN (RA 6713, Section 8)"),
            "Officials and employees file a sworn Statement of Assets, Liabilities and Net Worth within 30 days "
            "after assuming office, on or before April 30 of every year after that, and within 30 days after "
            "leaving the service. Honorary officials, laborers and casual or temporary workers are not "
            "required to file.",
            ("h", "What RA 3019 punishes (Section 3)"),
            ("list", [
                "Requesting or receiving any gift, present, share, percentage or benefit in connection with a "
                "government contract or transaction in which the officer must intervene officially "
                "(Section 3(b)).",
                "Requesting or receiving a gift or material benefit from a person for whom the officer secured, "
                "or will secure, a government permit or license (Section 3(c)).",
                "Causing undue injury to any party, including the government, or giving anyone unwarranted "
                "benefits, through manifest partiality, evident bad faith or gross inexcusable negligence "
                "(Section 3(e)).",
                "Having a financial interest in a business, contract or transaction in which the officer "
                "intervenes or takes part officially (Section 3(h)).",
            ]),
            "RA 3019 makes one exception: unsolicited gifts or presents of small or insignificant value, offered "
            "or given as a mere ordinary token of gratitude or friendship according to local customs or usage "
            "(Section 14).",
            ("h", "The penalties"),
            ("table", ["Law", "Penalty"], [
                ["RA 6713, violations of Sections 7, 8 or 9",
                 "Imprisonment of up to 5 years, a fine of up to ₱5,000, or both, and possible disqualification "
                 "from public office (Section 11(a))"],
                ["RA 6713, other violations",
                 "A fine of up to six months' salary, suspension of up to one year, or removal (Section 11(a))"],
                ["RA 3019, Section 3",
                 "Imprisonment of 6 years and 1 month to 15 years, perpetual disqualification from public "
                 "office, and forfeiture of unexplained wealth (Section 9, as amended by BP 195, 1982)"],
            ]),
            "Offenses under RA 3019 prescribe in 20 years (Section 11, as amended by RA 10910, 2016). Once a "
            "valid information is filed in court, the accused officer is suspended from office (Section 13).",
            ("tip", "At the window, the safe answer to any offer is a polite no. A treasury worker who never "
                    "accepts anything from a taxpayer with a pending transaction never has to explain."),
        ],
        "example": (
            "Worked example: three situations at the window",
            [
                "A business owner whose permit the treasurer's office just processed leaves ₱500 \"for "
                "merienda\". This is a material benefit from a person whose permit the office helped secure, the "
                "act described in RA 3019, Section 3(c). The answer is to return it.",
                "A taxpayer offers to pay a collector extra to have a receipt dated earlier, to avoid the "
                "surcharge. Accepting would be a gift in connection with a transaction affected by the office "
                "(RA 6713, Section 7(d)). The answer is no, and the payment is received on its actual date.",
                "A collector owns part of a hardware store that bids to supply the treasury. A financial or "
                "material interest in a transaction requiring the approval of one's office is prohibited "
                "(RA 6713, Section 7(a)), and so is having a financial interest in a transaction in which one "
                "intervenes officially (RA 3019, Section 3(h)).",
            ],
            "Return the money, refuse the backdated receipt, and do not let your own business deal with your office.",
        ),
        "practice": [
            ("Which law is the Code of Conduct and Ethical Standards for Public Officials and Employees?",
             ["RA 6713", "RA 3019", "RA 7160", "RA 9184"], 0,
             "RA 6713 (1989). RA 3019 is the Anti-Graft and Corrupt Practices Act."),
            ("Within how many working days must a letter from the public be answered?",
             ["5", "10", "15", "30"], 2,
             "RA 6713, Section 5(a): within 15 working days from receipt."),
            ("When is the yearly SALN due?",
             ["on or before January 31", "on or before March 31", "on or before April 30",
              "on or before June 30"], 2,
             "RA 6713, Section 8: on or before April 30 of every year."),
            ("Which of these is NOT one of the norms of conduct in RA 6713, Section 4?",
             ["profit maximization", "simple living", "political neutrality", "responsiveness to the public"], 0,
             "The eight norms include simple living, political neutrality and responsiveness to the public."),
            ("Receiving a gift from a person whose permit you helped secure is covered by ____.",
             ["RA 3019, Section 3(c)", "RA 3019, Section 14", "RA 6713, Section 4", "RA 7160, Section 141"], 0,
             "Section 3(c) of RA 3019 punishes requesting or receiving a gift from a person for whom the "
             "officer secured a permit or license."),
            ("Which gifts does RA 3019, Section 14 exclude?",
             ["unsolicited gifts of small value given as an ordinary token of gratitude or friendship",
              "any gift below ₱5,000", "gifts received after office hours", "gifts given by relatives in "
              "connection with a permit"], 0,
             "Section 14: unsolicited gifts or presents of small or insignificant value, according to local "
             "customs or usage."),
            ("What is the prison term for a violation of RA 3019, Section 3?",
             ["1 month to 1 year", "1 to 5 years", "6 years and 1 month to 15 years", "life imprisonment"], 2,
             "Section 9, as amended by BP 195: 6 years and 1 month to 15 years, plus perpetual "
             "disqualification."),
            ("In how many years do offenses under RA 3019 prescribe?",
             ["5 years", "10 years", "15 years", "20 years"], 3,
             "Section 11, as amended by RA 10910 (2016): 20 years."),
            ("Which act does RA 6713, Section 7(a) prohibit?",
             ["having a financial interest in a transaction requiring your office's approval",
              "answering letters within 15 working days", "filing a SALN", "attending to the public promptly"], 0,
             "RA 6713, Section 7(a) prohibits a financial or material interest in a transaction requiring the "
             "approval of one's office."),
            ("What happens to an officer once a valid information under RA 3019 is filed in court?",
             ["suspension from office", "automatic dismissal", "nothing until conviction",
              "transfer to another office"], 0,
             "RA 3019, Section 13: the officer is suspended from office."),
        ],
        "sources": [
            "Republic Act No. 6713, Code of Conduct and Ethical Standards for Public Officials and Employees "
            "(1989), Sections 4, 5, 7, 8 and 11",
            "Republic Act No. 3019, Anti-Graft and Corrupt Practices Act (1960), Sections 3, 9, 11, 13 and 14",
            "Batas Pambansa Blg. 195 (March 16, 1982), amending Section 9 of RA 3019",
            "Republic Act No. 10910 (July 21, 2016), amending Section 11 of RA 3019",
        ],
    },
    # ------------------------------------------------------------------ Note 15
    {
        "number": 15,
        "slug": "cashbooks-and-daily-records",
        "title": "Cashbooks and daily records",
        "summary": "The books an accountable officer keeps every day, why they must be balanced daily, and what "
                   "an auditor checks in them.",
        "publish_on": "2026-12-25 21:00",
        "body": [
            "Note 7 followed the money from the window to the bank, and Note 8 followed the receipts. Between "
            "them sits a quieter tool: the books where every peso in and out is written down. An accountable "
            "officer who keeps them well can show at any moment what they hold and why. This note explains "
            "those records, using the Government Accounting Manual for local governments (GAM for LGUs, "
            "Volume II) and the Commission on Audit's Revised Cash Examination Manual (COA Memorandum "
            "No. 2013-004).",
            ("h", "The main records"),
            ("table", ["Record", "What it shows"], [
                ["Cash Receipts Record (CRR)", "A collecting officer's collections and deposits"],
                ["Cash Disbursements Record (CDR)", "Payments made in cash by a disbursing officer"],
                ["Check Disbursements Record (CkDR)", "Payments made by check"],
                ["Cashbook – Cash in Treasury", "Cash held in the treasury"],
                ["Cashbook – Cash in Bank", "Cash held in the local government's bank accounts"],
                ["Cashbook – Cash Advances", "Cash advances held by disbursing officers"],
                ["Petty Cash Record", "Payments from, and replenishments of, a petty cash fund"],
            ]),
            "The cashbooks and the Petty Cash Record are among the books listed in GAM for LGUs, Volume II. The "
            "CRR, CDR and CkDR are the records the cash examination manual tells the auditor to check.",
            ("h", "Rule one: update and balance every day"),
            "The cash examination manual expects the cashbook to be updated and balanced daily. Each entry "
            "should carry the date, the document number (official receipt, check or voucher), the payor "
            "or payee, the amount, and the running balance. At the end of the day, the balance in the book "
            "should equal the cash and checks on hand.",
            ("h", "Rule two: record everything before a count"),
            "When an auditor arrives for a cash examination, the accountable officer enters in the "
            "cashbook, CRR, CDR or CkDR all valid transactions and adjustments up to the time of the count, "
            "and certifies that they are correctly and completely recorded (COA Memorandum No. 2013-004, "
            "Chapter III, Section J). The auditor examines all funds in the officer's custody at the same time, "
            "notes the last official receipt and check number issued to fix the cut-off, foots the books, and "
            "checks the entries against the source documents.",
            ("h", "Rule three: only real cash counts as cash"),
            "The manual tells the auditor to disallow accommodated private checks, post-dated and stale checks, "
            "chits and promissory notes found among the cash. Money in the hands of a collecting officer may "
            "never be used to cash private checks. A \"vale\" slip in the drawer is not cash, and the amount it "
            "covers is treated as missing.",
            ("tip", "If the book is late, the count is hard. A collector who posts every receipt as it is issued "
                    "can close the day in minutes, and can face a surprise count without worry."),
            ("h", "How the records connect"),
            ("list", [
                "Each official receipt is entered in the CRR. The day's total in the CRR matches the Report of "
                "Collections and Deposits (Note 7).",
                "Each deposit is entered as a deduction in the CRR and supported by a validated deposit slip.",
                "Each check issued is entered in the CkDR and appears in the Report of Checks Issued.",
                "The serial numbers used in the CRR agree with the RAAF (Note 8).",
                "What the books say the officer should hold is the accountability the auditor compares with "
                "the count (Note 10).",
            ]),
        ],
        "example": (
            "Worked example: one day in a Cash Receipts Record",
            [
                "The collector starts the day with an undeposited balance of ₱0.",
                "OR 5101, real property tax: ₱2,400. Balance ₱2,400.",
                "OR 5102, business permit fee: ₱1,500. Balance ₱3,900.",
                "OR 5103, cancelled. No amount. Balance ₱3,900.",
                "OR 5104, community tax: ₱365. Balance ₱4,265.",
                "Deposit with validated deposit slip: ₱4,265. Balance ₱0.",
                "Check: receipts 5101 to 5104 are all accounted for, the total collected is ₱4,265, and it "
                "equals the deposit.",
            ],
            "The CRR shows ₱4,265 collected and ₱4,265 deposited, with an ending balance of ₱0 and no missing "
            "receipt number.",
        ),
        "practice": [
            ("Which record shows a collecting officer's collections and deposits?",
             ["the Cash Receipts Record", "the Check Disbursements Record", "the Petty Cash Record",
              "the Cashbook – Cash Advances"], 0,
             "The CRR records the collecting officer's collections and deposits."),
            ("Which record lists payments made by check?",
             ["the Check Disbursements Record", "the Cash Receipts Record", "the RAAF",
              "the assessment roll"], 0,
             "The CkDR records payments made by check."),
            ("How often should a cashbook be updated and balanced?",
             ["daily", "weekly", "monthly", "at year-end"], 0,
             "The COA cash examination manual expects the cashbook to be updated and balanced daily."),
            ("Before a cash count, what must the accountable officer do with the records?",
             ["enter all valid transactions up to the time of the count", "close the books for the month",
              "send them to the BIR", "nothing; the auditor does it"], 0,
             "COA Memorandum No. 2013-004, Chapter III, Section J."),
            ("During a cash examination, which funds in the officer's custody are examined?",
             ["all funds at the same time", "only the general fund", "only the largest fund",
              "only funds named by the officer"], 0,
             "The manual directs a simultaneous examination of all funds in the officer's custody."),
            ("A chit for ₱1,000 signed by a co-worker is found in the cash drawer. How is it treated?",
             ["it is disallowed, not counted as cash", "it is counted as cash", "it is counted at half value",
              "it is returned to the co-worker"], 0,
             "The manual directs auditors to disallow chits and promissory notes under any circumstance."),
            ("May a collector use collections to cash a co-worker's personal check?",
             ["no, never", "yes, if the check is good", "yes, up to ₱5,000", "only on payday"], 0,
             "The manual says money in the collecting officer's hands must never be used to cash private "
             "checks."),
            ("Why does the auditor note the last official receipt and check number issued?",
             ["to fix the cut-off of the records", "to order new forms", "to compute the officer's salary",
              "to report to the BIR"], 0,
             "Noting the last OR and check numbers establishes the cut-off for the count."),
            ("A CRR shows receipts of ₱2,000, ₱750 and ₱1,250 and one deposit of ₱3,000. What is the "
             "balance?",
             ["₱750", "₱1,000", "₱1,250", "₱4,000"], 1,
             "₱2,000 + ₱750 + ₱1,250 − ₱3,000 = ₱1,000."),
            ("Which book shows the cash advances held by disbursing officers?",
             ["Cashbook – Cash Advances", "Cashbook – Cash in Bank", "Cash Receipts Record",
              "Report of Collections and Deposits"], 0,
             "GAM for LGUs, Volume II, lists a Cashbook – Cash Advances."),
        ],
        "sources": [
            "Commission on Audit, Government Accounting Manual for Local Government Units, Volume II (books, "
            "registries, records, forms and reports)",
            "Commission on Audit Memorandum No. 2013-004, Revised Cash Examination Manual",
        ],
    },
]

for _n in NOTES_11_TO_15:
    _n["practice"] = _spread(_n["practice"])
