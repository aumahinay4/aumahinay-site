"""Study Note 18 (Butch, 2026-11-18 PH: the treasurer's tax compliance side was missing; the impact report is the
assessor's). Tuesday January 5, 2027, 9 pm, after Note 17.

Facts checked (November 2026) against:
- RA 7160 Sections 248, 250, 254, 256 and 270, as already checked for Note 3, and Section 470(b) as quoted in the
  BLGF Local Treasury Operations Manual (LTOM), 2nd Edition, Book I, Chapter 2, Section 6;
- LTOM 2nd Edition, Book I, Section 4 (duties of the Real Property Tax Division of a treasury office);
- RA 12001 Section 17 (the impact report is prepared by the assessor in coordination with the treasurer).
The measures and steps are plain arithmetic and general good practice, not quoted from any issuance. Kept apart
from Note 3 (delinquency remedies, interest, auction) and the Data Analytics Series, Part 8 (one collection
efficiency formula); this note is about measuring who pays and who does not. Worked example and quiz recomputed.
"""

from notes_2_10 import _spread

NOTES_18 = [
    {
        "number": 18,
        "slug": "real-property-tax-compliance-study",
        "title": "The real property tax compliance study",
        "summary": "The treasurer's side of real property tax: measuring who pays, who does not, and why, with "
                   "simple formulas, a worked example and the steps of a compliance study.",
        "publish_on": "2027-01-05 21:00",
        "checked_against": "RA 7160 and the BLGF Local Treasury Operations Manual",
        "body": [
            "Note 17 covered the revenue and tax impact report, which the assessor leads. It asks what a new "
            "schedule of market values would raise. This note covers the treasurer's side. It asks a different "
            "question: of the tax already due, how much is actually paid, and by whom? A study that answers this "
            "is called a tax compliance study. It shows where the money is lost before anyone talks about new "
            "values.",
            ("h", "Words to know"),
            ("table", ["Word", "What it means"], [
                ["Assessment roll", "The assessor's official list of taxable property, with each property's "
                                    "owner, class and assessed value."],
                ["Tax due", "The real property tax (basic tax and Special Education Fund) billed for the "
                            "current year."],
                ["Arrears", "Unpaid real property tax from earlier years."],
                ["Delinquent", "Not paid by the due date. A delinquent property is one with unpaid tax."],
                ["Collection efficiency", "How much of the tax due was actually collected, shown as a "
                                          "percentage."],
                ["Compliance", "Paying the tax in full and on time. A compliant owner owes nothing for the "
                               "year."],
            ]),
            ("h", "Who does what"),
            ("table", ["Office", "Role"], [
                ["Assessor", "Values each property and keeps the assessment roll. Gives the roll to the "
                             "treasurer on or before December 31 each year (RA 7160, Section 248). Leads the "
                             "revenue and tax impact report, with the treasurer's help (RA 12001, Section 17)."],
                ["Treasurer", "Collects the tax and keeps the payment records. Posts the notice of delinquency "
                              "(RA 7160, Section 254) and uses the remedies for unpaid tax (Section 256). Reports "
                              "regularly to the governor or mayor on tax collection efforts (Section 470(b))."],
            ]),
            "The BLGF's Local Treasury Operations Manual, in its model setup for a city treasury office, lists the "
            "work of the real property tax division. It updates the records of payments. It prepares the list of delinquent properties for posting "
            "and publication and sends notices of delinquency. It prepares monthly or quarterly reports of real "
            "property tax collection. It also recommends ways to increase collection. A compliance study pulls "
            "this work together into one picture.",
            ("h", "Three simple measures"),
            ("list", [
                "Current-year collection efficiency = tax collected for this year ÷ tax due for this year.",
                "Arrears collection rate = arrears collected during the year ÷ arrears at the start of the year.",
                "Compliance by count = number of properties fully paid for this year ÷ number of properties on "
                "the roll.",
            ]),
            "Keep the first two apart. If arrears payments are added to this year's collections, the result "
            "looks better than it is, and it can even pass 100%. Keep the third one too, because a few large "
            "payers can make the peso figures look good while most owners do not pay.",
            ("tip", "A payment is applied first to the owner's unpaid tax, interest and penalties of earlier years "
                    "(RA 7160, Section 250). Record which year each payment covers, or the split between this "
                    "year and arrears will be wrong."),
            ("h", "Steps of a compliance study"),
            ("list", [
                "Start from the assessment roll the assessor gave the treasurer.",
                "Match each property on the roll with its payment records, using the tax declaration number.",
                "Sort the properties into four groups: paid in full, partly paid, unpaid this year, and unpaid "
                "for several years.",
                "Compute the three measures, for the whole local government and for each barangay and class.",
                "List the records that do not match: properties on the roll with no payment record, and "
                "payments with no matching property. Send the list to the assessor so the roll can be "
                "corrected.",
                "List the largest delinquent accounts, and check how old each unpaid year is. The tax must be "
                "collected within five years from the date it became due, or within ten years from discovery "
                "if there was fraud (RA 7160, Section 270).",
                "Propose actions, such as notices, reminders, payment drives in barangays, and the legal "
                "remedies for owners who still do not pay. Note 3 explains those remedies.",
                "Report the results to the governor or mayor (Section 470(b)), and repeat the study each year "
                "to see if things improve.",
            ]),
            ("h", "How the two studies fit together"),
            "The assessor's impact report estimates what a new schedule would bill. The treasurer's compliance "
            "study shows what share of the bills actually turns into cash. The impact report needs that rate to "
            "turn expected bills into expected cash (Note 17). One without the other gives the sanggunian only "
            "half the picture.",
        ],
        "link": ("How to measure collection rates honestly:", "Metrics and KPIs That Tell the Truth",
                 "/blog/data-analytics-part-8-metrics-and-kpis/"),
        "example": (
            "Worked example: one year in a municipality",
            [
                "The roll has 8,000 properties. The tax due for this year (basic tax and SEF) is ₱12,000,000. "
                "Arrears on January 1 are ₱5,000,000. All figures are tax only, without interest.",
                "During the year, the treasurer collects ₱10,200,000 in tax. Of this, ₱8,400,000 is for this "
                "year and ₱1,800,000 is for arrears.",
                "Current-year collection efficiency: ₱8,400,000 ÷ ₱12,000,000 = 70%.",
                "Arrears collection rate: ₱1,800,000 ÷ ₱5,000,000 = 36%.",
                "Compliance by count: 5,200 properties are fully paid for this year. 5,200 ÷ 8,000 = 65%.",
                "The wrong way: ₱10,200,000 ÷ ₱12,000,000 = 85%. Mixing in arrears makes this year look 15 "
                "points better than it is.",
                "Unpaid at year end: ₱12,000,000 − ₱8,400,000 = ₱3,600,000 from this year, plus ₱5,000,000 − "
                "₱1,800,000 = ₱3,200,000 of older arrears, or ₱6,800,000 in all.",
            ],
            "Current-year efficiency is 70%, the arrears rate is 36%, and 65% of owners paid in full. The "
            "₱6,800,000 still unpaid is the list to work on next year.",
        ),
        "practice": [
            ("Whose records show which owners have paid their real property tax?",
             ["the local treasurer's", "the sanggunian's", "the BIR's", "the register of deeds'"], 0,
             "The treasurer collects the tax and keeps the payment records."),
            ("Who leads the revenue and tax impact report?",
             ["the local assessor, with the treasurer", "the local treasurer alone", "the sanggunian",
              "the BIR"], 0,
             "RA 12001, Section 17: the assessor prepares it in coordination with the treasurer."),
            ("To whom does the treasurer report regularly on tax collection efforts?",
             ["the governor or mayor", "the Commission on Audit", "the BIR", "the register of deeds"], 0,
             "RA 7160, Section 470(b)."),
            ("The tax due this year is ₱2,000,000. Collections for this year are ₱1,500,000. What is the "
             "current-year collection efficiency?",
             ["50%", "70%", "75%", "80%"], 2,
             "₱1,500,000 ÷ ₱2,000,000 = 75%."),
            ("Arrears on January 1 are ₱800,000, and ₱200,000 of them are collected during the year. What is the "
             "arrears collection rate?",
             ["20%", "25%", "40%", "80%"], 1,
             "₱200,000 ÷ ₱800,000 = 25%."),
            ("Of 4,000 properties on the roll, 2,600 are fully paid for this year. What is compliance by count?",
             ["35%", "60%", "65%", "70%"], 2,
             "2,600 ÷ 4,000 = 65%."),
            ("Why can all collections ÷ this year's tax due pass 100%?",
             ["because arrears payments are mixed in", "because of the 20% discount", "because of the 6% cap",
              "because the SEF is left out"], 0,
             "Payments of earlier years' tax are added to this year's collections, so the ratio overstates "
             "this year."),
            ("A payment from an owner with arrears is applied first to ____.",
             ["the unpaid tax, interest and penalties of earlier years", "this year's tax",
              "the next year's tax", "the barangay share"], 0,
             "RA 7160, Section 250."),
            ("Without fraud, the tax must be collected within ____ from the date it became due.",
             ["3 years", "5 years", "10 years", "15 years"], 1,
             "RA 7160, Section 270: five years, or ten years from discovery if there was fraud."),
            ("Which list should the treasurer send to the assessor after the study?",
             ["properties and payments whose records do not match", "the list of business permits",
              "the collectors' cash counts", "the list of barangay officials"], 0,
             "The assessor keeps the roll, so records that do not match are sent there to be corrected."),
        ],
        "sources": [
            "Republic Act No. 7160, Local Government Code of 1991, Sections 248, 250, 254, 256, 270 and 470(b)",
            "Republic Act No. 12001, Real Property Valuation and Assessment Reform Act, Section 17",
            "Bureau of Local Government Finance, Local Treasury Operations Manual, 2nd Edition, Book I "
            "(duties of the Real Property Tax Division; Section 6 on the treasurer's reports to the governor "
            "or mayor)",
        ],
    },
]

for _n in NOTES_18:
    _n["practice"] = _spread(_n["practice"])
