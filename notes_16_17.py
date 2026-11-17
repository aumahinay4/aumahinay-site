"""Study Notes 16 and 17 (Butch, 2026-11-18 PH: "Try the personal study notes", put on the site without
mentioning where the topic came from): the schedule of market values under RA 12001, and the revenue and
tax impact report. Tuesday December 29, 2026 and Friday January 1, 2027, 9 pm, after Notes 11 to 15.

Same shape as Notes 2 to 15. Facts checked (November 2026) against:
- RA 12001 (Real Property Valuation and Assessment Reform Act), Sections 4, 5, 13, 15 to 20, 22 to 24 and 29
  (lawphil);
- the IRR of RA 12001 (BLGF Memorandum Circular No. 001.2025), Sections 36, 37, 38, 41 and 55 (lawyerly);
- RA 7160 Book II (Butch's Drive copy), Sections 199, 218, 233, 235, 251, 271 and 272, as already checked
  for Notes 2 and 3.
Kept apart from Note 2 (computing the tax), Note 3 (paying it), the RPT calculator and the amnesty post
(Section 30, 6% cap example of ₱2,400): these notes cover how the schedule is made and how its effect is
reported, and use their own numbers. No Wikipedia sources. Worked examples and quiz answers recomputed.
"""

from notes_2_10 import _spread

NOTES_16_TO_17 = [
    # ------------------------------------------------------------------ Note 16
    {
        "number": 16,
        "slug": "schedule-of-market-values",
        "title": "The schedule of market values",
        "summary": "How the schedule of market values is prepared, reviewed and approved under RA 12001, the "
                   "deadlines at each step, how often it is updated, and who else uses it.",
        "publish_on": "2026-12-29 21:00",
        "body": [
            "Every real property tax bill starts with a market value, and every market value starts with the "
            "schedule of market values, or SMV. Note 2 showed how the tax is computed from it. This note is "
            "about the schedule itself: who makes it, who checks it, and how fast each step must move. Unless "
            "stated otherwise, the sections cited are from the Real Property Valuation and Assessment Reform Act "
            "(Republic Act No. 12001), approved on June 13, 2024.",
            ("h", "What the schedule is"),
            "The SMV is a table of base unit market values for all kinds of real property in a local government, "
            "except machinery (Section 4). A market value is the estimated amount for which a property would "
            "change hands on the valuation date between a willing buyer and a willing seller, dealing at arm's "
            "length and knowing the facts. The assessor multiplies a property's area by the unit value in the "
            "schedule, with the adjustments the schedule allows, to get its market value.",
            ("h", "One standard for the whole country"),
            "Schedules must follow the Philippine Valuation Standards, or PVS: national standards based on the "
            "International Valuation Standards and approved by the Secretary of Finance (Section 4). The Bureau "
            "of Local Government Finance (BLGF) of the Department of Finance develops the standards and leads the "
            "carrying out of the law (Sections 5 and 13). Section 13 calls them uniform valuation standards, so "
            "every assessor values property by the same rules.",
            ("h", "From proposal to approved schedule"),
            ("table", ["Step", "Rule"], [
                ["1. Preparation", "The provincial, city or municipal assessor prepares the proposed SMV and "
                                   "completes it within 12 months after notice from the BLGF (Section 15)."],
                ["2. Publication", "The proposal is published for at least two weeks before the public "
                                   "consultation, on the local government's website and in two conspicuous "
                                   "places (Section 15)."],
                ["3. Public consultation", "At least two public consultations are held within 60 days before the "
                                           "proposal is submitted (Section 15)."],
                ["4. BLGF review", "Outside Metro Manila, the BLGF Regional Office reviews the proposal and "
                                   "endorses it to the head of the BLGF within 45 days. The head of the BLGF "
                                   "endorses it to the Secretary of Finance within 30 days. Proposals of cities "
                                   "and of the lone municipality in Metro Manila go to the BLGF Central Office "
                                   "(Section 15)."],
                ["5. Certification", "The Secretary of Finance certifies, within 30 days, that the schedule "
                                     "follows the latest PVS. A schedule that does not is sent back with a "
                                     "written explanation, and the assessor resubmits it within 30 days "
                                     "(Section 16)."],
                ["6. Effectivity", "The Department of Finance publishes the approved schedule in the Official "
                                   "Gazette or on its website. It takes effect 15 days after publication "
                                   "(Section 16)."],
            ]),
            ("tip", "Public consultation is the taxpayer's chance to question a unit value before it becomes "
                    "official. Watch the local government's website and bulletin boards for the notice."),
            ("h", "How often it is updated"),
            "Assessors had to make the first update within two years from the law's effectivity; the implementing "
            "rules set that deadline at July 5, 2026 (Section 19; IRR Section 41). After that, the schedule is "
            "updated and property assessments are generally revised every three years. An interim revision is "
            "allowed in between when values change sharply, for example when a new road opens, after a calamity or "
            "a declared public health emergency, or to correct errors in the schedule (Section 19).",
            ("h", "Where the values come from"),
            "The BLGF keeps a Real Property Information System, an electronic database of sales, leases, "
            "mortgages, donations and other transfers, plus construction costs and machinery prices "
            "(Section 22). Registers of deeds give assessors an abstract of their registry every three months "
            "(Section 23), and registers of deeds, the Bureau of Internal Revenue (BIR), notaries public, building "
            "officials and geodetic engineers send transaction data to the BLGF every quarter (Section 24).",
            ("h", "Who else uses it"),
            ("list", [
                "Local governments: the approved SMV is the basis of real property taxes and of the general "
                "revision of assessments (Section 18).",
                "The BIR: in computing internal revenue taxes, it uses the SMV or the actual gross selling price, "
                "whichever is higher (Section 18). Until a schedule is updated, it uses the existing SMV, its "
                "zonal value or the actual price, whichever is higher (Section 29).",
                "Other government agencies use it when they appraise real property (Section 18).",
                "Compliance with the law is an added indicator for the Seal of Good Local Governance "
                "(Section 20).",
            ]),
            "A new schedule does not by itself set the tax. The sanggunian still sets assessment levels and tax "
            "rates, and the first-year increase is capped at 6% (Section 29). Note 17 explains the report that "
            "helps the sanggunian decide.",
        ],
        "example": (
            "Worked example: counting the deadlines",
            [
                "A province's proposed SMV reaches the BLGF Regional Office on December 1, 2027. The 45 days for "
                "review end on January 15, 2028.",
                "The head of the BLGF receives the endorsement on January 12, 2028. The 30 days end on "
                "February 11, 2028.",
                "The Secretary of Finance receives it on February 8, 2028. The 30 days end on March 9, 2028 "
                "(2028 is a leap year, so February has 29 days).",
                "The Department of Finance publishes the approved schedule on March 10, 2028. It takes effect "
                "15 days later, on March 25, 2028.",
                "Now the BIR: a 200 sq m lot with a unit value of ₱3,000 a square meter has an SMV value of "
                "200 × ₱3,000 = ₱600,000. If the deed of sale says ₱500,000, the BIR computes its taxes on "
                "₱600,000, the higher amount.",
            ],
            "Review ends January 15, endorsement February 11, certification March 9, and the schedule takes "
            "effect March 25, 2028. The BIR's base for the lot is ₱600,000.",
        ),
        "practice": [
            ("Who prepares the proposed schedule of market values?",
             ["the provincial, city or municipal assessor", "the sanggunian", "the BIR", "the Secretary of Finance"],
             0, "Section 15: the provincial, city and municipal assessors prepare the SMV."),
            ("Within how many months after notice from the BLGF must the SMV be prepared?",
             ["6 months", "12 months", "18 months", "24 months"], 1,
             "Section 15: within 12 months following the notice from the BLGF."),
            ("How many public consultations must be held before the proposal is submitted?",
             ["none", "at least one", "at least two", "at least four"], 2,
             "Section 15: at least two public consultations, within 60 days before submission."),
            ("Within how many days does the BLGF Regional Office review and endorse a proposed SMV?",
             ["15 days", "30 days", "45 days", "60 days"], 2,
             "Section 15: within 45 days from receipt."),
            ("Who certifies that the SMV follows the Philippine Valuation Standards?",
             ["the Secretary of Finance", "the governor", "the BLGF Regional Director", "the Commission on Audit"],
             0, "Section 16: the Secretary of Finance certifies it within 30 days."),
            ("An approved SMV takes effect ____ after its publication by the Department of Finance.",
             ["immediately", "15 days", "30 days", "one year"], 1,
             "Section 16: 15 days after publication."),
            ("After the first update, how often is the SMV updated?",
             ["every year", "every two years", "every three years", "every five years"], 2,
             "Section 19: every three years, together with a general revision of assessments."),
            ("Which of these allows an interim revision of the SMV?",
             ["a new road right-of-way", "a change of mayor", "a new fiscal year", "a request of one owner"], 0,
             "Section 19 lists new road right-of-way or similar infrastructure, calamities, public health "
             "emergencies, and correction of errors."),
            ("The SMV value of a lot is ₱800,000 and its deed of sale says ₱700,000. What base does the BIR use?",
             ["₱700,000", "₱750,000", "₱800,000", "₱1,500,000"], 2,
             "Section 18: the SMV or the actual gross selling price, whichever is higher."),
            ("Which office leads the carrying out of RA 12001?",
             ["the Bureau of Local Government Finance", "the BIR", "the Department of the Interior and Local "
              "Government", "the Land Registration Authority"], 0,
             "Section 5: the BLGF of the Department of Finance is the primary agency."),
        ],
        "sources": [
            "Republic Act No. 12001, Real Property Valuation and Assessment Reform Act (approved June 13, 2024), "
            "Sections 4, 5, 13, 15, 16, 18, 19, 20, 22, 23, 24 and 29",
            "Implementing Rules and Regulations of RA 12001 (BLGF Memorandum Circular No. 001.2025), Section 41",
        ],
    },
    # ------------------------------------------------------------------ Note 17
    {
        "number": 17,
        "slug": "revenue-and-tax-impact-report",
        "title": "The revenue and tax impact report",
        "summary": "The report that tells the sanggunian what a new schedule of market values will raise and who "
                   "will feel it, the three options it must offer, and how to estimate the revenue.",
        "publish_on": "2027-01-01 21:00",
        "body": [
            "A new schedule of market values may raise the values on the assessment roll by a large amount, "
            "especially where the old schedule has not been updated for years. Before the new values reach anyone's tax bill, the law "
            "asks for a report that puts numbers on the change. Unless stated otherwise, the sections cited are "
            "from RA 12001 and its implementing rules (IRR).",
            ("h", "What the law requires"),
            ("table", ["Item", "Rule"], [
                ["Who prepares it", "The local assessor, together with the local treasurer (Section 17; IRR "
                                    "Section 36)."],
                ["When", "Within 30 days from receipt of the approved schedule (Section 17; IRR Section 37)."],
                ["To whom", "The local chief executive and the sanggunian (Section 17)."],
                ["Contents", "The revenue estimate from the new schedule, the impact on taxpayers, and three "
                             "proposed options for adjusting the assessment levels and tax rates in the existing "
                             "ordinance (IRR Section 37)."],
                ["Who decides", "The sanggunian. The IRR does not take away its power under RA 7160 to set and "
                                "adjust assessment levels and tax rates (IRR Section 38)."],
            ]),
            "The treasurer's part matters. The assessor knows the values; the treasurer knows what is billed, "
            "what is actually collected, and how much is in arrears. A revenue estimate needs both.",
            ("h", "The levers in the options"),
            "Under RA 12001, the Secretary of Finance certifies the values. What the sanggunian controls is how "
            "much of that value is taxed:",
            ("table", ["Lever", "Limit"], [
                ["Assessment level for each class", "Up to the ceilings in Section 218 of RA 7160, such as 20% "
                                                    "for residential land and 40% for agricultural land."],
                ["Basic tax rate", "Up to 1% for a province, or 2% for a city or a municipality in Metro Manila "
                                   "(RA 7160, Section 233). The Special Education Fund adds 1% (Section 235)."],
                ["Discount for early payment", "Up to 20% (RA 7160, Section 251)."],
            ]),
            "Lowering the assessment level of a class lowers the tax for that class only. Lowering the basic rate "
            "lowers it for every class at once. Good options show the trade-off, for example one that keeps the "
            "present levels, one that lowers them moderately, and one that keeps the tax close to what owners pay "
            "now.",
            ("h", "The 6% first-year cap"),
            "Whatever option is chosen, in the first year an approved schedule takes effect, any increase in real "
            "property taxes is limited to 6% (Section 29). The cap is measured against the taxes assessed before "
            "the first schedule under the law, and applies to each kind of real property tax, including the "
            "Special Education Fund, idle land tax and special levies (IRR Section 55). For later years, the local "
            "government may enact an ordinance setting its own cap (Section 29).",
            ("tip", "The cap protects owners in Year 1 only. A report that shows only Year 1 hides the real jump, "
                    "which arrives in Year 2 unless the sanggunian adjusts levels, rates or the later-year cap."),
            ("h", "Estimating the revenue, step by step"),
            ("list", [
                "List every property on the roll with its class, area and present tax.",
                "Apply the new unit values to get each property's new market value.",
                "Apply each option's assessment levels and tax rates to get the new tax.",
                "Apply the 6% cap property by property to get Year 1 billings.",
                "Add up by class and by barangay, and count how many owners face a large increase.",
                "Multiply the billings by the share actually collected in past years, so the estimate is cash, "
                "not just bills.",
                "Show the shares: in a province, basic tax goes 35% to the province, 40% to the municipality and "
                "25% to the barangay, and the Special Education Fund is split equally between the provincial and "
                "municipal school boards (RA 7160, Sections 271 and 272).",
            ]),
            "The step on collections is where the treasurer's records count most. How the collection rate is "
            "measured changes the answer; the Data Analytics Series, Part 8, shows why.",
        ],
        "link": ("How to measure collection rates honestly:", "Metrics and KPIs That Tell the Truth",
                 "/blog/data-analytics-part-8-metrics-and-kpis/"),
        "example": (
            "Worked example: three options for one lot",
            [
                "A 400 sq m residential lot in a municipality. Old unit value ₱1,000 a square meter; new unit "
                "value ₱3,500. Present assessment level 20%. Tax rate 2% (basic 1% plus Special Education Fund "
                "1%).",
                "Present tax: 400 × ₱1,000 = ₱400,000 market value × 20% = ₱80,000 assessed value × 2% = ₱1,600.",
                "New market value: 400 × ₱3,500 = ₱1,400,000.",
                "Option A, keep the 20% level: ₱1,400,000 × 20% × 2% = ₱5,600, or 250% more.",
                "Option B, lower the level to 10%: ₱1,400,000 × 10% × 2% = ₱2,800, or 75% more.",
                "Option C, lower the level to 7%: ₱1,400,000 × 7% × 2% = ₱1,960, or 22.5% more.",
                "Year 1 under any of the three: the increase is capped at 6%, so ₱1,600 × 1.06 = ₱1,696.",
            ],
            "Every option bills ₱1,696 in Year 1. From Year 2 the owner pays ₱5,600 under A, ₱2,800 under B or "
            "₱1,960 under C, unless a later-year cap ordinance applies.",
        ),
        "practice": [
            ("Who prepares the revenue and tax impact report?",
             ["the local assessor, with the local treasurer", "the BLGF Regional Office", "the sanggunian",
              "the Secretary of Finance"], 0,
             "Section 17 and IRR Section 36: the assessor, together with the treasurer."),
            ("Within how many days from receipt of the approved schedule must the report be submitted?",
             ["15 days", "30 days", "45 days", "60 days"], 1,
             "Section 17 and IRR Section 37: within 30 days."),
            ("How many proposed options must the report contain?",
             ["1", "2", "3", "5"], 2,
             "Section 17: three proposed options for adjusting assessment levels and tax rates."),
            ("The report's options adjust ____.",
             ["assessment levels and tax rates", "the unit values in the schedule", "the barangay shares",
              "the Philippine Valuation Standards"], 0,
             "IRR Section 37: options on the assessment levels and tax rates in the existing ordinance."),
            ("To whom is the report submitted?",
             ["the local chief executive and the sanggunian", "the BIR", "the Commission on Audit",
              "the provincial governor only"], 0,
             "Section 17: to the local chief executive and the sanggunian."),
            ("In the first year an approved schedule takes effect, an increase in real property tax is limited "
             "to ____.",
             ["3%", "6%", "10%", "20%"], 1,
             "Section 29: a maximum of 6%."),
            ("The 6% cap applies to ____.",
             ["each kind of real property tax, including the SEF and idle land tax", "the basic tax only",
              "commercial property only", "properties worth over ₱1 million only"], 0,
             "IRR Section 55: it applies to each type of real property tax, including the SEF, idle land tax "
             "and special levies."),
            ("A lot's tax was ₱3,000. Under the new schedule it would be ₱7,500. What is the most it can be "
             "billed in the first year?",
             ["₱3,000", "₱3,180", "₱3,450", "₱7,500"], 1,
             "₱3,000 × 1.06 = ₱3,180 (Section 29)."),
            ("Which lever lowers the tax of one class without changing the others?",
             ["its assessment level", "the basic tax rate", "the Special Education Fund rate",
              "the barangay share"], 0,
             "Assessment levels are set class by class (RA 7160, Section 218); the basic rate applies to all "
             "classes."),
            ("A new schedule raises a lot's market value to ₱900,000. At a 10% level and a 2% total rate, what is "
             "the full tax from Year 2?",
             ["₱900", "₱1,800", "₱9,000", "₱18,000"], 1,
             "₱900,000 × 10% = ₱90,000 assessed value × 2% = ₱1,800."),
        ],
        "sources": [
            "Republic Act No. 12001, Real Property Valuation and Assessment Reform Act, Sections 17 and 29",
            "Implementing Rules and Regulations of RA 12001 (BLGF Memorandum Circular No. 001.2025), Sections 36, "
            "37, 38 and 55",
            "Republic Act No. 7160, Local Government Code of 1991, Sections 218, 233, 235, 251, 271 and 272",
        ],
    },
]

for _n in NOTES_16_TO_17:
    _n["practice"] = _spread(_n["practice"])
