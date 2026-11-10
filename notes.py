"""Study Notes: local treasury topics, one note every Friday at 9 pm (Philippine time).

Butch chose this for the old Courses page (2026-11-10). Each note explains one part of local
revenue and treasury work in plain words, cites the law it explains, gives a worked example
and ends with a 10-question tap quiz (the same quiz as the vocabulary modules).

Each note: number, slug, title, summary, publish_on ("YYYY-MM-DD HH:MM" PH time),
body [str paragraph | ("h", heading) | ("list", [items]) | ("table", [header], [[cells]]) | ("tip", text)],
example (title, [steps], answer), practice [(question, [choices], index of right choice, why)].
Facts checked against RA 7160 (Book II) and RA 9640; see "checked" below.
"""

NOTES_INFO = {
    "title": "Study Notes",
    "url": "/study-notes/",
    "intro": (
        "Plain-language notes on local treasury work: where local revenue comes from, how "
        "real property and business taxes are computed, and how money is collected, kept and paid out. "
        "Each note explains the law in everyday words, works through an example and ends with a 10-question "
        "quiz. A new note comes out every Friday at 9 pm."
    ),
    "disclaimer": (
        "These are independent study notes written from the law and from years of treasury work. They are "
        "not official materials of the Bureau of Local Government Finance (BLGF), the Civil Service "
        "Commission or any office, and they do not contain actual exam questions. Always check the law and "
        "your local revenue code."
    ),
    "checked": "November 2026",
}

# The outline Butch approved (2026-11-10). Only notes with a body are published.
OUTLINE = [
    "Sources of local revenue",
    "Real property tax basics",
    "Paying real property tax: quarters, discounts and interest",
    "Business tax and the mayor's permit",
    "Community tax (cedula)",
    "Fees and charges",
    "Collection and deposit",
    "Accountable forms and the RAAF",
    "Disbursements: vouchers, checks and cash advances",
    "Accountability: bonds, cash counts and shortages",
]

NOTES = [
    {
        "number": 1,
        "slug": "sources-of-local-revenue",
        "title": "Sources of local revenue",
        "summary": "Where a province, city, municipality or barangay gets its money, what each level may tax, "
                   "and what no local government may tax at all.",
        "publish_on": "2026-11-10 17:00",  # published early in a batch for AdSense readiness (Butch, 2026-11-10)
        "body": [
            "Every peso a local government spends must first come from somewhere. The 1987 Constitution "
            "(Article X, Section 5) gives each local government the power to create its own sources of revenue "
            "and to levy taxes, fees and charges, subject to limits set by Congress. Congress set those limits in "
            "the Local Government Code of 1991, Republic Act No. 7160. Book II of the Code is the part every "
            "treasury worker should know well.",
            ("h", "The four main sources"),
            ("list", [
                "Local taxes: real property tax, business taxes, the community tax and the other taxes the Code "
                "allows each level to impose.",
                "Fees and charges: payments for a service or a permit, such as permit fees, market stall rentals "
                "and service charges.",
                "Shares in national taxes: the National Tax Allotment (NTA), formerly called the Internal Revenue "
                "Allotment (IRA).",
                "Shares in national wealth: a share of what the national government earns from mining, forestry, "
                "fishery and energy resources found in the area.",
            ]),
            "Local governments may also borrow money and receive grants, but loans must be paid back and grants "
            "are not regular income. This note covers the first three sources; the share in national wealth "
            "goes only to places where those resources are found.",
            ("h", "Rules every local tax must follow"),
            "Section 130 of the Code lists the fundamental principles. A local tax, fee or charge must be "
            "uniform within the local government, must be fair and based as far as practicable on the "
            "taxpayer's ability to pay, must be levied only for a public purpose, and must not be unjust, "
            "excessive, oppressive or confiscatory. The collection of a local tax can never be given to a "
            "private person. A tax can only be imposed by an ordinance passed by the sanggunian, after a public "
            "hearing (Sections 132 and 187).",
            ("h", "What no local government may tax"),
            "Section 133 lists what is off-limits to every province, city, municipality and barangay. Among "
            "them:",
            ("list", [
                "income tax, except on banks and other financial institutions",
                "documentary stamp tax, and estate, inheritance and gift taxes",
                "customs duties and taxes on goods passing through the area",
                "taxes on agricultural and aquatic products sold by marginal farmers or fishermen",
                "excise taxes under the Tax Code, and taxes on petroleum products",
                "registration fees for motor vehicles and driver's licenses, except for tricycles",
                "taxes on the national government, its agencies and other local governments",
            ]),
            ("tip", "A quick test: if the national government already taxes it under the Tax Code (income, "
                    "estate, excise, VAT), a local government usually cannot tax it again."),
            ("h", "What each level may tax"),
            ("table", ["Level", "Main local taxes (RA 7160)"], [
                ["Province", "Real property tax (up to 1% of assessed value) and Special Education Fund levy "
                             "(1%); tax on transfer of real property (up to 50% of 1%); printing and "
                             "publication tax; franchise tax; sand, gravel and quarry tax (up to 10% of fair "
                             "market value); professional tax (up to ₱300 a year); amusement tax on admission "
                             "(up to 10% of gross receipts, as amended by RA 9640); fixed tax on delivery "
                             "trucks and vans (up to ₱500 a year)"],
                ["Municipality", "Business taxes on manufacturers, wholesalers, retailers, contractors, banks "
                                 "and other businesses (Section 143); community tax; fees for sealing weights "
                                 "and measures; fishery rentals and fees"],
                ["City", "Any tax a province or municipality may impose, at rates up to 50% higher, except the "
                         "professional and amusement taxes (Section 151); real property tax up to 2% plus the "
                         "1% SEF levy"],
                ["Barangay", "Tax on small stores and retailers with gross sales of ₱50,000 or less (in cities) "
                             "or ₱30,000 or less (in municipalities), at up to 1% of gross sales; service "
                             "fees, barangay clearances, and fees on cockpits, billboards and similar "
                             "(Section 152)"],
            ]),
            "Notice what a municipality does not have: the power to levy real property tax. In a municipality "
            "outside Metro Manila, the real property tax is levied by the province, collected by the municipal "
            "treasurer, and then shared among the province, the municipality and the barangay. That sharing is "
            "the subject of Note 2.",
            ("h", "Shares in national taxes"),
            "Under Section 284, local governments as a group get 40% of national internal revenue taxes. The "
            "Supreme Court's Mandanas ruling widened the base to all national taxes, and since 2022 the share "
            "has been called the National Tax Allotment. Section 285 divides it: 23% to provinces, 23% to "
            "cities, 34% to municipalities and 20% to barangays. Within each group, it is shared by population "
            "(50%), land area (25%) and equal sharing (25%).",
            ("tip", "For most municipalities, the NTA is still the largest source of income. That is why "
                    "raising local collections matters: it gives the town money it can plan for on its own."),
            ("h", "Why this matters at the counter"),
            "A treasury worker who knows these limits can answer a taxpayer's \"Why am I paying this?\" "
            "with the law, and can spot an ordinance that charges something the Code does not allow. An unlawful "
            "tax can be challenged: a taxpayer may appeal a tax ordinance to the Secretary of Justice within 30 "
            "days of its effectivity (Section 187).",
        ],
        "example": (
            "Worked example: who may tax what?",
            [
                "A hardware store in a municipality has gross sales of ₱2 million. The business tax is a municipal "
                "tax under Section 143, so the municipality collects it.",
                "The owner also sells a lot. The tax on transfer of real property ownership is a provincial tax "
                "(Section 135), at up to 50% of 1% of the price or the fair market value, whichever is higher.",
                "On a ₱1,000,000 sale, the maximum transfer tax is 0.5% × ₱1,000,000 = ₱5,000.",
                "If the same store were in a city, the city could levy both taxes itself, and its rates could go "
                "up to 50% above the provincial or municipal limits (Section 151). For the transfer tax, that is "
                "up to 0.75%, or ₱7,500 on the same sale.",
            ],
            "The municipality taxes the business; the province taxes the transfer. In a city, the city does both.",
        ),
        "practice": [
            ("Which law sets the taxing powers of provinces, cities, municipalities and barangays?",
             ["RA 6713", "RA 7160", "RA 3019", "RA 9184"], 1,
             "The Local Government Code of 1991 (RA 7160), Book II, sets local taxing powers and their limits."),
            ("Which of these may a municipality NOT tax?",
             ["a retailer's gross sales", "a contractor's gross receipts", "income of an individual",
              "a manufacturer's gross sales"], 2,
             "Section 133 bars local governments from levying income tax, except on banks and other financial "
             "institutions."),
            ("Who levies the real property tax on land in a municipality outside Metro Manila?",
             ["the barangay", "the municipality", "the province", "the national government"], 2,
             "Section 232: provinces, cities and municipalities within Metro Manila levy real property tax."),
            ("What is the maximum basic real property tax rate a CITY may impose?",
             ["1% of assessed value", "2% of assessed value", "5% of assessed value", "10% of market value"], 1,
             "Section 233: up to 1% for provinces and up to 2% for cities and Metro Manila municipalities."),
            ("The Special Education Fund (SEF) levy is an additional real property tax of ____.",
             ["0.5%", "1%", "2%", "3%"], 1,
             "Section 235 allows an additional 1% annual tax on the assessed value of real property for the SEF."),
            ("A barangay in a municipality may tax a sari-sari store only if its gross sales are ____.",
             ["₱30,000 or less", "₱50,000 or less", "₱100,000 or less", "any amount"], 0,
             "Section 152(a): ₱50,000 or less in cities, ₱30,000 or less in municipalities, at up to 1%."),
            ("What is the most a province may charge as professional tax in a year?",
             ["₱100", "₱300", "₱500", "₱1,000"], 1,
             "Section 139 caps the annual professional tax at ₱300."),
            ("A city wants to raise its business tax rate above the municipal limit. By how much at most?",
             ["10%", "25%", "50%", "100%"], 2,
             "Section 151 lets cities exceed provincial and municipal rates by up to 50%, except for the "
             "professional and amusement taxes."),
            ("What share of the National Tax Allotment goes to all municipalities as a group?",
             ["20%", "23%", "34%", "40%"], 2,
             "Section 285: provinces 23%, cities 23%, municipalities 34% and barangays 20%."),
            ("Which statement follows the fundamental principles of local taxation (Section 130)?",
             ["A private agency may be hired to collect the tax for a commission.",
              "The tax must be uniform within the local government.",
              "The tax may be set by the mayor without an ordinance.",
              "The tax may be confiscatory if revenue is low."], 1,
             "Taxes must be uniform, fair, for a public purpose and not unjust or confiscatory, and they are "
             "imposed by ordinance (Section 132). Collection can never be given to a private person."),
        ],
    },
]


def note_url(n):
    return f"{NOTES_INFO['url']}{n['slug']}/"
