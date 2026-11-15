"""Business Intelligence series (Butch 2026-11-13 PH): 20 parts. Part 1 published Nov 14, 2026
(Butch: "Publish it today"); later parts follow the daily blog rotation at 9 pm PH (Butch 2026-11-14).

The series follows what Butch learned in the Google Business Intelligence certificate, retold in the
blog's own words with made-up treasury examples. It links to the Tuesday Data Analytics series for
spreadsheet formulas, pivot tables, SQL basics and chart choice instead of teaching them again.
Facts are checked privately before each part is approved; per Butch, posts show no Sources section
and no "coming next" teaser. Own category "bi" (Business Intelligence), separate from Data Analytics (Butch 2026-11-14).
Newest first, like BLOG in content.py.
"""

SERIES = "Business Intelligence Series"

BI_POSTS = [
    {
        "date": "March 1, 2027",
        "title": "Business Intelligence Series, Part 23: Blending Data, Two Sources in One Chart",
        "slug": "business-intelligence-part-23-blending-data",
        "category": "bi",
        "summary": "Some questions need numbers that live in two places. This part shows how to blend the "
                   "collections sheet with a barangay list kept by another office in Data Studio: choosing the "
                   "join key and the join type, avoiding doubled totals, and checking the result before anyone "
                   "reads it.",
        "publish_on": "2027-03-01 21:00",
        "body": [
            "The head of office looked at the collections dashboard and asked a fair question: “Poblacion "
            "brings in the most money, but it also has the most properties. Which barangay collects the most "
            "per account?”",
            "The collections were in the treasury’s Daily tab. The number of real property tax accounts in "
            "each barangay was in a list kept by the assessor’s office, in a sheet the treasury could read but "
            "did not own. The answer needed both.",
            "(As always in this series, the office, the people and the numbers are made up. No real town or "
            "taxpayer is described.)",
            "Part 22 built new measures from a single source. This part brings a second source into the same "
            "chart. By the end of this post you will know what a blend is in Data Studio, when to blend and "
            "when to copy data into the sheet instead, how to choose the join key and the join type, why a "
            "blend can double a total, and how to check a blend before anyone relies on it.",
            ("photo", "blog/bi-blending.jpg", "Blending data: match on one clean key, choose the join on "
             "purpose, keep one row per key, and check the total. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "What a Blend Is"),
            "Google’s Data Studio documentation says that blending data creates a resource called a blend, "
            "which combines information from several data sources in one view. A few facts from the "
            "documentation shape how it is used.",
            ("point", "Up to five sources", "A blend can combine up to five data sources, as up to five "
             "tables."),
            ("point", "It lives in the report", "Blends are embedded in the report where they are made. They "
             "cannot be shared with another report, although copying a report copies its blends too."),
            ("point", "It matches on equal values", "A join links rows whose fields hold equal values. The "
             "documentation says only equality is supported in the merge condition. The fields may have "
             "different names, as long as the values match."),
            ("quote", "A blend is only as good as the key that holds it together."),
            ("h", "Blend, or Copy Into the Sheet?"),
            "The same answer could be built in Google Sheets: copy the assessor’s list into a tab and look up "
            "each barangay’s account count with a formula. Both ways work. The choice depends on who owns "
            "the second source.",
            ("point", "Copy into the sheet", "When the second list rarely changes and the treasury maintains "
             "it, a lookup tab in the pipeline from Part 16 keeps everything in one place, with checks."),
            ("point", "Blend in the report", "When another office keeps the list and updates it on its own "
             "schedule, a blend reads their sheet directly. Nobody has to remember to paste a new copy."),
            "Here the assessor’s office updates its list when new tax declarations are recorded, so a blend "
            "was the better choice. The treasury asked for view access to that sheet and connected it as a "
            "second data source.",
            ("h", "Step 1: Check the Key First"),
            "The key is the field both tables share. Here it is Barangay. Before building anything, the "
            "analyst put the two barangay lists side by side.",
            ("point", "Same spelling", "The Daily tab wrote POBLACION in capitals. The assessor’s list wrote "
             "Poblacion. Since the join compares values for equality, the safest fix is to make the two lists "
             "identical. The analyst added a clean column to the treasury’s Clean tab that matched the "
             "assessor’s spelling, rather than asking the other office to change theirs."),
            ("point", "One row per key", "The documentation warns that multiple matches for the join "
             "condition can make more rows appear in the blend. If the assessor’s list held San Isidro on two "
             "rows, every San Isidro collection would be matched twice, and its total would double."),
            ("point", "Nothing missing", "Every barangay in the Daily tab should appear in the assessor’s "
             "list. One that is missing will not match, and what happens to its rows depends on the join "
             "type."),
            ("h", "Step 2: Choose the Join on Purpose"),
            "The documentation lists five join operators and a union. Three matter for this kind of question.",
            ("point", "Left outer", "Keeps every row from the left table, here the collections, and adds the "
             "matching information from the right. A barangay missing from the assessor’s list keeps its "
             "collections, with a blank account count. This is the safe default for a report on money."),
            ("point", "Inner", "Keeps only rows that match on both sides. A missing barangay disappears, and "
             "its collections vanish from the total without any warning."),
            ("point", "Cross", "Pairs every row with every other row. The documentation notes that a cross "
             "join always returns more rows than the source tables have together. It has no place in this "
             "report."),
            "Put the table you report on first, on the left, and join the reference list to it. Then a gap in "
            "the reference list shows up as a blank instead of a smaller total.",
            ("h", "Step 3: Mind the Grouping"),
            "One detail surprises people. The documentation explains that before merging, Data Studio groups "
            "and aggregates the rows in each table by that table’s dimensions. Metrics from the sources then "
            "become plain numbers in the blend, which the chart adds up again.",
            ("point", "What it means here", "If the collections table keeps both Date and Barangay as "
             "dimensions, each barangay appears once per date. The account count from the right table is then "
             "repeated on every one of those rows."),
            ("point", "The trap", "A chart that sums Accounts by barangay would then add the same count once "
             "per date. A barangay with 450 accounts and 20 collection days would show 9,000."),
            ("point", "The fix", "For a per-account measure, keep the collections table at the barangay level "
             "only, with Barangay as its dimension and Amount as its metric. Each barangay then appears once, "
             "with its total, next to its account count."),
            "The documentation also recommends adding a unique identifier to a table’s dimensions when its rows "
            "should not be grouped together. The rule underneath both cases is the same: decide what one row "
            "of each table should mean before joining.",
            ("h", "Step 4: Build It"),
            ("point", "Start the blend", "In edit mode, select the chart, and under Data source in the "
             "properties panel choose Blend data. The documentation also describes Resource, then Manage "
             "blended data, then Add blend."),
            ("point", "Add the second table", "Choose Merge another table, pick the assessor’s data source, and "
             "add Barangay and Accounts."),
            ("point", "Set the join", "Click the join box between the tables, choose Left outer, and pair "
             "Barangay with Barangay under the merge conditions. Save, and give the blend a clear name, such "
             "as “Collections with assessor accounts.”"),
            ("point", "Add the measure", "In the chart, create a field: SUM(Amount) / SUM(Accounts), the "
             "ratio of sums from Part 22. With one row per barangay, each side is summed once."),
            ("h", "Step 5: Check Before Sharing"),
            ("point", "Same total", "Put the blended chart’s total collections next to a scorecard built on "
             "the Daily tab alone, for the same dates. They must match. A larger blended total points to a "
             "duplicated key; a smaller one points to an inner join or a filter."),
            ("point", "Find the blanks", "Make a small table of barangays with a blank account count. Each "
             "row is a name that did not match, and the fix belongs in the key."),
            ("point", "One by hand", "Pick one barangay. Divide its collections by its account count on a "
             "calculator and compare with the chart."),
            ("h", "Filters and Speed"),
            ("point", "Before or after the merge", "The documentation explains that a filter set on a table "
             "inside the blend applies before the tables are merged, while a filter on the chart applies to "
             "the blended result. The two can give different answers, so decide which one you mean."),
            ("point", "Only the fields you need", "The documentation warns that blending can create very large "
             "data sets and slow charts down. Add only the fields the question needs."),
            ("h", "The Answer for the Head of Office"),
            "The first blended total came out ₱18,500 higher than the plain scorecard. The assessor’s list "
            "had San Roque on two rows, one of them an old entry from before a boundary update. The assessor’s "
            "office removed the old row, and the totals matched. The chart then showed Poblacion first in "
            "money but third in collections per account, behind two outer barangays where many owners paid in "
            "full at the start of the year. The head of office asked for that ranking in the next briefing, "
            "with the account count printed beside each bar so readers could see the base.",
            ("h", "Mistakes to Avoid"),
            ("point", "Joining on names that do not match", "Make the key identical before blending."),
            ("point", "A reference list with repeats", "One row per key, or totals double."),
            ("point", "Inner join on money", "Use left outer so missing matches show as blanks."),
            ("point", "Skipping the total check", "Compare with a scorecard built on one source."),
            ("h", "Key Takeaways"),
            ("point", "What a blend is", "Up to five sources, joined on equal values, inside one report."),
            ("point", "The key", "Same spelling, one row per key, nothing missing."),
            ("point", "The grouping", "Decide what one row of each table means before joining."),
            ("point", "The check", "The blended total must equal the single-source total."),
            ("h", "Your Part 23 Exercise"),
            "Use the practice dashboard from your Part 22 exercise.",
            ("point", "Make a reference list", "A new sheet with one row per barangay and one number, such as "
             "the number of accounts."),
            ("point", "Blend it", "Left outer, joined on the barangay, with the collections table at barangay "
             "level."),
            ("point", "Break it on purpose", "Add a repeated row to the reference list and watch the total "
             "change. Then remove it."),
            "Seeing a total double once is the best reminder to check every blend before sharing it.",
            ("cta", "Read: Business Intelligence Series, Part 22", "/blog/business-intelligence-part-22-calculated-fields/"),
            ("cta", "Read: Business Intelligence Series, Part 20", "/blog/business-intelligence-part-20-first-data-studio-dashboard/"),
            ("cta", "Read: Business Intelligence Series, Part 5", "/blog/business-intelligence-part-5-data-modeling/"),
            ("cta", "Read: Data Analytics Series, Part 14", "/blog/data-analytics-part-14-databases-101/"),
            ("ask", "Which question in your office needs numbers from two offices, and who keeps the key that joins them?"),
        ],
    },
    {
        "date": "February 24, 2027",
        "title": "Business Intelligence Series, Part 22: Calculated Fields, New Measures Without Touching the Sheet",
        "slug": "business-intelligence-part-22-calculated-fields",
        "category": "bi",
        "summary": "Calculated fields let a dashboard create new measures from the data it already has. This "
                   "part adds four to the collections dashboard in Data Studio: an area grouping, an average "
                   "per receipt, a share of total and a size label, and explains why a "
                   "formula may refuse to save.",
        "publish_on": "2027-02-24 21:00",
        "body": [
            "A week after the dashboard from Part 20 went live, the head of office had three new questions. "
            "How much does the town center bring in compared with the outer barangays? What is the average "
            "amount per receipt? And what share of the week’s total did each collector bring in?",
            "The analyst’s first thought was to add three new columns to the sheet. Then the analyst "
            "remembered that the sheet feeds other reports, and every new column is one more thing to keep "
            "in step. The answers could be worked out inside the dashboard instead.",
            "(As always in this series, the office, the people and the numbers are made up. No real town or "
            "taxpayer is described.)",
            "This part covers calculated fields in Data Studio. By the end of this post you will know what a "
            "calculated field is, the difference between one saved in the data source and one made for a single "
            "chart, how to group values with CASE, how to build a ratio that adds up correctly, how to show a "
            "share of the total, and how to read the errors that stop a formula from saving.",
            ("photo", "blog/bi-calculated-fields.jpg", "Calculated fields: group with CASE, build ratios from "
             "sums, show shares of the total, and test each new field. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "What a Calculated Field Is"),
            "Google’s Data Studio documentation describes calculated fields as formulas that create new metrics "
            "and dimensions from your data. The formula works on fields that already exist, and the result can "
            "be used in charts like any other field.",
            ("point", "A new dimension", "A new way to group rows, such as an area made from barangay names."),
            ("point", "A new metric", "A new number, such as an amount divided by a count."),
            "The sheet itself does not change. That keeps the source simple, and it keeps the definitions in "
            "one place that the dashboard’s readers can trust.",
            ("quote", "Keep the data plain and put the meaning in a field with a clear name."),
            ("h", "Two Places to Create One"),
            ("point", "In the data source", "The field is available in every report that uses that data "
             "source. The documentation notes that this needs editing rights on the data source. Use it for "
             "measures several reports share."),
            ("point", "In one chart", "A chart-specific field exists only in the chart where it is made. Report "
             "editors can create these, but the data source must allow field editing in reports. Use it for a "
             "one-time question."),
            "For a measure the head of office will ask about every week, the data source is the better home. "
            "One definition, used everywhere, cannot drift into two versions.",
            ("h", "Adding the Daily Tab’s Missing Column"),
            "The Daily tab from Part 20 has Date, Barangay, Collector and Amount. For an average per receipt, "
            "the analyst added one more column to it, Receipts, with the number of receipts behind each row. "
            "It comes from counting the receipts in the Clean tab, which the dashboard cannot do from the Daily totals alone, so it belongs in the sheet.",
            ("point", "Add the field", "Open the data source for editing, choose Add a field, then Add calculated field, give it a name, "
             "write the formula and save. The Data Studio tutorial on calculated fields walks through these "
             "steps."),
            ("h", "Field 1: Group With CASE"),
            ("point", "The formula", "Area: CASE WHEN Barangay IN (\"POBLACION\", \"SAN ISIDRO\") THEN \"Town "
             "center\" ELSE \"Outer barangays\" END"),
            ("point", "How it reads", "For each row, if the barangay is one of the two named, the area is Town "
             "center. Otherwise it is Outer barangays. The documentation notes that CASE returns the result of "
             "the first condition that is true."),
            ("point", "Always add ELSE", "Without ELSE, a row that matches none of the conditions returns NULL. "
             "A new barangay name would then fall out of both groups without anyone noticing."),
            "Write the names exactly as they appear in the data. If the Clean tab writes POBLACION in capitals, "
            "a formula that says Poblacion will not match it.",
            ("h", "Field 2: A Ratio That Adds Up"),
            "The average per receipt looks simple: amount divided by receipts. But there are two ways to "
            "write it, and only one is right for totals.",
            ("point", "Ratio of sums", "Average per receipt: SUM(Amount) / SUM(Receipts). For any group of rows, "
             "it adds up the amounts, adds up the receipts, and divides once."),
            ("point", "The trap", "Dividing on each row and then averaging those results gives a different "
             "answer. A day with 2 receipts and a day with 200 receipts would count the same."),
            ("point", "A worked check", "Day 1: ₱10,000 from 2 receipts, ₱5,000 each. Day 2: ₱200,000 from 200 "
             "receipts, ₱1,000 each. The ratio of sums is ₱210,000 ÷ 202, about ₱1,040. The average of the two "
             "daily figures is ₱3,000, nearly three times as much."),
            "The documentation shows this pattern for ratios: put the aggregation, such as SUM, inside the "
            "formula for each number, then divide. The field then works for a day, a week or a whole year.",
            ("h", "Field 3: Share of the Total"),
            "For each collector’s share of the week, no new formula is needed. Data Studio can apply a "
            "comparison calculation to a metric in a chart.",
            ("point", "How to set it", "Select the chart, open the metric’s edit option in the Setup tab, and "
             "choose Percent of total under Comparison calculation."),
            ("point", "What it divides by", "The documentation says it divides each row’s value by the column "
             "total. If a reader filters the chart to one area, the total changes with it, unless the option to "
             "ignore canvas filters in the total is turned on."),
            ("point", "Say which total", "Add a short note: “Share of collections for the dates and barangays "
             "selected.” A percentage without its base invites the wrong reading, as Part 19 explained."),
            ("h", "Field 4: A Size Label in Words"),
            ("point", "The formula", "Entry size: CASE WHEN Amount >= 20000 THEN \"Large\" WHEN Amount >= "
             "5000 THEN \"Medium\" ELSE \"Small\" END"),
            ("point", "What it labels", "Each row of the Daily tab: one day, one barangay, one collector. A "
             "table filtered to Large shows the entries worth a second look."),
            ("point", "Order matters", "CASE stops at the first true condition, so the largest threshold goes "
             "first. Reversed, every amount of ₱5,000 or more would be labeled Medium."),
            ("point", "Words, not only colors", "A label in words can be read without color, the habit from "
             "Part 18."),
            ("h", "When a Formula Will Not Save"),
            "The formula editor shows a warning and will not save a field with an error. Three rules from the documentation explain what the editor checks.",
            ("point", "Dimensions or metrics, not both", "A formula can use dimensions or metrics, but not mix "
             "them. SUM(Amount) / Barangay makes no sense, and the editor refuses it."),
            ("point", "No second aggregation", "A field that is already aggregated cannot be aggregated again. "
             "SUM of a field that is itself a SUM is refused."),
            ("point", "Names must match", "Field names in a formula must match the data source exactly. The documentation notes that a valid field name appears as a green or blue chip in the editor."),
            ("h", "Test Every New Field"),
            ("point", "Check one group by hand", "Pick one week and one collector. Work out the average per "
             "receipt in the sheet with SUMIFS and compare."),
            ("point", "Check the edges", "Filter to a barangay that is not in the CASE list and confirm it "
             "lands in Outer barangays."),
            ("point", "Write it down", "Add each field’s name, formula and meaning to the data dictionary from "
             "Part 10."),
            ("h", "The Three Questions, Answered"),
            "By Friday, the dashboard had an Area filter, an Average per receipt scorecard and a collector "
            "chart showing each share of the week. The sheet had gained one column, Receipts. The head of office "
            "noticed that the outer barangays had fewer receipts but a higher average per receipt, and asked "
            "why. The answer, larger annual payments made in one visit, became the next week’s briefing.",
            ("h", "Mistakes to Avoid"),
            ("point", "Averaging ratios", "Divide sums, not row-by-row results."),
            ("point", "CASE without ELSE", "New values fall into NULL and disappear from both groups."),
            ("point", "Wrong order in CASE", "Put the strictest condition first."),
            ("point", "Undocumented fields", "Record every formula in the data dictionary."),
            ("h", "Key Takeaways"),
            ("point", "Where to make it", "Data source for shared measures; chart-specific for one-time "
             "questions."),
            ("point", "CASE for groups", "First true condition wins; always add ELSE."),
            ("point", "Ratios", "SUM over SUM, so the field works at every level."),
            ("point", "Test and record", "Check by hand, then add it to the dictionary."),
            ("h", "Your Part 22 Exercise"),
            "Use the practice dashboard from your Part 20 exercise, and add a Receipts column to its sheet.",
            ("point", "Group", "Create an area field with CASE and an ELSE."),
            ("point", "Divide", "Create an average per receipt as SUM over SUM."),
            ("point", "Compare", "Check both against figures worked out in the sheet."),
            "Then try the wrong ratio once, averaging daily figures, and see how far it is from the right "
            "one. Seeing the gap makes the rule easy to remember.",
            ("cta", "Read: Business Intelligence Series, Part 20", "/blog/business-intelligence-part-20-first-data-studio-dashboard/"),
            ("cta", "Read: Business Intelligence Series, Part 10", "/blog/business-intelligence-part-10-keeping-bi-honest/"),
            ("cta", "Read: Business Intelligence Series, Part 19", "/blog/business-intelligence-part-19-fair-comparisons/"),
            ("cta", "Read: Data Analytics Series, Part 8", "/blog/data-analytics-part-8-metrics-and-kpis/"),
            ("ask", "Which number on your office’s reports is an average of averages?"),
        ],
    },
    {
        "date": "February 19, 2027",
        "title": "Business Intelligence Series, Part 21: Putting It Together, a Treasury BI Setup in Four Weeks",
        "slug": "business-intelligence-part-21-putting-it-together",
        "category": "bi",
        "summary": "Twenty parts covered the pieces of business intelligence one at a time. This part puts "
                   "them in order as a four-week plan for a small treasury office: from the first question to "
                   "a checked, shared dashboard and a weekly routine, with a checklist for each week.",
        "publish_on": "2027-02-19 21:00",
        "body": [
            "A colleague from another treasury office calls the analyst. “We want what you have: the "
            "dashboard, the weekly numbers, the alerts. Where do we start?”",
            "The analyst almost answers “with the dashboard,” then stops. The dashboard was the last thing "
            "built, not the first. Everything people see on it rests on work they never see: a question agreed "
            "on, a model, a pipeline, checks and rules about who sees what.",
            "(As always in this series, the office, the people and the numbers are made up. No real town or "
            "taxpayer is described.)",
            "This part gathers the earlier parts of this series into one plan, in the order the work is "
            "actually done. By the end of this post you will have a four-week plan for a first treasury BI "
            "setup, a checklist for each week, the questions to ask before calling it finished, and a routine "
            "that keeps it trustworthy afterward. Each step links back to the part that explains it.",
            ("photo", "blog/bi-four-weeks.jpg", "A first treasury BI setup in four weeks: the question, the "
             "pipeline, the dashboard, then sharing and routine. (Illustration: Butch Mahinay, aumahinay.dev)",
             "medium"),
            ("h", "Before Week 1: Keep It Small"),
            "The aim is one working setup, not a complete one. Choose one area, such as daily collections, "
            "and leave the rest for later. A small setup that people trust does more good than a large one "
            "that nobody checks.",
            ("point", "One audience", "The head of office, for example, and the questions they ask each week."),
            ("point", "One source", "The cashier’s daily export of receipts."),
            ("point", "Free tools", "Google Sheets for the pipeline and Data Studio for the dashboard, as in "
             "Parts 16 and 20."),
            ("quote", "Build the smallest thing people will trust, then let trust pay for the next step."),
            ("h", "Week 1: The Question and the Measures"),
            ("point", "Talk to the people", "Ask the head of office what decisions they make each week and "
             "what they wish they knew sooner. Part 4 explains how, and how to write the answers into a short "
             "BI brief."),
            ("point", "Pick what to watch", "Choose three to five measures, such as collections by day, by barangay, by collector and by revenue source. Part 3 "
             "describes what a treasury can watch every day."),
            ("point", "Define each measure", "Write one sentence for each: what is counted, from which field, "
             "over what period. These sentences start the data dictionary from Part 10."),
            ("point", "Decide who sees what", "Write the access line in the brief now, before any data is "
             "shared. Part 17 explains why."),
            "End of week 1: a one-page brief, signed off by the head of office, with the measures defined.",
            ("h", "Week 2: The Model and the Pipeline"),
            ("point", "Sketch the model", "One fact table of receipts, and dimension tables for dates, "
             "barangays, collectors and revenue accounts. Part 5 explains facts and dimensions, Part 14 the "
             "date table, and Part 15 how to shape the account levels."),
            ("point", "Build the pipeline", "A Raw tab where the export is pasted as it arrived, a Clean tab of "
             "formulas, and a Summary tab of totals, as in Part 16. That is the ETL pattern from Part 7 inside "
             "one file."),
            ("point", "Add the checks", "A Checks tab that compares row counts and totals, flags duplicates "
             "and unknown codes, and says READY or STOP. Part 9 explains the tests, and Part 16 builds them."),
            "End of week 2: a pipeline that turns one real week of exports into a summary, with every check "
            "passing, or failing for a reason you can explain.",
            ("h", "Week 3: The Dashboard"),
            ("point", "Connect a clean table", "Build a sharing file with only what readers may see, and "
             "connect Data Studio to it, as in Parts 17 and 20."),
            ("point", "Three pieces first", "A scorecard with a fair comparison, a trend line and a "
             "breakdown. Part 19 explains fair comparisons, and Part 8 when a report serves better than a "
             "dashboard."),
            ("point", "Let readers ask", "Add a date control and one filter. Part 13 explains how far a reader’s "
             "drill path should go."),
            ("point", "Fit the phone", "Check it on a phone, since that may be where the head of office opens "
             "it. Part 12 covers layout and speed."),
            "End of week 3: a dashboard whose numbers match the sheet, checked by someone other than the person "
            "who built it.",
            ("h", "Week 4: Sharing and the Routine"),
            ("point", "Share by name", "Viewers by name, with the credentials setting chosen on purpose, as in "
             "Part 17."),
            ("point", "Add one or two alerts", "A threshold for the measure that matters most, with an owner "
             "and a first check, as in Part 18."),
            ("point", "Brief the first reader", "Walk the head of office through it in five minutes: the answer first, "
             "the few facts behind it, and the decision needed. Part 11 gives the shape."),
            ("point", "Write it down", "The data dictionary, the owner of each piece, and a change log, as in "
             "Part 10."),
            "End of week 4: the first weekly briefing given from the dashboard, and the steps for running the "
            "pipeline written down for whoever does it next.",
            ("h", "Before Calling It Finished"),
            ("point", "Can someone else run it?", "Ask a colleague to paste next week’s export using only the "
             "written guide."),
            ("point", "Does every number have a source?", "Pick any figure on the dashboard and trace it back "
             "to the receipts."),
            ("point", "Does each reader see only what they should?", "Open it with a viewer’s account and look."),
            ("point", "Does the brief still match?", "Compare what was built with the questions from week 1. "
             "Anything built that nobody asked for can go."),
            ("h", "The Weekly Routine Afterward"),
            ("point", "Monday", "Paste the export, read the Checks tab, and fix any STOP before anyone looks at "
             "the dashboard."),
            ("point", "During the week", "Alerts go to their owners, who record what they found."),
            ("point", "Friday", "Note any change to a definition, a source or a layout in the change log."),
            ("point", "Each quarter", "Ask the readers what they use and what they ignore, and remove what "
             "nobody uses."),
            ("h", "Questions That Come Up Along the Way"),
            ("point", "Do we need a database first?", "Not for a first setup. A spreadsheet pipeline can carry "
             "one office’s daily receipts while the volume is modest. Part 6 explains what a database or a warehouse would add when "
             "that time comes."),
            ("point", "What if the export changes?", "The Checks tab should say STOP, because the row counts "
             "or the columns no longer match. Agree on the export layout with whoever makes it, and record any "
             "change in the change log."),
            ("point", "Who should build it?", "Someone who knows the data and has the time. Part 2 describes "
             "the BI roles, and in a small office one person may hold several of them."),
            ("point", "How do we know it worked?", "Go back to the brief. If the head of office makes the "
             "decisions named there sooner, or with fewer phone calls, it worked."),
            ("h", "The Other Office, Four Weeks Later"),
            "The colleague followed the plan with one change: their first audience was the revenue unit head, "
            "not the head of office. In week 2, the checks found that one collector’s receipts came from a "
            "second export nobody had mentioned. In week 4, the first briefing took six minutes, and the only "
            "question was why one barangay’s collections had dropped. That was the kind of question the "
            "dashboard was built to raise.",
            ("h", "Mistakes to Avoid"),
            ("point", "Starting with the dashboard", "Start with the question and the measures."),
            ("point", "Building for everyone at once", "One audience, one source, then grow."),
            ("point", "Skipping the checks", "A dashboard without checks can show a mistake to every reader at once."),
            ("point", "No written routine", "If only one person knows how it runs, it stops when they are away."),
            ("h", "Key Takeaways"),
            ("point", "Week 1", "Brief, measures, definitions and access."),
            ("point", "Week 2", "Model, pipeline and checks."),
            ("point", "Week 3", "A dashboard on a clean table, checked by someone else."),
            ("point", "Week 4", "Sharing, alerts, a briefing and a written routine."),
            ("h", "Your Part 21 Exercise"),
            "Plan your own four weeks on one page.",
            ("point", "Name the scope", "One audience, one source, three to five measures."),
            ("point", "Write the weekly goals", "One line for what will be finished at the end of each week."),
            ("point", "Name the checker", "Who, other than you, will test the numbers in week 3?"),
            "Then show the page to the person you are building it for, and ask one question: “If this works, "
            "what decision will you make faster?” The answer is the reason to start.",
            ("cta", "Read: Business Intelligence Series, Part 4", "/blog/business-intelligence-part-4-the-bi-brief/"),
            ("cta", "Read: Business Intelligence Series, Part 16", "/blog/business-intelligence-part-16-pipeline-in-sheets/"),
            ("cta", "Read: Business Intelligence Series, Part 20", "/blog/business-intelligence-part-20-first-data-studio-dashboard/"),
            ("cta", "Read: Business Intelligence Series, Part 10", "/blog/business-intelligence-part-10-keeping-bi-honest/"),
            ("ask", "If your office had a dashboard four weeks from now, what is the first question it should answer?"),
        ],
    },
    {
        "date": "February 14, 2027",
        "title": "Business Intelligence Series, Part 20: Your First Data Studio Dashboard, Connected to Live Data",
        "slug": "business-intelligence-part-20-first-data-studio-dashboard",
        "category": "bi",
        "summary": "A step-by-step build of a small collections dashboard in Google’s free Data Studio, "
                   "connected to a Google Sheets tab: preparing the data, connecting it, checking the fields, "
                   "adding a scorecard, a trend line, a bar chart and a date control, and sharing it safely.",
        "publish_on": "2027-02-14 21:00",
        "body": [
            "Every Monday, the analyst copies the week’s totals from the spreadsheet into a slide, saves it as "
            "a file and sends it to the head of office. By Wednesday, someone asks for the same chart for a "
            "different week, and the copying starts again.",
            "The spreadsheet already updates itself, as Part 16 set up. What is missing is a view that updates "
            "with it, that anyone allowed can open on a phone, and that lets them pick their own dates.",
            "(As always in this series, the office, the people and the numbers are made up. No real town or "
            "taxpayer is described.)",
            "This part builds that view in Data Studio, Google’s free web tool for reports and dashboards. It "
            "was called Looker Studio until April 2026, the name used in Part 17. By the end of this post you "
            "will know how to prepare a sheet for a dashboard, connect it, check its fields, add a scorecard, a "
            "trend line, a bar chart and a date control, and share the result without sharing more than you "
            "meant to.",
            ("photo", "blog/bi-data-studio.jpg", "A first dashboard: prepare the sheet, connect it, add charts "
             "and controls, then share. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Step 1: Prepare the Sheet"),
            "A dashboard can only be as tidy as the table under it. Google’s Data Studio tutorial on Sheets "
            "data sources gives a short list of rules, and they match the habits from earlier parts.",
            ("point", "A simple table", "One value per cell, field names in the first row, no merged cells, "
             "and no charts or pictures inside the data range."),
            ("point", "Complete dates", "Each date with day, month and year, formatted as a date, not as text."),
            ("point", "Long, not wide", "One row per day, barangay and collector, instead of one column per "
             "barangay. This is the one-row-per-record layout from Part 12 of the Data Analytics series."),
            ("point", "No totals rows", "Leave totals out. The tutorial advises this so Data Studio can "
             "calculate totals itself. A totals row in the sheet would be added up along with the rows it "
             "totals."),
            "For this office, the analyst adds a Daily tab to the sharing file from Part 17, brought in with "
            "IMPORTRANGE like the rest of that file. It has four columns, Date, Barangay, Collector and Amount, "
            "with small barangays combined as before. It carries no taxpayer names, so the dashboard cannot "
            "show any.",
            ("quote", "Build the dashboard on the cleanest table you have, not the one that is easiest to find."),
            ("h", "Step 2: Connect the Data"),
            ("point", "Create a data source", "Sign in to Data Studio, click Create in the top left, and choose "
             "Data source."),
            ("point", "Choose Google Sheets", "Select the Google Sheets connector, then the spreadsheet and the "
             "worksheet, here the Daily tab."),
            ("point", "Check the options", "“Use first row as headers” takes the field names from row 1. "
             "“Include hidden and filtered cells” is on by default, so rows hidden in the sheet are still "
             "counted unless you turn it off. An optional range limits the source to certain cells."),
            ("point", "Connect", "Click Connect in the upper right."),
            "Google’s help notes that Data Studio checks the sheet for changed values and new rows each time a "
            "report that uses it runs a query. When the Daily tab gains a new day, the dashboard can show it "
            "without anyone copying anything.",
            ("h", "Step 3: Check the Fields"),
            "After connecting, Data Studio lists the fields it found. Each one is either a dimension, something "
            "to group by, or a metric, something to add up or count.",
            ("point", "Date", "Its type should be a date. If it shows as text, the sheet probably holds dates "
             "typed as text. Fix the column in the sheet, as in Part 18 of the Data Analytics series, because "
             "the date settings in Step 6 need complete dates."),
            ("point", "Barangay and Collector", "Text dimensions, used to group the totals."),
            ("point", "Amount", "A number metric, added up with Sum. Check that it is not set to Average or "
             "Count by mistake."),
            ("point", "Name the source", "Click the name in the upper left and give it a clear one, such as "
             "“Collections Daily, sharing file.” Six months from now, someone will need to know where the "
             "numbers come from."),
            ("h", "Step 4: The Scorecard"),
            "Click Create report, and Data Studio opens a report with a table of the fields. Remove it, then use "
            "Add a chart in the toolbar to place the pieces one by one.",
            ("point", "One number", "A scorecard shows a summary of a single metric. Add one with Amount as its "
             "metric: total collections for the dates selected."),
            ("point", "A comparison", "In the scorecard’s setup, a comparison date range can be added, such as "
             "the previous period or the previous year. The scorecard then shows the change, as a percentage "
             "by default or as an amount if you choose that option."),
            ("point", "Fair by design", "A previous-year comparison sets this year’s dates against the same "
             "period a year before, the like-with-like comparison from Part 19. Add a text box beside it that "
             "says what is being compared, and check one figure against the sheet."),
            ("h", "Step 5: The Trend and the Breakdown"),
            ("point", "A time series", "Add a time series chart with Date as its dimension and Amount as its "
             "metric. It shows how collections change over time, with dates along the horizontal axis."),
            ("point", "Missing days", "The office does not collect on weekends, so those days have no rows. "
             "Data Studio’s default for missing data draws the line down to zero, which can look like a "
             "collapse every Saturday. The Missing data setting can show breaks in the line instead."),
            ("point", "A bar chart", "Add a bar chart with Barangay as its dimension and Amount as its metric, "
             "sorted from largest to smallest. A second bar chart by Collector, on the same page or a second "
             "page, answers the next question."),
            "Three charts are enough for a first page. Part 12 explained why a phone screen rewards fewer, "
            "clearer pieces, and Part 13 explained how to let readers dig deeper without crowding the first view.",
            ("h", "Step 6: Let Readers Choose"),
            ("point", "A date range control", "Use Add a control in the toolbar and choose Date range control. "
             "Readers can then pick any period, and the charts on the page follow it."),
            ("point", "A drop-down list", "Add a drop-down list control with Barangay as its control field, so "
             "a reader can show one barangay at a time."),
            ("point", "Set the default", "In the Properties panel, the default date range can be left on Auto or "
             "set to a custom range, fixed or rolling. Google’s help notes that the date range dimension must "
             "hold complete dates, which Step 1 already made sure of."),
            "Controls placed on a page apply to that page. Data Studio can also make a control report-level, "
            "so it stays in place and keeps its setting across every page.",
            ("h", "Step 7: Check It, Then Share It"),
            ("point", "Check one number", "Pick one week and compare the scorecard with the same total worked out "
             "in the sheet with SUMIFS, as in Part 19. If they differ, look first at hidden rows and the Amount "
             "aggregation."),
            ("point", "View it as a reader", "Switch to View mode. It shows the report as others will see it. "
             "Open it on a phone too."),
            ("point", "Share by name", "Click Share and add the people or Google Groups who need it. Choose "
             "“Can view” for readers. Only the people who maintain the report need editing rights."),
            ("point", "Mind the credentials", "As Part 17 explained, a report using the owner’s credentials "
             "shows its data to every reader. That is why this one is built on the sharing file, which holds "
             "only totals."),
            ("h", "The Monday Slide, Retired"),
            "The analyst sent the head of office one link. On Monday, the scorecard showed the week against the "
            "same week last year, the trend line showed each working day with gaps for the weekends, and the "
            "bars showed which barangays were behind. When the head of office wanted to see only Poblacion, a "
            "tap on the drop-down did it. Nobody copied a chart into a slide that week, and the analyst spent "
            "Monday morning on the question the bars raised instead.",
            ("h", "Mistakes to Avoid"),
            ("point", "Connecting to the working file", "Build on a table with only what readers may see."),
            ("point", "Dates stored as text", "Fix them in the sheet, so the date settings work as expected."),
            ("point", "Trusting the default aggregation", "Check that Amount is summed, not averaged or counted."),
            ("point", "Sharing before checking", "Match one total with the sheet before anyone else sees it."),
            ("h", "Key Takeaways"),
            ("point", "Prepare first", "A simple, long table with complete dates and no totals rows."),
            ("point", "Connect and check", "Google Sheets connector, then dimensions, metrics and their types."),
            ("point", "Three pieces", "A scorecard with a fair comparison, a trend line and a breakdown."),
            ("point", "Share with care", "View access by name, built on a table that holds only what readers "
             "may see."),
            ("h", "Your Part 20 Exercise"),
            "Make a practice sheet with made-up data: four columns, Date, Barangay, Collector and Amount, and "
            "about thirty rows.",
            ("point", "Build the page", "Connect it to Data Studio and add a scorecard, a time series and a bar "
             "chart."),
            ("point", "Add a control", "Add a date range control and pick a different week."),
            ("point", "Check it", "Compare one total in the dashboard with the same total in the sheet."),
            "Then change one amount in the sheet and look at the dashboard again. Seeing the number change "
            "without copying anything is the moment a report becomes a dashboard.",
            ("cta", "Read: Business Intelligence Series, Part 16", "/blog/business-intelligence-part-16-pipeline-in-sheets/"),
            ("cta", "Read: Business Intelligence Series, Part 17", "/blog/business-intelligence-part-17-who-sees-what/"),
            ("cta", "Read: Business Intelligence Series, Part 19", "/blog/business-intelligence-part-19-fair-comparisons/"),
            ("cta", "Read: Business Intelligence Series, Part 12", "/blog/business-intelligence-part-12-fast-and-readable-on-a-phone/"),
            ("ask", "Which report in your office is still copied into a slide by hand every week?"),
        ],
    },
    {
        "date": "February 9, 2027",
        "title": "Business Intelligence Series, Part 19: Fair Comparisons, This Month, Last Month and Last Year",
        "slug": "business-intelligence-part-19-fair-comparisons",
        "category": "bi",
        "summary": "“Down 78% from last month” can be true and still mislead. This part shows how to compare "
                   "periods fairly: the same number of days, the same season, the same working days and the "
                   "same definitions, with formulas for each and a plain way to label the result.",
        "publish_on": "2027-02-09 21:00",
        "body": [
            "On the morning of February 11, the head of office opens the dashboard and sees a red figure: "
            "February collections so far, ₱410,000, are down 78% compared with January’s ₱1,850,000.",
            "A worried meeting is called. Then the analyst points out what the chart compared: ten days of "
            "February with all thirty-one days of January, a month that includes business permit renewals. "
            "Compared with the first ten days of February last year, collections were up.",
            "The number was calculated correctly. The comparison was not fair.",
            "(As always in this series, the office, the people and the numbers are made up. No real town or "
            "taxpayer is described.)",
            "Part 14 built a date table, and Part 18 set thresholds on weekly totals. Both rely on comparing "
            "one period with another. By the end of this post you will know four questions to ask before any "
            "comparison, how to compare period-to-date figures, how to adjust for working days, the "
            "difference between percent and percentage points, and how to label a comparison so nobody "
            "misreads it.",
            ("photo", "blog/bi-comparisons.jpg", "Fair comparisons: same length, same season, same working "
             "days and same definitions. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Four Questions Before Any Comparison"),
            ("point", "Same length?", "Ten days cannot be compared with thirty-one days as if they were "
             "equal."),
            ("point", "Same season?", "Collections follow the calendar. A month with tax deadlines or permit "
             "renewals is not a fair match for a quiet month."),
            ("point", "Same working days?", "Two periods with the same dates can have a different number of "
             "weekdays and holidays."),
            ("point", "Same definitions?", "If an account was moved to a new group, or a new fee was added, "
             "last year’s figure may not be counting the same things."),
            "If the answer to any of these is no, the comparison needs an adjustment, a different choice of "
            "periods, or a note beside it.",
            ("quote", "A comparison is only as fair as the two things being compared."),
            ("h", "Period-to-Date: Compare Like With Like"),
            "When a month is not finished, compare it with the same days of another period. On February 11, "
            "that means February 1 to 10 of this year against February 1 to 10 of last year, or against "
            "January 1 to 10.",
            ("point", "In a spreadsheet", "=SUMIFS(Amount, PaidOn, \">=\"&Start, PaidOn, \"<=\"&End) adds up "
             "the amounts between two dates. Here Amount and PaidOn stand for the amount and date columns, "
             "and Start and End for the cells holding the two dates."),
            ("point", "Last year’s dates", "=EDATE(Start, -12) gives the same date twelve months earlier. "
             "Use it for both the start and the end of the comparison period."),
            ("point", "Label the dates", "Write “February 1 to 10, 2027 compared with February 1 to 10, 2026” "
             "beside the figure, not just “vs last year.”"),
            ("h", "Year-to-Date: The Longer View"),
            "A single month can swing because of one large payment or one slow week. Year-to-date figures, "
            "from January 1 to the latest date with data, smooth out some of that and show whether the year "
            "as a whole is on track.",
            ("point", "Match the dates", "January 1 to February 10, 2027 against January 1 to February 10, "
             "2026. The same SUMIFS and EDATE formulas work; only the start date changes."),
            ("point", "Compare with the target too", "If the office has an annual collection target, show how "
             "much of it has been reached so far, next to the share of the year that has passed."),
            ("point", "Check the working days again", "A longer period evens out some differences, but not "
             "all. A holiday that moved from one month to another can still shift the comparison."),
            ("h", "Same Period Last Year: Respecting the Season"),
            "Treasury collections have seasons. Business permits are renewed in January, and real property "
            "tax has quarterly installment deadlines. Comparing February with January mixes a busy "
            "month with a quieter one. Comparing February with last February keeps the season the same.",
            "In the example, the first ten days of February brought in ₱410,000. The same ten days last year "
            "brought in ₱372,000. That is an increase of about 10.2%, very different from the “down 78%” "
            "that started the meeting.",
            ("h", "Working Days: The Hidden Difference"),
            "The same dates do not always hold the same number of working days. February 1, 2027 falls on a "
            "Monday, so February 1 to 10 has eight weekdays. February 1, 2026 fell on a Sunday, so the same "
            "dates last year had seven.",
            "In this example, assume neither period had a holiday. Then the fairer measure is collections per "
            "working day.",
            ("point", "This year", "₱410,000 ÷ 8 = ₱51,250 per working day."),
            ("point", "Last year", "₱372,000 ÷ 7 = about ₱53,143 per working day."),
            ("point", "The change", "About 3.6% lower per working day, even though the total was 10.2% "
             "higher."),
            "Neither figure is wrong. They answer different questions. The total says how much came in. The "
            "per-day figure says whether the office collected faster or slower. Show both, and say which is "
            "which.",
            ("point", "Counting working days", "=NETWORKDAYS(Start, End) counts weekdays between two dates, in "
             "both Google Sheets and Excel. Add a list of holidays as the third argument to leave them out "
             "too, or use the working-day column from the date table in Part 14."),
            ("h", "Percent or Percentage Points?"),
            "When the measure is itself a percentage, there are two ways to describe a change, and they give "
            "different numbers.",
            ("point", "Percentage points", "If collection efficiency rises from 62% to 68%, it rose by 6 "
             "percentage points."),
            ("point", "Percent", "The same change is a rise of about 9.7%, because 6 is about 9.7% of 62."),
            "Both are correct, but they are not the same thing. When a rate changes, say “percentage points” "
            "for the difference, and avoid writing “6%” where readers could take it either way.",
            ("h", "Small Bases and One-Off Payments"),
            ("point", "Small bases", "A fee that went from ₱2,000 to ₱6,000 rose by 200%, but only by ₱4,000. "
             "Show the amount beside the percentage, so a large percentage of a small number does not "
             "outshine a small percentage of a large one."),
            ("point", "One-off payments", "A single large payment, such as a big business settling several "
             "years of tax at once, can make one month look unusual. Show the total with and without it, or "
             "add a note naming it."),
            ("point", "Changed definitions", "If accounts were moved between the revenue groups from Part 15, restate last "
             "year’s figures under the new grouping before comparing. Otherwise part of the change is only a "
             "change in labels."),
            ("h", "Showing a Comparison Clearly"),
            ("point", "Show both numbers", "The two amounts, then the change. A percentage alone hides the "
             "size of the money."),
            ("point", "Name both periods", "Exact dates for each side."),
            ("point", "Say what was adjusted", "“Per working day” or “excluding one large payment.”"),
            ("point", "Use words with color", "As in Part 18, write a word such as “Higher” or “Lower,” not color alone."),
            ("h", "The February Figure, Corrected"),
            "The dashboard now shows month-to-date figures against the same days last year, with the dates "
            "written out. A second line shows collections per working day. The comparison with January was "
            "removed from the main screen and kept on a separate page for those who need it, with a note that "
            "January includes permit renewals.",
            "The next morning’s figure read: “February 1 to 10: ₱410,000, up 10.2% on the same dates last "
            "year. Per working day: down 3.6%.” The meeting that followed was shorter, and it was about the "
            "right question: why each working day brought in a little less.",
            ("h", "Mistakes to Avoid"),
            ("point", "Partial against full periods", "Compare the same number of days."),
            ("point", "Ignoring the season", "Compare with the same period last year when seasons differ."),
            ("point", "Mixing percent and points", "Say which one you mean."),
            ("point", "Percentages without amounts", "Show the money beside the change."),
            ("h", "Key Takeaways"),
            ("point", "Four questions", "Same length, same season, same working days, same definitions."),
            ("point", "Period-to-date", "SUMIFS with matching dates, and EDATE for last year."),
            ("point", "Per working day", "A fairer pace measure when weekday counts differ."),
            ("point", "Label everything", "Both periods, both amounts and any adjustment."),
            ("h", "Your Part 19 Exercise"),
            "Take one comparison your office reports often, such as this month against last month.",
            ("point", "Ask the four questions", "Write down where the two periods differ."),
            ("point", "Rebuild it fairly", "Use the same days, the same season, or a per-working-day figure."),
            ("point", "Label it", "Write both dates, both amounts and the change in one sentence."),
            "Then compare the fair version with the original. If they tell different stories, the original "
            "has been answering a different question than the one people thought.",
            ("cta", "Read: Business Intelligence Series, Part 14", "/blog/business-intelligence-part-14-the-date-table/"),
            ("cta", "Read: Business Intelligence Series, Part 18", "/blog/business-intelligence-part-18-thresholds-and-alerts/"),
            ("cta", "Read: Business Intelligence Series, Part 15", "/blog/business-intelligence-part-15-star-or-snowflake/"),
            ("cta", "Read: Data Analytics Series, Part 8", "/blog/data-analytics-part-8-metrics-and-kpis/"),
            ("ask", "Which comparison in your office’s reports has never been checked for fairness?"),
        ],
    },
    {
        "date": "February 4, 2027",
        "title": "Business Intelligence Series, Part 18: Thresholds and Alerts, Letting the Dashboard Say When to Look",
        "slug": "business-intelligence-part-18-thresholds-and-alerts",
        "category": "bi",
        "summary": "A dashboard that is checked every day can still hide a problem in plain sight. This part "
                   "explains how to set thresholds that mean something, give every alert an owner and an "
                   "action, keep alerts few, and build a simple status column with conditional formatting in "
                   "Google Sheets.",
        "publish_on": "2027-02-04 21:00",
        "body": [
            "The head of office opens the collections dashboard every morning. Twelve collectors, twelve "
            "lines on a chart, totals by week. Everything looks roughly the way it looked last month.",
            "Three weeks later, a barangay captain mentions that nobody has come to collect in two sitios. "
            "The analyst checks: one collector’s weekly total had dropped by half and stayed there. It was on "
            "the chart the whole time, one thin line among twelve.",
            "The dashboard did its job of showing the numbers. What it did not do was say which number "
            "needed a person to look at it.",
            "(As always in this series, the office, the people and the numbers are made up. No real town or "
            "taxpayer is described.)",
            "Part 3 chose what to watch, and Part 16 added checks that stop bad data. This part adds "
            "thresholds: rules that point to the numbers that need attention. By the end of this post you "
            "will know four ways to set a threshold, why every alert needs an owner and an action, how to "
            "keep alerts few enough to matter, and how to build a status column in Google Sheets.",
            ("photo", "blog/bi-thresholds.jpg", "Thresholds and alerts: a clear rule, an owner, an action, and a "
             "label that does not rely on color alone. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "What a Threshold Is"),
            "A threshold is a value that, when a measure crosses it, means someone should look. It turns "
            "“the line went down a bit” into a plain question: is this below the level we agreed to act on?",
            "A threshold does not say what is wrong. It says where to start looking. A drop in one collector’s "
            "total could mean fewer payments, a missing remittance, a data error, or a collector reassigned "
            "for the week. The person who looks finds out which.",
            ("quote", "A dashboard shows the numbers. A threshold says which ones need a person."),
            ("h", "Four Ways to Set a Threshold"),
            ("point", "1. A target", "A number the office has agreed to reach, such as a monthly collection "
             "goal. Below a stated share of the target by a given date, the measure is flagged."),
            ("point", "2. The same period last year", "Collections follow the calendar, with busy months near "
             "tax deadlines. Comparing January with last January avoids flagging a normal seasonal dip."),
            ("point", "3. A normal range from recent history", "Take the lowest and highest weekly totals for "
             "each collector over, say, the last twelve weeks. A week outside that range is flagged. This "
             "needs no target, only the office’s own data."),
            ("point", "4. A rule", "Some alerts are yes or no: a collector’s remittance not recorded by the "
             "next working day, or a receipt series with a gap in its numbers."),
            "The choice depends on the measure. A target suits a total the office is responsible for. A "
            "normal range suits measures that vary from week to week for ordinary reasons. A rule suits "
            "anything that should always happen.",
            ("h", "Every Alert Needs an Owner and an Action"),
            "An alert that nobody is responsible for becomes decoration. Before adding one, write three "
            "things beside it.",
            ("point", "Who looks", "One named person or role, such as the head of the collections unit."),
            ("point", "What they check first", "For a low collector total: whether all of that collector’s "
             "receipts were entered, then whether the collector was reassigned, then the barangays covered."),
            ("point", "By when", "Within one working day, for example, so an alert does not wait for the "
             "monthly meeting."),
            "Write these in the BI brief from Part 4, next to the measure. When the dashboard changes hands, "
            "the alerts still make sense to the next person.",
            ("h", "Keeping Alerts Few Enough to Matter"),
            "If ten things are flagged every morning, people stop reading the flags. A threshold set too "
            "tight can do more harm than having none, because it teaches everyone to ignore it.",
            ("point", "Start with a few", "Two or three alerts on the measures that matter most."),
            ("point", "Count what happens", "For a month, note each alert and whether it led to an action. An "
             "alert that never leads to anything needs a wider threshold or should be removed."),
            ("point", "Review after changes", "A new collector, a new barangay assignment or a new tax rate "
             "can change what normal looks like. Adjust the threshold when the facts change."),
            ("h", "Data Alerts and Business Alerts"),
            "Part 16 built a Checks tab that shows READY or STOP. That is a data alert: it says whether the "
            "numbers can be trusted. The thresholds in this post are business alerts: they say whether "
            "something in the office needs attention.",
            "Check the data alert first. A collector’s total that drops because forty receipts were never "
            "pasted into the Raw tab is a data problem, not a collection problem. Sending a supervisor to "
            "the field to look for it wastes a day.",
            ("h", "Show It So Everyone Can Read It"),
            ("point", "Use words as well as color", "The W3C’s accessibility guidelines (WCAG, success "
             "criterion 1.4.1) say color should not be the only visual means of conveying information. Some readers have difficulty telling certain colors apart, such as red and green. A label such as “Below range” or a symbol says the same "
             "thing without color."),
            ("point", "Show the threshold itself", "Draw the target or the normal range on the chart, so "
             "readers can see how far the measure is from it."),
            ("point", "Put flagged items first", "A short list at the top of the dashboard, “Needs a look this "
             "week,” is read before anything else."),
            ("point", "Say why", "“Below its 12-week range for 3 weeks” explains more than a red dot."),
            ("h", "Building a Status Column in Google Sheets"),
            "In a weekly summary with one row per collector, four columns are enough.",
            ("point", "B: This week", "The collector’s total for the week, from the Summary tab of Part 16."),
            ("point", "C and D: Normal range", "The lowest and highest weekly totals over the last twelve "
             "weeks, with =MIN and =MAX over that collector’s past weeks."),
            ("point", "E: Status", "=IF(B2<C2, \"BELOW RANGE\", IF(B2>D2, \"ABOVE RANGE\", \"OK\")). The "
             "status is written in words, so it can be read without color."),
            ("point", "Color as a second signal", "Select the rows, then use conditional formatting with "
             "“Custom formula is” and =$E2=\"BELOW RANGE\" to shade a whole row. Google’s help gives the same "
             "kind of example, and notes that these formulas can only reference the same sheet, so keep the "
             "status column on the tab being formatted."),
            "An above-range week is worth a look too. A sudden jump can be a real windfall, or a receipt "
            "entered twice.",
            ("h", "The Collections Dashboard, With Thresholds"),
            "The office added a normal-range status for each collector’s weekly total and one rule: any "
            "remittance not recorded by the next working day. Each had an owner and a first check written in "
            "the brief. The top of the dashboard now lists only what needs a look.",
            "Two weeks later, one collector showed BELOW RANGE. The Checks tab said READY, so the data was "
            "complete. The first check found the answer in minutes: the collector had been assigned to the "
            "counter for the busy period, and two sitios had no one covering them. The office arranged "
            "another collector the same day.",
            ("h", "Mistakes to Avoid"),
            ("point", "Alerts without owners", "Name who looks, what they check and by when."),
            ("point", "Too many flags", "Start with a few, and remove any that never lead to action."),
            ("point", "Color only", "Write the status in words as well."),
            ("point", "Skipping the data check", "Confirm the numbers are complete before chasing a drop."),
            ("h", "Key Takeaways"),
            ("point", "Thresholds point", "They say where to look, not what is wrong."),
            ("point", "Four sources", "A target, last year, a normal range, or a rule."),
            ("point", "Owner and action", "Every alert needs a person, a first check and a deadline."),
            ("point", "Few and readable", "Keep alerts few, and show them in words as well as color."),
            ("h", "Your Part 18 Exercise"),
            "Pick one measure on a dashboard or report your office uses.",
            ("point", "Choose a threshold", "Decide which of the four ways fits it, and write the number."),
            ("point", "Name the owner", "Write who looks, what they check first, and by when."),
            ("point", "Build the status", "Add a status column in words, then color it as a second signal."),
            "Then look back over the last three months of that measure. Count how many times the threshold "
            "would have been crossed, and whether each time deserved a look.",
            ("cta", "Read: Business Intelligence Series, Part 3", "/blog/business-intelligence-part-3-what-to-watch/"),
            ("cta", "Read: Business Intelligence Series, Part 16", "/blog/business-intelligence-part-16-pipeline-in-sheets/"),
            ("cta", "Read: Business Intelligence Series, Part 4", "/blog/business-intelligence-part-4-the-bi-brief/"),
            ("cta", "Read: Data Analytics Series, Part 8", "/blog/data-analytics-part-8-metrics-and-kpis/"),
            ("ask", "Which number in your office would you want a dashboard to flag before anyone has to ask?"),
        ],
    },
    {
        "date": "January 30, 2027",
        "title": "Business Intelligence Series, Part 17: Who Sees What, Sharing Dashboards Without Sharing Too Much",
        "slug": "business-intelligence-part-17-who-sees-what",
        "category": "bi",
        "summary": "A dashboard link can open far more than the dashboard. This part shows how sharing settings, "
                   "separate files, report credentials and small-number rules decide who sees what, with a "
                   "treasury example and an access list you can keep up to date.",
        "publish_on": "2027-01-30 21:00",
        "body": [
            "The collections dashboard from Part 16 is working, and people have noticed. The budget officer "
            "wants the monthly totals. The heads of the revenue units want their own accounts. A staff member "
            "from the municipal council asks for “the link, so we can follow the numbers.”",
            "The analyst opens the share menu of the spreadsheet, chooses “Anyone with the link,” and starts "
            "to paste the link into the office group chat. Then the analyst stops. The link opens the whole "
            "file: the Summary tab, but also the Raw tab, with every receipt, every taxpayer’s name and every "
            "amount.",
            "Nothing had leaked yet. But one paste would have shared far more than anyone asked for.",
            "(As always in this series, the office, the people and the numbers are made up. No real town or "
            "taxpayer is described.)",
            "Part 4 put an access line in the BI brief, and Part 13 planned where each reader’s drill path "
            "stops. This part is about the settings that carry out those decisions. By the end of this post "
            "you will know how file sharing settings work, why a separate file for sharing is safer than a "
            "hidden tab, how dashboard credentials decide what readers can reach, how small numbers can "
            "reveal a person, and how to keep an access list current.",
            ("photo", "blog/bi-who-sees-what.jpg", "Who sees what: sharing settings, a separate file for "
             "sharing, report credentials and small-number rules. (Illustration: Butch Mahinay, aumahinay.dev)",
             "medium"),
            ("h", "Start With the Readers, Not the File"),
            "Before touching any setting, write down who wants to see the numbers and what each of them needs "
            "to decide. In the collections example, there are four groups.",
            ("point", "The analyst", "Works with every receipt, so needs the Raw and Clean tabs."),
            ("point", "Revenue unit heads", "Follow up accounts, so need account-level detail for their own "
             "kind of tax."),
            ("point", "The budget officer", "Plans spending from monthly totals by class of revenue. No names "
             "needed."),
            ("point", "Council staff", "Follow the overall trend. Totals by month and by kind "
             "of tax are enough."),
            "Only one of the four groups needs to see individual receipts. That single fact shapes every "
            "setting below.",
            ("quote", "Share the answer the reader needs, not the file you used to find it."),
            ("h", "How File Sharing Works in Google Drive"),
            "Google’s help for Drive describes two separate controls: the role each person gets, and the "
            "general access of the file.",
            ("point", "Viewer", "Can open the file, but cannot comment or edit."),
            ("point", "Commenter", "Can open and comment, but cannot edit."),
            ("point", "Editor", "Can open, comment and edit, and can also share the file with others."),
            ("point", "Restricted", "Only the people added by name can open the file."),
            ("point", "Anyone with the link", "Anyone who has the link can open the file without signing in. "
             "A link pasted in a group chat can be forwarded beyond it."),
            "Google’s help also notes that an owner can stop viewers and commenters from downloading, "
            "printing or copying a file. That is worth turning on for anything sensitive, but it does not "
            "stop someone from taking a photo of the screen. The safest file to share is one that holds "
            "nothing private in the first place.",
            ("h", "A Separate File for Sharing"),
            "Sharing a spreadsheet shares the whole spreadsheet. Hiding a tab does not change who can open the "
            "file, and protecting a range, as in Part 16, controls who can edit it, not who can see it.",
            "A safer pattern is to keep two files.",
            ("point", "The working file", "Raw, Clean, Summary and Checks. Restricted to the analyst and a "
             "backup person."),
            ("point", "The sharing file", "Holds only the Summary totals, brought in with IMPORTRANGE from the "
             "working file. Shared with the readers who need totals."),
            ("point", "Keep its editors few", "Google’s help for IMPORTRANGE warns that once access is "
             "granted, any editor of the destination file can pull from any part of the source file. So the "
             "sharing file should have the analyst as its only editor, and everyone else as viewers."),
            "The budget officer and council staff now open a file that simply does not contain a single name. "
            "There is nothing to hide, because nothing private is there.",
            ("h", "Dashboards: Whose Access Does the Report Use?"),
            "Dashboard tools add one more question: when a reader opens a report, whose permission is used to "
            "fetch the data? Looker Studio, Google’s free dashboard tool, offers two answers, which its help "
            "calls data credentials.",
            ("point", "Owner’s credentials", "The report uses the access of one person, such as the person who built it. "
             "Readers can see the data in the report even if they have no access to the data source itself."),
            ("point", "Viewer’s credentials", "Each reader’s own access is used. Readers who cannot open the "
             "data source cannot see its data in the report."),
            "Owner’s credentials are convenient, because readers need nothing else. That makes it important "
            "to connect such a report to the sharing file, not the working file. A report can only show what "
            "its data source contains.",
            "For the revenue unit heads, who need account detail, viewer’s credentials on a separate data "
            "source with only their kind of tax keeps the decision in one place: whoever can open that source "
            "can see that detail, and nobody else can.",
            ("h", "When a Total Points to a Person"),
            "Removing names is not always enough. A total can reveal a person when the group behind it is "
            "very small.",
            "Suppose a barangay has only two registered businesses. A dashboard that shows the business tax "
            "collected there, and a reader who knows one of the two owners, can work out roughly what the "
            "other one paid. The chart named no one, but it still told something about a person.",
            ("point", "Set a minimum group size", "Decide with your data protection officer how many records a "
             "total must include before it is shown on its own."),
            ("point", "Combine small groups", "Show barangays below that size together as “Other barangays.”"),
            ("point", "Watch filters", "A filter, as in Part 13, can shrink a large group into a small one. "
             "Check the smallest view a reader can reach, not only the default view."),
            "This follows the proportionality principle discussed in Part 6 of the Data Analytics series: "
            "show what the purpose needs, and no more.",
            ("h", "Keep an Access List"),
            "Settings drift. People transfer, retire or change roles, and a link shared for one meeting stays "
            "open for years. A short list keeps track.",
            ("point", "What it records", "Each file or report, who has access, what role, why, and the date "
             "it was given."),
            ("point", "Review it on a schedule", "Once a quarter is a reasonable start. Remove anyone who no "
             "longer needs access."),
            ("point", "Use office accounts", "As in Part 15 of the Data Analytics series, files owned by an "
             "office account stay with the office when a person leaves."),
            ("point", "Test as a reader", "Open each shared file or report while signed in as someone with "
             "the reader’s level of access, and confirm they see what they should and nothing more."),
            ("h", "The Collections Dashboard, Shared Again"),
            "The analyst never pasted that link. Instead, the office set up a sharing file holding only "
            "monthly totals by class, group and barangay, with small barangays combined. The budget officer "
            "and council staff were added to it as viewers by name. Each revenue unit head received a "
            "separate report with account detail for their own kind of tax only.",
            "The working file stayed restricted to the analyst and one backup person, and the access list "
            "went into the same folder, with its first quarterly review on the calendar.",
            ("h", "Mistakes to Avoid"),
            ("point", "“Anyone with the link” on working files", "Keep files with personal data restricted to "
             "named people."),
            ("point", "Hiding instead of separating", "A hidden tab is still in the file. Put shared numbers in "
             "a file of their own."),
            ("point", "Too many editors", "Editors can share further, and on an IMPORTRANGE file they can reach "
             "the source."),
            ("point", "Forgetting small groups", "Check whether any total describes only one or two people."),
            ("h", "Key Takeaways"),
            ("point", "Readers first", "List who needs what before choosing any setting."),
            ("point", "Separate files", "Share a file that holds only what readers need."),
            ("point", "Know the credentials", "A report using the owner’s access shows its data to every reader."),
            ("point", "Review access", "Keep a list, and check it on a schedule."),
            ("h", "Your Part 17 Exercise"),
            "Pick one file or dashboard your office shares with people outside your unit.",
            ("point", "Check its sharing", "Open the share settings and write down every person, every role and "
             "the general access."),
            ("point", "Look inside", "List every tab or data source a reader can reach, not just the one they "
             "use."),
            ("point", "Find the smallest total", "Filter to the smallest group a reader can reach and count the "
             "records behind it."),
            "Then decide what you would remove, separate or combine. Start your access list with that one file.",
            ("cta", "Read: Business Intelligence Series, Part 16", "/blog/business-intelligence-part-16-pipeline-in-sheets/"),
            ("cta", "Read: Business Intelligence Series, Part 13", "/blog/business-intelligence-part-13-filters-and-drill-down/"),
            ("cta", "Read: Business Intelligence Series, Part 4", "/blog/business-intelligence-part-4-the-bi-brief/"),
            ("cta", "Read: Data Analytics Series, Part 6", "/blog/data-analytics-part-6-data-ethics-privacy/"),
            ("ask", "Who can open your office’s most important spreadsheet today, and does each of them still need to?"),
        ],
    },
    {
        "date": "January 25, 2027",
        "title": "Business Intelligence Series, Part 16: A Small Pipeline in Google Sheets, Raw to Clean to Summary",
        "slug": "business-intelligence-part-16-pipeline-in-sheets",
        "category": "bi",
        "summary": "A pipeline does not have to start with servers or paid tools. This part builds a small, free "
                   "pipeline inside one Google Sheets file: a Raw tab that is never edited, a Clean tab of "
                   "formulas, a Summary tab built with QUERY, and a Checks tab that shows when something is off.",
        "publish_on": "2027-01-25 21:00",
        "body": [
            "Every Monday morning, the analyst opens the cashier’s export of last week’s receipts, copies it into "
            "a working sheet, deletes the extra spaces in the collector names by hand, retypes a few amounts "
            "that came in as text, and adds up the totals by barangay. Then the totals are typed into the "
            "dashboard. It takes most of the morning.",
            "One Monday, the copy misses the last forty rows. Nobody notices until the head of office asks why "
            "one barangay collected almost nothing that week.",
            "The steps were right. The problem was doing them by hand, from memory, every week.",
            "(As always in this series, the office, the people and the numbers are made up. No real town or "
            "taxpayer is described.)",
            "Part 7 explained what a pipeline does: extract, transform and load. Part 15 flattened the revenue "
            "account levels during that loading step. This part builds a small pipeline in Google Sheets, which is free to use with a Google account. By the end of this post you will know how to lay out a pipeline in one "
            "Google Sheets file, the formulas for each stage, how to add checks that catch a bad week, and when "
            "the file has outgrown the job.",
            ("photo", "blog/bi-sheets-pipeline.jpg", "A small pipeline in one spreadsheet: a Raw tab, a Clean "
             "tab, a Summary tab and a Checks tab. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Four Tabs, Four Jobs"),
            "The idea is to give each stage of the work its own tab, and to let formulas carry the data from "
            "one tab to the next. People touch only the first tab. Everything after it is calculated.",
            ("point", "Raw", "The export exactly as it arrived. Nobody types here."),
            ("point", "Clean", "Formulas that read Raw row by row and fix what needs fixing."),
            ("point", "Summary", "Formulas that total the Clean tab by barangay, collector or account."),
            ("point", "Checks", "A few cells that compare the tabs and show whether this week’s run can be "
             "trusted."),
            "A fifth tab, Lists, holds the revenue account dimension from Part 15: account code, account title, "
            "group and class. The Clean tab looks up each receipt’s account there.",
            ("quote", "Let people fill one tab. Let formulas fill the rest."),
            ("h", "Step 1: The Raw Tab"),
            "The Raw tab holds one row per receipt, with the same columns every week: receipt number, date, "
            "collector, barangay, account code and amount. This follows the one-row-per-record layout from "
            "Part 12 of the Data Analytics series.",
            ("point", "Paste as it arrived", "Paste the export into Raw without fixing anything. If it has "
             "problems, the Clean tab will deal with them, and the original stays available to compare."),
            ("point", "Or pull it in", "If the cashier keeps the receipts in another Google Sheets file, "
             "IMPORTRANGE can bring them in: =IMPORTRANGE(\"file URL\", \"Receipts!A2:F\"). Google’s help notes "
             "that the first time, you must click Allow Access to connect the two files."),
            ("point", "Same columns, same order", "If the export layout changes, every formula after it can "
             "point to the wrong column. Agree on the layout with whoever makes the export."),
            ("h", "Step 2: The Clean Tab"),
            "Each column in the Clean tab is a formula that reads the same row in Raw. Write the formula in row "
            "2, then copy it down to more rows than a busy month needs. Wrapping each formula in IF(Raw!A2=\"\",\"\", …) keeps the unused rows blank. Columns A to F keep the same order as Raw, and two new columns follow: G for the account group and H for a duplicate flag.",
            ("point", "Extra spaces", "=TRIM(Raw!C2). Google’s help says TRIM removes leading, trailing and "
             "repeated spaces, so “ Reyes  M.” becomes “Reyes M.” and groups correctly."),
            ("point", "Spaces TRIM misses", "The same help page notes that non-breaking spaces are not trimmed. "
             "They can arrive in data copied from web pages or some exports. "
             "=TRIM(SUBSTITUTE(Raw!C2,CHAR(160),\" \")) replaces them with ordinary spaces first."),
            ("point", "Amounts stored as text", "=VALUE(Raw!F2) turns text that looks like a number into a "
             "number, so it can be added up."),
            ("point", "Account levels", "=XLOOKUP(Raw!E2, Lists!A:A, Lists!C:C, \"NOT FOUND\") brings in the "
             "account’s group. The last part tells the formula what to show when the code is missing from "
             "Lists, so a gap is visible instead of silent."),
            ("point", "A duplicate flag", "=IF(COUNTIF(Raw!A:A, Raw!A2)>1, \"DUPLICATE\", \"OK\") marks any "
             "receipt number that appears more than once."),
            "Notice what the Clean tab does not do. It does not delete rows or change Raw. If a cleaning rule "
            "turns out to be wrong, you fix the formula, and every row is recalculated from the original.",
            ("h", "Step 3: The Summary Tab"),
            "The QUERY function lets a formula group and total data using a short query language. Google’s help "
            "gives its form as QUERY(data, query, headers), where headers is the number of header rows.",
            ("point", "Totals by barangay", "In cell A1 of Summary: =QUERY(Clean!A1:H, \"select D, sum(F) where F is not null group "
             "by D label sum(F) 'Total'\", 1). The letters refer to the columns of the range: D is the "
             "barangay and F the amount."),
            ("point", "Totals by group", "The same pattern with the group column gives collections by kind of tax, one level of the class, group and account path from Part 15."),
            ("point", "Why VALUE matters here", "Google’s help notes that when a column has mixed data types, "
             "QUERY uses the majority type and treats the others as empty. An amount left as text could drop "
             "out of the total without any error."),
            "Because these are formulas, the Summary tab updates when new rows arrive in Raw. Nobody retypes a "
            "total.",
            ("h", "Step 4: The Checks Tab"),
            "Part 9 set out a full test plan for a pipeline. In a spreadsheet, a few cells can carry several of those tests, so the analyst sees at a glance whether this week’s data is safe to share.",
            ("point", "Totals agree", "=SUM(Clean!F2:F) beside =SUM(Summary!B2:B). If they differ, some rows "
             "did not make it into the summary."),
            ("point", "No duplicates", "=COUNTIF(Clean!H2:H, \"DUPLICATE\") should be 0."),
            ("point", "No unknown codes", "=COUNTIF(Clean!G2:G, \"NOT FOUND\") should be 0."),
            ("point", "Rows match the export", "Write the row count the cashier reports, and compare it with "
             "=COUNTA(Raw!A2:A). This is the check that would have caught the missing forty rows."),
            "Add a cell that combines them, such as =IF(AND(…), \"READY\", \"STOP\"), and use conditional "
            "formatting to turn it green or red. The rule for the office is simple: if it says STOP, the "
            "dashboard waits.",
            ("h", "Step 5: Let the Dashboard Read the Summary"),
            "Charts in the same file, or a dashboard tool connected to it, should read from the Summary tab, "
            "not from Raw or Clean. The dashboard then shows only numbers that have passed through the "
            "cleaning formulas and the checks.",
            ("point", "One source", "If two dashboards need the same total, they read the same Summary cell."),
            ("point", "No typing", "A number typed into a dashboard by hand has skipped every check above."),
            ("h", "Protecting the Pipeline"),
            ("point", "Protect the formula tabs", "Google Sheets lets you protect a tab or a range so only "
             "chosen people can edit it. Protect Clean, Summary, Checks and Lists, and leave only Raw open to "
             "the person who pastes the export."),
            ("point", "Write a short guide", "A note at the top of Raw: what to paste, where it comes from, and "
             "what to do if Checks says STOP."),
            ("point", "Keep versions", "Before changing a formula, make a copy of the file, using the naming "
             "and version habits from Part 15 of the Data Analytics series."),
            ("point", "Mind who can see it", "Receipts carry taxpayer details. Share the file only with the "
             "people who need it, and give others who need only the totals a dashboard built on the Summary tab."),
            ("h", "Is This Really a Pipeline?"),
            "It is a small one. Raw is the extract, Clean is the transform, and Summary is the load into the "
            "shape the dashboard needs: the ETL pattern from Part 7, inside one file. It has three important parts: the original kept untouched, cleaning written down as rules, and checks before "
            "anyone sees a number.",
            "It also has limits. A spreadsheet that holds years of receipts can become slow to open and "
            "recalculate, and formulas can be broken by anyone with edit access. When the file starts to feel "
            "heavy, or several offices need the same data, it may be time for the database or warehouse "
            "options described in Part 6. The tabs you built still help: they are a written record of every "
            "cleaning rule the new system will need.",
            ("h", "The Monday Routine, Rebuilt"),
            "The analyst now pastes the export into Raw, types the cashier’s row count into Checks, and waits "
            "a moment for the formulas. The Checks tab shows READY, and the dashboard is already up to date. "
            "On the one Monday it showed STOP, the cause was a new account code missing from Lists. Adding it "
            "took two minutes, and the wrong total never reached the head of office.",
            ("h", "Mistakes to Avoid"),
            ("point", "Fixing data in Raw", "Fix it with a formula in Clean, so the original stays as it "
             "arrived."),
            ("point", "Copying values instead of formulas", "A pasted total does not update. Keep the "
             "Summary as formulas."),
            ("point", "Leaving amounts as text", "Convert them with VALUE before any QUERY totals them."),
            ("point", "Skipping the Checks tab", "A pipeline without checks moves mistakes faster."),
            ("h", "Key Takeaways"),
            ("point", "One tab per stage", "Raw, Clean, Summary and Checks, with formulas between them."),
            ("point", "Raw stays raw", "People paste; formulas clean."),
            ("point", "QUERY for totals", "Group and total the Clean tab without typing a number."),
            ("point", "Checks before sharing", "If the checks say STOP, the dashboard waits."),
            ("h", "Your Part 16 Exercise"),
            "Take one weekly or monthly report your office still totals by hand.",
            ("point", "Set up the tabs", "Make Raw, Clean, Summary and Checks in a new file, and paste one "
             "period’s export into Raw."),
            ("point", "Write three formulas", "One TRIM, one VALUE and one QUERY that totals by a column you "
             "report on."),
            ("point", "Add two checks", "Compare the totals, and count the rows against the export."),
            "Then paste the next period’s export and time how long the report takes. Compare it with the "
            "time the hand-made version took.",
            ("cta", "Read: Business Intelligence Series, Part 7", "/blog/business-intelligence-part-7-etl-or-elt/"),
            ("cta", "Read: Business Intelligence Series, Part 9", "/blog/business-intelligence-part-9-testing-the-pipeline/"),
            ("cta", "Read: Business Intelligence Series, Part 15", "/blog/business-intelligence-part-15-star-or-snowflake/"),
            ("cta", "Read: Data Analytics Series, Part 12", "/blog/data-analytics-part-12-one-row-per-record/"),
            ("ask", "Which report in your office is still totaled by hand every week?"),
        ],
    },
    {
        "date": "January 20, 2027",
        "title": "Business Intelligence Series, Part 15: Star or Snowflake? Shaping Dimensions for a Treasury Model",
        "slug": "business-intelligence-part-15-star-or-snowflake",
        "category": "bi",
        "summary": "When a dimension has levels inside it, such as revenue accounts grouped into kinds of tax, "
                   "you can keep it in one table or split it into several. This part explains star and "
                   "snowflake designs in plain words, what each costs, and how to choose for a treasury model.",
        "publish_on": "2027-01-20 21:00",
        "body": [
            "The analyst is extending the collections model from Part 5. The revenue account table has grown: "
            "each account now belongs to a group, such as real property tax or business tax, and each group "
            "belongs to a wider class, such as tax revenue or non-tax revenue.",
            "A colleague who studied databases suggests splitting it into three tables: accounts, groups and "
            "classes, each linked to the next. “That way each group name is stored only once.” Another "
            "colleague, who builds the dashboards, prefers one table with all three levels side by side. "
            "“That way the dashboard has fewer tables to join.”",
            "Both are describing real designs. The first is a snowflake. The second is a star.",
            "(As always in this series, the office, the people and the numbers are made up. No real town or "
            "taxpayer is described.)",
            "Part 14 built the date table, one of the dimensions in the model. This part looks at dimensions "
            "that have levels inside them. By the end of this post you will know what makes a design a star or "
            "a snowflake, the trade-offs of each, and a simple way to decide which one to use.",
            ("photo", "blog/bi-star-snowflake.jpg", "Star and snowflake: the same revenue account levels kept "
             "in one table, or split into a chain of linked tables. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "A Quick Reminder: Facts and Dimensions"),
            "In Part 5, the collections model had one fact table in the middle, holding the amounts, and "
            "dimension tables around it for date, collector, barangay and revenue account. Each dimension was "
            "a single table linked directly to the facts. That shape is a star schema.",
            "The question now is what to do when a dimension has its own levels. Accounts sit inside groups, "
            "and groups sit inside classes. Barangays may sit inside districts. Where should those levels "
            "live?",
            ("h", "The Snowflake: Each Level in Its Own Table"),
            "Microsoft’s Power BI guidance describes a snowflake dimension as a set of normalized tables for a "
            "single business entity. In plain words: one dimension, split into a chain of tables, one per "
            "level.",
            ("point", "Accounts table", "Account code, account title and a group code."),
            ("point", "Groups table", "Group code, group name such as “Real property tax,” and a class code."),
            ("point", "Classes table", "Class code and class name such as “Tax revenue.”"),
            "Drawn out, the chain branches away from the fact table like the arms of a snowflake, which is "
            "where the name comes from.",
            ("h", "The Star: All Levels in One Table"),
            "In a star design, the same information sits in a single, wider dimension table. Each account row "
            "carries its own group name and class name.",
            ("point", "Accounts table", "Account code, account title, group name and class name, all on one "
             "row."),
            "The group name “Real property tax” now appears on every account row in that group. That is "
            "repetition, but it is repetition inside a small dimension table, rebuilt from one source.",
            ("quote", "A snowflake saves repetition. A star saves steps."),
            ("h", "What Each Design Costs"),
            ("point", "Snowflake: less repetition", "Each group and class name is stored once. Renaming a "
             "group means changing one row."),
            ("point", "Snowflake: more steps", "Microsoft’s guidance notes that mimicking a snowflake in a "
             "Power BI model loads more tables, which is less efficient for storage and performance, and that "
             "filters must travel along longer chains of relationships."),
            ("point", "Snowflake: harder to read", "Report builders see more tables, some with only one or two "
             "columns, which the same guidance says can be a less intuitive experience."),
            ("point", "Star: simpler to use", "One table per dimension. The same guidance notes that a single "
             "table lets you build a hierarchy from the highest to the lowest level, such as class, then "
             "group, then account."),
            ("point", "Star: some repeated text", "Group and class names repeat on many rows, which can add to "
             "storage size when the dimension is large."),
            "Microsoft’s summary for Power BI is that, generally, the benefits of a single model table "
            "outweigh the benefits of multiple model tables, and that the best decision can depend on data "
            "volumes and how the model will be used.",
            ("h", "Where Each One Fits"),
            ("point", "In the source system", "The system where data is entered can keep levels in separate "
             "tables, so a group name is edited in one place. That is the database habit from Part 14 of the "
             "Data Analytics series."),
            ("point", "In the reporting model", "When the data is loaded for dashboards, the levels can be "
             "combined into one dimension table, so readers and report builders deal with fewer tables."),
            "These are not in conflict. A practical approach is to keep the source tidy and split, then "
            "flatten the dimensions during the loading step from Part 7. The pipeline does the joining once, so every "
            "dashboard does not have to.",
            ("h", "When a Separate Table Still Helps"),
            "Flattening is not always the right call, even in the reporting model.",
            ("point", "A level with its own details", "If each revenue group has its own target, owner and "
             "notes, a separate groups table can hold them without repeating them on every account row."),
            ("point", "A level shared by several dimensions", "If both accounts and budget lines use the same "
             "list of classes, one shared classes table keeps them consistent."),
            "In those cases, test both designs with the real dashboard before deciding.",
            ("h", "Flattening a Snowflake, Step by Step"),
            ("point", "1. Start with the lowest level", "Take the accounts table: one row per account."),
            ("point", "2. Bring in the next level", "Look up each account’s group code in the groups table "
             "and add the group name as a new column."),
            ("point", "3. Repeat upward", "Look up each group’s class and add the class name."),
            ("point", "4. Check the row count", "The result must have exactly as many rows as the accounts "
             "table. More rows mean a code matched twice; fewer mean a code did not match at all."),
            ("point", "5. Check for blanks", "Any blank group or class name points to an account whose code "
             "is missing from the next table. Fix the source, not the dashboard."),
            ("h", "The Collections Model, Decided"),
            "The office kept the three tables in the source spreadsheet, where the revenue unit maintains "
            "them. In the pipeline, it flattened them into one revenue account dimension with three columns: "
            "class, group and account. The dashboard gained a drill path from class to group to account, the "
            "kind of path planned in Part 13, without any extra joins in the dashboard itself.",
            ("h", "Test Before You Share"),
            ("point", "Same totals", "Collections by class, by group and by account must all add up to the "
             "same grand total."),
            ("point", "No orphans", "Every account in the fact table must appear in the dimension, with a "
             "group and a class."),
            ("point", "Rename test", "Change one group name in the source, run the pipeline, and confirm the "
             "new name appears on every account in that group."),
            ("h", "Mistakes to Avoid"),
            ("point", "Splitting everything by habit", "A level with one or two columns may not need its own "
             "table in the reporting model."),
            ("point", "Flattening without checking", "Count the rows before and after. A duplicate code can "
             "multiply rows quietly."),
            ("point", "Editing the flattened table", "Make changes in the source tables and let the pipeline "
             "rebuild the dimension."),
            ("point", "Mixing levels in one column", "Keep class, group and account in separate columns, so "
             "each can be filtered on its own."),
            ("h", "Key Takeaways"),
            ("point", "Star", "Each dimension is one table linked directly to the facts."),
            ("point", "Snowflake", "A dimension split into a chain of tables, one per level."),
            ("point", "Trade-off", "A snowflake saves repetition; a star is simpler and quicker to use."),
            ("point", "Both in their place", "Keep the source split if it helps, and flatten for reporting."),
            ("h", "Your Part 15 Exercise"),
            "Pick one dimension in your office’s data that has levels, such as revenue accounts, barangays or "
            "offices.",
            ("point", "List the levels", "Write them from the widest to the narrowest."),
            ("point", "Draw both designs", "Sketch it once as a chain of tables and once as a single table."),
            ("point", "Flatten a sample", "Take ten rows and build the single table by hand, then check the "
             "row count."),
            "Then ask the person who builds your reports which version they would rather work with, and why.",
            ("cta", "Read: Business Intelligence Series, Part 5", "/blog/business-intelligence-part-5-data-modeling/"),
            ("cta", "Read: Business Intelligence Series, Part 14", "/blog/business-intelligence-part-14-the-date-table/"),
            ("cta", "Read: Business Intelligence Series, Part 7", "/blog/business-intelligence-part-7-etl-or-elt/"),
            ("cta", "Read: Data Analytics Series, Part 14", "/blog/data-analytics-part-14-databases-101/"),
            ("ask", "Which dimension in your office’s data has levels that nobody has written down?"),
        ],
    },
    {
        "date": "January 15, 2027",
        "title": "Business Intelligence Series, Part 14: The Date Table, a Calendar Your Dashboard Can Count On",
        "slug": "business-intelligence-part-14-the-date-table",
        "category": "bi",
        "summary": "Treasury reports are organized by day, month and quarter, and dates are where a BI view "
                   "can go quietly wrong. This part explains the date table: one row per day, the columns it needs, "
                   "how to build one in a spreadsheet, and how it fixes missing days, odd sorting and unfair "
                   "comparisons.",
        "publish_on": "2027-01-15 21:00",
        "body": [
            "The analyst builds a chart of daily collections for the month. It looks fine until the head of "
            "office asks why the line jumps straight from Friday to Monday, as if the weekend never happened. "
            "Then someone sorts the monthly totals and gets April, August, December, February. And when the "
            "office compares this January with last January, nobody is sure whether both months had the same "
            "number of working days.",
            "None of these is a problem with the collections. Each one is a problem with the dates.",
            "(As always in this series, the office, the people and the numbers are made up. No real town or "
            "taxpayer is described.)",
            "Part 5 introduced facts and dimensions. This part builds a dimension that treasury "
            "models rely on: the date table. By the end of this post you will know what a date table is, which "
            "columns to put in it, how to build one in a spreadsheet, and how it fixes gaps, sorting and "
            "comparisons.",
            ("photo", "blog/bi-date-table.jpg", "A date table gives every day one row and answers the "
             "calendar questions once: which year, which month, which kind of day and which period. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "What a Date Table Is"),
            "A date table is a list with one row for every day in the period you report on, including days "
            "when nothing happened. Each row holds the date itself and facts about that date: its year, its "
            "month, its day of the week, whether the office was open.",
            "The receipts table, which Part 5 called the fact table, records what happened. The date table "
            "describes when. The two are linked by the date: each receipt’s date matches one row in the date "
            "table.",
            ("quote", "Record the calendar once, and every chart can use it."),
            ("h", "Why the Receipts Alone Are Not Enough"),
            ("point", "Missing days", "The receipts table has rows only for days with collections. A chart "
             "built from it skips weekends and holidays, which can hide the fact that nothing was collected. "
             "A date table has every day, so a day with no collections can show as zero."),
            ("point", "Sorting by name", "Month names sort alphabetically: April, August, December. A month "
             "number column keeps them in calendar order."),
            ("point", "Fair comparisons", "Two months can have different numbers of working days. Without a "
             "working day column, a month with more holidays can look like a month with weaker collections."),
            ("point", "One definition", "When every view reads its year, quarter and month from the same "
             "table, two dashboards cannot disagree about which quarter a day belongs to."),
            ("h", "The Columns a Treasury Date Table Needs"),
            ("point", "Date", "The key. One row per day, no gaps, no repeats."),
            ("point", "Year, quarter, month number, month name", "For grouping and for sorting in the right "
             "order."),
            ("point", "Day of week", "Monday to Sunday, to compare like with like."),
            ("point", "Working day", "Yes or No. No for weekends and for the days the office was closed."),
            ("point", "Holiday name", "Blank on ordinary days. The list of holidays for each year is "
             "announced by presidential proclamation, and further non-working days can be declared during the year, so "
             "this column needs updating as announcements come out."),
            ("point", "Tax period", "Which payment period the day falls in. For example, the Local Government "
             "Code allows real property tax to be paid in four installments due on or before March 31, June "
             "30, September 30 and December 31, so a column can mark which installment period each day "
             "belongs to."),
            "Add other columns only when a report needs them, such as a week number or a flag for the days of "
            "a special collection drive.",
            ("h", "Building One in a Spreadsheet"),
            "A date table can be built in Google Sheets or Excel in a few minutes.",
            ("point", "1. The dates", "Type the first date of the period, such as January 1, 2026, in the "
             "first cell under a Date header. In the next cell, add 1 to the cell above, and fill down until "
             "the last day you need."),
            ("point", "2. Year and month", "Use YEAR() and MONTH() on the date for the year and the month "
             "number."),
            ("point", "3. Month and day names", "Use TEXT() with a format such as \"mmmm\" for the month name "
             "and \"dddd\" for the day name."),
            ("point", "4. Quarter", "Divide the month number by 3 and round up: ROUNDUP(MONTH(A2)/3, 0) gives "
             "1 to 4."),
            ("point", "5. Holidays and working days", "Keep a small Holidays sheet with each holiday’s date "
             "and name. Look each date up in it, and mark a day as a working day only if it is not a weekend "
             "and not on the holidays list."),
            ("point", "6. Check it", "The number of rows should equal the number of days in the period: 365, "
             "or 366 in a leap year. No date should appear twice."),
            ("h", "Using It in a Dashboard"),
            ("point", "Link by date", "In the BI tool, connect the receipts to the date table on the date "
             "field, so each receipt picks up its year, month and working day."),
            ("point", "Group from the date table", "Build charts using the date table’s month and quarter, not "
             "fields calculated separately in each chart."),
            ("point", "Show zeros", "Where the tool allows it, include days with no receipts so the reader can "
             "see the gaps instead of a line that skips them."),
            ("point", "Compare per working day", "Divide collections by the number of working days for a fair "
             "month-to-month comparison."),
            ("h", "The January Comparison, Done Fairly"),
            "Back to the question from the start. Suppose the date table shows that this "
            "January had 19 working days and last January had 21, because of where the weekends and holidays "
            "fell. Total "
            "collections were ₱9.5 million this year against ₱10.0 million last year, which looked like a 5% "
            "drop.",
            "Per working day, the picture changes: ₱500,000 a day this year against about ₱476,000 a day last "
            "year, an increase of about 5%. The office was not collecting less. It had two fewer days to "
            "collect in. Both figures go in the report, with the working days beside them, so the reader can "
            "see why they differ.",
            ("h", "Test Before You Share"),
            ("point", "Count the rows", "One row per day, with no gaps and no repeats."),
            ("point", "Spot-check the holidays", "Pick three holidays and check that each is marked as a "
             "non-working day with the right name."),
            ("point", "Match the totals", "Total collections grouped by the date table’s months must equal the "
             "total from the receipts. If they do not, some receipts have dates outside the table."),
            ("point", "Check the sorting", "Months should appear January to December, not alphabetically."),
            ("h", "Mistakes to Avoid"),
            ("point", "Dates stored as text", "A date typed as text may not match the date table. Part 10 of "
             "the Data Analytics series shows how to spot it."),
            ("point", "A table that ends too soon", "Extend the date table before the new year starts, or "
             "January’s receipts will have nowhere to link."),
            ("point", "Holidays never updated", "Add newly declared non-working days as soon as they are "
             "announced."),
            ("point", "Each chart with its own calendar", "Calculate months and quarters once, in the date "
             "table, not in every chart."),
            ("h", "Key Takeaways"),
            ("point", "One row per day", "Including days when nothing happened."),
            ("point", "The right columns", "Year, quarter, month, day, working day, holiday and tax period."),
            ("point", "Built once, used everywhere", "Every view reads its calendar from the same table."),
            ("point", "Fair comparisons", "Compare per working day when the number of days differs."),
            ("h", "Your Part 14 Exercise"),
            "Build a date table for the current year in a spreadsheet.",
            ("point", "Fill the columns", "Date, year, quarter, month number, month name, day name and working "
             "day."),
            ("point", "Add the holidays", "List this year’s holidays on their own sheet and link them."),
            ("point", "Count", "Find how many working days each month of the year has."),
            "Then take last month’s collections and divide by its working days. Compare the result with the "
            "same month last year, worked out the same way.",
            ("cta", "Read: Business Intelligence Series, Part 5", "/blog/business-intelligence-part-5-data-modeling/"),
            ("cta", "Read: Business Intelligence Series, Part 13", "/blog/business-intelligence-part-13-filters-and-drill-down/"),
            ("cta", "Read: Business Intelligence Series, Part 9", "/blog/business-intelligence-part-9-testing-the-pipeline/"),
            ("cta", "Read: Data Analytics Series, Part 10", "/blog/data-analytics-part-10-data-types-and-table-shapes/"),
            ("ask", "How many working days did your office have last month, and does your report say so?"),
        ],
    },
    {
        "date": "January 10, 2027",
        "title": "Business Intelligence Series, Part 13: Filters and Drill-Down, Letting Readers Ask the Next Question",
        "slug": "business-intelligence-part-13-filters-and-drill-down",
        "category": "bi",
        "summary": "A good BI view answers the first question and lets the reader ask the next one. This part "
                   "explains filters and drill-down in plain words, how to choose them, how to keep them "
                   "honest, and where to stop so private details stay private.",
        "publish_on": "2027-01-10 21:00",
        "body": [
            "The head of office opens the collections view on Monday morning. Business tax collections are "
            "down 8% from the same month last year. The next question comes at once: where? Which barangays, "
            "which kinds of business, which weeks?",
            "The view has no way to answer. It shows one total and one trend line. So the head of office sends "
            "a message to the analyst, the analyst builds a new table, and the answer arrives on Wednesday. "
            "By then, the meeting where it was needed is over.",
            "(As always in this series, the office, the people and the numbers are made up. No real town or "
            "taxpayer is described.)",
            "Part 12 made the view readable on a phone. This part makes it useful for the second question. "
            "By the end of this post you will know the difference between a filter and a drill-down, how to "
            "choose the few that matter, how to keep filtered numbers honest, and where to stop drilling so "
            "private details stay private.",
            ("photo", "blog/bi-drill-down.jpg", "Drilling down from the total to the detail beneath it, one "
             "level at a time. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Two Ways to Ask the Next Question"),
            ("point", "A filter", "Narrows what the whole view shows. Choose “Barangay: San Isidro” and every "
             "chart and total on the page now counts only San Isidro. A filter answers “show me only this.”"),
            ("point", "A drill-down", "Opens the detail beneath one number. Start from the year’s total, open "
             "it into months, then open one month into days. A drill-down answers “what is inside this?”"),
            "Both let the reader move from the answer to the reason without waiting for the analyst. The "
            "difference matters when you design: a filter changes the whole page, while a drill-down follows "
            "one number down a path you have planned.",
            ("quote", "Plan for the second question before the reader has to ask it."),
            ("h", "Choosing Filters: Fewer, and the Right Ones"),
            "A view with twelve filters along the top looks powerful but can leave the reader unsure where to "
            "start. Choose filters from the questions the readers actually ask. The BI brief from Part 4 "
            "already lists them.",
            ("point", "Time", "Collections are counted by period: this month, this quarter, this year. A date "
             "filter belongs on nearly every collections view."),
            ("point", "Place", "Barangay, when collections are tracked by location."),
            ("point", "Kind", "Revenue source, such as real property tax, business tax or fees."),
            ("point", "Who", "Collector or office, for the views used to manage the work."),
            "In the example below, these four answer every question in the brief. Add a fifth only when a "
            "reader asks for it more than once.",
            ("h", "Planning a Drill Path"),
            "A drill-down follows a hierarchy, where each level sits neatly inside the one above it. Write the "
            "path down before building it.",
            ("point", "Time path", "Year, then quarter, then month, then day."),
            ("point", "Place path", "Whole municipality, then barangay, then account."),
            ("point", "Source path", "All collections, then revenue source, then the kind of fee or tax "
             "within it."),
            "Each level should add up to the one above. If the twelve months do not add up to the year, the "
            "reader has good reason to stop trusting the view. Part 5’s data model helps here: when every receipt "
            "carries a date, a barangay and a revenue source, each path can be built to add up.",
            ("h", "Keeping Filtered Numbers Honest"),
            ("point", "Show what is filtered", "Write the active filters near the top, in words: “Showing: "
             "San Isidro, business tax, October 2026.” A screenshot shared without this line can be mistaken "
             "for the whole picture."),
            ("point", "Say what a percentage is a share of", "Under a filter, “25%” can mean a share of the "
             "filtered total or a share of the whole. Label it: “25% of San Isidro’s collections” or "
             "“25% of all collections.”"),
            ("point", "Keep the date line", "The “data as of” date from earlier parts should stay visible "
             "whatever the filters are."),
            ("point", "Offer a reset", "Give the reader one clear way back to the full view, such as a "
             "“Clear filters” button or a note on how to clear them."),
            ("point", "Handle empty results", "If a combination returns nothing, say so in words: “No "
             "collections match these filters.” A blank chart can look like a broken one."),
            ("h", "Watch Out for Small Numbers"),
            "The deeper the reader drills, the smaller the numbers get, and small numbers swing easily. If a barangay had two new business "
            "permits issued last March and four this March, that is a 100% "
            "increase built on two permits.",
            ("point", "Show the count beside the percentage", "“Up 100% (from 2 to 4 permits)” tells the "
             "real story."),
            ("point", "Set a floor", "For percentage changes, consider showing “too few to compare” when the "
             "base is below a number your office agrees on."),
            ("h", "Where to Stop Drilling"),
            "Drill-down makes it easy to go from a total to a single taxpayer, and that is where privacy "
            "begins. Part 4’s BI brief asked who may see what. The drill path is where that decision is "
            "enforced.",
            ("point", "Stop at the level the reader needs", "The head of office deciding where to send "
             "collectors may need barangay totals, not taxpayer names."),
            ("point", "Give names only to those who work with them", "The revenue unit, which follows up "
             "accounts, may need account-level detail. Give them a separate view with its own access."),
            ("point", "Ask before you open the last level", "Personal information is protected under the Data "
             "Privacy Act of 2012 (Republic Act No. 10173). Check the account-level view with your office’s "
             "data protection officer before sharing it."),
            ("h", "The Collections View, With Filters and Drill-Down"),
            ("point", "Filters", "Month, revenue source and barangay, with the active filters written under "
             "the title."),
            ("point", "Drill path", "Total collections, then revenue source, then barangay. It stops there for "
             "the head of office."),
            ("point", "A second view", "For the revenue unit only: barangay, then account, for follow-up "
             "work."),
            "On Monday morning, the head of office sees business tax down 8%, opens it by barangay, and finds "
            "that most of the drop is in two barangays where two large stores closed during the year. The question "
            "that took until Wednesday now takes a minute, and the follow-up list goes to the revenue unit, "
            "whose view shows the accounts.",
            ("h", "Test Before You Share"),
            ("point", "Add it up", "Pick one filter, note the total, then check it against the same total "
             "from the source report. They must match."),
            ("point", "Walk every path", "Drill down each path to the bottom and back up. Check that each "
             "level adds up to the one above."),
            ("point", "Try odd combinations", "Choose filters that should return nothing, and check that the "
             "view says so clearly."),
            ("point", "Check the access", "Sign in as a reader who should not see account names and confirm "
             "that they cannot."),
            ("h", "Mistakes to Avoid"),
            ("point", "A filter for everything", "Too many filters can hide the few that matter."),
            ("point", "Hidden filters", "A view that does not say what is filtered can mislead anyone who "
             "sees a screenshot."),
            ("point", "Percentages of unclear wholes", "Always say what the percentage is a share of."),
            ("point", "Drilling past privacy", "Plan where each reader’s path stops before building it."),
            ("h", "Key Takeaways"),
            ("point", "Filter or drill", "A filter narrows the whole view; a drill-down opens one number."),
            ("point", "Few and chosen", "Pick filters from the questions readers actually ask."),
            ("point", "Honest under filters", "Show the active filters, label percentages and keep the date "
             "line."),
            ("point", "Stop at the right level", "Plan each reader’s drill path with privacy in mind."),
            ("h", "Your Part 13 Exercise"),
            "Take one view your office uses and write down the last three follow-up questions someone asked "
            "about it.",
            ("point", "Sort them", "For each question, decide whether a filter or a drill-down would answer it."),
            ("point", "Draw the path", "Write the drill path from the top level to the lowest level that "
             "reader needs."),
            ("point", "Mark the stop", "Draw a line at the level where names or other personal details "
             "begin, and note who may go below it."),
            "If the three questions need more than four filters, look again: some of them may belong in a "
            "drill-down instead.",
            ("cta", "Read: Business Intelligence Series, Part 12", "/blog/business-intelligence-part-12-fast-and-readable-on-a-phone/"),
            ("cta", "Read: Business Intelligence Series, Part 4", "/blog/business-intelligence-part-4-the-bi-brief/"),
            ("cta", "Read: Business Intelligence Series, Part 5", "/blog/business-intelligence-part-5-data-modeling/"),
            ("cta", "Read: Data Analytics Series, Part 6", "/blog/data-analytics-part-6-data-ethics-privacy/"),
            ("ask", "What is the follow-up question your office’s reports most often leave unanswered?"),
        ],
    },
    {
        "date": "January 5, 2027",
        "title": "Business Intelligence Series, Part 12: Fast and Readable on a Phone",
        "slug": "business-intelligence-part-12-fast-and-readable-on-a-phone",
        "category": "bi",
        "summary": "A dashboard built on a wide office monitor can be unreadable on the phone where it is "
                   "actually opened. This part shows how to design BI views for small screens and slow "
                   "connections: one column, fewer charts, bigger numbers and lighter data.",
        "publish_on": "2027-01-05 21:00",
        "body": [
            "The analyst builds the collections dashboard on a wide monitor in the office: six charts in two "
            "rows, a table of collectors on the right and four filters along the top. It looks clean. The next "
            "morning, the head of office opens it on a phone while waiting for a meeting. The charts have "
            "shrunk to the size of stamps, the table runs off the edge of the screen, and the page takes long "
            "enough to load on mobile data that the meeting starts first.",
            "The dashboard was correct and well designed for the analyst’s screen. It was not designed for "
            "the reader’s.",
            "(As always in this series, the office, the people and the numbers are made up. No real town or "
            "taxpayer is described.)",
            "Part 4 asked who reads each view and on what device. This part is about acting on the answer. "
            "By the end of this post you will know how to lay out a BI view for a phone, which charts work "
            "on a small screen, how to keep a page light enough to load quickly, and how to test it before "
            "anyone complains.",
            ("photo", "blog/bi-phone-layout.jpg", "A view built for the phone: the answer first in one column, simple charts, a light page and a real test. "
             "(Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "Start From the Reader’s Screen"),
            "Before building anything, find out where the view will be opened. Ask the readers, or look at how "
            "they open the views they already have. If the head of office reads on a phone and the cashier on "
            "a desktop, those are two different design problems.",
            "When a view will be read on both, design for the phone first. A single column stretches easily "
            "onto a wide screen, while six charts in two rows have to be rearranged to fit a phone.",
            ("quote", "Design for the screen your reader actually holds."),
            ("h", "Layout: One Column, Answer First"),
            ("point", "One column", "Stack everything in a single column so the reader scrolls down, never "
             "sideways. A reader may not notice that part of the page is hidden off to the side."),
            ("point", "The answer at the top", "Put the one number that matters most where the screen opens: "
             "for example, collections this month against target. The reader should not have to scroll to "
             "find it."),
            ("point", "Then the supporting facts", "Below the answer, add the two or three charts that explain "
             "it, in the order of the five-minute briefing from Part 11."),
            ("point", "Details last", "Tables and filters go at the bottom, for the reader who wants to dig."),
            ("h", "Charts That Survive a Small Screen"),
            ("point", "Big number tiles", "A single large figure with a short label and a comparison, such as "
             "“₱3.1M collected, 92% of target.” They stay readable on a small screen."),
            ("point", "Horizontal bars", "Bars running across the screen leave room for long labels such as "
             "barangay or account names. Vertical bars leave little room under each bar, so long labels have to be shortened or tilted."),
            ("point", "Simple lines", "A line chart with one or two lines shows a trend clearly. Five lines in "
             "five colors become hard to tell apart on a phone."),
            ("point", "Short tables", "If a table is needed, keep it to three or four columns and the top ten "
             "rows. A twelve-column table may run off a phone screen."),
            "Avoid charts that need hovering to read. A phone has no mouse, so a value shown only on hover may "
            "be hard to reach.",
            ("h", "Text and Numbers People Can Read"),
            ("point", "Size", "Make the main number large enough to read at arm’s length, and labels large "
             "enough to read without zooming. Test this on a real phone, not by shrinking a browser window."),
            ("point", "Round", "Show ₱3.1M rather than ₱3,104,226.15 on the main tile. Keep the exact figure "
             "in the table further down."),
            ("point", "Contrast", "Dark text on a light background, or the reverse. Pale gray labels may be hard to read in bright daylight."),
            ("point", "Color with a label", "Do not rely on color alone. A red bar should also say “below "
             "target,” so the meaning survives a small screen, a dim display or a reader who sees colors "
             "differently."),
            ("h", "Fast: Keeping the Page Light"),
            "A view that takes too long to load may never get read. One part of the speed is in the analyst’s "
            "control: how much data the page asks for.",
            ("point", "Summarize before the dashboard", "Build a small summary table in the pipeline, such as "
             "collections by day, account and barangay, and point the dashboard at it instead of at every "
             "receipt. The dashboard then reads far fewer rows."),
            ("point", "Fewer charts per page", "Each chart may send its own request for data. More charts can "
             "mean more waiting. Move secondary charts to a second page."),
            ("point", "Sensible default filters", "Open on this month, not on all years. Readers can widen the "
             "range if they need to."),
            ("point", "Light images", "Leave out large logos and background pictures. They add to loading "
             "time and say nothing about the numbers."),
            ("h", "The Collections Dashboard, Redesigned"),
            ("point", "Top", "One tile: collections this month and the percentage of target, with the “data as "
             "of” date beneath it."),
            ("point", "Second", "Horizontal bars: this month’s collections by revenue source, sorted from "
             "largest to smallest."),
            ("point", "Third", "A line: daily collections this month against the same days last year."),
            ("point", "Bottom", "A short table of the five accounts furthest below target, and one date "
             "filter."),
            ("point", "Second page", "The collector table and the full set of filters, for the desktop reader."),
            "On the phone, the head of office now sees the answer as soon as the page opens, and "
            "the page reads a small summary table instead of a full year of receipts.",
            ("h", "One View or Two?"),
            "Sometimes one layout cannot serve both readers well. The head of office wants one answer in "
            "the morning; the revenue unit wants every filter and every collector for a full afternoon of "
            "checking. Forcing both into one page can make it too long for the phone and too thin for the desk.",
            ("point", "Make two views", "Build a short phone view for the daily answer and a fuller desktop "
             "view for the detailed work."),
            ("point", "Use the same data", "Point both views at the same summary table, so the numbers on the "
             "phone always match the numbers on the desk."),
            ("point", "Label them clearly", "Name them for their use, such as “Daily summary (phone)” and "
             "“Collections detail (desktop),” so nobody opens the wrong one."),
            ("h", "Test Before You Share"),
            ("point", "On a real phone", "Open the view on an ordinary phone, not only on the analyst’s "
             "computer."),
            ("point", "On mobile data", "Turn off office Wi-Fi and load it again. Time how long the first "
             "number takes to appear."),
            ("point", "With a reader", "Hand the phone to someone who will use the view and ask them to find "
             "one specific number. Watch where they get stuck."),
            ("point", "In both orientations", "Check it upright and sideways. A reader may turn the phone sideways to see a chart better."),
            ("h", "Mistakes to Avoid"),
            ("point", "Designing only on the big monitor", "What fits on the analyst’s screen may not fit on "
             "the reader’s."),
            ("point", "Every chart on one page", "More charts mean more scrolling and more loading."),
            ("point", "Reading straight from raw receipts", "Summarize first, then display."),
            ("point", "Tiny text to fit more in", "If the text must shrink to fit, the page has too much on it."),
            ("h", "Key Takeaways"),
            ("point", "Phone first", "One column, the answer at the top, details at the bottom."),
            ("point", "Simple charts", "Number tiles, horizontal bars, simple lines and short tables."),
            ("point", "Light pages", "Summary tables, fewer charts per page and sensible default filters."),
            ("point", "Test for real", "On an actual phone, on mobile data, with an actual reader."),
            ("h", "Your Part 12 Exercise"),
            "Open one dashboard or report your office uses on your own phone, using mobile data.",
            ("point", "Time it", "How many seconds until the first number appears?"),
            ("point", "Find the answer", "Can you see the most important number without scrolling?"),
            ("point", "Count the problems", "List every chart, label or table that is hard to read."),
            "Then sketch a one-column version on paper, with the answer at the top. If it fits on two phone "
            "screens, you have a layout worth building.",
            ("cta", "Read: Business Intelligence Series, Part 11", "/blog/business-intelligence-part-11-five-minute-briefing/"),
            ("cta", "Read: Business Intelligence Series, Part 4", "/blog/business-intelligence-part-4-the-bi-brief/"),
            ("cta", "Read: Business Intelligence Series, Part 8", "/blog/business-intelligence-part-8-report-or-dashboard/"),
            ("cta", "Read: Data Analytics Series, Part 10", "/blog/data-analytics-part-10-data-types-and-table-shapes/"),
            ("ask", "On which screen do the readers of your office’s reports actually open them?"),
        ],
    },
    {
        "date": "December 31, 2026",
        "title": "Business Intelligence Series, Part 11: The Five-Minute Briefing for Decision Makers",
        "slug": "business-intelligence-part-11-five-minute-briefing",
        "category": "bi",
        "summary": "A dashboard is not a briefing. This part shows how to turn BI numbers into a five-minute "
                   "talk for a busy decision maker: the answer first, three supporting facts, what they mean, "
                   "and the decision you need, with a year-end treasury example.",
        "publish_on": "2026-12-31 21:00",
        "body": [
            "On the last working day of the year, the analyst gets ten minutes with the head of office to "
            "present the year’s collections. The analyst opens the dashboard and begins at the top: twelve "
            "charts, every revenue source, every month. Seven minutes in, the head of office asks, “So, are we "
            "on target or not?” The answer is on chart nine. There is no time left to discuss what to do "
            "about it.",
            "The numbers were correct and the dashboard was well built. What was missing was a briefing: a "
            "short spoken answer, shaped for one person who has to make a decision.",
            "(As always in this series, the office, the people and the numbers are made up. No real town or "
            "taxpayer is described.)",
            "Parts 8 to 10 covered how BI views are built and kept trustworthy. This part is about the moment "
            "someone has to act on them. By the end of this post you will have a five-minute structure, a way "
            "to choose the three facts that matter, a worked year-end example, and a checklist for the "
            "questions that follow.",
            ("photo", "blog/bi-five-minute-briefing.jpg", "A five-minute briefing: the answer, three facts, "
             "what they mean and the decision needed. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "A Dashboard Is Not a Briefing"),
            "A dashboard is built for exploring. It lets a reader check many things, in whatever order they choose. A briefing is built for deciding. It shows only what this reader "
            "needs today, in the order that leads to a decision.",
            "The same data can serve both. The difference is the work the analyst does before walking in: "
            "choosing, ordering and cutting.",
            ("quote", "Start with the answer. The reader can ask how you got there."),
            ("h", "The Five-Minute Structure"),
            ("point", "Minute 1: The answer", "One or two sentences that answer the question the decision "
             "maker cares about. “We collected 96% of the year’s target. Real property tax is on target; "
             "business tax fell short by ₱1.2 million.”"),
            ("point", "Minutes 2 and 3: Three facts", "The three numbers that explain the answer, each with "
             "one picture or one line. No more than three."),
            ("point", "Minute 4: What it means", "What the facts suggest, and two or three options for "
             "responding."),
            ("point", "Minute 5: The decision needed", "Exactly what you are asking for, and by when."),
            "If you finish early, stop. The remaining time belongs to the decision maker’s questions.",
            ("h", "Choosing the Three Facts"),
            "From a dashboard of twelve charts, pick the three that pass this test: if the decision maker "
            "knew only these, would they understand the answer and the choice in front of them?",
            ("point", "One fact that confirms", "Shows that the answer is true. For example: total collections "
             "against target, by month."),
            ("point", "One fact that explains", "Shows why. For example: business tax renewals in January were "
             "lower than last year."),
            ("point", "One fact that points forward", "Shows what can still change. For example: the number "
             "of businesses that have not renewed, and how much they paid last year."),
            "Everything else stays in the dashboard, ready if someone asks.",
            ("h", "The Year-End Briefing, Worked Through"),
            ("point", "The answer", "“We reached 96% of the collection target. Real property tax met its "
             "target. Business tax fell short by ₱1.2 million, and most of the gap comes from businesses that "
             "did not renew.”"),
            ("point", "Fact 1", "A single bar chart: target and actual for each of the three largest revenue "
             "sources. One bar is clearly short."),
            ("point", "Fact 2", "Business permit renewals this year compared with last year: 612 against 689."),
            ("point", "Fact 3", "Of the 77 businesses that renewed last year but not this year, 41 still "
             "appear active on the barangay clearance list. Last year they paid a combined ₱740,000."),
            ("point", "What it means", "The shortfall is concentrated and can be followed up. Options: send "
             "reminder letters to the 41, add a field visit for the largest 15, or wait for the next renewal "
             "period."),
            ("point", "Decision needed", "“I recommend letters to all 41 and visits to the largest 15 in "
             "January. I need approval for two staff for three afternoons.”"),
            "Notice that “most of the gap” in the answer is backed by fact 3. In a briefing, every word in "
            "the answer should be one the analyst can point to.",
            ("h", "Making Each Fact Easy to See"),
            ("point", "One message per picture", "Give each chart a title that states the point, such as "
             "“Business tax is the only source below target,” not “Collections by Source.”"),
            ("point", "Round the numbers", "Say ₱1.2 million, not ₱1,213,456.78. Keep the exact figure in "
             "the handout."),
            ("point", "Compare with something", "A number on its own is hard to judge. Show it against the target, "
             "last year or another period."),
            ("point", "Large enough for the room", "If you show a screen or a printout, check that the "
             "smallest label can be read from where the decision maker sits."),
            ("h", "The One-Page Handout"),
            "Bring one page the decision maker can keep. It repeats the answer, the three facts and the "
            "decision needed, with the exact numbers and the “data as of” date at the top. Add the definition "
            "of each measure in small print, from the data dictionary in Part 10.",
            "The handout is also the record. If someone asks next year what was reported on December 31, the "
            "page answers, as a static report should.",
            ("h", "Preparing for the Questions"),
            "Before the briefing, write down the three questions you would ask if you were the decision maker, "
            "and have the answer to each ready.",
            ("point", "“Are these numbers final?”", "Say what date the data is as of, and whether any receipts "
             "are still being posted."),
            ("point", "“Compared with what?”", "Have last year’s figure and the target ready for each fact."),
            ("point", "“What happens if we do nothing?”", "Have a one-sentence answer, using the same numbers."),
            "If you are asked something you cannot answer, say so and give a time when you will. A guess in "
            "a briefing can become a fact in the decision maker’s memory.",
            ("h", "Rehearse It Out Loud"),
            "A briefing that reads well on paper can still run long when spoken. Rehearse it once, with a "
            "timer.",
            ("point", "Say the first sentence from memory", "If the meeting is cut short after one minute, "
             "that sentence may be all the decision maker takes away."),
            ("point", "Ask a colleague to say “So what?”", "After each fact, a colleague asks it. If you cannot "
             "answer in one sentence, the fact is not ready, or it is not one of the three."),
            ("point", "Cut words, not the ask", "When you run over, shorten the facts. The answer and the "
             "decision needed stay."),
            "Rehearsing also catches numbers you are not sure about. If you hesitate over one while "
            "practicing, check it before the meeting.",
            ("h", "Mistakes to Avoid"),
            ("point", "Walking through the dashboard", "The order of the screen is not the order of the "
             "argument."),
            ("point", "Saving the answer for last", "If time runs out, the answer can be what gets cut."),
            ("point", "Too many facts", "Five facts in five minutes leaves little time to decide."),
            ("point", "No clear ask", "A briefing without a decision needed is only an update."),
            ("h", "Key Takeaways"),
            ("point", "Answer first", "Start with the conclusion in one or two sentences."),
            ("point", "Three facts", "One that confirms, one that explains, one that points forward."),
            ("point", "End with the decision", "Name the options and what you need, by when."),
            ("point", "Leave a page", "A one-page handout with exact numbers, definitions and the date."),
            ("h", "Your Part 11 Exercise"),
            "Pick one dashboard or report your office reviews regularly.",
            ("point", "Answer", "Write the one or two sentences that answer the question its main reader cares "
             "about most."),
            ("point", "Facts", "Choose three charts or numbers that confirm, explain and point forward."),
            ("point", "Decision", "Write what you would ask the reader to decide."),
            "Then time yourself saying it out loud. If it takes more than five minutes, cut a fact, not the "
            "answer or the decision.",
            ("cta", "Read: Business Intelligence Series, Part 10", "/blog/business-intelligence-part-10-keeping-bi-honest/"),
            ("cta", "Read: Business Intelligence Series, Part 8", "/blog/business-intelligence-part-8-report-or-dashboard/"),
            ("cta", "Read: Project Management Series, Part 10", "/blog/project-management-part-10-business-case/"),
            ("cta", "Read: Year-End in the Treasury", "/blog/year-end-in-the-treasury/"),
            ("ask", "If you had five minutes with your head of office tomorrow, what would your first sentence be?"),
        ],
    },
    {
        "date": "December 26, 2026",
        "title": "Business Intelligence Series, Part 10: Keeping BI Honest With a Data Dictionary, Owners and a Change Log",
        "slug": "business-intelligence-part-10-keeping-bi-honest",
        "category": "bi",
        "summary": "Dashboards stay trustworthy only if someone can say what each number means, who answers "
                   "for it and what changed. This part shows how to write a data dictionary, name owners and "
                   "keep a change log for a small treasury BI setup.",
        "publish_on": "2026-12-26 21:00",
        "body": [
            "In March, the head of office compares two screens. The collections dashboard says real property "
            "tax collected in February was ₱1.84 million. The revenue unit’s spreadsheet says ₱1.97 million. "
            "Both people who built them are sure they are right.",
            "After an afternoon of checking, the answer turns up. In January, someone gave interest on late "
            "real property tax its own account code. The dashboard counted only the basic tax account. The "
            "spreadsheet still counted both. Nobody had written the change down, so nobody "
            "knew to update the other view.",
            "(As always in this series, the office, the people and the numbers are made up. No real town or "
            "taxpayer is described.)",
            "Parts 7 to 9 made the pipeline reliable. This part is about keeping the meaning reliable. By the "
            "end of this post you will know how to write a data dictionary, which owners a small BI setup "
            "needs, how to keep a change log, and how these three habits work together.",
            ("photo", "blog/bi-keeping-honest.jpg", "Three habits that keep BI honest: a data dictionary that "
             "says what each field means, owners who answer for it, and a change log that records what "
             "changed. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Why Correct Data Can Still Mislead"),
            "In the opening story, no number was wrong. Each view added up its own data correctly. What "
            "differed was the meaning of “real property tax collected,” and the meaning had changed without "
            "anyone being told.",
            "Pipelines and tests protect the data. They cannot protect a definition that lives only in "
            "someone’s memory. That takes three plain documents: a dictionary, a list of owners and a log of "
            "changes.",
            ("quote", "A number is only as honest as the definition written beside it."),
            ("h", "1. The Data Dictionary"),
            "A data dictionary lists every field in your tables and says what it means. It is the reference "
            "both the dashboard builder and the reader can check.",
            ("point", "Field name", "Exactly as it appears in the table, such as “account_code.”"),
            ("point", "Plain meaning", "One or two sentences anyone in the office can understand, such as "
             "“The revenue account the receipt was credited to.”"),
            ("point", "Type and format", "Text, number, date or yes/no, and the format, such as “amount in "
             "pesos, two decimal places.”"),
            ("point", "Allowed values", "The list or range a value must come from, or where that list is "
             "kept, such as the office’s chart of revenue accounts."),
            ("point", "Source", "Which system or form the field comes from."),
            ("point", "Notes", "Anything a reader could misread. For the opening story: “Since January, "
             "interest on late real property tax has its own account code.”"),
            "Start with the fields that appear on a dashboard. A dictionary that covers the ten fields "
            "people read every day is more useful than an unfinished one that tries to cover everything.",
            ("h", "Measures Need Entries Too"),
            "A measure is built from fields, and its definition belongs in the dictionary as well. Use the "
            "five parts from Part 8 of the Data Analytics series: name, numerator, denominator, period and "
            "source.",
            ("point", "Example", "Real property tax collected: sum of amounts on official receipts for the basic "
             "tax account and the interest account, excluding cancelled "
             "receipts, by receipt date, from the collections table."),
            "With that entry on the screen, the head of office in the opening story could have seen quickly that the two views counted different accounts.",
            ("h", "2. Owners"),
            "Every important piece of a BI setup needs a person who answers for it. In a small office, one "
            "person may hold several of these roles, but each role should have a name.",
            ("point", "Data owner", "Answers for what a field or measure means and approves changes to its "
             "definition. Each office decides who this is, so write the name down."),
            ("point", "Dashboard owner", "Answers for a view: that it refreshes, that it uses the agreed "
             "definitions, and that questions about it get answered."),
            ("point", "Pipeline owner", "Answers for the nightly run, reads the run log and fixes failed "
             "tests, as in Part 9."),
            "Put each owner’s name in the dictionary beside the fields and measures they answer for, and on "
            "each dashboard beside the “data as of” date.",
            ("h", "3. The Change Log"),
            "A change log is a simple list of every change that could affect a number. Keep it in one place "
            "that every owner can open.",
            ("point", "Date", "When the change took effect, not just when it was written down."),
            ("point", "What changed", "For example: “Interest on late real property tax moved to its own "
             "account code.”"),
            ("point", "Why", "The reason or the instruction behind it."),
            ("point", "Who approved it", "The data owner’s name."),
            ("point", "Effect on numbers", "Which measures and dashboards are affected, and whether past "
             "periods were recomputed. For example: “Collections dashboard updated on January 12. Revenue "
             "unit spreadsheet must also include the new account.”"),
            "The last line is the one that would have prevented the opening story. A change is not finished "
            "until every view that uses it has been checked.",
            ("h", "How the Three Work Together"),
            "Picture a new request: the office will start recording online payments through a separate "
            "collection channel.",
            ("point", "Owner decides", "The data owner decides whether online payments count in “real property "
             "tax collected” and approves the definition."),
            ("point", "Dictionary updated", "The new field for payment channel is added, with its allowed "
             "values. The measure’s entry is updated to say that online payments are included."),
            ("point", "Log entry written", "The change, its date, its approval and every affected view are "
             "listed."),
            ("point", "Views checked", "Each dashboard owner confirms the view uses the new definition and "
             "ticks the log entry."),
            "None of these steps is technical. They are habits, and each one can take only a few minutes per change.",
            ("h", "When Two Views Disagree"),
            "The three habits also give you a calm way to settle a difference like the one in the opening "
            "story. Work through four steps before anyone argues about whose number is right.",
            ("point", "1. Compare the definitions", "Open the dictionary entry each view claims to use. If the "
             "two views count different accounts, periods or receipts, you have found the reason."),
            ("point", "2. Read the change log", "Look for any change during the period in question. A change that only one view picked up can explain a gap that appears from a certain date onward."),
            ("point", "3. Compare at the lowest level", "Total both views by account and by day. The first "
             "account or day where they differ points to the cause."),
            ("point", "4. Write down the answer", "Add a log entry that names the cause, the fix and the views "
             "that were updated, so the same question does not take another afternoon."),
            ("h", "Starting Small"),
            ("point", "Week 1", "List the fields on your most-used dashboard and write a plain meaning for each."),
            ("point", "Week 2", "Add the measures, using the five parts, and name an owner for each."),
            ("point", "Week 3", "Start the change log. Write down every change from today, and any past change "
             "you know about."),
            ("h", "Mistakes to Avoid"),
            ("point", "Definitions only in the builder’s head", "If the builder is on leave, it can be hard to find out what a number means."),
            ("point", "A dictionary nobody can find", "Link it from every dashboard."),
            ("point", "Logging the change but not its effect", "Name every view that must be checked."),
            ("point", "Owners in name only", "An owner who never reviews changes is not an owner. Ask them to "
             "approve each log entry."),
            ("h", "Key Takeaways"),
            ("point", "Meaning needs protecting too", "Correct data can still mislead when definitions drift."),
            ("point", "Write the dictionary", "Field, meaning, type, allowed values, source and notes, plus the "
             "five parts for each measure."),
            ("point", "Name the owners", "Data, dashboard and pipeline, each with a person."),
            ("point", "Log every change and its effect", "A change is done only when every affected view is "
             "checked."),
            ("h", "Your Part 10 Exercise"),
            "Pick the dashboard or report your office looks at most often.",
            ("point", "Dictionary", "Write a dictionary entry for its three most important numbers."),
            ("point", "Owners", "Write one name for each: who decides what it means?"),
            ("point", "Log", "Think back over the past year. Write down one change that affected those numbers, "
             "with its date and effect."),
            "If you could not name an owner or remember when something changed, that is the gap to close "
            "first.",
            ("cta", "Read: Business Intelligence Series, Part 9", "/blog/business-intelligence-part-9-testing-the-pipeline/"),
            ("cta", "Read: Data Analytics Series, Part 8", "/blog/data-analytics-part-8-metrics-and-kpis/"),
            ("cta", "Read: Business Intelligence Series, Part 4", "/blog/business-intelligence-part-4-the-bi-brief/"),
            ("cta", "Read: Data Analytics Series, Part 9", "/blog/data-analytics-part-9-where-data-comes-from/"),
            ("ask", "Which number in your office has changed meaning at least once without anyone writing it down?"),
        ],
    },
    {
        "date": "December 21, 2026",
        "title": "Business Intelligence Series, Part 9: Testing the Pipeline Before Anyone Sees a Number",
        "slug": "business-intelligence-part-9-testing-the-pipeline",
        "category": "bi",
        "summary": "A pipeline can run without errors and still load wrong numbers. This part gives a test plan "
                   "for a small treasury pipeline: schema, uniqueness, validity, consistency and freshness "
                   "checks, what to do when one fails, and how to test a change before it goes live.",
        "publish_on": "2026-12-21 21:00",
        "body": [
            "On Tuesday morning, the head of office opens the collections dashboard and sees that Monday’s collections were zero. The cashier is sure that was not true and remembers a "
            "busy day at the window.",
            "The pipeline had run on time. The run log showed the right number of receipts. But the week "
            "before, the counter system had been updated, and the column once called “amount” was now called "
            "“amount_paid.” The script could not find the old column, filled the amounts with zero, and "
            "carried on. Every count matched. Every peso was missing.",
            "(As always in this series, the office, the people and the numbers are made up. No real town or "
            "taxpayer is described.)",
            "Part 7 added four basic checks to the nightly pipeline: count, total, completeness and a run log. "
            "This part turns them into a full test plan. By the end of this post you will know five more kinds of tests, how to respond when a test fails, and how to try a "
            "change safely before it reaches the dashboard.",
            ("photo", "blog/bi-pipeline-tests.jpg", "Five tests a pipeline runs before anyone sees a number: "
             "schema, uniqueness, validity, consistency and freshness. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "Why a Clean Run Is Not Enough"),
            "A pipeline can fail in two ways. A loud failure stops the run with an error, so the missing data is easy to notice. A quiet failure finishes normally but loads something wrong. The opening story "
            "was a quiet failure, and those are the ones a test plan exists to catch.",
            "The rule behind every test below is simple: the pipeline should prove that the data looks right "
            "before it replaces what readers saw yesterday.",
            ("quote", "A pipeline that runs is not the same as a pipeline that is right."),
            ("h", "1. Schema Tests: Is the Shape What We Expect?"),
            "The schema is the list of columns and the kind of value each one holds. Before reading any row, "
            "the pipeline should compare what arrived with what it expects.",
            ("point", "Columns present", "Every expected column exists, with the expected name: receipt "
             "number, date, collector code, account code, barangay code and amount."),
            ("point", "Types correct", "Dates are dates, amounts are numbers, and codes are text. An amount "
             "that arrives as text, such as “1,250.00” with a comma, may be read wrongly or not at all."),
            ("point", "Stop on a mismatch", "If a column is missing or renamed, stop the run and leave "
             "yesterday’s data in place. This single test would have caught the opening story."),
            ("h", "2. Uniqueness Tests: Does Anything Appear Twice?"),
            "Official receipts are pre-numbered accountable forms, so a receipt number from the same series should "
            "never appear twice in the collections table. A duplicate is a sign that something went wrong upstream: a file copied twice, a "
            "rerun that added instead of replaced, or two collectors encoding the same receipt.",
            ("point", "What to test", "Count the rows for each series and receipt number. Any number with a count above "
             "one fails."),
            ("point", "What to do", "Set the duplicates aside on a review list and load the rest. One "
             "duplicate receipt should not hold back a day of correct ones."),
            ("h", "3. Validity Tests: Is Each Value Possible?"),
            "A value can be present and still be impossible. Validity tests set the limits of what can be "
            "true.",
            ("point", "Amounts", "Above zero for a regular receipt. A cancelled receipt is marked as "
             "cancelled, not entered as a negative amount, unless that is how your system records it."),
            ("point", "Dates", "Within the day being loaded. A receipt dated next month, or ten years ago, is "
             "a typing error until proven otherwise."),
            ("point", "Codes", "From the official list. A barangay code that is not on the barangay list fails, "
             "even if it looks close."),
            "Write each limit down with a short reason, so the next person can tell a real rule from a "
            "guess.",
            ("h", "4. Consistency Tests: Do the Tables Agree?"),
            "Consistency tests compare one part of the data with another. They catch mistakes that look fine "
            "row by row.",
            ("point", "Every code has a match", "Each collector code in the collections table exists in the "
             "collector table, and each account code exists in the account table. A receipt pointing to a "
             "code nobody knows can drop out of reports that join the two tables."),
            ("point", "Totals agree across levels", "The day’s total by collector, added up, equals the day’s "
             "total for the office. The month’s total in the warehouse equals the sum of its days."),
            ("point", "Warehouse agrees with the signed report", "Once a month’s collections report is signed, "
             "the warehouse total for that month should match it. A difference is either a correction made "
             "after signing, which should be on record, or a problem to find."),
            ("h", "5. Freshness Tests: Is the Data Current?"),
            "A dashboard can show perfectly correct numbers from three days ago. Freshness tests make sure "
            "the latest data is really the latest.",
            ("point", "Latest date", "After the nightly run, the newest receipt date should be the last working "
             "day. If it is older, a source file did not arrive."),
            ("point", "Show it", "Put the latest date on the dashboard as “data as of,” so readers can see "
             "freshness for themselves."),
            ("h", "Stop, Set Aside or Warn"),
            "Not every failure deserves the same response. Decide in advance which tests stop the run, which "
            "set rows aside and which only send a warning.",
            ("point", "Stop the run", "Schema failures and totals that do not match the source. Loading "
             "anything would make the dashboard wrong."),
            ("point", "Set rows aside", "Duplicates, impossible values and unknown codes. Load the good rows, "
             "put the rest on a review list and show how many were set aside."),
            ("point", "Warn only", "Unusual but possible results, such as a day’s total far above the daily "
             "average. Someone should look, but the numbers may be real."),
            "Whatever the response, every failure goes into the run log with the test’s name, so the person "
            "who reads it in the morning knows where to start.",
            ("h", "Testing a Change Before It Goes Live"),
            "Tests also protect you when you change the pipeline yourself, such as adding a new revenue "
            "account or a new column.",
            ("point", "Keep a test day", "Save one small, made-up day of receipts with answers you worked out "
             "by hand: the total, the count by collector and the rows that should be set aside."),
            ("point", "Run the change on the test day first", "If the new version gives the same answers, try "
             "it on a copy of the warehouse. Only then let it run on the real one."),
            ("point", "Add a test for every mistake", "When a new kind of error slips through, add a test that "
             "would have caught it. The test plan grows from experience."),
            ("h", "Mistakes to Avoid"),
            ("point", "Testing only the count", "Rows can all arrive with the wrong amounts, as the opening "
             "story shows. Test values, not just rows."),
            ("point", "Silent set-asides", "Rows set aside and never reviewed are collections missing from the reports. Show the count on the dashboard and review the list daily."),
            ("point", "Tests nobody reads", "A failed test only helps if someone sees it. Name the person who "
             "reads the run log each morning."),
            ("h", "Key Takeaways"),
            ("point", "Quiet failures are the danger", "A run that finishes can still load wrong data."),
            ("point", "Five more tests", "Schema, uniqueness, validity, consistency and freshness, on top of "
             "count, total and completeness."),
            ("point", "Decide the response in advance", "Stop, set aside or warn, and log every failure."),
            ("point", "Test changes on a known day", "Use a small test day with answers worked out by hand."),
            ("h", "Your Part 9 Exercise"),
            "Take one table your office reports from, even if it is a spreadsheet, and write a test plan for "
            "it:",
            ("point", "Schema", "List each column and the kind of value it should hold."),
            ("point", "Limits", "Write one validity rule for each column, with a reason."),
            ("point", "Response", "For each rule, decide whether a failure stops, sets aside or warns."),
            "Then run your rules by hand on last week’s data. If a rule fails on data you know is correct, the "
            "rule needs fixing. If nothing fails at all, look again at the limits.",
            ("cta", "Read: Business Intelligence Series, Part 7", "/blog/business-intelligence-part-7-etl-or-elt/"),
            ("cta", "Read: Business Intelligence Series, Part 8", "/blog/business-intelligence-part-8-report-or-dashboard/"),
            ("cta", "Read: Business Intelligence Series, Part 5", "/blog/business-intelligence-part-5-data-modeling/"),
            ("cta", "Read: Data Analytics Series, Part 8", "/blog/data-analytics-part-8-metrics-and-kpis/"),
            ("ask", "What is the quietest data mistake your office has ever found, and how long did it hide?"),
        ],
    },
    {
        "date": "December 16, 2026",
        "title": "Business Intelligence Series, Part 8: Report or Dashboard? Static, Live and Self-Service Views",
        "slug": "business-intelligence-part-8-report-or-dashboard",
        "category": "bi",
        "summary": "Not every question needs a live dashboard. This part explains the three kinds of BI views, "
                   "static reports, live dashboards and self-service views, with a treasury example of each, "
                   "and a simple test for choosing the right one.",
        "publish_on": "2026-12-16 21:00",
        "body": [
            "The head of office asks for “a dashboard for the year-end report.” The analyst spends two weeks "
            "building a live screen with filters, date pickers and twelve charts. On the day of the meeting, "
            "the head of office prints one page of it, signs it and files it. Nobody opens the dashboard "
            "again.",
            "The work was good. The format was wrong. A year-end report is a record that must stay exactly "
            "as it was signed. A live dashboard is built to change every time the data does. Choosing between them is a decision worth making at the start of a BI request, and it can go wrong when everything is called “a dashboard.”",
            "(As always in this series, the office, the people and the numbers are made up. No real town or "
            "taxpayer is described.)",
            "Parts 6 and 7 built the warehouse and the pipeline that fills it. This part is about the views "
            "people actually look at. By the end of this post you will know the three kinds of BI views, what "
            "each one is for, how to choose between them, and how often each should refresh.",
            ("photo", "blog/bi-three-views.jpg", "Three kinds of BI views: a static report fixed at a point in "
             "time, a live dashboard that refreshes on a schedule, and a self-service view that readers can "
             "filter themselves. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "1. The Static Report: A Snapshot You Can Sign"),
            "A static report shows data as of one moment and never changes after that. The monthly report of "
            "collections, the year-end summary and anything submitted to another office belong here.",
            ("point", "Use it when", "The numbers must be signed, filed, audited or compared later exactly "
             "as they were. If someone asks next year what the office reported in December, the answer must "
             "be the same."),
            ("point", "Make it trustworthy", "Print the “data as of” date and time on every page, name the "
             "source, and keep the file. A static report without a date is a guess about when it was true."),
            ("h", "2. The Live Dashboard: Watching What Is Happening"),
            "A live dashboard reads from the warehouse on a schedule and shows the current state of things. "
            "It is built for monitoring: the daily measures from Part 3, such as collections against target, "
            "undeposited cash and forms in stock.",
            ("point", "Use it when", "Someone needs to check the same few numbers often and act when one "
             "crosses a limit."),
            ("point", "Keep it small", "Aim for a short list of always-on questions that fit on one screen. Everything else belongs in a report or a self-service view."),
            "“Live” does not have to mean “every second.” It means “as fresh as the decision needs.” Data Studio, "
            "Google’s free report builder, refreshes data from Google Sheets every 15 minutes by default, and "
            "the report editor can change that to every hour, every 4 hours or every 12 hours. For a treasury "
            "dashboard fed by a nightly pipeline, a refresh after the pipeline runs is fresh enough.",
            ("h", "3. The Self-Service View: Letting Readers Ask"),
            "A self-service view gives readers the controls: filters for barangay, collector, account and "
            "date, so they can answer their own follow-up questions without asking the analyst each time.",
            ("point", "Use it when", "Different readers keep asking variations of the same question, such as "
             "collections by barangay for different months."),
            ("point", "Set the limits", "Self-service works on top of a clean, well-defined model, like the "
             "star from Part 5. It also needs access rules, so each reader can filter only the data they are "
             "allowed to see."),
            ("quote", "A report records. A dashboard watches. A self-service view answers the next question."),
            ("h", "A Simple Test for Choosing"),
            "Ask three questions about the request.",
            ("point", "Must the numbers stay fixed?", "If yes, it is a static report, even if it is built "
             "from the same data as a dashboard."),
            ("point", "Will someone check it often and act on it?", "If yes, it is a live dashboard. Keep it "
             "to the few measures that lead to action."),
            ("point", "Do readers keep asking follow-up questions?", "If yes, add a self-service view with "
             "filters, built on the same model."),
            "A request can need two of the three. The year-end meeting needed a static report. The weekly "
            "check on arrears might need a live dashboard. The revenue unit’s questions about each barangay "
            "might need a self-service view. They can all read from the same warehouse.",
            ("h", "The Treasury Year, Three Ways"),
            ("point", "Static", "The monthly report of collections and deposits, signed and filed. The "
             "year-end collection summary. Reports submitted to other offices."),
            ("point", "Live", "Collections today against the daily average, undeposited collections, "
             "official receipts left with each collector, and business permit renewals during January."),
            ("point", "Self-service", "Collections by barangay, account and month, with filters, for the "
             "revenue unit and the head of office."),
            ("h", "Refresh Rules That Match the Decision"),
            "Each view needs a refresh rule written down, so nobody wonders whether the numbers are current.",
            ("point", "Static", "Never refreshes. Produce a new edition instead, with a new date."),
            ("point", "Live", "Refreshes after each pipeline run. Show the “data as of” time at the top of the "
             "screen."),
            ("point", "Self-service", "Same as live, plus a note on the earliest and latest dates included."),
            "In Data Studio, viewers can also refresh a report themselves, but only if the editor turns on "
            "the setting that allows it. Decide this on purpose: allowing it helps impatient readers, but it "
            "does not make the warehouse any fresher than the last pipeline run.",
            ("h", "One Number, Three Places"),
            "Suppose November collections appear in all three views. The monthly report was signed on "
            "December 3 and shows ₱4,210,000. On December 5, a cancelled receipt from November 28 is corrected "
            "in the collection system. After the next pipeline run, the live dashboard and the self-service "
            "view show ₱4,195,000.",
            "Nothing is broken. The signed report is correct as of December 3, and the other two are correct "
            "as of the latest run. Trouble starts only when a reader sees both numbers without their dates "
            "and concludes that one of them is wrong.",
            ("point", "Label every number with its date", "“November collections, as of December 3” and "
             "“November collections, as of December 6” can sit side by side without confusing anyone."),
            ("point", "Record corrections after signing", "When a signed report changes after the fact, note the "
             "correction in the next edition rather than editing the old file."),
            ("h", "Write Each View Down in One Line"),
            "Before building any view, write one line that answers six questions: what is it for, who reads "
            "it, which kind is it, how often does it refresh, who owns it, and where is its date shown. For "
            "example: “Undeposited collections, for the cashier and head of office, live, refreshed after the "
            "nightly run, owned by the cashier, date at the top.”",
            "Keep these lines together in one list. When someone asks for a new dashboard, the list shows "
            "whether an existing view already answers the question, and the one-line format makes the "
            "request specific enough to build.",
            ("h", "Mistakes to Avoid"),
            ("point", "Live screens for signed reports", "If a number appears in a signed document, the "
             "document must keep its own copy. A dashboard may show a different number tomorrow."),
            ("point", "Dashboards with no owner", "Every live view needs someone who checks that it "
             "refreshed and who answers questions about it."),
            ("point", "Self-service without definitions", "Filters invite comparisons. If readers do not know how each measure is defined, they may compare the wrong things. Put the definitions from the "
             "BI brief in Part 4 on the screen."),
            ("point", "No date on the screen", "Every view, of every kind, should say when its data was "
             "current."),
            ("h", "Key Takeaways"),
            ("point", "Three kinds of views", "Static reports record, live dashboards watch, and "
             "self-service views answer follow-up questions."),
            ("point", "Fixed numbers need a static report", "Anything signed or filed must not change after "
             "the fact."),
            ("point", "Fresh enough, not fastest", "Refresh to match the decision, and show the “data as of” "
             "time."),
            ("point", "One model, many views", "All three can read from the same warehouse and the same "
             "definitions."),
            ("h", "Your Part 8 Exercise"),
            "List every regular report and screen your office uses, and label each one:",
            ("point", "Static, live or self-service?", "Which kind is it today?"),
            ("point", "Which should it be?", "Run the three-question test above."),
            ("point", "Does it show a date?", "If not, add one this week."),
            "Any view where today’s label and the right label differ is the next thing worth fixing.",
            ("cta", "Read: Business Intelligence Series, Part 7", "/blog/business-intelligence-part-7-etl-or-elt/"),
            ("cta", "Read: Business Intelligence Series, Part 3", "/blog/business-intelligence-part-3-what-to-watch/"),
            ("cta", "Read: Data Analytics Series, Part 5", "/blog/data-analytics-part-5-zero-budget-toolkit/"),
            ("cta", "Read: Year-End in the Treasury", "/blog/year-end-in-the-treasury/"),
            ("ask", "Which report in your office is called a dashboard but is really a signed snapshot?"),
        ],
    },
    {
        "date": "December 11, 2026",
        "title": "Business Intelligence Series, Part 7: ETL or ELT? Moving Data From the Counter to the Report",
        "slug": "business-intelligence-part-7-etl-or-elt",
        "category": "bi",
        "summary": "Data has to travel from the system that records it to the warehouse that reports on it. "
                   "This part explains the two ways to make that trip, ETL and ELT, with a worked treasury "
                   "example of each, and a checklist for deciding which fits your office.",
        "publish_on": "2026-12-11 21:00",
        "body": [
            "Every evening, the analyst downloads the day’s collections from the counter system, opens the "
            "file, fixes the date format, replaces barangay names with codes, deletes the cancelled receipts "
            "and pastes the result into the warehouse workbook. It takes forty minutes. On the night she is "
            "on leave, nobody does it, and the next morning’s dashboard shows a day with no collections.",
            "Every step she does by hand has a name. Together they are a data pipeline, and the order in "
            "which they happen has a name too. Getting that order right, and making it run without her, is "
            "what this part is about.",
            "(As always in this series, the office, the people and the numbers are made up. No real town or "
            "taxpayer is described.)",
            "Part 6 introduced the nightly copy from the working database to the warehouse. By the end of this "
            "post you will know the two main patterns for that copy, ETL and ELT, what each does well, which "
            "one suits a small treasury, and the checks every pipeline needs whichever pattern you choose.",
            ("photo", "blog/bi-etl-elt.jpg", "Two orders for the same three steps: ETL transforms data before "
             "loading it, while ELT loads raw data first and transforms it inside the warehouse. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Three Steps, Two Orders"),
            "Both patterns use the same three steps.",
            ("point", "Extract", "Read data out of the system where it was recorded, without changing the "
             "source."),
            ("point", "Transform", "Clean and reshape it: fix formats, turn names into codes, remove "
             "duplicates, apply business rules such as leaving out cancelled receipts."),
            ("point", "Load", "Write it into the warehouse, where reports will read it."),
            "The difference is only where the transform step sits.",
            ("h", "ETL: Clean First, Then Load"),
            "In ETL, data is extracted, transformed on the way, and only then loaded. The warehouse receives "
            "data that is already clean and in its final shape. AWS describes ETL as the older of the two "
            "approaches, in use since the 1970s, and tied to the rise of data warehouses.",
            "The analyst’s evening routine is ETL done by hand. The file is cleaned before it touches the "
            "warehouse workbook.",
            ("point", "Strength", "The warehouse only ever holds checked data. Readers cannot stumble on a raw "
             "or half-cleaned row."),
            ("point", "Weakness", "If a cleaning rule turns out to be wrong, the original rows are no longer "
             "in the warehouse. You must go back to the source and extract them again."),
            ("h", "ELT: Load First, Clean Inside"),
            "In ELT, data is extracted and loaded as it is, into a raw area of the warehouse. The transform "
            "step then runs inside the warehouse, producing clean tables from the raw ones. AWS calls ELT "
            "the standard choice for modern analytics, made practical by cloud storage that can hold large "
            "amounts of raw data.",
            ("point", "Strength", "The raw rows stay available. If a rule changes, for example how a "
             "cancelled receipt is handled, you rerun the transform on the raw data without touching the "
             "source system again."),
            ("point", "Weakness", "Raw data now sits in the warehouse too. It needs the same access controls "
             "as the clean tables, and readers must be pointed only at the clean ones."),
            ("quote", "ETL protects the warehouse from messy data. ELT protects you from your own cleaning "
             "mistakes. Choose the risk you can manage better."),
            ("h", "A Treasury Example, Both Ways"),
            "Take the same nightly job: the day’s official receipts, including two cancelled ones and a "
            "barangay typed as “Pob. 1” instead of its code.",
            ("point", "ETL version", "A script reads the day’s receipts, drops the cancelled ones, replaces "
             "“Pob. 1” with the barangay code, and appends the clean rows to the collections fact table."),
            ("point", "ELT version", "A script copies the day’s receipts, untouched, into a raw receipts table. "
             "A saved SQL query then builds the collections fact table from the raw table, dropping cancelled "
             "receipts and mapping names to codes."),
            "A month later, the head of office asks for a report of cancelled receipts by collector. In the "
            "ETL version, the cancelled rows were never kept, so someone must extract them again from the "
            "counter system. In the ELT version, they are already in the raw table, and the report is one "
            "query away.",
            ("h", "Which Fits a Small Treasury?"),
            "There is no single right answer. These questions point the way.",
            ("point", "Where will transforms run?", "If your warehouse is a spreadsheet, transforms are easiest to do before loading, so ETL is the natural fit. If it is a database such as SQLite, it can run "
             "SQL itself, and ELT becomes easy."),
            ("point", "Will the rules change?", "If the office is still deciding how to count things, keeping "
             "raw data makes changes cheaper. That favors ELT."),
            ("point", "How sensitive is the raw data?", "If raw rows contain personal details you do not need "
             "for reporting, removing them before loading, ETL style, keeps them out of the warehouse "
             "altogether."),
            "You can also mix the two: personal details are removed on the way in, as in ETL, while "
            "everything else is loaded raw and shaped inside, as in ELT. That is a deliberate choice, made for a clear reason.",
            ("h", "Checks Every Pipeline Needs"),
            "Whichever pattern you pick, a pipeline that runs without someone watching needs to check itself "
            "and leave a record.",
            ("point", "Count check", "The number of receipts loaded should match the number recorded in the "
             "source for that day."),
            ("point", "Total check", "The sum of amounts loaded should match the day’s total in the "
             "collection report."),
            ("point", "Completeness check", "Every row must have a date, a collector code, a barangay code "
             "and an account code. Rows that fail go to a review list, not into the reports."),
            ("point", "Run log", "Each run writes one line: date, time, rows read, rows loaded, rows set "
             "aside. If last night’s line is missing, the pipeline did not run."),
            "These four checks turn a silent failure, like the empty day in the opening story, into a visible "
            "one that someone can fix before the morning meeting.",
            ("h", "Making It Run Without You"),
            "A pipeline only removes the evening chore if it starts by itself. Desktop computers have built-in schedulers for this: Task Scheduler on Windows, and cron on Linux and macOS. Either can start a script at a fixed time every day. After setting it up, read the run log for the first few mornings to confirm it really runs.",
            ("point", "Pick a time after the day closes", "Schedule the run after the cashier’s closing, so the day’s "
             "records are complete. Write that time on the dashboard as “data as of.”"),
            ("point", "Make reruns safe", "If the job runs twice for the same day, it should replace that day’s rows, "
             "not add them again. Otherwise one accidental rerun doubles a day’s collections."),
            ("point", "Name an owner", "Someone must read the run log each morning and act when a check fails. A "
             "pipeline nobody watches only fails more quietly."),
            ("h", "Key Takeaways"),
            ("point", "Same steps, different order", "ETL transforms before loading; ELT loads raw data and "
             "transforms inside the warehouse."),
            ("point", "ETL keeps the warehouse clean", "Good when the warehouse cannot run transforms, or "
             "when sensitive details should never enter it."),
            ("point", "ELT keeps the raw data", "Good when rules may change and the warehouse can run SQL."),
            ("point", "Every pipeline checks itself", "Counts, totals, completeness and a run log catch "
             "problems before readers do."),
            ("h", "Your Part 7 Exercise"),
            "Write down, step by step, how one daily or monthly report in your office gets its data today. "
            "Then mark each step:",
            ("point", "E, T or L", "Is this step extracting, transforming or loading?"),
            ("point", "Manual or automatic", "Does a person do it, or does it run by itself?"),
            ("point", "Checked or unchecked", "Is there any count or total that proves it worked?"),
            "The first manual, unchecked step on your list is the best place to start automating.",
            ("cta", "Read: Business Intelligence Series, Part 6", "/blog/business-intelligence-part-6-warehouses-marts-lakes/"),
            ("cta", "Read: Business Intelligence Series, Part 5", "/blog/business-intelligence-part-5-data-modeling/"),
            ("cta", "Read: Data Analytics Series, Part 6", "/blog/data-analytics-part-6-data-ethics-privacy/"),
            ("cta", "Read: Keep a receipts register in SQLite", "/tutorials/receipts-register-with-sqlite/"),
            ("ask", "Which step in your office’s reporting still depends on one person remembering to do it?"),
        ],
    },
    {
        "date": "December 6, 2026",
        "title": "Business Intelligence Series, Part 6: Databases, Warehouses, Marts and Lakes, in Plain Words",
        "slug": "business-intelligence-part-6-warehouses-marts-lakes",
        "category": "bi",
        "summary": "Where should the data behind a dashboard live? This part explains the difference between a "
                   "database, a data warehouse, a data mart and a data lake, with a treasury example for each, "
                   "and shows how a small office can start without buying anything.",
        "publish_on": "2026-12-06 21:00",
        "body": [
            "The cashier is closing the day. At the same moment, the head of office opens the collections "
            "dashboard, and the dashboard asks the collection system to add up every receipt of the year by "
            "barangay and by account. The cashier’s screen freezes for a minute. Two taxpayers at the window "
            "wait while a chart loads in another room.",
            "Nothing is broken. The same system is simply being asked to do two very different jobs at once: "
            "record each payment quickly and correctly, and answer big questions about thousands of past "
            "payments. Business intelligence works better when those two jobs are kept apart.",
            "(As always in this series, the office, the people and the numbers are made up. No real town or "
            "taxpayer is described.)",
            "In Part 5, we shaped the data into a star: facts in the middle, dimensions around them. This part "
            "is about where that star should live. By the end of this post you will know the difference "
            "between a database, a data warehouse, a data mart and a data lake, which one a treasury needs "
            "first, and how to set up a small, free version to practice on.",
            ("photo", "blog/bi-data-homes.jpg", "Four homes for data: the database runs the day, the warehouse "
             "keeps the history, the mart serves one unit, and the lake holds raw files for later. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "The Database: Built to Run the Day"),
            "A system that records transactions keeps them in a database. In a treasury, it is the "
            "database of the collection system: each official receipt, each payment line, each cancellation, "
            "saved the moment it happens.",
            "This kind of database is designed for many small, fast actions: add one receipt, look up one "
            "taxpayer, correct one entry. It holds the current state of things, and it must stay quick for the "
            "people at the counter.",
            ("point", "Good at", "Recording and finding single transactions, all day, without errors."),
            ("point", "Not built for", "Adding up a whole year of receipts every time someone opens a chart. "
             "Heavy reporting queries compete with the counter for the same system."),
            ("h", "The Data Warehouse: Built to Answer Questions"),
            "A data warehouse is a separate store, copied from the working systems and arranged for analysis. "
            "Bill Inmon, one of the early writers on the subject, described it as a subject-oriented, "
            "integrated, time-variant and non-volatile collection of data that supports management’s "
            "decisions. Each of those four words is worth unpacking.",
            ("point", "Subject-oriented", "Organized around the things the office asks about, such as "
             "collections, taxpayers and accounts, rather than around the screens of each system."),
            ("point", "Integrated", "Data from several sources is brought together and made consistent. The "
             "barangay codes from the collection system and from the assessor’s records match."),
            ("point", "Time-variant", "It keeps history, so you can compare this month with the same month "
             "in past years."),
            ("point", "Non-volatile", "Once loaded, records are not changed by daily work. New data is added; "
             "old data stays as it was, so last year’s report gives the same answer next year."),
            "The star model from Part 5 is a common shape inside a warehouse. The dashboard reads from the "
            "warehouse, never from the cashier’s system, so a chart no longer slows down the counter.",
            ("h", "The Data Mart: One Unit’s Slice"),
            "A data mart is a smaller store built for one unit or one subject. It can be built as a slice of the warehouse.",
            "For example, the revenue unit may need only collections and delinquencies, while the cash unit "
            "needs deposits and disbursements. Each mart holds only what its users need, which keeps it simple "
            "and makes it easier to control who sees what.",
            ("h", "The Data Lake: Keep Everything Now, Shape It Later"),
            "A data lake is a central store for data in its original form: spreadsheets, exported files, "
            "scanned documents, system logs. Nothing has to be cleaned or modeled before it goes in. The "
            "structure is decided only when someone reads the data for a particular analysis.",
            "That flexibility is the lake’s strength and its risk. A lake without a clear list of what is in "
            "it, who owns each file and who may open it becomes very hard to use and very hard to protect. "
            "For an office that holds taxpayers’ personal data, that is a serious concern.",
            ("quote", "A warehouse answers the questions you planned for. A lake keeps the data for questions "
             "you have not asked yet, but only if someone keeps track of what is in it."),
            ("h", "How Data Moves From the Counter to the Warehouse"),
            "Data does not jump into a warehouse by itself. A small, regular job copies it, usually after the day "
            "is closed. This job is often called ETL, short for extract, transform and load.",
            ("point", "Extract", "Read the day’s receipts, cancellations and deposits from the working database "
             "without changing anything there."),
            ("point", "Transform", "Turn names into codes, check that every receipt has a date, a collector and an "
             "account, and set aside anything that fails a check for someone to review."),
            ("point", "Load", "Add the checked rows to the warehouse tables, and record how many rows were added and "
             "when, so anyone can see whether last night’s copy ran."),
            "Run it at the same time every day. A dashboard that says “data as of last night, 8:00 p.m.” is "
            "easier to trust than one that leaves readers guessing.",
            ("h", "Side by Side"),
            ("point", "Database", "Purpose: run daily work. Data: current, detailed, changing all day. Users: "
             "counter staff and the system itself."),
            ("point", "Warehouse", "Purpose: analysis across the office. Data: cleaned, integrated, with "
             "history. Users: analysts, dashboards, management."),
            ("point", "Mart", "Purpose: one unit’s reports. Data: a cleaned subset. Users: one team."),
            ("point", "Lake", "Purpose: keep raw data for later use. Data: any format, as received. Users: "
             "analysts who know how to shape it."),
            ("h", "What a Small Treasury Needs First"),
            "A small office does not need all four. A sensible order is:",
            ("point", "1. Keep the working database clean", "Everything starts here. If receipts are encoded "
             "late or wrongly, no warehouse can fix it."),
            ("point", "2. Build a small warehouse", "A nightly copy of the day’s transactions into a separate "
             "file or database, arranged as a star. Even a separate SQLite file works for a start."),
            ("point", "3. Add marts only when units need different views", "Begin with one warehouse that "
             "everyone reads. Split it only when access or performance requires it."),
            ("point", "4. Treat a lake with caution", "Collecting files “just in case” is easy. Knowing what "
             "they contain, and protecting them, is the hard part."),
            ("h", "Practicing for Free"),
            "You can practice building a warehouse without spending anything. On your own computer, a SQLite "
            "file can hold a small star model with made-up data. In the cloud, Google offers a BigQuery "
            "sandbox that needs no credit card. It allows 10 GiB of storage and 1 TiB of query processing a "
            "month, and tables in the sandbox expire automatically after 60 days, so it is a place to learn, "
            "not to keep records.",
            "Use made-up or fully aggregated data for practice. Real taxpayer records should stay inside the "
            "systems and rules your office has approved.",
            ("h", "Key Takeaways"),
            ("point", "Separate running from reporting", "The counter’s database records the day; the "
             "warehouse answers questions about it."),
            ("point", "A warehouse keeps history", "It is integrated, organized by subject and not changed by "
             "daily work."),
            ("point", "Marts serve one unit", "Smaller, simpler and easier to control."),
            ("point", "Lakes need a catalog", "Raw data without a list of what is in it is hard to use and "
             "hard to protect."),
            ("h", "Your Part 6 Exercise"),
            "Make a short inventory of where your office’s data lives today:",
            ("point", "Working systems", "Which systems record transactions every day?"),
            ("point", "Report sources", "When a report is prepared, does it read from those systems directly, "
             "or from a copy?"),
            ("point", "Loose files", "Which spreadsheets and exports sit on shared drives or personal "
             "computers, and who owns each one?"),
            "If every report reads straight from the working system, a simple nightly copy is your first "
            "warehouse project.",
            ("cta", "Read: Business Intelligence Series, Part 5", "/blog/business-intelligence-part-5-data-modeling/"),
            ("cta", "Read: Business Intelligence Series, Part 3", "/blog/business-intelligence-part-3-what-to-watch/"),
            ("cta", "Read: Data Analytics Series, Part 5", "/blog/data-analytics-part-5-zero-budget-toolkit/"),
            ("cta", "Read: Keep a receipts register in SQLite", "/tutorials/receipts-register-with-sqlite/"),
            ("ask", "Where does the data behind your office’s monthly report actually come from?"),
        ],
    },
    {
        "date": "December 1, 2026",
        "title": "Business Intelligence Series, Part 5: Data Modeling 101, Facts, Dimensions and the Star",
        "slug": "business-intelligence-part-5-data-modeling",
        "category": "bi",
        "summary": "A dashboard can only be as right as the tables behind it. This part explains facts, "
                   "dimensions, grain and keys in plain words, and shows how one star-shaped model turns a "
                   "messy collections spreadsheet into numbers everyone can trust.",
        "publish_on": "2026-12-01 21:00",
        "body": [
            "The new dashboard says Barangay 1 collected ₱412,000 last month. The cashier’s report says "
            "₱356,500. Both people are sure they are right, and the meeting turns into an argument about "
            "who made a mistake.",
            "Nobody made a typing mistake. The spreadsheet behind the dashboard listed every official receipt "
            "with its total, and also listed each revenue line on that receipt with the same total beside it. "
            "Some receipts were counted twice. The same barangay was also spelled three ways, so part of its "
            "money landed in rows the chart never picked up. The fix was not a better chart. It was a better "
            "shape for the data.",
            "(As always in this series, the office, the people and the numbers are made up. No real town or "
            "taxpayer is described.)",
            "In Part 4, the BI brief defined each measure in plain words. This part is about the tables that "
            "hold those measures. That design is called the data model, and it decides whether a dashboard "
            "gives the same answer as the cashier. By the end of this post you will know the four ideas behind a sound model (facts, dimensions, grain and keys), and you will be able to sketch one for "
            "your own office on a single sheet of paper.",
            ("h", "What a Data Model Is"),
            "A data model is the set of tables a report reads, the columns in each table, and the links "
            "between them. You can build one in a spreadsheet with a few tabs, in a small database, or in a "
            "BI tool. The tool matters less than the design.",
            "Suppose the office starts with one wide table: every receipt on its own row, with the collector’s name, "
            "the barangay, the revenue account and the amount typed in full each time. It works for a month. "
            "Then the problems pile up.",
            ("point", "Repeated text drifts", "A barangay typed by hand a thousand times will be typed "
             "differently some of those times, and each spelling becomes its own group in a chart."),
            ("point", "Totals get mixed with details", "When a receipt total and its line amounts sit in the "
             "same column, adding the column counts the money twice."),
            ("point", "Changes are hard", "If a collector’s name or a revenue account title changes, "
             "every past row has to be edited, and it is easy to miss some."),
            ("h", "Facts and Dimensions"),
            "A well-known way to fix this is to split the data into two kinds of tables. Microsoft describes it as a mature approach widely adopted by data warehouses, and its guidance for Power BI is built on it.",
            ("point", "Fact tables", "Each row records an event or an observation, such as one revenue line "
             "on an official receipt. A fact table holds numbers to add up, like the amount, plus key columns "
             "that point to the dimensions. It has many rows and keeps growing over time."),
            ("point", "Dimension tables", "Each row describes one thing you want to filter or group by: one "
             "date, one collector, one barangay, one revenue account. A dimension table has a unique key and "
             "descriptive columns. It has far fewer rows."),
            "A simple test helps. If you would add it up, it belongs in a fact table. If you would filter, "
            "sort or group by it, it belongs in a dimension.",
            ("h", "The Star Shape"),
            ("photo", "blog/bi-star-schema.jpg", "A star-shaped model for treasury collections: one fact "
             "table in the middle, with the date, collector, barangay and revenue account tables around it. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            "Draw the fact table in the middle and the dimensions around it, and the picture looks like a "
            "star. That is why this design is called a star schema.",
            "Each line in the picture is a one-to-many link. One barangay appears once in the barangay table "
            "but on many rows of the collections table. One collector appears once in the collector table but "
            "on every receipt line that collector issued.",
            "When someone asks for collections by barangay for October, the work is split cleanly. The date "
            "table filters to October. The barangay table groups the rows. The fact table adds up the "
            "amounts. Dimensions filter and group, and facts are summarized. Charts by "
            "barangay, by collector or by month all follow that same pattern.",
            ("h", "A Treasury Example"),
            "Here is a small model for collections. Every table fits on one spreadsheet tab.",
            ("point", "Collections (fact)", "One row per revenue line on an official receipt: receipt "
             "number, date key, collector key, barangay key, account key and amount. Nothing else."),
            ("point", "Date (dimension)", "One row per calendar day, with the month, the quarter and the "
             "year already worked out, so nobody has to calculate them in every chart."),
            ("point", "Collector (dimension)", "One row per collector: a code, the name and the unit."),
            ("point", "Barangay (dimension)", "One row per barangay: a code and the official name, spelled "
             "correctly once."),
            ("point", "Revenue account (dimension)", "One row per account: a code, the account title and the "
             "group it belongs to, such as real property tax or business tax."),
            "Notice what is missing from the fact table: names. The fact row carries only codes and the "
            "amount. The names live in one place each, so a misspelling can be fixed once and every chart "
            "picks up the correction.",
            ("h", "Grain: Decide What One Row Means"),
            "Before a single row goes into a fact table, write one sentence: “One row in this table is "
            "one ...” That sentence is the grain.",
            "For collections, the grain could be one receipt, or one revenue line on a receipt. Either can "
            "work. Mixing them cannot. Suppose receipt 1201 has two lines, ₱1,000 for one account and ₱500 "
            "for another, so the receipt total is ₱1,500. If the fact table stores the line amounts, the "
            "receipt adds up to ₱1,500. If it also stores the ₱1,500 total on each line, the same receipt "
            "adds up to ₱3,000 on the dashboard. That is exactly the kind of error from the opening story.",
            "Choose the finest grain your reports need. Line-level rows can always be added up to receipt "
            "totals, but receipt totals can never be split back into accounts.",
            ("quote", "Write down what one row means before you load the first row. A grain nobody "
             "wrote down is a double count waiting to happen."),
            ("h", "Keys: Link With Codes, Not Names"),
            "A key is the column that links a fact row to its dimension row. Every key in a dimension table "
            "must be unique, or the link breaks.",
            "Use codes, not names. Two collectors can share a surname. A barangay can be renamed. A code that "
            "never changes keeps every past row linked correctly.",
            "If the source records have no code, make one. A running number added to the dimension table "
            "works. Microsoft calls this a surrogate key: a unique identifier that you add to support the "
            "model, even though it does not exist in the original data.",
            ("h", "Building It Without Special Software"),
            "You can build this model in any spreadsheet. Put each table on its own tab. In the collections "
            "tab, type only codes, and use a lookup formula to show the names beside them when you need to "
            "read a row. A pivot table can then sum the amounts by any column from the dimension tabs.",
            "BI tools make the links visible. In Power BI Desktop, which Microsoft offers as a free download "
            "for Windows, you load each tab as a table and draw the one-to-many links between them. The same "
            "design then works for every chart you add.",
            ("h", "Mistakes to Avoid"),
            ("point", "One giant table", "Easy to start, hard to trust. Split it into facts and dimensions as "
             "soon as more than one person reads the reports."),
            ("point", "Mixed grain", "Receipt totals and line amounts in the same fact table will double "
             "count. Keep one grain per fact table."),
            ("point", "Names as keys", "Spellings drift and names change. Link with codes."),
            ("point", "Calculating dates in every chart", "Put month, quarter and year in the date table "
             "once, so every chart groups dates the same way."),
            ("h", "Key Takeaways"),
            ("point", "Shape before charts", "A dashboard can only be as accurate as the tables behind it."),
            ("point", "Facts are added, dimensions describe", "Amounts go in the fact table; dates, people, "
             "places and accounts go in dimensions."),
            ("point", "Write the grain down", "One sentence about what a row means keeps totals and details "
             "from being counted twice."),
            ("point", "Link with codes", "Unique codes keep every row connected when names change."),
            ("h", "Your Part 5 Exercise"),
            "Take one report your office prepares every month and sketch its model on paper:",
            ("point", "The fact", "What event does each row record? Write the grain in one sentence."),
            ("point", "The dimensions", "List every column people filter or group by. Each is a candidate "
             "dimension table."),
            ("point", "The keys", "For each dimension, what code will link it to the facts? If there is none, "
             "plan a running number."),
            "If your sketch looks like a star, you are ready to build. If it looks like one long table, you "
            "have just found the reason your totals sometimes disagree.",
            ("cta", "Read: Business Intelligence Series, Part 4", "/blog/business-intelligence-part-4-the-bi-brief/"),
            ("cta", "Read: Business Intelligence Series, Part 3", "/blog/business-intelligence-part-3-what-to-watch/"),
            ("cta", "Read: Data Analytics Series, Part 4", "/blog/data-analytics-part-4-four-questions-worked/"),
            ("cta", "Read: Keep a receipts register in SQLite", "/tutorials/receipts-register-with-sqlite/"),
            ("ask", "Which report in your office would give a different total if you rebuilt it as a star?"),
        ],
    },
    {
        "date": "November 26, 2026",
        "title": "Business Intelligence Series, Part 4: Start With the People, Then Write the Brief",
        "slug": "business-intelligence-part-4-the-bi-brief",
        "category": "bi",
        "summary": "Before anyone builds a dashboard, someone has to ask the people who will use it what they "
                   "need to decide. Here is how to run those conversations and turn the answers into a "
                   "one-page BI brief that everyone can agree on.",
        "publish_on": "2026-11-26 21:00",
        "body": [
            "The head of office calls the clerk who is good with spreadsheets. “I want a dashboard for "
            "collections. Can you have it ready by the end of the month?” The clerk says yes, goes back to her "
            "desk, and starts building charts of everything she can find.",
            "Three weeks later she shows the result. The head of office looks at it politely and asks, “Where "
            "can I see which collectors have not yet turned in their reports?” That was never on the screen, "
            "because nobody asked what the dashboard was for.",
            "(As always in this series, the office, the people and the numbers are made up. No real town or "
            "taxpayer is described.)",
            "In Part 3, I listed six measures a treasury could watch every day. This part goes one step earlier. Before you choose a single measure, find out who will use the dashboard and what they will decide with it, then write it down on one page. I call that page the BI brief. By the end of this post you will have five interview questions, a six-line template and a filled-in example you can copy.",
            ("h", "Ask About Decisions, Not Charts"),
            "Asking people which charts they want to see is the wrong starting point, because a chart is only "
            "useful if it changes what someone does.",
            "Ask instead about the decisions they make. A good first conversation sounds like this:",
            ("point", "What do you decide every week?", "For example: which barangays get a collection visit, "
             "whether to request more official receipts, when to remind collectors about late reports."),
            ("point", "What do you need to know to make that decision?", "The answer to this question is the "
             "first draft of your measures."),
            ("point", "How do you find out now?", "Phone calls, printed reports, asking the cashier. This shows "
             "you where the data already lives and how much time the dashboard can save."),
            ("point", "When do you need to know it?", "Every morning, every Friday, before the monthly meeting. "
             "This sets how often the data must be updated."),
            ("point", "What would you do if the number looked wrong?", "This tells you who should be alerted "
             "and what the limit should be."),
            "Notice that none of these questions mentions software. The conversation is about the work, and the tools come later.",
            "If you are not sure how to begin, try this opening: “I am not here to ask what charts you want. I want to understand what you decide each week, and what you wish you knew sooner.” It keeps the conversation on their own work, which they know better than anyone.",
            ("h", "Talk to More Than One Person"),
            "The person who asked for the dashboard is not the only person who will use it. In a treasury, the "
            "head of office, the revenue unit, the cashier and the collectors may all open the same screen for "
            "different reasons.",
            "Talk to each group separately, even for ten minutes. The head of office may want totals against "
            "target. The cashier may want undeposited collections by day. A collector may simply want to see their own receipts for the week. If all three needs are known at the start, the dashboard can be "
            "designed with separate views instead of one crowded page.",
            "Write down each answer in the person’s own words. Later, when someone asks why a chart exists, you "
            "can point to the conversation that asked for it.",
            ("h", "The One-Page BI Brief"),
            "When the conversations are done, put what you learned on one page. Show it to the people you "
            "talked to and ask them to confirm it before you build anything.",
            ("photo", "blog/bi-brief.jpg", "A one-page BI brief covers six things: the decisions it supports, "
             "its readers, the measures and how each is defined, the data sources, how often it refreshes, and "
             "who may see what. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("point", "1. Decisions", "The two or three decisions the dashboard will support, in one sentence each."),
            ("point", "2. Readers", "Who will use it, when and on what device. If most readers will use a phone, "
             "say so here."),
            ("point", "3. Measures", "Each measure with a plain definition: what is counted, what is left out, "
             "and over which period."),
            ("point", "4. Sources", "Where each measure comes from: which record, kept by which unit."),
            ("point", "5. Refresh", "How often the data is updated and what time of day it is complete."),
            ("point", "6. Access", "Who may see what. Totals may be open to all staff, while anything with "
             "names or property details is limited to those who need it for their work."),
            ("h", "A Sample Brief"),
            "Here is how the clerk’s brief might look after a second try.",
            ("point", "Decisions", "Whether to follow up with a collector about a late report. Whether to "
             "request more official receipts. Whether collections are on track for the month."),
            ("point", "Readers", "The head of office, on a phone, each morning before 9. The cashier and the "
             "revenue unit, on a computer, during the day."),
            ("point", "Measures", "Reports not yet submitted, by collector, as of yesterday. Official receipts "
             "left, by collector. Collections this month against the monthly target."),
            ("point", "Sources", "The daily report of collections and deposits, the register of accountable "
             "forms, and the monthly target set by the office."),
            ("point", "Refresh", "Every evening after the cashier closes the day."),
            ("point", "Access", "All three measures show totals by collector only. No taxpayer names appear "
             "on any screen."),
            "The brief has fewer lines than the first dashboard had charts, and it is far more useful, because every line answers something a real person asked.",
            ("quote", "A dashboard built from a brief answers the reader’s questions. A dashboard built without "
             "one answers the builder’s."),
            ("h", "Defining Each Measure"),
            "The measures line deserves extra care. Two people can use the same word and mean different things. "
            "Does “collections this month” include payments received on the last day but deposited the next "
            "morning? Does it include fees collected for other offices? Is it counted by the date on the "
            "official receipt or by the date of encoding?",
            "Agree on these answers before building. Write each definition in one or two sentences, and put "
            "the same definition in a small note on the dashboard itself. When someone compares the dashboard "
            "with a printed report and finds a difference, the definition is the first thing to check.",
            ("h", "Privacy Belongs in the Brief"),
            "Treasury records hold taxpayers’ names, addresses and property details. In the Philippines, the "
            "handling of personal information is governed by the Data Privacy Act of 2012 (Republic Act No. "
            "10173). The access line of the brief is where you decide, in advance, which screens show only "
            "totals and which, if any, show individual records.",
            "A simple rule helps: if a decision can be made from totals, the screen shows totals. Decide this with the people who use the dashboard and with your office’s data protection officer. The National Privacy Commission’s Advisory No. 2017-01 asks every local government unit to designate one, so there should be someone to ask.",
            ("h", "Mistakes to Avoid"),
            ("point", "Building before asking", "Charts made before the conversations can end up showing what was easy "
             "to count, not what anyone needed. Ask first, then build."),
            ("point", "Asking only the boss", "The head of office matters most, but the people who use the "
             "screen every day often know which numbers are missing or confusing."),
            ("point", "Promising everything", "If five people ask for twenty measures, the brief should still "
             "choose the few that support real decisions. Keep the rest on a list for later."),
            ("point", "Skipping the sign-off", "A brief that nobody confirmed is just the builder’s guess. Ask "
             "each reader to say, in writing or in a short message, that it matches what they need."),
            ("h", "When the Brief Changes"),
            "Needs change. A new head of office arrives, a new revenue source is added, or a measure turns out "
            "to be less useful than expected. When that happens, update the brief first, confirm it with the "
            "readers, and only then change the dashboard. The brief stays the single place where everyone can "
            "see what the dashboard is meant to do.",
            ("h", "Key Takeaways"),
            ("point", "Ask about decisions, not charts", "A dashboard is only worth building if it changes what someone does."),
            ("point", "Talk to every kind of reader", "The head of office, the cashier and the collectors need different views of the same data."),
            ("point", "Put it on one page and get it confirmed", "Decisions, readers, measures, sources, refresh and access, agreed before anything is built."),
            ("h", "Your Part 4 Exercise"),
            "Pick one person in your office who receives a regular report. This week, ask them three questions:",
            ("point", "Decision", "What do you decide with this report?"),
            ("point", "Timing", "When do you need it, and how old can the numbers be?"),
            ("point", "Gaps", "What do you still have to ask someone about after reading it?"),
            "Write their answers on half a page. You now have the start of a BI brief, and very likely an idea "
            "for making that report shorter and more useful.",
            ("cta", "Read: Business Intelligence Series, Part 3", "/blog/business-intelligence-part-3-what-to-watch/"),
            ("cta", "Read: Business Intelligence Series, Part 2", "/blog/business-intelligence-part-2-the-bi-team/"),
            ("cta", "Read: Project Management Series, Part 3", "/blog/project-management-part-3-stakeholder-mapping/"),
            ("cta", "Read: Your Data at the Treasury Counter", "/blog/your-data-at-the-treasury-counter/"),
            ("ask", "What is one question your current reports never answer?"),
        ],
    },
    {
        "date": "November 21, 2026",
        "title": "Business Intelligence Series, Part 3: What a Treasury Should Watch Every Day",
        "slug": "business-intelligence-part-3-what-to-watch",
        "category": "bi",
        "summary": "A dashboard that shows everything helps no one. Here are six measures worth watching every day "
                   "in a local treasury, how to tell an early warning from an after-the-fact report, and how to "
                   "set limits that tell you when to act.",
        "publish_on": "2026-11-21 21:00",
        "body": [
            "A newly built treasury dashboard has forty-two charts. There are collections by "
            "every revenue account, by every collector, by every barangay, by week, by month and "
            "by year. The head of office opens it twice, scrolls for a minute, and goes back to "
            "asking the cashier for the total over the phone.",
            "Nothing on the dashboard is wrong. There is simply too much of it, and none of it "
            "says what needs attention today. It answers every question except the one the reader"
            " actually has.",
            "(As always in this series, the office, the people and the numbers are made up. No "
            "real town or taxpayer is described.)",
            "In Part 1, I described BI as a service that keeps answers coming. This part is about"
            " choosing which answers deserve that treatment. The secret is to move from one-time "
            "questions to a short list of measures that are watched every day, each with a clear "
            "limit that tells you when to act. By the end of this post, you will be able to tell "
            "one-time questions from always-on ones, choose a short list of daily measures, and "
            "set limits that tell someone when to act.",
            ("h", "One-Time Questions and Always-On Questions"),
            "Some questions are asked once. Should the office open a second payment window? Did "
            "last year’s tax amnesty bring in more than it cost? These are perfect for an "
            "analysis: gather the data, study it, report a finding and move on.",
            "Other questions come back every single day. Did we deposit everything we collected? "
            "Are we on track for this month’s target? Are we about to run out of official "
            "receipts? Answering these by hand every morning wastes time and invites mistakes. "
            "These are the questions a BI system should answer on its own.",
            "A simple test helps. If the same person asks the same question more than once a "
            "week, and the answer can change what they do that day, it belongs on the dashboard. "
            "If not, it is probably better as a report or a one-time study.",
            ("h", "Six Measures Worth Watching"),
            "Every office is different, but a local treasury can start with these six.",
            ("photo",
             "blog/bi-watch.jpg",
             "Six measures a treasury BI system can check every day: collections against target, "
             "deposits against collections, accountable forms in stock, arrears by age, permit "
             "renewals and cash on hand. (Illustration: Butch Mahinay, aumahinay.dev)",
             "medium"),
            ("point",
             "1. Collections against target",
             "How much has come in so far this month and this year, compared with what was "
             "expected by this date. A month that is 60% over with only 40% of its target "
             "collected is worth a question today, not at month-end."),
            ("point",
             "2. Deposits against collections",
             "Audit rules expect collections to be deposited intact, daily or by the next banking"
             " day. A measure that compares what was collected with what reached the bank, by "
             "date, shows at once when cash is staying in a drawer longer than it should."),
            ("point",
             "3. Accountable forms in stock",
             "How many official receipts, by form type, are left in stock and with each "
             "collector. This measure looks ahead, so new forms can be issued before anyone runs "
             "out during the January rush."),
            ("point",
             "4. Arrears by age",
             "Unpaid real property tax grouped by how long it has been unpaid: this year, one to "
             "two years, three years or more."),
            ("point",
             "5. Permit renewals",
             "In January, how many businesses from last year’s list have renewed so far, compared"
             " with the same day last year. A slow start in the second week is still fixable."),
            ("point",
             "6. Cash on hand",
             "How much is in the vault and in the bank accounts, by fund, against the payments "
             "due this week. This one is for the head of office and the budget office together."),
            "Six is not a magic number. The point is to keep the list short enough that someone "
            "can read all of it in under a minute. If a measure has not changed anyone’s decision"
            " in three months, take it off the main screen.",
            ("h", "Early Warnings and After-the-Fact Reports"),
            "Measures come in two kinds. Some tell you what already happened. Others warn you "
            "about what is about to happen. These are often called lagging and leading "
            "indicators.",
            ("point",
             "Lagging: the score",
             "Total collections last month. Collection efficiency for the year. These are "
             "important, and they are what higher offices and auditors will look at, but by the "
             "time you see them, it is too late to change them."),
            ("point",
             "Leading: the warning",
             "Forms left in stock. Renewals in the first week of January. Undeposited collections"
             " older than one day. These move before the score does, so they give you time to "
             "act."),
            "A good dashboard has both, but it puts the leading measures where the eye lands "
            "first. The head of office cannot change last month. She can still send more forms to"
            " a collector before he runs out.",
            ("quote",
             "A lagging measure tells you how the game ended. A leading measure tells you while "
             "you can still play."),
            ("h", "Give Every Measure a Limit"),
            "A number on a screen does not tell anyone whether to worry. A limit does. For each "
            "measure, agree in advance on the point where someone must act, and on who that "
            "someone is.",
            ("point",
             "Forms in stock",
             "If any collector has fewer than two booklets of official receipts left, the "
             "accountable forms custodian issues more that day."),
            ("point",
             "Undeposited collections",
             "If any collection is still undeposited after the next banking day, the cashier "
             "explains why before noon."),
            ("point",
             "Collections against target",
             "If the month is past its halfway point and less than 40% of the target is in, the "
             "revenue unit reviews which sources are behind."),
            "Dashboard tools such as Power BI can send an alert when a number crosses a limit you"
            " set. Even without that, a simple rule written next to each chart turns watching "
            "into acting.",
            "Be careful with limits that are too tight. A warning that goes off every second day "
            "stops telling you anything. Start with limits that catch real problems, then adjust "
            "them after a month of watching.",
            ("h", "Watching Without Gaming"),
            "Any measure that people are judged by can start to change their behavior, and not "
            "always in the way you hoped. If collectors are praised only for the amount they "
            "collect, they may chase the easy payments and avoid the hard delinquent accounts. If"
            " the office is praised only for fast deposits, someone may be tempted to deposit "
            "before counting carefully.",
            "The cure is to pair measures that keep each other honest. Watch the amount collected"
            " and the arrears by age together. Watch deposit speed and cash shortages together. "
            "When one improves at the cost of the other, the dashboard shows it.",
            ("h", "Where Each Number Comes From"),
            "A measure is only as good as the record behind it. Before putting any of the six on "
            "a screen, write down where its data is born and how often it is updated.",
            ("point",
             "Collections and deposits",
             "From the official receipts and the daily report of collections and deposits. If "
             "receipts are encoded only at the end of the day, the dashboard will always be a few"
             " hours behind, and everyone should know that."),
            ("point",
             "Forms in stock",
             "From the register of accountable forms kept by the custodian, and from each "
             "collector’s report of forms used. If that register is still on paper, this measure "
             "has to wait until it is encoded."),
            ("point",
             "Arrears and renewals",
             "From the real property tax records and the business permit list. These change "
             "slowly, so updating them once a day is enough."),
            ("point",
             "Cash on hand",
             "From the cashbook and the bank balances. Show the date of each figure clearly on the screen."),
            "Writing this list also shows you which measures are ready now and which need better "
            "record keeping first. That is useful on its own, even before any chart is drawn.",
            ("h", "Start Small, With One Screen"),
            "You do not need all six measures on the first day. Pick the one that causes the most"
            " phone calls in your office and build it well. Make sure the data behind it is "
            "complete and checked every morning, as described in Part 2. Agree on its limit and "
            "its owner. Then add the next one.",
            "A single trusted measure does more good than forty-two charts nobody reads.",
            ("h", "Key Takeaways"),
            ("point",
             "Watch only what changes decisions",
             "If a measure has not changed anyone's choice in three months, take it off the main screen."),
            ("point",
             "Lead with leading measures",
             "Forms in stock and undeposited cash warn you while there is still time to act."),
            ("point",
             "Give every measure a limit and an owner",
             "A number becomes useful when everyone knows the point where someone must act, and who that is."),
            ("point",
             "Pair measures to prevent gaming",
             "Watch amounts with arrears and speed with shortages, so one cannot improve at the "
             "cost of the other."),
            ("h", "Your Part 3 Exercise"),
            "Take ten minutes and list the questions your head of office asks most often. For "
            "each one, write:",
            ("point", "How often", "Daily, weekly, monthly or only once?"),
            ("point", "Leading or lagging", "Does it warn you early, or report what already happened?"),
            ("point", "The limit", "At what number should someone act, and who is that person?"),
            "The questions that are asked daily, give early warning and have a clear limit are "
            "your first dashboard. Everything else can wait.",
            ("cta",
             "Read: Business Intelligence Series, Part 2",
             "/blog/business-intelligence-part-2-the-bi-team/"),
            ("cta",
             "Read: Business Intelligence Series, Part 1",
             "/blog/business-intelligence-part-1-same-data-different-jobs/"),
            ("cta", "Read: Year-End in the Treasury", "/blog/year-end-in-the-treasury/"),
            ("cta",
             "Read: The ALTOS Framework, Principle 9: Evidence Before Decision",
             "/blog/altos-framework-evidence-before-decision/"),
            ("ask", "If your office could watch only one number every morning, which would it be?"),
        ],
    },
    {
        "date": "November 16, 2026",
        "title": "Business Intelligence Series, Part 2: The BI Team, Role by Role",
        "slug": "business-intelligence-part-2-the-bi-team",
        "category": "bi",
        "summary": "Behind every dashboard that people trust are three kinds of work: building the pipes, building "
                   "the screens and explaining what the numbers mean. Here is each BI role in plain words, and "
                   "how one person in a small treasury can wear all three hats.",
        "publish_on": "2026-11-16 21:00",
        "body": [
            "A head of office opens a collections dashboard on a Monday morning and sees that "
            "market fees are down by a third compared with the same week last year. She calls the"
            " person who made the dashboard. “Is this real?”",
            "That question has three possible answers, and each one belongs to a different kind "
            "of work. Maybe the data never arrived because the evening export failed. That is a "
            "pipeline problem. Maybe the chart is adding the wrong field, or the filter is stuck "
            "on one barangay. That is a dashboard problem. Or maybe the numbers are correct, and "
            "something really did happen at the market. That is a question of meaning, and "
            "somebody has to go and find out what it was.",
            "(As always in this series, the office, the people and the numbers are made up. No "
            "real town or taxpayer is described.)",
            "In a large organization, three different people might take that call. In a small "
            "treasury, it may be one person. Either way, it helps to know the three jobs apart, "
            "because each one fails in its own way and each one is fixed in its own way. By the "
            "end of this post, you will know the three kinds of BI work, how each one fails, and "
            "how one person in a small office can do all three.",
            ("photo",
             "blog/bi-roles.jpg",
             "The BI loop: people bring questions, an engineer builds the pipes, a developer "
             "builds the screens, and an analyst explains what the numbers mean. (Illustration: "
             "Butch Mahinay, aumahinay.dev)",
             "medium"),
            ("h", "Start With the People Who Ask"),
            "Every BI system exists because somebody needs to know something, again and again. In"
            " BI language, these people are the stakeholders. In a local treasury, they include "
            "the head of office, the revenue and cash units, the collectors in the field, the "
            "budget and accounting offices, and the local chief executive who asks how the town "
            "is doing against its revenue target.",
            "Stakeholders do not need to know how the data moves. They need to say clearly what "
            "they want to watch and what they will do when the number changes. A head of office "
            "who says “I want to see everything” has not yet asked a question. One who says “I "
            "want to know by noon each day whether yesterday’s collections were deposited in "
            "full” has asked a very good one.",
            "That is why every BI role, whatever the title, begins by listening. The rest of the "
            "team turns those questions into something that answers itself every day.",
            ("h", "The BI Engineer: Building the Pipes"),
            "The BI engineer makes sure the right data arrives in the right place, on time and in"
            " good shape. If BI is a road from the payment counter to the decision maker, the "
            "engineer builds and maintains the road.",
            ("point",
             "What the work looks like",
             "Connecting to the sources, such as the collection system, the cashbook or the list "
             "of business permits. Writing the steps that copy the data out on a schedule. "
             "Combining it into clean tables. Setting up checks so that a missing day or a "
             "repeated receipt number is caught before anyone builds a chart on top of it."),
            ("point",
             "The tools",
             "Usually SQL, often a scripting language such as Python, and a database or data "
             "warehouse. Small offices can do the same work with a spreadsheet, a free database "
             "such as SQLite, and a scheduled task on one computer."),
            ("point",
             "How it fails",
             "Quietly. The dashboard still shows numbers, but they are a day old, half complete "
             "or counted twice. Nobody notices until a total does not match the official report."),
            "When the head of office asks “Is this real?”, the engineer’s first move is to check "
            "that yesterday’s data actually arrived and passed its checks. It is not glamorous "
            "work, but every other role depends on it.",
            ("h", "The BI Developer: Building the Screens"),
            "The BI developer turns clean tables into something people can read and use: "
            "dashboards, reports, filters and alerts. If the engineer builds the road, the "
            "developer builds the place where people stop and look.",
            ("point",
             "What the work looks like",
             "Deciding which measures go on the screen and how each one is calculated. Choosing "
             "the right chart for each measure. Adding date controls and filters so users can ask"
             " follow-up questions. Making sure the layout still works on a phone, because a busy"
             " official may see it there."),
            ("point",
             "The tools",
             "Dashboard tools such as Looker Studio, Power BI or Tableau, plus a good working "
             "knowledge of SQL so the developer can shape the data the screens need."),
            ("point",
             "How it fails",
             "Loudly but misleadingly. A chart that sums when it should count, a filter that "
             "silently hides half the data, or two screens that define “collections” in two "
             "different ways. Each looks fine on its own, but together they start arguments."),
            "In the market fee example, the developer checks that the chart is reading the right "
            "field, that no filter is left on, and that “this week” on the dashboard means the "
            "same days as “this week” in the head of office’s mind.",
            ("h", "The BI Analyst: Explaining What It Means"),
            "The BI analyst stands between the numbers and the people. The analyst helps "
            "stakeholders turn vague worries into clear questions, decides with them which "
            "measures matter, and explains what a change on the dashboard really means.",
            ("point",
             "What the work looks like",
             "Interviewing stakeholders about the decisions they make. Writing down each measure "
             "in plain words, so “collections” always means the same thing. Spotting unusual "
             "patterns, digging into them and reporting the cause. Suggesting improvements to the"
             " dashboard when people keep asking the same follow-up question."),
            ("point",
             "The tools",
             "A spreadsheet, SQL, the dashboard tool itself and, most of all, good conversation "
             "and clear writing."),
            ("point",
             "How it fails",
             "By staying at the desk. An analyst who never asks the collectors or the market "
             "supervisor what happened will report a drop without explaining it."),
            "In our example, the engineer and the developer both confirm that the data is "
            "complete and the chart is correct. So the analyst calls the market supervisor and "
            "learns that one row of stalls was closed for repairs for two weeks. The drop is "
            "real, it has a cause, and it will end. The head of office now knows not to send "
            "collectors out to chase payments that cannot happen yet.",
            ("quote",
             "The engineer makes the number arrive. The developer makes it visible. The analyst "
             "makes it mean something."),
            ("h", "Titles Vary, the Work Does Not"),
            "Job titles in BI are not standard. One organization’s BI engineer is another’s data "
            "engineer. Some companies call the dashboard builder a BI analyst, others a report "
            "developer. In a small team, one person may do the analyst and developer work "
            "together. Do not worry about the labels. Look at the three kinds of work, because "
            "those stay the same everywhere.",
            "BI work also connects with nearby roles. Database administrators keep the systems "
            "that hold the data running and secure. Data analysts, the subject of my other "
            "series, take on one-time questions that may later grow into something a dashboard "
            "should watch every day. Records officers and the data protection officer help decide"
            " who may see what, which matters a great deal when the data includes taxpayers’ "
            "names and properties.",
            ("h", "One Person, Three Hats"),
            "A small treasury may never hire a BI team. That is fine. What matters is that "
            "someone in the office knows when to switch hats.",
            ("point",
             "Monday morning: engineer hat",
             "Before opening the dashboard, check that the weekend’s files arrived and the totals"
             " match the cashbook. Five minutes here saves an hour of confusion later."),
            ("point",
             "Midweek: developer hat",
             "Fix the chart someone found confusing. Add the filter the collectors keep asking "
             "for. Remove a measure nobody uses."),
            ("point",
             "Any time a number moves: analyst hat",
             "Ask what happened before reporting that something did. Talk to the people closest "
             "to the money."),
            "Keeping the three hats separate also helps when something goes wrong. Instead of "
            "saying “the dashboard is broken”, you can say which part failed: the data, the "
            "screen or the explanation. That makes the fix faster and the conversation calmer.",
            ("h", "Skills That Matter in Every Role"),
            "Whatever hat you wear, a few skills carry across all three.",
            ("point",
             "Curiosity about the work behind the data",
             "Knowing how an official receipt is issued, cancelled or reported tells you more "
             "about the data than any tool can."),
            ("point",
             "Care with definitions",
             "Agree in writing on what each measure means and keep that list where everyone can see it."),
            ("point",
             "Respect for privacy",
             "Show totals, not names, unless a person truly needs to see individual records for their work."),
            ("point",
             "Plain communication",
             "Explain what changed, why it matters and what to do, in words a busy official can "
             "read in one minute."),
            ("h", "Key Takeaways"),
            ("point",
             "Start with the people who ask",
             "A good BI question names what to watch and what someone will do when it changes."),
            ("point",
             "Engineer, developer, analyst",
             "One makes the data arrive, one makes it visible, and one explains what it means."),
            ("point",
             "Name what broke",
             "When a number looks wrong, ask whether the data, the screen or the explanation "
             "failed. The fix is faster."),
            ("point",
             "Titles vary; the work does not",
             "Whatever the job is called, all three kinds of work must be done, even if one "
             "person does them."),
            ("h", "Your Part 2 Exercise"),
            "Take the repeated report you circled in Part 1, or pick one now. Then write three short lines:",
            ("point",
             "Engineer",
             "Where does the data for this report come from, and how would you know if one day’s "
             "data were missing?"),
            ("point",
             "Developer",
             "If this report became a single screen, which three measures would go at the top?"),
            ("point", "Analyst", "Who reads this report, and what decision do they make with it?"),
            "If you cannot answer the last line, talk to the reader before changing anything "
            "else. A report that drives no decision is the first one to simplify.",
            ("cta",
             "Read: Business Intelligence Series, Part 1",
             "/blog/business-intelligence-part-1-same-data-different-jobs/"),
            ("cta", "Read: Data Analytics Series, Part 2", "/blog/data-analytics-part-2-six-steps/"),
            ("cta",
             "Read: Project Management Series, Part 1",
             "/blog/project-management-part-1-accidental-project-manager/"),
            ("cta", "Read: Your Data at the Treasury Counter", "/blog/your-data-at-the-treasury-counter/"),
            ("ask",
             "In your office, which hat do you wear most often: the pipes, the screens or the meaning?"),
        ],
    },
    {
        "date": "November 14, 2026",
        "title": "Business Intelligence Series, Part 1: Same Data, Different Jobs",
        "slug": "business-intelligence-part-1-same-data-different-jobs",
        "category": "bi",
        "summary": "Business intelligence and data analytics use the same records but do different jobs. "
                   "Here is what BI really means, where the name came from, what a BI system is made of, "
                   "and how a monthly treasury report can stop being rebuilt by hand.",
        "publish_on": "2026-11-14",
        "body": [
            "On the first working day of every month, a clerk in a municipal treasury starts the "
            "same task. She opens last month's file, copies in the new receipts, fixes the "
            "formulas that broke, and rebuilds the collections report for the head of office. It "
            "takes two days. By the time the report is printed, the numbers are already a week "
            "old, and next month she will do it all again.",
            "(As always on this blog, the office, the people and the numbers are made up. No real"
            " town or taxpayer is described.)",
            "Nothing is wrong with the clerk's work. The totals are correct. The problem is that "
            "the same questions are asked every month, and every month the answers are built from"
            " scratch. Business intelligence, or BI, is the discipline that fixes exactly this "
            "kind of problem. By the end of this post, you will know how BI differs from data "
            "analytics, where the name came from, the five parts of a BI system, and how a "
            "monthly report can stop being rebuilt by hand.",
            ("h", "Why a Second Series?"),
            "My Data Analytics series walks through the full craft of analysis: asking a good "
            "question, preparing and cleaning data, analyzing it and sharing what you found.",
            "After finishing the Google Data Analytics certificate, I went on to the Google "
            "Business Intelligence certificate. It made me see the same data from a different "
            "angle. Analytics taught me how to answer a question. BI taught me how to make sure "
            "the answer keeps arriving, correct and on time, without anyone rebuilding it by "
            "hand. Both matter in a local treasury, so each gets its own series.",
            ("h", "Same Data, Different Jobs"),
            "The simplest way to tell the two apart is to look at what each one delivers.",
            ("point",
             "A data analyst delivers an answer",
             "Someone asks a question, such as whether the office needs a second payment window. "
             "The analyst gathers the data, studies it and reports a finding. The work has a "
             "beginning and an end."),
            ("point",
             "A BI professional delivers a system",
             "Someone needs to watch the same measures again and again, such as daily collections"
             " by revenue source. The BI professional builds the data flow, the model and the "
             "dashboard that keep those answers up to date for everyone who needs them."),
            "In other words, analytics is usually a project, while BI is usually a service. An "
            "analyst might discover that business tax payments drop sharply in the second half of"
            " January. A BI system would show that drop every day, as it happens, so the office "
            "can act before the month ends.",
            "The two overlap a great deal. Good BI depends on the habits of analysis: clear "
            "questions, clean data and honest measures. Good analysis, in turn, often starts with"
            " a pattern someone noticed on a BI dashboard.",
            ("quote", "Analytics answers a question once. BI keeps the answer coming."),
            ("h", "Where the Name Came From"),
            "The phrase is older than computers. In 1865, Richard Millar Devens used “business "
            "intelligence” in a book of commercial stories to describe a banker, Sir Henry "
            "Furnese, who profited by gathering news about events in Europe and acting on it "
            "before his competitors. The idea was simple: whoever has better information, sooner,"
            " makes better decisions.",
            "In 1958, Hans Peter Luhn, a researcher at IBM, published a paper titled “A Business "
            "Intelligence System.” He described a machine that would automatically sort incoming "
            "documents and send each one to the people in an organization who needed it. He "
            "thought of intelligence as the ability to understand how facts relate to each other "
            "well enough to guide action toward a goal. That is still a good definition today.",
            "The modern meaning took shape around 1989, when Howard Dresner, who later worked as "
            "an analyst at the research firm Gartner, proposed business intelligence as an "
            "umbrella term for concepts and methods that improve decisions using fact-based "
            "support systems. Since then the tools have changed many times, from printed reports "
            "to data warehouses to live dashboards on a phone. The goal has not changed at all.",
            ("h", "What a BI System Is Made Of"),
            "A BI system sounds expensive, but its parts are easy to understand. Think of it as a"
            " road from the payment counter to the decision maker.",
            ("photo",
             "blog/bi-system-flow.jpg",
             "A BI system is a road from the records to the decision: data comes from its "
             "sources, a pipeline moves and checks it, a model organizes it, a dashboard shows "
             "it, and people decide. (Illustration: Butch Mahinay, aumahinay.dev)",
             "medium"),
            ("point",
             "Sources",
             "Where the records are born: the collection system, the cashbook, the real property "
             "tax roll, the list of business permits."),
            ("point",
             "Pipeline",
             "The steps that copy data out of each source on a schedule, check it, and combine "
             "it. In BI language this is called ETL, for extract, transform and load."),
            ("point",
             "Model",
             "The organized store where the data waits, arranged so questions are fast and totals"
             " always agree. In larger offices this is a data warehouse."),
            ("point",
             "Dashboard",
             "The screen or report where people see the measures they care about, usually with "
             "filters so they can ask their own follow-up questions."),
            ("point",
             "People",
             "The head of office, the collectors and the budget officer who read the numbers and "
             "decide what to do. Without this last step, the rest is decoration."),
            "Each of these parts can be built in a small version with free tools, which is what "
            "makes BI practical even for a small office.",
            ("h", "Back to the Monthly Report"),
            "Let us return to the clerk and her two-day report. Here is how the same work looks "
            "with even a very simple BI setup.",
            "The collection system exports the day's receipts into a shared folder every evening."
            " A small, scheduled step reads the file, checks that no receipt number is missing or"
            " repeated, and adds the new rows to one clean table. A free dashboard tool, such as "
            "Looker Studio, is connected to that table. It shows collections by revenue source, "
            "by month and against target, and it updates itself.",
            "The head of office now opens the dashboard on a phone whenever she wants. The clerk "
            "no longer rebuilds the report. Instead, she spends her time on the questions the "
            "dashboard raises, such as why market fees in one barangay are lower than last year. "
            "That is analysis, and it is a far better use of a skilled person's day.",
            "Notice that nothing in this example needs a large budget. It needs clear measures, "
            "clean data and someone who knows how the pieces fit together.",
            ("h", "What BI Is Not"),
            "Three misunderstandings are worth clearing up early.",
            ("point",
             "It is not just pretty charts",
             "A dashboard built on messy data spreads wrong numbers faster. The real work in BI "
             "starts before anything is drawn."),
            ("point",
             "It is not expensive software",
             "Commercial tools exist, but a treasury can start with a spreadsheet, a small "
             "database and a free dashboard tool."),
            ("point",
             "It does not replace judgment",
             "A dashboard can show that collections dropped. It cannot tell you whether to send "
             "notices, extend a deadline or fix the encoding backlog. People still decide."),
            "That last point is the same one I made when I built ALTOS: every number the system "
            "produces is a prompt for a person to look and decide, never an automatic action.",
            "All examples in this series use made-up data, and each step can be started with free tools.",
            ("h", "Key Takeaways"),
            ("point",
             "Analytics answers once; BI keeps answering",
             "An analysis ends with a finding. A BI system keeps the same answers current for "
             "everyone who needs them."),
            ("point",
             "A BI system is a road",
             "Sources, pipeline, model, dashboard and people. Each part can start small."),
            ("point",
             "Start small and free",
             "A spreadsheet, a small database and a free dashboard tool are enough to stop "
             "rebuilding a report by hand."),
            ("point",
             "Judgment stays human",
             "A dashboard shows that a number moved. People still decide what to do about it."),
            ("h", "Your Part 1 Exercise"),
            "Take ten minutes and do this:",
            ("point",
             "List your repeated reports",
             "Write down every report your office prepares again and again, daily, weekly, "
             "monthly or quarterly."),
            ("point",
             "Time them",
             "Next to each one, estimate how many hours it takes to prepare and how old the "
             "numbers are by the time someone reads them."),
            ("point",
             "Circle one",
             "Pick the report that costs the most time and is read most often. That is your first"
             " BI candidate: the place where a simple BI setup would save the most time."),
            ("cta", "Read: Data Analytics Series, Part 1", "/blog/data-analytics-part-1-what-it-is/"),
            ("cta", "Read: Why I Built ALTOS", "/blog/why-i-built-altos/"),
            ("cta",
             "Read: The ALTOS Framework, Principle 9: Evidence Before Decision",
             "/blog/altos-framework-evidence-before-decision/"),
            ("ask", "Which report in your office would you most like to stop rebuilding by hand?"),
        ],
    },
]
