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
        "checked_against": "RA 12001 and its implementing rules",
        "body": [
            "Every real property tax bill starts with a market value. For land and buildings, that value comes "
            "from the schedule of market values, or SMV. Note 2 showed how the tax is computed. This note is about "
            "the schedule itself: who makes it, who checks it, and how long each step may take. Unless stated "
            "otherwise, the sections cited are from Republic Act No. 12001, the Real Property Valuation and "
            "Assessment Reform Act, approved on June 13, 2024.",
            ("h", "Words to know"),
            ("table", ["Word", "What it means"], [
                ["Real property", "Land, buildings, machinery and other improvements on land. Local "
                                  "governments tax them every year."],
                ["Schedule of market values (SMV)", "A table of base values per unit, such as per square "
                                                    "meter, for each kind of real property in a local "
                                                    "government, except machinery (Section 4)."],
                ["Unit value", "The value of one unit of property, such as one square meter of land, as shown "
                               "in the SMV."],
                ["Assessor", "The local official who values real property and keeps the list of taxable "
                             "property."],
                ["Sanggunian", "The local council that passes ordinances: the Sangguniang Panlalawigan of a "
                               "province, the Sangguniang Panlungsod of a city, or the Sangguniang Bayan of a "
                               "municipality."],
                ["BLGF", "The Bureau of Local Government Finance, an office of the Department of Finance. It "
                         "leads the carrying out of RA 12001 (Section 5)."],
                ["IRR", "Implementing rules and regulations: the detailed rules that carry out a law. The IRR "
                        "of RA 12001 is BLGF Memorandum Circular No. 001.2025."],
            ]),
            ("h", "What the schedule is"),
            "The SMV lists base unit market values for all kinds of real property in a local government, except "
            "machinery (Section 4). The assessor uses these unit values to work out the market value of each "
            "property. In the simplest case, a lot's market value is its area times its unit value.",
            "Market value has a legal meaning. It is the estimated price at which a property would change hands "
            "on the valuation date between a willing buyer and a willing seller (Section 4). The two must deal "
            "at arm's length, which means as independent parties, each looking after their own interest. The "
            "property must have been properly offered for sale. Both sides must know what they are doing, act "
            "carefully, and not be forced to deal.",
            ("h", "One standard for the whole country"),
            "Every schedule must follow the Philippine Valuation Standards, or PVS. These are national rules for "
            "valuing property. They are based on the International Valuation Standards and approved by the "
            "Secretary of Finance (Section 4). The BLGF develops them (Section 13). Because every assessor uses "
            "the same rules, property is valued the same way across the country.",
            ("h", "From proposal to approved schedule"),
            ("table", ["Step", "Rule"], [
                ["1. Preparation", "The provincial, city or municipal assessor prepares the proposed SMV. It must "
                                   "be done within 12 months after notice from the BLGF (Section 15)."],
                ["2. Publication", "The proposal is published for at least two weeks before the public "
                                   "consultation. It goes on the local government's website and is posted in "
                                   "two conspicuous places (Section 15)."],
                ["3. Public consultation", "Two public consultations must be held within the 60 days before the "
                                           "proposal is submitted (Section 15)."],
                ["4. BLGF review", "The assessor submits the proposal to the BLGF Regional Office. It reviews "
                                   "the proposal and sends it to the head of the BLGF within 45 days. Cities and "
                                   "the lone municipality in Metro Manila submit to the BLGF Central Office "
                                   "instead. The head of the BLGF then endorses it to the Secretary of Finance "
                                   "within 30 days (Section 15)."],
                ["5. Certification", "Within 30 days, the Secretary of Finance certifies that the schedule "
                                     "follows the latest PVS. If it does not, it is sent back with a written "
                                     "explanation. The assessor must resubmit it within 30 days (Section 16)."],
                ["6. Effectivity", "The Department of Finance publishes the approved schedule in the Official "
                                   "Gazette or on its website. It takes effect 15 days after publication "
                                   "(Section 16)."],
            ]),
            ("tip", "The public consultation is the taxpayer's chance to question a unit value before it becomes "
                    "official. Watch the local government's website and its posted notices."),
            ("h", "How often it is updated"),
            "The first update had to be done within two years after the law took effect. The IRR set that "
            "deadline at July 5, 2026 (Section 19; IRR Section 41). After that, the schedule is updated every "
            "three years. At the same time, the assessor does a general revision, which means reassessing all "
            "real property in the local government (Section 19).",
            "A smaller update, called an interim revision, is allowed in between. Examples are when a new road "
            "is built, after a calamity or a declared public health emergency, or to correct errors in the "
            "schedule (Section 19).",
            ("h", "Where the values come from"),
            "The BLGF keeps the Real Property Information System. It is an electronic database of property "
            "sales, leases, mortgages, donations and other transfers. It also holds construction costs and "
            "machinery prices (Section 22).",
            "Registers of deeds are the offices that record land titles and deeds. Every three months, they send "
            "the assessor a summary of their records (Section 23). Once the database is running, registers of "
            "deeds, the Bureau of Internal Revenue (BIR), notaries public, building officials and geodetic "
            "engineers send their transaction data to the BLGF every quarter (Section 24).",
            ("h", "Who else uses it"),
            ("list", [
                "Local governments. The approved SMV is the basis of real property taxes and of the general "
                "revision of assessments (Section 18).",
                "The BIR. For national taxes on a property, it uses the SMV value or the actual selling price, "
                "whichever is higher (Section 18). Until a local government's schedule is updated, the BIR uses "
                "the existing SMV, its own zonal values (its table of land values), or the actual price, "
                "whichever is highest (Section 29).",
                "Other government agencies, when they appraise real property (Section 18).",
                "The Seal of Good Local Governance. Following the law is an added indicator for this national "
                "recognition of well-run local governments (Section 20).",
            ]),
            "A new schedule does not set the tax by itself. The sanggunian still decides the assessment levels, "
            "which are the share of market value that is taxed, and the tax rates (IRR Section 38). The tax "
            "increase in the first year is also capped at 6% (Section 29). Note 17 explains the report that "
            "helps the sanggunian decide.",
        ],
        "example": (
            "Worked example: counting the deadlines",
            [
                "In this example, each period is counted from the day after the office receives the papers.",
                "A province's proposed SMV reaches the BLGF Regional Office on December 1, 2027. Its 45 days for "
                "review end on January 15, 2028.",
                "The head of the BLGF receives it on January 12, 2028. The 30 days end on February 11, 2028.",
                "The Secretary of Finance receives it on February 8, 2028. The 30 days end on March 9, 2028. "
                "(2028 is a leap year, so February has 29 days.)",
                "The Department of Finance publishes the approved schedule on March 10, 2028. It takes effect "
                "15 days later, on March 25, 2028.",
                "Now the BIR. A 200 sq m lot has a unit value of ₱3,000 per square meter. Its value under the "
                "SMV is 200 × ₱3,000 = ₱600,000. The deed of sale says ₱500,000. The BIR computes its taxes on "
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
             ["1", "2", "3", "4"], 1,
             "Section 15: two mandatory public consultations, within 60 days before submission."),
            ("Within how many days does the BLGF Regional Office review and endorse a proposed SMV?",
             ["15 days", "30 days", "45 days", "60 days"], 2,
             "Section 15: within 45 days from receipt."),
            ("Who certifies that the SMV follows the Philippine Valuation Standards?",
             ["the Secretary of Finance", "the governor", "the BLGF Regional Director", "the Commission on Audit"],
             0, "Section 16: the Secretary of Finance certifies it within 30 days."),
            ("An approved SMV takes effect ____ after its publication by the Department of Finance.",
             ["immediately", "15 days", "30 days", "one year"], 1,
             "Section 16: 15 days after publication."),
            ("After the first update, the SMV is updated every ____.",
             ["1 year", "2 years", "3 years", "5 years"], 2,
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
            "Implementing Rules and Regulations of RA 12001 (BLGF Memorandum Circular No. 001.2025), Sections 38 "
            "and 41",
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
        "checked_against": "RA 12001, its implementing rules and RA 7160",
        "body": [
            "A new schedule of market values changes the values on the assessment roll, the assessor's official "
            "list of taxable property and its values. When values change, taxes can change too. So before the "
            "new values reach anyone's tax bill, the law asks for a report that shows the effect in numbers. "
            "This report is the assessor's task. The treasurer's own study of who actually pays is in Note 18. "
            "Unless stated otherwise, the sections cited are from RA 12001 and its implementing rules (IRR).",
            ("h", "Words to know"),
            ("table", ["Word", "What it means"], [
                ["Market value", "The price a property would fetch between a willing buyer and a willing seller. "
                                 "It comes from the schedule of market values, or SMV (Note 16)."],
                ["Assessment level", "The percentage of market value that is taxed. The sanggunian sets it for "
                                     "each class of property, such as residential or agricultural, up to the "
                                     "limits in RA 7160, Section 218."],
                ["Assessed value", "Market value × assessment level. The tax rate is applied to this amount "
                                   "(RA 7160, Section 199)."],
                ["Tax rate", "The percentage of the assessed value that is paid as tax each year."],
                ["Special Education Fund (SEF)", "An added 1% yearly tax on real property. It goes to the local "
                                                 "school board for public schools (RA 7160, Sections 235 and "
                                                 "272)."],
                ["Sanggunian", "The local council that passes ordinances, including the tax ordinance."],
                ["Local chief executive", "The governor, the city mayor or the municipal mayor."],
                ["Collection rate", "The share of the billed tax that is actually paid."],
            ]),
            ("h", "What the law requires"),
            ("table", ["Item", "Rule"], [
                ["Who prepares it", "The local assessor leads, together with the local treasurer (Section 17; "
                                    "IRR Section 36)."],
                ["When", "Within 30 days after the approved schedule is received (Section 17; IRR Section 37)."],
                ["To whom", "The local chief executive and the sanggunian (Section 17)."],
                ["Contents", "How much revenue the new schedule will raise, how it will affect taxpayers, and "
                             "three proposed options for adjusting the assessment levels and tax rates in the "
                             "present tax ordinance (IRR Section 37)."],
                ["Who decides", "The sanggunian. RA 7160 gives it the power to set and adjust assessment levels "
                                "and tax rates, and the IRR does not take that power away (IRR Section 38)."],
            ]),
            "The estimate needs two kinds of records. The assessor has the property values. The treasurer has "
            "the bills, the payments, and the unpaid taxes from past years.",
            ("h", "The levers in the options"),
            "The Secretary of Finance certifies the values in the schedule (Section 16). What the sanggunian "
            "controls is how much of each value is taxed, and at what rate. It has three levers:",
            ("table", ["Lever", "Limit"], [
                ["Assessment level for each class", "Up to the limits in RA 7160, Section 218. For example, up "
                                                    "to 20% for residential land and 40% for agricultural land."],
                ["Basic tax rate", "Up to 1% for a province, or up to 2% for a city or a municipality in Metro "
                                   "Manila (RA 7160, Section 233). The SEF adds 1% (Section 235)."],
                ["Discount for paying early", "Up to 20%, for taxes paid in advance according to the payment "
                                              "schedule (RA 7160, Section 251)."],
            ]),
            "Lowering the assessment level of one class lowers the tax for that class only. Lowering the basic "
            "rate lowers it for every class at once. Good options show these trade-offs. For example, one option "
            "keeps the present levels, one lowers them a little, and one keeps the tax close to what owners pay "
            "now.",
            ("h", "The 6% first-year cap"),
            "Whatever option is chosen, the law protects owners in the first year. In the first year an approved "
            "schedule takes effect, any increase in real property tax is limited to 6% (Section 29).",
            "The 6% is measured against the taxes assessed before the first schedule under the law. It applies "
            "to each kind of real property tax, including the SEF, the idle land tax and special levies (IRR "
            "Section 55). For later years, the local government may pass an ordinance that sets its own cap "
            "(Section 29).",
            ("tip", "The cap covers Year 1 only. A report that shows only Year 1 hides the real jump. That jump "
                    "comes in Year 2, unless the sanggunian adjusts the levels, the rates, or the cap for later "
                    "years."),
            ("h", "Two common misconceptions"),
            ("list", [
                "\"The tax follows the market value alone.\" It does not. The tax is market value × assessment "
                "level × tax rate. The sanggunian sets the levels and rates by ordinance (RA 7160, Sections 218 "
                "and 233; IRR Section 38).",
                "\"A higher schedule means a tax that rises just as much.\" It does not. In the worked example "
                "below, the lot's market value rises 250%. Its Year 1 bill rises only 6%, because of the cap "
                "(Section 29). Under Option C, its full tax from Year 2 rises 22.5%.",
            ]),
            ("h", "Estimating the revenue, step by step"),
            ("list", [
                "List every property on the assessment roll, with its class, area and present tax.",
                "Apply the new unit values to get each property's new market value.",
                "For each option, apply its assessment levels and tax rates to get the new tax.",
                "Apply the 6% cap, property by property, to get the Year 1 bills.",
                "Add up the results by class and by barangay. Count how many owners face a large increase.",
                "Multiply the bills by the collection rate of past years, from the treasurer's compliance "
                "study (Note 18). This turns expected bills into expected cash.",
                "Show how the money is shared. In a province, the basic tax goes 35% to the province, 40% to the "
                "municipality and 25% to the barangay. The SEF is split equally between the provincial and "
                "municipal school boards (RA 7160, Sections 271 and 272).",
            ]),
            "How the collection rate is measured changes the answer. The Data Analytics Series, Part 8, shows "
            "why.",
        ],
        "link": ("How to measure collection rates honestly:", "Metrics and KPIs That Tell the Truth",
                 "/blog/data-analytics-part-8-metrics-and-kpis/"),
        "example": (
            "Worked example: three options for one lot",
            [
                "The lot: 400 sq m, residential, in a municipality. The old unit value is ₱1,000 per square "
                "meter. The new one is ₱3,500. The assessment level is 20%. The tax rate is 2% (basic tax 1% "
                "plus SEF 1%).",
                "The formula: market value × assessment level = assessed value. Then assessed value × tax rate "
                "= tax.",
                "Present tax: 400 × ₱1,000 = ₱400,000 market value. ₱400,000 × 20% = ₱80,000 assessed value. "
                "₱80,000 × 2% = ₱1,600.",
                "New market value: 400 × ₱3,500 = ₱1,400,000.",
                "Option A, keep the level at 20%: ₱1,400,000 × 20% × 2% = ₱5,600. That is 250% more.",
                "Option B, lower the level to 10%: ₱1,400,000 × 10% × 2% = ₱2,800. That is 75% more.",
                "Option C, lower the level to 7%: ₱1,400,000 × 7% × 2% = ₱1,960. That is 22.5% more.",
                "Year 1, under any option: the increase is capped at 6%. ₱1,600 × 1.06 = ₱1,696.",
            ],
            "Every option bills ₱1,696 in Year 1. From Year 2, the owner pays ₱5,600 under A, ₱2,800 under B, "
            "or ₱1,960 under C, unless a cap ordinance for later years applies.",
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
            "Republic Act No. 12001, Real Property Valuation and Assessment Reform Act, Sections 16, 17 and 29",
            "Implementing Rules and Regulations of RA 12001 (BLGF Memorandum Circular No. 001.2025), Sections 36, "
            "37, 38 and 55",
            "Republic Act No. 7160, Local Government Code of 1991, Sections 199, 218, 233, 235, 251, 271 and 272",
        ],
    },
]

for _n in NOTES_16_TO_17:
    _n["practice"] = _spread(_n["practice"])
