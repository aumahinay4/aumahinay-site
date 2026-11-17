"""Data Analytics blog series (Butch 2026-11-13 PH): Part 1 live Nov 13, 2026 (Butch: "post this first part today"),
then one part every few days at 9 pm PH ("YYYY-MM-DD 21:00") in the daily blog rotation (Butch 2026-11-14).

The series teaches the whole craft in plain words, from asking a good question to acting on the answer,
with examples from local treasury work. Every number, office and taxpayer in an example is made up.
The wording is the blog's own, not the course's or the ALTOS book's. Facts are checked privately
before each part is approved; per Butch, posts show no Sources section and no "coming next" teaser.
Newest first, like BLOG in content.py.
"""

SERIES = "Data Analytics Series"

DATA_POSTS = [
    {
        "title": "Data Analytics Series, Part 48: Average Growth Over Several Years, and Why Averaging the Percentages Misleads",
        "slug": "data-analytics-part-48-average-annual-growth",
        "category": "data",
        "date": "June 19, 2027",
        "summary": "Collections grew from ₱12.0 million to ₱16.1 million in five years. What was the average growth "
                   "per year? Averaging the yearly percentages gives the wrong answer. This part explains the "
                   "compound annual growth rate, computes it by formula and with RRI in Google Sheets, and shows "
                   "how to use it honestly.",
        "publish_on": "2027-06-19 21:00",
        "body": [
            "The draft report said business tax collections had grown by “an average of 6.5 percent a year” "
            "from 2021 to 2026. The treasurer tried the number: ₱12.0 million grown by 6.5 percent five times. "
            "She got about ₱16.4 million. The actual 2026 figure was ₱16.1 million.",
            "The analyst had averaged the five yearly growth rates. Each rate was right. The average was not "
            "the right summary.",
            "(The office and the collections are invented for this lesson. The Google Sheets function is real.)",
            "Part 30 separated percent change from percentage points. This part looks at growth across several "
            "years. Read to the end and you will know why averaging yearly percentages misleads, what the "
            "compound annual growth rate is, how to compute it with a formula and with RRI, how to use it for "
            "a careful projection, and which pitfalls to avoid.",
            ("photo", "blog/data-growth-rate.jpg", "Average growth over several years: the compound annual "
             "growth rate is the one steady rate that leads from the first value to the last. (Illustration: "
             "Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "The Practice Data"),
            "Type the years in column A and business tax collections, in millions of pesos, in column B.",
            ("point", "Rows 2 to 7", "2021: 12.0. 2022: 13.8. 2023: 12.4. 2024: 14.3. 2025: 15.2. 2026: 16.1."),
            ("point", "Yearly change", "In C3, type =B3/B2-1 and fill down to C7. Format as percent."),
            ("point", "The five changes", "Plus 15.0, minus 10.1, plus 15.3, plus 6.3 and plus 5.9 percent."),
            "2023 dipped, perhaps because of a delayed renewal deadline or a large business closing. Then "
            "collections recovered.",
            ("h", "Why Averaging the Percentages Misleads"),
            "=AVERAGE(C3:C7) returns about 6.5 percent. It looks reasonable. It is not the rate that turns "
            "₱12.0 million into ₱16.1 million.",
            ("point", "Percentages build on each other", "A 15 percent rise followed by a 10 percent fall does "
             "not bring you back to where you started plus 5. It leaves you about 3.5 percent above the start."),
            ("point", "Ups and downs inflate the average", "The more the yearly rates swing, the further their "
             "simple average drifts above the true steady rate."),
            ("point", "The test", "Apply the average five times. ₱12.0 million times 1.065, five times over, "
             "gives about ₱16.4 million, about ₱340,000 more than what was actually collected."),
            "Part 36 showed how averaging averages misleads when groups differ in size. This is a cousin of the "
            "same problem: rates that compound need a different kind of average.",
            ("h", "The Compound Annual Growth Rate"),
            "The compound annual growth rate, often shortened to CAGR, answers a simple question: what single "
            "steady yearly rate would lead from the first value to the last in the same number of years?",
            ("point", "The formula", "(last ÷ first) raised to the power of (1 ÷ number of years), minus 1."),
            ("point", "Count the years correctly", "From 2021 to 2026 is 5 years of growth, not 6. Count the "
             "gaps between years, not the years listed."),
            ("point", "In Google Sheets", "=(B7/B2)^(1/5)-1 returns about 6.05 percent."),
            ("point", "Check it", "₱12.0 million times 1.0605, five times over, gives ₱16.1 million. It lands "
             "on the actual figure, which the simple average did not."),
            ("h", "The Same Answer With RRI"),
            "Google Sheets has a function built for this. Google’s help says “The RRI function returns the "
            "interest rate needed for an investment to reach a specific value within a given number of "
            "periods.” Collections are not an investment, but the arithmetic is the same.",
            ("point", "Syntax", "RRI(number_of_periods, present_value, future_value)"),
            ("point", "Formula", "=RRI(5, B2, B7) returns about 6.05 percent."),
            ("point", "Why use it", "It is easier to read than the power formula, and the number of periods is "
             "written plainly as the first argument."),
            ("photo", "blog/data-growth-rate-lines.jpg", "Actual collections with their dip in 2023, the steady "
             "6.05 percent path that ends at the same ₱16.1 million, and the 6.5 percent path that overshoots. "
             "Figures are invented. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Using the Rate Honestly"),
            "A compound annual growth rate is a summary, not a description of what happened each year.",
            ("point", "It hides the path", "Steady growth and a crash followed by a recovery can give the same "
             "rate. Show the yearly figures or a chart beside it."),
            ("point", "It depends on the endpoints", "Start in 2022 instead of 2021, and the rate over four "
             "years is about 3.9 percent. Choosing a start year that makes the rate look good is a common "
             "trick. Say why you chose the years you did."),
            ("point", "Nominal or real", "These are nominal pesos. Part 41 showed how to adjust for inflation. "
             "Growth in real terms will usually be lower."),
            ("point", "Rate changes and new taxes", "If a rate was raised in the middle of the period, part of "
             "the growth came from the ordinance, not from more business."),
            ("h", "Comparing Two Sources Fairly"),
            "The rate is most useful for comparing things that started at different sizes.",
            ("point", "Two revenue sources", "Suppose market fees grew from ₱4.0 million to ₱5.6 million, and "
             "real property tax from ₱8.0 million to ₱10.5 million, over the same five years."),
            ("point", "Raw increases mislead", "Real property tax rose by ₱2.5 million and market fees by ₱1.6 "
             "million, so real property tax looks like the faster grower."),
            ("point", "Rates tell a different story", "=RRI(5, 4.0, 5.6) returns about 7.0 percent for market "
             "fees, and =RRI(5, 8.0, 10.5) about 5.6 percent for real property tax."),
            "Market fees grew faster relative to their size. Whether that matters depends on the question, but "
            "the reader deserves to see both views. Part 30 made the same point about reporting change in pesos "
            "and in percent.",
            ("point", "Same period for both", "Compare rates only over the same years. A rate from 2021 to 2026 "
             "and another from 2023 to 2026 cannot be compared fairly."),
            ("h", "A Careful Projection"),
            "The rate can support a rough projection, as long as it is labeled as one.",
            ("point", "One year ahead", "₱16.1 million times 1.0605 is about ₱17.1 million for 2027."),
            ("point", "Give a range", "Part 45 built low, likely and high cases. The yearly changes here ranged "
             "from minus 10 to plus 15 percent, so a single figure claims too much."),
            ("point", "Compare with other methods", "Part 31 of Inside the Local Treasury described how income "
             "estimates are built by source. A growth rate is a check on that work, not a replacement for it."),
            ("h", "Back to the Report"),
            "The analyst replaced “an average of 6.5 percent a year” with “collections grew from ₱12.0 million "
            "in 2021 to ₱16.1 million in 2026, equal to about 6 percent a year compounded, with a dip in 2023.” "
            "She added the yearly table and a small line chart.",
            "The treasurer checked the new figure the same way as before. This time it landed on ₱16.1 million.",
            ("h", "Mistakes to Avoid"),
            ("point", "Averaging yearly percentages", "Use the compound rate for growth over several years."),
            ("point", "Counting years instead of gaps", "2021 to 2026 is 5 periods."),
            ("point", "Hiding the path", "Show the yearly figures with the rate."),
            ("point", "Choosing flattering endpoints", "Explain the period, and try another to see how much "
             "the rate changes."),
            ("h", "Key Takeaways"),
            ("point", "Rates compound", "Their simple average overstates steady growth when they swing."),
            ("point", "CAGR", "(last ÷ first)^(1 ÷ years) − 1, the one steady rate that fits."),
            ("point", "RRI does it in one step", "=RRI(periods, first, last)."),
            ("point", "Report it with context", "Yearly figures, the period chosen, and nominal or real pesos."),
            ("h", "Your Part 48 Exercise"),
            ("point", "Step 1", "Enter the practice data and compute the five yearly changes."),
            ("point", "Step 2", "Compare =AVERAGE(C3:C7) with =RRI(5, B2, B7)."),
            ("point", "Step 3", "Grow ₱12.0 million at each rate for five years and see which lands on ₱16.1 "
             "million."),
            ("point", "Step 4", "Compute the rate from 2022 instead of 2021 and explain the difference."),
            ("cta", "Read: Data Analytics Series, Part 30: Percent Change or Percentage Points? Reporting Growth Without Confusion", "/blog/data-analytics-part-30-percent-change/"),
            ("cta", "Read: Data Analytics Series, Part 36: Weighted Averages, and Why Averaging Averages Misleads", "/blog/data-analytics-part-36-weighted-averages/"),
            ("cta", "Read: Data Analytics Series, Part 41: Real or Nominal Pesos? Adjusting Collections for Inflation", "/blog/data-analytics-part-41-real-and-nominal-pesos/"),
            ("cta", "Read: Data Analytics Series, Part 45: What If? Low, Likely and High Scenarios in Google Sheets", "/blog/data-analytics-part-45-what-if-scenarios/"),
            ("ask", "Which growth figure in your office’s reports was computed by averaging percentages?"),
        ],
    },
    {
        "title": "Data Analytics Series, Part 47: Break-Even Analysis, How Many Before It Pays for Itself?",
        "slug": "data-analytics-part-47-break-even-analysis",
        "category": "data",
        "date": "June 16, 2027",
        "summary": "Should the office buy its own printer for certified copies, or keep sending the work out? A "
                   "break-even analysis answers with one number: the volume at which two choices cost the same. "
                   "This part separates fixed and variable costs, computes the break-even point in Google "
                   "Sheets, draws it, and tests how sure the answer is.",
        "publish_on": "2027-06-16 21:00",
        "body": [
            "The assessor’s office and the treasury shared a problem. Taxpayers asked for certified copies of "
            "their tax declarations, and each copy went to a print shop across the street at ₱40 a page, with a "
            "messenger walking back and forth.",
            "A supplier offered a printer and scanner for ₱180,000. The administrative officer asked the analyst "
            "a fair question: “At how many copies a year does buying our own machine become cheaper?”",
            "(The office, the prices and the volumes are invented for this lesson. The method is standard, and "
            "the Google Sheets formulas are real. Any fee for copies must come from the local government’s own "
            "ordinance.)",
            "Part 45 built low, likely and high scenarios. This part answers a narrower question that comes up "
            "whenever an office weighs a purchase: how many before it pays for itself? By the end of this post, "
            "you will know the difference between fixed and variable costs, how to compute a break-even point "
            "by hand and in Google Sheets, how to compare two options with a crossover point, how to draw it, "
            "and how to check whether the answer holds up.",
            ("photo", "blog/data-break-even.jpg", "Break-even analysis: fixed costs, variable costs per unit, "
             "and the volume where two choices cost the same. (Illustration: Butch Mahinay, aumahinay.dev)",
             "medium"),
            ("h", "Fixed and Variable Costs"),
            "Every cost in a break-even analysis goes into one of two groups.",
            ("point", "Fixed costs", "Costs that stay the same whether the office prints 100 copies or 3,000: "
             "the machine itself, spread over its useful life, and a yearly maintenance contract."),
            ("point", "Variable costs", "Costs that rise with every copy: paper, toner and the security paper "
             "used for certified copies."),
            "For the printer, the analyst gathered these figures.",
            ("point", "Machine", "₱180,000, expected to last 5 years, so ₱36,000 a year."),
            ("point", "Maintenance contract", "₱12,000 a year."),
            ("point", "Fixed cost per year", "₱36,000 + ₱12,000 = ₱48,000."),
            ("point", "Variable cost per copy", "₱15 for paper, toner and security paper."),
            ("point", "Print shop price per copy", "₱40, with no fixed cost."),
            "Spreading the purchase price over its life is a simplification. It treats the machine as costing "
            "a fifth of its price each year, which is enough for a first answer.",
            ("h", "Step 1: The Crossover Point by Hand"),
            "Write each option as a cost for a given number of copies, which we can call Q.",
            ("point", "Own printer", "₱48,000 + ₱15 × Q"),
            ("point", "Print shop", "₱40 × Q"),
            ("point", "Set them equal", "48,000 + 15Q = 40Q, so 25Q = 48,000, and Q = 1,920 copies a year."),
            "Below 1,920 copies a year, the print shop is cheaper. Above it, the office’s own machine is "
            "cheaper. The ₱25 saved on each copy, the difference between ₱40 and ₱15, has to pay back the "
            "₱48,000 of fixed cost first.",
            "That ₱25 has a name: the margin per unit. The general rule is break-even volume equals fixed cost "
            "divided by margin per unit.",
            ("h", "Step 2: The Same Thing in Google Sheets"),
            "Put each number in its own labeled cell, as Part 45 advised.",
            ("point", "Inputs", "B1: 180000 (machine). B2: 5 (years of life). B3: 12000 (maintenance). B4: 15 "
             "(variable cost per copy). B5: 40 (print shop price)."),
            ("point", "Fixed cost per year", "In B7: =B1/B2+B3 returns 48,000."),
            ("point", "Crossover", "In B8: =B7/(B5-B4) returns 1,920."),
            "Change any input and the crossover moves. If the print shop raised its price to ₱45, B8 would "
            "drop to 1,600 copies. Part 46 showed how to give cells like these plain names, so the formula "
            "could read =FixedCost/(ShopPrice-CopyCost).",
            ("h", "Step 3: Draw It"),
            "A chart makes the crossover visible to people who do not want to read formulas.",
            ("point", "A column of volumes", "D2 to D7: 0, 500, 1000, 1500, 2000, 2500."),
            ("point", "Own printer cost", "E2: =$B$7+$B$4*D2, filled down."),
            ("point", "Print shop cost", "F2: =$B$5*D2, filled down."),
            ("point", "The chart", "Select D1:F7 and insert a line chart. The two lines cross between 1,500 "
             "and 2,000 copies."),
            "At 2,500 copies, the office’s own printer costs ₱85,500 a year against ₱100,000 at the print shop. "
            "At 1,000 copies, it costs ₱63,000 against ₱40,000.",
            ("photo", "blog/data-break-even-chart.jpg", "Two cost lines cross at 1,920 copies a year. Below that, "
             "the print shop is cheaper. Above it, the office’s own printer is. Figures are invented. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Step 4: How Many Copies Does the Office Really Make?"),
            "A break-even point means little without a good estimate of volume. The analyst counted the print "
            "shop’s receipts for the past 12 months: 1,240 copies. Requests had grown slowly, by about 5 "
            "percent a year.",
            "At about 1,300 copies a year, the office stays well below the crossover. Buying the machine would "
            "cost about ₱67,500 a year, against ₱52,000 at the print shop.",
            ("point", "Look at the range, not one guess", "Even at a high estimate of 1,600 copies, the print "
             "shop is still cheaper."),
            ("point", "Check the trend", "At 5 percent growth a year, 1,240 copies would take roughly nine "
             "years to pass 1,920, longer than the machine’s expected life."),
            ("point", "Count, do not guess", "Receipts, logbooks and request forms give real volumes. Part 12 "
             "showed how to keep such records one row per request."),
            ("h", "Step 5: Is the Answer Sturdy?"),
            "Change one input at a time, as Part 45 did, and see whether the decision flips.",
            ("point", "Machine lasts 7 years instead of 5", "Fixed cost drops to about ₱37,700. Crossover about "
             "1,510 copies. Still above 1,300."),
            ("point", "Print shop raises its price to ₱50", "Crossover 1,371. Close to the current volume."),
            ("point", "Toner costs more, ₱20 per copy", "Crossover 2,400. The print shop looks even better."),
            "The decision holds in most cases, but it is close if the print shop raises its price. That is "
            "worth watching.",
            ("h", "What the Numbers Leave Out"),
            ("point", "Time", "The messenger’s walk and the taxpayer’s wait have a cost that is not in the "
             "formula. If an in-house copy saves a return visit, say so beside the numbers."),
            ("point", "Control of records", "Keeping certified copies inside the office may reduce the risk of "
             "documents being mishandled. That is a reason, not a peso figure."),
            ("point", "Other uses", "A scanner could also serve records digitization. Include that only if the "
             "work is planned and funded."),
            "Report these alongside the break-even result, clearly labeled as judgments, not calculations.",
            ("h", "Back to the Printer"),
            "The analyst reported that the office would need about 1,920 copies a year to justify the machine, "
            "and it made about 1,240. She recommended staying with the print shop, asking for a written price "
            "for the next two years, and checking the volume again in a year.",
            "She added one line: if the print shop price rose to ₱50 and requests kept growing, the decision "
            "would be worth revisiting.",
            ("h", "Mistakes to Avoid"),
            ("point", "Counting the full purchase price in one year", "Spread it over the useful life."),
            ("point", "Forgetting variable costs", "Paper, toner and security paper add up."),
            ("point", "Guessing the volume", "Count from records."),
            ("point", "Ignoring what the formula leaves out", "List time and control separately."),
            ("h", "Key Takeaways"),
            ("point", "Fixed and variable", "Sort every cost into one group."),
            ("point", "Break-even", "Fixed cost divided by the saving per unit."),
            ("point", "Compare with real volume", "Count from records, and look at a range."),
            ("point", "Test the inputs", "Change one at a time and see whether the decision flips."),
            ("h", "Your Part 47 Exercise"),
            ("point", "Step 1", "Build the input cells and confirm the crossover is 1,920 copies."),
            ("point", "Step 2", "Draw the two cost lines for 0 to 2,500 copies."),
            ("point", "Step 3", "Change the print shop price to ₱50 and find the new crossover."),
            ("point", "Step 4", "Apply the method to a choice in your own office, such as renting or buying a "
             "vehicle."),
            ("cta", "Read: Data Analytics Series, Part 45: What If? Low, Likely and High Scenarios in Google Sheets", "/blog/data-analytics-part-45-what-if-scenarios/"),
            ("cta", "Read: Data Analytics Series, Part 46: Named Ranges and ARRAYFORMULA, Formulas Anyone Can Read", "/blog/data-analytics-part-46-named-ranges-arrayformula/"),
            ("cta", "Read: Data Analytics Series, Part 27: Choosing the Right Chart, Starting From the Question", "/blog/data-analytics-part-27-choosing-the-right-chart/"),
            ("cta", "Read: Inside the Local Treasury, Part 15: Fee or Tax? Why the Difference Matters", "/blog/fee-or-tax/"),
            ("ask", "Which purchase in your office would look different after a break-even analysis?"),
        ],
    },
    {
        "title": "Data Analytics Series, Part 46: Named Ranges and ARRAYFORMULA, Formulas Anyone Can Read",
        "slug": "data-analytics-part-46-named-ranges-arrayformula",
        "category": "data",
        "date": "June 13, 2027",
        "summary": "=SUM(LastYear)*(1+Growth) is easier to check than =SUM(Sheet2!$B$2:$B$13)*(1+Sheet2!$E$1). "
                   "This part shows how to give ranges and key cells plain names in Google Sheets, and how one "
                   "ARRAYFORMULA can fill a whole column, so a sheet is easier to read, check and hand over.",
        "publish_on": "2027-06-13 21:00",
        "body": [
            "The monthly targets sheet had been built by an analyst who had since moved to another office. "
            "Cell C2 held =Sheet2!$B2*(1+Sheet2!$E$1). Cell C3 held the same formula with a 3. So did the cells "
            "down to C13, except C8, which someone had overwritten with a typed number months ago.",
            "The new analyst needed half an hour to work out what Sheet2!$E$1 was. It turned out to be the "
            "growth target: 5 percent. Nobody had noticed that July’s target no longer followed it.",
            "(The office and the figures are invented for this lesson. The Google Sheets features are real.)",
            "Part 45 kept inputs in their own cells. This part makes formulas that use those inputs easier to "
            "read and harder to break. After this post, you will know how to name a range or a single cell, how "
            "to use those names in formulas, how ARRAYFORMULA fills a whole column from one formula, how to "
            "keep blank rows blank, and when plain cell references are still the better choice.",
            ("photo", "blog/data-named-ranges.jpg", "Readable formulas: give key ranges and input cells plain "
             "names, and let one ARRAYFORMULA fill a whole column instead of twelve copies. (Illustration: Butch "
             "Mahinay, aumahinay.dev)", "medium"),
            ("h", "The Practice Sheet"),
            "Set up a small sheet of monthly business tax collections, in thousands of pesos.",
            ("point", "Column A", "A1: Month. A2 to A13: Jan to Dec."),
            ("point", "Column B, last year", "B1: Last year. Then 9800, 4100, 3600, 5200, 3900, 3400, 4600, "
             "3800, 3500, 4400, 3700, 4000. The total is 54,000."),
            ("point", "The growth target", "E1: 5%. D1: Growth target, as a label."),
            ("point", "Column F, this year so far", "F1: Actual. F2 to F7: 10100, 4300, 3500, 5600, 4000, "
             "3600. Leave F8 to F13 blank, since July to December have not happened yet."),
            "These are the same twelve monthly figures used in Part 44, written in thousands.",
            ("h", "Step 1: Name a Range"),
            "Google’s help explains the steps: select the cells, open Data, then Named ranges, type a name, and "
            "confirm.",
            ("point", "Name B2:B13", "Call it LastYear."),
            ("point", "Name E1", "Call it Growth. A single cell can have a name too."),
            ("point", "Name F2:F13", "Call it Actual."),
            "The help page lists the rules. Names “can contain only letters, numbers, and underscores,” “can’t "
            "start with a number, or the words ‘true’ or ‘false,’” and “can’t contain any spaces or "
            "punctuation.” So LastYear and Last_Year work, but Last Year does not.",
            ("h", "Step 2: Use the Names in Formulas"),
            ("point", "Total last year", "=SUM(LastYear) returns 54,000."),
            ("point", "Target for the year", "=SUM(LastYear)*(1+Growth) returns 56,700."),
            ("point", "Actual so far", "=SUM(Actual) returns 31,100."),
            "Read those formulas aloud. A supervisor who has never opened the sheet can tell what they do. "
            "Compare =SUM(Sheet2!$B$2:$B$13)*(1+Sheet2!$E$1), which means the same thing.",
            ("point", "Names are fixed references", "A name always points to the same cells, so there is no need "
             "for dollar signs."),
            ("point", "Names work across tabs", "A formula on a Summary tab can use LastYear without naming the "
             "tab it lives on."),
            ("h", "Step 3: One Formula for a Whole Column"),
            "The old sheet had twelve copies of the target formula, and one had been overwritten. ARRAYFORMULA "
            "replaces all twelve. Google’s help describes it as enabling “the display of values returned from "
            "an array formula into multiple rows and/or columns.”",
            ("point", "Target column", "C1: Target. In C2, type =ARRAYFORMULA(LastYear*(1+Growth)). Sheets fills "
             "C2 to C13 with 10,290, 4,305, 3,780 and so on, down to 4,200 for December."),
            ("point", "Only C2 holds a formula", "C3 to C13 show results, but they are part of C2’s output. "
             "Type something in C8 and the formula shows an error instead of quietly accepting the change."),
            ("point", "Check the total", "=SUM(C2:C13) returns 56,700, the same as Step 2."),
            "That is the protection the old sheet lacked. A stray number cannot sit unnoticed in the middle of "
            "a column that one formula controls.",
            ("photo", "blog/data-named-ranges-sheet.jpg", "One formula in C2 fills the target column, and one in "
             "G2 fills the gaps while leaving future months blank. Figures are invented. (Illustration: Butch "
             "Mahinay, aumahinay.dev)", "medium"),
            ("h", "Step 4: Keep Blank Rows Blank"),
            "A gap column should show actual minus target, but only for months that have actual figures.",
            ("point", "Without care", "=ARRAYFORMULA(Actual-C2:C13) shows minus 4,830 for July, because a blank "
             "actual counts as zero. That looks like a disaster that has not happened."),
            ("point", "With IF", "In G2, type =ARRAYFORMULA(IF(Actual=\"\", \"\", Actual-C2:C13)). Now July to "
             "December stay blank."),
            ("point", "Read the result", "January minus 190, February minus 5, March minus 280, April plus 140, "
             "May minus 95, June plus 30."),
            "The six gaps add up to minus 400, the same as 31,100 actual against 31,500 targeted for January to "
            "June. Part 40 used IF to sort records. Here it decides whether there is anything to show.",
            ("h", "Step 5: Add the Header in the Same Formula"),
            "Some analysts put the header inside the formula, so a whole column is controlled from row 1.",
            ("point", "Formula in G1", "={\"Gap\"; ARRAYFORMULA(IF(Actual=\"\", \"\", Actual-C2:C13))}"),
            ("point", "What the braces do", "They stack the word Gap on top of the twelve results. The "
             "semicolon means “next row.”"),
            "This is optional. It helps when rows are added above the data, but it can confuse a beginner. Use "
            "it only if everyone who maintains the sheet understands it.",
            ("h", "When Plain References Are Better"),
            ("point", "A one-time calculation", "A quick check in a scratch tab does not need names."),
            ("point", "Too many names", "Fifty names are as hard to follow as fifty cell addresses. Name the "
             "inputs and the main ranges, not every cell."),
            ("point", "Ranges that will grow", "A name fixed at B2:B13 will not include a new row 14. For a list "
             "that grows, name the whole column, such as B2:B, and check that blank rows do not break the "
             "formulas."),
            ("point", "Shared sheets", "Deleting a named range breaks every formula that uses it. The help page "
             "warns that formulas referencing a deleted name “will no longer work.”"),
            ("h", "Back to the Targets Sheet"),
            "The new analyst named the three ranges, replaced the twelve target formulas with one ARRAYFORMULA, "
            "and found the typed number in July at once: the formula refused to spill over it. The corrected "
            "July target was 4,830.",
            "She added a note at the top of the sheet listing the names and what each held. When the growth "
            "target changed to 6 percent in the next budget cycle, one cell changed, and every target followed.",
            ("h", "Leaving a Map for the Next Person"),
            "The targets sheet became hard to maintain because its builder left without notes. Names help, but "
            "a short guide helps more.",
            ("point", "List the names", "On a Notes tab, write each name, the cells it covers and what it holds. "
             "The Data, then Named ranges panel shows the current list to copy from."),
            ("point", "Say which cells to edit", "Usually only the inputs, such as Growth and the monthly "
             "actuals."),
            ("point", "Say which cells not to touch", "The first cell of each ARRAYFORMULA column."),
            "Part 15 suggested saving a dated copy before big changes. Do that before renaming or deleting any "
            "named range.",
            ("h", "Mistakes to Avoid"),
            ("point", "Names with spaces", "Use LastYear or Last_Year."),
            ("point", "Typing over spilled results", "Edit the formula in the first cell, not the cells below it."),
            ("point", "Gaps against blank months", "Wrap the calculation in IF so empty rows stay empty."),
            ("point", "Deleting a name without checking", "Search for it first. Every formula that uses it will "
             "break."),
            ("h", "Key Takeaways"),
            ("point", "Named ranges", "Data, then Named ranges. Plain names make formulas readable."),
            ("point", "Name the inputs", "A single cell like Growth is the best first name to create."),
            ("point", "ARRAYFORMULA", "One formula fills a column and refuses stray typed numbers."),
            ("point", "IF keeps blanks blank", "Show results only where there is data."),
            ("h", "Your Part 46 Exercise"),
            ("point", "Step 1", "Build the practice sheet and name LastYear, Growth and Actual."),
            ("point", "Step 2", "Check that =SUM(LastYear)*(1+Growth) returns 56,700."),
            ("point", "Step 3", "Fill the target column with one ARRAYFORMULA, then type 5000 in C9 and see "
             "what happens."),
            ("point", "Step 4", "Build the gap column with IF, and confirm the six gaps add up to minus 400."),
            ("cta", "Read: Data Analytics Series, Part 45: What If? Low, Likely and High Scenarios in Google Sheets", "/blog/data-analytics-part-45-what-if-scenarios/"),
            ("cta", "Read: Data Analytics Series, Part 40: IF, IFS and SWITCH, Letting the Sheet Sort Records Into Groups", "/blog/data-analytics-part-40-if-ifs-switch/"),
            ("cta", "Read: Data Analytics Series, Part 33: FILTER, SORT and UNIQUE, Lists in Google Sheets That Update Themselves", "/blog/data-analytics-part-33-filter-sort-unique/"),
            ("cta", "Read: Data Analytics Series, Part 12: Spreadsheets Done Right, One Row per Record", "/blog/data-analytics-part-12-one-row-per-record/"),
            ("ask", "Which formula in your office’s sheets would be easier to check with a plain name?"),
        ],
    },
    {
        "title": "Data Analytics Series, Part 45: What If? Low, Likely and High Scenarios in Google Sheets",
        "slug": "data-analytics-part-45-what-if-scenarios",
        "category": "data",
        "date": "June 10, 2027",
        "summary": "A single estimate hides how uncertain it is. This part builds a small what-if model in Google "
                   "Sheets: inputs kept apart from formulas, low, likely and high scenarios, a dropdown to switch "
                   "between them, and a one-at-a-time test that shows which input matters most.",
        "publish_on": "2027-06-10 21:00",
        "body": [
            "The draft estimate said business tax next year would bring in ₱15.7 million. A council member "
            "asked what would happen if the collection rate dropped the way it had two years before. Nobody "
            "could answer without rebuilding the whole computation.",
            "The estimate had been typed as one long formula with the numbers inside it. To test a different "
            "collection rate, someone would have to find the right number in the formula, change it, and hope "
            "nothing else broke.",
            "(The office, the inputs and the amounts are invented for this lesson. The Google Sheets features "
            "are real.)",
            "Part 44 drew a chart in Python. This part returns to Google Sheets to answer a question that "
            "comes up in many budget meetings: what if? By the end, you will know how to separate inputs from "
            "formulas, build low, likely and high scenarios, switch between them with a dropdown, find the "
            "input that moves the answer most, and report a range instead of a single number.",
            ("photo", "blog/data-scenarios.jpg", "A what-if model: inputs in their own cells, one formula that "
             "uses them, and three scenarios, so a question in a meeting can be answered in seconds. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Step 1: Keep the Inputs Apart"),
            "An input is any number you might want to change. Give each one its own labeled cell.",
            ("point", "A2: Businesses paying next year", "B2: 1230"),
            ("point", "A3: Average tax due per business", "B3: 14500"),
            ("point", "A4: Collection rate", "B4: 88%"),
            ("point", "A6: Estimated collections", "B6: =B2*B3*B4 returns 15,694,800."),
            "Now anyone can change B4 to 82% and watch B6 update. The formula stays the same, and the "
            "assumptions are visible to every reader.",
            ("point", "Color the inputs", "Give input cells a light fill, such as pale yellow, so readers know "
             "which cells they may change."),
            ("point", "Label the units", "Write “per business” and “percent of tax due” beside the inputs."),
            ("h", "Step 2: Write Down Three Scenarios"),
            "A scenario is a set of inputs that could happen together. Build a small table to the right.",
            ("point", "Headers", "Leave D1 blank, and type Low, Likely and High in E1, F1 and G1. Put the input "
             "names in D2 to D4."),
            ("point", "Businesses, E2 to G2", "1180, 1230 and 1260."),
            ("point", "Average tax due, E3 to G3", "13800, 14500 and 15000."),
            ("point", "Collection rate, E4 to G4", "82%, 88% and 92%."),
            "Base each value on something you can explain: last year’s count and new registrations, recent "
            "growth in average tax, and the best and worst collection rates of the past five years. Part 31 "
            "of Inside the Local Treasury explained why income estimates should be realistic.",
            ("h", "Step 3: Switch With a Dropdown"),
            ("point", "A label", "In A1, type Scenario."),
            ("point", "Make the dropdown", "In B1, choose Data, then Data validation, add a rule, and set the "
             "criteria to Dropdown with the options Low, Likely and High."),
            ("point", "Pull the matching input", "In B2, type =INDEX(E2:G2, MATCH($B$1, $E$1:$G$1, 0)) and fill "
             "down to B4."),
            ("point", "What it does", "MATCH finds which column holds the chosen scenario, and INDEX takes the "
             "value from that column."),
            "Now B6 shows the estimate for whichever scenario is chosen in B1.",
            ("point", "Low", "₱13,352,880."),
            ("point", "Likely", "₱15,694,800."),
            ("point", "High", "₱17,388,000."),
            ("photo", "blog/data-scenarios-swing.jpg", "Changing one input at a time from low to high, with the "
             "others kept at likely. The collection rate moves the estimate most. Figures are invented. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Step 4: Which Input Matters Most?"),
            "Scenarios change everything at once. To see which input drives the result, change one at a time "
            "and keep the others at likely.",
            ("point", "Businesses, low to high", "₱15,056,800 to ₱16,077,600, a swing of about ₱1.0 million."),
            ("point", "Average tax due, low to high", "₱14,937,120 to ₱16,236,000, a swing of about ₱1.3 "
             "million."),
            ("point", "Collection rate, low to high", "₱14,624,700 to ₱16,408,200, a swing of about ₱1.8 "
             "million."),
            "The collection rate matters most in this example. That points the office’s effort at follow-up "
            "on unpaid accounts, which Part 30 of Inside the Local Treasury covered, rather than at counting "
            "new businesses more precisely.",
            "To build this table quickly, copy the model to a second tab, change one input in each row, and "
            "record the result. Part 38 measured spread within a set of numbers. This measures how far the "
            "answer can move when an assumption changes.",
            ("h", "Step 5: Report a Range"),
            ("point", "Lead with the likely figure", "“About ₱15.7 million is likely.”"),
            ("point", "Give the range", "“It could be as low as ₱13.4 million or as high as ₱17.4 million.”"),
            ("point", "Name the key assumption", "“The collection rate makes the biggest difference.”"),
            ("point", "Say what would change your mind", "“If first-quarter collections run below 80 percent of "
             "the quarterly target, we will revise toward the low case.”"),
            ("h", "Keeping the Model Honest"),
            ("point", "One formula, many inputs", "Never type a number inside a formula that someone may need to "
             "change."),
            ("point", "Explain each scenario value", "Add a note beside each with its source, such as the year "
             "the rate was observed."),
            ("point", "Keep low and high realistic", "Scenarios far beyond anything seen before make the range "
             "useless."),
            ("point", "Version the file", "Save a dated copy when the estimate is submitted, as Part 15 "
             "suggested."),
            ("h", "Back to the Council Member’s Question"),
            "The next time the question came up, the analyst changed the dropdown to Low while the council "
            "watched. The estimate dropped to ₱13.4 million, and the one-at-a-time table showed that most of "
            "the drop came from the collection rate.",
            "The council kept the likely estimate in the budget, but asked for a quarterly check against the "
            "collection rate and a plan for what to defer if collections ran toward the low case.",
            ("h", "Scenarios for Spending Too"),
            "The same layout works on the spending side.",
            ("point", "Fuel and repairs", "Inputs for liters per month, price per liter and the number of "
             "vehicles in use."),
            ("point", "Overtime during the January rush", "Inputs for staff, hours per person and the hourly "
             "rate."),
            ("point", "Printing of notices", "Inputs for the number of notices, pages each and the cost per "
             "page."),
            "Pair an income model with a spending model, and the low case for income can be checked against "
            "the high case for spending. That pairing is the one most worth discussing before the budget is "
            "final.",
            ("h", "Sharing the Model"),
            ("point", "Protect the formulas", "In Google Sheets, use Data, then Protect sheets and ranges, so "
             "only the input cells can be edited by others."),
            ("point", "Add a short guide", "A note at the top: which cells to change, what each scenario "
             "assumes, and the date the values were last updated."),
            ("point", "Keep a log of changes", "A small table of who changed which input and why, so the "
             "estimate can be traced later."),
            ("h", "Mistakes to Avoid"),
            ("point", "Numbers buried in formulas", "Put every assumption in its own cell."),
            ("point", "One estimate with no range", "Readers assume it is certain."),
            ("point", "Changing everything at once", "Test inputs one at a time to find what matters."),
            ("point", "Unexplained scenario values", "Each low and high should have a reason."),
            ("h", "Key Takeaways"),
            ("point", "Inputs apart from formulas", "Labeled, colored and easy to change."),
            ("point", "Three scenarios", "Low, likely and high, chosen with a dropdown."),
            ("point", "One at a time", "Shows which input moves the answer most."),
            ("point", "Report a range", "Likely figure, low and high, and the key assumption."),
            ("h", "Your Part 45 Exercise"),
            ("point", "Step 1", "Build the input cells and the formula, and check that B6 returns 15,694,800."),
            ("point", "Step 2", "Add the scenario table and the dropdown, and switch between Low, Likely and "
             "High."),
            ("point", "Step 3", "Build the one-at-a-time table and confirm the collection rate has the largest "
             "swing."),
            ("point", "Step 4", "Replace the inputs with your own office’s figures for one revenue source."),
            ("cta", "Read: Inside the Local Treasury, Part 31: Estimating Next Year’s Income, the Numbers Behind the Budget", "/blog/estimating-next-years-income/"),
            ("cta", "Read: Data Analytics Series, Part 25: XLOOKUP, Bringing the Right Detail Into Every Row", "/blog/data-analytics-part-25-xlookup/"),
            ("cta", "Read: Data Analytics Series, Part 43: Drawing a Line Through the Points, Simple Regression in Google Sheets", "/blog/data-analytics-part-43-simple-regression/"),
            ("cta", "Read: Inside the Local Treasury, Part 30: Unpaid Business Taxes, Distraint, Levy and What Cannot Be Seized", "/blog/unpaid-business-taxes-distraint-and-levy/"),
            ("ask", "Which estimate in your office would be more useful as a range than as one number?"),
        ],
    },
    {
        "title": "Data Analytics Series, Part 44: Your First Chart in Python, Monthly Collections With Matplotlib",
        "slug": "data-analytics-part-44-first-chart-in-python",
        "category": "data",
        "date": "June 7, 2027",
        "summary": "A chart made by code can be rebuilt in seconds when the numbers change. This part walks "
                   "through a short Python script that uses the Matplotlib library to draw monthly collections "
                   "as a bar chart, label it clearly and save it as a picture, line by line, for readers who "
                   "have never drawn a chart in code.",
        "publish_on": "2027-06-07 21:00",
        "body": [
            "Every month, the clerk rebuilt the same collections chart for the report. She copied the new "
            "figures, fixed the colors that had reset themselves, retyped the title, and adjusted the labels "
            "that had shifted. It took most of an hour, and it never looked quite the same twice.",
            "Her officemate, who had finished the site’s Python lessons, offered to try something else: a short "
            "script that draws the chart the same way every time. The first version was sixteen lines long.",
            "(The office and the collections are invented for this lesson. The Python code is real, and the "
            "chart shown in this post is its actual output.)",
            "Part 43 fitted a line through points in Google Sheets. This part steps into Python for the first "
            "time in this series. By the end, you will know what Matplotlib is, how to install it, what each "
            "line of a short chart script does, how to save the chart as a picture, and when a script is worth "
            "the trouble.",
            ("photo", "blog/data-matplotlib.jpg", "A chart from code: list the numbers, draw the bars, label "
             "them, and save the picture, so next month’s chart is one run away. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "What You Need"),
            "Matplotlib’s own website describes it as “a comprehensive library for creating static, animated, "
            "and interactive visualizations in Python.” It is free and open source.",
            ("point", "Python", "Lesson 0 of the site’s Python for Treasury Work tutorials walks through "
             "installing it."),
            ("point", "Matplotlib", "In a terminal, type py -m pip install matplotlib on Windows, or python3 -m "
             "pip install matplotlib on a Mac or Linux computer."),
            ("point", "A text editor", "Any plain-text editor works. Save the file as collections_chart.py."),
            "Part 5 listed Python among the free tools for analysts. This is a first, small use of it.",
            ("h", "The Whole Script"),
            "Here is the script in full. The sections below explain it line by line.",
            ("point", "Lines 1 to 2", "import matplotlib.pyplot as plt, then a blank line."),
            ("point", "Lines 3 to 4", "months = [\"Jan\", \"Feb\", \"Mar\", \"Apr\", \"May\", \"Jun\", "
             "\"Jul\", \"Aug\", \"Sep\", \"Oct\", \"Nov\", \"Dec\"]"),
            ("point", "Lines 5 to 6", "collections = [9.8, 4.1, 3.6, 5.2, 3.9, 3.4, 4.6, 3.8, 3.5, 4.4, 3.7, "
             "4.0]"),
            ("point", "Line 8", "fig, ax = plt.subplots(figsize=(8, 4.5))"),
            ("point", "Line 9", "ax.bar(months, collections, color=\"#1d58b8\")"),
            ("point", "Line 10", "ax.set_title(\"January brings in the most: collections by month, 2026\")"),
            ("point", "Line 11", "ax.set_ylabel(\"Collections (₱ millions)\")"),
            ("point", "Line 12", "ax.spines[[\"top\", \"right\"]].set_visible(False)"),
            ("point", "Lines 13 to 14", "for i, value in enumerate(collections): then, indented, "
             "ax.text(i, value + 0.1, f\"{value:.1f}\", ha=\"center\")"),
            ("point", "Lines 15 to 16", "fig.tight_layout() then fig.savefig(\"collections.png\", dpi=150)"),
            "Run it with py collections_chart.py on Windows, or python3 collections_chart.py elsewhere. A file "
            "named collections.png appears in the same folder.",
            ("h", "Line by Line"),
            ("point", "import matplotlib.pyplot as plt", "Loads the charting part of Matplotlib and gives it "
             "the short name plt, a common habit."),
            ("point", "The two lists", "months holds the labels and collections holds the amounts, in millions "
             "of pesos. The two lists must be the same length, in the same order."),
            ("point", "plt.subplots", "Creates a blank figure, the whole picture, and an axes, the area where "
             "the bars go. figsize sets the size in inches: 8 wide and 4.5 tall."),
            ("point", "ax.bar", "Draws one bar per month. The color is a hex code, like the ones used for web "
             "pages."),
            ("point", "set_title and set_ylabel", "Add the title and the label on the vertical axis. Part 27 "
             "recommended titles that state the finding, not only the topic."),
            ("point", "spines", "The four border lines around the chart. Hiding the top and right ones makes "
             "the chart lighter."),
            ("point", "The for loop", "Goes through each amount and writes it just above its bar. enumerate "
             "gives both the position, i, and the value. The f\"{value:.1f}\" part shows one decimal place."),
            ("point", "tight_layout and savefig", "Fit everything inside the picture and save it as a PNG file. "
             "dpi=150 sets the sharpness."),
            ("photo", "blog/data-matplotlib-output.jpg", "The actual output of the script: twelve bars, a title "
             "that states the finding, a labeled axis and the value above each bar. Figures are invented. "
             "(Chart: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Reading the Result"),
            "January stands far above the rest at ₱9.8 million, while most other months sit between ₱3.4 and "
            "₱5.2 million. The twelve months add up to ₱54.0 million. The smaller bumps in April, July and "
            "October fall at the start of each quarter, when quarterly payments may come due.",
            "The chart did not discover anything new. Its value is that next month, the clerk changes twelve "
            "numbers and runs the script again, and the chart looks exactly as it did before.",
            ("h", "When Something Goes Wrong"),
            ("point", "ModuleNotFoundError: No module named 'matplotlib'", "The install step did not run for "
             "this Python. Run the pip command again in the same terminal you use to run the script."),
            ("point", "shape mismatch", "The two lists have different lengths. Count the items in each."),
            ("point", "SyntaxError", "A missing quote, comma or bracket. Python points to the line where it "
             "got confused, which is often just after the real mistake."),
            ("point", "The peso sign shows as a box", "The font in use lacks that character. Write PHP instead, "
             "or choose a font that has it."),
            ("h", "Small Changes to Try"),
            ("point", "A line instead of bars", "Change ax.bar to ax.plot and add marker=\"o\" inside the parentheses."),
            ("point", "Highlight one month", "Give the bars a list of colors, with gold for January and blue for "
             "the rest."),
            ("point", "A wider picture", "Change figsize to (10, 4.5) for a slide."),
            ("h", "Reading the Numbers From a File"),
            "Typing twelve numbers into the script each month works, but the figures already exist in a "
            "spreadsheet. A small change lets the script read them.",
            ("point", "Save a CSV file", "In Google Sheets, choose File, then Download, then Comma-separated "
             "values. Keep two columns: Month and Collections."),
            ("point", "Read it with Python’s csv module", "It comes with Python, so nothing else needs "
             "installing. Lesson 1 of the site’s tutorials used it to add up a day’s collections."),
            ("point", "Fill the two lists from the rows", "Then the rest of the script stays exactly the same."),
            "That way, the numbers live in one place, and the chart always matches the report.",
            ("h", "When a Script Is Worth It"),
            ("point", "Worth it", "The same chart every week or month, several charts from one data set, or a "
             "chart that must look identical across reports."),
            ("point", "Not worth it", "A one-time chart for a single meeting. Google Sheets is faster for that, "
             "as Part 27 showed."),
            ("point", "Keep the numbers private", "A script runs on your own computer. If you use an online "
             "notebook, remove names and personal details first, as Part 6 advised."),
            ("h", "Back to the Monthly Report"),
            "The clerk kept the script in the report folder with a short note on how to run it. The next month, "
            "the chart took two minutes. The month after, she added a second script that drew the same chart "
            "for each of the three largest revenue sources.",
            ("h", "Mistakes to Avoid"),
            ("point", "Lists of different lengths", "Every month needs one amount."),
            ("point", "A title that only names the topic", "Say what the chart shows."),
            ("point", "Typing the numbers twice", "Keep them in one place in the script, or read them from a "
             "file."),
            ("point", "Uploading personal data", "Charts need totals, not names."),
            ("h", "Key Takeaways"),
            ("point", "Matplotlib draws charts in Python", "Install it once with pip."),
            ("point", "Sixteen lines are enough", "Data, bars, title, labels, values and save."),
            ("point", "The payoff is repeat use", "Change the numbers and run the script again."),
            ("point", "Errors are readable", "The message usually names the problem and the line."),
            ("h", "Your Part 44 Exercise"),
            ("point", "Step 1", "Install Matplotlib and run the script as shown."),
            ("point", "Step 2", "Change the title to describe your own office’s pattern."),
            ("point", "Step 3", "Switch to a line chart with markers."),
            ("point", "Step 4", "Color January gold and the other months blue."),
            ("cta", "Read: Data Analytics Series, Part 27: Choosing the Right Chart, Starting From the Question", "/blog/data-analytics-part-27-choosing-the-right-chart/"),
            ("cta", "Read: Data Analytics Series, Part 5: The Analyst’s Toolkit on a Zero Budget", "/blog/data-analytics-part-5-zero-budget-toolkit/"),
            ("cta", "Read: Data Analytics Series, Part 43: Drawing a Line Through the Points, Simple Regression in Google Sheets", "/blog/data-analytics-part-43-simple-regression/"),
            ("cta", "Read: Data Analytics Series, Part 39: Histograms, Seeing the Shape of the Data", "/blog/data-analytics-part-39-histograms/"),
            ("ask", "Which chart do you rebuild by hand every month that a script could draw for you?"),
        ],
    },
    {
        "title": "Data Analytics Series, Part 43: Drawing a Line Through the Points, Simple Regression in Google Sheets",
        "slug": "data-analytics-part-43-simple-regression",
        "category": "data",
        "date": "June 4, 2027",
        "summary": "When one number tends to rise with another, a straight line can summarize how much. This part "
                   "uses SLOPE, INTERCEPT, RSQ and FORECAST in Google Sheets to fit a line, read what it means, "
                   "use it for a careful estimate, find the points that sit far from it, and avoid stretching it "
                   "too far.",
        "publish_on": "2027-06-04 21:00",
        "body": [
            "A new subdivision was opening, and the planning office expected about 100 businesses to register "
            "there within two years. The council wanted to know how much business tax that might bring.",
            "The analyst had ten barangays to learn from. Each had a number of registered businesses and a "
            "business tax total for the year. Plotted on a chart, the dots climbed from left to right in a "
            "rough line. The question was how steep that line was.",
            "(The barangays and the amounts are invented for this lesson. The Google Sheets functions are real.)",
            "Part 42 tested whether a gap between two groups was likely to be luck. This part looks at two "
            "numbers that move together and puts a line through them. By the end, you will know what simple "
            "regression is, how to compute the slope and intercept in Google Sheets, how to read R-squared, "
            "how to make a cautious estimate, and where the line should not be trusted.",
            ("photo", "blog/data-regression.jpg", "Simple regression: fit one straight line through the points, "
             "read its slope as the change in y for each extra unit of x, and check how closely the points "
             "follow it. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "The Practice Data"),
            "Type the businesses in column A and the business tax, in thousands of pesos, in column B, with "
            "headers in row 1.",
            ("point", "Rows 2 to 6", "40 and 520. 52 and 560. 60 and 760. 68 and 700. 75 and 980."),
            ("point", "Rows 7 to 11", "84 and 900. 90 and 1,180. 102 and 1,150. 115 and 1,420. 128 and 1,500."),
            "Type the amounts as plain numbers, without commas.",
            "Start with a picture. Select A1:B11, choose Insert, then Chart, and set the chart type to Scatter "
            "chart. The dots rise from left to right with some wobble. Part 35 used the same kind of chart to "
            "look at two numbers that move together.",
            ("h", "What Regression Does"),
            "Simple linear regression finds the one straight line that sits closest to all the dots, in the "
            "sense that the squared vertical gaps between the dots and the line add up to as little as "
            "possible. That line has two numbers.",
            ("point", "The slope", "How much y changes, on average, for each extra unit of x. Here: how much "
             "more business tax comes with each extra business."),
            ("point", "The intercept", "Where the line crosses the vertical axis, when x is zero."),
            ("h", "Step 1: The Slope"),
            "Google’s help describes SLOPE as calculating “the slope of the line resulting from linear "
            "regression of a dataset.”",
            ("point", "Formula", "=SLOPE(B2:B11, A2:A11)"),
            ("point", "Result", "About 11.88."),
            ("point", "In plain words", "Each extra registered business goes with about ₱11,880 more business "
             "tax a year, on average, across these barangays."),
            "Notice the order: y first, then x. Swapping them gives a different line.",
            ("h", "Step 2: The Intercept"),
            ("point", "Formula", "=INTERCEPT(B2:B11, A2:A11)"),
            ("point", "Result", "About 0.19, which is close to zero."),
            ("point", "In plain words", "A barangay with no businesses would collect almost no business tax. "
             "That makes sense here, but an intercept does not always mean something real, especially when no "
             "data sits near zero."),
            ("h", "Step 3: How Well the Line Fits"),
            "Google’s help describes RSQ as calculating “the square of r, the Pearson product-moment "
            "correlation coefficient of a dataset.”",
            ("point", "Formula", "=RSQ(B2:B11, A2:A11)"),
            ("point", "Result", "About 0.95."),
            ("point", "In plain words", "Differences in the number of businesses account for about 95 percent "
             "of the differences in business tax across these ten barangays. The other 5 percent comes from "
             "everything else."),
            "A value near 1 means the dots hug the line. A value near 0 means the line explains little.",
            ("photo", "blog/data-regression-fit.jpg", "Ten barangays, one fitted line, and the gap between each "
             "barangay and the line. The largest gaps point to barangays worth a closer look. Figures are "
             "invented. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Step 4: A Careful Estimate"),
            "Google’s help describes FORECAST as calculating “the expected y-value for a specified x based on "
            "a linear regression of a dataset.”",
            ("point", "Formula", "=FORECAST(100, B2:B11, A2:A11)"),
            ("point", "Result", "About 1,188, or roughly ₱1.19 million a year."),
            ("point", "Same as", "Intercept plus slope times 100. You can check it by hand."),
            "Report it as a range, not a single figure. The dots sit as much as about ₱110,000 above or below "
            "the line, so a fair statement is “roughly ₱1.1 to ₱1.3 million, once the businesses are "
            "registered and paying.”",
            ("h", "Step 5: Look at the Gaps"),
            "The line is also useful for what it does not explain. In column C, type =FORECAST(A2, $B$2:$B$11, "
            "$A$2:$A$11) and fill down. In column D, type =B2-C2 and fill down. Column D holds each "
            "barangay’s gap from the line, often called its residual.",
            ("point", "Biggest shortfall", "The barangay with 68 businesses collected about ₱108,000 less than the "
             "line suggests."),
            ("point", "Biggest surplus", "The barangay with 90 businesses collected about ₱111,000 more."),
            ("point", "What to do", "Ask why. Smaller businesses, unpaid accounts, a large taxpayer or a "
             "recording error could each explain a gap. Part 34 covered checking an unusual value before "
             "deciding what it means."),
            ("h", "Where the Line Should Not Go"),
            ("point", "Outside the data", "The barangays had 40 to 128 businesses. An estimate for 300 "
             "businesses would stretch the line far beyond anything it has seen."),
            ("point", "Not proof of cause", "Part 35 warned that two numbers moving together do not prove that "
             "one drives the other. Here the link is plausible, but the line alone does not show it."),
            ("point", "Not every pattern is straight", "Check the scatter chart first. If the dots curve, a "
             "straight line will mislead."),
            ("point", "Few points, shaky line", "Ten points give a rough line. Add more data when you can."),
            "A quick way to see the fit is to compare the largest residual with the typical amount. Here the "
            "biggest gap is about ₱111,000 against barangay totals of ₱520,000 to ₱1.5 million.",
            ("h", "Adding the Line to the Chart"),
            ("point", "Trendline", "In the Chart editor, open Customize, then Series, and tick Trendline."),
            ("point", "Show the numbers", "Set the label to use the equation, and tick the option to show "
             "R-squared, so readers see the slope and the fit."),
            "Business Intelligence Part 24 used trend lines across time. Here the line runs across a second "
            "measure instead.",
            ("h", "Back to the Subdivision"),
            "The analyst reported a range of roughly ₱1.1 to ₱1.3 million a year, stated that it assumed the "
            "new businesses would resemble those in existing barangays, and noted that some may take a year or "
            "more to start paying.",
            "She also attached the two barangays with the largest gaps. The council asked for a follow-up on the "
            "one that collected less than its businesses suggested, which turned out to have several accounts "
            "that had not renewed.",
            ("h", "Mistakes to Avoid"),
            ("point", "Skipping the scatter chart", "Look at the dots before fitting a line."),
            ("point", "Swapping x and y", "SLOPE and INTERCEPT take y first."),
            ("point", "Estimating far outside the data", "The line only knows the range it was built on."),
            ("point", "Reporting one exact figure", "Give a range, and state the assumptions."),
            ("h", "Key Takeaways"),
            ("point", "Slope", "The average change in y for each extra unit of x."),
            ("point", "RSQ", "How closely the points follow the line, from 0 to 1."),
            ("point", "FORECAST", "An estimate from the line, best given as a range."),
            ("point", "Residuals", "The gaps from the line point to cases worth checking."),
            ("h", "Your Part 43 Exercise"),
            ("point", "Step 1", "Enter the practice data and draw the scatter chart."),
            ("point", "Step 2", "Compute SLOPE, INTERCEPT and RSQ, and check them against the numbers above."),
            ("point", "Step 3", "Use FORECAST for 100 businesses, then add the residual columns and find the "
             "two largest gaps."),
            ("point", "Step 4", "Change the 700 in row 5 to 1,000 and see how the slope and RSQ change."),
            ("cta", "Read: Data Analytics Series, Part 35: Correlation Is Not Causation, When Two Numbers Move Together", "/blog/data-analytics-part-35-correlation-and-causation/"),
            ("cta", "Read: Data Analytics Series, Part 34: Outliers, Finding the Number That Doesn’t Fit", "/blog/data-analytics-part-34-outliers/"),
            ("cta", "Read: Data Analytics Series, Part 42: Is the Difference Real? Testing Two Groups With a Chi-Square Test", "/blog/data-analytics-part-42-chi-square-test/"),
            ("cta", "Read: Inside the Local Treasury, Part 31: Estimating Next Year’s Income, the Numbers Behind the Budget", "/blog/estimating-next-years-income/"),
            ("ask", "Which two numbers in your office would you put on a scatter chart first?"),
        ],
    },
    {
        "title": "Data Analytics Series, Part 42: Is the Difference Real? Testing Two Groups With a Chi-Square Test",
        "slug": "data-analytics-part-42-chi-square-test",
        "category": "data",
        "date": "June 1, 2027",
        "summary": "When one group does better than another, the gap may be real or may be luck. A chi-square test "
                   "in Google Sheets gives a number for how likely a gap that size would be by chance alone. This "
                   "part shows how to set up the counts, compute the expected values, run CHITEST, read the "
                   "result, and avoid the usual traps.",
        "publish_on": "2027-06-01 21:00",
        "body": [
            "The treasury tried something new with its delinquent business accounts. Half of the 300 owners "
            "received the usual letter. The other half received the same letter and a phone call two days later.",
            "Within 30 days, 78 of the 150 who got a call had paid, or 52 percent. Of the 150 who got only the "
            "letter, 54 had paid, or 36 percent. The collector was pleased. The budget officer asked whether "
            "16 points could simply be luck, since the calls took two staff members most of a week.",
            "(The office, the owners and the counts are invented for this lesson. The Google Sheets functions "
            "are real.)",
            "Part 41 adjusted pesos for inflation. This part answers a different question: when two groups "
            "differ, is the gap large enough to take seriously? By the end, you will know what a chi-square "
            "test checks, how to lay out the counts, how to compute expected values, how to run CHITEST in "
            "Google Sheets, how to read the result in plain words, and when not to trust it.",
            ("photo", "blog/data-chi-square.jpg", "A chi-square test: compare the counts you saw with the counts "
             "you would expect if both groups behaved the same, and ask how often a gap that size happens by "
             "chance. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Why a Gap Can Be Luck"),
            "Flip a fair coin 150 times and you will rarely get exactly 75 heads. Two groups of taxpayers work the same way: even if calls made no difference at all, the two payment rates would almost never match "
            "exactly. Some gap is normal. The question is whether this gap is bigger than chance would usually "
            "produce.",
            "Part 17 met the same idea as a margin of error around one sample. A chi-square test applies it to "
            "a comparison between groups.",
            ("h", "What the Test Asks"),
            "The test starts from a cautious assumption: the call made no difference, and both groups paid at "
            "the same rate. It then works out how many payers each group would have under that assumption and "
            "measures how far the real counts are from it.",
            ("point", "Observed counts", "What actually happened: paid and not paid, for each group."),
            ("point", "Expected counts", "What would happen if both groups paid at the same overall rate."),
            ("point", "The p-value", "The chance of seeing a gap at least this large if the call truly made no "
             "difference. A small p-value means luck is an unlikely explanation."),
            ("h", "Step 1: Lay Out the Observed Counts"),
            "Type a small table with the groups in rows and the outcomes in columns.",
            ("point", "Row 1 headers", "A1 is blank, B1 is Paid, C1 is Not paid, D1 is Total."),
            ("point", "Letter and call", "In row 2: 78 in B2 and 72 in C2. In D2: =B2+C2 returns 150."),
            ("point", "Letter only", "In row 3: 54 in B3 and 96 in C3. In D3: =B3+C3 returns 150."),
            ("point", "Totals", "In row 4: =B2+B3 returns 132 paid, =C2+C3 returns 168 not paid, and D4 "
             "returns 300."),
            "Use counts of people, not percentages. The test needs to know how many owners stand behind each "
            "rate.",
            ("h", "Step 2: Compute the Expected Counts"),
            "Overall, 132 of 300 owners paid, or 44 percent. If the call made no difference, each group of 150 "
            "would have about 44 percent payers.",
            ("point", "Formula", "Build a second table in F2:G3. In F2, type =$D2*B$4/$D$4 and fill it across "
             "to G2 and down to G3."),
            ("point", "Read it as", "Row total times column total, divided by the grand total."),
            ("point", "Results", "66 paid and 84 not paid in each group."),
            "So the call group had 12 more payers than expected, and the letter group had 12 fewer.",
            ("photo", "blog/data-chi-square-table.jpg", "Observed and expected counts side by side. The call group had 12 more payers than the no-difference assumption predicts. Figures are invented. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Step 3: Run CHITEST"),
            "Google’s help describes CHITEST as returning “the probability associated with a Pearson’s "
            "chi-squared test on the two ranges of data.” The newer name CHISQ.TEST works the same way.",
            ("point", "Formula", "=CHITEST(B2:C3, F2:G3)"),
            ("point", "Result", "About 0.005."),
            ("point", "In plain words", "If the call truly made no difference, a gap this large would turn up "
             "only about 5 times in 1,000 tries."),
            "Many analysts treat a p-value below 0.05 as strong enough to act on. That line is a habit, not a "
            "law of nature, so report the number itself, not only whether it passed.",
            ("h", "When the Groups Are Small"),
            "Suppose the office had tried the call on only 25 owners and compared them with 25 others. Thirteen "
            "of the call group paid, against 9 of the letter group, a gap of 16 points again.",
            ("point", "Same gap, smaller groups", "CHITEST on that table returns about 0.25."),
            ("point", "In plain words", "A gap that size would turn up about 1 time in 4 by chance. Not enough "
             "to decide."),
            "The percentages were the same. The number of people behind them was not. That is why the test "
            "needs counts.",
            ("h", "Reading the Result Honestly"),
            ("point", "A small p-value says the gap is probably not luck", "It does not say the gap is large or "
             "worth the cost. Sixteen points may or may not justify a week of calls."),
            ("point", "A large p-value is not proof of no effect", "It may only mean the groups were too small "
             "to tell."),
            ("point", "Size and cost still matter", "Report the rates, the gap, the p-value and the staff time "
             "together."),
            ("h", "Fair Groups Come First"),
            "The test checks luck. It cannot fix groups that were different from the start. If the collector "
            "called only the owners she knew were likely to pay, the call group would look better even if the "
            "calls did nothing.",
            ("point", "Assign by chance", "Before any calls, add a column with =RAND(), sort by it, and give the "
             "top half the call. Part 32 of the Project Management Series kept a comparison group for the same reason."),
            ("point", "Decide the measure first", "Write down “paid within 30 days” before the trial starts, so "
             "the measure cannot be chosen after the results are in."),
            ("point", "Same period", "Run both groups at the same time, so the season and deadlines affect "
             "them equally."),
            "Part 35 explained why two numbers moving together do not prove that one caused the other. "
            "Assigning groups by chance is one of the few ways to get closer to cause.",
            ("h", "Checks Before You Trust the Test"),
            ("point", "Expected counts of at least 5", "A common rule of thumb asks for an expected count of 5 "
             "or more in every cell. With smaller counts, the result becomes less reliable."),
            ("point", "Each person counted once", "An owner with three businesses should not count three times "
             "unless each business was assigned separately."),
            ("point", "Counts, not amounts", "The test compares how many paid, not how many pesos. For amounts, "
             "a different test is needed."),
            ("h", "Back to the Calls"),
            "The office reported all of it on one line: 52 percent paid after a call, 36 percent after a letter "
            "alone, p about 0.005, and about 60 staff hours for 150 calls.",
            "The 12 extra payers brought in more than the staff time cost, so the treasurer kept the calls for "
            "accounts above a set amount and kept letters alone for the rest.",
            ("h", "Mistakes to Avoid"),
            ("point", "Testing percentages", "Feed the test counts of people, not rates."),
            ("point", "Choosing who gets the treatment", "Assign by chance, or the groups differ from the start."),
            ("point", "Treating 0.05 as magic", "Report the p-value and the size of the gap."),
            ("point", "Reading a large p-value as no effect", "Small groups often cannot tell."),
            ("h", "Key Takeaways"),
            ("point", "A gap can be luck", "Some difference between groups is normal."),
            ("point", "Expected counts", "Row total times column total, divided by the grand total."),
            ("point", "CHITEST returns a p-value", "A small value means chance is an unlikely explanation."),
            ("point", "Fair groups matter most", "Assign by chance and fix the measure before you start."),
            ("h", "Your Part 42 Exercise"),
            ("point", "Step 1", "Enter the observed table and compute the totals."),
            ("point", "Step 2", "Build the expected table with =$D2*B$4/$D$4 and check that it gives 66 and "
             "84."),
            ("point", "Step 3", "Run =CHITEST(B2:C3, F2:G3) and confirm a result near 0.005."),
            ("point", "Step 4", "Change the table to 13 and 12 for the call group and 9 and 16 for the letter "
             "group. Run the test again and explain why the answer changed."),
            ("cta", "Read: Data Analytics Series, Part 35: Correlation Is Not Causation, When Two Numbers Move Together", "/blog/data-analytics-part-35-correlation-and-causation/"),
            ("cta", "Read: Data Analytics Series, Part 17: Samples and Margin of Error, Checking 400 Receipts Instead of 12,000", "/blog/data-analytics-part-17-samples-margin-of-error/"),
            ("cta", "Read: Project Management Series, Part 32: Running a Pilot, Testing Small Before Going Big", "/blog/project-management-part-32-running-a-pilot/"),
            ("cta", "Read: Data Analytics Series, Part 30: Percent Change or Percentage Points? Reporting Growth Without Confusion", "/blog/data-analytics-part-30-percent-change/"),
            ("ask", "Which change in your office was judged a success before anyone checked whether it was luck?"),
        ],
    },
    {
        "title": "Data Analytics Series, Part 41: Real or Nominal Pesos? Adjusting Collections for Inflation",
        "slug": "data-analytics-part-41-real-and-nominal-pesos",
        "category": "data",
        "date": "May 29, 2027",
        "summary": "A peso collected today buys less than a peso collected four years ago. Comparing amounts across "
                   "years without adjusting for prices can make a flat year look like growth. This part explains "
                   "the Consumer Price Index, how to turn nominal pesos into real pesos in Google Sheets, and how "
                   "to report both honestly.",
        "publish_on": "2027-05-29 21:00",
        "body": [
            "The slide said collections had grown 15 percent in four years, from ₱40.0 million to ₱46.0 million. "
            "The room applauded.",
            "The budget officer did not clap. Fuel, rice, office supplies and contractors had all become more "
            "expensive over the same four years. Her question was simple: “Can we buy 15 percent more with it?” "
            "Nobody had checked.",
            "(The collections and the index values below are invented for this lesson, so the arithmetic is easy "
            "to follow. For real work, use the official Consumer Price Index from the Philippine Statistics "
            "Authority.)",
            "Part 40 sorted records into groups with IF, IFS and SWITCH. This part deals with comparisons across "
            "years, where the peso itself changes value. After this post, you will know what the Consumer Price "
            "Index measures, the difference between nominal and real amounts, how to convert one to the other "
            "in Google Sheets, and how to report the result without confusing anyone.",
            ("photo", "blog/data-real-pesos.jpg", "Real or nominal pesos: divide by a price index to compare "
             "amounts from different years in the same purchasing power. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "What the Consumer Price Index Measures"),
            "The Philippine Statistics Authority describes the Consumer Price Index, or CPI, as an indicator of "
            "the change in the average retail prices of a fixed basket of goods and services. It defines the "
            "inflation rate as the annual or monthly rate of change of the CPI, in percent.",
            ("point", "A base year equals 100", "The current series uses 2018 as its base year, after the PSA "
             "rebased it from 2012."),
            ("point", "A higher index means higher prices", "An index of 120 means the basket costs about 20 "
             "percent more than in the base year."),
            ("point", "It is an average", "Your own costs may rise faster or slower than the basket."),
            ("h", "Nominal and Real"),
            ("point", "Nominal pesos", "The amounts as recorded on the receipts, in each year’s own pesos."),
            ("point", "Real pesos", "The same amounts restated in the prices of one chosen year, so they can be "
             "compared fairly."),
            "Real pesos answer the budget officer’s question: how much can this money buy, compared with before?",
            ("h", "The Practice Data"),
            "Type this into a new sheet, with headers in row 1: Year in column A, Collections in millions in B, "
            "and the example index in C.",
            ("point", "2022", "Collections 40.0, index 110"),
            ("point", "2023", "Collections 41.5, index 116"),
            ("point", "2024", "Collections 43.0, index 120"),
            ("point", "2025", "Collections 44.4, index 124"),
            ("point", "2026", "Collections 46.0, index 128"),
            "Again, these index values are invented for practice. They are not official figures.",
            ("h", "Converting to Real Pesos"),
            "To restate every year in 2022 pesos, multiply each amount by the 2022 index and divide by that "
            "year’s index.",
            ("point", "Formula", "In D2: =B2*$C$2/C2, then fill down to D6. The dollar signs keep the 2022 "
             "index fixed."),
            ("point", "2022", "40.0 × 110 ÷ 110 = 40.0"),
            ("point", "2024", "43.0 × 110 ÷ 120 = about 39.4"),
            ("point", "2026", "46.0 × 110 ÷ 128 = about 39.5"),
            "In nominal pesos, collections rose 15 percent. In 2022 pesos, they slipped about 1 percent. The "
            "office was collecting more pesos that bought slightly less.",
            ("photo", "blog/data-real-pesos-lines.jpg", "Nominal collections rise every year, while the same "
             "amounts in 2022 pesos stay nearly flat. Figures and index values are invented. (Illustration: "
             "Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Choosing the Base Year"),
            "Any year can be the base, as long as you say which one.",
            ("point", "Use the earliest year", "To ask whether buying power grew since then."),
            ("point", "Use the latest year", "To restate old amounts in today’s pesos, which readers find "
             "easier to picture. In E2: =B2*$C$6/C2."),
            ("point", "Label it", "Write “in 2022 pesos” or “in 2026 pesos” in the column header and the chart "
             "title."),
            "The growth rate in real terms is the same whichever year you choose as the base.",
            ("h", "Real Growth in One Formula"),
            ("point", "Nominal growth", "=B6/B2-1 returns 15.0 percent."),
            ("point", "Price growth", "=C6/C2-1 returns about 16.4 percent."),
            ("point", "Real growth", "=(B6/B2)/(C6/C2)-1 returns about −1.2 percent."),
            "Part 30 explained how to describe changes like these without mixing up percent and percentage "
            "points.",
            ("h", "Where to Find the Official Index"),
            ("point", "The PSA releases", "The Philippine Statistics Authority publishes the CPI and inflation "
             "rate each month, with technical notes explaining the method."),
            ("point", "Annual averages for yearly data", "When your data is by year, use the annual average "
             "index, not a single month."),
            ("point", "One series only", "Use indices from the same base year. Mixing a 2012-based figure with "
             "a 2018-based one gives wrong results."),
            ("point", "Record the source", "Note the release and the date you copied the numbers in a source "
             "note, as Part 9 described."),
            ("h", "The Same Idea for Fees"),
            "Real pesos also show what happens to a fee that has not changed in years.",
            ("point", "The example", "A certification fee of ₱100 was set in 2022, when the example index "
             "was 110. By 2026 the index is 128."),
            ("point", "Its buying power", "=100*110/128 returns about 86. The same ₱100 now buys what ₱86 "
             "bought in 2022."),
            ("point", "What it means", "The fee did not change, but its real value fell by about 14 percent, "
             "while the cost of paper, printing and staff time to issue the certification may have risen."),
            "This does not mean a fee should rise automatically. Fees are set by ordinance, within the limits "
            "of the law. It does give the sanggunian a clear number to look at when it reviews them.",
            ("h", "Charting Both Lines"),
            ("point", "One chart, two lines", "Select the Year, nominal and real columns and insert a line chart."),
            ("point", "Same axis", "Keep both lines on one vertical axis in pesos, so the gap between them is "
             "honest."),
            ("point", "A clear title", "“Collections rose in pesos but stayed flat in buying power,” not just "
             "“Collections, 2022 to 2026.” Part 27 recommended titles that state the finding."),
            ("h", "When to Adjust, and When Not To"),
            ("point", "Adjust", "Comparing collections, spending or fees across several years."),
            ("point", "Do not adjust", "Within a single year, or when checking amounts against receipts, "
             "ordinances or the budget, which are all in nominal pesos."),
            ("point", "Show both", "In a report, give the nominal figure first, because it matches the books, "
             "then the real figure for comparison."),
            ("h", "Back to the Slide"),
            "The next version of the slide showed two lines: nominal collections rising, and real collections "
            "nearly flat. The caption read: “Collections grew 15 percent in pesos, but prices grew about as "
            "fast. In buying power, collections were about the same as in 2022.”",
            "Nobody applauded. Instead, the council asked which revenue sources had kept up with prices and "
            "which had fallen behind, which was the more useful question for the next budget.",
            ("h", "Mistakes to Avoid"),
            ("point", "Comparing pesos across years without saying so", "Label every amount nominal or real."),
            ("point", "Hiding the nominal figure", "It is the one that matches the books."),
            ("point", "Mixing base years", "Use one CPI series throughout."),
            ("point", "Treating the CPI as your own costs", "It is an average basket, a reasonable guide, not "
             "an exact measure of your office’s prices."),
            ("h", "Key Takeaways"),
            ("point", "CPI tracks average prices", "Base year 2018 equals 100 in the current series."),
            ("point", "Real = nominal × base index ÷ year’s index", "One formula, filled down."),
            ("point", "Real growth can be negative", "Even when nominal growth looks healthy."),
            ("point", "Report both, labeled", "Nominal for the books, real for comparison."),
            ("h", "Your Part 41 Exercise"),
            ("point", "Step 1", "Enter the practice data and compute real collections in 2022 pesos."),
            ("point", "Step 2", "Compute them again in 2026 pesos and confirm the real growth is the same."),
            ("point", "Step 3", "Chart nominal and real collections as two lines."),
            ("point", "Step 4", "Find the official annual CPI for the same years and repeat with real figures."),
            ("cta", "Read: Data Analytics Series, Part 30: Percent Change or Percentage Points? Reporting Growth Without Confusion", "/blog/data-analytics-part-30-percent-change/"),
            ("cta", "Read: Data Analytics Series, Part 9: Where Data Comes From, First-, Second- and Third-Party", "/blog/data-analytics-part-9-where-data-comes-from/"),
            ("cta", "Read: Data Analytics Series, Part 8: Metrics and KPIs That Tell the Truth", "/blog/data-analytics-part-8-metrics-and-kpis/"),
            ("cta", "Read: Data Analytics Series, Part 40: IF, IFS and SWITCH, Letting the Sheet Sort Records Into Groups", "/blog/data-analytics-part-40-if-ifs-switch/"),
            ("ask", "Which of your office’s yearly figures would look different in real pesos?"),
        ],
    },
    {
        "title": "Data Analytics Series, Part 40: IF, IFS and SWITCH, Letting the Sheet Sort Records Into Groups",
        "slug": "data-analytics-part-40-if-ifs-switch",
        "category": "data",
        "date": "May 26, 2027",
        "summary": "Typing a category by hand into thousands of rows invites spelling errors and missed rows. IF, "
                   "IFS and SWITCH in Google Sheets assign the category from a rule instead. This part shows how "
                   "each one works, why the order of conditions matters, how to avoid the #N/A trap in IFS, and "
                   "when a lookup table is better.",
        "publish_on": "2027-05-26 21:00",
        "body": [
            "The pivot table showed five payment sizes instead of three. Besides “Large,” “Medium” and “Small,” "
            "there were “large” and “Meduim.” Two clerks had typed the size of each payment by hand into 3,000 "
            "rows, and a few rows had been skipped altogether, leaving them in no group at all.",
            "The rule itself was simple: ₱100,000 or more was large, ₱20,000 or more was medium, and everything "
            "else was small. A rule that simple belongs in a formula, not in someone’s typing.",
            "(The office, the payments and the categories are invented for this lesson. The Google Sheets "
            "functions are real.)",
            "Part 39 drew the shape of a set of numbers with a histogram. This part sorts each record into a "
            "named group, so it can be counted, filtered and charted. You will learn how IF makes a choice, how "
            "to nest it, how IFS reads more cleanly, how SWITCH maps codes to names, how to combine conditions, "
            "and when to use a lookup table instead.",
            ("photo", "blog/data-ifs.jpg", "IF, IFS and SWITCH: let a rule assign each row’s category, so the "
             "same amount always lands in the same group. (Illustration: Butch Mahinay, aumahinay.dev)",
             "medium"),
            ("h", "The Practice Data"),
            "Type these into a new sheet, with headers in row 1. Column A is the receipt number, B the amount, "
            "and C the fund code.",
            ("point", "Rows 2 to 5", "R-101, 2,500, GF. R-102, 18,000, GF. R-103, 145,000, SEF. R-104, 7,200, "
             "GF."),
            ("point", "Rows 6 to 9", "R-105, 52,000, TF. R-106, 310,000, GF. R-107, 950, SEF. R-108, 99,999, "
             "GF."),
            "Type the amounts as plain numbers, without the comma or peso sign, so the formulas can compare "
            "them. Part 18 covered cleaning amounts that arrive as text.",
            ("h", "IF: One Question, Two Answers"),
            "IF asks one yes-or-no question and returns one value for yes and another for no.",
            ("point", "Formula", "In D2: =IF(B2>=100000, \"Large\", \"Not large\")"),
            ("point", "Read it as", "If the amount is at least 100,000, write Large. Otherwise, write Not large."),
            "That handles two groups. The rule has three.",
            ("h", "Nested IF: A Question Inside a Question"),
            ("point", "Formula", "=IF(B2>=100000, \"Large\", IF(B2>=20000, \"Medium\", \"Small\"))"),
            ("point", "How it reads", "If the amount is at least 100,000, Large. If not, ask again: at least "
             "20,000? Then Medium. Otherwise, Small."),
            "Nested IF works, but each extra group adds another layer of parentheses, and a missing one breaks "
            "the whole formula.",
            ("h", "IFS: Several Questions in a Row"),
            "Google’s help says IFS evaluates multiple conditions and returns a value that corresponds to the "
            "first true condition.",
            ("point", "Formula", "=IFS(B2>=100000, \"Large\", B2>=20000, \"Medium\", TRUE, \"Small\")"),
            ("point", "The TRUE at the end", "The same help page warns that if all conditions are false, IFS "
             "returns #N/A. A final TRUE acts as “everything else,” so no row is left without a group."),
            ("point", "Results", "R-101 Small, R-102 Small, R-103 Large, R-104 Small, R-105 Medium, R-106 "
             "Large, R-107 Small, R-108 Medium."),
            ("photo", "blog/data-ifs-order.jpg", "Order matters: IFS stops at the first true condition, so the "
             "biggest threshold must be checked first. Figures are invented. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "Why the Order Matters"),
            "IFS stops at the first true condition. Try the conditions the other way around:",
            ("point", "Wrong order", "=IFS(B2>=20000, \"Medium\", B2>=100000, \"Large\", TRUE, \"Small\")"),
            ("point", "What goes wrong", "For ₱145,000, the first test, at least 20,000, is already true, so the "
             "formula returns Medium and never reaches Large. No row would ever be Large."),
            ("point", "The fix", "Check the largest threshold first, then work down."),
            ("point", "Test the edges", "Try 99,999, 100,000, 19,999 and 20,000. R-108, at 99,999, should be "
             "Medium. Change it to 100,000 and it should become Large."),
            ("h", "SWITCH: Turning Codes Into Names"),
            "Google’s help says SWITCH tests an expression against a list of cases and returns the value of the "
            "first matching case, with an optional default when nothing matches.",
            ("point", "Formula", "In E2: =SWITCH(C2, \"GF\", \"General Fund\", \"SEF\", \"Special Education "
             "Fund\", \"TF\", \"Trust Fund\", \"Check code\")"),
            ("point", "The default", "“Check code” appears for any code not on the list, such as a typing error, "
             "so it stands out instead of hiding."),
            "SWITCH suits exact matches, such as codes. IFS suits ranges, such as amounts.",
            ("h", "Combining Conditions With AND and OR"),
            ("point", "AND", "=IF(AND(C2=\"GF\", B2>=100000), \"Review\", \"\") flags large General Fund "
             "payments only."),
            ("point", "OR", "=IF(OR(C2=\"SEF\", C2=\"TF\"), \"Special\", \"General\") groups two codes "
             "together."),
            "Keep each formula readable. If it needs more than three conditions, consider a helper column or a "
            "lookup table.",
            ("h", "Check the Inputs First"),
            "A rule is only as good as the values it reads. An amount stored as text will not compare the way "
            "you expect.",
            ("point", "Test for numbers", "In a helper column: =ISNUMBER(B2). It returns TRUE for a real number "
             "and FALSE for text that only looks like one."),
            ("point", "Count the problems", "=COUNTIF(F2:F9, FALSE) shows how many rows need fixing before "
             "the categories can be trusted."),
            ("point", "Flag them in the formula", "=IF(ISNUMBER(B2), IFS(B2>=100000, \"Large\", B2>=20000, "
             "\"Medium\", TRUE, \"Small\"), \"Check amount\") puts a clear label on any row that is not a "
             "number."),
            "Part 31 showed how conditional formatting can color such rows so they stand out.",
            ("h", "Counting the Groups"),
            "Once every row has a category, summaries become one formula each.",
            ("point", "How many in each group", "=COUNTIF(D2:D9, \"Large\") returns 2. Medium also returns 2, "
             "and Small returns 4."),
            ("point", "How much in each group", "=SUMIF(D2:D9, \"Large\", B2:B9) returns 455,000."),
            "Because the categories come from a rule, the counts change by themselves when an amount is "
            "corrected.",
            ("h", "When a Lookup Table Is Better"),
            "If the thresholds change every year, or there are many groups, put the rule in a small table "
            "instead of inside every formula.",
            ("point", "Step 1", "In G2:H4, list the lower limits and names: 0 Small, 20000 Medium, 100000 Large."),
            ("point", "Step 2", "In D2: =XLOOKUP(B2, $G$2:$G$4, $H$2:$H$4, \"\", -1). The -1 tells XLOOKUP to "
             "take an exact match or the next smaller value."),
            ("point", "Why it helps", "When the limit for Large changes, edit one cell, and every row updates."),
            "Part 25 covered XLOOKUP in detail.",
            ("h", "Back to the Pivot Table"),
            "The clerks deleted the typed column and filled the IFS formula down all 3,000 rows. The pivot table "
            "dropped to three groups. A quick ISNUMBER check beside the amounts found two rows typed with a "
            "letter O instead of a zero. Those two had been given a size by hand before, and nobody had "
            "noticed that the amounts themselves were not numbers.",
            ("h", "Mistakes to Avoid"),
            ("point", "Typing categories by hand", "A rule in a formula is consistent on every row."),
            ("point", "Checking small thresholds first", "IFS and nested IF stop at the first true test."),
            ("point", "Forgetting the catch-all", "End IFS with TRUE, and give SWITCH a default."),
            ("point", "Hiding thresholds inside formulas", "Use a lookup table when the rule may change."),
            ("h", "Key Takeaways"),
            ("point", "IF", "One question, two answers."),
            ("point", "IFS", "Several questions, first true wins, TRUE at the end."),
            ("point", "SWITCH", "Exact codes to names, with a default for anything else."),
            ("point", "Lookup table", "Best when the rule changes or the groups are many."),
            ("h", "Your Part 40 Exercise"),
            ("point", "Step 1", "Enter the practice data and add the IFS formula. Check that R-103 and R-106 "
             "are Large."),
            ("point", "Step 2", "Reverse the order of the conditions and see what breaks."),
            ("point", "Step 3", "Add the SWITCH formula and type a wrong code, such as GG, to see the default."),
            ("point", "Step 4", "Build the lookup table version and change the Large limit to 150,000."),
            "With the categories now set by formula, the office added a COUNTIFS summary from Part 23 beside the "
            "data. It updated itself every morning, and the monthly report no longer needed an afternoon of checking spellings before it could be sent.",
            ("cta", "Read: Data Analytics Series, Part 39: Histograms, Seeing the Shape of the Data", "/blog/data-analytics-part-39-histograms/"),
            ("cta", "Read: Data Analytics Series, Part 25: XLOOKUP, Bringing the Right Detail Into Every Row", "/blog/data-analytics-part-25-xlookup/"),
            ("cta", "Read: Data Analytics Series, Part 23: SUMIFS, COUNTIFS and AVERAGEIFS", "/blog/data-analytics-part-23-sumifs-countifs-averageifs/"),
            ("cta", "Read: Data Analytics Series, Part 16: Dirty Data, the Usual Suspects and How to Spot Them", "/blog/data-analytics-part-16-dirty-data/"),
            ("ask", "Which column in your office’s sheets is still typed by hand when a rule could fill it?"),
        ],
    },
    {
        "title": "Data Analytics Series, Part 39: Histograms, Seeing the Shape of the Data",
        "slug": "data-analytics-part-39-histograms",
        "category": "data",
        "date": "May 21, 2027",
        "summary": "An average gives one number, and a histogram shows how all the numbers are spread out. "
                   "This part shows how to group values into bins with COUNTIFS, build a histogram chart in Google "
                   "Sheets, choose a bin width, and read the common shapes, including a long tail and two peaks.",
        "publish_on": "2027-05-21 21:00",
        "body": [
            "The monthly report said the average waiting time at the payment counter was 15.75 minutes. The "
            "target was 15. The head of office asked for a second cashier.",
            "The cashier on duty was puzzled. Most people she served were done in about ten minutes. A few "
            "waited far longer, and she remembered each of them, because they had come with transactions that "
            "needed several offices to sign. One chart settled it, and it was not a bar chart of the average.",
            "(The office, the taxpayers and the waiting times are invented for this lesson. The Google Sheets "
            "functions and chart settings are real.)",
            "Part 38 measured spread with the range and the standard deviation. Those are still single numbers. "
            "This part draws the whole set at once. By the end, you will know what a histogram is, how to build "
            "one in Google Sheets with a formula and with a chart, how to choose a bin width, how to read the "
            "common shapes, and what each shape suggests you do next.",
            ("photo", "blog/data-histogram.jpg", "A histogram: group the values into equal bins, count each bin, "
             "and draw the counts as touching bars to see the shape of the data. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "What a Histogram Is"),
            "Google’s help for Sheets says to use a histogram when you want to show the distribution of a data "
            "set across different buckets or ranges. In plain words, you split the number line into equal "
            "ranges, called bins or buckets, and count how many values fall into each one.",
            ("point", "Bars touch", "Each bar covers a range of numbers, and the ranges meet, so the bars sit "
             "side by side with no gaps."),
            ("point", "Height is a count", "A tall bar means many values landed in that range."),
            ("point", "Width is the bin", "Every bin has the same width, such as ten minutes."),
            "Part 27 matched each question to a chart and paired distribution with the histogram. This part "
            "shows how to build one.",
            ("h", "The Practice Data"),
            "Type these twenty waiting times, in minutes, into A2:A21, with the header “Minutes” in A1.",
            ("point", "Waiting times", "4, 6, 7, 8, 8, 9, 9, 10, 11, 12, 12, 13, 14, 16, 18, 21, 24, 29, 38, 46"),
            ("point", "Average", "=AVERAGE(A2:A21) returns 15.75."),
            ("point", "Median", "=MEDIAN(A2:A21) returns 12."),
            "The average is higher than the median. Part 26 explained that a few large values pull the average "
            "up while the median stays in the middle. A histogram shows where those large values sit.",
            ("h", "Method 1: Count the Bins With a Formula"),
            "A formula table lets you see the exact counts, which a chart alone does not show.",
            ("point", "Step 1: List the bin starts", "In C2 to C6, type 0, 10, 20, 30 and 40. Each bin covers ten "
             "minutes."),
            ("point", "Step 2: Label each bin", "In D2, type =C2&\"–\"&(C2+9) and fill down, so the labels read "
             "0–9, 10–19 and so on."),
            ("point", "Step 3: Count", "In E2, type =COUNTIFS($A$2:$A$21, \">=\"&C2, $A$2:$A$21, \"<\"&C2+10) and "
             "fill down. Part 23 covered COUNTIFS."),
            ("point", "Step 4: Check the total", "=SUM(E2:E6) should return 20, the number of values. If it does "
             "not, a value is outside the bins."),
            "The counts: 7 people waited 0 to 9 minutes, 8 waited 10 to 19, 3 waited 20 to 29, 1 waited 30 to "
            "39, and 1 waited 40 to 49. Fifteen of the twenty waited less than 20 minutes.",
            ("photo", "blog/data-histogram-bins.jpg", "The twenty waiting times in five ten-minute bins. Most "
             "people waited under 20 minutes, and a thin tail stretches to the right. Figures are invented. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Method 2: The Histogram Chart"),
            ("point", "Step 1", "Select A1:A21."),
            ("point", "Step 2", "Choose Insert, then Chart. In the Chart editor, set the chart type to "
             "Histogram chart."),
            ("point", "Step 3", "On the Customize tab, open Histogram. Google’s help lists options to show item "
             "dividers and to change the bucket size or the outlier percentile."),
            ("point", "Step 4", "Set the bucket size to 10, to match the formula table."),
            ("point", "Step 5", "Give the chart a title that states the finding, such as “Most waits are under "
             "20 minutes; a few run past 30.”"),
            "The chart is quick. The formula table is easier to check and to copy into a report. Keeping "
            "both is useful.",
            ("h", "Choosing the Bin Width"),
            "The bin width changes what you see, so try more than one.",
            ("point", "Too wide", "With bins of 25 minutes, 17 of the 20 land in the first bar and the "
             "tail shrinks into a single short bar."),
            ("point", "Too narrow", "With bins of 1 minute, most bars hold zero or one person, and the shape "
             "turns into noise."),
            ("point", "A useful middle", "Pick a width that matches how people think about the measure, such "
             "as five or ten minutes, or ₱1,000 for payments."),
            ("point", "Keep it fixed when comparing", "Two histograms with different bin widths cannot be "
             "compared bar by bar."),
            ("h", "Reading the Shape"),
            ("point", "A single hump in the middle", "Values cluster around the center and thin out evenly on "
             "both sides. The average and the median are close."),
            ("point", "A long tail to the right", "Most values are small, and a few are large. The average sits "
             "above the median. Waiting times, payment amounts and days late can look like this."),
            ("point", "Two humps", "Two groups are mixed together. Split the data by a likely cause, such as "
             "type of transaction or time of day, and draw each group on its own."),
            ("point", "A sudden wall", "Values pile up at one edge, such as a deadline or a system limit. Ask "
             "what stops values from going past it."),
            ("point", "A lonely bar far away", "A value well apart from the rest. Part 34 explained how to check "
             "whether it is an error or a real case."),
            ("h", "Back to the Counter"),
            "The histogram showed a large group of short waits and a thin tail. The cashier pulled the two "
            "longest cases from the log. Both were business retirements that needed signatures from three "
            "offices before payment could be taken.",
            "A second cashier would not have shortened those two waits by much, because the time was spent "
            "waiting for signatures, not in the payment line. The office instead set up a separate desk for "
            "transactions that need other offices, with a clerk who walks the papers through. Part 14 of Inside "
            "the Local Treasury describes what a business retirement involves.",
            ("h", "Comparing Two Histograms"),
            "To see whether a change worked, draw the before and after with the same bins.",
            ("point", "Same bins, same scale", "Use the same bin width and the same height on the vertical "
             "axis for both."),
            ("point", "Side by side or stacked", "Place the two charts next to each other, or one above the "
             "other, so the eye can compare bar heights."),
            ("point", "Look at the tail", "In the waiting-time case, the goal was to shrink the tail, not to "
             "move the main hump."),
            ("h", "Mistakes to Avoid"),
            ("point", "Reporting only the average", "Show the shape, or at least the median beside the average."),
            ("point", "Gaps between the bars", "A histogram’s bars touch, because the ranges are continuous."),
            ("point", "Unequal bins", "Bins of different widths make some bars look taller than they should."),
            ("point", "Trusting one bin width", "Try a wider and a narrower one before deciding what the shape "
             "is."),
            ("h", "Key Takeaways"),
            ("point", "A histogram counts values in equal bins", "And shows the counts as touching bars."),
            ("point", "Two ways to build it", "COUNTIFS for a checkable table, the Histogram chart for speed."),
            ("point", "Bin width matters", "Too wide hides detail, too narrow shows noise."),
            ("point", "The shape suggests the next step", "A long tail, two humps or a wall each point to a "
             "different question."),
            ("h", "Your Part 39 Exercise"),
            ("point", "Step 1", "Enter the practice data and build the formula table with ten-minute bins."),
            ("point", "Step 2", "Insert a Histogram chart and set the bucket size to 10, then to 5. Note what "
             "changes."),
            ("point", "Step 3", "Add five more waits of 40 to 45 minutes. What happens to the shape, the "
             "average and the median?"),
            ("point", "Step 4", "Pick one measure in your office, such as payment amounts or days late, and draw "
             "its histogram."),
            "Two months after the separate desk opened, the office drew the histogram again with the same bins. "
            "The main hump had barely moved. The tail past 30 minutes was gone.",
            ("cta", "Read: Data Analytics Series, Part 38: Same Average, Different Story, Range and Standard Deviation", "/blog/data-analytics-part-38-range-and-standard-deviation/"),
            ("cta", "Read: Data Analytics Series, Part 26: Mean or Median? Choosing the Middle That Tells the Truth", "/blog/data-analytics-part-26-mean-or-median/"),
            ("cta", "Read: Data Analytics Series, Part 34: Outliers, Finding the Number That Doesn’t Fit", "/blog/data-analytics-part-34-outliers/"),
            ("cta", "Read: Data Analytics Series, Part 27: Choosing the Right Chart, Starting From the Question", "/blog/data-analytics-part-27-choosing-the-right-chart/"),
            ("ask", "Which number in your office would look different as a histogram than as an average?"),
        ],
    },
    {
        "title": "Data Analytics Series, Part 38: Same Average, Different Story, Range and Standard Deviation",
        "slug": "data-analytics-part-38-range-and-standard-deviation",
        "category": "data",
        "date": "May 16, 2027",
        "summary": "Two sets of numbers can share the same average and behave completely differently. This part "
                   "shows how to measure spread with the range and the standard deviation in Google Sheets, "
                   "how to compare spread between groups of different sizes, and how to use it to plan.",
        "publish_on": "2027-05-16 21:00",
        "body": [
            "The supervisor compared the two field collectors over ten working days. Both averaged ₱40,000 a "
            "day. On paper, they were the same.",
            "The cashier did not agree. One collector arrived every afternoon with almost exactly the same "
            "amount. The other might bring ₱20,000 one day and ₱65,000 the next, and on the big days the cash "
            "count took twice as long and the bank run had to wait.",
            "(The collectors and the amounts are invented for this lesson. The Google Sheets functions are "
            "real.)",
            "Part 37 compared places of different sizes with rates. This part looks at what an average leaves "
            "out: how far the numbers spread around it. By the end of this post, you will know how to measure "
            "spread with the range and the standard deviation, which Google Sheets function to use, how to "
            "compare spread fairly, and how spread helps an office plan.",
            ("photo", "blog/data-spread.jpg", "Spread: two sets of daily collections with the same average, one "
             "tightly grouped and one widely scattered. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "The Practice Data"),
            "Type the daily collections, in thousands of pesos, into two columns. Column A is Collector A, "
            "column B is Collector B, with headers in row 1 and ten days in rows 2 to 11.",
            ("point", "Collector A", "40, 42, 38, 41, 39, 40, 43, 37, 40, 40"),
            ("point", "Collector B", "20, 65, 30, 55, 25, 60, 40, 35, 50, 20"),
            ("point", "Check the average", "=AVERAGE(A2:A11) and =AVERAGE(B2:B11) both return 40."),
            "If you stopped at the average, as Part 26 warned, you would miss the difference that matters to "
            "the cashier.",
            ("h", "Measure 1: The Range"),
            "The range is the biggest value minus the smallest.",
            ("point", "Formula", "=MAX(A2:A11)-MIN(A2:A11)"),
            ("point", "Collector A", "43 − 37 = 6, or ₱6,000."),
            ("point", "Collector B", "65 − 20 = 45, or ₱45,000."),
            ("point", "Strength", "Anyone can understand it at once."),
            ("point", "Weakness", "It uses only two numbers. One unusual day can make it look wide, even if "
             "every other day was steady."),
            ("h", "Measure 2: The Standard Deviation"),
            "The standard deviation uses every value. In plain words, it is a typical distance between each "
            "day’s amount and the average. A small number means the days cluster near the average. A large one "
            "means they scatter.",
            ("point", "Formula", "=STDEV(A2:A11)"),
            ("point", "Collector A", "About 1.76, or roughly ₱1,800."),
            ("point", "Collector B", "About 16.67, or roughly ₱16,700."),
            "Same average, but Collector B’s days typically land more than nine times as far from it.",
            ("photo", "blog/data-spread-dots.jpg", "Ten days for each collector, one dot per day, with the "
             "average line and a band one standard deviation wide on each side. Figures are invented. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "STDEV or STDEVP?"),
            "Google’s help page explains the difference in two lines. STDEV calculates the standard deviation "
            "based on a sample. To calculate it across an entire population, use STDEVP.",
            ("point", "Use STDEV", "When the ten days stand for the collector’s usual pattern, which is the "
             "common case. Here it gives 1.76 and 16.67."),
            ("point", "Use STDEVP", "When the data is every case there is, such as all twelve months of one "
             "closed year, and you only want to describe that set. Here it would give 1.67 and 15.81."),
            ("point", "Say which you used", "The difference is small for large sets and larger for small ones."),
            ("h", "Comparing Spread Fairly"),
            "A standard deviation is in the same units as the data. That makes comparisons tricky when the "
            "averages differ. A spread of ₱5,000 is large for someone averaging ₱10,000 and small for someone "
            "averaging ₱200,000.",
            ("point", "Coefficient of variation", "Divide the standard deviation by the average: "
             "=STDEV(B2:B11)/AVERAGE(B2:B11)."),
            ("point", "Collector A", "About 4.4 percent."),
            ("point", "Collector B", "About 41.7 percent."),
            "Now a collector with a bigger route and a bigger average can be compared with a small one.",
            ("h", "Why Spread Is Not Bad by Itself"),
            "A wide spread is a fact, not a fault. It needs a reason.",
            ("point", "The route", "Collector B covers the market on its busy days and quiet barangays on the "
             "others. That alone can explain the swings."),
            ("point", "The calendar", "Deadlines bring big days. Part 24 of the Business Intelligence Series "
             "showed how moving averages smooth those out."),
            ("point", "The records", "If neither the route nor the calendar explains it, look closer. Part 34 "
             "showed how to find single days that do not fit."),
            ("h", "Using Spread to Plan"),
            ("point", "Cash handling", "On Collector B’s market days, plan a second counter for the cash count "
             "and an earlier bank run."),
            ("point", "Expected amounts", "A rough band of the average plus or minus one standard deviation, "
             "about ₱23,000 to ₱57,000 for Collector B, describes a typical day. Days far outside it deserve a "
             "note in the log."),
            ("point", "Targets", "A single daily target means little for a collector whose days naturally swing "
             "widely. A weekly or monthly target fits better. Part 8 covered metrics that tell the truth."),
            ("h", "Spread for Many Groups at Once"),
            "With twelve collectors or twenty barangays, compute spread in a summary table instead of one "
            "formula at a time.",
            ("point", "In a pivot table", "Part 24 built pivot tables. Add the amount twice to Values: once "
             "summarized by AVERAGE and once by STDEV. Each row then shows a group’s average and its spread "
             "side by side."),
            ("point", "With a formula per group", "If the data is in a long table with the collector’s name in "
             "column A and the amount in column C, a filtered formula works for one name: "
             "=STDEV(FILTER(C2:C, A2:A=\"Collector B\"))."),
            ("point", "Sort by the coefficient of variation", "The groups at the top have the least "
             "predictable days and are where planning matters most."),
            ("h", "Watching Spread Over Time"),
            "Spread can change even when the average does not. A collector whose standard deviation doubles from "
            "one quarter to the next may have a new route, a new schedule or a records problem.",
            ("point", "Compute it by month", "One standard deviation per month gives a short series you can "
             "chart."),
            ("point", "Look for jumps", "A sudden rise is a question to ask, not an answer."),
            ("point", "Keep the same window", "Compare ten working days with ten working days, or months with "
             "months, so the measure is fair."),
            ("h", "Reporting It"),
            ("point", "Pair the average with the spread", "“Average ₱40,000 a day (standard deviation "
             "₱16,700).”"),
            ("point", "Show the dots", "A simple dot chart of each day says more than either number."),
            ("point", "Explain it in words", "“Collector B’s days vary widely because of the market schedule.”"),
            ("h", "Mistakes to Avoid"),
            ("point", "Reporting only the average", "Add the range or the standard deviation."),
            ("point", "Trusting the range alone", "One odd day can stretch it."),
            ("point", "Comparing standard deviations of very different averages", "Use the coefficient of "
             "variation."),
            ("point", "Treating spread as wrongdoing", "Find the reason first."),
            ("h", "Key Takeaways"),
            ("point", "Averages hide spread", "Same average, different behavior."),
            ("point", "Range is quick", "MAX minus MIN, but sensitive to one value."),
            ("point", "Standard deviation uses every value", "STDEV for a sample, STDEVP for a whole population."),
            ("point", "Coefficient of variation compares", "Standard deviation divided by the average."),
            ("h", "Your Part 38 Exercise"),
            ("point", "Step 1", "Enter the practice data and compute the average, range and STDEV for each "
             "collector."),
            ("point", "Step 2", "Change Collector B’s 65 to 45. Which measure changes more, the range or the "
             "standard deviation?"),
            ("point", "Step 3", "Compute the coefficient of variation for both."),
            ("point", "Step 4", "Pick one daily figure in your office and report its average with its spread."),
            "The supervisor’s next report gave both collectors the same average and a second line beneath it. "
            "The cashier finally had a number for what she had seen every afternoon, and the market-day bank run "
            "moved to one o’clock, so the bigger count no longer ran past the bank’s cut-off time.",
            ("cta", "Read: Data Analytics Series, Part 26: Mean or Median? Choosing the Middle That Tells the Truth", "/blog/data-analytics-part-26-mean-or-median/"),
            ("cta", "Read: Data Analytics Series, Part 34: Outliers, Finding the Number That Doesn’t Fit", "/blog/data-analytics-part-34-outliers/"),
            ("cta", "Read: Data Analytics Series, Part 8: Metrics and KPIs That Tell the Truth", "/blog/data-analytics-part-8-metrics-and-kpis/"),
            ("cta", "Read: Business Intelligence Series, Part 24: Trend Lines and Moving Averages, Seeing the Direction Without Guessing", "/blog/business-intelligence-part-24-trend-lines-and-moving-averages/"),
            ("ask", "Which number in your office has a steady average but days that swing widely?"),
        ],
    },
    {
        "title": "Data Analytics Series, Part 37: Rates per 1,000, Comparing Barangays of Different Sizes",
        "slug": "data-analytics-part-37-rates-per-1000",
        "category": "data",
        "date": "May 11, 2027",
        "summary": "A big barangay will have more of almost everything than a small one, so raw counts can point "
                   "the office in the wrong direction. This part shows how to turn counts into rates per 1,000 "
                   "residents in Google Sheets, how to read them, and the traps of small populations and "
                   "mismatched years.",
        "publish_on": "2027-05-11 21:00",
        "body": [
            "The plan for the business registration drive was already on the whiteboard. The two barangays with "
            "the fewest registered businesses, Mabini with 45 and Bukal with 48, would get the first visits. "
            "It seemed obvious. Fewer registrations meant more businesses operating without a permit.",
            "Then the analyst added one column to the sheet, and Mabini dropped off the list.",
            "(The barangays, the populations and the business counts below are invented for this lesson. The "
            "method and the Google Sheets formulas are real.)",
            "Part 36 showed how an average can mislead when groups differ in size. This part deals with the "
            "same problem in its simplest form: comparing plain counts between places of different sizes. "
            "When you finish, you will know why raw counts mislead, how to compute a rate per 1,000 "
            "residents, how to choose the right denominator, and when a rate itself should not be trusted.",
            ("photo", "blog/data-rates.jpg", "Rates per 1,000: divide each count by the population, then "
             "multiply by 1,000, so a small barangay and a large one can be compared fairly. (Illustration: "
             "Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Why Counts Mislead"),
            "A count answers “how many?” It does not answer “how many for its size?”",
            ("point", "Big places have more of everything", "More residents, more stores, more complaints, "
             "more late payments. A large count may simply mean a large barangay."),
            ("point", "Small places look quiet", "A low count can hide a high share, because there were few "
             "people to begin with."),
            ("point", "Rankings flip", "Once size is taken into account, the barangay at the bottom of the "
             "count list may be in the middle, or near the top."),
            ("h", "The Practice Data"),
            "Type this into a new sheet. Column A is the barangay, B the population, and C the number of "
            "registered businesses.",
            ("point", "Poblacion", "Population 8,200, businesses 410"),
            ("point", "San Isidro", "Population 3,100, businesses 62"),
            ("point", "Malinao", "Population 2,400, businesses 60"),
            ("point", "Santa Cruz", "Population 5,600, businesses 84"),
            ("point", "Mabini", "Population 1,500, businesses 45"),
            ("point", "Bukal", "Population 4,000, businesses 48"),
            "Put headers in row 1, so the data runs from row 2 to row 7.",
            ("h", "Computing the Rate"),
            ("point", "Formula", "In D2, enter =C2/B2*1000 and fill down to D7."),
            ("point", "Rounding", "To show one decimal place, use =ROUND(C2/B2*1000, 1). Part 32 covered "
             "rounding and why totals may not add up."),
            ("point", "Header", "Name the column “Businesses per 1,000 residents,” not just “Rate.”"),
            "The results:",
            ("point", "Poblacion", "50.0 per 1,000"),
            ("point", "Mabini", "30.0 per 1,000"),
            ("point", "Malinao", "25.0 per 1,000"),
            ("point", "San Isidro", "20.0 per 1,000"),
            ("point", "Santa Cruz", "15.0 per 1,000"),
            ("point", "Bukal", "12.0 per 1,000"),
            "Mabini, last by count, is second by rate. Santa Cruz, with the second-highest count, is "
            "second from the bottom by rate. Bukal is low on both lists, so it stays a priority. The drive "
            "now starts in Bukal and Santa Cruz.",
            ("photo", "blog/data-rates-bars.jpg", "The same six barangays ranked two ways: by count of "
             "registered businesses, and by businesses per 1,000 residents. Figures are invented. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Why 1,000?"),
            "Any multiplier works, as long as every row uses the same one. The choice is about readability.",
            ("point", "Per 100 is a percent", "Useful when the count is a part of the whole, such as businesses "
             "that renewed out of all businesses."),
            ("point", "Per 1,000 suits small rates", "Twelve per 1,000 is easier to read than 1.2 percent of "
             "residents, which sounds like something else."),
            ("point", "Per 10,000 or 100,000", "Used for rare events, so the numbers are not tiny decimals."),
            "Pick one, write it in the header, and do not mix them in the same table.",
            ("h", "Choosing the Right Denominator"),
            "The number you divide by decides what the rate means. Ask what the count could have come from.",
            ("point", "Residents", "For businesses, complaints or permits, where people are the source."),
            ("point", "Households", "For things counted once per home, such as water connections."),
            ("point", "Businesses", "For late renewals or inspections, divide by registered businesses, not "
             "by residents."),
            ("point", "Land area or road length", "For things spread over space, such as market stalls per "
             "hectare or potholes per kilometer."),
            "Where official counts are needed, the Philippine Statistics Authority publishes census population "
            "counts down to the barangay. Use the same census year for every row.",
            ("h", "When a Rate Should Not Be Trusted"),
            ("point", "Small populations jump", "In Mabini, one more business moves the rate from 30.0 to about "
             "30.7. In the Poblacion, one more business moves it by about 0.1. A small barangay’s rate can swing "
             "a lot from year to year by chance, as Part 17 explained for small samples."),
            ("point", "Mismatched years", "Dividing this year’s businesses by a population count from many "
             "years ago overstates the rate wherever the population has grown."),
            ("point", "Different definitions", "If one barangay counts branches separately and another does "
             "not, the rates are not comparable. Agree on what is counted first."),
            ("point", "Rates do not add", "You cannot sum six barangay rates to get a municipal rate. Add the "
             "counts, add the populations, and divide, as Part 36 showed with totals."),
            "For the whole municipality here: 709 businesses ÷ 24,800 residents × 1,000 = about 28.6 per "
            "1,000.",
            ("h", "Rates Over Time"),
            "A rate is most useful when it is tracked. One year’s figure says where each barangay stands. "
            "Several years say which way each one is moving.",
            ("point", "Keep the same denominator", "If the population is updated with a new census, note the "
             "year the change took effect, so a jump in the rate is not mistaken for a jump in businesses."),
            ("point", "Watch the direction", "A barangay whose rate rises from 12 to 15 over two years may "
             "deserve less attention than one that slipped from 25 to 20."),
            ("point", "Look at the counts too", "If both the count and the population fell, the rate can stay "
             "flat while the barangay is shrinking. The rate alone would not show that."),
            ("h", "Showing It Clearly"),
            ("point", "Sort by the rate", "A sorted bar chart, as Part 27 suggested for comparisons, puts the "
             "lowest and highest at the ends."),
            ("point", "Show the count beside it", "A rate without its count hides how small some groups are. "
             "“12.0 per 1,000 (48 businesses)” tells the whole story."),
            ("point", "Mark the overall rate", "A line at 28.6 shows which barangays are above or below the "
             "municipality as a whole."),
            ("point", "Color only the outliers", "Conditional formatting from Part 31 can shade rates below a "
             "chosen level."),
            ("h", "Mistakes to Avoid"),
            ("point", "Ranking places by raw counts", "Divide by size first."),
            ("point", "Using the wrong denominator", "Match it to where the count comes from."),
            ("point", "Trusting tiny populations", "Show the count, and look at more than one year."),
            ("point", "Averaging or adding rates", "Combine the counts and populations instead."),
            ("h", "Key Takeaways"),
            ("point", "Counts reflect size", "A big barangay can have bigger counts just by being big."),
            ("point", "Rate = count ÷ population × 1,000", "One formula, filled down."),
            ("point", "The denominator is a choice", "Residents, households, businesses or area."),
            ("point", "Small groups are noisy", "Report the count beside the rate."),
            ("h", "Your Part 37 Exercise"),
            ("point", "Step 1", "Enter the practice data and compute businesses per 1,000 residents."),
            ("point", "Step 2", "Sort by count, then by rate, and note which barangays change places."),
            ("point", "Step 3", "Compute the municipal rate from the totals and draw it as a line on a bar "
             "chart."),
            ("point", "Step 4", "Find one count in your office’s reports that compares places of different "
             "sizes, and turn it into a rate."),
            "Three months later, the drive had registered 14 new businesses in Bukal and 11 in Santa Cruz. "
            "Mabini, the barangay that almost got the first visit, already had one of the highest rates in the "
            "municipality. Its low count had simply reflected its size.",
            ("cta", "Read: Data Analytics Series, Part 36: Weighted Averages, and Why Averaging Averages Misleads", "/blog/data-analytics-part-36-weighted-averages/"),
            ("cta", "Read: Data Analytics Series, Part 17: Samples and Margin of Error, Checking 400 Receipts Instead of 12,000", "/blog/data-analytics-part-17-samples-margin-of-error/"),
            ("cta", "Read: Data Analytics Series, Part 27: Choosing the Right Chart, Starting From the Question", "/blog/data-analytics-part-27-choosing-the-right-chart/"),
            ("cta", "Read: Business Intelligence Series, Part 27: Maps by Barangay, When Location Is the Point", "/blog/business-intelligence-part-27-maps-by-barangay/"),
            ("ask", "Which report in your office compares places by raw counts that should be rates?"),
        ],
    },
    {
        "title": "Data Analytics Series, Part 36: Weighted Averages, and Why Averaging Averages Misleads",
        "slug": "data-analytics-part-36-weighted-averages",
        "category": "data",
        "date": "May 6, 2027",
        "summary": "Averaging five barangay collection rates does not give the town’s collection rate. This part "
                   "explains why a plain average of percentages or averages can mislead, how to compute a "
                   "weighted average in Google Sheets with AVERAGE.WEIGHTED or SUMPRODUCT, and when a simple "
                   "average is still the right choice.",
        "publish_on": "2027-05-06 21:00",
        "body": [
            "Two reports reached the mayor’s office on the same day. The planning office said the town "
            "collected 76 percent of its real property tax billings last year. The treasury said 82.5 "
            "percent. Both used the same five barangay figures, and both had checked their arithmetic.",
            "The difference was one decision. The planning office averaged the five barangay rates. The "
            "treasury divided the town’s total collections by its total billings. Only one of them answered "
            "the question the mayor had asked.",
            "(The barangays and the amounts are invented for practice. The Google Sheets functions are real.)",
            "Part 35 showed that two numbers moving together do not prove a cause. This part looks at a "
            "quieter mistake that hides inside a single average. By the end of this post, you will know when "
            "a plain average misleads, what a weighted average is, how to compute one in Google Sheets, and "
            "how to tell which average a question needs.",
            ("photo", "blog/data-weighted.jpg", "Weighted averages: when groups differ in size, give each one "
             "a weight in proportion to its size, or compute from the totals. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "The Practice Data"),
            "Type this into a new sheet. Column A is the barangay, B the amount billed, C the amount "
            "collected, and D the collection rate.",
            ("point", "Poblacion", "Billed ₱2,000,000, collected ₱1,800,000, rate 90%."),
            ("point", "San Isidro", "Billed ₱500,000, collected ₱400,000, rate 80%."),
            ("point", "Malinao", "Billed ₱200,000, collected ₱100,000, rate 50%."),
            ("point", "Santa Cruz", "Billed ₱800,000, collected ₱560,000, rate 70%."),
            ("point", "Mabini", "Billed ₱350,000, collected ₱315,000, rate 90%."),
            "Put headers in row 1, so the data runs from row 2 to row 6. In D2, enter =C2/B2 and fill down. "
            "Format column D as a percent.",
            ("h", "The Plain Average"),
            ("point", "Formula", "=AVERAGE(D2:D6)"),
            ("point", "Result", "76.0 percent."),
            ("point", "What it treats as equal", "Each barangay counts the same. Malinao’s ₱200,000 billing "
             "pulls the result as hard as the poblacion’s ₱2,000,000."),
            "That is the average of the barangays’ rates. It is not the town’s rate.",
            ("h", "The Town’s Real Rate"),
            ("point", "From the totals", "=SUM(C2:C6)/SUM(B2:B6) gives ₱3,175,000 ÷ ₱3,850,000 = 82.5 percent."),
            ("point", "Why it is higher", "The poblacion holds more than half the billings and collected 90 "
             "percent. Its weight should be larger, and the totals give it that weight automatically."),
            "When the question is “What share of the town’s billings did we collect?”, the answer is 82.5 "
            "percent.",
            ("photo", "blog/data-weighted-bars.jpg", "Five barangays drawn by the size of their billings: "
             "equal votes give 76 percent, weighting by billings gives 82.5 percent. Figures are invented. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "What a Weighted Average Is"),
            "A weighted average multiplies each value by a weight, adds the results, and divides by the total "
            "of the weights. Here, each rate is weighted by the amount billed.",
            ("point", "AVERAGE.WEIGHTED", "Google’s help describes AVERAGE.WEIGHTED(values, weights) as "
             "finding the weighted average of a set of values. =AVERAGE.WEIGHTED(D2:D6, B2:B6) returns 82.5 "
             "percent."),
            ("point", "SUMPRODUCT", "=SUMPRODUCT(D2:D6, B2:B6)/SUM(B2:B6) gives the same answer, and works in "
             "other spreadsheet programs too."),
            ("point", "Weights must line up", "The help page notes that the weights range must have the same "
             "number of rows and columns as the values, and that weights cannot be negative."),
            "Weighting the rates by billings gives the same result as dividing the totals. That is a useful "
            "check: if the two do not match, something in the sheet is wrong.",
            ("h", "A Second Example: Time at the Counter"),
            "The same trap appears with averages that are not percentages. Suppose Window 1 served 300 "
            "taxpayers last week with an average of 6 minutes each, and Window 2, which handles complicated "
            "cases, served 50 with an average of 20 minutes.",
            ("point", "Plain average of the two windows", "(6 + 20) ÷ 2 = 13 minutes."),
            ("point", "Weighted by taxpayers served", "(300 × 6 + 50 × 20) ÷ 350 = 2,800 ÷ 350 = 8 minutes."),
            ("point", "Which one describes a taxpayer’s visit", "The weighted one. Most visitors went to "
             "Window 1, and an average visit took about 8 minutes, not 13."),
            "If the question were “Which window is slower?”, you would compare 6 and 20 directly, with no "
            "average at all.",
            ("h", "Rates in a Pivot Table"),
            "Part 24 built pivot tables. If you summarize by barangay and want a rate, add billed and collected "
            "as two values with SUM, then divide the two sums. Do not put the rate column itself into the pivot "
            "table and choose AVERAGE, because that gives the plain average of the rows again. Part 22 of the "
            "Business Intelligence Series showed the same rule for calculated fields: SUM of one divided by SUM "
            "of the other.",
            ("h", "Where the Trap Hides"),
            ("point", "Averages of averages", "An average daily collection for each month, averaged across "
             "twelve months, ignores that months have different numbers of working days."),
            ("point", "Rates from different-sized groups", "Collection rates, on-time rates and error rates by "
             "office, barangay or collector."),
            ("point", "Summary tabs built from summary tabs", "A table of percentages by barangay, averaged "
             "again in another tab, loses the sizes behind each percentage."),
            ("point", "A small group with an extreme rate", "A barangay with only ten businesses and a 20 "
             "percent rate can drag a plain average down far more than it affects the town’s money."),
            ("h", "When the Plain Average Is Right"),
            "A plain average is not wrong. It answers a different question.",
            ("point", "“How is a typical barangay doing?”", "Each barangay is one unit, and the plain "
             "average, or better the median from Part 26, describes the typical one."),
            ("point", "“How much of the town’s money did we collect?”", "Use the totals or the weighted "
             "average."),
            ("point", "Say which one you used", "Write it under the number: “weighted by amount billed” or "
             "“average of barangay rates.”"),
            "The mayor needed the second answer. A barangay captain asking whether her barangay is behind the "
            "others might need the first.",
            ("h", "Three Questions Before You Average"),
            ("point", "What is one unit?", "A barangay, a taxpayer, a peso or a day. The answer decides the "
             "weight."),
            ("point", "Are the groups the same size?", "If yes, plain and weighted averages agree. If not, "
             "they can differ by several points, as they did here."),
            ("point", "Can I compute it from totals?", "If the raw amounts exist, divide the totals. It is "
             "the simplest weighted average there is."),
            ("h", "Mistakes to Avoid"),
            ("point", "Averaging percentages from groups of different sizes", "Weight them, or use totals."),
            ("point", "Mismatched ranges", "Values and weights must be the same size and in the same order."),
            ("point", "Weighting by the wrong thing", "Collection rates weigh by billings, not by number of "
             "taxpayers, if the question is about pesos."),
            ("point", "Not labeling the method", "Two honest offices produced two different numbers."),
            ("h", "Key Takeaways"),
            ("point", "Plain average", "Every group counts the same."),
            ("point", "Weighted average", "Each group counts by its size."),
            ("point", "Totals are the check", "Sum the parts, then divide."),
            ("point", "Match the question", "Typical group, or the whole town."),
            ("h", "Your Part 36 Exercise"),
            ("point", "Step 1", "Enter the practice data and compute the plain average, the totals rate and "
             "AVERAGE.WEIGHTED."),
            ("point", "Step 2", "Change Malinao’s collection to ₱180,000. Which of the three results moves "
             "the most, and why?"),
            ("point", "Step 3", "Weight the rates by number of taxpayers instead, using numbers you invent. "
             "Write one sentence on what question that average answers."),
            ("point", "Step 4", "Find one percentage in your office’s reports that is an average of other "
             "percentages, and check it against the totals."),
            "The two offices met for fifteen minutes. The final report showed 82.5 percent for the town, "
            "weighted by billings, with a second line beneath it: “average of barangay rates, 76 percent, "
            "for comparing barangays.” Nobody had been wrong. They had been answering different questions.",
            ("cta", "Read: Data Analytics Series, Part 26: Mean or Median? Choosing the Middle That Tells the Truth", "/blog/data-analytics-part-26-mean-or-median/"),
            ("cta", "Read: Data Analytics Series, Part 30: Percent Change or Percentage Points? Reporting Growth Without Confusion", "/blog/data-analytics-part-30-percent-change/"),
            ("cta", "Read: Data Analytics Series, Part 24: Pivot Tables, a Summary You Can Rearrange in Seconds", "/blog/data-analytics-part-24-pivot-tables/"),
            ("cta", "Read: Data Analytics Series, Part 8: Metrics and KPIs That Tell the Truth", "/blog/data-analytics-part-8-metrics-and-kpis/"),
            ("ask", "Which percentage in your office’s reports is really an average of other percentages?"),
        ],
    },
    {
        "title": "Data Analytics Series, Part 35: Correlation Is Not Causation, When Two Numbers Move Together",
        "slug": "data-analytics-part-35-correlation-and-causation",
        "category": "data",
        "date": "May 1, 2027",
        "summary": "Two numbers that rise and fall together are not proof that one causes the other. This part "
                   "shows how to measure a relationship with CORREL in Google Sheets, how to read the result, "
                   "the three common reasons a strong correlation misleads, and how to test a cause before "
                   "spending money on it.",
        "publish_on": "2027-05-01 21:00",
        "body": [
            "The analyst had a chart that looked like an answer. Each dot was a barangay. Across the bottom ran "
            "the share of businesses with a mobile number on file. Up the side ran the share that renewed their "
            "permits on time. The dots climbed together in a neat line from the lower left to the upper right.",
            "The proposal wrote itself: collect a mobile number from every business, and on-time renewals would "
            "rise everywhere. Before it went to the budget officer, a colleague asked one question. “Which "
            "barangays are these, and how far are they from the town hall?”",
            "(The barangays, the figures and the people in this lesson are invented for practice. The Google "
            "Sheets function is real.)",
            "Part 34 looked for single numbers that do not fit. This part looks at pairs of numbers that seem to "
            "fit too well. Read to the end and you will know what correlation measures, how to compute it in "
            "Google Sheets, how to read the result, why a strong correlation can still mislead, and how to test "
            "whether one thing really causes another.",
            ("photo", "blog/data-correlation.jpg", "Correlation is not causation: two numbers can move together "
             "because of a third factor, by chance, or in the opposite direction from what you assume. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "What Correlation Measures"),
            "Correlation measures how closely two sets of numbers move together in a straight-line pattern. "
            "The usual measure is r, the Pearson correlation coefficient. It runs from −1 to +1.",
            ("point", "Close to +1", "When one number is high, the other tends to be high too."),
            ("point", "Close to −1", "When one number is high, the other tends to be low."),
            ("point", "Close to 0", "No straight-line pattern. There may still be a curved one, so look at the chart."),
            "Correlation answers one narrow question: do these two numbers move together? It says nothing about "
            "why.",
            ("h", "The Practice Data"),
            "Type this table into a new sheet. Column A is the barangay, B the distance from the town hall in "
            "kilometers, C the percent of businesses with a mobile number on file, and D the percent that "
            "renewed on time.",
            ("point", "Poblacion", "0.5 km, 85, 90"),
            ("point", "San Isidro", "3 km, 62, 80"),
            ("point", "Malinao", "6 km, 58, 66"),
            ("point", "Bagong Silang", "4 km, 70, 74"),
            ("point", "Santa Cruz", "2 km, 74, 82"),
            ("point", "Mabini", "9 km, 40, 62"),
            ("point", "San Roque", "7 km, 51, 61"),
            ("point", "Bukal", "11 km, 38, 57"),
            "Put the headers in row 1, so the data runs from row 2 to row 9.",
            ("h", "Computing It in Google Sheets"),
            "Google Sheets has a CORREL function. Its help page describes it as calculating r, the Pearson "
            "product-moment correlation coefficient, and notes that it is the same as PEARSON.",
            ("point", "Mobile numbers and renewals", "=CORREL(D2:D9, C2:C9) returns about 0.93. A strong positive "
             "relationship."),
            ("point", "Distance and renewals", "=CORREL(D2:D9, B2:B9) returns about −0.96. Even stronger, and "
             "negative: the farther the barangay, the lower the on-time rate."),
            ("point", "Distance and mobile numbers", "=CORREL(C2:C9, B2:B9) returns about −0.97. Barangays far "
             "from the town hall also have fewer numbers on file."),
            "Then make a scatter chart, as Part 27 described. Select C1:D9, insert a chart, and choose Scatter. "
            "Always look at the chart. A single number cannot show a curve, a cluster or one extreme point "
            "pulling the line.",
            ("photo", "blog/data-correlation-hidden.jpg", "The same eight barangays: mobile numbers and on-time "
             "renewals move together, but distance from the town hall moves with both. Figures are invented. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Why a Strong Correlation Can Mislead"),
            "The colleague’s question pointed at the first of three common traps.",
            ("point", "1. A third factor", "Distance is related to both numbers. Barangays near the town hall "
             "may have more established businesses that keep their records updated, and owners who can "
             "easily drop by to renew. Mobile numbers and renewals may both be results of being close, not causes of each "
             "other. Analysts call this a confounding variable."),
            ("point", "2. The arrow points the other way", "A business that renews on time visits the counter "
             "every year, and each visit is a chance to update its mobile number. Renewing could be causing "
             "the numbers on file, not the reverse."),
            ("point", "3. Chance", "With only eight barangays, a strong pattern can appear by luck. Small "
             "samples make striking correlations easy to find, as Part 17 explained when it discussed sample "
             "size."),
            "None of these means the mobile-number idea is wrong. They mean the chart cannot prove it right.",
            ("h", "Two More Cautions"),
            ("point", "Look for many comparisons", "If you test twenty pairs of columns, one or two may show a "
             "strong correlation by chance. Report how many pairs you checked, not only the one that worked."),
            ("point", "Groups are not individuals", "This data is by barangay. It does not show that a single "
             "business with a mobile number is more likely to renew on time. A pattern across groups can be "
             "weaker, or even reversed, inside each group."),
            ("h", "How to Test a Cause"),
            "To find out whether one thing causes another, change one thing on purpose and compare.",
            ("point", "Run a small test", "Part 32 of the Project Management Series ran a pilot: text reminders "
             "in one barangay, with similar barangays left as they were. That design compares like with like."),
            ("point", "Compare similar groups", "Test the idea in two barangays at a similar distance, one with "
             "the change and one without. Distance then cannot explain the difference."),
            ("point", "Measure before and after", "Record the on-time rate for the same period last year, then "
             "again after the change. Part 30 showed how to report the difference in percentage points."),
            ("point", "Write down what else changed", "A new road, a new collector or a deadline extension "
             "can move the numbers too. Note them in the report."),
            ("h", "How to Write It in a Report"),
            "Words matter. Choose verbs that match what the data can show.",
            ("point", "Say", "“Barangays with more mobile numbers on file also had higher on-time renewal "
             "rates.”"),
            ("point", "Do not say", "“Collecting mobile numbers increases on-time renewals.” That claims a "
             "cause the data has not shown."),
            ("point", "Add the third factor", "“Both measures were lower in barangays farther from the town "
             "hall.”"),
            "A report that separates what moved together from what caused what is a report a decision maker "
            "can trust.",
            ("h", "Mistakes to Avoid"),
            ("point", "Treating r as proof of cause", "Correlation shows a pattern, not a reason."),
            ("point", "Skipping the chart", "Check the scatter chart for curves, clusters and outliers."),
            ("point", "Ignoring a third factor", "Ask what else differs between the high and low groups."),
            ("point", "Spending before testing", "Run a small, fair comparison first."),
            ("h", "Key Takeaways"),
            ("point", "CORREL gives r", "From −1 to +1, a measure of straight-line pattern only."),
            ("point", "Three traps", "A third factor, a reversed arrow, or chance."),
            ("point", "Test a cause on purpose", "Change one thing and compare similar groups."),
            ("point", "Write carefully", "Use “moved together,” not “caused,” unless a test showed it."),
            ("h", "Your Part 35 Exercise"),
            ("point", "Step 1", "Enter the practice data and compute the three CORREL results."),
            ("point", "Step 2", "Make a scatter chart of mobile numbers against renewals, and another of "
             "distance against renewals."),
            ("point", "Step 3", "Write two sentences about the data: one that describes the pattern, and one "
             "that names a possible third factor."),
            ("point", "Step 4", "Design a fair test for the mobile-number idea using two barangays at a "
             "similar distance."),
            "The proposal went to the budget officer in a different form: a three-month test in two barangays, "
            "each about six kilometers from the town hall, with mobile numbers collected in only one. The "
            "colleague’s question had saved the office from paying for a cause it could not yet prove.",
            ("cta", "Read: Data Analytics Series, Part 27: Choosing the Right Chart, Starting From the Question", "/blog/data-analytics-part-27-choosing-the-right-chart/"),
            ("cta", "Read: Data Analytics Series, Part 13: Bias in Data, and How to Catch It", "/blog/data-analytics-part-13-bias-in-data/"),
            ("cta", "Read: Project Management Series, Part 32: Running a Pilot, Testing Small Before Going Big", "/blog/project-management-part-32-running-a-pilot/"),
            ("cta", "Read: Data Analytics Series, Part 17: Samples and Margin of Error, Checking 400 Receipts Instead of 12,000", "/blog/data-analytics-part-17-samples-margin-of-error/"),
            ("ask", "What two numbers in your office move together, and what else might explain it?"),
        ],
    },
    {
        "title": "Data Analytics Series, Part 34: Outliers, Finding the Number That Doesn’t Fit",
        "slug": "data-analytics-part-34-outliers",
        "category": "data",
        "date": "April 26, 2027",
        "summary": "One unusual number can pull an average far from the truth, or hide a typing error or a "
                   "missing remittance. This part shows how to find outliers with quartiles and the 1.5 IQR "
                   "rule in Google Sheets, how to flag them automatically, and what to do once you find one.",
        "publish_on": "2027-04-26 21:00",
        "body": [
            "The analyst was preparing a chart of one collector’s daily remittances for the first two weeks "
            "of March. The average was ₱6,892 a day. The head of office was pleased. It was the highest "
            "average in the office.",
            "Then the analyst looked at the twelve numbers behind it. Ten of them were between ₱3,700 and "
            "₱4,500. One day showed ₱41,000. Another showed ₱600. The average described none of them.",
            "(The collector, the remittances and the figures are invented for practice. No real person or "
            "office is described.)",
            "Part 33 built lists that update themselves. This part looks for the numbers in those lists that "
            "do not fit. You will learn what an outlier is, why it matters, how to find one with quartiles and "
            "a simple rule, how to flag it automatically in Google Sheets, and, most important, what to do "
            "after you find it.",
            ("photo", "blog/data-outliers.jpg", "Outliers: find them with quartiles, flag them, check the "
             "source document, and never delete one just because it is inconvenient. (Illustration: Butch "
             "Mahinay, aumahinay.dev)", "medium"),
            ("h", "What an Outlier Is"),
            "An outlier is a value far from the rest of the data. It is not automatically an error. It is a "
            "question.",
            ("point", "It can be a mistake", "₱41,000 might be ₱4,100 with an extra zero."),
            ("point", "It can be real and important", "It might be a large business tax payment collected "
             "in the field that day."),
            ("point", "It can be a warning", "₱600 might mean a remittance that has not been recorded yet."),
            "Each of those explanations calls for a different response. The data alone cannot tell you "
            "which one is true.",
            ("h", "Why One Number Matters"),
            "Part 26 showed that the mean can be pulled by extreme values, while the median holds steady. "
            "In this example, the median of the twelve days is ₱4,150. The mean is ₱6,892, about two-thirds "
            "higher, because of one day. A report that used the mean would tell the head of office "
            "something that did not happen on any of the twelve days.",
            ("h", "The Practice Data"),
            "Type the twelve daily remittances into column B, from B2 to B13, in this order: 4200, 3900, "
            "4500, 4100, 3800, 4300, 41000, 4000, 3700, 4400, 600, 4200. Put the dates, March 1 to March 12, "
            "in column A if you like.",
            ("h", "Step 1: Find the Quartiles"),
            "Quartiles split sorted data into four parts. The first quartile, Q1, has a quarter of the values "
            "below it. The third quartile, Q3, has three quarters below it.",
            ("point", "Q1", "In E2: =QUARTILE(B2:B13, 1). The result is 3,875."),
            ("point", "Median", "In E3: =MEDIAN(B2:B13). The result is 4,150."),
            ("point", "Q3", "In E4: =QUARTILE(B2:B13, 3). The result is 4,325."),
            ("point", "Interquartile range", "In E5: =E4-E2. The result is 450. This is the spread of the "
             "middle half of the data."),
            ("h", "Step 2: Apply the 1.5 IQR Rule"),
            "A common rule, associated with the statistician John Tukey, treats a value as an outlier if it "
            "is more than 1.5 interquartile ranges below Q1 or above Q3.",
            ("point", "Lower fence", "In E6: =E2-1.5*E5. The result is 3,200."),
            ("point", "Upper fence", "In E7: =E4+1.5*E5. The result is 5,000."),
            ("point", "The outliers", "Anything below 3,200 or above 5,000: the ₱600 on March 11 and the "
             "₱41,000 on March 7."),
            "The rule is a screen, not a verdict. It tells you where to look. It does not tell you what you "
            "will find.",
            ("photo", "blog/data-outliers-box.jpg", "The twelve days on a number line, with the quartiles, "
             "the fences and the two outliers. Figures are invented. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "Step 3: Flag Them Automatically"),
            ("point", "A flag column", "In C2: =IF(OR(B2<$E$6, B2>$E$7), \"Check\", \"\"), then fill down "
             "to C13. Rows 8 and 12 say Check."),
            ("point", "A color", "Part 31 showed conditional formatting. A custom formula such as "
             "=OR($B2<$E$6, $B2>$E$7) colors the whole row."),
            ("point", "It updates itself", "When a new day is added and the ranges are extended, the "
             "quartiles and fences are recalculated."),
            ("h", "Step 4: Investigate, Don’t Delete"),
            "This is the step that matters. An outlier is checked against the source, not removed because "
            "it spoils a chart.",
            ("point", "Go to the source document", "For a remittance, that is the official receipts and the "
             "deposit slip. Part 13 of Inside the Local Treasury explained why deposits are matched to "
             "collections."),
            ("point", "If it is a typing error", "Correct it, and note the correction and its source in a "
             "change log, as Part 10 of the Business Intelligence Series described."),
            ("point", "If it is real", "Keep it, and explain it in the report. A single large payment is "
             "news, not noise."),
            ("point", "If it cannot be explained yet", "Mark it as pending and say so in the report. Do not "
             "guess."),
            "In the example, the receipts showed a ₱37,000 business tax payment collected in the field on "
            "March 7, so the ₱41,000 was real. The ₱600 on March 11 was the collector’s half day before a "
            "seminar, which the attendance record confirmed. Both stayed in the data, with a note.",
            ("h", "When the Rule Needs Care"),
            ("point", "Very few values", "With only five or six numbers, the quartiles move a lot when one "
             "value changes. Look at the values themselves instead."),
            ("point", "Data that is naturally lopsided", "Business tax payments in a town can include a few "
             "large establishments and many small stores. The rule may flag every large payer, although "
             "those payments are normal. Group the data first, for example large and small businesses, "
             "and screen each group on its own."),
            ("point", "Mixed periods", "January payments can be larger because of the deadline rush described "
             "in Part 2 of Inside the Local Treasury. Compare January with January, not with June."),
            ("h", "Two Quick Checks Without Formulas"),
            ("point", "Sort it", "Part 22 showed sorting. Sort the column from smallest to largest and look "
             "at both ends. Outliers sit there."),
            ("point", "MIN and MAX", "=MIN(B2:B13) and =MAX(B2:B13) show the extremes in two cells. If either "
             "surprises you, find the row."),
            ("h", "Reporting When Outliers Are Real"),
            ("point", "Use the median for a typical day", "₱4,150 describes the collector’s normal day "
             "far better than ₱6,892."),
            ("point", "Show the outlier separately", "“Includes one field collection of ₱37,000 on March 7.”"),
            ("point", "Don’t hide it", "Removing a real value makes the report less honest, not more accurate."),
            ("quote", "An outlier is a question. Answer it from the source document before you answer it in a "
             "chart."),
            ("h", "Mistakes to Avoid"),
            ("point", "Deleting outliers to make a chart look better", "Check, then correct or explain."),
            ("point", "Trusting an average without looking", "Look at the values, or the median."),
            ("point", "Treating the rule as proof", "The 1.5 IQR rule flags; the documents decide."),
            ("point", "Checking only the high values", "A low value can be the more serious warning."),
            ("h", "Key Takeaways"),
            ("point", "Outliers are questions", "Mistake, real event or warning."),
            ("point", "Quartiles find them", "Fences at 1.5 IQR below Q1 and above Q3."),
            ("point", "Flag them automatically", "An IF formula or conditional formatting."),
            ("point", "Investigate, don’t delete", "The source document decides."),
            ("h", "Your Part 34 Exercise"),
            ("point", "Step 1", "Enter the twelve values and build E2 to E7."),
            ("point", "Step 2", "Add the flag column and confirm that rows 8 and 12 say Check."),
            ("point", "Step 3", "Change 41000 to 4100 and watch the flag on row 8 disappear."),
            ("point", "Step 4", "Run the same test on one column of real data in your office, and check "
             "each flag against its source."),
            "The report that went to the head of office used the median, ₱4,150, and a note about the field "
            "collection. She asked why the average had been dropped. The analyst showed her the twelve "
            "numbers, and she agreed the median told the truth.",
            ("cta", "Read: Data Analytics Series, Part 26: Mean or Median? Choosing the Middle That Tells the Truth", "/blog/data-analytics-part-26-mean-or-median/"),
            ("cta", "Read: Data Analytics Series, Part 16: Dirty Data, the Usual Suspects and How to Spot Them", "/blog/data-analytics-part-16-dirty-data/"),
            ("cta", "Read: Data Analytics Series, Part 31: Conditional Formatting, Letting the Sheet Point at the Problems", "/blog/data-analytics-part-31-conditional-formatting/"),
            ("cta", "Read: Inside the Local Treasury, Part 13: From the Cash Box to the Bank, Why Deposits Cannot Wait", "/blog/deposits-cash-box-to-bank/"),
            ("ask", "Which number in your last report would you check first if you were looking for an outlier?"),
        ],
    },
    {
        "title": "Data Analytics Series, Part 33: FILTER, SORT and UNIQUE, Lists in Google Sheets That Update Themselves",
        "slug": "data-analytics-part-33-filter-sort-unique",
        "category": "data",
        "date": "April 21, 2027",
        "summary": "Copying rows into a new tab every time someone asks for a list makes a copy that is out "
                   "of date by the afternoon. This part shows how FILTER, SORT and UNIQUE in Google Sheets "
                   "build lists that update themselves, how to combine them, and how to handle the two errors "
                   "beginners meet first.",
        "publish_on": "2027-04-21 21:00",
        "body": [
            "Every Monday, the budget officer asked for the same thing: last week’s business tax payments of "
            "₱5,000 or more, largest first. Every Monday, the clerk filtered the payments log, copied the "
            "rows, pasted them into a new tab, sorted them and sent the file. By Tuesday, three late entries "
            "had been added to the log, and the copy was already wrong.",
            "The clerk did not need a new copy each week. She needed one formula that would keep the list "
            "current by itself.",
            "(The office, the barangays and the payments in this post are invented for practice. No real "
            "taxpayer or office is described.)",
            "Part 32 explained why rounded totals do not always add up. This part returns to everyday "
            "spreadsheet work. Part 22 showed how to sort and filter by hand. Here you will learn three "
            "functions that do the same thing with a formula, so the result changes when the data changes: "
            "FILTER, SORT and UNIQUE. You will also learn how to combine them, how to point them at a cell "
            "instead of typing the condition, and how to deal with the #N/A and #REF! errors.",
            ("photo", "blog/data-filter.jpg", "FILTER, SORT and UNIQUE: formulas that keep a list current, "
             "so nobody has to copy and paste it again. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "The Practice Sheet"),
            "Type this payments log into a new sheet, starting in cell A1. Column A is the date, B the "
            "barangay, C the kind of payment, D the amount and E the collector.",
            ("point", "Row 1", "Date, Barangay, Kind, Amount, Collector."),
            ("point", "Row 2", "January 4, 2027, Poblacion, RPT, 3200, Ana."),
            ("point", "Row 3", "January 4, 2027, San Isidro, Business, 8500, Ben."),
            ("point", "Row 4", "January 5, 2027, Poblacion, Business, 12000, Ana."),
            ("point", "Row 5", "January 5, 2027, Malinao, RPT, 1450, Carlo."),
            ("point", "Row 6", "January 6, 2027, San Isidro, Fees, 600, Ben."),
            ("point", "Row 7", "January 6, 2027, Poblacion, Fees, 350, Ana."),
            ("point", "Row 8", "January 7, 2027, Malinao, Business, 5000, Carlo."),
            ("point", "Row 9", "January 7, 2027, San Isidro, RPT, 2750, Ben."),
            "Put each formula below in an empty area to the right, such as cell H2, with nothing below or "
            "beside it. These functions fill as many cells as the result needs.",
            ("h", "UNIQUE: One of Each"),
            "Google’s help gives the form UNIQUE(range, by_column, exactly_once). For a simple list, you need "
            "only the range.",
            ("point", "Formula", "=UNIQUE(B2:B9)"),
            ("point", "Result", "Poblacion, San Isidro and Malinao, each once, in the order they first "
             "appear."),
            ("point", "Exactly once", "=UNIQUE(B2:B9, FALSE, TRUE) lists only values that appear a single "
             "time. In this log, none do, so the result is empty."),
            "Google’s help adds a warning worth remembering: if values that look the same still appear "
            "twice, check for hidden differences such as extra spaces at the end. Part 18 showed how TRIM "
            "removes them.",
            ("h", "SORT: The Same Rows in a New Order"),
            "The form is SORT(range, sort_column, is_ascending). The sort column can be a number counting "
            "from the left of the range. TRUE sorts low to high, FALSE high to low.",
            ("point", "Formula", "=SORT(A2:E9, 4, FALSE)"),
            ("point", "Result", "All eight rows, largest amount first: ₱12,000, ₱8,500, ₱5,000, ₱3,200, "
             "₱2,750, ₱1,450, ₱600 and ₱350."),
            ("point", "Two sort keys", "=SORT(A2:E9, 2, TRUE, 4, FALSE) sorts by barangay first, then by "
             "amount from largest to smallest within each barangay."),
            "Unlike sorting with the menu, SORT leaves the original log untouched. The sorted list is a "
            "view of the data, not a second copy.",
            ("h", "FILTER: Only the Rows You Want"),
            "The form is FILTER(range, condition1, condition2, and so on). Each condition is a column of "
            "TRUE or FALSE values, one for each row of the range.",
            ("point", "One condition", "=FILTER(A2:E9, B2:B9=\"Poblacion\") returns rows 2, 4 and 7."),
            ("point", "Two conditions", "=FILTER(A2:E9, B2:B9=\"Poblacion\", D2:D9>=5000) returns row 4 "
             "only. A row must pass every condition."),
            ("point", "Same length", "Google’s help says each condition must have exactly the same length "
             "as the range. B2:B9 matches A2:E9; B2:B10 would not."),
            ("h", "Putting Them Together"),
            "The real strength comes from nesting one function inside another. The budget officer’s Monday "
            "request becomes a single formula.",
            ("point", "Formula", "=SORT(FILTER(A2:E9, C2:C9=\"Business\", D2:D9>=5000), 4, FALSE)"),
            ("point", "Result", "₱12,000 from Poblacion, ₱8,500 from San Isidro and ₱5,000 from Malinao, "
             "largest first."),
            ("point", "Read it from the inside out", "FILTER keeps business payments of ₱5,000 or more. SORT "
             "puts what is left in order by column 4, the amount."),
            ("photo", "blog/data-filter-results.jpg", "One log, three formulas, three lists that update "
             "themselves when a new payment is entered. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "FILTER or a Pivot Table?"),
            "Part 24 used pivot tables to summarize. The two tools answer different questions.",
            ("point", "Use FILTER and SORT for rows", "When the reader needs the actual payments: who paid, "
             "when and how much."),
            ("point", "Use a pivot table for totals", "When the reader needs sums or counts by barangay, kind "
             "or month, and not the rows behind them."),
            "The budget officer wanted the payments themselves, so FILTER was the right choice.",
            ("h", "Point the Formula at a Cell"),
            "Typing “Poblacion” into the formula means editing the formula for every new question. Put the "
            "condition in a cell instead.",
            ("point", "Set it up", "Type Poblacion in cell G1. Then use =FILTER(A2:E9, B2:B9=G1)."),
            ("point", "Change the question", "Type San Isidro in G1, and the list changes at once."),
            ("point", "Add a dropdown", "Part 12 showed data validation. A dropdown in G1, built from the "
             "UNIQUE list, lets anyone choose a barangay without typing errors."),
            ("h", "Let the List Grow"),
            "A fixed range such as A2:E9 stops at row 9. When the log grows, use an open range that runs to "
            "the bottom of the column, such as A2:E and B2:B.",
            ("point", "FILTER with open ranges", "=FILTER(A2:E, B2:B=G1) picks up every new row as it is "
             "entered."),
            ("point", "UNIQUE with open ranges", "=UNIQUE(B2:B) also counts the empty rows below the data, "
             "so the result ends with a blank. Filter the blanks out first: "
             "=UNIQUE(FILTER(B2:B, B2:B<>\"\"))."),
            ("h", "The Two Errors You Will Meet First"),
            ("point", "#N/A: nothing matched", "Google’s help says FILTER returns #N/A when no values meet "
             "the conditions. Wrap it to show a message instead: =IFERROR(FILTER(A2:E9, B2:B9=G1), "
             "\"No payments\")."),
            ("point", "#REF!: no room", "These formulas need empty cells to spill into. If something is "
             "typed in their way, the result stops with #REF!, and the message says the result would "
             "overwrite data. Clear the blocking cell, or move the formula."),
            "One more caution: do not type over the cells a formula filled. They belong to the formula. To "
            "change the result, change the data or the condition.",
            ("quote", "A copied list is right once. A formula list is right every time it is opened."),
            ("h", "Mistakes to Avoid"),
            ("point", "Copying and pasting a weekly list", "Use FILTER and SORT once, and reuse them."),
            ("point", "Conditions of a different length", "Match the rows of the range exactly."),
            ("point", "Typing the condition into the formula", "Point it at a cell instead."),
            ("point", "Leaving no room below", "Keep the space under and beside the formula empty."),
            ("h", "Key Takeaways"),
            ("point", "UNIQUE lists each value once", "Watch for hidden spaces."),
            ("point", "SORT orders without touching the log", "Use FALSE for largest first."),
            ("point", "FILTER keeps the rows you want", "Every condition must be true."),
            ("point", "Nest them", "SORT(FILTER(...)) answers a whole request in one formula."),
            ("h", "Your Part 33 Exercise"),
            ("point", "Step 1", "Build the practice sheet and try each formula above."),
            ("point", "Step 2", "Add a tenth row: January 8, 2027, Poblacion, Business, 7000, Ana. Watch "
             "which lists change on their own."),
            ("point", "Step 3", "Put a barangay name in G1 and build =IFERROR(FILTER(A2:E, B2:B=G1), "
             "\"No payments\")."),
            ("point", "Step 4", "Find one list in your office that someone copies by hand every week, and "
             "rebuild it as a formula."),
            "The next Monday, the clerk sent the budget officer a link instead of a file. The tab held one "
            "formula. When the officer opened it on Tuesday, the three late entries were already there.",
            ("cta", "Read: Data Analytics Series, Part 22: Sorting and Filtering With Purpose", "/blog/data-analytics-part-22-sorting-and-filtering/"),
            ("cta", "Read: Data Analytics Series, Part 23: SUMIFS, COUNTIFS and AVERAGEIFS", "/blog/data-analytics-part-23-sumifs-countifs-averageifs/"),
            ("cta", "Read: Data Analytics Series, Part 12: Spreadsheets Done Right, One Row per Record", "/blog/data-analytics-part-12-one-row-per-record/"),
            ("cta", "Read: Data Analytics Series, Part 31: Conditional Formatting, Letting the Sheet Point at the Problems", "/blog/data-analytics-part-31-conditional-formatting/"),
            ("ask", "Which list in your office is still copied and pasted by hand every week?"),
        ],
    },
    {
        "title": "Data Analytics Series, Part 32: Rounding, and Why the Totals Don’t Add Up",
        "slug": "data-analytics-part-32-rounding-and-totals",
        "category": "data",
        "date": "April 16, 2027",
        "summary": "A report can be correct and still show shares that add up to 101 percent, or a peso "
                   "total that does not match its rows. This part explains where rounding differences come from, "
                   "how to fix a split so it adds to the centavo, how Google Sheets and Python round "
                   "halves differently, and how to tell readers what they are looking at.",
        "publish_on": "2027-04-16 21:00",
        "body": [
            "The council member held up the quarterly report and pointed at the pie chart. “Real property "
            "tax, 43 percent. Business tax, 32 percent. Fees, 26 percent. That is 101 percent,” he said. "
            "“Where did the extra one percent come from?”",
            "The analyst checked the sheet that night. Nothing was missing and nothing was counted twice. "
            "Every number in the report was right. The problem was rounding, and the report had not said so.",
            "(The council meeting and the figures are invented for this lesson. The rounding rules described "
            "for Google Sheets and Python come from their official documentation.)",
            "Part 30 showed how to report change without confusing percent and percentage points. This part "
            "deals with a smaller problem that can cause just as many questions: totals that don’t match "
            "their parts. You will learn why it happens, how to split an amount so the pieces add up to the "
            "centavo, why the same number can round differently in two tools, and what to write in a report "
            "so readers are not left guessing.",
            ("photo", "blog/data-rounding.jpg", "Rounding: each part is rounded on its own, so the parts "
             "can miss the total by a little. Fix the split, or say so in a note. (Illustration: Butch "
             "Mahinay, aumahinay.dev)", "medium"),
            ("h", "Why Rounded Parts Miss the Total"),
            "Rounding moves each number a little up or down. When you round each part separately, those "
            "small moves can add up instead of cancelling out.",
            ("point", "The percent example", "Collections for the quarter were ₱10,000,000: ₱4,260,000 in "
             "real property tax, ₱3,170,000 in business tax and ₱2,570,000 in fees. The exact shares are "
             "42.6, 31.7 and 25.7 percent, which add to exactly 100. Rounded to whole numbers, they become "
             "43, 32 and 26, which add to 101. Each one was rounded up, and the three small moves did not "
             "cancel out."),
            ("point", "The peso example", "A table shows amounts in thousands with no decimals. Two "
             "offices collected ₱1,234,400 and ₱2,345,400, which display as 1,234 and 2,345. The total, "
             "₱3,579,800, displays as 3,580. A reader who adds the two rows gets 3,579."),
            "Neither report is wrong. The total was computed from the full amounts, and then each number was "
            "rounded for display. The parts and the total were rounded separately, and that is where the "
            "difference comes from.",
            ("photo", "blog/data-rounding-table.jpg", "Two ways rounding shows up in a report: shares that add "
             "to 101 percent, and a total one more than its rows. Figures are invented. (Illustration: Butch "
             "Mahinay, aumahinay.dev)", "medium"),
            ("h", "Display Rounding vs Stored Rounding"),
            "Spreadsheets round in two different ways, and it helps to know which one you are using.",
            ("point", "Display rounding", "Changing the number format, or clicking the button that removes "
             "decimals, changes only what you see. The cell still holds the full value, and formulas that "
             "use it work with the full value."),
            ("point", "Stored rounding", "A formula such as =ROUND(A2, 2) produces a new value rounded to "
             "two decimals. Formulas that use it work with the rounded value."),
            "Display rounding is what produces the 3,579 and 3,580 puzzle: the total adds the full values, "
            "and the screen shows the rounded ones. Stored rounding is what you need when the rounded amount "
            "is the real amount, such as a peso figure that will be printed on a receipt or a check.",
            ("h", "Splitting an Amount So It Adds Up"),
            "Treasury work has several kinds of splits: a fund divided among barangays, a payment allocated across "
            "accounts, a share computed for each office. Here the parts must add up exactly, because each "
            "part becomes a real amount of money.",
            ("point", "The problem", "Divide ₱1,000.00 equally among three barangays. Each exact share is "
             "₱333.333…, which rounds to ₱333.33. Three of those add up to ₱999.99. One centavo is missing."),
            ("point", "The remainder fix", "Round all the shares except the last. Compute the last one as "
             "the total minus the others: ₱1,000.00 − ₱333.33 − ₱333.33 = ₱333.34. Now the shares add up "
             "to ₱1,000.00 exactly."),
            ("point", "In Google Sheets", "If the total is in B1 and the shares are in B2 to B4, put "
             "=ROUND($B$1/3, 2) in B2 and B3, and =B1-SUM(B2:B3) in B4. Then add a check cell, "
             "=SUM(B2:B4)=B1, which should say TRUE."),
            ("point", "Decide who gets the extra centavo", "The remainder fix gives it to the last line. "
             "If the order matters, write down the rule, for example “the largest share absorbs the "
             "difference,” and use it every time."),
            "The check cell is easy to skip, but it is the most useful part. If someone later types a number "
            "over the formula in the last share, the check turns FALSE before the numbers go out.",
            ("h", "Same Number, Two Answers: How Halves Are Rounded"),
            "The trickiest case is a number exactly halfway, such as 2.5. Not every tool treats it the same.",
            ("point", "Google Sheets", "Its help page says ROUND works “according to standard rules”: a 5 "
             "in the next place rounds up. =ROUND(2.5, 0) gives 3."),
            ("point", "Python", "The built-in round() rounds halves to the nearest even number. round(2.5) "
             "gives 2, and round(3.5) gives 4. This is sometimes called banker’s rounding."),
            ("point", "Hidden decimals", "Computers store numbers such as 2.675 as close binary "
             "approximations. Python’s documentation gives the example round(2.675, 2), which returns 2.67, "
             "not 2.68, because 2.675 is stored as a value slightly below it."),
            "For peso amounts in Python, the decimal module avoids both surprises. Decimal(\"2.675\") "
            "quantized to two places with ROUND_HALF_UP gives 2.68, the answer taught in school. The "
            "lesson for an analyst is simple: if two tools disagree by a centavo, check how each one rounds "
            "before assuming a mistake in the data.",
            ("h", "Telling the Reader"),
            "Sometimes the right answer is not to change the numbers but to explain them.",
            ("point", "Add a note", "A short line under the table or chart, such as “Figures may not add "
             "up to the total because of rounding,” answers the question before anyone asks it."),
            ("point", "Show one more decimal", "In the percent example, one decimal place, 42.6, 31.7 and "
             "25.7, adds up to exactly 100.0. Part 30 also suggested one decimal place, to keep a report "
             "readable."),
            ("point", "Don’t force a share", "Changing 43 to 42 so the chart adds to 100 makes one number "
             "wrong to make the total look right. If you use a method that adjusts shares, say so in the note."),
            ("quote", "A rounding note costs one line. A council member’s doubt about the whole report "
             "costs much more."),
            ("h", "Mistakes to Avoid"),
            ("point", "Hunting for a missing amount that isn’t missing", "Check rounding first when the "
             "difference is one unit of the last digit shown."),
            ("point", "Rounding every share in a split", "Use the remainder fix so the parts add up."),
            ("point", "Assuming tools round the same way", "Sheets and Python treat halves differently."),
            ("point", "Leaving readers to guess", "Add a rounding note under the table."),
            ("h", "Key Takeaways"),
            ("point", "Rounded parts can miss the total", "Each part moves a little on its own."),
            ("point", "Display is not storage", "Formatting hides decimals; ROUND changes the value."),
            ("point", "Splits need the remainder fix", "Plus a check cell that says TRUE."),
            ("point", "Explain it", "One note, or one more decimal place."),
            ("h", "Your Part 32 Exercise"),
            ("point", "Step 1", "In a new sheet, put 1000 in B1. Put =ROUND($B$1/3, 2) in B2, B3 and B4, "
             "and =SUM(B2:B4) in B5. You should see 999.99."),
            ("point", "Step 2", "Change B4 to =B1-SUM(B2:B3). B5 should now show 1000."),
            ("point", "Step 3", "Add =SUM(B2:B4)=B1 in B6 and confirm it says TRUE. Try typing 333.35 into B4, "
             "replacing its formula, and watch the check turn FALSE. Then undo."),
            ("point", "Step 4", "Find one table in your last report that shows percentages, add them up, and "
             "decide whether it needs a rounding note."),
            "The next quarterly report had the same pie chart, with one difference: the shares showed one "
            "decimal place, and a line underneath said the figures may not add up to the total because of "
            "rounding. The council member read it, nodded, and moved on to his next question.",
            ("cta", "Read: Data Analytics Series, Part 30: Percent Change or Percentage Points? Reporting Growth Without Confusion", "/blog/data-analytics-part-30-percent-change/"),
            ("cta", "Read: Data Analytics Series, Part 23: SUMIFS, COUNTIFS and AVERAGEIFS", "/blog/data-analytics-part-23-sumifs-countifs-averageifs/"),
            ("cta", "Read: Data Analytics Series, Part 16: Dirty Data, the Usual Suspects and How to Spot Them", "/blog/data-analytics-part-16-dirty-data/"),
            ("cta", "Read: Data Analytics Series, Part 8: Metrics and KPIs That Tell the Truth", "/blog/data-analytics-part-8-metrics-and-kpis/"),
            ("ask", "Has a report of yours ever been questioned over a total that was off by one?"),
        ],
    },
    {
        "date": "April 11, 2027",
        "title": "Data Analytics Series, Part 31: Conditional Formatting, Letting the Sheet Point at the Problems",
        "slug": "data-analytics-part-31-conditional-formatting",
        "category": "data",
        "summary": "A long list hides the three rows that need attention. This part uses conditional "
                   "formatting in Google Sheets to color unpaid accounts, late payments and duplicate entries "
                   "automatically, explains custom formulas and the dollar sign, and shows how rule order "
                   "decides which color wins.",
        "publish_on": "2027-04-11 21:00",
        "body": [
            "On the first working day of February, the head of office asked a simple question: which "
            "business permit renewals due on January 20 were still unpaid? The clerk opened the log. It had "
            "hundreds of rows. She sorted by the paid date, scrolled, filtered, and twenty minutes later had "
            "a list on a sticky note. By the afternoon, two more people had paid, and the sticky note was "
            "already wrong.",
            "The sheet could have answered the question by itself, in color, every time it was opened.",
            "(The office, the accounts and the amounts in this post are invented for practice. No real "
            "taxpayer or office is described.)",
            "Part 30 reported changes in percent and in points. This part makes problems visible before "
            "anyone asks. You will learn what conditional formatting does in Google Sheets, how to set a "
            "simple rule, how to write a custom formula that colors a whole row, how to catch duplicate "
            "entries, why the order of rules matters, and when color helps and when it gets in the way.",
            ("photo", "blog/data-format.jpg", "Conditional formatting: one rule per question, whole rows "
             "colored, the most important rule first, and a legend readers can see. (Illustration: Butch "
             "Mahinay, aumahinay.dev)", "medium"),
            ("h", "What Conditional Formatting Does"),
            "Conditional formatting changes the look of a cell, such as its fill color or text color, when "
            "the cell meets a condition you set. The data does not change. Only its appearance does, and "
            "it updates as the data changes.",
            ("point", "It answers a standing question", "“Which accounts are unpaid?” is asked every month. "
             "A rule answers it every time the sheet is opened."),
            ("point", "It keeps up with edits", "When a payment is entered, the red row turns back to normal "
             "without anyone touching the formatting."),
            ("point", "It does not replace a filter", "Color shows where problems are. To count or list them, "
             "you still need COUNTIFS or a filter, as in Parts 22 and 23."),
            ("h", "The Practice Sheet"),
            "Type this small log into a new sheet, starting in cell A1. Column A is the account, B the due "
            "date, C the date paid (blank if unpaid) and D the amount.",
            ("point", "Row 1", "Account, Due date, Paid date, Amount."),
            ("point", "Row 2", "B-101, January 20, 2027, January 18, 2027, ₱2,500."),
            ("point", "Row 3", "B-102, January 20, 2027, blank, ₱3,200."),
            ("point", "Row 4", "B-103, January 20, 2027, January 25, 2027, ₱1,800."),
            ("point", "Row 5", "B-104, January 20, 2027, January 20, 2027, ₱4,100."),
            ("point", "Row 6", "B-105, January 20, 2027, blank, ₱2,900."),
            ("point", "Row 7", "B-101, January 20, 2027, January 18, 2027, ₱2,500. This is the same "
             "payment typed twice, the kind of error Part 16 called a usual suspect."),
            ("h", "Step 1: Open the Panel"),
            "Select the range A2:D7. Click Format, then Conditional formatting. A panel opens on the right. "
            "Under “Format cells if,” choose a condition, then choose a formatting style below it.",
            "The simple conditions, such as “Less than” or “Text contains,” test each cell on its own. They "
            "are fine for one column. To color a whole row based on one column, you need a custom formula.",
            ("h", "Step 2: Color Unpaid Accounts Past Due"),
            "Choose “Custom formula is” and type:",
            ("point", "Formula", "=AND($C2=\"\", $B2<TODAY())"),
            ("point", "What it says", "The paid date is blank, and the due date is before today."),
            ("point", "The style", "A light red fill."),
            "On February 1, 2027, rows 3 and 6, accounts B-102 and B-105, turn red. When B-105 pays and the "
            "date is typed in C6, that row returns to normal by itself.",
            ("h", "Why the Dollar Sign Matters"),
            "The formula is written for the first row of the range, row 2, and Sheets moves it down for each "
            "row. The dollar sign controls what moves.",
            ("point", "$C2", "The column is locked to C, but the row changes: C2, C3, C4 and so on. Every "
             "cell in a row looks at that row’s column C, so the whole row gets the same color."),
            ("point", "C2 without the dollar sign", "The column would also shift as Sheets moves across the "
             "row: cell A2 would look at C2, but B2 would look at D2 and D2 at F2. Only part of the row would "
             "follow the rule."),
            ("point", "$A$2:$A$7", "Both locked. Every row looks at the same full range, which is what a "
             "duplicate check needs."),
            ("h", "Step 3: Color Late Payments"),
            "Click “Add another rule,” choose “Custom formula is,” and type:",
            ("point", "Formula", "=AND($C2<>\"\", $C2>$B2)"),
            ("point", "What it says", "There is a paid date, and it is after the due date."),
            ("point", "The style", "A light orange fill. Row 4, account B-103, paid on January 25, turns "
             "orange."),
            "The first part, $C2<>\"\", keeps blank paid dates out of this rule. They belong to the red rule.",
            ("h", "Step 4: Catch Duplicates"),
            "Add a third rule with this custom formula, the pattern shown on Google’s help page for "
            "highlighting duplicates:",
            ("point", "Formula", "=COUNTIF($A$2:$A$7, $A2)>1"),
            ("point", "What it says", "This account appears more than once in the list."),
            ("point", "The style", "A light purple fill. Rows 2 and 7, both B-101, turn purple."),
            ("h", "Step 5: Put the Rules in Order"),
            "Google’s help page says rules are evaluated in the order listed, and the first rule that is true "
            "decides the format. You can drag rules up or down in the panel.",
            ("point", "Put the most important rule first", "A duplicate can make a total wrong, so this "
             "office put the duplicate rule at the top."),
            ("point", "Then the urgent one", "Unpaid and past due came second."),
            ("point", "Then the informative one", "Paid late came third."),
            "With this order, row 7 shows purple even if someone later clears its paid date. The duplicate "
            "is fixed first, and the payment status is checked after.",
            ("photo", "blog/data-format-sheet.jpg", "The practice sheet on February 1, 2027, with all three rules "
             "applied in order. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "A Color Scale for Amounts"),
            "For numbers, a color scale can shade cells from light to dark by size. Select D2:D7, open the "
            "panel, choose the “Color scale” tab, and set the minimum and maximum colors. The largest "
            "amounts stand out without a rule for each.",
            "Use a scale for size, and single colors for status. Mixing many scales and colors on one sheet "
            "makes it harder to read, not easier.",
            ("h", "Keep Color Readable"),
            ("point", "Add a legend", "A line above the table: “Purple: duplicate. Red: unpaid, past due. "
             "Orange: paid late.” A color without a meaning is decoration."),
            ("point", "Do not rely on color alone", "Part 26 of the Business Intelligence Series explained "
             "that some readers cannot tell red from green. Light fills plus a legend, or a status column "
             "with words, keep the meaning clear."),
            ("point", "Use few colors", "Three statuses, three colors. Every extra color asks the reader to "
             "learn one more thing."),
            ("h", "Mistakes to Avoid"),
            ("point", "Forgetting the dollar sign", "Write $C2, not C2, when a rule should color a whole row."),
            ("point", "Writing the formula for the wrong row", "Write it for the first row of the selected "
             "range."),
            ("point", "Ignoring rule order", "The first true rule wins. Drag the most important to the top."),
            ("point", "Color with no legend", "Say what each color means, in words."),
            ("h", "Key Takeaways"),
            ("point", "Format, then Conditional formatting", "Rules change the look, not the data."),
            ("point", "Custom formulas color whole rows", "Lock the column with a dollar sign."),
            ("point", "COUNTIF finds duplicates", "=COUNTIF($A$2:$A$7, $A2)>1."),
            ("point", "Order decides", "The first rule that is true sets the format."),
            ("h", "Your Part 31 Exercise"),
            "Build the practice sheet, then try these.",
            ("point", "Add the three rules", "Red for unpaid and past due, orange for late, purple for "
             "duplicates."),
            ("point", "Test them", "Type a paid date into C3, then clear C2. Watch the colors change."),
            ("point", "Use your own log", "Pick one list in your office that someone checks by scrolling, and "
             "give it one rule that answers that person’s question."),
            "The next month, the clerk opened the log on the first working day and sent the head of office a "
            "screenshot of the red rows before she was asked. Two of them were paid by noon. Nobody needed a "
            "sticky note.",
            ("cta", "Read: Data Analytics Series, Part 30: Percent Change or Percentage Points? Reporting Growth Without Confusion", "/blog/data-analytics-part-30-percent-change/"),
            ("cta", "Read: Data Analytics Series, Part 29: Counting Days in Google Sheets, Working Days, Due Dates and Days Late", "/blog/data-analytics-part-29-counting-days/"),
            ("cta", "Read: Data Analytics Series, Part 23: SUMIFS, COUNTIFS and AVERAGEIFS", "/blog/data-analytics-part-23-sumifs-countifs-averageifs/"),
            ("cta", "Read: Business Intelligence Series, Part 26: Colors Everyone Can Read, Contrast, Labels and the Red-Green Trap", "/blog/business-intelligence-part-26-accessible-colors/"),
            ("ask", "Which list in your office would be easier to check if the problems lit up by themselves?"),
        ],
    },
    {
        "date": "April 6, 2027",
        "title": "Data Analytics Series, Part 30: Percent Change or Percentage Points? Reporting Growth Without Confusion",
        "slug": "data-analytics-part-30-percent-change",
        "category": "data",
        "summary": "Collection efficiency rose from 72 to 81 percent. Is that a 9 percent increase or a 12.5 "
                   "percent one? This part separates percent change from percentage points, shows the "
                   "formulas in Google Sheets, and covers the small-base, reverse-change and averaging traps "
                   "that make honest numbers mislead.",
        "publish_on": "2027-04-06 21:00",
        "body": [
            "The draft press release said: “Real property tax collection efficiency rose 9 percent this "
            "year.” The budget officer read it and disagreed. “It went from 72 to 81. That is 12.5 percent.” "
            "The analyst who wrote it said both were right. The head of office asked which one would be "
            "printed, because a councilor would certainly check.",
            "They were both right, about different things. The sentence was wrong because it did not say "
            "which.",
            "(The office, the press release and every figure below are invented for this lesson. No real "
            "town is described.)",
            "Part 29 counted days. This part counts change. When you finish, you will know the difference "
            "between percent change and percentage points, how to compute each in Google Sheets, how to "
            "write growth so nobody misreads it, how to avoid three traps: small bases, changes that do not "
            "reverse evenly, and averages of percentages, and how to describe growth over several years.",
            ("photo", "blog/data-percent.jpg", "Percent change or percentage points: change in an amount is a "
             "percent, change in a rate is in points, and the base always matters. (Illustration: Butch "
             "Mahinay, aumahinay.dev)", "medium"),
            ("h", "Two Ways to Describe a Change"),
            ("point", "Percent change", "How much an amount grew or shrank, relative to where it started. "
             "Collections of ₱8,400,000 rising to ₱9,240,000 is a change of ₱840,000, which is 10 percent of "
             "₱8,400,000."),
            ("point", "Percentage points", "The plain difference between two percentages. Efficiency rising "
             "from 72 percent to 81 percent is a rise of 9 percentage points."),
            ("point", "Percent change of a percentage", "The same efficiency figures, treated as amounts: "
             "9 divided by 72 is 0.125, a 12.5 percent increase."),
            "So the press release could say “up 9 percentage points” or “up 12.5 percent.” It could not say "
            "“up 9 percent,” which mixes the two.",
            ("photo", "blog/data-percent-points.jpg", "The same change, said two ways: from 72 to 81 percent is up 9 "
             "percentage points, or up 12.5 percent. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("quote", "When the thing you measure is already a percentage, say “points.”"),
            ("h", "The Formulas in Google Sheets"),
            "Put last year’s figure in B2 and this year’s in C2.",
            ("point", "Change in the amount", "=C2-B2. For collections, ₱840,000."),
            ("point", "Percent change", "=(C2-B2)/B2, then format the cell as a percentage with Format, "
             "Number, Percent. For collections, 10.0%."),
            ("point", "Percentage points", "If B2 and C2 hold 72% and 81%, =C2-B2 returns 9%, which you "
             "should label as 9 percentage points, not 9 percent."),
            ("point", "Guard against zero", "If last year was zero, the percent change divides by zero. "
             "=IFERROR((C2-B2)/B2, \"new\") shows “new” instead of an error."),
            ("h", "When to Use Which"),
            ("point", "Use percent change for amounts", "Pesos collected, number of taxpayers, receipts "
             "issued, days taken."),
            ("point", "Use percentage points for rates", "Collection efficiency, share of taxpayers who paid "
             "on time, share of permits released within target."),
            ("point", "Give both numbers when it matters", "“Efficiency rose from 72 percent to 81 percent, "
             "up 9 percentage points.” The reader sees the start, the end and the change, and can compute "
             "anything else."),
            ("h", "Trap 1: The Small Base"),
            "Percent change is relative to the start. When the start is small, the percent can be huge.",
            ("point", "An example", "A barangay’s business tax collections went from ₱2,000 to ₱6,000. That "
             "is a 200 percent increase, from one new store."),
            ("point", "The comparison", "Poblacion went from ₱800,000 to ₱900,000, a 12.5 percent increase, "
             "but ₱100,000 more in pesos, fifty times the small barangay’s ₱4,000 gain."),
            ("point", "The fix", "Show the amounts beside the percentages. A ranking by percent change alone "
             "will put the smallest base on top."),
            ("h", "Trap 2: Changes Do Not Reverse Evenly"),
            ("point", "Down, then up", "If a figure of ₱1,000 falls 50 percent, it becomes ₱500. If it then "
             "rises 50 percent, it becomes ₱750, not ₱1,000. The second 50 percent is taken from a smaller "
             "base."),
            ("point", "Why it matters", "After a bad year, a “recovery of 50 percent” may still leave "
             "collections below where they started. Compare with the original level, not only with last "
             "year."),
            ("h", "Trap 3: Averaging Percentages"),
            "Three barangays had these real property tax results against their targets:",
            ("point", "Poblacion", "Collected ₱1,800,000 of a ₱2,000,000 target: 90 percent."),
            ("point", "San Isidro", "Collected ₱450,000 of ₱500,000: 90 percent."),
            ("point", "San Roque", "Collected ₱40,000 of ₱100,000: 40 percent."),
            ("point", "The simple average", "(90 + 90 + 40) ÷ 3 is about 73.3 percent. It gives the "
             "smallest barangay the same weight as the largest."),
            ("point", "The overall rate", "Total collected over total target: ₱2,290,000 ÷ ₱2,600,000, "
             "about 88.1 percent. In Sheets, =SUM(collected)/SUM(target)."),
            "For the town’s efficiency, the overall rate is the right number. The simple average answers a "
            "different question: how a typical barangay did, regardless of size. Part 26 showed a similar "
            "choice between the mean and the median. Name which one you used.",
            ("h", "Growth Over Several Years"),
            "Suppose collections were ₱8,000,000 in 2024 and ₱9,680,000 in 2026. The total change over the "
            "two years is ₱1,680,000, or 21 percent.",
            ("point", "Do not just divide by the years", "21 percent ÷ 2 = 10.5 percent a year sounds right, "
             "but it ignores that the second year grew from a larger base."),
            ("point", "The average yearly rate", "In Sheets: =(C2/B2)^(1/2)-1, where 2 is the number of years. "
             "It returns 10 percent. Check it: ₱8,000,000 grown 10 percent is ₱8,800,000, and another 10 "
             "percent is ₱9,680,000."),
            ("point", "When to use it", "For a three- or five-year summary in a budget message or an annual "
             "report, where readers want one yearly figure."),
            "Say which one you report. “Up 21 percent over two years” and “up an average of 10 percent a "
            "year” are both true and easy to confuse.",
            ("h", "Writing Change Clearly"),
            ("point", "Always give the start and the end", "“From ₱8.4 million to ₱9.24 million” before "
             "“up 10 percent.”"),
            ("point", "Name the period", "“Compared with 2026” or “compared with the same month last year.” "
             "Part 19 of the Business Intelligence series covered fair comparisons."),
            ("point", "Say points for rates", "“Up 9 percentage points,” or simply “up 9 points” after the "
             "first mention."),
            ("point", "Round sensibly", "One decimal place keeps a report readable: 12.5 percent, not "
             "12.4999 percent."),
            ("point", "Check the direction", "A fall in “days to release a permit” is good news. Write “down "
             "from 4.2 to 2.6 working days,” and let the reader see it is an improvement."),
            ("h", "A Quick Check Before Publishing"),
            ("point", "Is it an amount or a rate?", "Percent change for amounts, points for rates."),
            ("point", "What is the base?", "If it is small, show the amounts too."),
            ("point", "Are percentages averaged?", "If so, compute the overall rate from totals instead, or "
             "say clearly that it is a simple average."),
            ("point", "Can a reader recompute it?", "Give the start, the end and the period."),
            ("h", "Mistakes to Avoid"),
            ("point", "Saying “percent” for a change in a rate", "Use percentage points."),
            ("point", "Ranking by percent change alone", "Small bases jump to the top."),
            ("point", "Expecting a rise to undo an equal fall", "Compare with the starting level."),
            ("point", "Averaging rates of different sizes", "Use totals for the overall rate."),
            ("h", "Key Takeaways"),
            ("point", "Amounts change by percent", "=(new-old)/old."),
            ("point", "Rates change by points", "=new rate minus old rate, labeled as points."),
            ("point", "The base matters", "Show amounts beside percentages."),
            ("point", "Overall rates come from totals", "Not from averaging the parts."),
            ("h", "Your Part 30 Exercise"),
            "Take two years of any figure your office reports, one amount and one rate.",
            ("point", "Compute both", "Percent change for the amount, percentage points for the rate."),
            ("point", "Rewrite one sentence", "Give the start, the end, the period and the change, with the "
             "right unit."),
            ("point", "Check an average", "Find one report that averages percentages, and recompute it from "
             "totals."),
            "Then read your sentence to a colleague and ask them to repeat the number back. If they say the "
            "same unit you wrote, the sentence works.",
            "The final press release read: “Real property tax collection efficiency rose from 72 percent "
            "to 81 percent, up 9 percentage points from last year.” The councilor checked it, found nothing "
            "to argue with, and asked about San Roque instead.",
            ("cta", "Read: Data Analytics Series, Part 29: Counting Days in Google Sheets, Working Days, Due Dates and Days Late", "/blog/data-analytics-part-29-counting-days/"),
            ("cta", "Read: Data Analytics Series, Part 26: Mean or Median? Choosing the Middle That Tells the Truth", "/blog/data-analytics-part-26-mean-or-median/"),
            ("cta", "Read: Data Analytics Series, Part 8: Metrics and KPIs That Tell the Truth", "/blog/data-analytics-part-8-metrics-and-kpis/"),
            ("cta", "Read: Business Intelligence Series, Part 19: Fair Comparisons, This Month, Last Month and Last Year", "/blog/business-intelligence-part-19-fair-comparisons/"),
            ("ask", "Which percentage in your office’s reports should really be written in points?"),
        ],
    },
    {
        "date": "April 1, 2027",
        "title": "Data Analytics Series, Part 29: Counting Days in Google Sheets, Working Days, Due Dates and Days Late",
        "slug": "data-analytics-part-29-counting-days",
        "category": "data",
        "summary": "How long did each application take, and when is the next one due? This part counts days "
                   "in Google Sheets with DAYS, NETWORKDAYS and WORKDAY, adds months with EDATE and EOMONTH, "
                   "handles holidays, and shows why calendar days and working days give different answers.",
        "publish_on": "2027-04-01 21:00",
        "body": [
            "The head of office wanted one number for the quarterly report: how many days, on average, it "
            "took to release a business permit after the papers came in. The clerk subtracted each received "
            "date from each release date and got an average of 4.2 days. The office’s own target was three "
            "working days. On paper, it looked late.",
            "Then the clerk looked at application A-03. It came in on a Friday and was released on Monday, "
            "the next working day. Her formula had counted Saturday and Sunday as three days of delay.",
            "(The office, the applications and the dates in this post are invented for practice. No real "
            "office or applicant is described.)",
            "Part 28 joined tables in SQL. This part returns to Google Sheets for a question that comes up whenever an office tracks applications or payments: how many days? When you finish, you will know the difference between calendar days and "
            "working days, how to count each in Sheets, how to add holidays, how to find a due date a number "
            "of working days or months away, and how to compute days late without mistakes.",
            ("photo", "blog/data-days.jpg", "Counting days in Sheets: DAYS for calendar days, NETWORKDAYS for "
             "working days, WORKDAY for due dates, and a holiday list everyone uses. (Illustration: Butch "
             "Mahinay, aumahinay.dev)", "medium"),
            ("h", "Why Working Days Matter"),
            "Government service targets can be written in working days. Republic Act No. 11032, the Ease "
            "of Doing Business and Efficient Government Service Delivery Act of 2018, sets maximum processing "
            "times of three working days for simple transactions, seven for complex ones and twenty for "
            "highly technical ones, as summarized by the law firm NDV Law. A report that measures in calendar "
            "days compares a working-day target with a number that includes weekends.",
            ("point", "Calendar days", "Every day counts: Saturdays, Sundays and holidays included."),
            ("point", "Working days", "Monday to Friday, minus the holidays you list."),
            ("point", "Pick one, and say which", "Label every column and every report line with the kind of "
             "day it counts."),
            ("quote", "A Friday-to-Monday release is one working day, not three."),
            ("h", "The Practice Data"),
            "In a new sheet, put the application number in column A, the date received in column B and the "
            "date released in column C, for five rows, A2 to C6. All dates are in January 2027.",
            ("point", "A-01", "Received Monday, January 4. Released Wednesday, January 6."),
            ("point", "A-02", "Received Thursday, January 7. Released Tuesday, January 12."),
            ("point", "A-03", "Received Friday, January 8. Released Monday, January 11."),
            ("point", "A-04", "Received Wednesday, January 13. Released Wednesday, January 20."),
            ("point", "A-05", "Received Friday, January 15. Released Tuesday, January 19."),
            "Type the dates as real dates, such as 2027-01-04, so Sheets stores them as dates and not as "
            "text. Part 18 showed how to check.",
            ("h", "Step 1: Calendar Days With DAYS"),
            ("point", "The formula", "In D2: =DAYS(C2, B2), then copy down. Google’s help describes DAYS as "
             "returning the number of days between two dates, with the end date first."),
            ("point", "The results", "2, 5, 3, 7 and 4 days. The total is 21, and the average is 4.2."),
            ("point", "Simple subtraction works too", "=C2-B2 gives the same answer, since Sheets stores "
             "dates as numbers. DAYS makes the order of the dates clearer to the next reader."),
            "These are the numbers that made the office look late. A-02 and A-04 each crossed a weekend, "
            "and A-03 and A-05 started on a Friday.",
            ("h", "Step 2: Working Days With NETWORKDAYS"),
            ("point", "The formula", "In E2: =NETWORKDAYS(B2, C2). Google’s help says it returns the number "
             "of net working days between two dates, and treats only Saturday and Sunday as the weekend."),
            ("point", "Both ends are counted", "Google’s page does not say whether the start and end dates "
             "count. Microsoft’s help for the same function in Excel gives an example: from October 1, 2012 "
             "to March 1, 2013, it returns 110 working days, which is only possible if both ends are "
             "counted. Check your own sheet with a test: =NETWORKDAYS of a Monday and the next Monday. If it "
             "returns 6, both ends are counted."),
            ("point", "Days taken, not days touched", "Counting both ends means a same-day release shows as "
             "1. To measure working days after the day of receipt, subtract one: =NETWORKDAYS(B2, C2) - 1."),
            ("point", "The results", "With the minus one: 2, 3, 1, 5 and 2 working days. The average is 2.6."),
            "Same applications, same dates. The average fell from 4.2 calendar days to 2.6 working days, "
            "and only A-04, at 5, missed a three-working-day target.",
            ("h", "Step 3: Add the Holidays"),
            "NETWORKDAYS takes an optional third argument: a range of dates to treat as holidays. Google’s "
            "help says it can be a range or an array of dates.",
            ("point", "Make a Holidays tab", "One column of dates, one per row, with a second column naming "
             "each one. For this practice, add Monday, January 18, 2027, as an invented local holiday."),
            ("point", "The formula", "=NETWORKDAYS(B2, C2, Holidays!A$2:A$20) - 1. The dollar signs keep the "
             "range fixed when you copy down."),
            ("point", "What changed", "A-04 drops from 5 to 4 working days, and A-05 from 2 to 1. The other "
             "three did not cross January 18, so they stay the same."),
            ("point", "One list for everyone", "Keep a single holiday list for the office, updated when "
             "holidays are proclaimed, and point every formula to it. Two lists can give two different "
             "answers."),
            ("h", "Step 4: Due Dates With WORKDAY"),
            "Counting backward from a release is half the job. The other half is knowing, on the day an "
            "application arrives, when it is due.",
            ("point", "The formula", "=WORKDAY(B2, 3, Holidays!A$2:A$20). Google’s help says WORKDAY "
             "calculates the end date after a number of working days, and also uses only Saturday and Sunday "
             "as the weekend."),
            ("point", "The result for A-04", "Received Wednesday, January 13. Three working days later, "
             "skipping the weekend and the January 18 holiday, is Tuesday, January 19."),
            ("point", "Put it in the log", "A due-date column filled in when the application is received "
             "lets the counter see, each morning, which ones are due today."),
            ("point", "Other weekends", "Google’s help notes that NETWORKDAYS.INTL and WORKDAY.INTL let you "
             "choose other weekend days, for an office that also works on Saturdays."),
            ("h", "Step 5: Months With EDATE and EOMONTH"),
            "Some deadlines are counted in months, not days.",
            ("point", "EDATE", "Google’s help says it returns a date a number of months before or after "
             "another date. =EDATE(DATE(2027,1,15), 3) returns April 15, 2027."),
            ("point", "EOMONTH", "It returns the last day of a month a number of months before or after a "
             "date. =EOMONTH(DATE(2027,1,15), 0) returns January 31, 2027, and with 2 instead of 0, March 31, "
             "2027: the end of the first quarter."),
            ("point", "A use in the treasury", "Monthly reports due on the last day of the month, quarter-end "
             "cutoffs for a summary, or a follow-up letter three months after a notice."),
            ("h", "Step 6: Days Late"),
            "For a payment, the question is how many days after the due date it came in.",
            ("point", "The formula", "=MAX(0, DAYS(paid_date, due_date)). A payment on or before the due "
             "date returns 0, not a negative number."),
            ("point", "An example", "Due January 20, 2027, paid February 8, 2027: =DAYS(DATE(2027,2,8), "
             "DATE(2027,1,20)) returns 19 calendar days."),
            ("point", "Follow the rule that applies", "Whether lateness is counted in days, working days or "
             "months depends on the ordinance or rule behind the charge. The formula should follow that rule, "
             "not the other way around."),
            ("h", "Mistakes to Avoid"),
            ("point", "Comparing calendar days with a working-day target", "Use NETWORKDAYS for working-day targets."),
            ("point", "Forgetting that both ends count", "Subtract one when you mean days after receipt."),
            ("point", "Each person keeping their own holiday list", "One list, one range, every formula."),
            ("point", "Dates stored as text", "Check before you count, or the formulas return errors or wrong numbers."),
            ("h", "Key Takeaways"),
            ("point", "DAYS", "Calendar days between two dates, end date first."),
            ("point", "NETWORKDAYS", "Working days, counting both ends, with an optional holiday list."),
            ("point", "WORKDAY", "The due date a number of working days ahead."),
            ("point", "EDATE and EOMONTH", "Dates a number of months away, and month-ends."),
            ("h", "Your Part 29 Exercise"),
            "Type the five practice applications into a new sheet.",
            ("point", "Count both ways", "Add a DAYS column and a NETWORKDAYS minus one column, and compare "
             "the averages."),
            ("point", "Add a holiday", "Make a Holidays tab, add one date inside the range, and watch which "
             "rows change."),
            ("point", "Add due dates", "Use WORKDAY to compute a three-working-day due date for each one, and "
             "mark the ones released after it."),
            "Then take one real log from your office, and ask which kind of day its target is written in. "
            "If the report and the target use different days, fix the report first.",
            "The clerk rebuilt the column with NETWORKDAYS and the office holiday list, and labeled it "
            "“Working days after receipt.” The quarterly report showed an average of 2.6, one application "
            "over target, and the reason for it. The head of office asked for the same column on every log "
            "from then on.",
            ("cta", "Read: Data Analytics Series, Part 18: Taming Text and Dates, Names, Pesos and Day-Month Puzzles", "/blog/data-analytics-part-18-text-and-dates/"),
            ("cta", "Read: Data Analytics Series, Part 26: Mean or Median? Choosing the Middle That Tells the Truth", "/blog/data-analytics-part-26-mean-or-median/"),
            ("cta", "Read: Data Analytics Series, Part 23: SUMIFS, COUNTIFS and AVERAGEIFS", "/blog/data-analytics-part-23-sumifs-countifs-averageifs/"),
            ("cta", "Read: Data Analytics Series, Part 8: Metrics and KPIs That Tell the Truth", "/blog/data-analytics-part-8-metrics-and-kpis/"),
            ("ask", "Is your office’s service target written in calendar days or working days, and does the report match it?"),
        ],
    },
    {
        "date": "March 27, 2027",
        "title": "Data Analytics Series, Part 28: SQL Joins, Finding Who Is Missing and Why Totals Double",
        "slug": "data-analytics-part-28-sql-joins",
        "category": "data",
        "summary": "Part 19 joined two tables to get totals by barangay. This part goes further: the "
                   "difference between an inner join and a left join, how to list taxpayers with no "
                   "receipts, why a condition in the wrong place hides them again, and how a join can "
                   "quietly double a total.",
        "publish_on": "2027-03-27 21:00",
        "body": [
            "The head of office wanted a simple list: every registered business and how much each one paid "
            "this year. The analyst joined the taxpayers table to the receipts table, grouped by taxpayer, "
            "and printed the result. Four businesses, four totals. The head of office counted the folders "
            "on the shelf. “We have five registered businesses in this sample. Where is Lim Trading?”",
            "Lim Trading had not paid anything. And because it had not paid, the query had left it out, "
            "without a word. The one taxpayer the head of office most needed to see was the one the report "
            "could not show.",
            "(A made-up office and made-up figures, built for this lesson. No real business or taxpayer is "
            "described.)",
            "In Part 19, a JOIN brought the barangay from the taxpayers table into a total of receipts. "
            "This part looks closely at how joins decide which rows to keep. By the end, you will know "
            "the difference between an inner join and a left join, how to list who has no matching record, "
            "where to put a date condition so it does not hide anyone, and how to catch a join that "
            "counts the same money twice. Every result below was checked by running the queries in SQLite.",
            ("photo", "blog/data-joins.jpg", "SQL joins: an inner join keeps only matches, a left join "
             "keeps everyone, IS NULL finds who is missing, and a check total catches double counting. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "The Sample Tables"),
            "The tables are the ones from Part 19, with one taxpayer added.",
            ("point", "taxpayers", "Five businesses: T-00125 Ramos Bakery, T-00140 Cruz Store and T-00152 "
             "Dela Rosa Eatery in Poblacion, T-00131 Santos Hardware in San Isidro, and the new one, "
             "T-00163 Lim Trading in San Roque."),
            ("point", "receipts", "The same six receipts, 004512 to 004517, totaling 8,150. Ramos Bakery "
             "paid twice, Santos Hardware paid twice, and Cruz Store and Dela Rosa Eatery paid once each. "
             "Lim Trading has no receipt."),
            ("point", "contacts", "A third table, added later in this post: phone numbers, one row per "
             "number. Ramos Bakery has two numbers on file and Santos Hardware has one."),
            ("quote", "A join answers two questions at once: what matches, and what to do with what does "
             "not. Only the second one is easy to forget."),
            ("h", "The Inner Join Keeps Only Matches"),
            ("point", "The query", "SELECT t.name, SUM(r.amount) AS paid FROM taxpayers AS t JOIN "
             "receipts AS r ON r.taxpayer_id = t.taxpayer_id GROUP BY t.taxpayer_id;"),
            ("point", "What it returned", "Four rows: Ramos Bakery 3,050, Santos Hardware 2,500, Cruz "
             "Store 800 and Dela Rosa Eatery 1,800. Lim Trading is not there."),
            ("point", "Why", "JOIN on its own means an inner join. It keeps a row only when a match is "
             "found on both sides. A taxpayer with no receipt has nothing to match, so the taxpayer "
             "disappears from the result."),
            "For a total of money collected, that is exactly right. Every peso comes from a receipt, and "
            "every receipt has a taxpayer. The trouble starts when the question is about the taxpayers, "
            "including the ones who did not pay.",
            ("h", "The Left Join Keeps Everyone on the Left"),
            ("point", "The query", "SELECT t.name, COUNT(r.receipt_no) AS receipts, SUM(r.amount) AS paid "
             "FROM taxpayers AS t LEFT JOIN receipts AS r ON r.taxpayer_id = t.taxpayer_id GROUP BY "
             "t.taxpayer_id;"),
            ("point", "What it returned", "Five rows. The first four are the same as before. The fifth is "
             "Lim Trading with 0 receipts and an empty total."),
            ("point", "Why", "SQLite’s documentation explains that a LEFT JOIN adds an extra row for each "
             "row in the left table that matches nothing on the right, and fills the right table’s "
             "columns in that row with NULL. The table named first, before LEFT JOIN, is the one whose "
             "rows are all kept."),
            ("point", "Count a column, not the row", "COUNT(r.receipt_no) gave 0 for Lim Trading because "
             "COUNT of a column skips NULL, as Part 20 showed. COUNT(*) would have counted the filler row "
             "and reported 1 receipt that does not exist."),
            ("point", "Turn the blank into zero", "SUM over nothing but NULL returned NULL, not 0. "
             "COALESCE(SUM(r.amount), 0) shows 0, which reads better in a report."),
            "The same idea works by barangay. A LEFT JOIN from taxpayers to receipts, grouped by "
            "barangay, with COALESCE, returned Poblacion 5,650, San Isidro 2,500 and San Roque 0. With "
            "an inner join, San Roque was missing from the list entirely, and a reader could think the "
            "town has only two barangays with businesses.",
            ("h", "Finding Who Is Missing"),
            "In a treasury, a left join is especially handy for one question: “Who has not "
            "paid?”",
            ("point", "The query", "SELECT t.taxpayer_id, t.name FROM taxpayers AS t LEFT JOIN receipts "
             "AS r ON r.taxpayer_id = t.taxpayer_id WHERE r.receipt_no IS NULL;"),
            ("point", "What it returned", "One row: T-00163 Lim Trading."),
            ("point", "How it works", "The left join keeps every taxpayer. For the ones with no receipt, "
             "the receipt columns are NULL. The WHERE line then keeps only those rows. Use IS NULL here, "
             "not = NULL, because in SQL nothing is equal to NULL, not even another NULL."),
            ("point", "Another way", "SELECT taxpayer_id FROM taxpayers WHERE taxpayer_id NOT IN (SELECT "
             "taxpayer_id FROM receipts); returned the same taxpayer. Be careful with NOT IN if the inner "
             "list can contain NULL: in standard SQL, one NULL in that list makes the whole test return "
             "no rows. The left join version does not have that trap."),
            "This list is where follow-up work begins: a reminder letter, a visit, or a check that the "
            "business is still operating. It is the same list the head of office was asking for at the "
            "start.",
            ("h", "Where the Date Condition Goes"),
            "Now the head of office asks a narrower question: “How many receipts did each business get "
            "in November?” This is where a left join can quietly turn back into an inner join.",
            ("point", "The condition in WHERE", "Adding WHERE r.paid_on BETWEEN '2026-11-01' AND "
             "'2026-11-30' after the left join returned only two rows: Santos Hardware with 1 and Dela "
             "Rosa Eatery with 1. Ramos Bakery, Cruz Store and Lim Trading disappeared."),
            ("point", "Why", "For a taxpayer with no November receipt, the date column is NULL or an "
             "October date, and the WHERE test fails, so the row is dropped. The left join kept everyone; "
             "the WHERE line threw them away again."),
            ("point", "The condition in ON", "Moving the date test into the join, ON r.taxpayer_id = "
             "t.taxpayer_id AND r.paid_on BETWEEN '2026-11-01' AND '2026-11-30', returned all five "
             "businesses: Santos Hardware 1, Dela Rosa Eatery 1, and 0 for the other three."),
            "The rule of thumb: a condition about the right-hand table belongs in ON when you want to "
            "keep every row on the left. A condition about the left-hand table, such as WHERE t.barangay "
            "= 'Poblacion', can stay in WHERE.",
            ("h", "When a Join Doubles the Money"),
            "Later, the analyst added the contacts table so the report could show a phone number beside "
            "each payment.",
            ("point", "The query", "SELECT COUNT(*), SUM(r.amount) FROM receipts AS r LEFT JOIN contacts "
             "AS k ON k.taxpayer_id = r.taxpayer_id;"),
            ("point", "What it returned", "8 rows and a total of 11,200. There are six receipts and the "
             "true total is 8,150."),
            ("point", "Why", "Ramos Bakery has two phone numbers. Each of its two receipts matched both "
             "numbers, so each receipt appeared twice. Its 3,050 was counted twice, and 8,150 plus 3,050 "
             "is 11,200."),
            ("point", "The fix", "Join one row per taxpayer, not one row per phone number. For example, "
             "total the receipts first in one query, or keep a single main number per taxpayer, and join "
             "to that. Then check the row count and total again."),
            "This is sometimes called fan-out: a join to a table that has several rows per key multiplies "
            "the rows on the other side. No error appears. The total is simply wrong.",
            ("h", "Right Joins, Full Joins and Cross Joins"),
            ("point", "RIGHT JOIN", "Keeps every row of the second table instead of the first. Writing the "
             "tables in the other order and using LEFT JOIN does the same thing, so use "
             "whichever direction you find easier to read. If an older copy of sqlite3 rejects RIGHT JOIN, swap the tables "
             "and use LEFT JOIN."),
            ("point", "FULL JOIN", "SQLite’s documentation describes it as a combination of a left and a "
             "right join: unmatched rows from both sides are kept. It suits comparing two lists, such as "
             "the receipts in the system against a collector’s own list."),
            ("point", "CROSS JOIN", "Pairs every row with every row. The documentation says an inner join "
             "with no ON clause gives the same result. Five taxpayers and six receipts make 30 rows, "
             "which is why Part 19 warned about forgetting the ON line."),
            ("h", "Three Checks After Every Join"),
            ("point", "Count the rows", "Before the join, count the rows of the main table. After it, "
             "count again. If the number grew, look for a key with several matches."),
            ("point", "Check a known total", "SELECT SUM(amount) FROM receipts; gave 8,150. Any joined "
             "report of the same receipts should still add up to 8,150."),
            ("point", "Look for the missing", "Run the IS NULL query from both sides: taxpayers with no "
             "receipts, and receipts whose taxpayer ID is not in the taxpayers table. The second kind "
             "points to a typing error or a missing registration."),
            ("h", "The List, Corrected"),
            "The analyst changed JOIN to LEFT JOIN, counted receipt numbers instead of rows, and wrapped "
            "the total in COALESCE. The new report showed five businesses, with Lim Trading at the "
            "bottom with 0. A second page listed the businesses with no receipt this year, and the head "
            "of office used it to plan reminder letters. Beside the query, the analyst wrote the row "
            "count and the check total, so anyone running it next month can confirm it still adds up.",
            ("h", "Mistakes to Avoid"),
            ("point", "Using an inner join for a list of people", "It drops everyone with no match."),
            ("point", "Counting rows after a left join", "Count a column from the right table instead."),
            ("point", "Filtering the right table in WHERE", "Put that condition in ON to keep everyone."),
            ("point", "Joining to a table with several rows per key", "Check the row count and the total."),
            ("h", "Key Takeaways"),
            ("point", "Inner join", "Keeps only rows that match on both sides."),
            ("point", "Left join", "Keeps every row of the first table and fills the gaps with NULL."),
            ("point", "IS NULL after a left join", "Lists who or what has no match."),
            ("point", "Check totals", "A join should never change the sum of the money it reports."),
            ("h", "Your Part 28 Exercise"),
            "In your SQLite practice file from Part 19, add one taxpayer with no receipts.",
            ("point", "Run both joins", "Compare the inner join and the left join, and note the row "
             "counts."),
            ("point", "Find the missing", "Write the IS NULL query and confirm it returns the new "
             "taxpayer."),
            ("point", "Test the trap", "Add a date condition in WHERE, then move it into ON, and compare "
             "the two results."),
            "Last, make a small table with two rows for one taxpayer, join to it, and watch the total "
            "grow. Seeing it happen once makes it easier to catch at work.",
            ("cta", "Read: Data Analytics Series, Part 19: First Steps in SQL, Asking a Database Questions", "/blog/data-analytics-part-19-first-steps-in-sql/"),
            ("cta", "Read: Data Analytics Series, Part 20: Cleaning Data With SQL, Without Touching the Original", "/blog/data-analytics-part-20-cleaning-with-sql/"),
            ("cta", "Read: Data Analytics Series, Part 14: Databases 101, Tables, Primary Keys and Foreign Keys", "/blog/data-analytics-part-14-databases-101/"),
            ("cta", "Read: Data Analytics Series, Part 21: Stop Bad Data at the Door, Rules Inside the Database", "/blog/data-analytics-part-21-rules-inside-the-database/"),
            ("ask", "Which list in your office should include the people who did not show up in the data?"),
        ],
    },
    {
        "date": "March 22, 2027",
        "title": "Data Analytics Series, Part 27: Choosing the Right Chart, Starting From the Question",
        "slug": "data-analytics-part-27-choosing-the-right-chart",
        "category": "data",
        "summary": "A chart should answer one question at a glance. This part matches five basic questions "
                   "to the chart types Google Sheets offers, builds two of them from practice data, and "
                   "shows the axis, title and slice mistakes that make an honest number look misleading.",
        "publish_on": "2027-03-22 21:00",
        "body": [
            "The analyst was proud of the pie chart: twelve slices, one for each month’s collections, each in "
            "its own color. At the meeting, nobody could tell whether March was bigger than April, or whether "
            "the year had gone up or down. Someone asked for the numbers, and the analyst read them aloud "
            "from the table. The chart had used half a page and answered nothing.",
            "(The meeting, the months and the amounts below are invented for practice. No real office or "
            "taxpayer is described.)",
            "Part 26 chose the right middle number. This part chooses the right picture. After reading, you "
            "will be able to start from the question instead of the chart menu, match five basic questions "
            "to chart types in Google Sheets, build a line chart and a bar chart from practice data, and "
            "avoid the axis, title and pie mistakes that mislead readers.",
            ("photo", "blog/data-charts.jpg", "Choosing a chart: trend in a line, comparison in sorted bars, "
             "a few parts of a whole in a pie, spread in a histogram, and a title that states the finding. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Start With the Question"),
            "Before opening the chart menu, write the question the chart must answer in one sentence. The "
            "question decides the chart.",
            ("point", "How did it change over time?", "A trend."),
            ("point", "Which is bigger?", "A comparison between categories."),
            ("point", "What share does each part have?", "Parts of a whole."),
            ("point", "How are the values spread out?", "A distribution."),
            ("point", "Do two things move together?", "A relationship."),
            ("quote", "Pick the question first. The chart follows."),
            ("h", "What Google Says Each Chart Is For"),
            "Google’s help page on chart types in Sheets gives a one-line purpose for each.",
            ("point", "Line", "To look at trends or data over a time period."),
            ("point", "Bar", "To show the difference between the data points for one or more categories."),
            ("point", "Column", "To show one or more categories, or groups, of data, especially if each "
             "category has subcategories."),
            ("point", "Pie", "To show data as slices of pie, or proportions of a whole."),
            ("point", "Histogram", "To show the distribution of a data set across different buckets."),
            ("point", "Scatter", "To show numeric coordinates along the horizontal and vertical axes."),
            "Put the two lists together and the match is direct: trend to line, comparison to bar or column, "
            "parts of a whole to pie, distribution to histogram, relationship to scatter.",
            ("h", "Practice 1: A Trend in a Line"),
            "Type six months of practice collections into columns A and B: January ₱25,200; February ₱7,900; "
            "March ₱9,400; April ₱18,600; May ₱8,700; June ₱9,100.",
            ("point", "Insert it", "Select A1:B7 with the headers, then Insert, then Chart. In the chart "
             "editor, under Setup, set the chart type to Line."),
            ("point", "Read it", "The line shows two peaks, January and April, which matches the deadline "
             "months for business taxes discussed in the Business Intelligence series."),
            ("point", "Title it with the finding", "Not “Collections, January to June,” but “Collections "
             "peak in deadline months: January and April.”"),
            "Twelve slices of a pie could not show this. A line shows it in one look, because time runs left "
            "to right.",
            ("h", "Practice 2: A Comparison in Sorted Bars"),
            "Use the barangay totals from Part 24: Poblacion ₱15,100, San Isidro ₱9,200 and San Roque ₱8,800.",
            ("point", "Insert a bar chart", "Select the barangay names and totals, Insert, Chart, then Bar."),
            ("point", "Sort first", "Sort the data from largest to smallest before charting, as Part 22 "
             "showed, so the bars appear in order."),
            ("point", "Label the values", "With only three bars, show the amount on each bar so readers do "
             "not have to read the axis."),
            ("h", "Column or Bar?"),
            "Google’s description of the column chart mentions categories that have subcategories. That fits the pivot table from Part 24, where each barangay had a business tax amount and a real property tax amount.",
            ("point", "Clustered columns", "Barangays along the bottom, two columns each, one for business tax and one for real property tax. Poblacion’s ₱7,500 and ₱7,600 stand side by side, and the reader sees they are nearly equal."),
            ("point", "Bars for long names", "When category names are long, horizontal bars leave room for the labels. Long barangay names can fit better on a bar chart than under columns."),
            "Both show comparison. Choose by the labels and the subcategories, not by habit.",
            ("h", "The Axis That Starts at Zero"),
            "Bars show size by their length. If the axis starts above zero, the lengths stop telling the "
            "truth.",
            ("point", "Honest", "With the axis from zero, San Isidro’s ₱9,200 bar is a little longer than "
             "San Roque’s ₱8,800 bar, which is the truth: a difference of ₱400, under 5 percent."),
            ("point", "Misleading", "Start the axis at ₱8,000, and San Isidro’s visible bar is 1,200 long "
             "against San Roque’s 800. It looks one and a half times as big."),
            "In the chart editor, check the minimum of the horizontal axis on a bar chart. Line charts can "
            "start above zero when the point is the shape of the change, but say so on the axis.",
            ("h", "When a Pie Is Fine"),
            ("point", "Few parts", "Two to four slices that together make a meaningful whole, such as "
             "real property tax versus business tax in total collections."),
            ("point", "Big differences", "Slices that differ clearly. Close slices can be hard to tell apart by eye; use bars instead."),
            ("point", "Not for time", "Months are a sequence, not parts of a whole to compare by size. Use a "
             "line."),
            ("h", "Distribution and Relationship"),
            ("point", "Histogram for spread", "The nine payments from Part 26 in a histogram show eight small "
             "payments in the lowest buckets and one far to the right. That is the gap between the mean and "
             "the median, drawn as a picture."),
            ("point", "Scatter for two measures", "Each dot is one barangay, placed by two numbers, such as "
             "number of business taxpayers and total business tax. Dots that rise together suggest a "
             "relationship; they do not prove a cause."),
            ("h", "Titles, Labels and Notes"),
            ("point", "Say the finding", "The title states what the reader should see."),
            ("point", "Units on the axis", "Pesos, count, percent. Never leave the reader to guess."),
            ("point", "Source and date", "One line under the chart: where the data came from and when it "
             "was pulled."),
            ("point", "Color with a purpose", "Use one color for the bars unless a color carries meaning, such as one highlighted barangay. Part 26 of the Business Intelligence series covers colors that every reader can tell apart."),
            ("h", "Mistakes to Avoid"),
            ("point", "Choosing the chart before the question", "Write the question first."),
            ("point", "Pies with many slices", "More than a few slices can become hard to compare."),
            ("point", "Bar axes that skip zero", "They exaggerate small differences."),
            ("point", "Titles that only name the data", "State the finding."),
            ("h", "Key Takeaways"),
            ("point", "Five questions, five charts", "Trend, comparison, share, spread, relationship."),
            ("point", "Line for time, bars for comparison", "Sorted, labeled, from zero."),
            ("point", "Pies only for a few parts", "Of a meaningful whole."),
            ("point", "A title that says something", "Plus units, source and date."),
            ("h", "Your Part 27 Exercise"),
            "Use the practice data above, or your own.",
            ("point", "Write three questions", "One about time, one comparison, one share."),
            ("point", "Build three charts", "A line, a sorted bar chart and a pie with no more than four "
             "slices."),
            ("point", "Retitle them", "Write each title as the finding, in one sentence."),
            "Then show only the charts to a colleague and ask what each one says. If their answer matches "
            "your title, the chart works.",
            "At the next meeting, the analyst brought one line chart titled “Collections peak in deadline "
            "months: January and April.” Nobody asked for the table. The discussion moved straight to the "
            "question that mattered: how to prepare the cashiers for April.",
            ("cta", "Read: Data Analytics Series, Part 26: Mean or Median? Choosing the Middle That Tells the Truth", "/blog/data-analytics-part-26-mean-or-median/"),
            ("cta", "Read: Data Analytics Series, Part 24: Pivot Tables, a Summary You Can Rearrange in Seconds", "/blog/data-analytics-part-24-pivot-tables/"),
            ("cta", "Read: Data Analytics Series, Part 22: Sorting and Filtering With Purpose", "/blog/data-analytics-part-22-sorting-and-filtering/"),
            ("cta", "Read: Business Intelligence Series, Part 25: Annotating Charts, Lines, Bands and Notes That Explain the Bumps", "/blog/business-intelligence-part-25-annotating-charts/"),
            ("ask", "Which chart in your office would say more if it started from a question?"),
        ],
    },
    {
        "date": "March 17, 2027",
        "title": "Data Analytics Series, Part 26: Mean or Median? Choosing the Middle That Tells the Truth",
        "slug": "data-analytics-part-26-mean-or-median",
        "category": "data",
        "summary": "One very large payment can make an average describe nobody. This part compares the mean "
                   "and the median with nine practice receipts, shows both in Google Sheets, explains when "
                   "each one is the right answer, and gives a simple habit for reporting the middle "
                   "honestly.",
        "publish_on": "2027-03-17 21:00",
        "body": [
            "The report said the average business tax payment in the first week of January was ₱13,244. A "
            "councilor read it twice. “Our small stores pay that much now?” They did not. Eight of the nine "
            "payments that week were between ₱2,800 and ₱6,000. The ninth, from a large company, was "
            "₱85,000, and it had pulled the average far above every small store in town.",
            "(The payments, the stores and the company are invented for practice. They do not describe any "
            "real taxpayer.)",
            "Part 25 brought detail into each row. This part summarizes a column with a single number, and "
            "asks which number. By the end, you will know what the mean and the median are, how to compute "
            "both in Google Sheets, why one large value moves one and not the other, when each is the right "
            "choice, and how to report a middle value so that nobody is misled.",
            ("photo", "blog/data-median.jpg", "Mean or median: the mean rebuilds the total, the median finds "
             "the typical case, and showing both, with the range, tells the whole story. (Illustration: "
             "Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Two Kinds of Middle"),
            ("point", "The mean", "Add all the values and divide by how many there are. It is what the AVERAGE function computes in Sheets."),
            ("point", "The median", "Sort the values and take the one in the middle. Half the values are at or "
             "below it, half at or above."),
            "Both are honest numbers. They answer different questions, and a report goes wrong when it uses "
            "one to answer the other’s question.",
            ("quote", "An average can describe a town where nobody lives."),
            ("h", "The Practice Data"),
            "Nine business tax payments, in pesos, already sorted from smallest to largest: 2,800; 3,200; "
            "3,500; 4,100; 4,400; 5,000; 5,200; 6,000; and 85,000. Type them into cells B2 to B10.",
            ("point", "The total", "=SUM(B2:B10) gives ₱119,200."),
            ("point", "The mean", "=AVERAGE(B2:B10) gives ₱119,200 ÷ 9, about ₱13,244.44."),
            ("point", "The median", "=MEDIAN(B2:B10) gives ₱4,400, the fifth of the nine values."),
            "The mean is higher than eight of the nine payments. The median sits right among the small "
            "stores, where most of the payments are.",
            ("h", "What One Large Value Does"),
            "Remove the ₱85,000 payment and compute again on the other eight.",
            ("point", "The mean falls", "From about ₱13,244 to ₱4,275, because ₱34,200 ÷ 8 = ₱4,275."),
            ("point", "The median barely moves", "From ₱4,400 to ₱4,250. With an even number of values, "
             "Google’s help says MEDIAN interpolates between the two center values, here ₱4,100 and ₱4,400."),
            "One payment changed the mean by about ₱9,000 and the median by ₱150. That is the difference in "
            "one sentence: the mean feels every value, including the extreme ones; the median only cares "
            "about the order.",
            ("h", "When the Mean Is Right"),
            ("point", "When the total matters", "The mean times the count gives back the total: ₱13,244.44 "
             "× 9 is ₱119,200. For a budget estimate, a forecast of total collections or a cost per "
             "transaction, the mean is the one to use."),
            ("point", "When values are close together", "If payments ranged only from ₱4,000 to ₱5,000, the "
             "mean and the median would be close, and the mean is fine."),
            ("h", "When the Median Is Right"),
            ("point", "When you describe a typical case", "“What does a typical small store pay?” The median "
             "answers that without being dragged by the largest taxpayer."),
            ("point", "When a few values are very large", "Payments, property values and incomes can have a "
             "few very large values. The median stays near the middle of the group."),
            ("point", "When data may contain mistakes", "A payment typed as ₱850,000 instead of ₱8,500 would "
             "wreck the mean. The median would hardly notice, which is useful, and also a reason to find "
             "the typo anyway."),
            ("h", "Where This Shows Up in a Treasury"),
            ("point", "Collections per day", "For a budget estimate of yearly collections, the mean daily collection times the number of collection days rebuilds the total. The median day would understate it if a few deadline days are very large."),
            ("point", "Assessed values", "To describe a typical residential lot, the median is safer, since a few large commercial properties can pull the mean up."),
            ("point", "Time at the window", "To tell taxpayers how long a typical visit takes, the median wait describes the middle visitor better than a mean raised by a few very long visits."),
            ("h", "Look Before You Choose"),
            "Before picking either, look at the values. Part 22 sorted them; do the same here.",
            ("point", "Sort and read the ends", "=MIN(B2:B10) gives ₱2,800 and =MAX(B2:B10) gives ₱85,000. "
             "A maximum many times the median is a signal to check."),
            ("point", "Compare the two", "If the mean and the median are far apart, a few values are pulling "
             "the mean. Find them and decide whether they are real."),
            ("point", "Check the large values", "Values far from the rest are called outliers. Confirm each one against its receipt before deciding what to do."),
            "In this case, the ₱85,000 was real: a large company paying its tax. It belongs in the total. It "
            "does not belong in a sentence about what small stores pay.",
            ("h", "Medians by Group"),
            "Add a column C that labels each payment by size: Small for the first eight rows, Large for the ₱85,000 payment. Then a median can be computed for one group at a time.",
            ("point", "With FILTER", "=MEDIAN(FILTER(B2:B10, C2:C10=\"Small\")) keeps only the small payments and returns ₱4,250, the same as removing the large one by hand, but without deleting anything."),
            ("point", "In a pivot table", "The pivot table from Part 24 can summarize Values by MEDIAN instead of SUM. Put Size in Rows, Amount in Values, and choose MEDIAN to see one middle per group."),
            ("point", "Count each group too", "A median from two payments says much less than a median from two hundred. Add COUNTA beside it, as in Part 24, so the reader sees how many values stand behind each number."),
            "Here, grouping is the cleanest answer to the councilor’s question. The small stores get their own middle, the large company is reported as what it is, and nothing is hidden or removed.",
            ("h", "Reporting the Middle Honestly"),
            ("point", "Name the measure", "Write “median payment” or “mean payment,” not just “average.”"),
            ("point", "Show both when they differ", "“The median payment was ₱4,400; the mean was ₱13,244, "
             "raised by one large payment of ₱85,000.”"),
            ("point", "Add the range", "The smallest and largest values show the reader how spread out the "
             "data is."),
            ("point", "Split the groups", "Sometimes the best answer is two groups: small businesses and large "
             "ones, each with its own median. COUNTIFS and AVERAGEIFS from Part 23 do this."),
            ("h", "Mistakes to Avoid"),
            ("point", "Saying “average” without saying which", "Name the mean or the median."),
            ("point", "Using the mean for a typical case", "Large values can pull it away from the rest of the data."),
            ("point", "Using the median for totals", "The median times the count does not give the total."),
            ("point", "Deleting large values to fix the mean", "Check them; if real, report them."),
            ("h", "Key Takeaways"),
            ("point", "Mean for totals", "AVERAGE, and it rebuilds the sum."),
            ("point", "Median for the typical case", "MEDIAN, and it resists extreme values."),
            ("point", "Far apart means look closer", "A gap between them points to large values."),
            ("point", "Report clearly", "Name the measure, show both when they differ, add the range."),
            ("h", "Your Part 26 Exercise"),
            "Type the nine practice payments, or use a column from your own practice data.",
            ("point", "Compute both", "AVERAGE and MEDIAN, plus MIN and MAX."),
            ("point", "Remove the largest", "Recompute both and note which one moved."),
            ("point", "Write one sentence", "Describe the typical payment, naming the measure you chose and "
             "why."),
            "If your sentence would still be true for the small store owner reading it, you chose well.",
            "The analyst rewrote the line in the report: “The median business tax payment in the first week "
            "of January was ₱4,400. One large payment of ₱85,000 raised the mean to ₱13,244.” The councilor "
            "read it once and nodded. That was the town he knew.",
            ("cta", "Read: Data Analytics Series, Part 25: XLOOKUP, Bringing the Right Detail Into Every Row", "/blog/data-analytics-part-25-xlookup/"),
            ("cta", "Read: Data Analytics Series, Part 23: SUMIFS, COUNTIFS and AVERAGEIFS", "/blog/data-analytics-part-23-sumifs-countifs-averageifs/"),
            ("cta", "Read: Data Analytics Series, Part 22: Sorting and Filtering With Purpose", "/blog/data-analytics-part-22-sorting-and-filtering/"),
            ("cta", "Read: Data Analytics Series, Part 16: Dirty Data, the Usual Suspects and How to Spot Them", "/blog/data-analytics-part-16-dirty-data/"),
            ("ask", "Which “average” in your office reports would change its story if you used the median?"),
        ],
    },
    {
        "date": "March 12, 2027",
        "title": "Data Analytics Series, Part 25: XLOOKUP, Bringing the Right Detail Into Every Row",
        "slug": "data-analytics-part-25-xlookup",
        "category": "data",
        "summary": "Receipts list a taxpayer ID; the names and barangays live on another tab. XLOOKUP joins "
                   "them with one formula. This part builds it step by step in Google Sheets, shows what to "
                   "do when an ID is missing, how to return two columns at once, find the latest entry, and "
                   "match a value to a bracket.",
        "publish_on": "2027-03-12 21:00",
        "body": [
            "The receipts list had dates, amounts and a taxpayer ID in every row. The councilor’s question "
            "needed names and barangays, which lived on a separate Taxpayers tab. An encoder started copying "
            "them over by hand, row by row. Halfway down, she pasted one name a row too low, and every name "
            "below it was wrong. Nobody noticed until a store owner asked why his receipt showed a bakery.",
            "(The store, the bakery, the IDs and the amounts are fictional, invented for practice. No real "
            "taxpayer is described.)",
            "Part 24 summarized a list with a pivot table. This part brings detail into a list from another "
            "table. Work through it and you will be able to write an XLOOKUP formula in Google Sheets, show "
            "a clear message when a match is missing, return two columns at once, find the latest receipt for "
            "a taxpayer, match a value to a bracket, and check that every lookup found what it should.",
            ("photo", "blog/data-xlookup.jpg", "XLOOKUP: find the key, return the detail, say clearly when "
             "it is missing, and count the misses before you trust the list. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "What XLOOKUP Does"),
            "Google’s help for Sheets describes XLOOKUP as a function that searches a range for a key and "
            "returns the matching item from a second range. Its full form is:",
            ("point", "The syntax", "XLOOKUP(search_key, lookup_range, result_range, missing_value, "
             "match_mode, search_mode)"),
            ("point", "The three you always need", "What to look for, where to look, and what to bring "
             "back. The help says the lookup range must be a single row or column."),
            ("point", "The three optional ones", "What to show when nothing matches, how to match, and "
             "which direction to search."),
            ("quote", "Type the detail once, in one table, and let the formula bring it everywhere else."),
            ("h", "The Practice Data"),
            "The Taxpayers tab has an ID in column A, a name in column B and a barangay in column C:",
            ("point", "T-001", "Reyes Store, Poblacion."),
            ("point", "T-002", "Santos Bakery, San Isidro."),
            ("point", "T-003", "Cruz Hardware, San Roque."),
            ("point", "T-004", "Dela Cruz Farm, Poblacion."),
            "The Receipts tab has a date in column A, a taxpayer ID in column B and an amount in column C, "
            "in rows 2 to 7: January 4, T-001, ₱5,000; January 4, T-002, ₱3,200; January 5, T-003, ₱2,800; "
            "January 6, T-005, ₱1,500; February 1, T-002, ₱1,900; February 2, T-001, ₱2,600.",
            "Notice T-005. It is not on the Taxpayers tab. That is on purpose.",
            ("h", "Step 1: The Basic Lookup"),
            "In cell D2 of the Receipts tab, type:",
            ("point", "Formula", "=XLOOKUP(B2, Taxpayers!A$2:A$5, Taxpayers!B$2:B$5)"),
            "It takes the ID in B2, finds it in the Taxpayers IDs, and returns the name in the same position. "
            "D2 shows Reyes Store. The dollar signs lock the rows of the two ranges, so when you copy the "
            "formula down to D7, each row looks up its own ID in the same table.",
            "Row 5 shows #N/A. Google’s help says this is the default when no match is found. The formula is "
            "working; the data has a gap.",
            ("h", "Step 2: Say Clearly What Is Missing"),
            "Add the fourth argument:",
            ("point", "Formula", "=XLOOKUP(B2, Taxpayers!A$2:A$5, Taxpayers!B$2:B$5, \"NOT FOUND\")"),
            "Row 5 now reads NOT FOUND. An error code can look like a broken formula and get deleted. A "
            "plain message tells the next person exactly what to fix: add T-005 to the Taxpayers tab, or "
            "correct the ID on the receipt. Part 16 of the Business Intelligence series used the same idea in "
            "its cleaning tab.",
            ("h", "Step 3: Bring Back Two Columns at Once"),
            "Google’s help notes that if the result range covers more than one column, XLOOKUP returns the "
            "whole row at the matched position. So one formula can bring both the name and the barangay:",
            ("point", "Formula", "=XLOOKUP(B2, Taxpayers!A$2:A$5, Taxpayers!B$2:C$5, \"NOT FOUND\")"),
            "D2 shows Reyes Store and E2 shows Poblacion. Leave column E empty before you enter it, because "
            "the result needs that space.",
            ("h", "Step 4: Find the Latest Receipt"),
            "The last argument, search_mode, sets the direction. The help lists 1 for first to last, the "
            "default, and -1 for last to first. If the receipts are sorted by date, oldest first, searching "
            "from the bottom finds the most recent one.",
            ("point", "Formula", "=XLOOKUP(\"T-002\", B2:B7, A2:A7, \"none\", 0, -1)"),
            "It returns February 1, the later of Santos Bakery’s two receipts. The 0 before the -1 asks for an "
            "exact match. The same formula for T-001 returns February 2.",
            ("h", "Step 5: Match a Value to a Bracket"),
            "The fifth argument, match_mode, can do more than exact matches. The help lists 0 for exact, 1 "
            "for exact or the next larger value, -1 for exact or the next smaller value, and 2 for a wildcard "
            "match.",
            "Say a practice table on a Bands tab lists lower limits in column A, 0, 100,000 and 500,000, "
            "with labels Band A, Band B and Band C in column B. To place gross sales of ₱250,000:",
            ("point", "Formula", "=XLOOKUP(250000, Bands!A2:A4, Bands!B2:B4, \"none\", -1)"),
            "There is no exact 250,000, so -1 takes the next smaller limit, 100,000, and returns Band B. These "
            "bands are invented for practice; a real rate schedule comes from the ordinance.",
            ("h", "Check Every Lookup"),
            ("point", "Count the misses", "=COUNTIF(D2:D7, \"NOT FOUND\") returns 1, for T-005. Make it zero "
             "before using the list."),
            ("point", "Look for spaces", "An ID typed as “T-001 ” with a trailing space will not match. Part "
             "16 of the Business Intelligence series showed how TRIM cleans these."),
            ("point", "Spot-check by hand", "Pick two rows and find the ID on the Taxpayers tab yourself. If the name and barangay match what the formula returned, the formula and the table agree. If not, check the ranges first."),
            ("h", "XLOOKUP or VLOOKUP?"),
            "VLOOKUP searches the first column of a range and returns a column you name by its number, "
            "counting from the left. Insert a column in the middle, and that number can point to the wrong "
            "column. XLOOKUP names the lookup range and the result range separately, so the lookup column does not have to come first, and there is no column number to keep up to date. Both functions still work; XLOOKUP just removes the column number that can go out of date.",
            ("h", "Mistakes to Avoid"),
            ("point", "Unlocked ranges", "Without the dollar signs, the ranges slide when copied down."),
            ("point", "Ranges of different sizes", "The help says the result range should match the lookup "
             "range."),
            ("point", "Ignoring #N/A", "Give it a message, then count and fix the misses."),
            ("point", "Searching from the end on unsorted data", "“Latest” only works if the list is in date "
             "order."),
            ("h", "Key Takeaways"),
            ("point", "Three parts", "What to find, where to look, what to return."),
            ("point", "Name the gaps", "Use the missing value to show NOT FOUND."),
            ("point", "Direction and mode", "-1 in search mode finds the last entry; -1 in match mode finds "
             "a bracket."),
            ("point", "Count before you trust", "Zero misses, then a spot check."),
            ("h", "Your Part 25 Exercise"),
            "Type the two practice tabs into a new sheet, or use your own lists.",
            ("point", "Look up names", "Add a Name column to Receipts with XLOOKUP and a NOT FOUND message."),
            ("point", "Return two columns", "Change it to bring back name and barangay together."),
            ("point", "Find the latest", "Find the most recent receipt date for T-001."),
            "Then count the misses and fix them. A list with zero NOT FOUND rows is one you can sort, "
            "filter and pivot with confidence.",
            "The encoder deleted the pasted names and typed one XLOOKUP in D2. Copied down, it filled every "
            "row in a second, and one row said NOT FOUND. It was a receipt typed with the wrong ID. She fixed "
            "it, and the store owner’s receipt showed his store again.",
            ("cta", "Read: Data Analytics Series, Part 24: Pivot Tables, a Summary You Can Rearrange in Seconds", "/blog/data-analytics-part-24-pivot-tables/"),
            ("cta", "Read: Data Analytics Series, Part 23: SUMIFS, COUNTIFS and AVERAGEIFS", "/blog/data-analytics-part-23-sumifs-countifs-averageifs/"),
            ("cta", "Read: Business Intelligence Series, Part 16: A Small Pipeline in Google Sheets, Raw to Clean to Summary", "/blog/business-intelligence-part-16-pipeline-in-sheets/"),
            ("cta", "Read: Data Analytics Series, Part 16: Dirty Data, the Usual Suspects and How to Spot Them", "/blog/data-analytics-part-16-dirty-data/"),
            ("ask", "Which list in your office is still filled in by copying from another list?"),
        ],
    },
    {
        "date": "March 7, 2027",
        "title": "Data Analytics Series, Part 24: Pivot Tables, a Summary You Can Rearrange in Seconds",
        "slug": "data-analytics-part-24-pivot-tables",
        "category": "data",
        "summary": "A pivot table turns hundreds of receipt rows into a summary by barangay, type or month, and "
                   "lets you rearrange it with a click. This part builds one in Google Sheets step by step, "
                   "checks it against SUMIFS, and shows the traps: missing headers, value filters and totals "
                   "that hide a gap.",
        "publish_on": "2027-03-07 21:00",
        "body": [
            "The day after the council received its sixty-number table, a councilor called with three new "
            "questions. What about totals by type of tax, not just by barangay? How many receipts were behind "
            "each total? And what share of the year did each barangay bring in? The analyst could write "
            "three new sets of SUMIFS formulas. Or she could build one pivot table and drag a few fields "
            "around.",
            "(Everyone and everything in this story is fictional, including the numbers. No real town or taxpayer is described.)",
            "Part 23 built a summary from formulas. This part builds one without writing any. Stay with me "
            "to the end, and you will know what a pivot table is, how to build one in Google Sheets, how to "
            "change what it counts and how it groups dates, how to check it against SUMIFS, and the "
            "mistakes that make a pivot table quietly wrong.",
            ("photo", "blog/data-pivot.jpg", "Pivot tables: one row per record in, a summary you can rearrange out, and a check against the grand total. (Illustration: Butch Mahinay, aumahinay.dev)",
             "medium"),
            ("h", "What a Pivot Table Is"),
            "A pivot table reads a list of records and summarizes it: totals, counts or other figures, "
            "grouped by whatever fields you choose. You do not type formulas. You choose which field goes "
            "down the side, which goes across the top, and what to add up. Change your mind, and the table "
            "rearranges itself.",
            "It works only on a clean list. Part 12 laid out the rule: one row per record, one column per "
            "field, and a header on top of every column.",
            ("quote", "A pivot table is a question you can rearrange."),
            ("h", "The Practice Data"),
            "The examples use eight receipts from a Receipts tab with four columns: Date, Barangay, Type "
            "and Amount.",
            ("point", "January 4", "Poblacion, RPT, ₱5,000; San Isidro, Business, ₱3,200."),
            ("point", "January 5", "Poblacion, Business, ₱7,500; San Roque, RPT, ₱2,800."),
            ("point", "January 6", "San Isidro, RPT, ₱4,100; Poblacion, RPT, ₱2,600."),
            ("point", "February 1 and 2", "San Roque, Business, ₱6,000; San Isidro, RPT, ₱1,900."),
            "Together they add up to ₱33,100. Keep that number in mind; every summary below must reach it.",
            ("h", "Step 1: Create It"),
            "Google’s help for Sheets gives the steps. Select the cells with the source data, including the "
            "headers, since each column needs a header. Then click Insert, then Pivot table. The pivot table "
            "opens in a new sheet, with an editor panel at the side.",
            ("h", "Step 2: Rows, Columns and Values"),
            ("point", "Rows", "Click Add next to Rows and choose Barangay. The three barangays appear down "
             "the side."),
            ("point", "Columns", "Click Add next to Columns and choose Type. Business and RPT appear across "
             "the top."),
            ("point", "Values", "Click Add next to Values and choose Amount, summarized by SUM."),
            "With the practice data, the table shows Poblacion with ₱7,500 in business tax and ₱7,600 in "
            "real property tax, for ₱15,100. San Isidro shows ₱3,200 and ₱6,000, for ₱9,200. San Roque shows "
            "₱6,000 and ₱2,800, for ₱8,800. The grand total is ₱33,100, the same as the list.",
            ("h", "Step 3: Ask the Councilor’s Questions"),
            ("point", "How many receipts?", "Add Amount to Values a second time and summarize it by COUNTA, "
             "which counts the filled cells. Poblacion has 3 receipts, San Isidro 3 and San Roque 2, for 8."),
            ("point", "What share of the total?", "Under Values, change Show as from Default to a percentage "
             "of the grand total. Poblacion brought in about 45.6 percent, San Isidro 27.8 percent and San "
             "Roque 26.6 percent."),
            ("point", "By month?", "Move Barangay out of Rows and put Date there instead. Then right-click a "
             "date in the table, choose Create pivot date group, and pick a period such as month. January "
             "shows ₱25,200 and February ₱7,900."),
            "Each answer took a few clicks. The data underneath never moved.",
            ("h", "Step 4: See the Rows Behind a Number"),
            "Google’s help describes a drill-down: in the pivot table, double-click a value, and a new sheet "
            "opens with the source rows behind it. Double-clicking Poblacion’s RPT total of ₱7,600 shows the "
            "two receipts, ₱5,000 and ₱2,600. It is a fast way to answer “where did this number come "
            "from?”",
            ("h", "Sorting and Totals"),
            "A summary is easier to read when the biggest numbers come first. Google’s help explains that "
            "under Rows or Columns you can click the arrow under Order or Sort by to change the order, and check Show totals to display the totals.",
            ("point", "Sort by the value", "Sort the barangays by the SUM of Amount, largest first, so the "
             "councilor sees Poblacion at the top."),
            ("point", "Keep the totals on", "The grand total is the number you will check, so leave it "
             "visible."),
            ("h", "Step 5: Filters, With One Warning"),
            "The Filters section of the editor narrows what the pivot table includes, either by condition or "
            "by values, unchecking items you want to hide.",
            "Google’s help adds a warning worth remembering: a filter by values does not pick up new source "
            "data automatically. If a new barangay appears in the list next month, a values filter set "
            "today can leave it out without any message. Check the filter whenever the source grows.",
            ("h", "Check It Against SUMIFS"),
            "A pivot table is convenient, but it still deserves a check. Pick one cell and recompute it with "
            "the tool from Part 23.",
            ("point", "One cell", "=SUMIFS(D2:D9, B2:B9, \"POBLACION\", C2:C9, \"RPT\") should equal "
             "Poblacion’s RPT cell, ₱7,600."),
            ("point", "The grand total", "=SUM(D2:D9) should equal the pivot table’s grand total, "
             "₱33,100."),
            "If the grand totals match but a barangay looks wrong, look for a spelling variant. “POBLACION ” "
            "with a trailing space becomes its own row in a pivot table, which is at least easier to spot "
            "than a missing amount in a formula.",
            ("h", "Keeping It Current"),
            "Google’s help says the pivot table refreshes whenever you change the source cells it is drawn "
            "from. New rows are another matter: if the pivot table reads a fixed range, such as rows 1 to 9, "
            "receipts added in row 10 are left out. Set the range to cover the whole columns, or extend it "
            "when the data grows, and compare the grand total with the list after every update.",
            ("h", "Pivot Table or SUMIFS?"),
            ("point", "Pivot table", "Suited to exploring: trying different groupings quickly, counting and "
             "drilling down."),
            ("point", "SUMIFS", "Suited to a fixed report layout that must stay exactly the same every month, "
             "such as the council’s table."),
            "You can use both: a pivot table to explore, then SUMIFS for the final report, with each checking the other.",
            ("h", "Mistakes to Avoid"),
            ("point", "Missing or repeated headers", "Every column needs one clear header."),
            ("point", "A range that stops short", "New rows outside the range are left out."),
            ("point", "Trusting a values filter on growing data", "It does not pick up new items."),
            ("point", "Skipping the grand total check", "It must match the list."),
            ("h", "Key Takeaways"),
            ("point", "A clean list goes in", "One row per record, headers on every column."),
            ("point", "Rows, columns, values", "Choose them, then rearrange freely."),
            ("point", "Drill down to the source", "Double-click a value to see its rows."),
            ("point", "Check it", "One cell with SUMIFS, the grand total with SUM."),
            ("h", "Your Part 24 Exercise"),
            "Type the eight practice receipts into a new sheet, or use your own practice list.",
            ("point", "Build it", "Barangay in Rows, Type in Columns, SUM of Amount in Values."),
            ("point", "Ask three questions", "Add a count, show the share of the grand total, and group by "
             "month."),
            ("point", "Check it", "Recompute one cell with SUMIFS and the grand total with SUM."),
            "When all three checks pass, you have a summary you can trust and rearrange in seconds.",
            "The analyst sent the councilor one pivot table, then rearranged it twice during the phone call "
            "as new questions came up. Before hanging up, she ran the grand total check. It matched, to the "
            "peso.",
            ("cta", "Read: Data Analytics Series, Part 23: SUMIFS, COUNTIFS and AVERAGEIFS", "/blog/data-analytics-part-23-sumifs-countifs-averageifs/"),
            ("cta", "Read: Data Analytics Series, Part 22: Sorting and Filtering With Purpose", "/blog/data-analytics-part-22-sorting-and-filtering/"),
            ("cta", "Read: Data Analytics Series, Part 16: Dirty Data, the Usual Suspects and How to Spot Them", "/blog/data-analytics-part-16-dirty-data/"),
            ("cta", "Read: Data Analytics Series, Part 12: Spreadsheets Done Right, One Row per Record", "/blog/data-analytics-part-12-one-row-per-record/"),
            ("ask", "Which report in your office would you rebuild as a pivot table first?"),
        ],
    },
    {
        "date": "March 2, 2027",
        "title": "Data Analytics Series, Part 23: SUMIFS, COUNTIFS and AVERAGEIFS",
        "slug": "data-analytics-part-23-sumifs-countifs-averageifs",
        "category": "data",
        "summary": "Totals by barangay, by month or by collector do not need a calculator and sixty filters. "
                   "This part explains SUMIFS, COUNTIFS and AVERAGEIFS with treasury examples: text, number "
                   "and date conditions, a summary table that fills itself in, and a check row that catches "
                   "what the formulas miss.",
        "publish_on": "2027-03-02 21:00",
        "body": [
            "The council wanted a table for its budget hearing: real property tax collections for each of "
            "five barangays, for each month of last year. Sixty numbers.",
            "A staff member started with filters. Filter to Poblacion and January, read the total "
            "at the bottom of the screen, write it on a pad. Clear the filter. Poblacion and February. By the "
            "middle of the afternoon the pad had forty numbers, two of them crossed out, and nobody was sure "
            "which filter had been left on when the twenty-third was written down.",
            "(This is a teaching case: the office, its staff and its figures are fictional. No real "
            "town or taxpayer is described.)",
            "Part 22 sorted and filtered a table to find rows. This part adds up rows without hiding any of "
            "them. By the end of this post, you will know how SUMIFS, COUNTIFS and AVERAGEIFS work, how to "
            "write conditions for text, numbers and dates, how to build a summary table that fills itself in, "
            "and how to check it so that no peso falls through a gap.",
            ("photo", "blog/data-sumifs.jpg", "SUMIFS, COUNTIFS and AVERAGEIFS: add, count or average only "
             "the rows that meet every condition, then check the total. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "The Practice Table"),
            "The examples use a Receipts tab laid out as Part 12 recommends, one row per receipt, with "
            "column A for the date, B for the barangay, C for the collector, D for the type (RPT or "
            "BUSINESS) and E for the amount. Rows 2 to 500 hold the data.",
            ("h", "How the Three Functions Read"),
            ("point", "SUMIFS", "=SUMIFS(E2:E500, B2:B500, \"POBLACION\") adds the amounts in column E for the "
             "rows where column B says POBLACION. The first range is what to add. Then come pairs: a range to "
             "test, and the test."),
            ("point", "COUNTIFS", "=COUNTIFS(B2:B500, \"POBLACION\") counts the rows that pass. It has no range "
             "to add, so it starts with the first pair."),
            ("point", "AVERAGEIFS", "=AVERAGEIFS(E2:E500, B2:B500, \"POBLACION\") averages the amounts of the "
             "rows that pass. Like SUMIFS, the range to average comes first."),
            "Each function takes more pairs, and a row is included only when it meets all of them. Google’s "
            "help for SUMIFS and Microsoft’s help for Excel describe the same rule: the row must meet every "
            "condition. =SUMIFS(E2:E500, B2:B500, \"POBLACION\", D2:D500, \"RPT\") adds only Poblacion rows that "
            "are also real property tax.",
            ("point", "Watch the order", "The older SUMIF puts the range to add last. Microsoft’s help points "
             "out that the sum range is the first argument in SUMIFS but the third in SUMIF. Using SUMIFS "
             "everywhere, even for one condition, keeps one pattern to remember."),
            ("quote", "Write the question as conditions, and the formula almost writes itself."),
            ("h", "Writing the Conditions"),
            ("point", "Text", "Put it in quotation marks: \"POBLACION\". Microsoft’s help lists a missing pair "
             "of quotation marks around text as a reason a formula shows 0 instead of the expected result."),
            ("point", "Numbers with a comparison", "Put the operator inside the quotation marks: "
             "\">=10000\" for amounts of ₱10,000 or more. =COUNTIFS(B2:B500, \"POBLACION\", E2:E500, "
             "\">=10000\") counts the large receipts in Poblacion."),
            ("point", "A value in another cell", "Join the operator to the cell with an ampersand: "
             "\">=\"&H1 uses whatever amount is typed in H1. Change H1, and every formula that points to it "
             "follows."),
            ("point", "Patterns", "An asterisk stands for any run of characters, and a question mark for any "
             "single character. \"SAN*\" matches San Isidro and San Roque. Google’s help for "
             "SUMIF and Microsoft’s help for SUMIFS both describe these wildcards."),
            ("h", "Dates Without Gaps"),
            "Dates are one place where totals quietly go wrong. For January 2027, use two conditions on the same column: "
            "on or after the first day of the month, and before the first day of the next month.",
            ("point", "The formula", "=SUMIFS(E2:E500, A2:A500, \">=\"&DATE(2027,1,1), A2:A500, "
             "\"<\"&DATE(2027,2,1))"),
            ("point", "Why “before the next month”", "It includes every receipt on January 31, and the same "
             "pattern works for any month without remembering whether it has 28, 30 or 31 days."),
            ("point", "Real dates only", "The conditions compare numbers, so a date stored as text will not "
             "pass. Part 18 showed how to find and convert those first."),
            "In a test sheet of six receipts, this formula returned ₱40,500 for January and left out a "
            "receipt dated February 1, exactly as intended.",
            ("h", "A Summary Table That Fills Itself In"),
            "Back to the council’s sixty numbers. Put the five barangay names down column H, from H2 to H6, "
            "and the first day of each month across row 1, from I1 to T1.",
            ("point", "One formula", "In I2: =SUMIFS($E$2:$E$500, $B$2:$B$500, $H2, $A$2:$A$500, "
             "\">=\"&I$1, $A$2:$A$500, \"<\"&EDATE(I$1,1))"),
            ("point", "The dollar signs", "They keep the data ranges fixed, the barangay tied to column H and "
             "the month tied to row 1. Copy the formula across and down, and all sixty cells fill in."),
            ("point", "EDATE", "EDATE(I$1,1) gives the same day one month later, so each cell stops at the "
             "first day of the next month."),
            ("h", "The Check Row That Catches Gaps"),
            "A summary table can look complete and still miss money. Every row that matches none of the names "
            "in column H is left out, without an error.",
            ("point", "Add one check", "Below the table, total all sixty cells. Beside it, add up the whole "
             "Amount column for the same year with one SUMIFS on the dates alone. The two must match."),
            ("point", "Why it fails", "In the same test sheet, one receipt was typed “POBLACION ” with a space "
             "at the end. SUMIFS for POBLACION left its ₱2,000 out. The stray space was one of the suspects in "
             "Part 16, and TRIM in the Clean tab removes it."),
            ("point", "Text amounts", "An amount stored as text is skipped, as with SUM in Part 16. The check "
             "row will not catch it, because the grand total skips it too. Run the ISNUMBER test from Part 16 "
             "on the Amount column as well."),
            ("h", "Averages and Empty Groups"),
            ("point", "When nothing matches", "Microsoft’s help says AVERAGEIFS returns the #DIV/0! error when "
             "no cell meets all the criteria. A barangay with no receipts in a month produces exactly that."),
            ("point", "Handle it honestly", "=IFERROR(AVERAGEIFS(…), \"none\") shows a word instead of an "
             "error. Avoid replacing it with 0: an average of zero claims receipts that were all zero, which "
             "is not the same as no receipts."),
            ("point", "Count beside it", "Put COUNTIFS next to every average. An average of ₱8,000 from two "
             "receipts means less than one from two hundred."),
            ("h", "Either One, Not Both"),
            "SUMIFS keeps a row only when every condition is true. For Poblacion or San Isidro, add two "
            "SUMIFS together: =SUMIFS(E2:E500, B2:B500, \"POBLACION\") + SUMIFS(E2:E500, B2:B500, \"SAN "
            "ISIDRO\"). The two sets of rows cannot overlap, because a receipt has one barangay, so nothing "
            "is counted twice.",
            ("point", "Same size ranges", "Microsoft’s help says each criteria range must have the same number "
             "of rows and columns as the sum range. A formula with E2:E500 and B2:B499 returns an error, which "
             "is better than a wrong total."),
            ("h", "The Council Table, Done Right"),
            "The analyst built the table with one formula, copied across and down, and added the check row. "
            "The first check showed ₱6,200 missing. Three receipts had a barangay name with a trailing space. "
            "After TRIM, the check matched, and the council received sixty numbers that added up to the "
            "year’s total. The next year’s table took one change: the year in row 1.",
            ("h", "Mistakes to Avoid"),
            ("point", "Mixing up SUMIF and SUMIFS", "Use SUMIFS for everything, with the sum range first."),
            ("point", "Dates with “less than or equal to the 31st”", "Use “before the first of next month.”"),
            ("point", "No check row", "Compare the table’s total with the grand total."),
            ("point", "Hiding empty groups as zero", "Show “none,” with a count beside each average."),
            ("h", "Key Takeaways"),
            ("point", "Pairs of range and test", "A row counts only if it passes every pair."),
            ("point", "Conditions", "Text in quotes, operators inside quotes, cells joined with &."),
            ("point", "One formula, many cells", "Dollar signs let one formula fill a whole table."),
            ("point", "Check the total", "The parts must add up to the whole."),
            ("h", "Your Part 23 Exercise"),
            "Use your practice list from Part 22, and add a Date column with made-up dates across two or three months.",
            ("point", "One total", "Write a SUMIFS for one barangay and one month."),
            ("point", "One table", "Build a barangay-by-month table from a single formula."),
            ("point", "One check", "Add the check row, then add a trailing space to one name and watch it fail."),
            "Then fix the space with TRIM and watch the check pass. A check you have seen fail is one you will "
            "trust when it passes.",
            ("cta", "Read: Data Analytics Series, Part 22", "/blog/data-analytics-part-22-sorting-and-filtering/"),
            ("cta", "Read: Data Analytics Series, Part 16", "/blog/data-analytics-part-16-dirty-data/"),
            ("cta", "Read: Data Analytics Series, Part 12", "/blog/data-analytics-part-12-one-row-per-record/"),
            ("cta", "Read: Data Analytics Series, Part 8", "/blog/data-analytics-part-8-metrics-and-kpis/"),
            ("ask", "Which table does your office still build with a filter and a calculator?"),
        ],
    },
    {
        "date": "February 25, 2027",
        "title": "Data Analytics Series, Part 22: Sorting and Filtering With Purpose",
        "slug": "data-analytics-part-22-sorting-and-filtering",
        "category": "data",
        "summary": "Sorting and filtering are the first tools of analysis, and the easiest to misuse. This part "
                   "shows how to sort without scrambling rows, use sorting to find problems, filter without "
                   "changing what colleagues see, and keep a filtered answer up to date with the SORT and "
                   "FILTER functions.",
        "publish_on": "2027-02-25 21:00",
        "body": [
            "The head of office needs a list for Monday’s meeting: the twenty largest delinquent real property "
            "tax accounts in two barangays, biggest first. A staff member opens the shared delinquency sheet, "
            "selects the Amount column, and sorts it from largest to smallest.",
            "The amounts move. The names beside them do not. For about ten minutes, until someone notices, the "
            "sheet shows each taxpayer next to someone else’s balance.",
            "(The story is made up for teaching, and so are its office, people and figures. No real "
            "town or taxpayer is described.)",
            "Part 12 laid out data as one row per record, and Part 19 asked questions of a database with WHERE "
            "and ORDER BY. This part does the same everyday work in a spreadsheet. Read to the end and you will know how to sort a table safely, use sorting to spot problems, filter without changing what "
            "colleagues see, build answers that update themselves with SORT and FILTER, and decide when a "
            "filtered list is the right tool and when it is not.",
            ("photo", "blog/data-sort-filter.jpg", "Sorting and filtering with purpose: keep rows together, "
             "find problems, use filter views and write formulas that update. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "Sort the Whole Row, Every Time"),
            "A row is one record. Its cells belong together: the account number, the name, the barangay, the "
            "years unpaid and the amount. Sorting one column on its own breaks that link.",
            ("point", "In Google Sheets", "Select the whole table, including every column, then choose Data, "
             "Sort range, and Advanced range sorting options. Google’s help describes this path. Tick “Data has "
             "header row” so the column titles stay at the top, then choose the column to sort by."),
            ("point", "In Excel", "If you select a single column inside a larger table and sort, Excel shows a "
             "warning and offers to expand the selection. Choose to expand it."),
            ("point", "Before any sort", "Add a column called Row with the numbers 1, 2, 3 and so on. Sorting "
             "by it later puts the table back in its original order."),
            ("quote", "Sort the record, not the cell."),
            ("h", "Sorting to Find Problems"),
            "Sorting is not only for presentation. Putting values in order pushes the unusual ones to the top "
            "or the bottom, where they are easy to see.",
            ("point", "Amount, smallest first", "Zero, negative or blank amounts gather at one end. So do amounts stored as text, the problem Part 16 described, because a sort places text apart from numbers."),
            ("point", "Amount, largest first", "A balance ten times bigger than the next one is either the "
             "most important account in the list or a typing error. Either way, someone should look."),
            ("point", "Names, A to Z", "Near-duplicates sit next to each other: “Dela Cruz, Juan” and “Dela "
             "Cruz, Juan P.” Part 14 explained why these become one taxpayer ID."),
            ("point", "Dates, oldest first", "A date far outside the period, such as a year that has not "
             "happened yet, shows up at the end."),
            ("h", "Filters and Filter Views"),
            "A filter hides the rows that do not match a condition. In a shared sheet, the kind of filter "
            "matters.",
            ("point", "A filter", "Google’s help notes that when you add a filter, anyone with access to the "
             "spreadsheet will see it. If a colleague is working in the same sheet, their rows disappear too."),
            ("point", "A filter view", "A filter view applies only to your view of the spreadsheet, so several "
             "people can filter the same sheet at once in different ways. Create one from the Data menu with "
             "“Create filter view,” then name it."),
            ("point", "View-only access", "The same help page notes that someone who can only view a sheet can "
             "create a temporary filter view that only they can use, and it is not saved."),
            "For the Monday list, a named filter view such as “Delinquent, Poblacion and San Isidro, largest "
            "first” lets anyone open the same view later without disturbing the sheet for others.",
            ("h", "Filter by Condition"),
            ("point", "By values", "Tick the barangays to keep. Simple, but new values that appear later are "
             "not ticked automatically."),
            ("point", "By condition", "Rules such as “greater than or equal to 10,000” or “text contains.” A "
             "rule keeps working when new rows arrive."),
            ("point", "Combine with care", "Filters on two columns keep only rows that pass both. A list of "
             "accounts that are both over ₱10,000 and over three years unpaid can be much shorter than either "
             "list alone."),
            ("h", "Answers That Update Themselves"),
            "A sorted and filtered sheet shows the answer today. A formula can show it every day. Google Sheets "
            "has SORT and FILTER functions that return a new range of results in another place, leaving the "
            "original table as it is.",
            ("point", "FILTER", "=FILTER(A2:E500, C2:C500=\"POBLACION\") returns only the rows where column C, "
             "the barangay, is POBLACION. More conditions can be added as extra arguments, and a row must meet "
             "all of them."),
            ("point", "SORT", "=SORT(A2:E500, 5, FALSE) returns the table sorted by its fifth column, the "
             "amount, from largest to smallest. TRUE would sort from smallest to largest."),
            ("point", "Together", "=SORT(FILTER(A2:E500, (C2:C500=\"POBLACION\")+(C2:C500=\"SAN ISIDRO\")), 5, "
             "FALSE) keeps rows from either barangay, then sorts them. Adding two conditions with a plus sign "
             "means “either one”; listing them as separate arguments means “both.”"),
            ("point", "The top twenty", "Wrap the result in ARRAY_CONSTRAIN(…, 20, 5) to keep the first twenty "
             "rows and five columns."),
            "Put these formulas on a separate tab, such as Monday List, and the list updates when the "
            "delinquency sheet changes. Excel has SORT and FILTER functions too, in recent versions, with "
            "slightly different rules for combining conditions.",
            ("h", "When a Filtered List Is Not Enough"),
            ("point", "Totals by group", "A filter shows rows, not totals by barangay. That is a job for SUMIFS "
             "or a pivot table."),
            ("point", "Hidden rows still count", "Some tools include hidden rows in totals. Check how a total "
             "treats filtered rows before quoting it, as Part 20 of the Business Intelligence series noted for "
             "Data Studio."),
            ("point", "Privacy", "A filtered list of named delinquent taxpayers is personal data. Share it only "
             "with the people who need it, as Part 6 explained."),
            ("h", "The Monday List, Done Right"),
            "After the scrambled sort, the staff member pressed undo, then spot-checked several accounts against the cashier’s records to be sure every name was back with its balance. The analyst added a Row column for next time, then built a Monday List tab "
            "with one SORT and FILTER formula and a note above it with the conditions in words. The head of "
            "office received a list whose rules anyone could read, and the next month’s list took no work at "
            "all.",
            ("h", "Mistakes to Avoid"),
            ("point", "Sorting one column", "Select the whole table, or let Excel expand the selection."),
            ("point", "Filtering a shared sheet", "Use a filter view, so colleagues are not affected."),
            ("point", "Ticking values for a rule", "Use a condition when new values will arrive."),
            ("point", "Quoting totals from a filtered sheet", "Check whether hidden rows are counted."),
            ("h", "Key Takeaways"),
            ("point", "Keep rows together", "Sort the whole table, with a Row column to return to."),
            ("point", "Sort to find problems", "Extremes and near-duplicates gather at the ends and side by side."),
            ("point", "Filter views", "Your own view, without changing anyone else’s."),
            ("point", "SORT and FILTER", "Answers that update when the data does."),
            ("h", "Your Part 22 Exercise"),
            "Make a copy of a list your office uses, or a practice list of thirty made-up accounts with name, "
            "barangay, years unpaid and amount.",
            ("point", "Sort safely", "Add a Row column, sort the whole table by amount, then sort it back."),
            ("point", "Find one problem", "Sort each column in turn and note anything odd at the ends."),
            ("point", "Write the formula", "Build one SORT and FILTER that answers a real question."),
            "Then write the question above the formula in plain words. A list with its rules in words can be "
            "checked by anyone, not only by the person who built it.",
            ("cta", "Read: Data Analytics Series, Part 12", "/blog/data-analytics-part-12-one-row-per-record/"),
            ("cta", "Read: Data Analytics Series, Part 16", "/blog/data-analytics-part-16-dirty-data/"),
            ("cta", "Read: Data Analytics Series, Part 19", "/blog/data-analytics-part-19-first-steps-in-sql/"),
            ("cta", "Read: Data Analytics Series, Part 6", "/blog/data-analytics-part-6-data-ethics-privacy/"),
            ("ask", "Which list does your office rebuild by hand every month that one formula could keep up to date?"),
        ],
    },
    {
        "date": "February 20, 2027",
        "title": "Data Analytics Series, Part 21: Stop Bad Data at the Door, Rules Inside the Database",
        "slug": "data-analytics-part-21-rules-inside-the-database",
        "category": "data",
        "summary": "Cleaning fixes yesterday’s mistakes; rules prevent tomorrow’s. This part builds a receipts "
                   "table in SQLite that refuses duplicates, blanks, negative amounts, badly written dates and "
                   "unknown collectors, tests every rule with a bad row, and explains the two settings that "
                   "quietly switch some protection off.",
        "publish_on": "2027-02-20 21:00",
        "body": [
            "Part 20 ended with a view that cleans the satellite office’s import every week: commas removed, "
            "names trimmed, blanks labeled, repeats dropped. It works. But every week the same mistakes "
            "arrive, and every week the view has to fix them again.",
            "The analyst asks a different question: what if the database simply refused a receipt with no "
            "barangay, an amount below zero, or a date written the wrong way, at the moment someone tries to "
            "save it?",
            "(This is a teaching case: the office, its staff and its figures are fictional. No real "
            "town or taxpayer is described.)",
            "Part 12 stopped errors at the door of a spreadsheet with dropdown lists. This part does the same "
            "for a database. By the end of this post, you will know how to write rules into a table so it "
            "rejects bad rows, what NOT NULL, UNIQUE, CHECK and foreign keys each catch, why SQLite needs two extra steps to be strict, and how to find bad rows that were saved before the rules existed. "
            "Every statement below was run in SQLite, and the results shown are what it returned.",
            ("photo", "blog/data-db-rules.jpg", "Rules inside the database: required values, no repeats, "
             "sensible values and known codes. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Why Rules Belong in the Table"),
            "A form on a screen can check entries, and a careful clerk can check them again. But data can "
            "reach a table by other routes too: an import, a script, a copy from another file. A rule written "
            "into the table itself applies to every one of them, because the database checks it on every "
            "insert and every update.",
            ("quote", "A rule in the table is a check that never gets tired."),
            ("h", "The Table, With Its Rules"),
            "Here is the receipts table, written with a rule on each column. The collectors table it refers to "
            "holds C-04 Reyes and C-07 Lim, as in Part 19.",
            ("point", "The statement", "CREATE TABLE receipts ( receipt_no TEXT NOT NULL PRIMARY KEY, "
             "taxpayer_id TEXT NOT NULL, collector_id TEXT NOT NULL REFERENCES collectors(collector_id), "
             "barangay TEXT NOT NULL CHECK (trim(barangay) <> ''), amount REAL NOT NULL CHECK (amount > 0), "
             "paid_on TEXT NOT NULL CHECK (paid_on IS date(paid_on)) ) STRICT;"),
            "It looks long, but each line is one plain rule. The sections below take them one at a time, each "
            "with a bad row that tests it.",
            ("h", "NOT NULL: A Value Is Required"),
            ("point", "The rule", "NOT NULL means the column must have a value. SQLite’s documentation says "
             "that trying to save NULL there is a constraint violation."),
            ("point", "The test", "A receipt with NULL as its barangay was refused with “NOT NULL constraint "
             "failed: receipts.barangay.”"),
            ("point", "What it misses", "An empty text value is not NULL, so NOT NULL alone lets it through. "
             "That is why the barangay column has a second rule."),
            ("h", "UNIQUE and PRIMARY KEY: No Repeats"),
            ("point", "The rule", "A primary key identifies each row, so no two rows may share it. Saving "
             "receipt 004701 a second time was refused with “UNIQUE constraint failed: receipts.receipt_no.”"),
            ("point", "Why it matters", "This is the duplicate import from Part 20, stopped before it is saved "
             "instead of removed after."),
            ("point", "Watch for NULL", "SQLite’s documentation says that for UNIQUE rules, NULL values count as "
             "different from each other, so several rows may hold NULL in a UNIQUE column. Pair UNIQUE with NOT "
             "NULL when a value must always be there."),
            ("h", "CHECK: Values That Make Sense"),
            "A CHECK rule is a condition each row must meet. SQLite tests it every time a row is inserted or "
            "updated.",
            ("point", "No blank barangay", "CHECK (trim(barangay) <> '') refused a receipt whose barangay was "
             "an empty value: “CHECK constraint failed.”"),
            ("point", "No zero or negative amount", "CHECK (amount > 0) refused a receipt for -500."),
            ("point", "Dates in one format", "CHECK (paid_on IS date(paid_on)) refused “11/09/2026.” It also "
             "refused “2026-02-30,” because SQLite’s date function turned that into 2026-03-02, which does not "
             "match what was typed."),
            "The date rule uses IS rather than =, and the reason is worth knowing. SQLite’s date function "
            "returns NULL for “11/09/2026,” and comparing anything with NULL using = gives NULL. SQLite’s "
            "documentation says a CHECK that comes out NULL is not a violation. In a test table with "
            "CHECK (paid_on = date(paid_on)), “11/09/2026” was saved without complaint. IS treats NULL as a "
            "value to compare, so the rule fails as it should.",
            ("h", "Foreign Keys: Only Known Codes"),
            ("point", "The rule", "REFERENCES collectors(collector_id) says every receipt’s collector must "
             "exist in the collectors table, the link Part 14 sketched on paper."),
            ("point", "The surprise", "A receipt for collector C-99, who does not exist, was saved. SQLite’s "
             "documentation explains that foreign key rules are switched off by default and must be switched "
             "on for each connection."),
            ("point", "The switch", "After PRAGMA foreign_keys = ON; the same kind of receipt was refused with "
             "“FOREIGN KEY constraint failed.” Run it at the start of every session, before any other "
             "statement. The documentation notes that it has no effect inside an open transaction."),
            ("h", "STRICT: Types That Are Enforced"),
            "The table ends with the word STRICT, and that is the second switch. In an ordinary SQLite table, "
            "a column’s type is a preference, not a rule.",
            ("point", "Without STRICT", "In an ordinary test table, an amount column declared as REAL "
             "accepted “1,250.00” and stored it as text. That is how the commas in Part 20 got in."),
            ("point", "With STRICT", "The receipts table refused “1,250.00” with “cannot store TEXT value in "
             "REAL column.” It accepted “800,” because that text converts cleanly, and stored it as the number "
             "800."),
            ("point", "Which versions", "SQLite’s documentation says STRICT tables arrived in version 3.37.0, "
             "released in November 2021. Check your version with sqlite3 --version before relying on it."),
            ("h", "Bad Rows That Were Already There"),
            "Rules protect the table from the moment they exist. Rows saved while foreign keys were off "
            "are not checked again when the switch is turned on, and old data copied in from an earlier table "
            "deserves a look before anyone relies on it.",
            ("point", "Unknown codes", "PRAGMA foreign_key_check; lists rows whose foreign key points nowhere. "
             "In the test, it found the C-99 receipt saved before the switch was on."),
            ("point", "Other rules", "Run the rule as a query. SELECT receipt_no FROM receipts WHERE amount "
             "<= 0 OR paid_on IS NOT date(paid_on); finds rows that break the amount or date rules."),
            ("point", "Fix at the source", "Look up the paper receipt, correct the row, and note it in the "
             "cleaning log from Part 16."),
            ("h", "The Satellite Office, One Week Later"),
            "The analyst rebuilt the receipts table with its rules, switched foreign keys on in the import "
            "script, and ran the next week’s file. Four rows were refused, each with a message that named "
            "the rule. The satellite office fixed them the same afternoon and sent them again. The view from "
            "Part 20 still runs, but now it has less to clean.",
            ("h", "Mistakes to Avoid"),
            ("point", "Trusting NOT NULL for blanks", "Add a CHECK for empty text too."),
            ("point", "Comparing with = in a CHECK", "A NULL result passes. Use IS where NULL can appear."),
            ("point", "Forgetting the switch", "Turn foreign keys on in every session."),
            ("point", "Assuming types are enforced", "Use STRICT, or check types with TYPEOF."),
            ("h", "Key Takeaways"),
            ("point", "Rules in the table", "They apply to every route data takes, every time."),
            ("point", "Four kinds", "NOT NULL, UNIQUE, CHECK and foreign keys, each catching a different "
             "mistake."),
            ("point", "Two switches", "PRAGMA foreign_keys = ON and STRICT tables."),
            ("point", "Old rows", "Check them with foreign_key_check and with each rule run as a query."),
            ("h", "Your Part 21 Exercise"),
            "In your SQLite practice file, create a small receipts table with at least one rule of each kind "
            "and the word STRICT at the end.",
            ("point", "Test each rule", "Try to insert one bad row per rule, and read the message each time."),
            ("point", "Try the NULL trap", "Write a date rule with = and then with IS, and insert “11/09/2026” "
             "into each."),
            ("point", "Switch it on", "Insert an unknown collector before and after PRAGMA foreign_keys = ON."),
            "Then list the mistakes your office’s data arrives with most often, and write one rule for each. "
            "Every rule written is a mistake you no longer clean by hand.",
            ("cta", "Read: Data Analytics Series, Part 20", "/blog/data-analytics-part-20-cleaning-with-sql/"),
            ("cta", "Read: Data Analytics Series, Part 14", "/blog/data-analytics-part-14-databases-101/"),
            ("cta", "Read: Data Analytics Series, Part 12", "/blog/data-analytics-part-12-one-row-per-record/"),
            ("cta", "Read: Data Analytics Series, Part 19", "/blog/data-analytics-part-19-first-steps-in-sql/"),
            ("ask", "Which mistake would you most like your office’s data to refuse at the door?"),
        ],
    },
    {
        "date": "February 15, 2027",
        "title": "Data Analytics Series, Part 20: Cleaning Data With SQL, Without Touching the Original",
        "slug": "data-analytics-part-20-cleaning-with-sql",
        "category": "data",
        "summary": "Messy imports reach databases too. This part cleans a small table of receipts with SQL: "
                   "finding the mess with DISTINCT and COUNT, fixing spaces and letter case, turning text "
                   "amounts into numbers, filling blanks, removing duplicates, and saving the rules in a view "
                   "so the original stays as it arrived.",
        "publish_on": "2027-02-15 21:00",
        "body": [
            "The analyst imports a week of receipts from a satellite office into the database from Part 19 and "
            "runs a quick total. It comes back as 3,354. The receipts on paper add up to 8,300.50.",
            "No error message appeared. The query ran, the database answered, and the answer was wrong by more "
            "than half. The amounts had arrived as text with commas in them, and the database had quietly read "
            "“1,250.00” as 1.",
            "(The story is made up for teaching, and so are its office, people and figures. No real "
            "town or taxpayer is described.)",
            "Part 16 listed the usual kinds of dirty data, and Part 18 cleaned text and dates in a spreadsheet. "
            "This part does the same work in SQL. Read to the end and you will know how to find the mess "
            "with DISTINCT and COUNT, fix spaces and letter case, turn text into numbers, handle blanks and "
            "empty values, find and remove duplicates, and keep your cleaning rules in a view that leaves the "
            "original table untouched. Every query below was run in SQLite on the sample data, and the results "
            "shown are what it returned.",
            ("photo", "blog/data-sql-cleaning.jpg", "Cleaning with SQL: find the mess, fix text, fix numbers, "
             "save the rules in a view. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "The Sample Table"),
            "The import went into a table called raw_receipts, with five columns: receipt number, taxpayer ID, "
            "barangay, amount and payment date. Every column was imported as text. It has eight rows, and they "
            "hold the problems this post will fix.",
            ("point", "Barangay names", "“Poblacion,” “ poblacion ” with spaces at both ends, and "
             "“POBLACION” in capitals, plus “San Isidro” and “Sto. Niño.”"),
            ("point", "Gaps", "One receipt with an empty barangay, and one with no value at all, which SQL "
             "calls NULL."),
            ("point", "Amounts as text", "Values such as “1,250.00” and “2,400.50,” with commas."),
            ("point", "A duplicate", "Receipt 004606 appears twice, the same row imported two times."),
            ("quote", "Clean the copy, keep the original, and write every rule down."),
            ("h", "Step 1: Find the Mess Before Fixing It"),
            ("point", "See the variants", "SELECT DISTINCT barangay FROM raw_receipts; returned seven values "
             "for what are really three barangays and two kinds of gap: three spellings of Poblacion, San Isidro, Sto. Niño, an empty "
             "value and NULL."),
            ("point", "Count the gaps", "SELECT COUNT(barangay), COUNT(*) FROM raw_receipts; returned 6 and 8. "
             "COUNT of a column skips NULL, while COUNT(*) counts every row. The empty value is not NULL, so it "
             "was counted."),
            ("point", "Count the duplicates", "SELECT COUNT(*), COUNT(DISTINCT receipt_no) FROM raw_receipts; "
             "returned 8 and 7: eight rows, but only seven different receipt numbers."),
            "These three queries change nothing. They tell you what to fix, and they give you numbers to check "
            "against once the cleaning is done.",
            ("h", "Step 2: Spaces and Letter Case"),
            ("point", "The query", "SELECT DISTINCT UPPER(TRIM(barangay)) FROM raw_receipts;"),
            ("point", "What it returned", "POBLACION, SAN ISIDRO, an empty value, NULL, and STO. NIñO. The three "
             "spellings of Poblacion became one."),
            ("point", "What TRIM does", "SQLite’s documentation says TRIM with one argument removes spaces from "
             "both ends. It does not touch other characters, such as tabs. A second argument lists the "
             "characters to remove instead."),
            ("point", "Watch the ñ", "The ñ stayed small in “STO. NIñO.” SQLite’s documentation says its "
             "built-in UPPER converts only lower-case ASCII letters, the basic English alphabet, so letters "
             "such as ñ are left as they are. Grouping is not affected here, because Sto. Niño appears in only one form. A name typed once as “NIÑO” and once as “Niño” would stay two groups, so check names with "
             "letters outside the basic alphabet by eye."),
            "In a spreadsheet, the same fixes came from TRIM and UPPER in Part 18. The difference is where the "
            "rule lives: in SQL, it is written once in a query and applied to every row the query reads.",
            ("h", "Step 3: Turn Text Into Numbers"),
            ("point", "The trap", "SELECT CAST(amount AS REAL) FROM raw_receipts; turned “1,250.00” into 1.0 "
             "and “2,400.50” into 2.0. SQLite’s documentation explains why: when it converts text to a number, "
             "it reads the longest part at the start that looks like a number and ignores the rest. Reading "
             "stops at the comma."),
            ("point", "The fix", "SELECT CAST(REPLACE(amount, ',', '') AS REAL) FROM raw_receipts; removes the "
             "commas first. “1,250.00” became 1250.0 and “2,400.50” became 2400.5."),
            ("point", "Check the type", "SELECT typeof(amount) returned text for the raw column, and "
             "typeof( CAST( REPLACE(amount, ',', '') AS REAL ) ) returned real. The TYPEOF function shows what the "
             "database is really holding."),
            "This is the same lesson as the amounts stored as text in Part 16 of the Business Intelligence "
            "series: a number that is really text can drop out of a total, or count as the wrong amount, "
            "without any warning.",
            ("h", "Step 4: Blanks and NULL"),
            "An empty value and NULL are different things in a database. An empty text value is a value that "
            "happens to have no characters. NULL means no value at all. A clean column should use one of them, "
            "not both.",
            ("point", "Empty to NULL", "NULLIF(TRIM(barangay), '') returns NULL when the trimmed value is empty, "
             "and the value itself otherwise."),
            ("point", "NULL to a label", "COALESCE(x, '(no barangay)') returns the first value that is not "
             "NULL. Together, COALESCE( NULLIF( TRIM(barangay), '' ), '(no barangay)' ) gave both problem receipts, "
             "004605 and 004606, the same clear label."),
            ("point", "Label, do not guess", "Do not fill a missing barangay with the most common one. A label "
             "keeps the gap visible, so someone can find the paper receipt and fix the source."),
            ("h", "Step 5: Find and Remove Duplicates"),
            ("point", "Find them", "SELECT receipt_no, COUNT(*) FROM raw_receipts GROUP BY receipt_no HAVING "
             "COUNT(*) > 1; returned one row: 004606, appearing 2 times. HAVING filters groups after they are "
             "counted, the way WHERE filters rows before."),
            ("point", "Check before removing", "Look at both rows. Here they matched in every column, so one "
             "was an import repeat. If two rows share a receipt number but differ in amount, that is a question "
             "for the cashier, not something to delete."),
            ("point", "Remove exact repeats", "SELECT DISTINCT over all the columns keeps one copy of rows that "
             "match completely."),
            ("h", "Step 6: Save the Rules in a View"),
            "A view is a saved query with a name. It holds no data of its own. Each time it is used, it reads "
            "the original table and applies the rules again.",
            ("point", "The view", "CREATE VIEW clean_receipts AS SELECT DISTINCT receipt_no, taxpayer_id, "
             "COALESCE( NULLIF( UPPER( TRIM(barangay) ), '' ), '(NO BARANGAY)' ) AS barangay, "
             "CAST( REPLACE(amount, ',', '') AS REAL ) AS amount, paid_on FROM raw_receipts;"),
            ("point", "Use it like a table", "SELECT barangay, COUNT(*) AS receipts, SUM(amount) AS total FROM "
             "clean_receipts GROUP BY barangay ORDER BY total DESC; returned POBLACION with 3 receipts and "
             "4,450.50, (NO BARANGAY) with 2 and 2,300, STO. NIñO with 1 and 900, and SAN ISIDRO with 1 and 650."),
            ("point", "Check against Step 1", "SELECT COUNT(*), SUM(amount) FROM clean_receipts; returned 7 rows "
             "and 8,300.50. Seven matches the distinct receipt count from Step 1, and the total matches the "
             "paper receipts."),
            "The raw table still holds every row exactly as it arrived. If a rule turns out to be wrong, you "
            "change the view, and nothing is lost. This is the Raw and Clean tab idea from Part 16 of the "
            "Business Intelligence series, written in SQL.",
            ("h", "The Satellite Office Total, Corrected"),
            "The analyst built the view, ran the totals, and wrote a short note beside the query: which rules "
            "it applies, the counts before and after, and the two receipts with no barangay. The paper receipts "
            "named the barangays, and the satellite office corrected them at the source. The next week’s import "
            "had commas in the amounts again, and the view handled them without anyone noticing.",
            ("h", "Mistakes to Avoid"),
            ("point", "Summing text", "Check the type with TYPEOF before adding up a column."),
            ("point", "Casting with commas", "Remove commas with REPLACE before CAST."),
            ("point", "Deleting duplicates without looking", "Rows that differ need a person, not a query."),
            ("point", "Cleaning the original", "Keep raw data as it arrived, and clean in a view."),
            ("h", "Key Takeaways"),
            ("point", "Find first", "DISTINCT and COUNT show the mess and give you numbers to check against."),
            ("point", "Fix text", "TRIM and UPPER, knowing what each one leaves alone."),
            ("point", "Fix numbers and gaps", "REPLACE then CAST, and NULLIF with COALESCE."),
            ("point", "Save the rules", "A view keeps the cleaning repeatable and the original safe."),
            ("h", "Your Part 20 Exercise"),
            "In your SQLite practice file from Part 19, make a small table of eight rows with the same kinds of "
            "mess: names with extra spaces and mixed capitals, amounts with commas, one blank and one repeated "
            "row.",
            ("point", "Find the mess", "Run DISTINCT and the two COUNT queries, and write down the numbers."),
            ("point", "Write the view", "Apply TRIM, UPPER, REPLACE, CAST, NULLIF and COALESCE in one view."),
            ("point", "Check the result", "Compare the row count and total from the view with what you expect "
             "by hand."),
            "Then add one new messy row to the raw table and query the view again. If the new row comes out "
            "clean without any change to the view, your rules are working.",
            ("cta", "Read: Data Analytics Series, Part 19", "/blog/data-analytics-part-19-first-steps-in-sql/"),
            ("cta", "Read: Data Analytics Series, Part 16", "/blog/data-analytics-part-16-dirty-data/"),
            ("cta", "Read: Data Analytics Series, Part 18", "/blog/data-analytics-part-18-text-and-dates/"),
            ("cta", "Read: Business Intelligence Series, Part 16", "/blog/business-intelligence-part-16-pipeline-in-sheets/"),
            ("ask", "Which column in your office’s data arrives messy every single time?"),
        ],
    },
    {
        "date": "February 10, 2027",
        "title": "Data Analytics Series, Part 19: First Steps in SQL, Asking a Database Questions",
        "slug": "data-analytics-part-19-first-steps-in-sql",
        "category": "data",
        "summary": "SQL lets you ask a database a question in one short sentence. This part walks through six "
                   "beginner queries on a small treasury database, from listing receipts to totals by "
                   "collector and barangay, with every result shown and a few safe habits for working on "
                   "real data.",
        "publish_on": "2027-02-10 21:00",
        "body": [
            "In Part 14, the analyst sketched three linked tables on paper: taxpayers, receipts and "
            "collectors. The office has since built them in SQLite, the free database engine that keeps a "
            "whole database in one file.",
            "Now the head of office asks: “How much did each collector receive in October, and how many "
            "receipts was that?” In a spreadsheet, the analyst would filter, copy and add up. In the database, "
            "the answer is one short query.",
            "(This is a teaching case: the office, its staff and its figures are fictional. No real "
            "town or taxpayer is described.)",
            "This part is a first look at SQL, the language used to ask databases questions. By the end of this post, you will know how to open a database, choose columns, filter rows, filter by date, "
            "total by group, join two tables, count distinct values, and keep your data safe while you "
            "practice. Every query below was run on the sample data, and the results shown are what it "
            "returned.",
            ("photo", "blog/data-sql.jpg", "First steps in SQL: SELECT, WHERE, GROUP BY and JOIN on a small "
             "treasury database. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "What SQL Is"),
            "SQL, short for Structured Query Language, is a language for working with data stored in tables. "
            "It is used by SQLite and by other database systems such as PostgreSQL and MySQL. The basic "
            "statements in this post look much the same in each of them.",
            "A query reads almost like an English sentence: select these columns, from this table, where "
            "this is true. The database does the searching and adding up.",
            ("quote", "A good query is a question written so precisely that a computer can answer it."),
            ("h", "Opening the Database"),
            ("point", "The program", "The SQLite project provides a free command-line program called sqlite3 "
             "(sqlite3.exe on Windows), available from its download page."),
            ("point", "Opening a file", "At the command prompt, sqlite3 treasury.db opens that database. "
             "SQLite’s documentation notes that if the file does not exist, it is created."),
            ("point", "Practice on a copy", "Following the habits from Part 15, copy the database file first "
             "and practice on the copy."),
            ("h", "The Sample Data"),
            "The examples use three small tables. To keep them short, the receipts here come from one series, "
            "so the receipt number alone identifies each receipt.",
            ("point", "collectors", "C-04 Reyes and C-07 Lim."),
            ("point", "taxpayers", "Four taxpayers, T-00125, T-00131, T-00140 and T-00152, each with a "
             "name and a barangay: one in San Isidro and three in Poblacion."),
            ("point", "receipts", "Six receipts, 004512 to 004517, each with a taxpayer ID, a collector ID, "
             "a payment date and an amount. Four were paid in October 2026 and two in November."),
            ("h", "Query 1: Choose the Columns"),
            ("point", "The query", "SELECT receipt_no, paid_on, amount FROM receipts;"),
            ("point", "What it returns", "All six receipts, showing only the three columns named. SELECT "
             "picks the columns, FROM names the table, and the semicolon ends the statement."),
            "SELECT * returns every column. It is handy for a first look, but naming the columns you need "
            "keeps the result readable and avoids showing fields nobody asked for.",
            ("h", "Query 2: Filter the Rows"),
            ("point", "The query", "SELECT receipt_no, amount FROM receipts WHERE amount >= 1000;"),
            ("point", "What it returns", "Four receipts: 004512 for 1,250, 004514 for 2,400, 004516 for "
             "1,250 and 004517 for 1,800."),
            "WHERE keeps only the rows for which the condition is true. Conditions can use =, <>, <, >, <= "
            "and >=, and can be combined with AND and OR.",
            ("h", "Query 3: Filter by Date"),
            ("point", "The query", "SELECT receipt_no, amount FROM receipts WHERE paid_on BETWEEN "
             "'2026-10-01' AND '2026-10-31';"),
            ("point", "What it returns", "The four October receipts, 004512 to 004515."),
            "The dates are stored as text in year-month-day order, the same order recommended for file names "
            "in Part 15. In that order, sorting the text also sorts the dates, so BETWEEN works. BETWEEN "
            "includes both end dates.",
            ("h", "Query 4: Totals by Group"),
            ("point", "The query", "SELECT collector_id, COUNT(*) AS receipts, SUM(amount) AS total FROM "
             "receipts GROUP BY collector_id ORDER BY total DESC;"),
            ("point", "What it returns", "C-07 with 3 receipts totaling 4,850, then C-04 with 3 receipts "
             "totaling 3,300."),
            "GROUP BY puts rows with the same collector together. COUNT and SUM work on each group. AS gives "
            "a result column a readable name, and ORDER BY ... DESC lists the largest total first. Adding the "
            "October date condition from Query 3 as a WHERE line answers the head of office’s question for "
            "October only.",
            ("h", "Query 5: Join Two Tables"),
            "The barangay is not in the receipts table. It belongs to the taxpayer, as Part 14 explained. A "
            "JOIN brings the two tables together through the key they share.",
            ("point", "The query", "SELECT t.barangay, SUM(r.amount) AS total FROM receipts AS r JOIN "
             "taxpayers AS t ON r.taxpayer_id = t.taxpayer_id GROUP BY t.barangay ORDER BY total DESC;"),
            ("point", "What it returns", "Poblacion with 5,650 and San Isidro with 2,500."),
            "The letters r and t are short names for the two tables, so each column can say which table it "
            "comes from. The ON line is the foreign key from Part 14 at work: each receipt’s taxpayer ID is "
            "matched with the same ID in the taxpayers table.",
            ("h", "Query 6: Count Distinct Values"),
            ("point", "The query", "SELECT COUNT(DISTINCT taxpayer_id) AS taxpayers_who_paid FROM receipts;"),
            ("point", "What it returns", "4. Six receipts were issued, but one taxpayer paid twice and "
             "another paid twice, so four different taxpayers paid."),
            "This is the count Part 14 promised would be easy once each taxpayer had one ID: no guessing "
            "which spellings are the same person.",
            ("h", "Reading a Query in the Right Order"),
            "A query is written starting with SELECT, but it helps to read it in the order the work happens:",
            ("point", "FROM and JOIN", "Which tables, and how they connect."),
            ("point", "WHERE", "Which rows to keep."),
            ("point", "GROUP BY", "How to group the rows that are left."),
            ("point", "SELECT and ORDER BY", "What to show, and in what order."),
            "Reading it this way makes a wrong result easier to trace. If a total is too high, check the "
            "JOIN and the WHERE first.",
            ("h", "Safe Habits for Real Data"),
            ("point", "SELECT only reads", "Every query in this post only reads data. Statements such as "
             "UPDATE and DELETE change it, and a missing WHERE line can change every row at once."),
            ("point", "Look before you change", "Before an UPDATE or DELETE, run a SELECT with the same WHERE "
             "line and check exactly which rows it returns."),
            ("point", "Work on a copy", "Practice and test on a copy of the database file, and keep backups "
             "as in Part 15."),
            ("point", "Check against a known total", "Compare a new query’s grand total with a report you "
             "trust. If they differ, find out why before sharing the result."),
            ("h", "The October Question, Answered"),
            "The analyst added WHERE paid_on BETWEEN '2026-10-01' AND '2026-10-31' to Query 4 and had the "
            "answer in seconds, with the receipt count beside each total. The query went into a text file "
            "named with the date and a short description, so next month the same question takes only a "
            "change of dates.",
            ("h", "Mistakes to Avoid"),
            ("point", "Dates in mixed formats", "Store dates as year-month-day so they sort and filter "
             "correctly."),
            ("point", "Forgetting the JOIN condition", "Without ON, rows can be matched with every row of "
             "the other table, and totals multiply."),
            ("point", "Changing data without a SELECT first", "Look at the rows before you change them."),
            ("point", "Sharing an unchecked total", "Compare it with a figure you already trust."),
            ("h", "Key Takeaways"),
            ("point", "SELECT and FROM", "Choose the columns and the table."),
            ("point", "WHERE", "Keep only the rows you need, including date ranges."),
            ("point", "GROUP BY with COUNT and SUM", "Totals by collector, barangay or account."),
            ("point", "JOIN", "Connect tables through their keys, as designed in Part 14."),
            ("h", "Your Part 19 Exercise"),
            "Download the sqlite3 program and create a practice file with one small table you make up, such "
            "as a few receipts.",
            ("point", "Run three queries", "One SELECT with chosen columns, one WHERE, and one GROUP BY with "
             "SUM."),
            ("point", "Check by hand", "Add up the same totals on paper or in a spreadsheet and compare."),
            ("point", "Save your queries", "Keep them in a text file with a clear name."),
            "Then write one question your office asks every month, and try to write it as a single query.",
            ("cta", "Read: Data Analytics Series, Part 14", "/blog/data-analytics-part-14-databases-101/"),
            ("cta", "Read: Data Analytics Series, Part 15", "/blog/data-analytics-part-15-naming-versions-backups/"),
            ("cta", "Read: Data Analytics Series, Part 18", "/blog/data-analytics-part-18-text-and-dates/"),
            ("cta", "Read: Business Intelligence Series, Part 16", "/blog/business-intelligence-part-16-pipeline-in-sheets/"),
            ("ask", "Which monthly question in your office would you most like to answer with one query?"),
        ],
    },
    {
        "date": "February 5, 2027",
        "title": "Data Analytics Series, Part 18: Taming Text and Dates, Names, Pesos and Day-Month Puzzles",
        "slug": "data-analytics-part-18-text-and-dates",
        "category": "data",
        "summary": "An export from an older system can arrive with names in capitals, amounts with peso signs, "
                   "receipt numbers that lose their zeros and dates the spreadsheet cannot read. This part "
                   "shows the text and date formulas that fix each one, with a few traps to avoid.",
        "publish_on": "2027-02-05 21:00",
        "body": [
            "The analyst receives an export of last year’s business permit payments from an older system. "
            "Names are in capitals with the family name first: “DELA CRUZ, JUAN P.” Amounts look like "
            "“₱1,250.00.” Receipt numbers such as 004512 have turned into 4512. The payment dates read "
            "“15/01/2026,” and the spreadsheet will not sort them as dates.",
            "Every value is there. None of it is ready to use.",
            "(The story is made up for teaching, and so are its office, people and figures. No real "
            "town or taxpayer is described.)",
            "Part 16 found the usual kinds of dirty data. This part fixes two stubborn kinds: "
            "text and dates. Read to the end and you will know how to keep codes from losing their "
            "zeros, how to change and split text safely, how to turn peso text into numbers, how to build "
            "dates from text the spreadsheet cannot read, and how to show dates without breaking them.",
            ("photo", "blog/data-text-dates.jpg", "Taming text and dates: codes kept as text, names split, pesos "
             "turned into numbers and dates built from their parts. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "Codes Are Text, Even When They Look Like Numbers"),
            "A receipt number, a taxpayer ID or a barangay code is a label, not a quantity. Nobody adds two "
            "receipt numbers together. But when a spreadsheet sees 004512, it may treat it as the number 4512 "
            "and drop the zeros.",
            ("point", "Before pasting", "Format the column as plain text first. In Google Sheets this is under "
             "Format, then Number, then Plain text. Values pasted into it keep their zeros."),
            ("point", "If the zeros are already gone", "=TEXT(A2, \"000000\") turns 4512 back into the text "
             "004512, as long as you know every number should have six digits."),
            ("point", "Why it matters", "As Part 14 explained, keys link tables. If one table has 004512 "
             "and another has 4512, the link fails without any warning."),
            ("quote", "If you would never add it up, store it as text."),
            ("h", "Capitals and Small Letters"),
            ("point", "UPPER", "=UPPER(A2) turns “Dela Cruz” into “DELA CRUZ.”"),
            ("point", "LOWER", "=LOWER(A2) turns everything into small letters."),
            ("point", "PROPER", "=PROPER(A2) capitalizes the first letter of each word: “DELA CRUZ, JUAN P.” "
             "becomes “Dela Cruz, Juan P.”"),
            "PROPER is handy for display, but it cannot know how a person writes their own name. One family "
            "may write “dela Cruz” and another “Dela Cruz,” and a name such as “McArthur” comes out as "
            "“Mcarthur.” For letters and notices, check names against the source record.",
            "For matching, the safer habit is to compare in one case. =UPPER(A2)=UPPER(B2) treats “Dela Cruz” "
            "and “DELA CRUZ” as the same, without changing either one.",
            ("h", "Splitting and Joining Text"),
            "A name written as “DELA CRUZ, JUAN P.” holds two fields in one cell. Splitting it makes each part "
            "usable on its own.",
            ("point", "SPLIT in Google Sheets", "=SPLIT(A2, \",\") divides the text at the comma, giving "
             "“DELA CRUZ” and “ JUAN P.” in two cells. Wrap each result in TRIM to remove the leftover space."),
            ("point", "A trap to know", "Google’s help explains that SPLIT, by default, splits at each "
             "character in the delimiter. =SPLIT(A2, \", \") would split at every comma and every space, "
             "breaking “DELA CRUZ” in two. Use a single character, or set the third argument to FALSE."),
            ("point", "Taking part of a code", "For a code such as SI-2026-00451, =LEFT(A2, 2) gives “SI,” "
             "=MID(A2, 4, 4) gives “2026,” and =RIGHT(A2, 5) gives “00451.”"),
            ("point", "Joining", "=B2 & \" \" & C2 joins two cells with a space between them."),
            "Keep the original column. Splitting is done in new columns, so the source stays as it arrived, "
            "as Part 15 advised.",
            ("h", "Pesos Stored as Text"),
            "“₱1,250.00” contains a peso sign and a comma, so it is text, and SUM leaves it out. Remove the "
            "extra characters, then convert.",
            ("point", "The formula", "=VALUE(SUBSTITUTE(SUBSTITUTE(A2, \"₱\", \"\"), \",\", \"\")). The inner "
             "SUBSTITUTE removes the peso sign, the outer one removes the commas, and VALUE turns what is "
             "left into a number."),
            ("point", "Other labels", "If some amounts say “PHP 1,250.00,” add one more SUBSTITUTE for "
             "“PHP” and wrap the result in TRIM."),
            ("point", "Check it", "Compare the count of numbers before and after with =COUNT. Every amount "
             "row should now be counted."),
            "Once the values are numbers, format the column as currency if you want the peso sign shown. "
            "The sign then becomes part of the display, not part of the value.",
            ("h", "How Spreadsheets Store Dates"),
            "Behind every real date, a spreadsheet stores a number that counts days. Google’s help for "
            "DATEVALUE notes that it returns integers that can be used in formulas. That is why real dates "
            "can be sorted, subtracted and grouped by month, and text that only looks like a date cannot.",
            ("point", "Locale decides the default", "Google’s help explains that a spreadsheet’s locale sets "
             "its default date, number and currency formats. It is under File, then Settings."),
            ("point", "Why exports break", "If an export writes the day first, such as 15/01/2026, and the "
             "spreadsheet’s locale expects the month first, there is no month 15, so the value stays text. "
             "Worse, 03/04/2026 is accepted, but possibly as the wrong date."),
            ("h", "Building Dates From Their Parts"),
            "The safest fix does not ask the spreadsheet to guess. It takes the day, month and year out of "
            "the text and builds the date with DATE(year, month, day).",
            ("point", "Day first, such as 15/01/2026", "=DATE(VALUE(RIGHT(A2, 4)), VALUE(MID(A2, 4, 2)), "
             "VALUE(LEFT(A2, 2))). This works when every value has two-digit days and months."),
            ("point", "Year first, such as 2026-01-15", "=DATE(VALUE(LEFT(A2, 4)), VALUE(MID(A2, 6, 2)), "
             "VALUE(RIGHT(A2, 2)))."),
            ("point", "With a time attached, such as 2026-01-15 09:42", "Take the first ten characters with "
             "LEFT(A2, 10), then use the year-first formula on that."),
            ("point", "Check the result", "=ISNUMBER(B2) should be TRUE for every row, and sorting the new "
             "column should give a sensible first and last date."),
            "Before converting, look at a handful of rows by eye. If one export mixes day-first and "
            "month-first dates, no formula can tell 03/04 apart, and those rows go back to the source.",
            ("h", "Showing Dates Without Breaking Them"),
            ("point", "Format, do not convert", "To show a date as 2026-01-15 or January 15, 2026, change the "
             "cell’s number format. The value stays a date."),
            ("point", "TEXT for labels", "=TEXT(B2, \"yyyy-mm-dd\") gives the year-month-day text used in file "
             "names in Part 15. =TEXT(B2, \"mmmm\") gives the month name for a chart label."),
            ("point", "Do not calculate on TEXT", "The result of TEXT is text again. Keep the real date column "
             "for sorting and arithmetic."),
            ("h", "The Permit Payments, Cleaned"),
            "The analyst pasted the export into a column formatted as plain text, so the receipt numbers kept "
            "their zeros. Names were split at the comma and trimmed, and kept in capitals for matching, with "
            "a separate display column for notices. Amounts went through the SUBSTITUTE and VALUE formula, "
            "and =COUNT confirmed every row. Dates were built with DATE from their parts.",
            "The yearly report took one afternoon instead of two days, and the cleaning steps went into "
            "the change log, ready for the next export.",
            ("h", "Mistakes to Avoid"),
            ("point", "Letting codes become numbers", "Format code columns as plain text before pasting."),
            ("point", "Trusting PROPER with names", "Use it for display, and check against the source."),
            ("point", "Splitting at two characters", "In Google Sheets, SPLIT splits at each character unless "
             "told otherwise."),
            ("point", "Letting the spreadsheet guess dates", "Build dates from their parts when the order is "
             "not certain."),
            ("h", "Key Takeaways"),
            ("point", "Codes are text", "Keep IDs and receipt numbers as text so zeros and links survive."),
            ("point", "Clean text in new columns", "UPPER, PROPER, SPLIT, TRIM and SUBSTITUTE, with the "
             "original kept."),
            ("point", "Pesos to numbers", "Remove the sign and commas, then use VALUE."),
            ("point", "Dates from parts", "DATE(year, month, day) removes the guesswork."),
            ("h", "Your Part 18 Exercise"),
            "Take one export your office receives from another system.",
            ("point", "Find the codes", "List the columns that should be text, and check whether any lost "
             "their zeros."),
            ("point", "Fix one text column", "Split, trim or convert it in a new column."),
            ("point", "Fix one date column", "Build real dates with DATE and confirm with ISNUMBER."),
            "Then write the steps down in order. Next time the export arrives, the cleaning becomes a "
            "routine instead of a puzzle.",
            ("cta", "Read: Data Analytics Series, Part 16", "/blog/data-analytics-part-16-dirty-data/"),
            ("cta", "Read: Data Analytics Series, Part 10", "/blog/data-analytics-part-10-data-types-and-table-shapes/"),
            ("cta", "Read: Data Analytics Series, Part 15", "/blog/data-analytics-part-15-naming-versions-backups/"),
            ("cta", "Read: Business Intelligence Series, Part 16", "/blog/business-intelligence-part-16-pipeline-in-sheets/"),
            ("ask", "Which export in your office arrives with dates or amounts the spreadsheet cannot read?"),
        ],
    },
    {
        "date": "January 31, 2027",
        "title": "Data Analytics Series, Part 17: Samples and Margin of Error, Checking 400 Receipts Instead of 12,000",
        "slug": "data-analytics-part-17-samples-margin-of-error",
        "category": "data",
        "summary": "You do not always have to check every record to know how many are wrong. This part explains "
                   "random samples, the margin of error and how to choose a sample size, with a treasury "
                   "example worked out step by step and a plain way to report the result.",
        "publish_on": "2027-01-31 21:00",
        "body": [
            "After the cleanup in Part 16, the head of office asks a fair question: how many of last year’s "
            "12,000 receipts have a wrong barangay code in the system? Checking every receipt against its "
            "paper copy would take two staff members several weeks.",
            "The analyst suggests another way. Check 400 receipts chosen at random, count the errors, and "
            "use that count to estimate the rate for all 12,000, with an honest statement of how far off the "
            "estimate could be.",
            "The head of office is doubtful. “Four hundred out of twelve thousand? That is barely three "
            "percent.” It is a reasonable worry, and this post answers it.",
            "(This is a teaching case: the office, its staff and its figures are fictional. No real "
            "town or taxpayer is described.)",
            "Part 13 showed how the way data is collected can tilt a result. This part shows how a small, "
            "well-chosen sample can describe a large group. By the end of this post, you will know what makes "
            "a sample random, how to draw one in a spreadsheet, what a margin of error means, how to choose a "
            "sample size, and how to report the result so nobody reads more into it than it holds.",
            ("photo", "blog/data-sampling.jpg", "Sampling: a random sample, a margin of error, a sample size "
             "and a careful report. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Population and Sample"),
            ("point", "Population", "Every record you want to know about: here, all 12,000 receipts from last "
             "year."),
            ("point", "Sample", "The records you actually check: here, 400 of them."),
            ("point", "Estimate", "A number worked out from the sample, used as a stand-in for the true "
             "number in the population, which nobody knows until every record is checked."),
            "Checking every record is called a census. A census has no sampling error, but it costs the "
            "most time. A sample costs far less, and in exchange you accept a known amount of uncertainty.",
            ("quote", "A sample does not give the exact answer. It gives a close one, with its limits written beside it."),
            ("h", "What Makes a Sample Random"),
            "In a simple random sample, every record in the population has the same chance of being chosen. "
            "That is what lets the sample speak for the whole.",
            ("point", "Not the first 400", "The first 400 receipts of the year come from January, which may "
             "have different encoders, workloads or errors than other months."),
            ("point", "Not the easy 400", "Receipts from the counter nearest the records room are easier to "
             "pull, but they may not be typical. This is the sampling bias described in Part 13."),
            ("point", "Not hand-picked", "Choosing receipts that “look normal” quietly removes the unusual "
             "ones, which may be where the errors are."),
            ("h", "Drawing a Random Sample in a Spreadsheet"),
            ("point", "1. Start with the full list", "One row per receipt, as in Part 12: all 12,000."),
            ("point", "2. Add a random number", "In a new column, type =RAND() and copy it down. In both Google "
             "Sheets and Excel, RAND returns a random number between 0 and 1."),
            ("point", "3. Freeze it", "RAND gives new numbers every time the sheet recalculates. Copy the "
             "column and paste it back as values only, so the sample stays the same."),
            ("point", "4. Sort and take the top", "Sort the whole list by the random column and take the first "
             "400 rows. That is your sample."),
            ("point", "5. Save the list", "Keep the 400 receipt numbers in their own file, so anyone can check "
             "the same receipts later."),
            ("h", "The Result, and How Sure We Can Be"),
            "Two clerks check the 400 receipts against the paper copies and find 24 with a wrong barangay "
            "code. That is 24 ÷ 400 = 6%.",
            "But a different random 400 could have given 5% or 7%. The margin of error says how far the "
            "estimate is likely to be from the true rate. For a percentage from a simple random sample, "
            "the usual formula at 95% confidence is:",
            ("point", "Margin of error", "1.96 × √( p × (1 − p) ÷ n ), where p is the sample rate as a "
             "decimal and n is the sample size."),
            ("point", "Worked out", "p = 0.06 and n = 400. Then 0.06 × 0.94 ÷ 400 = 0.000141. Its square root "
             "is about 0.0119. Times 1.96 gives about 0.023, or 2.3 percentage points."),
            ("point", "The range", "6% minus 2.3 points is 3.7%; 6% plus 2.3 points is 8.3%. Applied to 12,000 "
             "receipts, that is roughly 440 to 1,000 receipts with a wrong code."),
            "The 1.96 comes from the normal curve and goes with 95% confidence. The meaning of “95% "
            "confidence” is easy to misread. It means that if the office drew many random samples the same "
            "way and built a range from each, about 95% of those ranges would contain the true rate. It does "
            "not promise that this particular range is correct.",
            ("h", "How Big Should the Sample Be?"),
            "The same formula can be turned around to find the sample size for a margin of error you choose. "
            "When you have no idea what the rate will be, the cautious choice is p = 0.5, which gives the "
            "largest sample:",
            ("point", "Sample size", "n = 0.25 × (1.96 ÷ E)², where E is the margin of error you want, as a "
             "decimal. Round up."),
            ("point", "E = 5 points", "0.25 × (1.96 ÷ 0.05)² = 384.16, so 385 records."),
            ("point", "E = 3 points", "0.25 × (1.96 ÷ 0.03)² = 1,067.1, so 1,068 records."),
            ("point", "E = 2 points", "0.25 × (1.96 ÷ 0.02)² = 2,401 records."),
            "Notice the pattern: cutting the margin of error in half takes about four times as many records. "
            "Precision gets expensive quickly, so decide how precise the answer needs to be before choosing "
            "the size.",
            ("h", "Does the Population Size Matter?"),
            "Less than you might expect. The formula above has no population size in it at all. For smaller "
            "populations, a finite population correction trims the sample a little: divide the starting sample size n by 1 + (n − 1) ÷ N, where N is the population size.",
            ("point", "For 12,000 receipts", "385 ÷ (1 + 384 ÷ 12,000) is about 373.1, so 374 records instead "
             "of 385."),
            "That is why 400 out of 12,000 is not “barely three percent” in the way the head of office feared. "
            "What sets the precision is mainly the number of records checked, not the share of the population "
            "they make up.",
            ("h", "What the Margin of Error Does Not Cover"),
            "The margin of error measures only one thing: the chance difference between a random sample and "
            "the whole population. It does not cover other problems.",
            ("point", "A sample that is not random", "If the 400 were hand-picked, the formula still produces "
             "a number, but the number means little."),
            ("point", "Checking mistakes", "If a clerk misreads a paper receipt, that error is not in the "
             "margin."),
            ("point", "Missing records", "Receipts never entered into the system cannot be sampled from it."),
            ("point", "Very few errors found", "The formula is an approximation. When a sample turns up only a "
             "handful of errors, or none, ask someone with statistics training before reporting a margin."),
            ("h", "Reporting the Result"),
            ("point", "Say how the sample was drawn", "“A random sample of 400 of last year’s 12,000 receipts.”"),
            ("point", "Give the estimate and the range", "“About 6% had a wrong barangay code, with a margin "
             "of error of about 2.3 percentage points at 95% confidence, or roughly 440 to 1,000 receipts.”"),
            ("point", "Say what it does not cover", "“This does not include receipts that were never entered.”"),
            ("point", "Keep the list", "Attach or file the list of sampled receipt numbers."),
            ("h", "The Receipts Check, Decided"),
            "The head of office accepted the estimate. A rate between about 4% and 8% was high enough to "
            "justify fixing the codes, so the office used a mapping table from Part 16 to correct them, then "
            "drew a fresh random sample of 400 to check the fix. That second sample found 2 errors, and the "
            "analyst, following the rule above, reported the count plainly instead of a margin.",
            ("h", "Mistakes to Avoid"),
            ("point", "Sampling the easy records", "Use a random number to choose, not convenience."),
            ("point", "Judging size by percentage", "The number checked matters more than the share of the "
             "population."),
            ("point", "Reporting one number alone", "Give the range and the confidence level with it."),
            ("point", "Treating the margin as the whole story", "It covers chance, not bias or checking errors."),
            ("h", "Key Takeaways"),
            ("point", "Random means equal chance", "Every record must have the same chance of being chosen."),
            ("point", "Margin of error", "1.96 × √(p(1 − p) ÷ n) at 95% confidence, for a rate from a random "
             "sample."),
            ("point", "Size from precision", "About 385 records for ±5 points; four times as many to halve "
             "that."),
            ("point", "Report honestly", "Estimate, range, how the sample was drawn, and what it leaves out."),
            ("h", "Your Part 17 Exercise"),
            "Pick one list in your office that is too long to check in full, such as receipts, permits or "
            "notices.",
            ("point", "Choose a margin", "Decide how precise the answer needs to be, and work out the sample "
             "size."),
            ("point", "Draw the sample", "Use RAND, freeze it, sort, and take the top rows."),
            ("point", "Check and calculate", "Count the problems, work out the rate and its margin of error."),
            "Then write the result in one sentence that a head of office could read without help, with the "
            "range included.",
            ("cta", "Read: Data Analytics Series, Part 13", "/blog/data-analytics-part-13-bias-in-data/"),
            ("cta", "Read: Data Analytics Series, Part 16", "/blog/data-analytics-part-16-dirty-data/"),
            ("cta", "Read: Data Analytics Series, Part 12", "/blog/data-analytics-part-12-one-row-per-record/"),
            ("cta", "Read: Business Intelligence Series, Part 17", "/blog/business-intelligence-part-17-who-sees-what/"),
            ("ask", "Which list in your office has never been checked because it seemed too long to check?"),
        ],
    },
    {
        "date": "January 26, 2027",
        "title": "Data Analytics Series, Part 16: Dirty Data, the Usual Suspects and How to Spot Them",
        "slug": "data-analytics-part-16-dirty-data",
        "category": "data",
        "summary": "A sheet can look tidy and still count one barangay as three. This part lines up the usual "
                   "suspects in treasury data, from duplicates and stray spaces to numbers stored as text and "
                   "impossible amounts, with a quick test to spot each one and a ten-minute scan to run "
                   "before any analysis.",
        "publish_on": "2027-01-26 21:00",
        "body": [
            "The head of office asks a simple question: how many business permits were renewed in each "
            "barangay this year? The analyst opens the permits sheet, which three encoders filled in, and "
            "makes a quick count by barangay.",
            "The town has 24 barangays. The count shows 31. “Poblacion,” “Pob.” and “Pob” each have their "
            "own line, and several other barangays are split the same way. A few renewals also appear twice. "
            "The totals are wrong before any analysis has started.",
            "The data is not fake, and the encoders were not careless. It is dirty: correct in spirit, but "
            "not yet fit to count.",
            "(The story is made up for teaching, and so are its office, people and figures. No real "
            "town or taxpayer is described.)",
            "Part 15 was about keeping data files safe. This part looks inside the file. Read to the end and you will know the usual kinds of dirty data, a quick test to spot each one in a "
            "spreadsheet, the first safe step to fix it, and a short scan to run before you trust any total.",
            ("photo", "blog/data-dirty-data.jpg", "The usual suspects in dirty data: duplicates, inconsistent "
             "names, stray spaces and numbers stored as text. (Illustration: Butch Mahinay, aumahinay.dev)",
             "medium"),
            ("h", "What Makes Data Dirty"),
            "Dirty data is data that is incomplete, incorrect or inconsistent in ways that can mislead an "
            "analysis. Google’s Data Analytics Certificate groups it into types such as duplicate, outdated, "
            "incomplete, incorrect and inconsistent data.",
            "In a treasury spreadsheet, those types show up as a handful of familiar problems. Each one below "
            "comes with a test you can run in Google Sheets or Excel, and a first step that does not destroy "
            "anything.",
            ("quote", "Clean data is not data with no problems. It is data whose problems you have found."),
            ("h", "Suspect 1: Duplicates"),
            "The same record entered twice. It happens when two encoders type the same batch, when an export "
            "is pasted twice, or when a corrected row is added without removing the old one.",
            ("point", "How to spot it", "Use the record’s key, such as the receipt number with its series "
             "from Part 14. =COUNTIFS(A:A, A2, B:B, B2)>1 returns TRUE when the same number and series, in columns A and B, appear more than once."),
            ("point", "Look before removing", "Two rows with the same date, name and amount are not always "
             "duplicates. Two receipts can match by chance. Only the key, or the source document, can say."),
            ("point", "A note on the built-in tool", "Google Sheets has a Remove duplicates tool. Its help page "
             "notes that values that differ only in letter case are treated as duplicates. Check what it "
             "will remove, and work on a copy."),
            ("h", "Suspect 2: Inconsistent Names and Codes"),
            "The same thing written in more than one way: “Pob.” and “Poblacion,” “RPT” and “Real Property "
            "Tax,” or a collector’s name with and without a middle initial. Each version is counted as "
            "something different.",
            ("point", "How to spot it", "List the distinct values in the column with =UNIQUE(D2:D), sort the "
             "list, and read it. Near-twins sit next to each other."),
            ("point", "First step", "Make a small mapping table: each version found, and the standard name it "
             "should be. Add a column that looks up the standard name, instead of retyping the original."),
            ("point", "Stop it coming back", "Use a dropdown list for that column, as shown in Part 12."),
            ("h", "Suspect 3: Extra and Hidden Spaces"),
            "“Reyes” and “Reyes ” look the same on screen, but the second has a space at the end, and a "
            "spreadsheet treats them as different values. Lookups fail and counts split for no visible reason.",
            ("point", "How to spot it", "=LEN(C2)<>LEN(TRIM(C2)) returns TRUE when a cell has spaces at the "
             "ends or doubled inside."),
            ("point", "First step", "=TRIM(C2) in a new column removes them."),
            ("point", "The space TRIM misses", "Microsoft’s help explains that Excel’s TRIM removes the "
             "ordinary space character but not the non-breaking space, character 160, which can arrive in "
             "text copied from web pages. Google’s help for Sheets says the same of its TRIM. "
             "=TRIM(SUBSTITUTE(C2, CHAR(160), \" \")) handles both."),
            ("h", "Suspect 4: Numbers Stored as Text"),
            "An amount that looks like 1,250.00 may be stored as text, especially after an export or a paste "
            "from another program. A SUM can leave it out, and the total comes up short without any error.",
            ("point", "How to spot it", "=ISNUMBER(F2) returns FALSE for a number stored as text. Another "
             "clue: in both Excel and Google Sheets, numbers line up on the right by default, while text lines "
             "up on the left. A column of amounts with a few left-aligned cells deserves a look."),
            ("point", "First step", "=VALUE(F2) in a new column converts text that looks like a number into a "
             "real number."),
            ("point", "Check the total", "Compare =SUM of the original column with =SUM of the converted one. "
             "The difference is the money the first total was missing."),
            ("h", "Suspect 5: Mixed Date Formats"),
            "A date typed as 03/04/2026 can mean March 4 or April 3, depending on who typed it and how the "
            "spreadsheet is set up. Other dates arrive as text, for example from an export, and the spreadsheet cannot sort them by date.",
            ("point", "How to spot it", "Spreadsheets store real dates as numbers, so =ISNUMBER(B2) returns "
             "FALSE for a date that is only text. Sorting the column also helps: text dates gather in one "
             "block, apart from the real ones."),
            ("point", "First step", "Agree on one format for new entries, such as the year-month-day order "
             "from Part 15, and fix the old ones in a new column. Ambiguous dates go back to the source "
             "document, not to a guess."),
            ("h", "Suspect 6: Missing Values"),
            "A blank cell can mean “zero,” “not yet known,” “not applicable” or “forgot to type.” Those are "
            "four different facts, and a blank hides which one it is.",
            ("point", "How to spot it", "=COUNTBLANK(F2:F500) counts the blanks in a column. Also look for "
             "stand-ins such as “N/A,” “none,” a dash or 0 used to mean “unknown.”"),
            ("point", "First step", "Do not fill a blank amount with zero or an average just to make the sheet "
             "complete. Find the source document, or mark the row so it can be counted separately."),
            ("point", "Report it", "If 40 of 600 permits have no barangay, say so beside the chart, instead of "
             "leaving them out quietly."),
            ("h", "Suspect 7: Impossible or Unlikely Values"),
            "An amount with an extra zero, a payment dated in 2062, a negative tax due, or a permit fee far "
            "above any fee in the schedule. Some are typing errors. Some are real and unusual.",
            ("point", "How to spot it", "Sort each number and date column from smallest to largest, then the "
             "other way, and read both ends. =MIN and =MAX do the same for a quick look."),
            ("point", "Check, do not delete", "A large amount may be a large business paying its real tax. "
             "Compare the row with the receipt or the assessment before changing anything."),
            ("point", "Set limits", "Data validation can reject a date outside the year or an amount below "
             "zero at the moment it is typed."),
            ("h", "Suspect 8: Outdated Records"),
            "A business that closed last year still listed as active, or a taxpayer’s old address. Each value "
            "was correct once.",
            ("point", "How to spot it", "Add a “last updated” column, and sort by it. Records not touched in "
             "a long time are the ones to confirm first."),
            ("point", "First step", "Update the record in one place, as Part 14 suggested, so the change "
             "reaches every row that points to it."),
            ("h", "Keep a Cleaning Log"),
            "Every fix changes the data, so write it down. A short log, like the change log from Part 15, "
            "lists what was found, how many rows, and what was done: “Mapped 7 barangay spellings to the "
            "standard list. Removed 6 duplicate renewals after checking receipt numbers.”",
            "The log lets someone else repeat the cleaning next month, and it answers the question “Why does "
            "your total differ from the raw file?” before anyone asks it.",
            ("h", "A Ten-Minute Dirty-Data Scan"),
            ("point", "1. Keys", "Count duplicates in the key column."),
            ("point", "2. Text columns", "List the distinct values, sorted, and read them."),
            ("point", "3. Spaces", "Run the LEN and TRIM test on names and codes."),
            ("point", "4. Numbers and dates", "Run ISNUMBER on every amount and date column."),
            ("point", "5. Blanks", "Count blanks and stand-ins in each important column."),
            ("point", "6. Both ends", "Sort each number and date column both ways and read the extremes."),
            "Ten minutes is a rough guide for a sheet of a few hundred rows. The point is to run the same scan "
            "every time, before any total leaves the office.",
            ("h", "The Permits Sheet, Cleaned"),
            "The analyst ran the scan on a copy of the permits sheet. A mapping table turned seven spellings "
            "into the standard barangay names, and the count fell from 31 to 24. Six renewals appeared twice "
            "because two encoders had typed the same batch; the receipt numbers confirmed it. Twelve fees "
            "were stored as text and were missing from the first total.",
            "The new count went to the head of office with one line underneath: “Cleaned on January 26; "
            "cleaning log attached.”",
            ("h", "Mistakes to Avoid"),
            ("point", "Cleaning the original", "Work on a copy, and keep the raw file as it arrived."),
            ("point", "Deleting what looks odd", "Check unusual values against the source first."),
            ("point", "Filling blanks with guesses", "A blank is a question, not a zero."),
            ("point", "Cleaning without a log", "Write down every fix so it can be repeated and explained."),
            ("h", "Key Takeaways"),
            ("point", "Dirty is not fake", "Dirty data is real data that is not yet fit to count."),
            ("point", "Know the suspects", "Duplicates, inconsistent names, spaces, text numbers, dates, "
             "blanks, odd values and old records."),
            ("point", "Spot before you fix", "A quick formula test finds each one."),
            ("point", "Fix safely", "Work in new columns or copies, and keep a cleaning log."),
            ("h", "Your Part 16 Exercise"),
            "Take one spreadsheet your office uses for counting, such as permits, receipts or notices.",
            ("point", "Run the scan", "Go through the six steps above on a copy of the sheet."),
            ("point", "Count the suspects", "Write down how many rows each kind of problem affects."),
            ("point", "Fix one", "Pick the problem that changes the totals most, fix it in a new column, and "
             "log it."),
            "Then compare the total before and after. The gap shows how much the dirty data was hiding.",
            ("cta", "Read: Data Analytics Series, Part 12", "/blog/data-analytics-part-12-one-row-per-record/"),
            ("cta", "Read: Data Analytics Series, Part 15", "/blog/data-analytics-part-15-naming-versions-backups/"),
            ("cta", "Read: Data Analytics Series, Part 10", "/blog/data-analytics-part-10-data-types-and-table-shapes/"),
            ("cta", "Read: Business Intelligence Series, Part 16", "/blog/business-intelligence-part-16-pipeline-in-sheets/"),
            ("ask", "Which column in your office’s data has the most ways of spelling the same thing?"),
        ],
    },
    {
        "date": "January 21, 2027",
        "title": "Data Analytics Series, Part 15: Naming, Versions and Backups, Keeping Data Files Safe",
        "slug": "data-analytics-part-15-naming-versions-backups",
        "category": "data",
        "summary": "“Final,” “final2” and “final-REAL” are how good analysis gets lost. This part gives simple "
                   "rules for naming data files, keeping versions you can trust, and backing them up with the "
                   "3-2-1 rule, so you can find, and trust, the right file.",
        "publish_on": "2027-01-21 21:00",
        "body": [
            "The analyst needs last quarter’s cleaned collections file. The shared folder holds "
            "“collections.xlsx,” “collections final.xlsx,” “collections final2.xlsx,” “collections final "
            "USE THIS.xlsx” and “Copy of collections final2.xlsx.” Each one has slightly different totals. "
            "The person who made them has since moved to another office.",
            "Then the computer that held the only other copy stops starting up. The cleaned file the head of "
            "office approved is somewhere in that folder, or it is gone.",
            "Nothing in the analysis was wrong. The problem was how the files were named, saved and copied.",
            "(This is a teaching case: the office, its staff and its figures are fictional. No real "
            "town or taxpayer is described.)",
            "Part 14 showed how to organize data inside a database. This part is about the files themselves. "
            "By the end of this post, you will know a naming pattern that sorts itself, a simple way to keep "
            "versions, the 3-2-1 backup rule, and how to test that a backup actually works.",
            ("photo", "blog/data-file-safety.jpg", "Keeping data files safe: clear names, numbered versions, "
             "three copies and a restore test. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Names That Sort Themselves"),
            "A good file name tells you what is inside before you open it, and puts related files in a useful "
            "order when sorted by name.",
            ("point", "Date first, year-month-day", "Write dates as 2026-10-31, not 10-31-2026 or Oct 31. "
             "Written this way, files sort in calendar order by name alone, and nobody wonders whether 10-11 "
             "means October 11 or November 10. This order follows the ISO 8601 date standard."),
            ("point", "Then what it is", "A short, plain description: collections-q3, rpt-delinquent-list, "
             "business-permits."),
            ("point", "Then the stage", "raw, clean or report, so nobody mistakes an untouched export for a "
             "checked file."),
            ("point", "Then the version", "v01, v02, v03, with a leading zero so v10 sorts after v09."),
            ("point", "No spaces or special characters", "Use hyphens or underscores. Some systems and "
             "scripts handle spaces, slashes and symbols poorly."),
            "Put together: 2026-09-30_collections-q3_clean_v03.xlsx. Anyone in the office can tell what it "
            "is, when it is from and which version it is.",
            ("quote", "A file name is the first line of documentation."),
            ("h", "Versions You Can Trust"),
            "A file called “final” can still change the next day. Numbered versions are easier to follow.",
            ("point", "Raw stays raw", "Keep the original export untouched, named with the stage raw. All "
             "cleaning happens on copies. If a cleaning step goes wrong, you can start again from the raw "
             "file."),
            ("point", "Number every saved change", "When a change matters, save as the next version number "
             "instead of overwriting. Old versions stay available if a question comes up."),
            ("point", "Keep a short change log", "Add a sheet or a text file that lists each version, the "
             "date, who made it and what changed: “v03: removed 12 duplicate receipts, fixed barangay codes.”"),
            ("point", "Mark the approved one", "When the head of office approves a version, write that in the "
             "change log with the date. The approved version is a fact, not a guess based on the file name."),
            "Google Sheets files, and Excel files stored in OneDrive or SharePoint, keep a version "
            "history of their own, which helps. It does not replace clear names and a change log, because it records when a "
            "file changed, not why.",
            ("h", "Inside the File: Sheets and Columns"),
            "Good names matter inside the file too, not only on the file itself.",
            ("point", "Name every sheet", "Replace Sheet1 and Sheet2 with names such as Receipts, Lists, Notes "
             "and Summary, so formulas that point to them are easier to read."),
            ("point", "Name columns plainly", "Use short, clear headers such as receipt_no, date, barangay and "
             "amount. Avoid headers that only make sense to the person who wrote them."),
            ("point", "Keep the change log inside", "A sheet called Changes, at the end of the workbook, "
             "travels with the file wherever it is copied."),
            ("point", "Note the source", "On the Notes sheet, write where the raw data came from and the date "
             "it was exported, so the next person can trace it back."),
            ("h", "One Home for Each File"),
            ("point", "One shared folder", "Agree on one folder where the working files live, not on "
             "anyone’s desktop or phone."),
            ("point", "A simple folder layout", "For example: one folder per year, and inside it raw, clean "
             "and reports."),
            ("point", "Office accounts", "Keep shared files in an account that belongs to the office, so they "
             "stay when someone transfers or retires."),
            ("point", "Access to match the data", "Files with taxpayer names and amounts carry personal "
             "information. Share them only with the people who need them, as discussed in Part 6."),
            ("h", "The 3-2-1 Backup Rule"),
            "A well-known rule for backups, often credited to photographer Peter Krogh and adopted in "
            "guidance from the U.S. Cybersecurity and Infrastructure Security Agency, has three parts.",
            ("point", "3 copies", "Keep at least three copies of data that matters: the working copy and two "
             "backups."),
            ("point", "2 kinds of storage", "Keep the copies on at least two different kinds of storage, such "
             "as the office computer and an external drive, or a drive and a cloud account."),
            ("point", "1 copy elsewhere", "Keep at least one copy away from the office, or in a separate "
             "account, so a fire, flood or theft does not take every copy at once."),
            "For a small treasury office, this can be as simple as the working files in the shared folder, a "
            "weekly copy to an external drive kept in a locked cabinet, and a copy in a separate cloud account "
            "that belongs to the office. Ask your IT staff or data protection officer which services the "
            "office is allowed to use for personal data.",
            ("h", "Test the Restore, Not Just the Backup"),
            "A backup you have never restored is a hope, not a backup. Once a month, try it.",
            ("point", "Pick one file", "Choose a file at random from the backup."),
            ("point", "Restore it to a new place", "Copy it back to a test folder, never over the working "
             "copy."),
            ("point", "Open and check", "Does it open? Do its totals match the change log?"),
            ("point", "Write it down", "Note the date and the result. If the restore failed, fix the backup "
             "before you need it."),
            ("h", "The Collections Folder, Cleaned Up"),
            "The analyst gathered the five files, compared their totals with the approved report, and found "
            "that “collections final2.xlsx” matched. It was renamed 2026-09-30_collections-q3_clean_v02.xlsx, "
            "with a change log entry noting the approval date. The other files went into an archive folder "
            "with their own version numbers, instead of being deleted.",
            "The office then set up the 3-2-1 copies and a monthly restore test on the first working day of "
            "each month.",
            ("h", "Mistakes to Avoid"),
            ("point", "“Final” in the name", "Use version numbers, and record approval in the change log."),
            ("point", "Overwriting the raw export", "Clean a copy. Keep the original as it arrived."),
            ("point", "Backups in the same place", "A copy on the same computer is lost with the computer."),
            ("point", "Never testing", "Restore a file each month to prove the backup works."),
            ("h", "Key Takeaways"),
            ("point", "Names that sort", "Date first, then what, then stage, then version."),
            ("point", "Versions with a log", "Number each change and write down why."),
            ("point", "3-2-1", "Three copies, two kinds of storage, one elsewhere."),
            ("point", "Test the restore", "A backup counts only if it can be opened."),
            ("h", "Your Part 15 Exercise"),
            "Open the folder where your office keeps its most important data file.",
            ("point", "Count the copies", "How many versions of the same file are there, and can you tell "
             "which one was approved?"),
            ("point", "Rename one", "Rename the approved version using the date, what, stage and version "
             "pattern, and start a change log."),
            ("point", "Check 3-2-1", "Count the copies of that file and where they are kept."),
            "Then restore one backup copy to a test folder and open it. If you cannot, you have found the most "
            "important task for this week.",
            ("cta", "Read: Data Analytics Series, Part 14", "/blog/data-analytics-part-14-databases-101/"),
            ("cta", "Read: Data Analytics Series, Part 12", "/blog/data-analytics-part-12-one-row-per-record/"),
            ("cta", "Read: Data Analytics Series, Part 6", "/blog/data-analytics-part-6-data-ethics-privacy/"),
            ("cta", "Read: Business Intelligence Series, Part 10", "/blog/business-intelligence-part-10-keeping-bi-honest/"),
            ("ask", "How many copies of your office’s most important data file exist, and where are they?"),
        ],
    },
    {
        "date": "January 16, 2027",
        "title": "Data Analytics Series, Part 14: Databases 101, Tables, Primary Keys and Foreign Keys",
        "slug": "data-analytics-part-14-databases-101",
        "category": "data",
        "summary": "A spreadsheet that repeats the same taxpayer’s name on every receipt is one typo away from "
                   "counting one person as two. This part explains, in plain words, how a database splits "
                   "data into linked tables using primary keys and foreign keys, with a three-table treasury "
                   "example you can sketch on paper.",
        "publish_on": "2027-01-16 21:00",
        "body": [
            "The collections sheet has a row for every receipt, and each row repeats the taxpayer’s full name "
            "and address. Over the year, one taxpayer appears as “Dela Cruz, Juan,” “Juan dela Cruz” and "
            "“Dela Cruz, Juan P.” A count of taxpayers who paid comes out higher than it should, because one "
            "person has become three.",
            "Then the taxpayer moves to a new address. The clerk updates it on the latest receipt row, but the "
            "older rows keep the old address. Now the sheet holds two addresses for the same person, and "
            "nobody can tell which one is current.",
            "Both problems have the same cause: the same fact is typed in many places. Databases are designed "
            "to avoid exactly that.",
            "(The story is made up for teaching, and so are its office, people and figures. No real "
            "town or taxpayer is described.)",
            "Part 12 showed how to lay out one clean table. This part shows how several tables work together. "
            "Read to the end and you will know what a database table, a record and a field are, what "
            "primary and foreign keys do, how tables are linked, and how to sketch a small treasury database "
            "before anyone builds it.",
            ("photo", "blog/data-database-keys.jpg", "Three linked tables: taxpayers, receipts and "
             "collectors. Each receipt points to one taxpayer and one collector by their keys. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "The Words You Need"),
            ("point", "Database", "An organized collection of data. In the kind of database "
             "this post describes, the data is kept in tables that can be linked to each other."),
            ("point", "Table", "A set of rows and columns about one kind of thing: taxpayers, receipts or "
             "collectors. It follows the same rules as the clean sheet from Part 12."),
            ("point", "Record", "One row in a table: one taxpayer, one receipt."),
            ("point", "Field", "One column in a table: a name, a date, an amount."),
            "If you have kept a clean spreadsheet with one row per record, you already know most of this. What "
            "a database adds is the idea of keys.",
            ("h", "Primary Key: One Value, One Record"),
            "A primary key is a field whose value identifies exactly one record in its table. No two records may share it, and it should never be left blank.",
            ("point", "Taxpayers table", "A taxpayer ID such as T-00125. Names are a poor key because two "
             "people can share a name, and the same person can be written in different ways."),
            ("point", "Receipts table", "The official receipt number together with its series, since numbers "
             "are unique only within a series."),
            ("point", "Collectors table", "A collector ID such as C-04."),
            "A good primary key does not change. A name or an address can change; an ID assigned once and "
            "never reused is a safer key.",
            ("quote", "Give every record one value that belongs to it alone."),
            ("h", "Foreign Key: Pointing to Another Table"),
            "A foreign key is a field in one table that holds the primary key of a record in another table. "
            "It is how tables point to each other.",
            "In the receipts table, instead of typing the taxpayer’s name and address on every receipt, you "
            "type only the taxpayer ID. That ID is a foreign key: it points to one row in the taxpayers table, "
            "where the name and address are kept once.",
            ("point", "Receipt 004512", "Taxpayer ID T-00125, collector ID C-04, date, amount."),
            ("point", "Taxpayer T-00125", "Name, address, contact details, typed once."),
            ("point", "Collector C-04", "Name and assigned barangays, typed once."),
            "When the taxpayer moves, the address is changed in one row of the taxpayers table, and every "
            "receipt that points to T-00125 now leads to the new address.",
            ("h", "How Tables Relate"),
            ("point", "One-to-many", "One taxpayer can have many receipts, but each receipt belongs to one "
             "taxpayer. Receipts and taxpayers are linked this way."),
            ("point", "One-to-one", "One record matches exactly one record in another table, for "
             "example when sensitive details are kept in a separate table with tighter access."),
            ("point", "Many-to-many", "One taxpayer can own several properties, and one property can have "
             "several owners. This needs a third table in between, such as an ownership table with one row "
             "for each taxpayer–property pair."),
            ("h", "Why Split the Data at All?"),
            ("point", "Each fact once", "A name or address typed once cannot disagree with itself."),
            ("point", "Easier counting", "Counting taxpayers who paid means counting distinct taxpayer IDs, "
             "not guessing which spellings are the same person."),
            ("point", "Rules the database can enforce", "A database can refuse a receipt whose taxpayer ID "
             "does not exist in the taxpayers table, or a second record with the same primary key."),
            ("point", "Tighter access", "Personal details can sit in one table that fewer people can open, "
             "while the receipts can be analyzed by ID. This supports the Data Privacy Act duties discussed "
             "in Part 6."),
            ("h", "Sketching a Treasury Database on Paper"),
            "Before anyone installs anything, draw it. A sheet of paper is enough.",
            ("point", "1. List the things", "Write one box for each kind of thing you record: taxpayers, "
             "receipts, collectors."),
            ("point", "2. Choose the keys", "Under each box, write its primary key first."),
            ("point", "3. List the fields", "Add the fields that belong to that thing and to nothing else. The "
             "taxpayer’s address belongs in Taxpayers, not in Receipts."),
            ("point", "4. Draw the links", "Draw a line from each foreign key to the table it points to, and "
             "mark which side is the “many.”"),
            ("point", "5. Test with a question", "Pick a real question, such as “How much did each collector "
             "receive from taxpayers in San Isidro last month?” Trace on paper how the tables would answer "
             "it. If you cannot, a field or a link is missing."),
            ("h", "Does This Field Belong Here?"),
            "When you are unsure where a field goes, ask what it describes.",
            ("point", "It describes the taxpayer", "Name, address, contact number. It goes in Taxpayers, "
             "even if you first saw it on a receipt."),
            ("point", "It describes the payment", "Date, amount, revenue source, receipt number. It goes in "
             "Receipts."),
            ("point", "It describes the collector", "Name, assigned barangays. It goes in Collectors."),
            ("point", "It describes a pair", "The share of a property owned by one taxpayer describes the "
             "taxpayer and the property together, so it goes in the ownership table between them."),
            ("h", "Spreadsheet or Database?"),
            "A spreadsheet can be enough for one person working with one table. A database starts to make "
            "sense when several tables need to be linked, several people enter data at the same time, or "
            "rules such as unique receipt numbers must be enforced every time.",
            "A free way to learn is SQLite, a database engine that stores a whole database in a single "
            "ordinary file, with no server to set up.",

            ("h", "Mistakes to Avoid"),
            ("point", "Names as keys", "Use an ID that never changes and never repeats."),
            ("point", "Copying fields across tables", "If the taxpayer’s address appears in the receipts "
             "table, it can drift out of date. Keep it in one place."),
            ("point", "Reusing old IDs", "An ID given to a closed account should not be given to a new one."),
            ("point", "Building before sketching", "Draw the tables and test them with a question first."),
            ("h", "Key Takeaways"),
            ("point", "Tables, records, fields", "Rows and columns about one kind of thing."),
            ("point", "Primary key", "One value, one record, never blank, never repeated."),
            ("point", "Foreign key", "A pointer to a record in another table."),
            ("point", "Each fact once", "Splitting data into linked tables keeps it consistent."),
            ("h", "Your Part 14 Exercise"),
            "Take one spreadsheet your office uses that repeats the same names or addresses on many rows.",
            ("point", "Find the things", "List each kind of thing it records, such as taxpayers, receipts or "
             "permits."),
            ("point", "Choose the keys", "Write a primary key for each, and mark where a foreign key would "
             "replace a repeated name."),
            ("point", "Draw it", "Sketch the boxes and lines on paper, and test them with one real question."),
            "Count how many columns would disappear from the main sheet once each repeated fact lives in its "
            "own table. That number shows how much room there was for errors.",
            ("cta", "Read: Data Analytics Series, Part 12", "/blog/data-analytics-part-12-one-row-per-record/"),
            ("cta", "Read: Data Analytics Series, Part 13", "/blog/data-analytics-part-13-bias-in-data/"),
            ("cta", "Read: Data Analytics Series, Part 6", "/blog/data-analytics-part-6-data-ethics-privacy/"),
            ("cta", "Read: Business Intelligence Series, Part 5", "/blog/business-intelligence-part-5-data-modeling/"),
            ("ask", "Which name or address does your office type again and again that belongs in its own table?"),
        ],
    },
    {
        "date": "January 11, 2027",
        "title": "Data Analytics Series, Part 13: Bias in Data, and How to Catch It",
        "slug": "data-analytics-part-13-bias-in-data",
        "category": "data",
        "summary": "Data can be accurate and still lead to the wrong answer when it leans one way. This part "
                   "explains four kinds of bias, sampling, observer, interpretation and confirmation, with "
                   "treasury examples and a short checklist for catching each one.",
        "publish_on": "2027-01-11 21:00",
        "body": [
            "The office wants to know how taxpayers feel about its service, so it runs a short survey at the "
            "counter for two weeks. The results are excellent: nine out of ten say the service is fast and "
            "friendly. The report goes up with a confident headline.",
            "A month later, a councilor mentions that several residents have complained about long waits and "
            "unclear notices. How can both be true?",
            "Look at who answered. The survey reached only people who came to the counter, during the two "
            "quietest weeks of the year, and who had time to stay a few minutes after paying. The people who "
            "gave up waiting, who never came because the notice confused them, or who came during the January "
            "rush, were never asked. Every answer was real. The sample was not the whole picture.",
            "(This is a teaching case: the office, its staff and its figures are fictional. No real "
            "town, councilor or taxpayer is described.)",
            "Part 11 tested whether a source can be trusted, and Part 12 put the data in a clean sheet. This "
            "part asks a different question: does the data, or the way we read it, lean one way? Stay with me to the end, and you will know four common kinds of bias, how each shows up in treasury work, and a "
            "simple check for each.",
            ("photo", "blog/data-bias.jpg", "Four kinds of bias: sampling, observer, interpretation and "
             "confirmation. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "What Bias Means Here"),
            "The Google Data Analytics course defines bias as a conscious or subconscious preference in favor "
            "of or against a person, group of people or thing. In data work, bias is any lean that pushes the "
            "result away from the truth in one direction.",
            "Bias is different from a random error. A typing mistake in one receipt may push a total up or "
            "down by chance. Bias pushes in the same direction "
            "again and again, so collecting more of the same data does not remove it. A bigger survey at the same counter in the same quiet weeks would only repeat the same "
            "lean with more confidence.",
            ("quote", "More data with the same lean is still leaning."),
            ("h", "1. Sampling Bias: Who Was Counted?"),
            "Sampling bias happens when the group you collected data from does not represent the whole group "
            "you want to describe. The counter survey above is one example.",
            ("point", "Treasury example", "Estimating how many businesses operate without a permit by "
             "checking only stores along the main road. The side streets and the barangays far from the town "
             "center may look very different."),
            ("point", "How to catch it", "Write down the whole group your question is about, such as “all "
             "taxpayers” or “all businesses in the municipality.” Then ask who in that group could not have "
             "ended up in your data."),
            ("point", "How to reduce it", "Choose from the full list rather than from whoever is nearby. One "
             "simple way is to take every tenth account from the complete list, so the sample is spread "
             "across the whole list."),
            ("h", "2. Observer Bias: Who Recorded It?"),
            "Observer bias happens when the expectations of the person collecting the data affect what gets "
            "recorded. Two people looking at the same thing can write it down differently.",
            ("point", "Treasury example", "Collectors marking visited accounts as “refused to pay” or “not "
             "home.” One collector who expects resistance may write “refused” for a door that simply was not "
             "answered. The count of refusals then depends on who visited, not only on what happened."),
            ("point", "How to catch it", "Compare the same measure across the people who record it. If one "
             "collector reports three times as many refusals as the others in similar areas, look closer "
             "before drawing conclusions."),
            ("point", "How to reduce it", "Write a short definition for each choice, such as “Refused: the "
             "taxpayer said they will not pay.” Train everyone on the same definitions, and use a dropdown "
             "with only those choices, as in Part 12."),
            ("h", "3. Interpretation Bias: How Was It Read?"),
            "Interpretation bias is the tendency to read unclear or neutral data in a way that fits what we "
            "already think. The numbers are fine; the reading leans.",
            ("point", "Treasury example", "Real property tax collections in March are lower than last March. "
             "One reader sees taxpayers becoming less willing to pay. Another notices that a discount "
             "deadline moved, shifting payments into February. The same number supports both readings until "
             "someone checks."),
            ("point", "How to catch it", "Before explaining a change, list at least two other possible causes. "
             "Check each one against the data: Did February rise by about the same amount? Did anything "
             "change in the calendar, the rules or the system?"),
            ("point", "How to reduce it", "Ask someone who was not involved to read the chart and explain it "
             "in their own words before you share your explanation."),
            ("h", "4. Confirmation Bias: What Did We Look For?"),
            "The Google course describes confirmation bias as the tendency to search for or interpret "
            "information in a way that confirms what we already believe. It affects which data we look at in "
            "the first place.",
            ("point", "Treasury example", "A staff member is sure that the new online payment option is "
             "lowering counter collections. They pull the three months where counter collections fell and "
             "stop there, without checking the months where counter collections rose after online payment "
             "started."),
            ("point", "How to catch it", "Ask: “What would I expect to see if I am wrong?” Then go and look "
             "for exactly that."),
            ("point", "How to reduce it", "Write down your question and how you will measure it before you "
             "open the data. Decide in advance which months, which accounts and which comparison you will "
             "use, and stick to them."),
            ("h", "Who Is Missing From the Data?"),
            "Some treasury records describe only the people who already deal with the office. A list of "
            "business taxpayers contains registered businesses. A list of payments contains people who paid. "
            "A complaint log contains people who knew how to complain.",
            "None of these lists is wrong. But a conclusion drawn from them describes only the people on them. "
            "Before saying “taxpayers think” or “businesses are,” check whether the data includes the people "
            "who are not yet on any list.",
            ("h", "A Five-Question Bias Check"),
            "Before sharing any finding, run through five questions. They take a few minutes.",
            ("point", "Who should be in this data?", "Name the whole group the question is about."),
            ("point", "Who could not be in it?", "Look for the people, places or periods that were left out."),
            ("point", "Who recorded it, and how?", "Check whether definitions were written down and shared."),
            ("point", "What else could explain it?", "List at least two other causes and check them."),
            ("point", "What would prove me wrong?", "Look for that evidence on purpose."),
            "Write the answers in a short note with the analysis. If a question cannot be answered, say so in "
            "the report: “The survey covered counter visitors only.” Readers can then judge the result fairly.",
            ("h", "The Survey, Done Again"),
            "The office ran the survey again. This time it chose every tenth taxpayer from the full list of "
            "property accounts, reached them by text message and by a short form at the barangay hall, and "
            "spread the survey across a busy month and a quiet one. The questions were written so they did not "
            "suggest an answer, for example “How long did you wait?” instead of “Was the service fast?”",
            "The results were more mixed and more useful. Most people still rated the staff well, but waiting "
            "time during the January rush and the wording of the notices stood out. Those became the two "
            "things the office set out to fix.",
            ("h", "Mistakes to Avoid"),
            ("point", "Trusting size over fairness", "A large sample from the wrong group is still the wrong "
             "group."),
            ("point", "Undefined categories", "If “refused” is not defined, each person may define it differently."),
            ("point", "One explanation only", "A single explanation, checked against nothing, is a guess."),
            ("point", "Hiding the limits", "State who the data covers, so readers can judge the "
             "finding fairly."),
            ("h", "Key Takeaways"),
            ("point", "Bias leans one way", "More of the same data does not fix it."),
            ("point", "Four kinds", "Sampling, observer, interpretation and confirmation."),
            ("point", "Check who is missing", "Records describe only the people on them."),
            ("point", "Run the five questions", "And write the limits into the report."),
            ("h", "Your Part 13 Exercise"),
            "Pick one finding your office shared in the last year, such as a survey result, a trend or a "
            "comparison.",
            ("point", "Run the check", "Answer the five questions above for that finding."),
            ("point", "Name the lean", "Decide which of the four kinds of bias, if any, could have affected it."),
            ("point", "Write one line", "Draft the sentence that should have gone with it, such as “This "
             "covers only accounts that paid at the counter.”"),
            "If you find no possible bias at all, ask a colleague to try. A second pair of eyes is one of the "
            "simplest checks there is.",
            ("cta", "Read: Data Analytics Series, Part 12", "/blog/data-analytics-part-12-one-row-per-record/"),
            ("cta", "Read: Data Analytics Series, Part 11", "/blog/data-analytics-part-11-roccc-test/"),
            ("cta", "Read: Data Analytics Series, Part 6", "/blog/data-analytics-part-6-data-ethics-privacy/"),
            ("cta", "Read: Business Intelligence Series, Part 10", "/blog/business-intelligence-part-10-keeping-bi-honest/"),
            ("ask", "Which of your office’s numbers describes only the people who already come to the counter?"),
        ],
    },
    {
        "date": "January 6, 2027",
        "title": "Data Analytics Series, Part 12: Spreadsheets Done Right, One Row per Record",
        "slug": "data-analytics-part-12-one-row-per-record",
        "category": "data",
        "summary": "A spreadsheet can look neat to people and still be hard to sort, filter or total. This part "
                   "gives seven layout rules for treasury spreadsheets, from one header row to no merged cells "
                   "and dropdown lists, and shows a messy collections tracker fixed step by step.",
        "publish_on": "2027-01-06 21:00",
        "body": [
            "The revenue unit keeps a collections tracker that everyone in the office has added to over the "
            "years. It opens with a large title across the top, a merged heading that says “First Quarter,” "
            "and the barangays listed in groups, each followed by a bold subtotal row. Paid accounts are "
            "shaded green. A blank row separates each group so the sheet is easier on the eyes.",
            "One afternoon the head of office asks a simple question: which ten accounts paid the most this "
            "quarter? The analyst tries to sort the amounts. The spreadsheet refuses because of the merged "
            "cells. After unmerging them, the sort runs, but now the subtotal rows are mixed in with the "
            "accounts, and the biggest “account” on the list is a barangay subtotal. And no simple formula counts the green rows.",
            "The sheet was built to be looked at. It was not built to be worked with.",
            "(As always in this series, the office, the people and every number below are made up. No real "
            "town, barangay or taxpayer is described.)",
            "Part 10 covered data types and the difference between wide and long tables. This part is about "
            "the layout of the sheet itself. When you finish reading, you will know seven rules that make a "
            "spreadsheet easy to sort, filter and total, how to fix a messy tracker without losing data, and "
            "how to keep it clean once it is fixed.",
            ("photo", "blog/data-one-row.jpg", "A sheet you can work with: one row per record, one header row, facts in cells and the same codes every time. "
             "(Illustration: Butch "
             "Mahinay, aumahinay.dev)", "medium"),
            ("h", "What “One Row per Record” Means"),
            "A record is one thing you want to count: one receipt, one payment, one taxpayer, one permit. In a "
            "working sheet, each record gets exactly one row, and each fact about it gets its own column. A "
            "row for receipt 004512 holds its date, account, barangay, amount and collector, and nothing else "
            "sits in that row.",
            "Decide first what one row stands for, and write it down. “One row per official receipt” and “one "
            "row per taxpayer” are both fine, but a sheet that mixes the two can count some things twice.",
            ("quote", "Decide what one row stands for before you type the first row."),
            ("h", "Seven Rules for a Sheet You Can Work With"),
            ("point", "1. One header row", "Put the column names in the first row, one name per column, with "
             "no title above them. Move the title to the file name or to a separate notes sheet. Filters, sorting and pivot tables use the top row of the data as the column names."),
            ("point", "2. No merged cells", "Merged cells look tidy but get in the way of sorting, filtering "
             "and copying. Microsoft’s support page notes that Excel will not sort a range where only some of "
             "the cells are merged. If a heading needs to span columns, keep it in the printed report, not in "
             "the data."),
            ("point", "3. No blank rows or columns", "A blank row may be read as the end of the table, so a "
             "filter or a selection can stop halfway through the data. Use formatting or a separate report "
             "if you need space for the eyes."),
            ("point", "4. No totals inside the data", "Subtotal rows look like records to a formula or a "
             "sort. Keep the raw rows clean, and calculate totals in a separate summary or pivot table."),
            ("point", "5. One table per sheet", "Two tables side by side on one sheet are easy to break when "
             "one of them grows. Give each table its own sheet, with a clear sheet name."),
            ("point", "6. Facts in cells, not in colors", "Green shading for “paid” cannot be counted or "
             "filtered as easily as a column called Status with the word Paid in it. Color can still be "
             "used, but only to highlight a fact that is already written in a cell."),
            ("point", "7. The same code every time", "“Brgy. 1,” “Barangay 1” and “Poblacion 1” for the same "
             "place become three different places in a count. Choose one code per item and keep a list of "
             "the allowed codes."),
            ("h", "Dropdown Lists: Stopping Errors at the Door"),
            "Rule 7 is easier to keep when the spreadsheet does the checking. Both Google Sheets and Excel can "
            "limit a cell to a list of allowed values, shown as a dropdown.",
            ("point", "In Google Sheets", "Select the cells, then go to Data, Data validation, Add rule, and "
             "choose “Dropdown” or “Dropdown (from a range).” Google’s help page explains that entries not on "
             "the list are rejected unless you change the rule to show a warning instead."),
            ("point", "In Excel", "Select the cells, then go to Data, Data Validation, and under Allow choose "
             "List. Point the source to a range that holds the allowed values."),
            ("point", "Keep the list on its own sheet", "Put the allowed barangays, revenue sources and "
             "collectors on a sheet called Lists. When a new item is approved, add it there once. Then check that each dropdown’s source range includes the new row."),
            "A dropdown does not make a value correct. It only makes sure the value is one of the allowed "
            "choices. Someone can still pick the wrong barangay, so the checks in the next section still "
            "matter.",
            ("h", "Fixing the Collections Tracker, Step by Step"),
            "Never fix the only copy. Save a copy of the original file first, with the date in its name, and "
            "work on the copy.",
            ("point", "1. Write down what a row is", "Here, one row per official receipt."),
            ("point", "2. Move the title", "Delete the title rows above the headers and put the title in the "
             "file name."),
            ("point", "3. Unmerge and fill", "Unmerge every merged cell. Where a merged cell held a barangay "
             "name for a group of rows, type that name into every row of the group, so each row carries its "
             "own barangay."),
            ("point", "4. Remove blanks and subtotals", "Delete the blank rows and the subtotal rows. Before "
             "deleting the subtotals, write their values down; you will use them in step 7."),
            ("point", "5. Turn colors into a column", "Add a Status column and type Paid or Unpaid for each "
             "row, matching the old shading. Then clear the shading."),
            ("point", "6. Standardize the codes", "Sort by barangay, read down the list and correct the "
             "variations to one code each. Add dropdowns so the codes stay fixed."),
            ("point", "7. Check the totals", "Build a pivot table of amounts by barangay and compare it with "
             "the subtotals you wrote down in step 4. They must match. If one does not, find out why before "
             "you go on."),
            "Step 7 is the most important one. A cleanup that changes the totals has damaged the data, even "
            "if the sheet looks better.",
            ("h", "Keeping It Clean"),
            ("point", "A notes sheet", "Add a sheet called Notes that says what one row stands for, what each "
             "column means, where the data comes from and who maintains it."),
            ("point", "Raw data and reports apart", "Keep the working data on one sheet and build reports, "
             "charts and summaries on others. People can format the report sheet however they like without "
             "touching the data."),
            ("point", "Freeze the header", "Freeze the first row so the column names stay in view while "
             "scrolling. In Google Sheets it is under View, Freeze; in Excel, under View, Freeze Panes."),
            ("point", "A unique ID column", "Give each record a value that never repeats, such as the receipt "
             "number with its series. It makes duplicates easy to find."),
            ("h", "Mistakes to Avoid"),
            ("point", "Fixing the only copy", "Always work on a dated copy."),
            ("point", "Typing totals by hand", "A total typed into a cell does not update when a row changes. "
             "Let a formula or pivot table calculate it."),
            ("point", "Notes in the amount column", "Text such as “paid half, balance next week” turns an "
             "amount into text. Put remarks in a separate Remarks column."),
            ("point", "Hiding rows instead of deleting them", "Hidden rows still count in some formulas, so a "
             "total can include rows nobody can see."),
            ("h", "Key Takeaways"),
            ("point", "One row, one record", "Decide what a row stands for and keep to it."),
            ("point", "Clean layout", "One header row, no merged cells, no blank rows and no totals inside "
             "the data."),
            ("point", "Facts in cells", "Write the status in a column, and use dropdowns to keep codes the "
             "same."),
            ("point", "Prove the cleanup", "Totals before and after must match."),
            ("h", "Your Part 12 Exercise"),
            "Open one spreadsheet your office uses every month, and work on a copy.",
            ("point", "Name the record", "Write one sentence: “One row in this sheet is one…”"),
            ("point", "Check the seven rules", "Count how many of the seven rules the sheet breaks."),
            ("point", "Fix one rule", "Pick the easiest one, fix it on the copy, and check that the totals "
             "still match."),
            "If you cannot finish the sentence “One row in this sheet is one…”, that is the first thing to "
            "fix.",
            ("cta", "Read: Data Analytics Series, Part 10", "/blog/data-analytics-part-10-data-types-and-table-shapes/"),
            ("cta", "Read: Data Analytics Series, Part 11", "/blog/data-analytics-part-11-roccc-test/"),
            ("cta", "Read: Data Analytics Series, Part 5", "/blog/data-analytics-part-5-zero-budget-toolkit/"),
            ("cta", "Read: Business Intelligence Series, Part 9", "/blog/business-intelligence-part-9-testing-the-pipeline/"),
            ("ask", "Which spreadsheet in your office would you clean up first, and which rule does it break most?"),
        ],
    },
    {
        "date": "January 1, 2027",
        "title": "Data Analytics Series, Part 11: Good Data or Bad Data? The ROCCC Test",
        "slug": "data-analytics-part-11-roccc-test",
        "category": "data",
        "summary": "Before you trust a data set, test it. This part explains the five ROCCC checks, reliable, "
                   "original, comprehensive, current and cited, scores two treasury data sets with them, and "
                   "shows what to do when a source fails.",
        "publish_on": "2027-01-01 21:00",
        "body": [
            "The revenue unit is preparing next year’s collection target for business tax. Two files are on "
            "the table. One is the office’s own record of business taxes paid over the last three years, "
            "taken from the official receipts. The other is a summary someone received in a seminar handout, "
            "showing “average business tax growth for towns like ours.” It has no date and no author.",
            "The handout’s number is higher, and it would make a more impressive target. Before anyone uses "
            "it, the analyst asks a simple question: how do we know this data is good enough to plan with?",
            "(Like every case in this series, this one is invented, from the office down to the last peso. No real "
            "town, business or taxpayer is described.)",
            "Part 9 explained where data comes from, and Part 10 explained what shape it is in. This part gives "
            "a quick test of whether a source can be trusted. After this post, you will know the five "
            "ROCCC checks, how to score a data set with them, and what to do when a source fails one.",
            ("photo", "blog/data-roccc.jpg", "The ROCCC test: reliable, original, comprehensive, current and "
             "cited. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Five Questions in One Word"),
            "ROCCC is a short checklist taught in the Google Data Analytics course for judging whether data "
            "is credible. Each letter is one question.",
            ("point", "R: Reliable", "Is the source trustworthy, and was the data collected in a consistent "
             "way? Official receipts issued under the office’s rules are reliable. Numbers copied by hand from "
             "memory are not."),
            ("point", "O: Original", "Can you trace the data back to where it was first recorded? A copy of a "
             "copy can carry errors you cannot see. Go back to the first source when you can."),
            ("point", "C: Comprehensive", "Does it contain everything needed to answer your question? A list "
             "of business tax payments that leaves out the first quarter cannot tell you the year’s total."),
            ("point", "C: Current", "Is it recent enough for the decision? Last year’s tax rates are not "
             "current if an ordinance changed them in January."),
            ("point", "C: Cited", "Is it documented, with a named source, a date and a description of how it "
             "was made? Data with no citation is hard to check."),
            ("quote", "Good data is not data you like. It is data you can trace, check and explain."),
            ("h", "Scoring the Two Files"),
            "Score each check as pass, partial or fail, and write one line explaining why.",
            ("point", "Office receipts, three years", "Reliable: pass, issued under the office’s rules. "
             "Original: pass, taken directly from the receipts. Comprehensive: partial, two months of one year "
             "were encoded late and must be checked. Current: pass, includes this year. Cited: pass, with a "
             "source note from Part 9."),
            ("point", "Seminar handout", "Reliable: unknown, the method is not given. Original: fail, it is a "
             "summary of data from elsewhere. Comprehensive: unknown, it does not say which towns were "
             "included. Current: unknown, no date. Cited: fail, no author or source."),
            "The office’s own data has one partial that can be fixed. The handout has two fails and three "
            "unknowns. It might be useful as a question to explore, but not as a number to plan with.",
            ("h", "Unknown Is Not the Same as Pass"),
            "When you cannot answer a ROCCC question, mark it unknown, not pass. An unknown is a task: ask the "
            "person who gave you the data, look for the original, or find the date.",
            "In the opening story, a phone call to the seminar organizer might turn the handout’s unknowns into "
            "answers. Until then, the honest description is: “source not verified.”",
            ("h", "What to Do When a Source Fails"),
            ("point", "Fix it", "If the problem is in your own data, such as months encoded late, correct "
             "the records and note the fix in the source note."),
            ("point", "Replace it", "If a better source exists, use it. Instead of a growth figure from an "
             "unknown handout, compute your own office’s growth from the receipts."),
            ("point", "Use it with a warning", "If there is no better source, use the data but say plainly "
             "which checks it failed. For example: “This comparison uses a figure we could not verify.”"),
            ("point", "Set it aside", "If a source fails on reliability and originality and cannot be "
             "traced, leave it out of decisions."),
            ("h", "ROCCC for the Treasury’s Common Sources"),
            ("point", "Official receipts and collection reports", "They are the first record, so they can "
             "score well on reliability and originality. Check comprehensiveness for late-encoded or "
             "missing days."),
            ("point", "Data shared by another office", "Ask for the date and how it was collected. Check "
             "currency: an assessment roll from last year may not include this year’s new declarations."),
            ("point", "Published statistics", "Check the citation: which agency, which year, and which "
             "table. Use the agency’s own publication rather than a news story or a slide that quotes it."),
            ("point", "Online lists and directories", "They can score poorly on original and cited. Treat them "
             "as leads, as in Part 9."),
            ("h", "Checking “Comprehensive” in Practice"),
            "Of the five checks, comprehensive is one your own data can fail without anyone noticing. Three "
            "quick tests help.",
            ("point", "Count the days", "For each month, count the days that have at least one receipt and "
             "compare with the working days. A working day with no receipts may mean a closed office or a missing file, so check it."),
            ("point", "Compare with signed reports", "Add up each month in your data and compare it with the "
             "monthly collections report that was signed. A difference points to missing or extra records."),
            ("point", "Check every category", "Make sure each revenue account, collector and barangay you "
             "expect appears at least once. One that is missing entirely may have been left out of the "
             "extract."),
            ("h", "A ROCCC Note, Written Out"),
            ("point", "Data set", "Business tax receipts, January 2024 to November 2026."),
            ("point", "Reliable: pass", "Official receipts issued under the office’s rules."),
            ("point", "Original: pass", "Extracted directly from the collection system."),
            ("point", "Comprehensive: partial", "March and April 2025 were encoded late; totals are being "
             "checked against the signed monthly reports."),
            ("point", "Current: pass", "Includes receipts up to November 30, 2026."),
            ("point", "Cited: pass", "Source note kept with the file, owner: the revenue unit."),
            ("h", "Making ROCCC a Habit"),
            "Add a short ROCCC section to every source note: five lines, one per letter, each with pass, "
            "partial, fail or unknown and a reason. It takes a few minutes and saves a reader from guessing "
            "later.",
            "When you present results, mention the weakest check. “This analysis uses our own receipts, "
            "complete except for March and April 2025, which are being checked” tells the reader exactly how far to "
            "trust it.",
            ("h", "Mistakes to Avoid"),
            ("point", "Trusting a number because it is convenient", "The handout’s growth figure was attractive "
             "because it was high. That is a reason to check it more, not less."),
            ("point", "Assuming official means current", "An official list can still be out of date."),
            ("point", "Skipping your own data", "Your office’s records can fail a check too, such as "
             "comprehensive when days are missing."),
            ("h", "Key Takeaways"),
            ("point", "Five checks", "Reliable, original, comprehensive, current and cited."),
            ("point", "Score honestly", "Pass, partial, fail or unknown, each with a reason."),
            ("point", "Unknown is a task", "Find the answer before treating it as a pass."),
            ("point", "Say the weakest check", "Tell readers how far to trust the result."),
            ("h", "Your Part 11 Exercise"),
            "Pick one number your office used in a plan or report this year that came from outside your own "
            "records.",
            ("point", "Score it", "Run the five ROCCC checks and write a reason for each."),
            ("point", "Find the original", "Try to trace it to the first place it was published or recorded."),
            ("point", "Decide", "Fix, replace, use with a warning, or set aside."),
            "If you cannot trace it at all, ask yourself whether the plan still holds without it.",
            ("cta", "Read: Data Analytics Series, Part 9", "/blog/data-analytics-part-9-where-data-comes-from/"),
            ("cta", "Read: Data Analytics Series, Part 10", "/blog/data-analytics-part-10-data-types-and-table-shapes/"),
            ("cta", "Read: Data Analytics Series, Part 8", "/blog/data-analytics-part-8-metrics-and-kpis/"),
            ("cta", "Read: Business Intelligence Series, Part 10", "/blog/business-intelligence-part-10-keeping-bi-honest/"),
            ("ask", "Which number has your office used that would fail the ROCCC test today?"),
        ],
    },
    {
        "date": "December 27, 2026",
        "title": "Data Analytics Series, Part 10: Data Types, Structured Data and Wide vs Long Tables",
        "slug": "data-analytics-part-10-data-types-and-table-shapes",
        "category": "data",
        "summary": "Before you can analyze data, you need to know what kind of data it is and what shape it "
                   "is in. This part explains data types, structured and unstructured data, and wide and "
                   "long tables, with treasury examples and the mistakes each one prevents.",
        "publish_on": "2026-12-27 21:00",
        "body": [
            "An analyst opens a spreadsheet of business permits and asks for the total gross sales declared. "
            "The answer comes back far too low. A quick look shows why: about a third of the amounts were typed "
            "with letters in front, like “PHP 1,250,000,” and the spreadsheet treated them as text. The "
            "SUM formula skipped every one of them without a warning.",
            "In another column, the barangay codes “007” and “012” have become 7 and 12. The lookup that "
            "matches codes to barangay names now fails for every barangay with a leading zero.",
            "(As always in this series, the office, the people and every number below are made up. No real "
            "town, business or taxpayer is described.)",
            "Part 9 asked where data comes from. This part asks what kind of data it is and what shape it is "
            "in. Read to the end and you will know the basic data types, the difference between structured "
            "and unstructured data, how wide and long tables differ, and when to use each shape.",
            ("photo", "blog/data-wide-long.jpg", "The same collections in two shapes: a wide table with one "
             "column per month, and a long table with one row per collector per month. (Illustration: Butch "
             "Mahinay, aumahinay.dev)", "medium"),
            ("h", "Data Types: What Kind of Value Is This?"),
            "Every value in a column has a type. The type decides what you can do with it.",
            ("point", "Number", "A value you can add, average or compare: amounts, counts, areas. Store "
             "amounts as plain numbers, and let the cell format show the peso sign and commas."),
            ("point", "Text", "Letters, or digits that are not meant for arithmetic: names, addresses, "
             "receipt numbers and codes. A barangay code is text, even if it looks like a number, because "
             "nobody adds codes together and the leading zeros matter."),
            ("point", "Date", "A day on the calendar. Stored as a real date, it can be sorted, filtered by "
             "month and used to count days late."),
            ("point", "True or false", "A value with only two possible answers, such as whether a receipt was "
             "cancelled. Analysts also call this a Boolean."),
            ("quote", "Ask what you will do with a column before you decide its type."),
            ("h", "How to Spot a Wrong Type in a Spreadsheet"),
            ("point", "Look at the alignment", "In Google Sheets and Excel, numbers line up on the right of a "
             "cell by default and text on the left. An amount sitting on the left may be stored as text."),
            ("point", "Count before you sum", "Use COUNT, which counts only numbers, beside COUNTA, which "
             "counts every filled cell. If the two differ in an amount column, some amounts are text."),
            ("point", "Check the codes", "If codes lost their leading zeros, set the column format to plain "
             "text and type or import them again."),
            ("point", "Check the dates", "A date typed as “12/01/2026” can be read as December 1 or January "
             "12, depending on the spreadsheet’s regional setting. Write dates as year-month-day, such as "
             "2026-12-01, or check the setting first."),
            ("h", "Structured and Unstructured Data"),
            "The second question is how the data is organized.",
            ("point", "Structured data", "Data in rows and columns, where every row follows the same layout: a "
             "receipts table, a list of permits, an assessment roll. Spreadsheets and databases are built for "
             "it."),
            ("point", "Unstructured data", "Data without a fixed layout: scanned letters, photos of business "
             "signs, recorded taxpayer complaints, free-written remarks. It holds real information, but it "
             "must be read or sorted before it can be counted."),
            "Some data falls in between. A permit form has fixed fields, such as name and address, and a "
            "remarks field where anything can be written. Treat the fixed fields as structured and the remarks "
            "as unstructured.",
            "A practical rule: if you will need to count or total something, give it its own column with a "
            "type. If a reason for cancellation is written only in remarks, nobody can count cancellations by "
            "reason without reading every line.",
            ("h", "Wide and Long Tables"),
            "Structured data can still come in different shapes. Take the same numbers, collections by "
            "collector for three months, arranged two ways.",
            ("point", "Wide table", "One row per collector, one column per month: Collector, January, February, "
             "March. Three rows of four columns."),
            ("point", "Long table", "One row per collector per month: Collector, Month, Amount. Nine rows of "
             "three columns."),
            "Both hold exactly the same information. They differ in what is easy to do with them.",
            ("point", "Wide is easier to read", "A person can scan across a row and compare months at a glance. "
             "It suits a printed report or a summary for the head of office."),
            ("point", "Long is easier to analyze", "Adding April means adding rows, not a new column, so "
             "formulas and charts keep working. Filters and pivot tables work best with one row per "
             "record."),
            ("h", "When to Use Each Shape"),
            ("point", "Store and analyze in long", "Keep the working data in long form: one row per "
             "receipt, per collector per day, or per collector per month."),
            ("point", "Present in wide", "Turn it into wide form at the end, for the report people will read. "
             "A pivot table does this in a few clicks: put collectors in rows, months in columns and amounts "
             "in values."),
            ("point", "Watch for wide tables that grow", "A sheet that gains a new column every month is a "
             "sign the data should be stored long."),
            ("h", "Turning a Wide Table Into a Long One"),
            "If you receive a wide table, you can reshape it by hand in a few minutes for a small sheet.",
            ("point", "1. Set up the columns", "On a new sheet, type three headers: Collector, Month and Amount."),
            ("point", "2. Copy the first month", "Paste the list of collectors under Collector, their January "
             "amounts under Amount, and type “January” in the Month column beside each one."),
            ("point", "3. Repeat below", "Paste the same collectors again under the January rows, with "
             "February’s amounts and “February” as the month. Do the same for each remaining month."),
            ("point", "4. Check the total", "The sum of the Amount column must equal the sum of all the month "
             "columns in the wide table. If it does not, a row was missed or pasted twice."),
            "For larger tables, Excel’s Power Query has an Unpivot Columns command that does the same "
            "reshaping in one step. Whichever way you use, run the total check at the end.",
            ("h", "A Quick Check Before Any Analysis"),
            "Before you write a single formula, look at each column and answer three questions.",
            ("point", "What type is it?", "Number, text, date or true/false."),
            ("point", "Is it stored as that type?", "Use the alignment and COUNT checks."),
            ("point", "Is the table long or wide?", "If you need to filter or pivot it, make it long first."),
            "Write the answers in the source note from Part 9, so the next person knows the shape before they "
            "start.",
            ("h", "Mistakes to Avoid"),
            ("point", "Typing letters into amounts", "Words like “PHP” turn a number into text. Let the cell "
             "format show the currency."),
            ("point", "Storing codes as numbers", "Leading zeros disappear, and matches fail."),
            ("point", "Hiding countable facts in remarks", "Give anything you will count its own column."),
            ("point", "Analyzing a wide table directly", "Reshape it to long first, or each new month can break your formulas."),
            ("h", "Key Takeaways"),
            ("point", "Type follows use", "Numbers are for arithmetic; codes and IDs are text."),
            ("point", "Check before you sum", "Alignment and COUNT reveal values stored as the wrong type."),
            ("point", "Structure what you will count", "Give countable facts their own typed column."),
            ("point", "Long to analyze, wide to present", "Keep working data long and build wide views for "
             "readers."),
            ("h", "Your Part 10 Exercise"),
            "Open one spreadsheet your office updates every month.",
            ("point", "Types", "For each column, write the type it should be and check that it is stored that "
             "way."),
            ("point", "Shape", "Decide whether the table is wide or long. If a new column appears every month, "
             "sketch the long version."),
            ("point", "Fix one thing", "Correct one column stored as the wrong type, and note the fix."),
            "Then rerun one total you report regularly. If it changes, you have found a number that was wrong "
            "before today.",
            ("cta", "Read: Data Analytics Series, Part 9", "/blog/data-analytics-part-9-where-data-comes-from/"),
            ("cta", "Read: Data Analytics Series, Part 5", "/blog/data-analytics-part-5-zero-budget-toolkit/"),
            ("cta", "Read: Business Intelligence Series, Part 5", "/blog/business-intelligence-part-5-data-modeling/"),
            ("cta", "Read: Business Intelligence Series, Part 9", "/blog/business-intelligence-part-9-testing-the-pipeline/"),
            ("ask", "Which column in your office’s spreadsheets is most often stored as the wrong type?"),
        ],
    },
    {
        "date": "December 22, 2026",
        "title": "Data Analytics Series, Part 9: Where Data Comes From, First-, Second- and Third-Party",
        "slug": "data-analytics-part-9-where-data-comes-from",
        "category": "data",
        "summary": "Every data set has a history: who collected it, how, when and why. This part explains "
                   "first-, second- and third-party data with treasury examples, gives six questions to ask "
                   "any source, and shows how to record a source so the next analyst can trust it.",
        "publish_on": "2026-12-22 21:00",
        "body": [
            "The revenue unit wants a list of businesses that may be operating without a permit. The analyst "
            "gathers three files: the office’s own list of permits issued this year, a list of barangay "
            "clearances shared by the barangays, and a business directory downloaded from a website. Any "
            "business in the second or third file but missing from the first goes on the list.",
            "The list has 140 names. In the first week of visits, the team finds that 30 of them closed years "
            "ago, 12 are the same business spelled two ways, and several are branches of businesses that "
            "already hold a permit under the main office’s name. The analysis was done correctly. The trouble "
            "was that the three files were treated as equally reliable, when each had a very different "
            "history.",
            "(Like every case in this series, this one is invented, from the office down to the last peso. No real "
            "town, business or taxpayer is described.)",
            "This part begins the Prepare step from Part 2. By the last section, you will know the three "
            "kinds of data by who collected them, six questions to ask any source, how to combine sources "
            "without creating false matches, and how to write a source note that keeps the history with the "
            "data.",
            ("photo", "blog/data-three-sources.jpg", "Three kinds of data by who collected it: first-party "
             "from your own office, second-party shared by the one who collected it, and third-party "
             "gathered by someone else from other sources. (Illustration: Butch Mahinay, aumahinay.dev)",
             "medium"),
            ("h", "Three Kinds of Data, by Who Collected It"),
            "One useful way to sort data is by who collected it and how it reached you.",
            ("point", "First-party data", "Data your own office collected from the people it serves, through "
             "its own work. Official receipts, the permits you issued and the taxpayer records you keep are all "
             "first-party data for the treasury."),
            ("point", "Second-party data", "Data another organization collected directly from its own people, "
             "then shared with you. The barangay clearance list in the opening story is an example: the "
             "barangays collected it from businesses and passed it on."),
            ("point", "Third-party data", "Data compiled by someone who did not collect it at the source, "
             "such as a list put together from many other lists. The downloaded business directory is an "
             "example: whoever built it compiled listings from many places, at different times."),
            "The further data travels from the people who collected it, the more questions you need to ask "
            "before relying on it. That is not because second- and third-party data are bad. It is because "
            "you know less about how they were made.",
            ("quote", "Data does not arrive from nowhere. Every file has a history, and the history decides "
             "how far you can trust it."),
            ("h", "Where the Lines Blur"),
            "Inside a local government, the labels can depend on where you stand. The assessor’s office "
            "collects property information directly from owners and keeps the assessment roll. From the "
            "whole local government’s point of view, that is its own data. From the treasury’s desk, it is "
            "data another office collected and shared.",
            "Do not spend long arguing over the label. The label is only a reminder to ask the real question: "
            "who collected this, how, and how much do I know about the way it was made?",
            ("h", "Six Questions to Ask Any Source"),
            ("point", "1. Who collected it?", "An office, a barangay, a private website, a person? Write the "
             "name of the unit and a contact, not just “from the province.”"),
            ("point", "2. How was it collected?", "A form filled in by the taxpayer, encoding by staff, an "
             "inspection, a copy of another list? Each method can introduce different kinds of errors."),
            ("point", "3. When, and how often is it updated?", "A list from January says nothing about "
             "businesses that closed in June. Note the date of the data, not just the date you received it."),
            ("point", "4. Why was it collected?", "Data collected for one purpose may not fit another. A "
             "clearance list shows who asked for a clearance, which is not the same as who is operating "
             "today."),
            ("point", "5. What does each field mean?", "Does “address” mean the business location or the "
             "owner’s home? Does “date” mean the date of application or of approval? Ask before you compare."),
            ("point", "6. May we use it this way?", "Check that sharing and using the data for this purpose is "
             "allowed, especially when it holds personal information. Part 6 covers the Data Privacy Act "
             "principles that apply."),
            "If you cannot answer a question, write that down too. “Collection method unknown” is useful "
            "information for whoever reads the results.",
            ("h", "The Opening Story, Source by Source"),
            ("point", "Permits issued (first-party)", "Collected by the office, at the counter, for this year. "
             "Reliable for who holds a permit, recorded under the name on the application."),
            ("point", "Barangay clearances (second-party)", "Collected by each barangay when a business asked "
             "for a clearance. Shows who applied, not who is still open, and spellings follow each barangay’s "
             "own encoding."),
            ("point", "Business directory (third-party)", "Compiled by an outside website from sources it does "
             "not name, updated at unknown times. Useful for leads, not for conclusions."),
            "Seen this way, the right result was not one list of 140 names. It was a short list of businesses "
            "found in both the barangay list and the directory but not in the permits, to check first, and a "
            "longer list of directory-only names to treat as leads.",
            ("h", "Combining Sources Without False Matches"),
            "Two of the three problems in the opening story came from matching names. Names can change, be "
            "abbreviated or be spelled differently by different people.",
            ("point", "Use a shared code when one exists", "A permit number, a tax declaration number or a "
             "barangay clearance number matches more safely than a business name."),
            ("point", "Clean names the same way on both sides", "When names are all you have, make both lists "
             "uppercase, remove extra spaces and write common words the same way, such as “Sto.” and “Store,” before comparing. Then review close matches by hand."),
            ("point", "Keep the source on every row", "Add a column that says which file each row came from. "
             "When a result looks odd, you can trace it back quickly."),
            ("h", "Write a Source Note"),
            "Keep a short note beside every data set you receive. It keeps the history with the data, so the "
            "next analyst does not have to rediscover it.",
            ("point", "What to write", "Name of the data set, who collected it, the contact person, how it was "
             "collected, the period it covers, the date received, what each unclear field means, and what "
             "it may be used for."),
            ("point", "Where to keep it", "In the same folder as the file, with a matching name, or on the "
             "first sheet of the workbook."),
            ("h", "Mistakes to Avoid"),
            ("point", "Treating every file as equally reliable", "Give more weight to sources you know more "
             "about, and say so in the results."),
            ("point", "Forgetting the date of the data", "The date you downloaded a file is not the date its "
             "information was true."),
            ("point", "Reporting leads as findings", "A name in a third-party directory is a reason to check, "
             "not proof that a business is operating."),
            ("h", "Key Takeaways"),
            ("point", "Three kinds by who collected it", "First-party is your own, second-party is shared by "
             "the collector, and third-party is compiled by someone else."),
            ("point", "Ask six questions", "Who, how, when, why, what each field means, and whether you may "
             "use it."),
            ("point", "Match on codes, not names", "And keep the source of every row."),
            ("point", "Keep a source note", "The history of the data belongs beside the data."),
            ("h", "Your Part 9 Exercise"),
            "Pick one data set your office received from outside your own unit. Answer the six questions for "
            "it, and write the answers as a source note.",
            "Then mark each answer as known or unknown. If more than two are unknown, ask the person who sent "
            "it before you use the data in a report.",
            ("cta", "Read: Data Analytics Series, Part 2", "/blog/data-analytics-part-2-six-steps/"),
            ("cta", "Read: Data Analytics Series, Part 6", "/blog/data-analytics-part-6-data-ethics-privacy/"),
            ("cta", "Read: Data Analytics Series, Part 8", "/blog/data-analytics-part-8-metrics-and-kpis/"),
            ("cta", "Read: Business Intelligence Series, Part 6", "/blog/business-intelligence-part-6-warehouses-marts-lakes/"),
            ("ask", "Which data set in your office has the least-known history?"),
        ],
    },
    {
        "date": "December 17, 2026",
        "title": "Data Analytics Series, Part 8: Metrics and KPIs That Tell the Truth",
        "slug": "data-analytics-part-8-metrics-and-kpis",
        "category": "data",
        "summary": "Two offices can both report 90% collection efficiency and mean completely different things. "
                   "This part explains the difference between a metric and a KPI, shows how one definition "
                   "can flatter or expose performance, and gives a template for measures that tell the truth.",
        "publish_on": "2026-12-17 21:00",
        "body": [
            "At a provincial meeting, two treasurers compare notes. Both report a real property tax "
            "collection efficiency of 90%. One is quietly proud. The other is worried. They are both right, "
            "because they are not measuring the same thing.",
            "The first divided this year’s collections by this year’s collection target. The second divided "
            "this year’s collections by everything that was actually due, including unpaid taxes from past "
            "years. Same name, same percentage, very different stories about how each office is doing.",
            "(As always in this series, the office, the people and every number below are made up. No real "
            "town or taxpayer is described.)",
            "Part 7 showed how to name the type of problem behind a request. This part is about the numbers "
            "that answer it. Stay with me to the end, and you will know the difference between a metric and a "
            "KPI, the questions that expose a misleading measure, and a template for writing measures that "
            "tell the same truth to everyone who reads them.",
            ("photo", "blog/data-kpi-parts.jpg", "A measure that tells the truth has five parts written down: "
             "its name, numerator, denominator, period and source. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "Metric or KPI?"),
            ("point", "Metric", "Any number that measures something: collections today, receipts issued, "
             "taxpayers served, average waiting time. An office can track as many as it finds useful."),
            ("point", "KPI", "A key performance indicator is a metric chosen because it shows progress toward "
             "a goal that matters. Keep the list short, and tie each one to an objective, like the "
             "objectives from the Project Management series."),
            "Every KPI is a metric, but not every metric is a KPI. The test is simple: if this number moved, "
            "would someone change what they do? If not, it is a metric worth keeping, but not a key one.",
            ("h", "One Name, Two Definitions"),
            "Here are the two treasurers’ numbers, worked out.",
            ("point", "Office A: collections against target", "Target for current-year real property tax: "
             "₱10,000,000. Collected: ₱9,000,000. Efficiency: 9,000,000 ÷ 10,000,000 = 90%."),
            ("point", "Office B: collections against amount due", "Current-year tax due: ₱8,000,000. Unpaid "
             "taxes from past years still due: ₱2,000,000. Total due: ₱10,000,000. Collected against all of "
             "it: ₱9,000,000. Efficiency: 90%."),
            "Now look underneath. If Office A’s target was set low, its 90% may hide a large unpaid balance. "
            "Office B’s 90% already counts the old debts, so it says more about how much of what taxpayers "
            "owe is actually coming in.",
            "Neither definition is wrong. Each answers a different question. The danger is reporting either "
            "one under the same name without saying which it is.",
            ("quote", "A percentage without its definition is not a fact. It is half of one."),
            ("h", "Five Parts Every Measure Needs"),
            "Write each KPI down with these five parts, and put the same text wherever the number appears.",
            ("point", "1. Name", "A plain name that says what it is, such as “Current-year RPT collected "
             "against amount due.”"),
            ("point", "2. Numerator", "What is counted on top. For example: current-year real property tax "
             "collected, by official receipt date, excluding cancelled receipts."),
            ("point", "3. Denominator", "What it is divided by. For example: current-year real property tax "
             "due, from the assessment roll as of January 1."),
            ("point", "4. Period", "The time it covers: January to the end of the reporting month."),
            ("point", "5. Source", "Where each part comes from: the collection system for the numerator, the "
             "assessment roll for the denominator."),
            "With these five parts written, two offices, or two people in the same office, can compare their "
            "numbers honestly.",
            ("h", "The Two Treasurers, Rewritten"),
            "Apply the five parts to the opening example, and the confusion disappears before anyone "
            "compares a single percentage.",
            ("point", "Office A", "Name: current-year RPT collected against collection target. Numerator: "
             "current-year tax collected, January to November. Denominator: the target set at the start of the "
             "year. Source: the collection system and the approved target."),
            ("point", "Office B", "Name: RPT collected against total amount due. Numerator: current-year and "
             "past-year tax collected, January to November. Denominator: current-year tax due plus unpaid taxes "
             "from past years. Source: the collection system and the assessment roll."),
            "Side by side, the two names already say that the measures cannot be compared directly. The "
            "provincial meeting could still discuss both, but no one would mistake one office’s 90% for the "
            "other’s.",
            ("h", "Questions That Expose a Misleading Measure"),
            ("point", "Who set the denominator?", "A target is a choice. An amount due is a record. Measures "
             "built on targets can look better simply because the target was modest."),
            ("point", "What is left out?", "Excluding past-year balances, or certain accounts, changes the "
             "story. Say what is excluded."),
            ("point", "Can it improve without real improvement?", "If a number can rise because records "
             "changed rather than because work improved, pair it with a second measure that would catch "
             "that."),
            ("point", "Is the period fair?", "Comparing January to March with a full year, or a month with a "
             "holiday break with one without, can mislead."),
            ("h", "Pairing Measures"),
            "A single number can rise for the wrong reasons. Two measures that pull in different directions "
            "check each other, so a gain in one that hides a loss in the other is easier to spot.",
            ("point", "Collections with arrears", "Collections against amount due, paired with the total of "
             "unpaid balances older than one year. One rises when work improves; the other should fall."),
            ("point", "Speed with accuracy", "Average waiting time at the window, paired with the number of "
             "receipts cancelled for errors. Faster service should not mean more mistakes."),
            "Part 3 of the Business Intelligence series made the same point for dashboards: watch amounts "
            "with arrears, and speed with shortages.",
            ("h", "Leading and Lagging KPIs"),
            "A lagging KPI reports a result after it has happened, such as collection efficiency for the year. "
            "A leading KPI moves earlier and gives time to act, such as the number of large accounts not yet "
            "reminded by the end of the first quarter.",
            "Keep at least one leading measure beside each lagging one. The lagging number tells you how you "
            "did. The leading one tells you whether you can still change it.",
            ("h", "Showing a KPI on a Report"),
            "A KPI on a page needs more than its value. Show four things together, so the reader does not "
            "have to guess.",
            ("point", "The full name", "Use the written name, not a short label like “efficiency.”"),
            ("point", "The period", "For example: January to November 2026."),
            ("point", "A comparison", "The same measure for the same period last year, computed with the same "
             "definition."),
            ("point", "The definition", "A one-line note under the number, or a link to the written five "
             "parts."),
            "A line such as “Current-year RPT collected against amount due, January to November 2026: 82% "
            "(same period in 2025: 78%)” can be read correctly by someone who was not in the room when the "
            "measure was designed.",
            ("h", "When a Definition Changes"),
            "Sometimes an office decides to change a measure, such as switching from a target to the amount "
            "due. The change may be right, but it breaks the comparison with past reports.",
            "When that happens, recompute the past periods with the new definition if the records allow it. "
            "If they do not, mark the break clearly on every report, with the date the new definition began, "
            "so no one reads a jump in the number as a jump in performance.",
            ("h", "Key Takeaways"),
            ("point", "Keep KPIs few", "A KPI is a metric tied to a goal that someone will act on."),
            ("point", "Write the definition", "Name, numerator, denominator, period and source, every time."),
            ("point", "Same name is not same measure", "Always say what a percentage is divided by."),
            ("point", "Pair and lead", "Pair measures that check each other, and keep a leading measure "
             "beside each lagging one."),
            ("h", "Your Part 8 Exercise"),
            "Pick one percentage your office reports regularly. Write its five parts: name, numerator, "
            "denominator, period and source.",
            "Then ask a colleague to compute it from the same records, using only what you wrote. If their "
            "answer differs from yours, the definition still has a gap. Fix the wording until two people "
            "get the same number.",
            ("cta", "Read: Data Analytics Series, Part 7", "/blog/data-analytics-part-7-six-problem-types/"),
            ("cta", "Read: Data Analytics Series, Part 4", "/blog/data-analytics-part-4-four-questions-worked/"),
            ("cta", "Read: Business Intelligence Series, Part 3", "/blog/business-intelligence-part-3-what-to-watch/"),
            ("cta", "Read: Project Management Series, Part 6", "/blog/project-management-part-6-writing-objectives/"),
            ("ask", "What does your office divide by when it reports collection efficiency?"),
        ],
    },
    {
        "date": "December 12, 2026",
        "title": "Data Analytics Series, Part 7: Six Kinds of Problems Data Can Solve",
        "slug": "data-analytics-part-7-six-problem-types",
        "category": "data",
        "summary": "A request for “a report” can hide one of several basic problem types. This part walks "
                   "through six of them with treasury examples, so you can name the problem first and pick "
                   "the right method before you open a spreadsheet.",
        "publish_on": "2026-12-12 21:00",
        "body": [
            "Three requests reach the analyst in one morning. The head of office asks, “Will we hit the "
            "target this year?” The cashier asks, “Why did yesterday’s deposit not match the collections?” "
            "The revenue unit asks, “Can you group the businesses so we know who to visit first?”",
            "All three are called “a report.” They are really three different kinds of problems, and each "
            "needs a different approach. An analyst who treats them all the same can end up building three "
            "tables and answering none of the questions.",
            "(Like every case in this series, this one is invented, from the office down to the last peso. No real town or "
            "taxpayer is described.)",
            "The Google Data Analytics Certificate groups the questions analysts meet into six common problem "
            "types. Naming the type is the first move of the Ask step from Part 2, because the type tells you "
            "what data you need and what method to use. By the end of this post, you will be able to recognize "
            "all six in your own office’s requests and know where to start with each.",
            ("photo", "blog/data-six-problems.jpg", "Six common problem types: making predictions, categorizing "
             "things, spotting something unusual, identifying themes, discovering connections and finding "
             "patterns. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "1. Making Predictions"),
            "The question is about the future: what is likely to happen? “Will we hit the collection target "
            "this year?” is a prediction problem.",
            ("point", "What you need", "Past data for the same measure over several periods, and a way to "
             "describe how the current period compares."),
            ("point", "Where to start", "Part 4 projected a year-end total from the share collected by "
             "October in past years. Simple methods like that are a good first step, as long as the answer is "
             "shown as a range."),
            ("h", "2. Categorizing Things"),
            "The question is about sorting items into groups by their features. “Group the businesses so we "
            "know who to visit first” is a categorizing problem.",
            ("point", "What you need", "A list of items, each with the features that matter: amount owed, "
             "months overdue, type of business, barangay."),
            ("point", "Where to start", "Agree on the groups and the rules first, for example: owes more than "
             "₱10,000 and overdue more than six months goes to the first visit list. Write the rule down so "
             "anyone can repeat it."),
            ("h", "3. Spotting Something Unusual"),
            "The question is about what does not fit the normal pattern. “Why did yesterday’s deposit not "
            "match the collections?” starts as this kind of problem: first find what is unusual, then explain "
            "it.",
            ("point", "What you need", "A clear idea of normal: the usual daily range, the usual difference "
             "between collections and deposits (ideally zero), the usual number of cancelled receipts."),
            ("point", "Where to start", "Compare each day with that normal and list the days, collectors or "
             "receipts that fall outside it. The list is not an accusation. It is where to look first."),
            ("h", "4. Identifying Themes"),
            "The question is about grouping categories into a few broader ideas. It fits comments and "
            "complaints well.",
            "Suppose the office has two hundred written comments from taxpayers at the counter. Reading them "
            "one by one gives impressions. Sorting them first into categories, such as long line, no seats, "
            "slow lookup of past payments, wrong amount and unclear wording, and then grouping those into "
            "themes, such as the waiting experience and the bill itself, turns them into evidence.",
            ("point", "How it differs from categorizing", "Categorizing places each item in a group. "
             "Identifying themes goes one level up and groups the categories into broader ideas."),
            ("h", "5. Discovering Connections"),
            "The question is about finding links between things that are usually looked at separately, often "
            "by combining data from different sources or offices.",
            "For example, the treasury has payment records and the assessor’s office has the property "
            "records. Joined by a common property number, they can show which properties have never had a "
            "recorded payment. Neither office can see that from its own records alone.",
            ("point", "What you need", "A shared key, such as a property number, and an agreement between "
             "the offices on how the combined data may be used."),
            ("h", "6. Finding Patterns"),
            "The question is about what repeats over time. “When during the year do business tax payments "
            "come in?” is a pattern problem.",
            "Under the Local Government Code, business taxes may be paid in quarterly installments within the "
            "first twenty days of January and of each following quarter. A chart of daily collections across "
            "several years will show whether payments in your office bunch up near those dates, which is useful for planning staff at the windows. Put two or three past years side by side, so a one-time spike is not mistaken for a pattern.",
            ("point", "How it differs from prediction", "Finding patterns describes what has repeated. "
             "Prediction uses that knowledge to estimate a specific future value."),
            ("quote", "Name the problem before you touch the data. The type of question decides the type of "
             "answer."),
            ("h", "When a Request Combines Types"),
            "The cashier’s deposit question starts as spotting something unusual, then becomes a "
            "connection problem when the analyst joins the receipts with the deposit slips to find which "
            "receipts were not deposited. The head of office’s target question needs patterns first, then a "
            "prediction.",
            "Naming the types in order gives you a plan: first this, then that. It also helps you explain to "
            "the person who asked why the answer will take two steps, not one.",
            ("h", "Turning a Vague Request Into a Typed Question"),
            "A request does not arrive with a type attached. Suppose the head of office says, “Give me some numbers on "
            "business permits.” Before opening any file, the analyst asks three follow-up questions.",
            ("point", "What decision is this for?", "“I want to know whether we need extra staff for the renewal "
             "period.” That points to timing."),
            ("point", "What would a useful answer look like?", "“Which weeks are busiest, and how busy.” That is a "
             "pattern problem: what repeats each year."),
            ("point", "Is anything else behind it?", "“Last January some renewals were very late.” That adds a second "
             "type: spotting something unusual, namely which businesses renewed late and whether they share "
             "features."),
            "The vague request has become two typed questions in a clear order: find the weekly pattern of "
            "renewals over past years, then list the late renewals and look at what they have in common. Each "
            "has its own data and its own method, and the head of office can see exactly what will be delivered.",
            "This short conversation also protects the analyst’s time. Without it, the result can be a long table of permit counts that answers nobody’s real question.",
            ("h", "A Quick Guide"),
            ("point", "“What will happen?”", "Making predictions."),
            ("point", "“Which group does each one belong to?”", "Categorizing things."),
            ("point", "“What doesn’t look right?”", "Spotting something unusual."),
            ("point", "“What are people telling us, overall?”", "Identifying themes."),
            ("point", "“How does this relate to that?”", "Discovering connections."),
            ("point", "“What keeps happening?”", "Finding patterns."),
            ("h", "Key Takeaways"),
            ("point", "Name the type first", "The problem type tells you what data and method you need."),
            ("point", "Categories versus themes", "Categories sort the items; themes group the categories "
             "into bigger ideas."),
            ("point", "Patterns versus predictions", "Patterns describe what repeats; predictions estimate "
             "what comes next."),
            ("point", "Some requests combine types", "Write the types in order and you have a plan."),
            ("h", "Your Part 7 Exercise"),
            "Collect the last five requests your office received for “a report” or “some numbers.” For each "
            "one, write:",
            ("point", "The question", "In one sentence, as the person asked it."),
            ("point", "The type or types", "Which of the six does it belong to, and in what order?"),
            ("point", "The data needed", "Which records would answer it, and does the office already keep "
             "them?"),
            "If a few types come up again and again, those are the ones worth building a routine for.",
            ("cta", "Read: Data Analytics Series, Part 6", "/blog/data-analytics-part-6-data-ethics-privacy/"),
            ("cta", "Read: Data Analytics Series, Part 4", "/blog/data-analytics-part-4-four-questions-worked/"),
            ("cta", "Read: Data Analytics Series, Part 2", "/blog/data-analytics-part-2-six-steps/"),
            ("cta", "Read: Business Intelligence Series, Part 3", "/blog/business-intelligence-part-3-what-to-watch/"),
            ("ask", "Which of the six problem types does your office ask about most often?"),
        ],
    },
    {
        "date": "December 7, 2026",
        "title": "Data Analytics Series, Part 6: Data Ethics and the Data Privacy Act for Analysts",
        "slug": "data-analytics-part-6-data-ethics-privacy",
        "category": "data",
        "summary": "Analysts handle other people’s information every day. This part explains the three privacy "
                   "principles of the Data Privacy Act in plain words, shows how a harmless-looking chart can "
                   "still reveal a person, and gives a checklist to run before any analysis leaves your desk.",
        "publish_on": "2026-12-07 21:00",
        "body": [
            "The analyst is proud of the new chart: business tax collections by barangay, by type of "
            "business, for the whole year. It goes into the monthly report and onto the bulletin board.",
            "A week later, a store owner comes to the office, upset. In her barangay there is only one "
            "hardware store, hers. The chart shows exactly how much the hardware stores in that barangay paid. "
            "Anyone who reads the bulletin board now knows what her business paid, and from that, roughly how much it sells, since business tax is based on gross sales. No name appeared on the chart. It still pointed to one person.",
            "(As always in this series, the office, the people and the numbers are made up. No real town or "
            "taxpayer is described.)",
            "Part 5 touched on privacy when choosing tools. This part goes further, because analysts make "
            "privacy decisions every time they choose what to collect, what to keep and what to show. When you finish reading, you will know the three principles the Data Privacy Act asks every analysis to "
            "follow, the ways a report can expose a person without naming them, and a short checklist to run "
            "before you share any result.",
            ("photo", "blog/data-privacy-principles.jpg", "The three general privacy principles of the Data "
             "Privacy Act: transparency, legitimate purpose and proportionality. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "Ethics Comes Before the Law"),
            "Data ethics asks a simple question: is this use of other people’s information fair to them? The "
            "law sets the minimum. Ethics asks whether you would be comfortable if the people in your data "
            "saw exactly what you did with it.",
            "In the Philippines, the minimum is the Data Privacy Act of 2012 (Republic Act No. 10173) and its "
            "implementing rules, overseen by the National Privacy Commission. It applies to government offices "
            "as well as private companies.",
            ("h", "The Three Principles in Plain Words"),
            "The law says that processing personal information must follow three general principles. Its "
            "implementing rules explain each one.",
            ("point", "Transparency", "The people in the data should know the nature, purpose and extent of "
             "what is done with their information. For an analyst, this means not using data in ways the "
             "office never told people about."),
            ("point", "Legitimate purpose", "Processing must fit a declared and specified purpose that is not "
             "against the law, morals or public policy. Data collected to issue a business permit is not "
             "automatically fair to use for something unrelated."),
            ("point", "Proportionality", "Processing must be adequate, relevant, suitable, necessary and not "
             "excessive for that purpose. If totals answer the question, use totals, not names."),
            "Put together, the three principles give an analyst a daily habit: before using a column, ask "
            "whether people were told, whether this use fits the reason it was collected, and whether you "
            "need it at all.",
            ("h", "Some Information Needs Extra Care"),
            "The law treats some information as sensitive personal information. It includes a person’s age, "
            "marital status, health, education, religious or political affiliations, and numbers issued by "
            "the government that are specific to the person, such as social security numbers and tax "
            "returns.",
            "Treasury records can contain some of these, especially government-issued numbers and details "
            "drawn from tax filings. Treat any column like that as off limits for analysis unless the purpose "
            "truly needs it and your office has approved its use.",
            ("h", "How a Report Can Point to One Person"),
            "The story at the start shows the trap. Removing names is not always enough. A report can still "
            "point to a person when:",
            ("point", "A group is very small", "If a category has only one or two members, its total is "
             "really their total. Merge small groups into a larger one, or show “fewer than five” instead of "
             "the exact figure."),
            ("point", "Details can be combined", "A barangay, a type of business and a year may each seem "
             "harmless. Together they can narrow a list down to one taxpayer."),
            ("point", "Rows are shared instead of results", "Sending a spreadsheet of individual records "
             "when only a summary was asked for exposes more than the question needed."),
            "The law itself recognizes the difference. Its rules allow personal data to be kept longer when it "
            "is aggregated or kept in a form that does not permit identification of the people in it. Shaping "
            "results so no one can be singled out protects people, and the rules treat such data differently.",
            ("quote", "Ask not only “Did I remove the names?” but “Could anyone still find the person?”"),
            ("h", "Ethics Beyond Privacy"),
            "Privacy is the part the law spells out. Ethical analysis also covers how results are presented.",
            ("point", "Honest charts", "Start bar charts at zero, label every axis, and do not hide a bad "
             "month by choosing a flattering time range."),
            ("point", "Fair comparisons", "Before ranking barangays or collectors, check whether they faced "
             "the same conditions. A low number may reflect a smaller area, not a weaker effort."),
            ("point", "Clear uncertainty", "Say when a cause is only likely, as Part 4 did, and show forecasts "
             "as ranges."),
            ("h", "People Have Rights Over Their Data"),
            "The implementing rules list rights that every data subject holds. Among them: the right to be "
            "informed, to object, to access their data, to have errors corrected, to have data blocked or "
            "erased on certain grounds, to damages, and, where data is processed electronically, to get a copy "
            "in a commonly used format.",
            "For an analyst, the right to correction has the most direct effect on daily work. If a taxpayer proves that a record is "
            "wrong, the fix must reach every copy, including the data you pulled for analysis last month.",
            ("h", "When Something Goes Wrong"),
            "Mistakes happen: a file is emailed to the wrong person, a laptop is lost, a shared folder is left "
            "open. Report it to your data protection officer at once.",
            "Under NPC Circular 16-03, when a reportable personal data breach happens, the office must notify "
            "the National Privacy Commission, and the affected people, within 72 hours of knowing about it. "
            "That clock only works if staff speak up quickly, so a culture where people report mistakes "
            "without fear is part of good data practice.",
            ("h", "Keep Working Copies Under Control"),
            "Analysis creates copies: an export for this report, a cleaned version, a version emailed for checking. "
            "Each copy is one more place where personal data can leak.",
            ("point", "Work from one approved location", "Keep working files in the folder or system your office has "
             "approved, not on a personal laptop, phone or private email."),
            ("point", "Strip what you do not need early", "Remove names, addresses and identification numbers in the "
             "first step if the question does not need them. Later copies are then safer by default."),
            ("point", "Delete when done", "When the report is final, delete the extra working copies and note in "
             "your notes file that you did."),
            ("h", "Before You Share: A Checklist"),
            ("point", "Purpose", "Does this analysis fit the reason the data was collected?"),
            ("point", "Minimum data", "Did I use only the columns the question needs?"),
            ("point", "Small groups", "Does any figure describe fewer than five people or businesses?"),
            ("point", "Combinations", "Could two or three details together point to one person?"),
            ("point", "Format", "Am I sharing results, not raw rows?"),
            ("point", "Storage", "Is my working copy saved only where the office allows, and will I delete "
             "it when the work is done?"),
            ("h", "Key Takeaways"),
            ("point", "Three principles", "Transparency, legitimate purpose and proportionality guide every "
             "use of personal data."),
            ("point", "No names is not enough", "Small groups and combined details can still identify a "
             "person."),
            ("point", "Share results, not rows", "Aggregated data protects people, and the rules allow it to be kept longer."),
            ("point", "Report mistakes fast", "Breach notice to the National Privacy Commission runs on a "
             "72-hour clock."),
            ("h", "Your Part 6 Exercise"),
            "Take the last report you shared and run the checklist above on it, line by line.",
            "Mark any figure that describes fewer than five people or businesses, and any table that could be "
            "a summary instead of a list. Fix one of them in the next edition. That single change is a real "
            "improvement in how your office treats the people behind its numbers.",
            ("cta", "Read: Your Data at the Treasury Counter", "/blog/your-data-at-the-treasury-counter/"),
            ("cta", "Read: Data Analytics Series, Part 5", "/blog/data-analytics-part-5-zero-budget-toolkit/"),
            ("cta", "Read: Data Analytics Series, Part 4", "/blog/data-analytics-part-4-four-questions-worked/"),
            ("cta", "Read: Cybersecurity Series, Part 6", "/blog/cybersecurity-part-6-cloud-and-privacy/"),
            ("ask", "Which figure in your office’s reports describes a group so small it could point to one person?"),
        ],
    },
    {
        "date": "December 2, 2026",
        "title": "Data Analytics Series, Part 5: The Analyst’s Toolkit on a Zero Budget",
        "slug": "data-analytics-part-5-zero-budget-toolkit",
        "category": "data",
        "summary": "No software budget is no excuse. This part lays out a complete analytics toolkit that costs "
                   "nothing to start: spreadsheets, a small database, Python, a free dashboard builder and a "
                   "plain notes file, with what each is good for and where each stops.",
        "publish_on": "2026-12-02 21:00",
        "body": [
            "The revenue clerk finishes an online course in data analytics and comes back to the office full "
            "of ideas. Then she checks the budget. There is no line for analytics software, and the next "
            "chance to add one is a year away. She decides the ideas will have to wait.",
            "They do not have to wait. Every step of the analysis process in this series can be done with "
            "tools that cost nothing to start. What they ask for instead is time to learn and care in how "
            "they are used.",
            "(Like every case in this series, this one is invented, from the office down to the last peso. No real town or "
            "taxpayer is described.)",
            "In Part 4, a whole analysis was done in a spreadsheet. This part widens the view to five kinds "
            "of free tools, what each one is good for, and where each one stops. After this post, you will be able to pick the right free tool for a task, know the limits to watch for, and set up a "
            "starter kit on your own computer this week.",
            ("photo", "blog/data-zero-budget-toolkit.jpg", "Five kinds of free tools cover the whole analysis: "
             "spreadsheets, a small database, Python, a dashboard builder and a notes file. (Illustration: "
             "Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "First, the Question"),
            "A tool cannot rescue a vague question. Part 2 started every analysis with the Ask step for a "
            "reason. Before opening any program, write the question in one sentence, name who will use the "
            "answer, and name the decision it supports. The cheapest tool that answers that question well is "
            "the right tool.",
            ("h", "1. Spreadsheets: The Place to Start"),
            "A spreadsheet is a quick way to look at a few thousand rows, add them up and spot "
            "something odd. Two free options are worth knowing.",
            ("point", "Google Sheets", "Free with a Google account and runs in a web browser. A single "
             "spreadsheet can hold up to 10 million cells."),
            ("point", "LibreOffice Calc", "Part of the free, open-source LibreOffice suite. It runs on the "
             "computer itself, so it works without an internet connection. Recent versions allow 1,048,576 "
             "rows in a sheet."),
            "Both have the tools used in Part 4: SUMIFS for totals with conditions, sorting and filtering, "
            "and pivot tables for quick summaries.",
            ("point", "Where it stops", "When the file gets slow, when the same cleaning steps must be "
             "repeated by hand every month, or when several people edit the same copy and nobody knows which "
             "version is right."),
            ("h", "2. A Small Database: SQLite"),
            "When the records outgrow a spreadsheet, the next step does not need a server. SQLite keeps a "
            "whole database in one ordinary file. Its authors have dedicated the code to the public domain, "
            "so anyone may use it for free.",
            "Python’s standard library includes a module for SQLite, so a standard Python installation can use it with nothing extra to install. For "
            "people who prefer clicking to typing, DB Browser for SQLite is a free, open-source program that "
            "lets you open the file, browse the tables and run SQL queries in a window.",
            "SQL is worth learning for one reason above all: a query is written down. Next month you run the "
            "same query on new data and get an answer built exactly the same way.",
            ("point", "Where it stops", "SQLite allows only one writer at a time per database file. That suits "
             "one analyst well. When many staff must enter records at the same moment all day, a server-based "
             "database is the better fit."),
            ("h", "3. Python: For Work You Repeat"),
            "Python is free to download and use. With the pandas library, which is also free and open source, "
            "a monthly report that takes an afternoon of copying and pasting can become a script that you run with one command and that gives the same result every time.",
            "The real gain is not speed. It is that every step is recorded. Anyone can read the script and "
            "see exactly how a number was produced, which makes the work easier to check and easier to hand "
            "over.",
            ("point", "Where it stops", "It takes practice before it saves time. Start with one "
             "report you prepare every month, not with the hardest problem in the office."),
            ("h", "4. Dashboards: Sharing the View"),
            "When the same numbers are needed by several people every week, a dashboard saves everyone from "
            "asking. Two free options are worth knowing.",
            ("point", "Data Studio", "Google’s web-based report builder, called Looker Studio until April "
             "2026. It has a no-cost tier, reads directly from Google Sheets, and shares a report through a "
             "link, the same way a document is shared."),
            ("point", "Power BI Desktop", "A free download from Microsoft for Windows computers. It is strong "
             "at linking several tables into one model, the topic of the Business Intelligence series. "
             "Building is free; sharing reports with others through Microsoft’s online service needs a paid "
             "license."),
            ("point", "Where it stops", "A dashboard only repeats what the data says. If the source sheet is "
             "wrong or late, the dashboard is wrong or late too, just in a nicer layout."),
            ("h", "5. A Notes File: The Tool That Makes Work Checkable"),
            "The last tool costs nothing and matters as much as the others: a plain text file or a simple document kept beside the data. For "
            "each analysis, write the question, where the data came from and on what date, every cleaning "
            "step, and any assumption you made.",
            "This file is what lets someone else check your work, and it is what lets you repeat the "
            "analysis next year without starting over. It costs nothing, and it is the first thing to reach "
            "for when someone questions a number.",
            ("quote", "Free tools lower the cost of starting. They do not lower the standard of the work."),
            ("h", "Free Is Not the Same as Safe"),
            "Free cloud tools keep your files on another company’s computers. Treasury records hold "
            "taxpayers’ names, addresses and payment details, which are protected under the Data Privacy Act "
            "of 2012 (Republic Act No. 10173).",
            "Before you upload anything, check your office’s rules on cloud services and ask your data "
            "protection officer. A safe habit is to work with totals, or to replace names with codes, before "
            "the data leaves the office computer. The collection analysis in Part 4, for example, needed only "
            "the amounts, the dates and the areas, not anyone’s name.",
            ("h", "What Free Tools Still Cost"),
            "Free software saves the license fee, not the effort. Three costs remain, and it helps to name them "
            "before you begin.",
            ("point", "Learning time", "Set aside a regular hour each week, with your head of office’s approval, "
             "so learning is part of the job rather than an after-hours hobby."),
            ("point", "A connection", "Browser-based tools need a working internet connection. Keep an offline "
             "copy of anything you need at the counter or in a meeting."),
            ("point", "Continuity", "If only one person knows how a script or a dashboard works, the office "
             "depends on that person. The notes file and a short handover session protect the work when people "
             "move to other posts."),
            ("h", "Which Tool for Which Job"),
            ("point", "A one-time total or a quick check", "A spreadsheet."),
            ("point", "Many months of records, asked the same questions again and again", "SQLite with saved "
             "queries."),
            ("point", "A monthly report built the same way every time", "A Python script."),
            ("point", "Numbers several people need to see every week", "A free dashboard builder."),
            ("point", "Every analysis, without exception", "A notes file."),
            ("h", "Key Takeaways"),
            ("point", "Start with the question", "The right tool is the cheapest one that answers it well."),
            ("point", "Know where each tool stops", "Move to the next tool when the current one gets slow, "
             "manual or confusing, not before."),
            ("point", "Write every step down", "A query, a script or a notes file makes your work checkable and "
             "repeatable."),
            ("point", "Protect personal data", "Use totals or codes before anything goes to a cloud service."),
            ("h", "Your Part 5 Exercise"),
            "Set up a starter kit this week:",
            ("point", "Install one offline tool", "LibreOffice, or Python if your office allows it."),
            ("point", "Rebuild one report", "Take a report you already prepare by hand and rebuild it once, "
             "using totals only, with no names."),
            ("point", "Start the notes file", "Write the question, the source, the date and each step. Keep it "
             "next to the data."),
            "Next month, run the same report again and compare how long it took. That difference is the first "
            "return on a toolkit that cost nothing.",
            ("cta", "Read: Data Analytics Series, Part 4", "/blog/data-analytics-part-4-four-questions-worked/"),
            ("cta", "Read: Data Analytics Series, Part 2", "/blog/data-analytics-part-2-six-steps/"),
            ("cta", "Read: Business Intelligence Series, Part 5", "/blog/business-intelligence-part-5-data-modeling/"),
            ("cta", "Read: Keep a receipts register in SQLite", "/tutorials/receipts-register-with-sqlite/"),
            ("ask", "Which report in your office would you rebuild first with free tools?"),
        ],
    },
    {
        "date": "November 27, 2026",
        "title": "Data Analytics Series, Part 4: Four Questions, One Data Set, Worked End to End",
        "slug": "data-analytics-part-4-four-questions-worked",
        "category": "data",
        "summary": "What happened, why, what is likely and what should we do? This part takes one made-up set of "
                   "real property tax records and answers all four questions in order, with every number "
                   "shown, so you can see how each answer builds on the last.",
        "publish_on": "2026-11-27 21:00",
        "body": [
            "“How are we doing, and what should we do in the last two months?” The head of office asks it at the November meeting, and the room goes quiet. Everyone has a feeling about the answer. Nobody has the answer.",
            "In Part 1, I introduced four kinds of analysis: descriptive, diagnostic, predictive and prescriptive. Definitions are easy to remember and hard to use, so this part puts them to work. It takes one small set of records and answers all four questions in order, with every number shown. By the end you will see how each answer feeds the next, and you will have a four-line routine to try on your own reports.",
            "(As always in this series, the office, the people and every number below are made up. No real "
            "town or taxpayer is described. The arithmetic, however, is real, so you can check every step.)",
            ("photo", "blog/data-four-questions.jpg", "Four questions asked of one data set, in order: describe "
             "what happened, diagnose why, predict what is likely, and prescribe what to do. (Illustration: "
             "Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "The Situation"),
            "A municipal treasury has a real property tax collection target of ₱12,000,000 for the year. It is early November, and the question from the meeting is waiting for an answer.",
            "The analyst has the office’s collection records from January to October of this year and the same "
            "records for the past three years. That is all. No new survey, no special software. A spreadsheet "
            "is enough.",
            ("h", "Question 1, Descriptive: What Happened?"),
            "Start by adding up what was collected, by period, and compare it with the same period last year.",
            ("point", "This year, January to October", "First quarter ₱4,200,000; second quarter ₱1,900,000; "
             "third quarter ₱1,500,000; October ₱800,000. Total ₱8,400,000."),
            ("point", "Against the target", "₱8,400,000 is 70% of the ₱12,000,000 target."),
            ("point", "Against last year", "The same ten months last year brought in ₱8,900,000. This year is "
             "₱500,000 lower, a drop of about 5.6%."),
            "That is the descriptive answer, and it is already useful. The office is behind last year, and it "
            "has 30% of its target left to collect in two months. But a total does not say where the money went "
            "missing, so the next question follows naturally.",
            ("h", "Question 2, Diagnostic: Why Did It Happen?"),
            "A drop in a total can come from anywhere. The analyst breaks the same numbers down by area and "
            "compares each part with last year.",
            ("point", "Town-center barangays", "₱5,600,000 this year against ₱5,550,000 last year. Up ₱50,000."),
            ("point", "Coastal barangays", "₱1,450,000 against ₱2,000,000. Down ₱550,000, or 27.5%."),
            ("point", "Upland barangays", "₱1,350,000 against ₱1,350,000. No change."),
            "The parts add up: ₱5,600,000 plus ₱1,450,000 plus ₱1,350,000 is ₱8,400,000, and the changes, plus "
            "₱50,000, minus ₱550,000 and zero, explain the whole ₱500,000 drop. Almost all of it is in the "
            "coastal barangays.",
            "Now the analyst asks the people who know the ground. The collectors explain that last year the "
            "office held six roving collection days in the coastal barangays during the third quarter. This "
            "year it held only two, because the service vehicle was under repair.",
            "Is that the cause? It is a strong lead, not yet proof. The timing fits, the place fits and the "
            "size is plausible. A careful analyst says exactly that: “The drop is concentrated in the coastal "
            "barangays, and it matches the reduced roving collection days. Other causes are possible, but this "
            "one fits the evidence best.”",
            ("h", "Question 3, Predictive: What Is Likely to Happen?"),
            "The head of office now wants to know where the year will end. The analyst looks at the past three "
            "years and asks: by the end of October, what share of the full year’s collection had usually come "
            "in?",
            ("point", "The past three years", "81%, 80% and 82% of each year’s total had been collected by the "
             "end of October."),
            ("point", "The projection", "If this year follows the same pattern, the full-year total is "
             "₱8,400,000 divided by that share. At 82%, that is about ₱10,240,000. At 80%, about ₱10,500,000. "
             "At the middle value of 81%, about ₱10,370,000."),
            ("point", "Against the target", "The likely year-end range of ₱10.2 to ₱10.5 million leaves a "
             "shortfall of roughly ₱1.5 to ₱1.8 million against the ₱12,000,000 target."),
            "Notice two things. First, the forecast is a range, not a single number. Three years of history is "
            "not much, and an honest forecast shows its uncertainty. Second, the forecast assumes nothing "
            "changes. Its real value is to show what will happen if the office does nothing different, which "
            "is exactly what the last question is about.",
            ("h", "Question 4, Prescriptive: What Should We Do?"),
            "Prescriptive analysis compares possible actions by their likely effect. The analyst lists two "
            "options, using the office’s own past results.",
            ("point", "Option A: restore roving days", "Last year, each roving collection day in the coastal "
             "barangays brought in about ₱90,000 on average. Four extra days in November and December could "
             "bring in about ₱360,000."),
            ("point", "Option B: letters to the largest delinquent accounts", "Last year, a similar round of "
             "letters to 40 accounts led about one in four to pay, at an average of ₱15,000 each. The same "
             "result this year would be about 10 payments, or ₱150,000."),
            ("point", "Both together", "About ₱510,000, if the past results hold."),
            "Then comes the uncomfortable part, which a good analyst does not hide. Even both options together would close only about a third of the smaller ₱1.5 million gap. The recommendation therefore has three "
            "lines: restore the roving days, send the letters, and tell the local chief executive and the "
            "budget office now that the year is likely to end below target, so they can plan for it.",
            ("quote", "A good recommendation tells people what to do and what it will not fix."),
            ("h", "How the Four Answers Fit Together"),
            "Look back at the chain. The descriptive answer showed a gap. The diagnostic answer found where it "
            "was. The predictive answer showed how big it would become if nothing changed. The prescriptive "
            "answer compared actions and was honest about their limits.",
            "Skip any link and the chain breaks. Without the diagnosis, the office might have sent letters "
            "everywhere instead of fixing the coastal schedule. Without the forecast, nobody would have known "
            "that the gap was too big to close, and the shortfall would have been a surprise in January.",
            ("h", "Doing It in a Spreadsheet"),
            "None of this needs special software. With one table of payments, where each row has a date, an "
            "area and an amount, the whole analysis takes four small steps.",
            ("point", "Totals by period", "Use SUMIFS to add the amounts between two dates, once for this year "
             "and once for last year."),
            ("point", "Totals by area", "Use SUMIFS again, with the area as a second condition. A pivot table "
             "does the same job in a few clicks."),
            ("point", "The projection", "Divide this year’s total so far by each past year’s October share. "
             "Show the smallest and largest results as the range."),
            ("point", "The options", "Multiply each past result by the planned number of days or letters, "
             "and write the assumption next to the answer."),
            "Keep each step on its own sheet, with a short note at the top saying what it does. Anyone in the "
            "office can then follow the work and check it, which matters as much as the result.",
            ("h", "What to Check Before You Present"),
            ("point", "Do the parts add up to the whole?", "Here, the three areas add up to ₱8,400,000 and the "
             "changes add up to the ₱500,000 drop. If they do not, something is missing or counted twice."),
            ("point", "Are the periods the same?", "Compare January to October with January to October, not "
             "with a full year."),
            ("point", "Is the cause confirmed or only likely?", "Say which one, in plain words."),
            ("point", "Is the forecast a range?", "A single number suggests more certainty than the data gives."),
            ("h", "Key Takeaways"),
            ("point", "Each answer feeds the next", "Describe the gap, find where it is, size it, then choose what to do."),
            ("point", "Say how sure you are", "A likely cause is not a proven one, and a forecast is a range, not a single number."),
            ("point", "Tell people what will not be fixed", "An honest recommendation lets the office plan for the shortfall early."),
            ("h", "Your Part 4 Exercise"),
            "Take any total your office reports every month. Then try the four questions on it, one line each:",
            ("point", "Describe", "What was the total, and how does it compare with the same period last year?"),
            ("point", "Diagnose", "Break it into two or three parts. Which part explains most of the change?"),
            ("point", "Predict", "Using past years, where is it likely to end, as a range?"),
            ("point", "Prescribe", "Name one action, its likely effect, and what it will not fix."),
            ("cta", "Read: Data Analytics Series, Part 3", "/blog/data-analytics-part-3-deciding-with-data/"),
            ("cta", "Read: Data Analytics Series, Part 1", "/blog/data-analytics-part-1-what-it-is/"),
            ("cta", "Read: Business Intelligence Series, Part 3", "/blog/business-intelligence-part-3-what-to-watch/"),
            ("cta", "Read: Year-End in the Treasury", "/blog/year-end-in-the-treasury/"),
            ("ask", "Which of the four questions does your office usually skip?"),
        ],
    },
    {
        "date": "November 22, 2026",
        "title": "Data Analytics Series, Part 3: Deciding With Data, Not Hunches",
        "slug": "data-analytics-part-3-deciding-with-data",
        "category": "data",
        "summary": "Experience and data are not rivals. Here is what a data-driven decision really looks like in a "
                   "local treasury, five ways analysts think before they touch a formula, and the traps that turn "
                   "good numbers into bad choices.",
        "publish_on": "2026-11-22 21:00",
        "body": [
            "Every December, a treasury holds the same short meeting. Should the office open on "
            "the Saturday before the business tax deadline? Business taxes are due within the "
            "first twenty days of January, and every year the last few days bring long lines.",
            "One senior collector is sure it is worth it. “People always come on Saturdays.” A "
            "clerk is just as sure it is not. “Last time we opened, the room was half empty by "
            "ten.” The head of office has to approve overtime and keep the vault staffed either "
            "way. Two experienced people, two opposite hunches, one decision.",
            "(Like every case in this series, this one is invented, from the office down to the last peso. No "
            "real town or taxpayer is described.)",
            "This part is about what happens next in an office that thinks like an analyst. It is"
            " not about fancy tools. It is about a habit: checking what the records say before "
            "deciding, and being honest about what they cannot say. Stay with me to the end, and you will know how to weigh experience against records, five thinking habits analysts "
            "use, the traps that spoil good data, and how to write a short decision note.",
            ("h", "What “Data-Driven” Really Means"),
            "A data-driven decision is one where evidence, gathered and checked with care, "
            "carries real weight in the choice. It does not mean the spreadsheet decides. People "
            "still decide. The data simply makes sure they are arguing about facts instead of "
            "memories.",
            "Some practitioners prefer the phrase data-inspired, and the difference is useful. A "
            "data-driven choice follows closely from a clear analysis. A data-inspired choice "
            "uses data to spark ideas or test a hunch, while leaving room for things the numbers "
            "cannot measure, such as goodwill with taxpayers or the morale of a tired staff. A "
            "decision can land somewhere in between, and that is fine as long as everyone knows "
            "which is which.",
            ("h", "Experience Is Data Too"),
            "The senior collector’s hunch is not worthless. Years at the counter are a kind of "
            "data, stored in a person instead of a table. The trouble is that one person sees "
            "only part of the picture, and a single memorable day can stand in for many ordinary "
            "ones.",
            "The best decisions use both. Experience suggests what to look at and what might "
            "explain it. Records show whether the pattern is real, how big it is and whether it "
            "has changed. When the two disagree, that is not a crisis. It is the most interesting"
            " moment in the whole analysis.",
            ("h", "Back to the Saturday Question"),
            "Here is how the office could settle it in an afternoon.",
            ("point",
             "Ask the real question",
             "Not “Do people come on Saturdays?” but “Would a Saturday opening in mid-January "
             "serve enough taxpayers to justify the cost, and would it shorten the lines on the "
             "last weekdays?”"),
            ("point",
             "Look at the records",
             "The office pulls the business tax receipts from the past three Januaries and counts"
             " them by date of payment. In the one year it opened on a Saturday, it has that "
             "day’s count too."),
            ("point",
             "Read the pattern",
             "Suppose the counts show that the Saturday opening served 140 taxpayers, almost all "
             "before eleven, and that the following Monday was about 20% lighter than the same "
             "Monday in other years. Both hunches were partly right: people did come, but only in"
             " the morning."),
            ("point",
             "Decide, then measure again",
             "Open on that Saturday, but only from eight to noon, and count again next January to"
             " see whether the result holds."),
            "Neither the collector nor the clerk lost the argument. The decision is better than "
            "either hunch, and it costs less than a full day.",
            ("h", "Five Ways an Analyst Thinks"),
            "Before typing a single formula, good analysts use a handful of thinking habits. You "
            "may already use some of them without naming them.",
            ("photo",
             "blog/data-analyst-thinking.jpg",
             "Five thinking habits that come before any formula: see it, plan it, frame it, "
             "connect it, and zoom between the whole and the part. (Illustration: Butch Mahinay, "
             "aumahinay.dev)",
             "medium"),
            ("point",
             "See it",
             "Picture the data before you calculate. A quick chart of receipts by day often "
             "answers the question faster than a table."),
            ("point",
             "Plan it",
             "Decide what you will do and in what order: which records, which period, which "
             "comparison. A plan keeps you from wandering."),
            ("point",
             "Frame it",
             "Keep the problem at the center. Every step should help answer the question that was"
             " asked, not a more interesting one."),
            ("point",
             "Connect it",
             "Look for links between things. Do long lines on the last day go with a slow first "
             "week? Remember that a link is not proof that one causes the other."),
            ("point",
             "Zoom in and out",
             "Move between the big picture and the details. The total for January matters, and so"
             " does the single day when the system was down."),
            ("h", "Traps That Spoil Good Data"),
            "Data does not protect you from bad decisions on its own. These traps can catch even "
            "experienced people.",
            ("point",
             "Looking only for support",
             "If you already believe Saturdays are busy, you will notice the one busy Saturday "
             "and stop looking. Decide what evidence would change your mind before you look."),
            ("point",
             "Trusting the loudest story",
             "One angry complaint can feel bigger than a hundred quiet payments. Count before you conclude."),
            ("point",
             "Forgetting the context",
             "A day with few receipts may have been a typhoon day, a holiday or a day the system "
             "was down. Numbers without notes can lie by accident."),
            ("point",
             "Measuring what is easy",
             "Receipts are easy to count. Waiting time is not, because no record shows when a "
             "person joined the line. Be honest about what your data cannot see, and find another"
             " way to check it, even if that means standing in the room with a notebook for an "
             "hour."),
            ("point",
             "Stopping at the decision",
             "A data-driven choice is a test. If you never measure the result, you will never "
             "learn whether it worked."),
            ("quote",
             "Data does not make the decision. It makes sure the decision is about the right facts."),
            ("h", "Write the Decision Down"),
            "One small habit makes every data-driven decision easier to learn from: a short "
            "decision note. It takes five minutes and fits on half a page.",
            ("point", "The question", "What exactly was being decided, in one sentence."),
            ("point",
             "The evidence",
             "Which records were used, for which period, and what they showed. Include the "
             "numbers, not just the conclusion."),
            ("point",
             "The choice and the reason",
             "What was decided, and which part of the evidence or experience tipped it."),
            ("point", "The check", "What will be measured afterwards, and on what date someone will look."),
            "Next December, when the same meeting comes around, nobody has to rely on memory. The"
            " office opens the note, compares the prediction with what actually happened, and "
            "decides again with better information. Over a few years, these notes become a "
            "valuable record, because they show not only what was done but why.",
            ("h", "When the Data Is Not Enough"),
            "Sometimes the records simply cannot answer the question. A new kind of fee has no "
            "history. A change in the law makes old patterns useless. A decision must be made "
            "today and the data will take a week to clean.",
            "In those cases, a good analyst says so plainly. “We do not have enough data to know."
            " Here is our best judgment, here is what it rests on, and here is how we will check "
            "it in a month.” That sentence is more useful, and more honest, than a confident "
            "number built on weak ground.",
            ("h", "Key Takeaways"),
            ("point",
             "Experience is data too",
             "Years at the counter suggest where to look. Records show whether the pattern is "
             "real and how big it is."),
            ("point",
             "Decide what would change your mind",
             "Write it down before you look, so you do not notice only the evidence that agrees with you."),
            ("point",
             "Count before you conclude",
             "One loud story can outweigh a hundred quiet records unless someone counts."),
            ("point",
             "Write a decision note",
             "Half a page on the question, the evidence, the choice and the check turns every "
             "decision into a lesson."),
            ("h", "Your Part 3 Exercise"),
            "Think of one recurring decision in your office that is usually settled by opinion. Then write:",
            ("point", "The two hunches", "What do the different sides believe, and why?"),
            ("point",
             "The record that could settle it",
             "Which existing record, with a date on it, would show who is right?"),
            ("point",
             "What would change your mind",
             "Before looking, write the result that would make you drop your own hunch."),
            "If you can, spend thirty minutes pulling that record. Even a rough count by day can "
            "be enough to move the conversation from memories to facts.",
            ("cta", "Read: Data Analytics Series, Part 2", "/blog/data-analytics-part-2-six-steps/"),
            ("cta", "Read: Data Analytics Series, Part 1", "/blog/data-analytics-part-1-what-it-is/"),
            ("cta",
             "Read: The ALTOS Framework, Principle 9: Evidence Before Decision",
             "/blog/altos-framework-evidence-before-decision/"),
            ("cta",
             "Read: Business Intelligence Series, Part 3",
             "/blog/business-intelligence-part-3-what-to-watch/"),
            ("ask",
             "What decision in your office is still settled by whoever argues longest? What "
             "record could settle it instead?"),
        ],
    },
    {
        "date": "November 17, 2026",
        "title": "Data Analytics Series, Part 2: The Six Steps of Every Analysis",
        "slug": "data-analytics-part-2-six-steps",
        "category": "data",
        "summary": "Ask, Prepare, Process, Analyze, Share and Act. Here is what each step means, the mistakes that "
                   "happen when one is skipped, and a full worked example: deciding whether a treasury office "
                   "needs a second payment window.",
        "publish_on": "2026-11-17 21:00",
        "body": [
            "Every week, someone in a government office opens a spreadsheet, scrolls through a "
            "few thousand rows, makes a chart and sends it to the boss. Sometimes it helps. Often"
            " it does not, and nobody can say exactly why. The chart was correct. The numbers "
            "added up. Yet no decision came out of it.",
            "In a case like this, the problem is not the math. It is the order of the work. The "
            "person started with the data and hoped a question would appear. Good analysis runs "
            "the other way around, and it follows a set of steps that experienced analysts repeat"
            " almost without thinking.",
            "In Part 1, we described data analytics as the craft of turning everyday records into"
            " answers people can act on. This part lays out the road from the first question to "
            "the final decision. When you finish reading, you will know the six steps of every "
            "analysis, see them used on a real office question, and know what goes wrong when a "
            "step is skipped.",
            ("h", "Six Steps, in Plain Words"),
            "The Google Data Analytics Professional Certificate teaches the process as six "
            "phases: Ask, Prepare, Process, Analyze, Share and Act. Other courses and companies "
            "use different names. An older and widely used model called CRISP-DM, developed in "
            "the late 1990s, also has six phases, starting with understanding the business "
            "problem and ending with putting the results to use. The labels differ, but the logic"
            " is the same everywhere. Here is that logic in my own words.",
            ("point",
             "Ask",
             "Decide exactly what you need to know, who needs to know it, and what they will do "
             "with the answer."),
            ("point",
             "Prepare",
             "Find the data that can answer the question, and check where it came from and "
             "whether it can be trusted."),
            ("point",
             "Process",
             "Clean the data: fix errors, remove duplicates, handle blanks and make the format consistent."),
            ("point",
             "Analyze",
             "Organize the clean data, calculate, compare and look for patterns that answer the question."),
            ("point",
             "Share",
             "Show the findings to the people who decide, in a form they can understand quickly."),
            ("point", "Act", "Make the decision, carry it out, and measure again to see whether it worked."),
            ("quote", "Start with the question, not the spreadsheet."),
            ("photo",
             "blog/data-six-steps.jpg",
             "The six steps of an analysis form a loop: after Act, you measure again and, if "
             "needed, start over with a sharper question. (Illustration: Butch Mahinay, "
             "aumahinay.dev)",
             "medium"),
            "The best way to understand the six steps is to watch them at work. So let us follow "
            "one ordinary office problem from beginning to end.",
            ("h", "A Worked Example: Do We Need a Second Window?"),
            "Imagine a municipal treasury with one payment window for walk-in taxpayers. (As "
            "always in this series, the office and the numbers are made up.) Every few weeks "
            "someone complains about the long line. A staff member suggests opening a second "
            "window. The head of office cannot simply say yes, because a second window means "
            "moving a person away from other work. She wants evidence first.",
            ("h", "Step 1: Ask"),
            "The first version of the question is “Are the lines too long?” That sounds "
            "reasonable, but it cannot be answered. Too long for whom? Every day, or only on some"
            " days? Compared with what?",
            "A better question is specific and tied to a decision: “On which days and hours does "
            "the wait at the payment window go beyond 30 minutes, and would a second window on "
            "those days alone fix it?”",
            "Now everyone knows what a good answer looks like. It also tells us who the answer is"
            " for, the head of office, and what she will do with it: decide whether to open a "
            "second window, and when. Notice that the question already hints at a cheaper option "
            "than a full-time window. Good questions often do.",
            ("h", "Step 2: Prepare"),
            "Next, find the data. Every payment produces an official receipt with a date and, in "
            "many systems, a time. That gives us when each transaction was finished. It does not "
            "tell us when each person joined the line, which is what waiting time really is.",
            "So the analyst has two choices: use the receipt times as a stand-in, or collect new "
            "data. In our example, the office does both. It pulls a full year of receipt times "
            "from its records. Then, for two weeks that include the busy days before the March 31"
            " real property tax deadline, a staff member writes down the time each person takes a"
            " queue number and the time the person is served.",
            "This step is also where we check the data. Who recorded it? Is it complete, or are "
            "some days missing? Were the receipt clocks set correctly? A receipt system whose "
            "clock runs ten minutes fast will quietly distort every result that follows.",
            ("h", "Step 3: Process"),
            "Real records are messy. When our analyst opens the files, the problems appear quickly:",
            ("point",
             "Duplicates",
             "A few receipts were printed twice after a printer jam and appear twice in the export."),
            ("point",
             "Cancelled receipts",
             "Some receipts were cancelled and reissued, so counting them would inflate the "
             "number of transactions."),
            ("point",
             "Inconsistent times",
             "The handwritten log mixes “2:15 PM” with “14:15” and, on one page, just “2:15”."),
            ("point",
             "Gaps",
             "One afternoon has no handwritten entries at all because the staff member was called"
             " to a meeting."),
            "Cleaning means removing the duplicates, leaving out cancelled receipts, writing "
            "every time in one format and marking the afternoon with no entries as missing "
            "instead of pretending it was quiet. Each change is written down, so anyone can see "
            "what was done and why. This step is rarely exciting, but it is where an analysis can"
            " be won or lost.",
            ("h", "Step 4: Analyze"),
            "With clean data, the analyst can finally count and compare. The two-week log shows "
            "how long each person waited, and it reveals a simple link: once one window gets more"
            " than about 25 payers in an hour, the wait climbs past 30 minutes. The analyst then "
            "counts receipts by day and by hour across the whole year to find every hour above "
            "that level. Three patterns stand out:",
            ("point",
             "The rush is predictable",
             "Most long waits happen in the first three weeks of January and in the days just "
             "before each quarterly real property tax deadline."),
            ("point",
             "Mornings are worse",
             "On busy days, the line peaks between 9 and 11 in the morning. Afternoons are usually calm."),
            ("point",
             "Ordinary days are fine",
             "On most days, the window serves well under 25 payers an hour, and the log shows "
             "typical waits of under ten minutes."),
            "The answer to the question is now clear. Waits go beyond 30 minutes on about "
            "twenty-five mornings a year, all of them predictable. A second window every day "
            "would sit idle most of the time. A second window on those mornings would cover "
            "nearly all the long waits.",
            ("h", "Step 5: Share"),
            "The head of office does not need the spreadsheet. She needs the answer, the evidence"
            " and a recommendation, on one page. The analyst prepares a simple bar chart showing,"
            " for each month, how many morning hours had more than 25 payers, a short table of "
            "the peak days and hours, and three sentences:",
            "“Long waits are not an everyday problem. They happen on about twenty-five "
            "predictable mornings a year, mostly in January and before quarterly deadlines. "
            "Opening a second window on those mornings only would cover nearly all of them, "
            "without taking a person away from other work for the rest of the year.”",
            "Notice what is left out: the cleaning details, the formulas and the dozens of other "
            "charts the analyst made while exploring. Those stay in the analyst's notes in case "
            "someone asks. Sharing is about what the decision maker needs, not about showing how "
            "hard the analyst worked.",
            ("h", "Step 6: Act"),
            "The head of office approves a second window on peak mornings and posts the schedule "
            "at the entrance and on the town's page. That is the decision. But the process is not"
            " finished.",
            "After the next January, the office keeps the two-week waiting log again, and the "
            "analyst compares the new numbers with the old ones. Did waits drop below 30 minutes?"
            " Did the second window get used? If the answer is yes, the change stays. If not, the"
            " office goes back to Step 1 with a sharper question. This loop is the quiet strength"
            " of the process. Every decision becomes a small experiment, and every experiment "
            "teaches the office something.",
            ("h", "What Goes Wrong When a Step Is Skipped"),
            "Each step protects against a common mistake. It helps to know them by name.",
            ("point",
             "Skipping Ask",
             "You produce a beautiful report that answers nothing. Everyone nods, and nothing changes."),
            ("point",
             "Skipping Prepare",
             "You trust data you should not. The clock was wrong, half the days were missing, or "
             "the file was last month's."),
            ("point",
             "Skipping Process",
             "Duplicates and cancelled receipts inflate the totals, and a correct formula gives a"
             " wrong answer."),
            ("point",
             "Skipping Analyze",
             "You jump from a hunch to a conclusion. “Everyone knows January is busy” is true, "
             "but it does not tell you how many staff you need or when."),
            ("point",
             "Skipping Share",
             "The findings stay in the analyst's head or laptop, and the people who decide never see them."),
            ("point",
             "Skipping Act",
             "The report is filed, the meeting ends, and the same problem returns next year."),
            ("h", "The Steps Are a Loop, Not a Ladder"),
            "In practice, analysts move back and forth. While cleaning, you may discover that a "
            "key field was never recorded, which sends you back to Prepare. While analyzing, you "
            "may find that the question was too narrow, which sends you back to Ask. That is "
            "normal. The six steps are a guide for thinking, not a form to fill in from top to "
            "bottom.",
            "What matters is that each step happens at least once, and that Ask comes first. A "
            "clear question makes every later step easier, because it tells you which data to "
            "look for, what to clean, what to calculate and what to show.",
            ("h", "Where the Six Steps Live in a Treasury System"),
            "A good information system can make some steps much lighter. When I designed ALTOS "
            "for Philippine local treasuries, I tried to support the steps that usually take the "
            "most effort. Receipts and deposits are recorded as they happen, with their dates and"
            " amounts, so the Prepare step does not start with a box of paper. Checks for "
            "duplicates and missing details help the Process step. Reports and charts make Share "
            "faster.",
            "But no system can do Ask or Act for you. Choosing the right question and making the "
            "decision remain human work, and that is exactly as it should be.",
            ("h", "Key Takeaways"),
            ("point",
             "Ask comes first",
             "A specific question tied to a decision tells you which data to find, what to clean "
             "and what to show."),
            ("point",
             "Check before you trust",
             "Duplicates, cancelled receipts and wrong clocks can make a correct formula give a "
             "wrong answer."),
            ("point",
             "Share the answer, not the work",
             "The decision maker needs the finding, the evidence and a recommendation on one page."),
            ("point",
             "Act, then measure again",
             "Every decision is a small experiment. Measure the result and loop back if it did not work."),
            ("h", "Your Part 2 Exercise"),
            "Take the question you wrote down after Part 1. If you did not do it yet, choose one "
            "now. Then write one or two lines for each step:",
            ("point", "Ask", "Rewrite your question so it is specific and names the decision it supports."),
            ("point", "Prepare", "List the data you would need, and where each piece comes from."),
            ("point", "Process", "Guess the three most likely problems in that data."),
            ("point", "Analyze", "Write the calculation or comparison that would answer the question."),
            ("point",
             "Share",
             "Name the person who needs the answer, and the one chart you would show them."),
            ("point", "Act", "Write what would change, and how you would know if it worked."),
            "If you can fill in all six, you already have the plan for a real analysis.",
            ("cta", "Read: Data Analytics Series, Part 1", "/blog/data-analytics-part-1-what-it-is/"),
            ("cta",
             "Read: The ALTOS Framework, Principle 9: Evidence Before Decision",
             "/blog/altos-framework-evidence-before-decision/"),
            ("cta", "Read: Year-End in the Treasury", "/blog/year-end-in-the-treasury/"),
            ("cta",
             "Try the free Python lesson: Build a simple RCD summary with pandas",
             "/tutorials/rcd-summary-with-pandas/"),
            ("ask",
             "Which step do you find hardest in your own work: asking the right question, finding"
             " the data, cleaning it, or getting people to act on it?"),
        ],
    },
    {
        "date": "November 13, 2026",
        "title": "Data Analytics Series, Part 1: What Data Analytics Really Is, and Why Every Office Already Has the Data",
        "slug": "data-analytics-part-1-what-it-is",
        "category": "data",
        "summary": "Data analytics is the craft of turning everyday records into answers people can act on. "
                   "Here is what it means, the four kinds of questions it can answer, a famous cholera map from 1854, "
                   "and why a local treasury is already sitting on a mountain of useful data.",
        "publish_on": "2026-11-13",
        "body": [
            "Picture a Monday morning in a municipal treasury office. The mayor calls and asks a "
            "simple question: “Will we reach our real property tax target this year?” Someone "
            "opens a logbook. Someone else starts adding up receipt stubs from the past months. "
            "By lunchtime, the office has a total, but not yet an answer.",
            "(As in all my examples, the office and the numbers are made up. No real taxpayer or "
            "town is described.)",
            "The answer was in the office all along. It was written, line by line, on thousands "
            "of official receipts: who paid, how much, for what, and on which day. What was "
            "missing was a way to turn those records into something the mayor could decide on. "
            "That way has a name. It is data analytics, and this post is the first in a series "
            "about it.",
            ("h", "Why I Am Writing This Series"),
            "I completed the Google Data Analytics Professional Certificate on Coursera, and "
            "later the Google Advanced Data Analytics Professional Certificate. What I learned "
            "there did not stay in the classroom. It shaped how I think about treasury records, "
            "and it became one of the foundations of ALTOS, the system I built for Philippine "
            "local treasuries.",
            "Data analytics lessons online can use examples such as online shops or bike rentals."
            " Those are fine, but they can feel far from a town hall in the province. This series"
            " explains the same ideas in plain words, with examples from the work I know: "
            "collections, disbursements, targets, deadlines and the people at the counter. By the"
            " end of this post, you will know what data analytics is, the four kinds of questions"
            " it answers, and why your office already holds the data to start.",
            ("h", "Data, Information and Insight"),
            "Three words are often mixed up, so let us start there. Think of them as three steps "
            "on a ladder.",
            ("point",
             "Data",
             "Raw facts, recorded one at a time. A single official receipt is data: receipt "
             "number 1234567, dated March 3, ₱2,450.00, real property tax, paid by a named owner,"
             " received by a named collector. On its own, one receipt tells you very little."),
            ("point",
             "Information",
             "Data that has been organized so it means something. “We collected ₱1.8 million in "
             "real property tax in the first quarter” is information. It came from hundreds of "
             "receipts, added up and grouped by period."),
            ("point",
             "Insight",
             "Information that explains something and points to an action. “Most of the shortfall"
             " comes from three barangays where no collection day was held this year” is an "
             "insight. It tells the office where to look and what to do next."),
            "Data analytics is the work of climbing that ladder on purpose: from scattered "
            "records, to organized information, to an insight that someone can act on.",
            ("quote", "Data is what happened. Insight is what you can do about it."),
            ("h", "So What Is Data Analytics?"),
            "Here is a working definition in plain words. Data analytics is the practice of "
            "collecting, cleaning, organizing and examining data in order to answer questions and"
            " support decisions.",
            "Notice the last part. Analytics is not about producing more reports or prettier "
            "charts. It exists to help a person decide something: where to send collectors, when "
            "to open an extra window, which accounts to follow up first, or whether a new "
            "procedure is working.",
            "You will also hear two related terms. A data analysis is one investigation, such as "
            "checking why collections dropped in May. Data analytics is the whole discipline "
            "around it: the process, the tools, the habits and the people. Data science is a "
            "wider field still. It includes building new statistical models and machine learning "
            "systems. A good analyst borrows from it, but you do not need it to begin.",
            ("h", "A Cholera Outbreak and a Famous Map"),
            "A famous story in this field happened long before computers. On August 31, 1854, "
            "cholera broke out in Soho, a crowded neighborhood in London. Hundreds of people died"
            " within days. Most doctors at the time believed the disease spread through foul air.",
            "A physician named John Snow suspected the water instead. He went through the records"
            " of who had died and where they had lived, and he asked families where they drew "
            "their water. Again and again, the answer led to one public pump on Broad Street. He "
            "also studied the exceptions. A brewery stood nearby, but none of its workers was "
            "recorded as dying of cholera. They drank the beer they were given, and the brewery "
            "had its own deep well.",
            "On September 7, Snow presented his findings to the local parish board. The next day,"
            " the handle of the pump was removed so no one could use it. Snow himself noted that "
            "the outbreak was already slowing by then, and that many residents had fled. That "
            "honesty is part of the lesson. His evidence was strong enough to act on, and he did "
            "not claim more than it showed.",
            "A few months later, Snow drew the picture that made the case famous. On a street map"
            " of the area, he placed a small mark for each death at its address. The marks pile "
            "up around the Broad Street pump and thin out farther away. Anyone could see the "
            "pattern in seconds, even without reading his tables.",
            "Snow had no spreadsheet, no database and no software. He had a clear question, "
            "carefully collected records, the courage to bring his evidence to the people who "
            "could act, and a simple picture that made the pattern plain to everyone. Those four "
            "things are still the heart of data analytics today.",
            ("h", "Four Kinds of Questions"),
            "Analysts often sort their work into four types, each answering a different question."
            " Here they are with treasury examples.",
            ("point",
             "Descriptive: What happened?",
             "Total collections last month by revenue source. This is the base for everything else."),
            ("point",
             "Diagnostic: Why did it happen?",
             "Business tax collections fell 12% compared with last January. Was it fewer "
             "businesses, smaller declared sales, or simply that more owners chose to pay in "
             "quarterly installments instead of the full year at once?"),
            ("point",
             "Predictive: What is likely to happen?",
             "Based on the pattern of the past three years, where will real property tax "
             "collections probably end by December, and how wide is the range of likely results?"),
            ("point",
             "Prescriptive: What should we do?",
             "Given the forecast, which barangays should get a collection day first, and which "
             "delinquent accounts deserve a personal visit rather than a letter?"),
            "Each type builds on the one before it. You cannot explain a drop you have not "
            "measured, and you cannot plan around a forecast you do not trust. That is why the "
            "first steps deserve care.",
            ("h", "You Do Not Need Expensive Software"),
            "A common worry is that analytics needs costly tools or a degree in mathematics. It "
            "does not. Useful analysis in a small office can start with tools that are free or "
            "already installed:",
            ("point",
             "A spreadsheet",
             "Google Sheets, LibreOffice Calc or Excel. Sorting, filtering, formulas and pivot "
             "tables will take you remarkably far."),
            ("point",
             "A database and SQL",
             "When records grow into tens of thousands of rows, a database such as SQLite keeps "
             "them organized, and SQL is the language for asking it questions."),
            ("point",
             "A charting tool",
             "A good chart can make a pattern obvious in seconds, as Snow's map did. Spreadsheets"
             " and free tools such as Looker Studio can do this."),
            ("point",
             "A programming language",
             "Python, later on, for work that is repeated every month or is too large for a "
             "spreadsheet. My free Python tutorials already cover some of this."),
            "The tool matters less than the thinking. A clear question answered with a simple "
            "spreadsheet is worth more than a beautiful dashboard that answers nothing.",
            ("h", "The Analyst's Mindset"),
            "Good analysts share a few habits. They are curious and keep asking why. They learn "
            "the context, because a number means nothing until you know how it was recorded. A "
            "dip in collections may be a real problem, or it may be a week of encoding that has "
            "not been posted yet. They are healthy skeptics who check their own results before "
            "trusting them. And they remember that behind every row there is a person.",
            "That last habit matters a great deal in government. Treasury records hold names, "
            "addresses, property details and amounts paid. In the Philippines, the Data Privacy "
            "Act of 2012 (Republic Act No. 10173) sets the rules for handling personal "
            "information. An analyst should work with the least personal data the question needs."
            " Totals by barangay, for example, rarely need anyone's name. I wrote about this in "
            "more detail in a separate post on data at the treasury counter.",
            ("h", "Where ALTOS Fits"),
            "When I built ALTOS, I kept one lesson from analytics in front of me: an answer is "
            "only as good as the records behind it. So ALTOS records each receipt and each "
            "deposit as the transaction happens, instead of copying figures later from paper. "
            "Collections can then be compared with targets by month and by revenue source, and "
            "year-end results can be forecast with an honest range rather than a single hopeful "
            "number.",
            "Just as important, every result in ALTOS is treated as a prompt for a person to "
            "decide, never as an automatic action. Data can point to where a problem might be. "
            "People still have to look, judge and act. That idea runs through this whole series.",
            ("h", "Key Takeaways"),
            ("point",
             "Data, information, insight",
             "Raw records become organized information, and information becomes insight when it "
             "points to an action."),
            ("point",
             "Analytics serves a decision",
             "If no one will decide anything with the answer, the analysis is not finished, no "
             "matter how good the chart looks."),
            ("point",
             "Four kinds of questions",
             "What happened, why, what is likely next, and what should we do. Each one rests on "
             "the one before it."),
            ("point",
             "Start with what you have",
             "Official receipts, registers and a free spreadsheet are enough to begin. The "
             "thinking matters more than the tool."),
            ("h", "Your Part 1 Exercise"),
            "Analytics is learned by doing. Before you read any further in this series, try these"
            " three small steps:",
            ("point",
             "Write down one question",
             "Pick a real question from your work that you wish you could answer with numbers. "
             "For example: Which month brings in the most collections? Or: How many days does it "
             "take for a voucher to be paid?"),
            ("point",
             "List the records that already exist",
             "Write down every logbook, register, report or file that holds part of the answer. "
             "You will probably find more than you expect."),
            ("point",
             "Name the decision",
             "Write down who would use the answer and what they would do differently. If no one "
             "would act on it, choose a better question."),
            "Keep that page. You will use it again in Part 2.",
            ("cta", "Read: Your Data at the Treasury Counter", "/blog/your-data-at-the-treasury-counter/"),
            ("cta", "Read: Why I Built ALTOS", "/blog/why-i-built-altos/"),
            ("cta",
             "Read: The ALTOS Framework, Principle 9: Evidence Before Decision",
             "/blog/altos-framework-evidence-before-decision/"),
            ("cta",
             "Try the free Python lesson: Add up a day's collections",
             "/tutorials/add-up-daily-collections/"),
            ("ask",
             "What question at your office would you most like to answer with data? Tell me, and "
             "it may become an example in this series."),
        ],
    },
]
