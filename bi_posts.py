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
        "title": "Business Intelligence Series, Part 40: The Closing Checklist, Forty Parts on One Page",
        "slug": "business-intelligence-part-40-closing-checklist",
        "category": "bi",
        "date": "May 25, 2027",
        "summary": "The last part of the Business Intelligence Series turns forty parts into one checklist to "
                   "run before any report or dashboard goes out, a map of where each topic was covered, and a "
                   "simple plan for the first month, quarter and year of treasury BI.",
        "publish_on": "2027-05-25 21:00",
        "body": [
            "The new analyst had read every part of this series, some twice. On her first Monday, the head of "
            "office handed her a dashboard that was due Friday and asked one question: “Is it ready to show the "
            "mayor?”",
            "She did not need to reread forty parts. She needed one page of questions she could answer yes or "
            "no, with each no pointing to the part that would fix it. That page is this final part.",
            "(The analyst and the office are invented. Each item points back to the part of the series that "
            "explains it, with its sources.)",
            "Part 39 traced a collection funnel step by step. This part steps back from single techniques to the "
            "whole series. By the end, you will have a closing checklist for any report or dashboard, a map of "
            "the series by topic, and a plan for building treasury BI over a year.",
            ("photo", "blog/bi-wrapup.jpg", "The closing checklist: the reader, the data, the numbers, the "
             "design and the upkeep, checked before any report or dashboard goes out. (Illustration: Butch "
             "Mahinay, aumahinay.dev)", "medium"),
            ("h", "The Closing Checklist"),
            "Answer each question yes or no. Every no has a part to go back to.",
            ("h", "1. The Reader"),
            ("point", "Do you know who will use it and for what decision?", "Part 4 started every project with "
             "the people, then the brief."),
            ("point", "Can the main finding be told in five minutes?", "Part 11 built the five-minute briefing."),
            ("point", "Does it read well on a phone?", "Part 12 kept dashboards fast and readable on small "
             "screens."),
            ("h", "2. The Data"),
            ("point", "Does every number trace back to its source?", "Part 7 moved data from the counter to the "
             "report, and Part 16 built a raw, clean and summary pipeline in Google Sheets."),
            ("point", "Were the pipeline’s checks run?", "Part 9 tested the pipeline before anyone saw a number."),
            ("point", "Is every measure defined in the data dictionary, with an owner?", "Part 10 kept BI honest "
             "with a dictionary, owners and a change log."),
            ("point", "Will last year’s numbers still be true after details change?", "Part 36 kept past reports "
             "true when a business moved to another barangay or a rate changed."),
            ("h", "3. The Numbers"),
            ("point", "Are comparisons fair?", "Part 19 compared this month with last month and last year, on "
             "equal terms."),
            ("point", "Are targets shown honestly?", "Part 33 warned about the year-to-date trap."),
            ("point", "Are trends shown without guessing?", "Part 24 used trend lines and moving averages."),
            ("point", "Do the bumps have explanations?", "Part 25 annotated charts with lines, bands and notes."),
            ("h", "4. The Design"),
            ("point", "Can everyone read the colors?", "Part 26 covered contrast, labels and the red-green trap."),
            ("point", "Can the reader ask the next question?", "Part 13 added filters and drill-down."),
            ("point", "Does it say when the data was last updated?", "Part 30 made freshness visible."),
            ("h", "5. The Upkeep"),
            ("point", "Does each viewer see only what they should?", "Part 17 shared dashboards without sharing "
             "too much, and Part 32 kept private data off public pages."),
            ("point", "Is anyone using it?", "Part 28 measured views and decisions."),
            ("point", "Is there a plan to retire it when it stops being useful?", "Part 29 turned off what "
             "nobody uses."),
            ("photo", "blog/bi-wrapup-map.jpg", "A map of the series by topic, from the BI team and the data "
             "model to the analyses near the end of the series. (Illustration: Butch Mahinay, aumahinay.dev)",
             "medium"),
            ("h", "A Map of the Series"),
            ("point", "Foundations", "Part 1 on what BI is for, Part 2 on the team, Part 3 on what a treasury "
             "should watch every day, and Part 4 on the brief."),
            ("point", "Data and models", "Parts 5, 6 and 15 on models and storage, Part 14 on the date table, "
             "and Parts 22 and 23 on calculated fields and blending."),
            ("point", "Reports and dashboards", "Part 8 on report or dashboard, Part 18 on alerts, Part 20 on a "
             "first live Data Studio dashboard, Part 27 on maps, and Part 31 on scheduled email delivery."),
            ("point", "Putting it together", "Part 21 on a treasury BI setup in four weeks."),
            ("point", "Analyses", "Part 34 on aging of arrears, Part 35 on small multiples, Part 37 on the "
             "Pareto chart, Part 38 on cohorts and Part 39 on the collection funnel."),
            ("h", "A Plan for the First Year"),
            ("point", "First month", "Write one brief, build one clean pipeline from the collection records, "
             "and publish one daily view with its update time. Part 3 suggested what a treasury should watch "
             "every day."),
            ("point", "First quarter", "Add the data dictionary, fair comparisons and one alert. Show it in a "
             "five-minute briefing, and ask what decision it helped."),
            ("point", "First year", "Add one deeper analysis each quarter, such as aging of arrears, a Pareto "
             "chart, cohorts or a funnel. Measure use, and retire what nobody opens."),
            "Part 21 laid out a four-week setup. This plan stretches the same steps over a year, so a small "
            "office can do them alongside its regular work.",
            ("h", "Back to Friday"),
            "The analyst ran the checklist on Tuesday. Three answers were no: the dashboard did not show its "
            "update time, two colors were hard to tell apart, and a total did not match the official report "
            "because a business that had moved was counted in two barangays.",
            "She fixed all three by Thursday. On Friday, the mayor asked why one barangay’s collections had "
            "dropped in March. The note on the chart already answered it.",
            ("h", "If You Read Reports Instead of Building Them"),
            "Not every reader of this series builds dashboards. Some simply receive them. Five questions help "
            "anyone judge a report someone else made.",
            ("point", "When was this updated?", "A number without a date may be months old."),
            ("point", "Compared with what?", "A total means little without last month, last year or a target "
             "beside it."),
            ("point", "Where does this number come from?", "The person who built the report should be able to "
             "say which records were counted."),
            ("point", "What is not included?", "Late postings, other funds or certain barangays may be left out "
             "on purpose. The report should say so."),
            ("point", "What should I do about it?", "A good report points to a decision, not only a fact."),
            "A builder who can answer all five on the spot has probably run the checklist above.",
            ("h", "What the Series Was Really About"),
            "Forty parts covered tools and charts, but the same idea ran through all of them: a number is only "
            "useful if the right person can trust it, understand it and act on it in time. Each part removed one "
            "reason a reader might not.",
            ("h", "Mistakes to Avoid"),
            ("point", "Building before asking", "Start with the reader and the decision."),
            ("point", "Publishing unchecked numbers", "Test the pipeline every time the data changes."),
            ("point", "Keeping everything forever", "Measure use and retire old reports."),
            ("point", "Hiding the date", "Every view should say when its data was last updated."),
            ("h", "Key Takeaways"),
            ("point", "Five areas to check", "The reader, the data, the numbers, the design and the upkeep."),
            ("point", "Every no has a fix", "The checklist points back to the part that explains it."),
            ("point", "Start small", "One brief, one pipeline and one daily view in the first month."),
            ("point", "Trust is the goal", "Right person, trusted number, understood, acted on in time."),
            ("h", "Your Final Exercise"),
            ("point", "Step 1", "Pick one report or dashboard your office already uses."),
            ("point", "Step 2", "Run the closing checklist and count the noes."),
            ("point", "Step 3", "Fix the easiest no this week and the hardest one this month."),
            ("point", "Step 4", "Print the checklist and keep it beside whoever builds the next report."),
            "Thank you for reading all forty parts of the Business Intelligence Series. The checklist is short "
            "on purpose. Run it before the next report leaves your desk, and every time after that.",
            ("cta", "Read: Business Intelligence Series, Part 21: Putting It Together, a Treasury BI Setup in Four Weeks", "/blog/business-intelligence-part-21-putting-it-together/"),
            ("cta", "Read: Business Intelligence Series, Part 4: Start With the People, Then Write the Brief", "/blog/business-intelligence-part-4-the-bi-brief/"),
            ("cta", "Read: Business Intelligence Series, Part 10: Keeping BI Honest With a Data Dictionary, Owners and a Change Log", "/blog/business-intelligence-part-10-keeping-bi-honest/"),
            ("cta", "Read: Business Intelligence Series, Part 28: Is Anyone Using the Dashboard? Measuring Views and Decisions", "/blog/business-intelligence-part-28-dashboard-usage/"),
            ("ask", "Which question on the checklist would your office’s main report fail first?"),
        ],
    },
    {
        "title": "Business Intelligence Series, Part 39: The Collection Funnel, Finding the Step Where Money Is Lost",
        "slug": "business-intelligence-part-39-collection-funnel",
        "category": "bi",
        "date": "May 20, 2027",
        "summary": "A collection rate tells you how much was collected, but not where the rest was lost. A funnel "
                   "counts the accounts at each step, from assessed to billed to paid, so the weakest step stands "
                   "out. This part explains how to build a collection funnel in Google Sheets and how to read it.",
        "publish_on": "2027-05-20 21:00",
        "body": [
            "The real property tax collection rate had stalled at about half of the accounts on the roll. The "
            "office tried the usual fix: a second round of reminder letters to every unpaid account. The rate "
            "barely moved.",
            "A clerk in the records section finally asked the question nobody had asked: “How many of those "
            "owners ever got the first bill?” Nobody knew. The report showed only the start and the end of the "
            "process, and the problem was hiding in the middle.",
            "(The office, the counts and the barangays are invented for this lesson. The method, the chart types "
            "and the formulas are real.)",
            "Part 38 followed groups of businesses over the years. This part follows accounts through the steps "
            "of a single process. Once you finish, you will know what a funnel is, how to count each step "
            "fairly, how to build a funnel table and chart in Google Sheets, how to read step rates, and how to "
            "turn the weakest step into a plan.",
            ("photo", "blog/bi-funnel.jpg", "The collection funnel: count the accounts at each step, from "
             "assessed to billed to paid, and the step that loses the most stands out. (Illustration: Butch "
             "Mahinay, aumahinay.dev)", "medium"),
            ("h", "What a Funnel Is"),
            "Microsoft’s Excel help says simply that funnel charts show values across multiple stages in a "
            "process. Google’s Analytics help describes its funnel exploration as a way to visualize the steps "
            "users take to complete a task and to see how well they are succeeding or failing at each step.",
            "Websites use funnels to see where visitors give up before buying. A treasury can use the same idea "
            "for any process with steps in a fixed order, where some accounts drop out along the way.",
            ("h", "The Four Steps in This Example"),
            ("point", "Assessed", "Accounts on the assessment roll for the year: 12,000."),
            ("point", "Bill delivered", "Accounts whose billing notice reached the owner, confirmed by a "
             "signed receipt or a delivery log: 8,400."),
            ("point", "Paid any amount", "Accounts with at least one payment during the year: 7,140."),
            ("point", "Paid in full", "Accounts with nothing left unpaid for the year: 6,426."),
            "The overall rate is 6,426 out of 12,000, or 53.6 percent. That was the only number the old report "
            "showed.",
            ("h", "Step Rates Tell the Real Story"),
            "A funnel adds two numbers to each step: the share of the starting count that is still there, and "
            "the share of the step just before.",
            ("point", "Assessed to delivered", "8,400 out of 12,000, or 70 percent. 3,600 accounts lost."),
            ("point", "Delivered to paid any amount", "7,140 out of 8,400, or 85 percent. 1,260 lost."),
            ("point", "Paid any amount to paid in full", "6,426 out of 7,140, or 90 percent. 714 lost."),
            "The weakest step was not payment at all. It was delivery. Nearly a third of the owners never "
            "received a bill, and the second round of reminder letters went out by the same route as the "
            "first.",
            ("photo", "blog/bi-funnel-steps.jpg", "The same funnel as a table: count, share of the start, share "
             "of the previous step and accounts lost at each step. The delivery step loses the most. Figures "
             "are invented. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Building the Funnel Table in Google Sheets"),
            ("point", "Step 1: One row per step, in order", "Put the step names in column A, from A2 to A5, "
             "starting with Assessed."),
            ("point", "Step 2: Count each step", "In column B, count the accounts. If your account list has a "
             "column for each step marked Yes or No, a formula such as =COUNTIF(Accounts!D:D, \"Yes\") counts "
             "the delivered bills."),
            ("point", "Step 3: Share of the start", "In C2, type =B2/$B$2 and copy it down. Format the column as "
             "a percentage."),
            ("point", "Step 4: Share of the previous step", "In D3, type =B3/B2 and copy it down. Leave D2 "
             "blank, since the first step has nothing before it."),
            ("point", "Step 5: Accounts lost", "In E3, type =B2-B3 and copy it down. The largest number in "
             "column E points to the weakest step."),
            ("point", "Step 6: Chart it", "Select columns A and B and insert a bar chart. Keep the rows in "
             "process order, never sorted by size, because the order is the point."),
            "If you work in Excel, Microsoft lists a Funnel chart type under Insert in Office 2021 and Microsoft "
            "365. A plain bar chart in process order tells the same story in either program.",
            ("h", "Counting Each Step Fairly"),
            "A funnel is only honest if every step counts the same thing over the same period.",
            ("point", "Same unit", "Count accounts at every step, not accounts at one step and owners or "
             "receipts at another."),
            ("point", "Same group", "Each step should hold only accounts that passed the step before. An "
             "account paid without a delivered bill, perhaps by an owner who walked in, should be noted "
             "separately so the steps still add up."),
            ("point", "Same period", "Use one tax year for every step. Mixing this year’s bills with last "
             "year’s payments produces rates that mean nothing."),
            ("h", "Splitting the Funnel by Barangay"),
            "One funnel for the whole local government shows the weakest step. Splitting it by barangay shows "
            "where that step is weakest. In this example, two remote barangays had delivery rates near 40 "
            "percent, while the poblacion was above 85 percent. The billing notices for the remote areas "
            "went out with addresses that had not been updated in years.",
            "Part 35 showed how small multiples put one chart per barangay side by side. The same layout works "
            "for funnels.",
            ("h", "Keeping the Funnel Current"),
            "A funnel built once at year-end tells you what went wrong after it is too late to fix. Built every "
            "month, it shows the weak step while there is still time to act.",
            ("point", "Refresh monthly", "Recount each step on the same day each month, from the same account "
             "list."),
            ("point", "Keep last year beside it", "Show last year’s step rates in a column next to this year’s, "
             "so a drop is easy to spot."),
            ("point", "Show the date", "Part 30 explained why every report should say when its data was last "
             "updated. A funnel is no different."),
            "A monthly funnel also shows whether a fix worked. If delivery rises after addresses are updated "
            "but payment does not follow, the next step needs attention.",
            ("h", "Back to the Reminder Letters"),
            "The office stopped sending second letters to every unpaid account. Instead, it spent two months "
            "updating owner addresses for the two weakest barangays, with help from the barangay offices, and "
            "redelivered the notices. Delivery for those areas rose, and so did payments.",
            "The funnel did not collect a single peso. It showed where to spend the effort.",
            ("h", "Mistakes to Avoid"),
            ("point", "Reporting only the overall rate", "It shows that money is lost, not where."),
            ("point", "Sorting the steps by size", "A funnel must stay in process order."),
            ("point", "Counting different things at each step", "Accounts, owners and receipts do not mix."),
            ("point", "Fixing the last step first", "The largest loss may be early in the process."),
            ("h", "Key Takeaways"),
            ("point", "A funnel counts each step", "From assessed to billed to paid, in order."),
            ("point", "Step rates find the weak point", "Compare each step with the one before it."),
            ("point", "Accounts lost guide the effort", "Start with the step that loses the most."),
            ("point", "Split by area", "The same funnel by barangay shows where the weak step is weakest."),
            ("h", "Your Part 39 Exercise"),
            "List the steps of one process your office runs, such as real property tax billing or business "
            "permit renewal. Count the accounts at each step for one year, build the five-column table above, "
            "and circle the step with the largest number of accounts lost. Then ask the people who handle that "
            "step what gets in the way.",
            ("cta", "Read: Business Intelligence Series, Part 37: The Pareto Chart, Finding the Few Causes Behind Most of a Problem", "/blog/business-intelligence-part-37-pareto-chart/"),
            ("cta", "Read: Business Intelligence Series, Part 35: Small Multiples, One Small Chart per Barangay", "/blog/business-intelligence-part-35-small-multiples/"),
            ("cta", "Read: Business Intelligence Series, Part 33: Targets vs Actual, Bullet Charts, Gauges and the Year-to-Date Trap", "/blog/business-intelligence-part-33-targets-vs-actual/"),
            ("cta", "Read: Data Analytics Series, Part 30: Percent Change or Percentage Points? Reporting Growth Without Confusion", "/blog/data-analytics-part-30-percent-change/"),
            ("ask", "Which step in your office’s collection process do you think loses the most accounts?"),
        ],
    },
    {
        "title": "Business Intelligence Series, Part 38: Cohorts, Do New Businesses Keep Renewing?",
        "slug": "business-intelligence-part-38-cohorts",
        "category": "bi",
        "date": "May 15, 2027",
        "summary": "Total renewals can rise while each new group of businesses renews less than the one before. "
                   "A cohort table follows each year’s new businesses separately, so the change is visible early. "
                   "This part explains what a cohort is, how to build a cohort table in Google Sheets, and how to "
                   "read it.",
        "publish_on": "2027-05-15 21:00",
        "body": [
            "The year-end report looked healthy. Business permit renewals had grown for the third year in a "
            "row. The head of office was ready to sign it when a clerk at the renewal window said something "
            "that did not fit: “A lot of the new ones from last year did not come back this January.”",
            "Both statements were true. The total was rising because more new businesses registered each year. "
            "Underneath it, a smaller share of each new group was returning. Only a cohort table could show both "
            "at once.",
            "(The office, the businesses and the counts are invented for this lesson. The method and the Google "
            "Sheets formulas are real.)",
            "Part 37 sorted causes from biggest to smallest. This part follows groups over time. When you "
            "finish reading, you will know what a cohort is, why totals can hide a decline, how to build a "
            "cohort table in Google Sheets from a list of payments, how to read it, and what to do with what "
            "it shows.",
            ("photo", "blog/bi-cohorts.jpg", "Cohorts: group businesses by the year they first registered, then "
             "follow what share of each group renews in each later year. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "What a Cohort Is"),
            "Google’s Analytics help describes a cohort as a group of users who share a common characteristic, "
            "and a cohort report as a way to explore the behavior of these groups over time. In a treasury, the "
            "users are taxpayers, and one useful shared characteristic is the year they started.",
            ("point", "The 2024 cohort", "All businesses that registered for the first time in 2024."),
            ("point", "Retention", "The share of a cohort still renewing in a later year."),
            ("point", "Year 1, Year 2", "Years since the cohort started, so different cohorts can be compared "
             "side by side."),
            ("h", "Why Totals Hide the Story"),
            "Total renewals mix old and new businesses. If more new businesses register each year, the total "
            "can rise even while fewer of each group stay. By the time the total finally falls, the decline has "
            "been running for years.",
            ("h", "The Example"),
            ("point", "2023 cohort", "120 new businesses. Renewed: 96 in 2024, 84 in 2025, 78 in 2026."),
            ("point", "2024 cohort", "140 new businesses. Renewed: 105 in 2025, 91 in 2026."),
            ("point", "2025 cohort", "150 new businesses. Renewed: 99 in 2026."),
            "Turned into percentages of each cohort’s starting size:",
            ("point", "Year 1 retention", "2023: 80%. 2024: 75%. 2025: 66%."),
            ("point", "Year 2 retention", "2023: 70%. 2024: 65%."),
            ("point", "Year 3 retention", "2023: 65%."),
            "Each new cohort keeps fewer of its businesses after the first year. The clerk was right.",
            ("photo", "blog/bi-cohorts-table.jpg", "The cohort table: one row per starting year, one column per "
             "year since registration, and the share still renewing in each cell. Figures are invented. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Building It in Google Sheets"),
            "Start with a Payments tab that has one row per business per year paid: column A the business ID, "
            "column B the year. If a business paid in installments, keep one row per year, for example with "
            "UNIQUE from Part 33 of the Data Analytics Series.",
            ("point", "Step 1: First year", "On a Businesses tab, list each ID once in column A. In B2, enter "
             "=MINIFS(Payments!B:B, Payments!A:A, A2) to find the first year that business paid."),
            ("point", "Step 2: Tag each payment", "Back on Payments, in C2, enter =XLOOKUP(A2, Businesses!A:A, "
             "Businesses!B:B) and fill down. Each payment now carries its cohort year. Part 25 of the Data "
             "Analytics Series covered XLOOKUP."),
            ("point", "Step 3: Cohort sizes", "On a Cohorts tab, put the cohort years in A2:A4. In B2, enter "
             "=COUNTIF(Businesses!B:B, A2)."),
            ("point", "Step 4: Renewals by year", "Put calendar years across row 1 from C1. In C2, enter "
             "=COUNTIFS(Payments!C:C, $A2, Payments!B:B, C$1) and fill across and down."),
            ("point", "Step 5: Percentages", "In a second block, divide each count by the cohort size in column "
             "B, and format as percent."),
            ("point", "Step 6: Shift to years since start", "Rearrange so the first column after the size is "
             "Year 1 for every cohort. Now each column compares cohorts at the same age."),
            ("h", "Reading a Cohort Table"),
            ("point", "Read down a column", "Year 1 for each cohort in turn: 80, 75, 66. A falling column means "
             "newer cohorts are doing worse at the same age."),
            ("point", "Read across a row", "One cohort over time: 80, 70, 65. Look for the "
             "steepest drop first, since it shows when a group is most likely to stop renewing."),
            ("point", "Watch the newest row", "It has the fewest years, but it shows the latest change first."),
            ("point", "Mind the size", "A cohort of 12 can swing widely by chance. Show the count beside each "
             "percentage."),
            ("h", "Asking Why"),
            "A cohort table shows where to look. It does not say why. In the example, the office checked the "
            "2025 cohort that did not renew.",
            ("point", "Closed without notice", "Some had simply stopped operating. Part 14 of Inside the Local "
             "Treasury explains how proper closure keeps the records clean."),
            ("point", "Moved", "Some had moved to another barangay or municipality. Part 36 showed how to keep a "
             "business’s history when its details change."),
            ("point", "Did not know", "Some first-year owners did not know a renewal was due every January."),
            "The last group was the one the office could reach. Part 37’s Pareto chart could rank these "
            "reasons once they are counted.",
            ("h", "Putting It on the Dashboard"),
            "A cohort table is dense. On a dashboard, two simpler views carry most of its message.",
            ("point", "One line per cohort", "A line chart with years since start along the bottom and the "
             "retention percentage up the side. Newer cohorts that sit lower are easy to spot."),
            ("point", "A single Year 1 figure", "The latest cohort’s Year 1 retention, beside the figure for "
             "the cohort before it, as a fair comparison of the kind Part 19 described."),
            ("point", "The full table on request", "Keep the complete table one click away for anyone who "
             "wants the detail."),
            "Update it once a year, after the renewal period closes, so every cohort is measured at the same "
            "point in the calendar.",
            ("h", "Other Cohorts Worth Building"),
            ("point", "Property owners by year of first payment", "Do new owners keep paying the amilyar on "
             "time?"),
            ("point", "Stallholders by year of contract", "How many are still in the market after two years?"),
            ("point", "Taxpayers by first payment channel", "Do those who started online renew more than those "
             "who started at the counter?"),
            ("h", "Mistakes to Avoid"),
            ("point", "Watching only totals", "Growth in new registrations can hide falling retention."),
            ("point", "Comparing by calendar year", "Compare cohorts at the same age, Year 1 with Year 1."),
            ("point", "Ignoring cohort size", "Show the counts beside the percentages."),
            ("point", "Stopping at the table", "Ask why, and test a fix."),
            ("h", "Key Takeaways"),
            ("point", "A cohort is a starting group", "Here, businesses by year of first registration."),
            ("point", "Retention by age", "Share still renewing in Year 1, Year 2 and onward."),
            ("point", "Three formulas", "MINIFS for the first year, XLOOKUP to tag, COUNTIFS to count."),
            ("point", "Read down the columns", "That is where a decline appears first."),
            ("h", "Your Part 38 Exercise"),
            ("point", "Step 1", "Make a Payments tab with 20 invented businesses over three years."),
            ("point", "Step 2", "Build the cohort sizes and renewal counts with the formulas above."),
            ("point", "Step 3", "Convert to percentages and arrange by years since start."),
            ("point", "Step 4", "Write one sentence about Year 1 retention across cohorts."),
            "The office added a simple step for every new business: a text and a call in December of its "
            "first year, reminding the owner that renewal is due in January. The 2026 cohort’s Year 1 figure "
            "would show whether it worked, and the cohort table was ready to tell them.",
            ("cta", "Read: Business Intelligence Series, Part 19: Fair Comparisons, This Month, Last Month and Last Year", "/blog/business-intelligence-part-19-fair-comparisons/"),
            ("cta", "Read: Business Intelligence Series, Part 36: When Details Change, Keeping Last Year’s Report True", "/blog/business-intelligence-part-36-changes-over-time/"),
            ("cta", "Read: Business Intelligence Series, Part 34: Aging of Arrears, Sorting Unpaid Accounts by How Long They Have Waited", "/blog/business-intelligence-part-34-aging-of-arrears/"),
            ("cta", "Read: Data Analytics Series, Part 25: XLOOKUP, Bringing the Right Detail Into Every Row", "/blog/data-analytics-part-25-xlookup/"),
            ("ask", "Of the businesses that registered in your area last year, how many do you think will renew?"),
        ],
    },
    {
        "title": "Business Intelligence Series, Part 37: The Pareto Chart, Finding the Few Causes Behind Most of a Problem",
        "slug": "business-intelligence-part-37-pareto-chart",
        "category": "bi",
        "date": "May 10, 2027",
        "summary": "When a problem has many causes, a few of them may deserve attention first. A Pareto "
                   "chart sorts the causes from biggest to smallest and adds a running total, so the office can "
                   "see which ones to fix. This part explains where the idea came from, how to build the chart "
                   "in Google Sheets, and how to read it without overstating the 80/20 rule.",
        "publish_on": "2027-05-10 21:00",
        "body": [
            "In the first quarter, the business permit counter turned back 300 applications. Each one meant a "
            "taxpayer going home, finding a missing paper, and lining up again. The staff had a list of reasons "
            "for every rejection, eight of them, and a long meeting about all eight.",
            "Then someone sorted the list and added one column. The meeting got much shorter.",
            "(The counter, the reasons and the counts are a made-up example for this lesson. The chart, its "
            "history and the Google Sheets steps are real.)",
            "Part 36 kept old reports true when details change. This part is about deciding where to start when "
            "a problem has many causes. Read to the end, and you will know where the Pareto idea came from, how "
            "to build a Pareto chart in Google Sheets, how to read it, and the mistakes that turn a useful chart "
            "into a slogan.",
            ("photo", "blog/bi-pareto.jpg", "The Pareto idea: sort the causes from biggest to smallest, add a "
             "running total, and see which few explain most of the problem. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "Where the Idea Came From"),
            "The Clinical Excellence Commission of New South Wales, Australia, explains the history in its "
            "quality improvement tools. Joseph Juran, a quality management expert, suggested the principle and "
            "named it after the Italian economist Vilfredo Pareto, who noted the 80/20 connection in 1896. "
            "Pareto had shown that approximately 80 percent of the land in Italy was owned by 20 percent of the "
            "population.",
            "The Commission states the principle as: for many events, roughly 80 percent of the effects come "
            "from 20 percent of the causes. It also calls it “the law of the vital few & trivial many.”",
            ("quote", "The point is not the numbers 80 and 20. The point is that causes are not equal in size, so "
             "they should not get equal attention."),
            ("h", "What a Pareto Chart Shows"),
            "The Commission describes the chart in two parts.",
            ("point", "Bars", "Individual values are shown as bars in descending order, biggest on the left."),
            ("point", "A line", "The cumulative total is shown as a line rising across the chart to 100 "
             "percent."),
            ("point", "An optional cut-off", "A line at 80 percent marks where the running total crosses that "
             "level. Causes to its left are the vital few."),
            ("h", "The Counter’s Data"),
            "Here are the 300 rejections by reason, already sorted from most to least.",
            ("point", "Missing barangay clearance", "112 (37.3%, running total 37.3%)"),
            ("point", "Form not signed", "68 (22.7%, running total 60.0%)"),
            ("point", "Lease contract missing or expired", "41 (13.7%, running total 73.7%)"),
            ("point", "Gross sales not supported", "27 (9.0%, running total 82.7%)"),
            ("point", "Missing community tax certificate", "18 (6.0%, running total 88.7%)"),
            ("point", "Missing sanitary permit", "15 (5.0%, running total 93.7%)"),
            ("point", "Old balance unpaid", "11 (3.7%, running total 97.3%)"),
            ("point", "Other", "8 (2.7%, running total 100.0%)"),
            "Two reasons explain 60 percent of the rejections. Four explain about 83 percent. Notice that four "
            "of eight causes is half, not 20 percent. Real data need not land exactly on 80/20, and it does not "
            "need to. What matters is that the top two are worth fixing first.",
            ("photo", "blog/bi-pareto-chart.jpg", "A Pareto chart of the 300 rejections: sorted bars, a "
             "running-total line, and an 80 percent cut-off. (Illustration: Butch Mahinay, aumahinay.dev)",
             "medium"),
            ("h", "Building It in Google Sheets"),
            "Start with a tab named Reasons. Column A holds each reason, and column B holds its count, in any "
            "order.",
            ("point", "Step 1: Sort", "In D2, enter =SORT(A2:B9, 2, FALSE). This copies the list sorted by "
             "count, largest first, into columns D and E. Part 33 of the Data Analytics series covered SORT."),
            ("point", "Step 2: Share", "In F2, enter =E2/SUM($E$2:$E$9) and fill down. Format as percent."),
            ("point", "Step 3: Running total", "In G2, enter =SUM($E$2:E2)/SUM($E$2:$E$9) and fill down. The "
             "first $E$2 stays fixed while the second E2 moves, so each row adds everything above it. The "
             "last row should show 100%."),
            ("point", "Step 4: The chart", "Select D1:E9 and G1:G9, then Insert, Chart. In the chart editor, "
             "choose Combo chart."),
            ("point", "Step 5: Two axes", "Under Customize, Series, pick the running total series and set "
             "its axis to Right axis. Set it to show as a line and the counts as columns."),
            ("point", "Step 6: Label it", "Give the chart a title that states the finding, such as “Two "
             "reasons explain 60% of rejections.”"),
            "If the reasons come from a log of individual rejections rather than a ready count, build column B "
            "with =COUNTIF(Log!C:C, A2), where column C of the Log tab holds the reason.",
            ("h", "Reading the Chart Well"),
            ("point", "Look where the line bends", "The steep part of the line is where each bar adds a lot. "
             "Where it flattens, extra causes add little."),
            ("point", "Keep “Other” last", "In this example we placed “Other” at the end even if it were "
             "large, since it is a mix of causes, not one cause to fix."),
            ("point", "Check the unit", "Counting rejections treats a small error and a costly one the same. "
             "If some causes take far longer to fix, a second chart by hours lost may rank them differently."),
            ("point", "Redo it after changes", "A Pareto chart is a snapshot. After the top causes are fixed, "
             "the order will change."),
            ("h", "Where a Pareto Chart Helps in a Treasury"),
            "The chart fits any problem that can be counted by cause. A few treasury examples:",
            ("point", "Corrected receipts", "Count cancelled or corrected official receipts by reason: wrong "
             "amount, wrong name, wrong account code."),
            ("point", "Taxpayer complaints", "Count complaints by subject, such as long lines, unclear "
             "assessments or missing notices."),
            ("point", "Late deposits", "Count the days a collection was deposited late by cause: no vehicle, "
             "bank cut-off missed, collector out."),
            ("point", "Arrears by account", "Part 34 sorted arrears by age. A Pareto chart sorts them by size, "
             "showing whether a handful of accounts hold most of the balance."),
            "It fits less well when there is one cause, or when the causes cannot be counted the same way. A "
            "chart is only as honest as the reason codes behind it, so agree on the list of reasons before "
            "staff start logging them.",
            ("h", "What the Counter Did"),
            ("point", "For barangay clearance", "The renewal notice now lists the clearance first, in bold, "
             "with the barangay hall hours."),
            ("point", "For unsigned forms", "The intake clerk checks every signature line before the "
             "application is logged."),
            "In the example, the next quarter’s chart showed 170 rejections, and the two former leaders had "
            "dropped to the middle. Lease contracts were now on top, and that became the next fix.",
            ("h", "Mistakes to Avoid"),
            ("point", "Treating 80/20 as a law of nature", "It is a rough pattern, not a promise."),
            ("point", "Leaving bars unsorted", "Without the order, it is just a bar chart."),
            ("point", "Fixing everything at once", "Start with the vital few and measure again."),
            ("point", "Ignoring cost", "A rare cause can still be the most expensive one."),
            ("h", "Key Takeaways"),
            ("point", "Causes differ in size", "A few can explain most of a problem."),
            ("point", "Two parts", "Bars from biggest to smallest, plus a running-total line."),
            ("point", "Built in minutes", "SORT, a running SUM and a combo chart with a right axis."),
            ("point", "A starting point", "Fix the top causes, then build the chart again."),
            ("h", "Your Part 37 Exercise"),
            ("point", "Step 1", "Pick one problem your office counts, such as returned forms, complaints or "
             "corrected receipts."),
            ("point", "Step 2", "List at least six reasons with a count for each from last quarter."),
            ("point", "Step 3", "Build the Pareto chart with the steps above."),
            ("point", "Step 4", "Write one sentence naming the top two causes and one action for each."),
            "The counter staff still keep all eight reasons on file. They just stopped discussing all eight at "
            "every meeting.",
            ("cta", "Read: Business Intelligence Series, Part 11: The Five-Minute Briefing for Decision Makers", "/blog/business-intelligence-part-11-five-minute-briefing/"),
            ("cta", "Read: Business Intelligence Series, Part 13: Filters and Drill-Down, Letting Readers Ask the Next Question", "/blog/business-intelligence-part-13-filters-and-drill-down/"),
            ("cta", "Read: Business Intelligence Series, Part 34: Aging of Arrears, Sorting Unpaid Accounts by How Long They Have Waited", "/blog/business-intelligence-part-34-aging-of-arrears/"),
            ("cta", "Read: Data Analytics Series, Part 33: FILTER, SORT and UNIQUE, Lists in Google Sheets That Update Themselves", "/blog/data-analytics-part-33-filter-sort-unique/"),
            ("ask", "Which problem in your office would you put on a Pareto chart first?"),
        ],
    },
    {
        "title": "Business Intelligence Series, Part 36: When Details Change, Keeping Last Year’s Report True",
        "slug": "business-intelligence-part-36-changes-over-time",
        "category": "bi",
        "date": "May 5, 2027",
        "summary": "A business moves to another barangay, a collector changes routes, a fee schedule is "
                   "revised. If the dashboard simply overwrites the old detail, last year’s numbers change "
                   "without anyone noticing. This part explains the three common ways to handle changes in a "
                   "dimension table and how to build the safest one in Google Sheets.",
        "publish_on": "2027-05-05 21:00",
        "body": [
            "The 2026 collections report had been approved in January. Malinao collected ₱1.42 million in "
            "business taxes that year. In April, someone printed the same report again for a meeting, and "
            "Malinao showed ₱1.31 million.",
            "Nobody had touched a single 2026 payment. What changed was one row in the business list: a "
            "hardware store had moved from Malinao to the poblacion in March 2027, and the clerk updated its "
            "barangay. The dashboard now credited all of the store’s past payments to its new address.",
            "(The office, the store and the figures are invented for this lesson. The design approach named "
            "below is real.)",
            "Part 35 split one crowded chart into many small ones. This part goes back to the data model. When "
            "you finish reading, you will know why changing details can rewrite history, the three main ways "
            "to handle them, how to choose between them, and how to keep a dated history in Google Sheets.",
            ("photo", "blog/bi-history.jpg", "Changes over time: when a detail changes, overwrite it, keep the "
             "original, or add a new dated row so old reports stay true. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "Why This Happens"),
            "Part 5 split data into facts and dimensions. Facts are events: a payment of ₱8,500 on a date. "
            "Dimensions describe them: which business, which barangay, which collector.",
            "Facts rarely change once recorded. Dimensions do. Businesses move, rename, change owners or "
            "switch lines of business. Collectors are reassigned. When the dashboard joins every payment to "
            "the current version of the business, every past payment takes on today’s details.",
            ("point", "Sometimes that is right", "If a business name was simply misspelled, fixing it "
             "everywhere is what you want."),
            ("point", "Sometimes it is wrong", "If the business really moved, its 2026 payments were made "
             "from Malinao and should stay there."),
            ("h", "Three Ways to Handle a Change"),
            "Data warehouse designers call these slowly changing dimensions. The Kimball Group, known for "
            "its work on dimensional modeling, numbers the approaches as types. A 2013 design tip by Margy Ross "
            "lists them from Type 0 upward. Three are enough for the examples here.",
            ("point", "Type 0: keep the original", "The value never changes after it is first recorded. Good "
             "for details that should stay fixed, such as the date a business first registered."),
            ("point", "Type 1: overwrite", "Replace the old value with the new one. History is lost, and old "
             "reports change. Good for corrections, such as a misspelled name."),
            ("point", "Type 2: add a new row", "Close the old row with an end date and add a new row with a "
             "start date. Old payments stay linked to the old details, and new payments to the new ones."),
            "There are more types, but these three are enough to make the right choice for each column.",
            ("h", "Choosing for Each Column"),
            "Decide column by column, and write the choice in the data dictionary from Part 10.",
            ("point", "Business name", "Type 1 for spelling fixes. A real change of name may deserve Type 2."),
            ("point", "Barangay", "Type 2. Collections by barangay must stay true for past years."),
            ("point", "Line of business", "Type 2, because the business tax schedule depends on it."),
            ("point", "Date first registered", "Type 0. It should never change."),
            ("point", "Contact number", "Type 1. Only the latest number matters."),
            ("point", "Assigned collector", "Type 2 if you report collections by collector, so last year’s "
             "results stay with the person who earned them."),
            ("photo", "blog/bi-history-rows.jpg", "One business, two rows: the old address closed on March "
             "14, 2027, and the new one starts on March 15. Payments find the row that was true on their "
             "date. Figures are invented. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Building Type 2 in Google Sheets"),
            "Start with a Businesses tab that has these columns: A business ID, B name, C barangay, D valid "
            "from, E valid to, and F current.",
            ("point", "Before the move", "One row: B-0417, Santos Hardware, Malinao, January 1, 2020, blank, "
             "Yes."),
            ("point", "Close the old row", "Change E to March 14, 2027, and F to No."),
            ("point", "Add the new row", "B-0417, Santos Hardware, Poblacion, March 15, 2027, blank, Yes."),
            "The business ID stays the same. The two rows share it, and the dates decide which one applies.",
            ("h", "Finding the Right Row for Each Payment"),
            "In the Payments tab, column A is the payment date and column B the business ID. In column C, "
            "find the barangay that was true on the payment date:",
            ("point", "Formula", "=INDEX(FILTER(Businesses!C:C, Businesses!A:A=B2, Businesses!D:D<=A2, "
             "(Businesses!E:E>=A2)+(Businesses!E:E=\"\")), 1)"),
            ("point", "Read it in parts", "Same business ID. Valid from on or before the payment date. Valid "
             "to on or after it, or still blank. INDEX takes the first match."),
            ("point", "Check it", "A payment dated June 2026 returns Malinao. A payment dated April 2027 "
             "returns Poblacion."),
            "Part 33 of the Data Analytics Series explained FILTER, and Part 14 of this series built the date "
            "table that keeps payment dates clean.",
            ("h", "The Same Idea for Rates"),
            "Changes are not only about businesses. When the revenue code revises a fee or a rate, the old "
            "rate still applies to bills from before the change.",
            ("point", "Keep a Rates tab", "One row per rate, with the item, the amount, valid from and valid "
             "to. Never type over an old rate."),
            ("point", "Look up by date", "Use the same FILTER pattern, matching the item and the bill date, so "
             "a 2026 bill finds the 2026 rate."),
            ("point", "Explain the jump", "When a chart shows a step up in collections at the start of a year, "
             "the Rates tab shows whether a new rate, and not more taxpayers, caused it. Part 25 showed how to "
             "annotate that on the chart."),
            ("h", "When Type 2 Is Too Much"),
            "Not every column needs history. Each extra row is one more thing to check. If nobody will ever "
            "report by a column over time, such as a contact person’s name, overwrite it and keep the table "
            "simple.",
            ("h", "Rules That Keep It Honest"),
            ("point", "No gaps, no overlaps", "Each new row starts the day after the old one ends. Two rows "
             "valid on the same day would double a payment."),
            ("point", "Only one current row", "Each business ID has exactly one row marked Yes. A COUNTIFS "
             "check can flag any ID with two."),
            ("point", "Record why", "Add a column for the reason: moved, renamed, corrected. Part 10’s change "
             "log idea applies here too."),
            ("point", "Corrections stay Type 1", "If Malinao was entered by mistake from the start, fix the "
             "row. Do not add a new one."),
            ("h", "Mistakes to Avoid"),
            ("point", "Overwriting every change", "Old reports will quietly change."),
            ("point", "Adding rows for typos", "Corrections are not history."),
            ("point", "Leaving gaps or overlaps in dates", "Payments will be lost or counted twice."),
            ("point", "Deciding without writing it down", "Record the type for each column."),
            ("h", "Key Takeaways"),
            ("point", "Facts stay, dimensions change", "And the join can rewrite history."),
            ("point", "Three choices", "Keep the original, overwrite, or add a dated row."),
            ("point", "Type 2 for history that matters", "Barangay, line of business."),
            ("point", "Dates decide the row", "FILTER on valid from and valid to."),
            ("h", "Your Part 36 Exercise"),
            ("point", "Step 1", "Build a Businesses tab with five businesses and the six columns above."),
            ("point", "Step 2", "Move one business to another barangay using Type 2."),
            ("point", "Step 3", "Add ten payments across both years and use the formula to find each "
             "barangay."),
            ("point", "Step 4", "Total collections by barangay for 2026. The total should not change after "
             "the move."),
            "After the fix, the 2026 report showed Malinao at ₱1.42 million again, matching the approved "
            "version. The reprinted copy from April was shredded, and the data dictionary gained a new line: "
            "“Barangay: Type 2, keep history.”",
            ("cta", "Read: Business Intelligence Series, Part 5: Data Modeling 101, Facts, Dimensions and the Star", "/blog/business-intelligence-part-5-data-modeling/"),
            ("cta", "Read: Business Intelligence Series, Part 10: Keeping BI Honest With a Data Dictionary, Owners and a Change Log", "/blog/business-intelligence-part-10-keeping-bi-honest/"),
            ("cta", "Read: Business Intelligence Series, Part 25: Annotating Charts, Lines, Bands and Notes That Explain the Bumps", "/blog/business-intelligence-part-25-annotating-charts/"),
            ("cta", "Read: Data Analytics Series, Part 33: FILTER, SORT and UNIQUE, Lists in Google Sheets That Update Themselves", "/blog/data-analytics-part-33-filter-sort-unique/"),
            ("ask", "When a business moves in your records, do last year’s reports change too?"),
        ],
    },
    {
        "title": "Business Intelligence Series, Part 35: Small Multiples, One Small Chart per Barangay",
        "slug": "business-intelligence-part-35-small-multiples",
        "category": "bi",
        "date": "April 30, 2027",
        "summary": "Six barangays on one line chart turn into a tangle. This part shows how to split them "
                   "into a grid of small, matching charts, why the charts should share one scale, when they "
                   "should not, and two ways to build the grid in Google Sheets.",
        "publish_on": "2027-04-30 21:00",
        "body": [
            "The analyst put six barangays on one line chart, one colored line each, and sent it to the "
            "council in time for the half-year review. One line ran across the top. The other five crowded "
            "together in the lower third, crossing and recrossing. Someone asked what happened in Malinao in "
            "April. Nobody could find Malinao.",
            "The answer was on the chart. It was lost among five other lines.",
            "(The barangays’ figures, the analyst and the meeting are invented for this lesson. The Google "
            "Sheets features and the book mentioned below are real.)",
            "Part 34 grouped unpaid accounts by age. This part takes on a different problem: too many "
            "series in one chart. You will learn what small multiples are, how to set them up so they can "
            "be compared, why a shared scale matters, when to break that rule, and two ways to build them "
            "in Google Sheets.",
            ("photo", "blog/bi-multiples.jpg", "Small multiples: split one crowded chart into a grid of "
             "small matching charts, one per barangay, on the same scale. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "What Small Multiples Are"),
            "A small multiple is a set of small charts of the same type, one for each group, arranged in a "
            "grid. Each chart uses the same measure, the same time period and the same layout. Only the "
            "data changes from one to the next.",
            "Edward Tufte, an American statistician and author, wrote about the idea in his 1990 book "
            "Envisioning Information. Data visualization guides still use the term today.",
            ("point", "One chart per group", "Six barangays, six charts. Each line has a box to itself."),
            ("point", "Same design everywhere", "Once a reader learns how to read one chart, they can read "
             "all of them."),
            ("point", "The comparison is the point", "The eye moves across the grid and spots the chart "
             "that looks different."),
            ("h", "Why One Crowded Chart Fails"),
            ("point", "Lines hide each other", "When values are close, lines overlap and cross, and the "
             "reader cannot follow any single one."),
            ("point", "Colors run out", "Six colors are hard to tell apart, and some readers cannot "
             "separate certain pairs at all. Part 26 covered this."),
            ("point", "The legend becomes a puzzle", "The reader looks back and forth between the legend "
             "and the lines, and loses the story on the way."),
            ("point", "Big values flatten small ones", "A barangay collecting ₱400,000 a month sets the "
             "scale, and one collecting ₱40,000 looks like a flat line on the floor."),
            ("h", "The Example Data"),
            "Monthly collections, in thousands of pesos, January to June:",
            ("point", "Poblacion", "410, 380, 395, 420, 405, 430"),
            ("point", "San Isidro", "120, 115, 125, 130, 128, 135"),
            ("point", "Malinao", "95, 98, 92, 60, 58, 55"),
            ("point", "Bagong Silang", "70, 72, 75, 78, 80, 85"),
            ("point", "Santa Cruz", "150, 145, 160, 155, 158, 162"),
            ("point", "Mabini", "40, 42, 41, 43, 90, 95"),
            "On one chart, Malinao’s fall in April and Mabini’s jump in May both get lost in the "
            "crowded lower part of the chart. Split into six small charts, they are the first two things a reader sees.",
            ("photo", "blog/bi-multiples-grid.jpg", "The same six barangays as small multiples on one "
             "shared scale. Malinao drops in April and Mabini jumps in May. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "Rule One: Share the Scale"),
            "If each small chart picks its own vertical scale, a line that rises from 40 to 95 can look as "
            "tall as one that rises from 380 to 430. The reader will compare heights, and the heights will "
            "lie.",
            ("point", "Same minimum", "Start every chart at the same value. For collections, zero is a "
             "safe choice."),
            ("point", "Same maximum", "Use the largest value in the whole table, not in each row. Here "
             "that is 430."),
            ("point", "Same size and order", "Keep the charts the same width and height, and arrange them "
             "in an order the reader expects, such as largest to smallest or the usual order of barangays."),
            ("h", "When to Break Rule One"),
            "Sometimes the question is about shape, not size. Did each barangay follow the same seasonal "
            "pattern? On a shared scale, the small barangays are too flat to show a pattern at all.",
            ("point", "Use separate scales on purpose", "Let each chart set its own range so each shape is "
             "visible."),
            ("point", "Say so in the title", "Write “Each chart has its own scale” above the grid, and show "
             "the axis numbers on every chart."),
            ("point", "Do not mix", "A grid where some charts share a scale and some do not misleads even "
             "careful readers."),
            ("h", "Building Them in Google Sheets: Sparklines"),
            "The quickest way is the SPARKLINE function, which draws a tiny chart inside one cell. Put the "
            "barangays in A2:A7, the month names in B1:G1, and the "
            "monthly figures in B2:G7. In H2, enter:",
            ("point", "Formula", "=SPARKLINE(B2:G2, {\"charttype\",\"column\"; \"ymin\",0; \"ymax\",MAX($B$2:$G$7)})"),
            "Fill it down to H7. The dollar signs keep the MAX pointed at the whole table, so every row "
            "uses the same scale. Google’s help page for SPARKLINE lists ymin and ymax as options for line "
            "and column sparklines.",
            ("point", "Make them bigger", "Widen column H and increase the row height so each sparkline is "
             "readable."),
            ("point", "Line instead of column", "Remove the charttype setting, or set it to line. The ymin "
             "and ymax settings work the same way."),
            ("point", "Highlight the last month", "Column sparklines accept a lastcolor setting, which "
             "colors the most recent bar differently."),
            ("h", "Building Them in Google Sheets: Copied Charts"),
            "For larger charts with titles and labels, build one chart and copy it.",
            ("point", "Make the first chart", "Select A1:G2 for Poblacion and insert a chart. Choose a line "
             "or column chart and give it a short title."),
            ("point", "Fix the scale", "In the chart editor, open Customize, then Vertical axis, and type "
             "the same Min and Max, such as 0 and 450."),
            ("point", "Copy, paste, change the range", "Use the chart’s menu to copy it, paste it beside the "
             "first, then edit the data range to the next barangay’s row and change the title."),
            ("point", "Line them up", "Resize and arrange the charts in a grid, two or three across."),
            "Copied charts look better in a printed report, because each one can carry a title, axis "
            "numbers and month labels. They also take more care: if one chart is pasted with the wrong "
            "range, the grid quietly shows the wrong barangay under the right name. Check every title "
            "against its data range before sharing.",
            "The copied-chart grid takes longer to build and to update. Sparklines refresh by themselves "
            "when the data changes, which matters if the table grows every month.",
            ("h", "Mistakes to Avoid"),
            ("point", "Letting each chart choose its own scale by accident", "Set the minimum and maximum "
             "yourself."),
            ("point", "Too many charts", "Thirty tiny charts on a phone are unreadable. Group or filter "
             "first."),
            ("point", "Different chart types in the grid", "Use one type throughout so the reader compares "
             "data, not designs."),
            ("point", "A grid with no labels", "Each chart needs its barangay name, and the grid needs one "
             "line saying what is measured and in what unit."),
            ("h", "Key Takeaways"),
            ("point", "One crowded chart hides detail", "Small multiples give each group its own space."),
            ("point", "Share the scale by default", "Same minimum, same maximum, same size."),
            ("point", "Separate scales only on purpose", "And say so in the title."),
            ("point", "Sheets can do it two ways", "SPARKLINE with ymin and ymax, or copied charts with a "
             "fixed axis."),
            ("h", "Your Part 35 Exercise"),
            ("point", "Step 1", "Type the example table into a new sheet, barangays in A2:A7 and January to "
             "June in B1:G1."),
            ("point", "Step 2", "Add the SPARKLINE formula in H2 and fill it down. Find Malinao and Mabini."),
            ("point", "Step 3", "Remove the ymin and ymax settings from Mabini’s row only. Notice how its "
             "May and June bars now reach as high as Poblacion’s, though its numbers are far smaller. Then put the settings back."),
            ("point", "Step 4", "Build one full line chart with all six barangays and compare it with your "
             "sparklines. Which one shows Malinao’s April drop faster?"),
            ("cta", "Read: Business Intelligence Series, Part 27: Maps by Barangay, When Location Is the Point", "/blog/business-intelligence-part-27-maps-by-barangay/"),
            ("cta", "Read: Business Intelligence Series, Part 19: Fair Comparisons, This Month, Last Month and Last Year", "/blog/business-intelligence-part-19-fair-comparisons/"),
            ("cta", "Read: Business Intelligence Series, Part 26: Colors Everyone Can Read, Contrast, Labels and the Red-Green Trap", "/blog/business-intelligence-part-26-accessible-colors/"),
            ("cta", "Read: Business Intelligence Series, Part 34: Aging of Arrears, Sorting Unpaid Accounts by How Long They Have Waited", "/blog/business-intelligence-part-34-aging-of-arrears/"),
            ("ask", "Which chart in your office has too many lines on it?"),
        ],
    },
    {
        "title": "Business Intelligence Series, Part 34: Aging of Arrears, Sorting Unpaid Accounts by How Long They Have Waited",
        "slug": "business-intelligence-part-34-aging-of-arrears",
        "category": "bi",
        "date": "April 25, 2027",
        "summary": "A single total of unpaid taxes hides the question that matters most: how old is the debt? "
                   "This part shows how to group arrears into age buckets in Google Sheets, chart them, "
                   "match an action to each bucket, and spot the accounts that are running out of time.",
        "publish_on": "2027-04-25 21:00",
        "body": [
            "The quarterly report said unpaid real property tax stood at ₱3.8 million. The council member "
            "asked whether that was good or bad. The analyst did not know. ₱3.8 million of last month’s bills "
            "would be one problem. ₱3.8 million from ten years ago would be a very different one.",
            "The total was correct. It just could not answer the question he had asked.",
            "(The office, the accounts and the figures are invented for this lesson. The legal time limit "
            "mentioned below is real and cited.)",
            "Part 33 compared collections with a target that follows the calendar. This part looks at the "
            "other side of the ledger: what has not been paid, and for how long. You will learn what an "
            "aging report is, how to choose the age buckets, how to build them in Google Sheets, how to "
            "chart the result, and how to match each bucket with an action.",
            ("photo", "blog/bi-aging.jpg", "Aging of arrears: group unpaid amounts by age, chart them, give "
             "each bucket an action, and watch the oldest closely. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "What an Aging Report Is"),
            "An aging report groups unpaid amounts by how long they have been overdue. Businesses use it for "
            "money customers owe them. A treasury can use it for unpaid taxes and fees.",
            ("point", "It shows age, not just size", "₱100,000 overdue by a month and ₱100,000 overdue by "
             "four years need different responses."),
            ("point", "It shows movement", "Run it every quarter, as of the same day. Money that moves from a young bucket to an "
             "older one is money the office is not reaching."),
            ("point", "It points to action", "Each bucket can have its own next step, owner and deadline."),
            ("h", "Choosing the Buckets"),
            "Pick buckets that match how the office actually follows up. For real property tax, this set "
            "works as a start:",
            ("point", "1 to 90 days", "Recently missed. A reminder may be enough."),
            ("point", "91 to 365 days", "Missed most of a year. A notice and a visit."),
            ("point", "1 to 3 years", "A pattern, not an accident. Formal steps under Part 5."),
            ("point", "3 to 5 years", "Running out of time. See the next section."),
            ("point", "Over 5 years", "Needs a legal review before any action."),
            ("h", "Why the Five-Year Mark Matters"),
            "Section 270 of the Local Government Code says real property tax must be collected within five "
            "years from the date it became due, or within ten years from discovery when there was fraud or "
            "intent to evade. Part 5 of Inside the Local Treasury explained that the period stops running in "
            "some cases, such as when the owner is out of the country or cannot be located. For other local "
            "taxes, Section 194 sets a similar five-year period.",
            "That makes the 3-to-5-year bucket the most time-sensitive on the report. An amount there is "
            "still collectible, but not for long. Amounts over five years old should go to the office’s "
            "legal adviser before anyone treats them as collectible or as lost.",
            ("h", "Building It in Google Sheets"),
            "Start from a table with one row per unpaid bill: the account, the due date and the balance still "
            "unpaid. Use the remaining balance, not the original bill, so partial payments are counted.",
            ("point", "Set the as-of date", "Type the date of the report in H1, for example March 31, 2027. "
             "Using a fixed date, not TODAY(), keeps the report the same each time it is opened."),
            ("point", "Days overdue", "In column D: =$H$1-B2. Part 29 of the Data Analytics Series covered "
             "counting days."),
            ("point", "The bucket", "In column E: =IFS(D2<=0, \"Current\", D2<=90, \"1-90 days\", D2<=365, "
             "\"91-365 days\", D2<=1095, \"1-3 years\", D2<=1825, \"3-5 years\", TRUE, \"Over 5 years\")."),
            ("point", "Totals by bucket", "Use SUMIFS and COUNTIFS from Part 23, or a pivot table from "
             "Part 24, with the bucket as the row and the balance as the value."),
            ("point", "Flag disputed accounts", "Add a status column for accounts under protest or in "
             "court. Part 18 of Inside the Local Treasury described protests. Keep those balances visible, "
             "but report them on a separate line so they are not chased like ordinary arrears."),
            "IFS checks its conditions in order and stops at the first true one, so the order of the "
            "buckets in the formula matters. The day counts treat a year as 365 days, which is close enough "
            "for grouping, but check any account near a boundary by hand.",
            ("h", "Charting It"),
            ("point", "A bar chart, oldest at the bottom or top", "Keep the buckets in age order, not sorted "
             "by size. The order is the point."),
            ("point", "Show both money and accounts", "₱650,000 over five years might be 25 accounts; "
             "₱420,000 in the youngest bucket might be 310. Each tells a different story about workload."),
            ("point", "Add the date", "As in Part 30, write the as-of date beside the chart."),
            ("photo", "blog/bi-aging-chart.jpg", "An aging chart for real property tax arrears, with the "
             "action for each bucket. Figures are invented. (Illustration: Butch Mahinay, aumahinay.dev)",
             "medium"),
            ("h", "Reading the Example"),
            "In the invented report for March 31, 2027, the ₱3.8 million broke down like this: ₱420,000 at 1 "
            "to 90 days in 310 accounts, ₱680,000 at 91 to 365 days in 190 accounts, ₱1,150,000 at 1 to 3 "
            "years in 140 accounts, ₱900,000 at 3 to 5 years in 60 accounts, and ₱650,000 over five years "
            "in 25 accounts.",
            ("point", "The biggest bucket is not the most urgent", "₱1.15 million at 1 to 3 years is the "
             "largest, but ₱900,000 at 3 to 5 years is closer to the time limit."),
            ("point", "Sixty accounts is a workable list", "A team can visit or write to sixty owners in a "
             "quarter. That list became the first priority."),
            ("point", "The youngest bucket is wide but shallow", "Many accounts, small amounts. A text "
             "reminder, like the pilot in Part 32 of the Project Management Series, fits it."),
            ("h", "Match an Action to Each Bucket"),
            ("point", "1 to 90 days", "Reminder by text or letter."),
            ("point", "91 to 365 days", "Notice, then a visit or a call."),
            ("point", "1 to 3 years", "Formal notice of delinquency and the remedies in Part 5."),
            ("point", "3 to 5 years", "Priority list, reviewed monthly, with a named owner."),
            ("point", "Over 5 years", "Legal review, account by account."),
            ("quote", "A total tells you how much is owed. An aging report tells you how much time you have."),
            ("h", "Mistakes to Avoid"),
            ("point", "Reporting only the total", "Break it down by age."),
            ("point", "Using TODAY() in a saved report", "Fix the as-of date so the report does not change."),
            ("point", "Using the original bill", "Use the remaining balance after partial payments."),
            ("point", "Sorting buckets by size", "Keep them in age order."),
            ("h", "Key Takeaways"),
            ("point", "Age matters as much as amount", "The same peso has a different urgency at different ages."),
            ("point", "Watch the five-year mark", "Section 270 for real property tax, Section 194 for other local taxes."),
            ("point", "IFS builds the buckets", "From days overdue against a fixed as-of date."),
            ("point", "One action per bucket", "With an owner and a review date."),
            ("h", "Your Part 34 Exercise"),
            ("point", "Step 1", "Make a table of ten invented unpaid bills with due dates across several years."),
            ("point", "Step 2", "Add the as-of date, the days overdue and the IFS bucket formula."),
            ("point", "Step 3", "Total the balances and count the accounts in each bucket."),
            ("point", "Step 4", "Write one action and one owner beside each bucket."),
            "At the next council meeting, the analyst showed one bar chart instead of one number. The council "
            "member looked at the 3-to-5-year bar for a long time, then asked how many people the office "
            "needed to work through sixty accounts before the end of the year.",
            ("cta", "Read: Inside the Local Treasury, Part 5: Unpaid Amilyar, From Notice to Auction", "/blog/unpaid-amilyar-notice-to-auction/"),
            ("cta", "Read: Business Intelligence Series, Part 33: Targets vs Actual, Bullet Charts, Gauges and the Year-to-Date Trap", "/blog/business-intelligence-part-33-targets-vs-actual/"),
            ("cta", "Read: Data Analytics Series, Part 29: Counting Days in Google Sheets, Working Days, Due Dates and Days Late", "/blog/data-analytics-part-29-counting-days/"),
            ("cta", "Read: Business Intelligence Series, Part 18: Thresholds and Alerts, Letting the Dashboard Say When to Look", "/blog/business-intelligence-part-18-thresholds-and-alerts/"),
            ("ask", "How old is the oldest unpaid account in your office’s records?"),
        ],
    },
    {
        "title": "Business Intelligence Series, Part 33: Targets vs Actual, Bullet Charts, Gauges and the Year-to-Date Trap",
        "slug": "business-intelligence-part-33-targets-vs-actual",
        "category": "bi",
        "date": "April 20, 2027",
        "summary": "A collection target is only useful if the dashboard compares it fairly with what has come "
                   "in. This part shows how to set a year-to-date target that follows the calendar, how to "
                   "show actual against target with a bullet chart or a gauge in Data Studio, how to set "
                   "the ranges, and how to label the gap so nobody misreads it.",
        "publish_on": "2027-04-20 21:00",
        "body": [
            "At the end of March, the head of office looked at the new gauge on the collections dashboard. "
            "The needle pointed at 35 percent of the year’s target. “A quarter of the year is gone, and we "
            "have more than a third of the money,” she said. “We’re ahead.”",
            "The analyst was not so sure. Last year, the first quarter had brought in 40 percent of the "
            "year’s collections, thanks to the January rush. By that measure, the office was behind.",
            "(The office, the target and the figures are invented for this lesson. The Data Studio chart "
            "settings below are from Google’s chart reference pages, and they can change, so check the "
            "current pages before you rely on a detail.)",
            "Part 32 put a public report on a website. This part deals with a question that sits at the top "
            "of internal dashboards: are we on target? You will learn why the full-year target can "
            "mislead early in the year, how to build a year-to-date target that follows the calendar, how a "
            "bullet chart and a gauge show actual against target in Data Studio, how to set their ranges, "
            "and how to label the gap.",
            ("photo", "blog/bi-target.jpg", "Targets vs actual: compare like with like, choose a compact "
             "chart, set honest ranges, and label the gap. (Illustration: Butch Mahinay, aumahinay.dev)",
             "medium"),
            ("h", "The Year-to-Date Trap"),
            "Collections in a local treasury can follow the calendar closely. Business taxes and the amilyar bring a rush "
            "in January, as Part 2 of Inside the Local Treasury described, and quieter months follow. A "
            "full-year target divided evenly by twelve ignores that pattern.",
            ("point", "The full-year view", "Annual target ₱60,000,000. Actual by March 31: ₱21,000,000, or "
             "35 percent. Against an even split, one quarter of ₱60,000,000 is ₱15,000,000, so the office "
             "looks 40 percent ahead."),
            ("point", "The calendar view", "Last year, the first quarter brought in 40 percent of the year. "
             "A year-to-date target built on that pattern is 40 percent of ₱60,000,000, or ₱24,000,000. "
             "Actual ₱21,000,000 is 87.5 percent of it. The office is behind by ₱3,000,000."),
            "Both numbers are arithmetic, and both are correct. Only the second compares like with like. "
            "Part 19 made the same point about comparing this month with the same month last year.",
            ("photo", "blog/bi-target-ytd.jpg", "The same ₱21 million against two different targets: ahead "
             "of an even split, behind the calendar. Figures are invented. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "Building a Year-to-Date Target"),
            "A year-to-date target needs only a small table and one column of arithmetic.",
            ("point", "Step 1: Find the pattern", "For each month of last year, or an average of the last "
             "three years, compute that month’s share of the year’s total. The twelve shares add to 100 "
             "percent."),
            ("point", "Step 2: Spread the target", "Multiply the annual target by each month’s share. That "
             "gives a monthly target that rises in busy months and falls in quiet ones."),
            ("point", "Step 3: Add them up", "A running total of the monthly targets gives the target for "
             "each month-end. Put it in the date table from Part 14, so every chart can use it."),
            ("point", "Step 4: Note the source", "Write down which years the pattern came from. If a rule "
             "changed a deadline, last year’s pattern may not fit this year."),
            "Part 32 of the Data Analytics Series explained why rounded monthly targets may not add up "
            "exactly to the annual one. Use the remainder fix there so the twelve months match the year.",
            ("h", "Two Charts for Actual Against Target"),
            "Data Studio offers two chart types built for this question. Both show a single number against a "
            "target, with colored ranges behind it.",
            ("point", "Bullet chart", "Google’s reference says bullet charts show “how well a given metric "
             "is performing against target benchmarks.” A bar shows the actual value, a vertical line marks "
             "the target, and up to three bands show poor, average and good."),
            ("point", "Gauge chart", "The gauge reference describes the same purpose: “how well a given "
             "metric is performing against a target goal.” It has a target, an axis minimum and maximum, "
             "and up to five ranges, which are turned off by default."),
            ("point", "One number each", "Both charts take a single metric. For several measures, place "
             "several charts side by side, or use a table."),
            "For a treasury dashboard with several measures, the bullet chart is a good default. It is "
            "compact, it can sit in a row with others, and bars lined up side by side are easier to compare "
            "than needles on separate dials. A single "
            "gauge can still work as the headline of a page, where one number matters more than the rest.",
            ("h", "Setting the Ranges Honestly"),
            "The colored bands tell the reader how to feel about the number, so they need agreed values, "
            "not defaults.",
            ("point", "Change the defaults", "The bullet chart’s default ranges are 1, 2 and 3. Google’s "
             "reference says to adjust them to fit your data."),
            ("point", "Tie them to the year-to-date target", "For example: below 90 percent of the "
             "year-to-date target is poor, 90 to under 100 percent is average, and 100 percent or more is "
             "good. In the March example, 87.5 percent lands in poor."),
            ("point", "Agree on them once", "Part 18 set thresholds before anyone looked at the data. Ranges "
             "work the same way. Changing them after a bad month hides the month, not the problem."),
            ("point", "Watch the direction", "For a measure where lower is better, such as days to release "
             "a permit, “good” is the low end. Label it so nobody reads a long bar as a win."),
            ("h", "Label the Gap"),
            "A chart shows the gap. A label explains it.",
            ("point", "Give both numbers", "“Actual ₱21.0M, year-to-date target ₱24.0M.”"),
            ("point", "Give the difference both ways", "“₱3.0M behind, 87.5 percent of target.”"),
            ("point", "Say which target", "“Year-to-date target based on the 2024 to 2026 monthly pattern.” "
             "Without that line, a reader may assume an even split."),
            ("point", "Keep the date", "Part 30’s “data as of” line belongs beside every target chart."),
            ("point", "Show the trend below it", "A small line chart of monthly actual and target under the "
             "bullet shows whether the gap is closing or growing."),
            ("quote", "Being ahead of the wrong target is not good news. It is a late surprise."),
            ("h", "Mistakes to Avoid"),
            ("point", "Comparing with the full-year target early in the year", "Use a year-to-date target."),
            ("point", "Dividing the target by twelve", "Follow the calendar of collections."),
            ("point", "Leaving the default ranges", "Set them from the target, and agree on them first."),
            ("point", "A dial for every measure", "Use bullet charts in a row, or a table."),
            ("h", "Key Takeaways"),
            ("point", "Compare like with like", "Year-to-date actual against year-to-date target."),
            ("point", "Spread the target by month", "Using the pattern of recent years."),
            ("point", "Bullet chart first", "Compact and easy to compare. A gauge for one headline number."),
            ("point", "Ranges and labels", "Agreed in advance, and stating which target is used."),
            ("h", "Your Part 33 Exercise"),
            ("point", "Step 1", "List last year’s collections by month and compute each month’s share of "
             "the total."),
            ("point", "Step 2", "Spread this year’s target with those shares, and add a running total."),
            ("point", "Step 3", "Compare this year’s actual so far with the running total for the same "
             "month-end."),
            ("point", "Step 4", "Build one bullet chart with ranges at 90 and 100 percent of the target, "
             "and a label that names the target."),
            "At the next meeting, the gauge was gone. In its place was a row of three bullet charts, each "
            "with a target line set to the year-to-date figure. The first bar stopped short of its line, "
            "and the label beside it said “₱3.0M behind.” The head of office asked what could be done in "
            "April, which was exactly the question the chart was built to raise.",
            ("cta", "Read: Business Intelligence Series, Part 19: Fair Comparisons, This Month, Last Month and Last Year", "/blog/business-intelligence-part-19-fair-comparisons/"),
            ("cta", "Read: Business Intelligence Series, Part 18: Thresholds and Alerts, Letting the Dashboard Say When to Look", "/blog/business-intelligence-part-18-thresholds-and-alerts/"),
            ("cta", "Read: Business Intelligence Series, Part 14: The Date Table, a Calendar Your Dashboard Can Count On", "/blog/business-intelligence-part-14-the-date-table/"),
            ("cta", "Read: Data Analytics Series, Part 32: Rounding, and Why the Totals Don’t Add Up", "/blog/data-analytics-part-32-rounding-and-totals/"),
            ("ask", "Does your office compare collections with a target that follows the calendar, or with an even split?"),
        ],
    },
    {
        "title": "Business Intelligence Series, Part 32: Embedding a Report on a Website, Public Numbers Without Private Data",
        "slug": "business-intelligence-part-32-embedding-a-report",
        "category": "bi",
        "date": "April 15, 2027",
        "summary": "Putting a live report on a website can make public numbers easy to find. This part shows "
                   "how embedding works in Data Studio, who can see an embedded report, why the report "
                   "must be built for the public before it is embedded, how to test it as a stranger would, "
                   "and how to turn it off.",
        "publish_on": "2027-04-15 21:00",
        "body": [
            "The information officer had an idea. The collections dashboard was updated every day, and "
            "people kept asking how the town was doing. Why not put the dashboard on the town’s website, "
            "so anyone could see it? She asked the analyst for “the code to paste.”",
            "The analyst opened the report and paused. The first page showed totals. The third page, built "
            "for the revenue unit heads, listed accounts with balances. The code would take less than a "
            "minute to make. Making the report safe for the public would take an afternoon.",
            "(The office and the report are invented for this lesson. The Data Studio features below are "
            "from Google’s help page on embedding a report, and they can change, so check the current page "
            "before you rely on a detail.)",
            "Part 31 sent a report to people by email. This part puts a report where anyone can find it: on "
            "a web page. By the end, you will know how embedding works, who can see an embedded report, why "
            "the public version has to be its own report, how to test it the way a stranger would, and how "
            "to switch it off when needed.",
            ("photo", "blog/bi-embed.jpg", "Embedding a report: build a public version, share it on "
             "purpose, test it as a stranger, and keep the off switch handy. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "What Embedding Does"),
            "Embedding places a live report inside another web page, the way a video can play inside a news "
            "article. The report stays in Data Studio. The web page simply shows a window into it, using a "
            "piece of HTML called an iframe.",
            ("point", "It stays live", "When the report’s data refreshes, the embedded view shows the new "
             "numbers. Nobody has to copy screenshots to the website."),
            ("point", "It opens in view mode", "Google’s help says embedded reports can’t be edited, copied "
             "or shared by the viewer, and there is no menu bar."),
            ("point", "Some parts can’t be removed", "The help page says the Data Studio watermark and the "
             "full-screen option always appear."),
            ("point", "Viewers can’t force a refresh", "The data refreshes when the report’s freshness "
             "setting allows. Part 30’s “data as of” line matters even more here."),
            ("h", "Who Can See It: Sharing Decides, Not Embedding"),
            "This is the most important point in the whole post. Embedding does not change who is allowed to "
            "see a report. The report’s sharing settings do.",
            ("point", "A public report", "Google’s help says that if the report is shared publicly, “anyone "
             "viewing your page can see the embedded report.”"),
            ("point", "A restricted report", "Only the people, groups or domains it is shared with can see it, "
             "and they must be signed in to a Google account. Everyone else cannot see the "
             "numbers."),
            "So a report for the town website has to be shared publicly, and anything inside a public report "
            "is public. That includes every page, not only the first one. Google’s help notes that a report "
            "with several pages shows page navigation at the bottom by default.",
            ("h", "Build the Public Report First"),
            "Part 17 separated a working file that holds names from a sharing file that holds only totals. "
            "Embedding uses the same idea, one step further.",
            ("point", "Make a new report", "Do not embed the office’s working report. Create a separate report "
             "for the public, with its own name, such as “Collections Summary (Public).”"),
            ("point", "Connect it to totals only", "Its data source should be the sharing file with monthly "
             "totals by kind of tax. If a name or an account number is not in the source, it cannot leak "
             "through a chart."),
            ("point", "Mind the credentials", "A public report needs owner’s credentials so strangers can "
             "see the data. That is exactly why the source behind it must contain nothing private."),
            ("point", "Watch small numbers", "Part 17 warned that a total of one can point to a person. A "
             "public report should group small categories, or show them at a level where no single taxpayer "
             "stands out."),
            ("point", "Add the context", "A title, a “data as of” date, a one-line note on what is counted, "
             "and an office to contact with questions."),
            ("photo", "blog/bi-embed-path.jpg", "From the working file to the website: only the totals "
             "travel. The working report is never embedded. (Illustration: Butch Mahinay, aumahinay.dev)",
             "medium"),
            ("h", "Getting the Embed Code"),
            "Once the public report is ready, the steps are short. Google’s help lists them in this order.",
            ("point", "Step 1: Share it", "For a public page, use link sharing, such as “Anyone with the link "
             "can view” or public on the web."),
            ("point", "Step 2: Open the embed dialog", "Choose File, then Embed report, or click the Embed "
             "icon at the upper right. Then select Enable embedding."),
            ("point", "Step 3: Choose the type", "Keep Embed Code to get an iframe for a regular web page. "
             "Choose Embed URL for Google Sites and similar platforms."),
            ("point", "Step 4: Set the size", "Adjust the width and height so the report fits the page. Check "
             "it on a phone, as Part 12 recommended."),
            ("point", "Step 5: Paste it", "Give the code to whoever manages the website, who pastes it where "
             "the report should appear."),
            "Two details from the help page save time. First, you must use the link from the embed dialog; "
            "the ordinary share link will not work. Second, to embed only one page, go to that page before "
            "you generate the link.",
            ("h", "Test It as a Stranger"),
            "The person who built the report is the worst person to test it, because they can see "
            "everything. Test it the way the public will.",
            ("point", "Use a private window", "Open the web page in a private or incognito window, signed out "
             "of every account. What you see there is what the public sees."),
            ("point", "Click every page and filter", "If a filter lets a reader narrow a total down to one "
             "account, fix the report before it goes live."),
            ("point", "Check on a phone", "Some readers will arrive from a phone. Make sure the numbers can "
             "be read without zooming."),
            ("point", "Ask a second person", "Someone who did not build it can spot a label that only makes "
             "sense inside the office."),
            ("h", "The Off Switch"),
            "Google’s help says you can turn embedding off by clearing the Enable embedding box in the same "
            "dialog. The report stays in Data Studio; it simply stops showing on other sites. Write down who "
            "can do this and how, before the report goes live. If a wrong number appears on the website at "
            "night, the office should not have to wait for the analyst to come back from leave.",
            ("quote", "Anything inside a public report is public, including the pages nobody meant to show."),
            ("h", "Mistakes to Avoid"),
            ("point", "Embedding the working report", "Build a separate public report."),
            ("point", "Assuming embedding hides pages", "Readers can move between pages unless you embed only one, and the report itself is still shared."),
            ("point", "Testing while signed in", "Use a private window to see what strangers see."),
            ("point", "Leaving out the date", "Readers can’t refresh it, so tell them how current it is."),
            ("h", "Key Takeaways"),
            ("point", "Sharing decides who sees it", "Embedding only places it on the page."),
            ("point", "Public source, public report", "Totals only, with small numbers grouped."),
            ("point", "Test as a stranger", "Private window, every page, every filter, on a phone."),
            ("point", "Know the off switch", "Clear Enable embedding, and write down who can."),
            ("h", "Your Part 32 Exercise"),
            ("point", "List", "Write down every page of a report you might publish, and every field each "
             "page shows."),
            ("point", "Mark", "Circle any field that names a person, an account or a small group."),
            ("point", "Rebuild", "Make a public copy connected to a totals-only source, with a date and a "
             "contact line."),
            ("point", "Test", "Open the shared link in a private window before anyone embeds it."),
            "The information officer got her report, a week later than she wanted. It had three pages: "
            "totals by month, totals by kind of tax, and a short note on what the numbers meant. When a "
            "council member asked whether the website showed who had not paid, the analyst could answer "
            "with confidence: it could not, because that information was never in the report.",
            ("cta", "Read: Business Intelligence Series, Part 17: Who Sees What, Sharing Dashboards Without Sharing Too Much", "/blog/business-intelligence-part-17-who-sees-what/"),
            ("cta", "Read: Business Intelligence Series, Part 30: Showing When the Data Was Last Updated, Freshness Readers Can See", "/blog/business-intelligence-part-30-data-freshness/"),
            ("cta", "Read: Business Intelligence Series, Part 31: Scheduled Email Delivery, Sending the Report Before Anyone Asks", "/blog/business-intelligence-part-31-scheduled-email-delivery/"),
            ("cta", "Read: Business Intelligence Series, Part 12: Fast and Readable on a Phone", "/blog/business-intelligence-part-12-fast-and-readable-on-a-phone/"),
            ("ask", "If your office published one report on its website, which numbers would the public want first?"),
        ],
    },
    {
        "title": "Business Intelligence Series, Part 31: Scheduled Email Delivery, Sending the Report Before Anyone Asks",
        "slug": "business-intelligence-part-31-scheduled-email-delivery",
        "category": "bi",
        "date": "April 10, 2027",
        "summary": "A dashboard helps only the people who open it. This part shows how to schedule Data "
                   "Studio to email a report as a PDF on a set day and time: the steps, the options, the "
                   "limits on recipients and frequency, the privacy questions to ask first, and how to "
                   "check that the email arrives with current data.",
        "publish_on": "2027-04-10 21:00",
        "body": [
            "Every Monday at eight, the head of office asked the same question: “How did collections do "
            "last week?” Every Monday, the analyst opened the dashboard, took screenshots, pasted them into "
            "a message and sent them. It took twenty minutes. On the Monday the analyst was out sick, "
            "nobody sent anything, and the head of office went into the council meeting without the "
            "numbers.",
            "The dashboard had the answer all along. It just did not leave the building on its own.",
            "(The office and its Mondays are invented for this lesson. The Data Studio features and limits "
            "below are from Google’s help page on scheduling report delivery, and they can change, so check "
            "the current page before you rely on a number.)",
            "Part 30 put a “data as of” date on every page. This part sends those pages to the people who "
            "need them, on a schedule. By the end, you will know how to set up a scheduled email in Data "
            "Studio, what the email contains, the limits on recipients and frequency, which reports should "
            "not be emailed at all, and how to time the schedule so the PDF carries fresh data.",
            ("photo", "blog/bi-schedule.jpg", "Scheduled delivery: choose the people, the pages and the time, "
             "check the data first, and keep private details out. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "Why Send the Report at All"),
            "A dashboard is a pull tool. People have to remember to open it. A scheduled email is a push "
            "tool. It arrives in the inbox whether anyone remembers or not.",
            ("point", "It removes a manual task", "No screenshots, no copying, no dependence on one person "
             "being at their desk."),
            ("point", "It arrives at the same time", "A report that comes every Monday at 7:30 can become part of the week, like the morning flag ceremony."),
            ("point", "It reaches people who will not log in", "Some readers who open every email "
             "attachment may not bookmark a dashboard."),
            ("quote", "The best time to send a report is a few minutes before someone would have asked "
             "for it."),
            ("h", "Setting Up the Schedule"),
            "Open the report you want to send. You need to be its owner or an editor, or have permission "
            "to schedule.",
            ("point", "Step 1: Open the menu", "Click Share, then choose Schedule delivery."),
            ("point", "Step 2: Add recipients", "Type individual addresses or a group email alias. You, as "
             "the person creating the schedule, are always included."),
            ("point", "Step 3: Choose the pages", "Select only the pages the readers need. The weekly "
             "summary page may be enough."),
            ("point", "Step 4: Set the start date and time", "The schedule follows the time zone of your "
             "computer’s operating system. Data Studio does not let you change it inside the report."),
            ("point", "Step 5: Choose how often", "Pick a repeat option, or Custom to choose specific days "
             "or intervals. Then click Schedule."),
            ("h", "What the Email Contains"),
            ("point", "A PDF of the selected pages", "Built the same way as the PDF you get when you download "
             "the report."),
            ("point", "A preview and a link", "The email shows a preview of the report’s first page and a "
             "link to view the complete report."),
            ("point", "The default filters", "The PDF uses the report’s default filter and date range "
             "settings. On the schedule’s Filters tab, you can change the values of existing controls for "
             "that schedule, but you cannot add or remove controls there."),
            "The filter point matters. If the report opens by default on “Last 28 days” and the head of "
            "office wants last week, set the date range for the schedule or change the default before "
            "relying on the email.",
            ("h", "The Limits to Know"),
            "The help page lists these limits. They differ between the regular version and Data Studio Pro.",
            ("point", "Recipients per schedule", "No more than 50 addresses, and the person who created the "
             "schedule must be among them."),
            ("point", "Schedules per report", "Without Pro, one schedule per report, sent at most once a "
             "day. With Pro, up to 200 schedules and hourly delivery."),
            ("point", "Daily and monthly quotas", "Without Pro, a personal account can send scheduled "
             "emails to 200 recipients a day and 800 a month; a Google Workspace account, 500 a day and "
             "3,000 a month."),
            ("point", "Preview length", "The preview inside the email shows no more than five pages. The "
             "PDF itself includes all the selected pages."),
            "For a small treasury office, one weekly schedule to a handful of people stays well inside "
            "these limits. If you need one email for the treasurer and a different one for the market "
            "supervisor, either use separate reports or check whether your office has Pro.",
            ("h", "Ask the Privacy Question First"),
            "A dashboard can limit who sees it. An email attachment cannot control where it goes after it "
            "arrives. A PDF can be forwarded, printed and left on a desk.",
            ("point", "Send summaries, not lists of people", "Totals by month, by barangay or by type of "
             "tax are good candidates. Lists of taxpayers with names, addresses and amounts owed are not."),
            ("point", "Check every page you select", "A summary page might include a small table of the "
             "top ten delinquent accounts. Leave that page out of the schedule."),
            ("point", "Use group aliases carefully", "Know who is on a group email list before you put it "
             "in the recipient field."),
            "Part 20 of the Cybersecurity Series covers the Data Privacy Act at work. The same questions "
            "apply here: who needs this, and what is the least they need to see?",
            ("h", "Time It After the Data, Not Before"),
            "Part 30 separated two things: when the report refreshed, and when the data inside it was last "
            "updated. A schedule makes this even more important, because a stale PDF can go out automatically without anyone checking it.",
            ("point", "Know when the data lands", "If the encoder finishes Friday’s collections by Friday "
             "evening, a Monday 7:30 schedule is safe."),
            ("point", "Keep the “data as of” date on the page", "Then a stale PDF announces itself to the "
             "reader."),
            ("point", "Open the first email yourself", "You are on the recipient list. Read the first one "
             "carefully, page by page, before anyone else depends on it."),
            ("h", "Editing and Stopping a Schedule"),
            ("point", "To edit", "Open Share, then Schedule delivery, click More, choose Edit, make your "
             "changes and save."),
            ("point", "To delete", "Click More, then Delete schedule. The help page warns that a deleted "
             "schedule cannot be restored."),
            ("point", "When people leave", "Remove recipients who have moved to another office. A schedule "
             "keeps sending until someone changes it."),
            ("h", "Mistakes to Avoid"),
            ("point", "Emailing taxpayer-level details", "Send summaries; keep lists on the dashboard."),
            ("point", "Ignoring the default date range", "The PDF follows the report’s defaults."),
            ("point", "Scheduling before the data is in", "Set the time after the last update lands."),
            ("point", "Forgetting the schedule exists", "Review recipients and pages every quarter."),
            ("h", "Key Takeaways"),
            ("point", "Share, then Schedule delivery", "Recipients, pages, start time and repeat."),
            ("point", "A PDF, a preview and a link", "Using the report’s default filters."),
            ("point", "Up to 50 recipients", "One schedule per report, at most daily, without Pro."),
            ("point", "Privacy and freshness first", "Summaries only, sent after the data is current."),
            ("h", "Your Part 31 Exercise"),
            "Pick one report that someone asks you about every week.",
            ("point", "Choose one page", "The page that answers that person’s usual question."),
            ("point", "Check it", "No personal details, a clear “data as of” date, and the right default "
             "date range."),
            ("point", "Schedule it to yourself first", "Then add the real reader once the first email looks "
             "right."),
            "After a month, ask the reader whether the email helps, and whether they would change anything "
            "in it.",
            "The next Monday, the head of office found the weekly summary in her inbox at 7:30, before she "
            "had finished her coffee. Beside the title on the first page was the line “Data as of April 9.” "
            "The analyst was at her desk by eight, and for once, nobody asked her for screenshots.",
            ("cta", "Read: Business Intelligence Series, Part 30: Showing When the Data Was Last Updated, Freshness Readers Can See", "/blog/business-intelligence-part-30-data-freshness/"),
            ("cta", "Read: Business Intelligence Series, Part 20: Your First Data Studio Dashboard, Connected to Live Data", "/blog/business-intelligence-part-20-first-data-studio-dashboard/"),
            ("cta", "Read: Business Intelligence Series, Part 28: Is Anyone Using the Dashboard? Measuring Views and Decisions", "/blog/business-intelligence-part-28-dashboard-usage/"),
            ("cta", "Read: Cybersecurity Series, Part 20: Privacy at Work, and the Data Privacy Act at Your Desk", "/blog/cybersecurity-part-20-privacy-at-work/"),
            ("ask", "Which report do you send by hand every week that could be sent on a schedule instead?"),
        ],
    },
    {
        "date": "April 5, 2027",
        "title": "Business Intelligence Series, Part 30: Showing When the Data Was Last Updated, Freshness Readers Can See",
        "slug": "business-intelligence-part-30-data-freshness",
        "category": "bi",
        "summary": "A dashboard that refreshes every 15 minutes can still show week-old data. This part "
                   "explains Data Studio’s data freshness settings, the difference between a refreshed report "
                   "and current data, and how to put a clear “data as of” date on every page.",
        "publish_on": "2027-04-05 21:00",
        "body": [
            "On Monday, the head of office opened the collections dashboard and frowned. Real property tax "
            "collections had not moved since the previous Tuesday. Six days of nothing, in a month when payments had been coming in steadily. She called the analyst, who checked the report: it had "
            "refreshed that morning, as it did every fifteen minutes. The numbers were correct for the data "
            "it had.",
            "The problem was in the sheet behind it. The encoder who typed in the daily collections had been "
            "on leave since Tuesday, and nobody had filled in for her. The dashboard was fresh. The data was "
            "not.",
            "(The office, the encoder and the dates are invented to explain the idea. They describe no real "
            "office.)",
            "Part 29 retired reports that nobody uses. This part keeps the ones people use honest about "
            "time. When you finish, you will know what Data Studio’s data freshness setting does and does "
            "not do, how to refresh by hand, the difference between when a report was refreshed and when its "
            "data was last updated, and how to show readers a “data as of” date they can trust.",
            ("photo", "blog/bi-fresh.jpg", "Showing freshness: the report’s refresh time, the latest date in the "
             "data, a warning when it is stale, and an owner who updates it. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "Two Different Times"),
            "A dashboard has two times that matter, and they are easy to confuse.",
            ("point", "When the report last read the data", "Data Studio checks the source on a schedule and "
             "keeps recent results in memory. This is the refresh time."),
            ("point", "When the data was last updated", "The date of the newest record in the source: the "
             "last receipt typed in, the last file uploaded. This is the data’s real age."),
            "A report can be refreshed every fifteen minutes and still show a sheet that nobody has touched "
            "in a week. Readers need the second time more than the first.",
            ("quote", "A dashboard is only as current as the last row someone typed."),
            ("h", "Data Studio’s Data Freshness Setting"),
            "Google’s documentation describes data freshness as a way to balance up-to-date information "
            "against report performance. Data Studio stores recent queries and results in memory, and serves "
            "repeat requests from memory until the freshness period runs out.",
            ("point", "Google Sheets", "The default for a Sheets data source is every 15 minutes. The other "
             "options are 1 hour, 4 hours and 12 hours."),
            ("point", "Other sources", "Google Analytics defaults to every 12 hours. Database connectors such "
             "as BigQuery and MySQL offer choices in minutes or hours."),
            ("point", "How to change it", "Edit the data source, click Data freshness on its configuration "
             "page, choose an option under Check for fresh data, then click Set Data Freshness."),
            ("point", "Which to choose", "For daily collections typed in once a day, checking every 12 hours "
             "is enough and makes the report faster. For a sheet updated through the day, 15 minutes keeps "
             "it closer to the counter."),
            ("h", "Refreshing by Hand"),
            ("point", "Editors", "Google’s page says editors can refresh all the data sources in a report "
             "from the More options menu, by clicking Refresh data."),
            ("point", "Viewers", "Viewers can refresh only if the editor turns on the viewer data refresh "
             "option in the report settings. Then they can right-click a chart and choose Refresh data."),
            ("point", "A short wait", "The documentation says there is a one-minute cooldown between data "
             "refreshes."),
            "A manual refresh helps right after the encoder updates the sheet. It cannot help if the sheet "
            "itself was never updated.",
            ("h", "What the Report Already Shows"),
            "Google’s page says the time and date of the last data refresh is displayed in the bottom left "
            "corner of the report. It adds that if that time is earlier than your latest change to a filter "
            "or date range, the charts are being served from memory.",
            "That small line answers “When did the report last check?” It does not answer “How old is the "
            "newest record?” For that, you need to build one more thing.",
            ("h", "Build a “Data As Of” Date"),
            "The simplest proof of freshness comes from the data itself: the latest date in the table.",
            ("point", "A scorecard with the maximum date", "Add a scorecard chart using the payment date "
             "field, with its aggregation set to Max. It shows the newest payment date in the data source, "
             "such as “Data as of: April 2, 2027.”"),
            ("point", "Place it at the top", "Put it beside the page title on every page, in the same spot, "
             "so readers learn to look there first."),
            ("point", "Label it plainly", "“Latest payment recorded” or “Data as of.” Avoid “Last updated,” "
             "which readers may confuse with the report’s refresh time."),
            ("point", "Watch the filters", "If the scorecard follows the page’s filters, a barangay with no "
             "payment this week shows an older date. That can be useful, so say in the label that the "
             "date follows the selection."),
            ("h", "Add a Warning When Data Is Stale"),
            "A date is easy to overlook. A warning is not.",
            ("point", "Count the days", "In the source sheet, add a small summary cell: the number of days "
             "between today and the newest payment date. Part 29 of the Data Analytics series showed DAYS and "
             "NETWORKDAYS for this. Working days are fairer, so a weekend does not set off the alarm."),
            ("point", "Set a rule", "If the data is more than one working day old, show “Data may be "
             "incomplete: last update was 4 working days ago.”"),
            ("point", "Use the same thresholds idea", "Part 18 built thresholds and alerts for collections. "
             "Freshness deserves an alert of its own."),
            ("h", "Give the Data an Owner and a Schedule"),
            "In the opening story, the technology worked. What failed was that nobody was named to update "
            "the sheet while the encoder was away.",
            ("point", "Name the owner", "The data dictionary from Part 10 lists an owner for each source. "
             "Add a backup person for leave and absences."),
            ("point", "Write the schedule", "“Daily collections: entered by 10 a.m. the next working day.” A "
             "schedule tells readers what “fresh” means for this data."),
            ("point", "Show it in the footer", "One line under each page: the source, its owner, and how often "
             "it is updated."),
            ("h", "What to Tell Readers"),
            ("point", "On the dashboard", "The data-as-of date, the update schedule, and a warning when it is "
             "behind."),
            ("point", "In a briefing", "Say the date out loud before the numbers: “These figures are as of "
             "Friday.” Part 11’s five-minute briefing works better when the first line is the date."),
            ("point", "In a printed copy", "Print the date on the page. A screenshot travels without the "
             "dashboard’s context."),
            ("h", "The Fix in the Treasury"),
            "The analyst added a “Latest payment recorded” scorecard at the top of each page, and a red line "
            "that appeared when the data was more than one working day old. The records clerk was named as "
            "backup for the encoder. The next time the encoder took leave, the clerk entered the collections "
            "by ten each morning, and the warning never appeared.",
            ("h", "Mistakes to Avoid"),
            ("point", "Trusting the refresh time", "It tells you when the report checked, not how old the data is."),
            ("point", "No date on the page", "Add a data-as-of scorecard to every page."),
            ("point", "Alerts for amounts but not for age", "Stale data deserves a warning too."),
            ("point", "No backup for the person who updates", "Name one in the data dictionary."),
            ("h", "Key Takeaways"),
            ("point", "Two times", "Refresh time and data age are different."),
            ("point", "Freshness settings", "15 minutes by default for Sheets, up to 12 hours."),
            ("point", "Data as of", "A Max-date scorecard shows the newest record."),
            ("point", "Owners keep it fresh", "With a schedule and a backup."),
            ("h", "Your Part 30 Exercise"),
            "Open the practice dashboard from your earlier exercises.",
            ("point", "Add the date", "A scorecard with the maximum payment date, labeled “Data as of.”"),
            ("point", "Check the setting", "Look at the data source’s freshness and choose one that matches "
             "how often the sheet is updated."),
            ("point", "Write the line", "A footer with the source, owner, backup and update schedule."),
            "Then stop updating your practice sheet for two days, open the dashboard, and see whether a "
            "reader would notice. If they would not, add the warning.",
            ("cta", "Read: Business Intelligence Series, Part 29: Retiring Reports, Turning Off What Nobody Uses", "/blog/business-intelligence-part-29-retiring-reports/"),
            ("cta", "Read: Business Intelligence Series, Part 18: Thresholds and Alerts, Letting the Dashboard Say When to Look", "/blog/business-intelligence-part-18-thresholds-and-alerts/"),
            ("cta", "Read: Business Intelligence Series, Part 10: Keeping BI Honest With a Data Dictionary, Owners and a Change Log", "/blog/business-intelligence-part-10-keeping-bi-honest/"),
            ("cta", "Read: Data Analytics Series, Part 29: Counting Days in Google Sheets, Working Days, Due Dates and Days Late", "/blog/data-analytics-part-29-counting-days/"),
            ("ask", "How old is the newest number on your office’s main report right now?"),
        ],
    },
    {
        "date": "March 31, 2027",
        "title": "Business Intelligence Series, Part 29: Retiring Reports, Turning Off What Nobody Uses",
        "slug": "business-intelligence-part-29-retiring-reports",
        "category": "bi",
        "summary": "Every report an office keeps must be refreshed, checked and explained. This part shows "
                   "how to decide which reports to retire, test the decision before acting, tell people "
                   "ahead, keep a copy, remove the report in Data Studio safely, and update the records so "
                   "nothing breaks later.",
        "publish_on": "2027-03-31 21:00",
        "body": [
            "Every Monday morning, the analyst spent forty minutes on a report called “Weekly Collections "
            "by Collector, Old Format.” It had been built two years earlier for a head of office who had "
            "since retired. The new dashboard showed the same numbers, updated daily. Still, the old report "
            "went out every week, because nobody had ever said it could stop.",
            "Forty minutes a week is more than thirty hours a year, spent on a report that may have had no "
            "readers.",
            "(This office, its reports and the hours in this story are invented for teaching.)",
            "Part 28 measured which pages of a dashboard are used. This part acts on what it found. You "
            "will learn how to pick the reports to retire, how to test the choice before acting, how to "
            "tell people, what to keep, how to remove a report in Data Studio without losing anything you "
            "might need, and how to update the records so nothing breaks later.",
            ("photo", "blog/bi-retire.jpg", "Retiring a report: find the candidates, test with a pause, "
             "tell people, keep a copy, then remove it and update the records. (Illustration: Butch "
             "Mahinay, aumahinay.dev)", "medium"),
            ("h", "Why Retire Anything"),
            "Reports can pile up. Each new request can add one, but nothing in a request says when "
            "it should end.",
            ("point", "Time", "Every report must be refreshed, checked and explained. Time spent on a report "
             "nobody reads is time taken from one people do read."),
            ("point", "Confusion", "Two reports that show the same figure in slightly different ways invite "
             "the question “Which one is right?” Part 10 warned about this."),
            ("point", "Risk", "An old report may still be shared with people who changed jobs, or still "
             "connected to a sheet with personal data. Part 17 covered who should see what."),
            ("point", "Trust", "A short list of reports that are all maintained is easier to trust than a "
             "long list where some are quietly out of date."),
            ("quote", "A report nobody reads still has a cost. It is just paid by the person who keeps it "
             "running."),
            ("h", "Step 1: Find the Candidates"),
            "Start with the evidence from Part 28: usage counts, readers’ answers and the decision log. "
            "A report is a candidate for retirement if one or more of these is true.",
            ("point", "Low use, no decisions", "Few or no visits in three months, and no entry in the "
             "decision log."),
            ("point", "A duplicate", "Another report or dashboard page shows the same figures, kept more "
             "up to date."),
            ("point", "The question is gone", "The report answered a question for a project, a meeting "
             "series or a person that has since ended."),
            ("point", "The data is gone", "The source sheet is no longer updated, so the report shows old "
             "numbers as if they were current."),
            "Make a short list with each candidate, its owner, the people it is shared with, and the reason "
            "it is on the list.",
            ("h", "Step 2: Ask the Owner and the Readers"),
            ("point", "The owner", "Every report should have an owner, as Part 10 recommended. Ask the "
             "owner first: is this still needed, and by whom?"),
            ("point", "The readers", "Ask the people it is shared with a direct question: “If this report "
             "stopped next month, what would you use instead?” If the answer is “the dashboard,” you have "
             "your answer."),
            ("point", "Hidden users", "Ask whether any other report, sheet or office process reads from "
             "this one. A report can feed a monthly summary that someone else prepares."),
            ("h", "Step 3: Test With a Pause"),
            "If the answers are unclear, pause the report before removing it.",
            ("point", "Stop sending it", "For a report sent by email, stop the sending for one cycle. For a "
             "shared report, add a note at the top: “This report will be retired on April 30. Please tell "
             "the analyst if you still use it.”"),
            ("point", "Wait one full cycle", "A weekly report needs at least one missed week. A monthly "
             "report needs a full month, so that the people who use it at month’s end have a chance to "
             "notice."),
            ("point", "Write down who asks", "If someone asks for it, find out what they used it for. "
             "The need may fit on a page of the main dashboard."),
            ("h", "Step 4: Tell People Ahead"),
            "Retiring a report without notice can leave someone without a figure they need on the day they "
            "need it. Send a short notice to everyone with access.",
            ("point", "What is retiring", "The report’s name and link."),
            ("point", "When", "A date at least two weeks away."),
            ("point", "What replaces it", "A link to the dashboard page that shows the same figures, if "
             "there is one."),
            ("point", "Whom to ask", "The analyst or the report’s owner."),
            ("h", "Step 5: Keep a Copy"),
            "Before removing anything, save what you might need later.",
            ("point", "A snapshot", "Save a copy of the report’s last version, such as a PDF of each page, "
             "in the folder where the office keeps its records, named with the report and the date."),
            ("point", "The definitions", "Copy the report’s calculated fields and filters into the data "
             "dictionary, so the logic is not lost if someone asks how a figure was made."),
            ("point", "The data", "Leave the source data where it is unless the office’s records rules say "
             "otherwise. Retiring a report is not the same as deleting the data it used."),
            ("h", "Step 6: Remove It in Data Studio"),
            "Google’s documentation for Data Studio describes how removing a report works.",
            ("point", "Only the owner", "The page says you need to own the report to delete it."),
            ("point", "Remove moves it to the trash", "From the report list, choose More options, then "
             "Remove. While the report is in the trash, Google’s page says it is not accessible by you or "
             "anyone else."),
            ("point", "Restoring is possible", "Removed reports stay in the trash unless you delete them "
             "permanently, and can be restored from the Trash tab. After a restore, the people it was shared "
             "with have access again."),
            ("point", "Delete forever cannot be undone", "The page warns that deleting a report "
             "permanently cannot be undone. Leave retired reports in the trash for a while, until you are "
             "sure no one needs them."),
            ("point", "Check the data source", "A data source can be used by more than one report. Before "
             "removing a data source, check that no other report depends on it."),
            ("h", "Step 7: Update the Records"),
            ("point", "Change log", "Add a line: the report, the date it was retired, the reason, and where "
             "the copy is kept."),
            ("point", "Data dictionary", "Mark the report’s fields as retired, or move them to the report "
             "that replaced it."),
            ("point", "Links", "Search the office’s shared documents and dashboard pages for links to the "
             "old report, and point them to the replacement."),
            ("point", "Calendar", "Remove the refresh task from your own weekly schedule. That is the time "
             "you just won back."),
            ("h", "The Analyst’s Spring Cleaning"),
            "The analyst listed nine reports. Four were candidates. The owner of one asked to keep it, "
            "because it fed a quarterly summary for the council. The other three were paused for a month. "
            "Only one person asked about one of them, and that question was answered by a dashboard page "
            "she had not known about.",
            "The three reports went to the trash on April 30, with copies saved and the change log "
            "updated. The Monday morning forty minutes went to checking the dashboard’s data instead.",
            ("h", "Mistakes to Avoid"),
            ("point", "Deleting without asking", "Ask the owner and readers, and test with a pause."),
            ("point", "Deleting forever right away", "Leave the report in the trash until you are sure."),
            ("point", "Forgetting hidden users", "Check for other reports and processes that depend on it."),
            ("point", "Retiring the report and the data together", "Keep the data under the office’s records rules."),
            ("h", "Key Takeaways"),
            ("point", "Retire on evidence", "Usage, readers’ answers and the decision log."),
            ("point", "Pause, then tell", "One full cycle of silence, then a notice with a date."),
            ("point", "Keep a copy", "A snapshot and the definitions, before removing anything."),
            ("point", "Trash first, delete later", "And update the change log and links."),
            ("h", "Your Part 29 Action Plan"),
            ("point", "Today", "List every report you maintain, with its owner and the hours it takes each "
             "month."),
            ("point", "This month", "Pick the two with the least use, ask their owners and readers, and "
             "start a pause."),
            ("point", "Next month", "Retire what nobody missed, save the copies, and record it in the "
             "change log."),
            "Then add up the hours the retired reports used to take. Write the number at the top of your "
            "change log. It is the clearest argument for doing this again next year.",
            ("cta", "Read: Business Intelligence Series, Part 28: Is Anyone Using the Dashboard? Measuring Views and Decisions", "/blog/business-intelligence-part-28-dashboard-usage/"),
            ("cta", "Read: Business Intelligence Series, Part 10: Keeping BI Honest With a Data Dictionary, Owners and a Change Log", "/blog/business-intelligence-part-10-keeping-bi-honest/"),
            ("cta", "Read: Business Intelligence Series, Part 17: Who Sees What, Sharing Dashboards Without Sharing Too Much", "/blog/business-intelligence-part-17-who-sees-what/"),
            ("cta", "Read: Business Intelligence Series, Part 8: Report or Dashboard? Static, Live and Self-Service Views", "/blog/business-intelligence-part-8-report-or-dashboard/"),
            ("ask", "Which report in your office would anyone miss if it stopped next Monday?"),
        ],
    },
    {
        "date": "March 26, 2027",
        "title": "Business Intelligence Series, Part 28: Is Anyone Using the Dashboard? Measuring Views and Decisions",
        "slug": "business-intelligence-part-28-dashboard-usage",
        "category": "bi",
        "summary": "A dashboard can be accurate, readable and still unused. This part shows how to find out "
                   "who opens it and what they do with it: Google Analytics for usage counts, a short "
                   "monthly question to readers, and a decision log that ties pages to actions.",
        "publish_on": "2027-03-26 21:00",
        "body": [
            "The analyst had spent three months on the treasury dashboard. It had six pages, a date table, "
            "fair comparisons, thresholds, annotations and colors everyone could read. At the monthly "
            "meeting, the head of office asked a question about real property tax collections in San "
            "Roque. The answer was on page four. Nobody in the room knew that page four existed.",
            "Afterward, the analyst asked a simple question for the first time: of the six pages, which "
            "ones does anyone actually open?",
            "(The office, its dashboard and its people are invented. They stand for no real local "
            "government.)",
            "Parts 20 to 27 built a dashboard and made it accurate and readable. This part asks whether it "
            "is used. When you are done reading, you will know why usage is worth measuring, how to connect "
            "a Data Studio report to Google Analytics, what the numbers can and cannot tell you, how to ask "
            "readers directly, and how to keep a small log that links each page to the decisions it "
            "supports.",
            ("photo", "blog/bi-usage.jpg", "Is anyone using the dashboard? Count the views, ask the "
             "readers, log the decisions, then improve or retire each page. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "Why Measure Usage at All"),
            "A dashboard costs time every month: data has to be refreshed, checked and explained. A page "
            "nobody reads still costs that time. Measuring usage tells you where to spend effort.",
            ("point", "Pages to improve", "A page opened often but followed by questions by email may be "
             "hard to read."),
            ("point", "Pages to promote", "A useful page nobody opens may simply be hard to find, like page "
             "four."),
            ("point", "Pages to retire", "A page nobody opens and nobody misses can go, after checking with "
             "the people who asked for it."),
            ("point", "Proof of value", "When someone asks whether the dashboard is worth the analyst’s "
             "time, usage and decisions are a better answer than “I think people like it.”"),
            ("quote", "A dashboard is finished when people use it to decide something, not when the last "
             "chart is placed."),
            ("h", "Connecting a Report to Google Analytics"),
            "Google’s documentation for Data Studio describes a way to measure report usage with Google "
            "Analytics. In summary:",
            ("point", "Create a property", "Set up a Google Analytics 4 property for the purpose. Google "
             "Analytics 4 measurement IDs begin with “G-”."),
            ("point", "Open the report settings", "Edit the report, then choose File, then Report settings."),
            ("point", "Enter the ID", "At the bottom of the Report settings panel, enter the measurement ID."),
            ("point", "Wait", "Google’s page says it may take up to 24 hours before data from the report "
             "begins to show up in Google Analytics."),
            "Google’s page adds a few limits worth knowing. A report can have only one Google Analytics 4 "
            "measurement ID. The page describes the data as anonymous usage data. It also mentions one "
            "named event, duplicate_report, which is sent when someone copies the report.",
            ("point", "Checking that it works", "Google’s page points to two places in Google Analytics: "
             "the Realtime report, to see activity as it happens, and the Reports snapshot, for a summary. "
             "Open the dashboard yourself, then look at Realtime to confirm that the visit appears."),
            ("point", "Seeing it in Data Studio", "The page also says you can create a Google Analytics "
             "data source connected to that property, so usage can be charted in Data Studio itself."),
            ("h", "What the Numbers Can Tell You"),
            ("point", "Which pages are opened", "Where your Analytics property lists views by page, the count shows where attention goes. If page one "
             "gets almost every view, readers may not be scrolling or clicking further."),
            ("point", "When it is opened", "A spike in the days before the monthly meeting, and silence "
             "after, tells you the dashboard is used for meetings, not daily work."),
            ("point", "Whether a change worked", "If you move the San Roque chart to page one, the count "
             "after the change can be compared with the count before."),
            ("h", "What the Numbers Cannot Tell You"),
            ("point", "Who opened it", "Google describes the data as anonymous. You will see that a page "
             "was viewed, not which employee viewed it. That is a good thing for privacy, and it means "
             "names must come from asking, not from tracking."),
            ("point", "Whether it helped", "A view is not a decision. A reader may open a page, fail to "
             "understand it, and close it."),
            ("point", "Your own visits", "The analyst opens the dashboard more than anyone while building "
             "and checking it. Keep that in mind before celebrating a high count, especially in a small "
             "office."),
            "A short line in the report footer, such as “Page visits to this report are counted "
            "anonymously to improve it,” tells readers what is happening. Measuring openly builds more "
            "trust than measuring quietly.",
            ("h", "Ask the Readers, Once a Month"),
            "Numbers show what happened. Readers can say why. A three-question message, sent once a "
            "month to the people on the sharing list from Part 17, takes them two minutes.",
            ("point", "Question 1", "Which page did you use this month, and for what?"),
            ("point", "Question 2", "What did you look for and not find?"),
            ("point", "Question 3", "If one page disappeared tomorrow, would you notice?"),
            "Keep the answers short and in one sheet. Three months of answers show which pages people "
            "rely on, and which questions the dashboard still does not answer.",
            ("h", "The Decision Log"),
            "Strong evidence that a dashboard works is a decision that changed because of it. A decision "
            "log is a small table with four columns.",
            ("point", "Date", "When the decision was made."),
            ("point", "Decision", "What was decided, in one sentence: “Send a second notice to "
             "business taxpayers in San Roque.”"),
            ("point", "Page used", "Which dashboard page showed the problem or supported the choice."),
            ("point", "Who decided", "The role, not necessarily the name: head of office, council "
             "committee, collector."),
            "Fill it in after each monthly meeting, using the minutes from Part 27 of the Project "
            "Management series as a model. A page that appears in the log is earning its place. A page "
            "that never appears after three months is a candidate for change or retirement.",
            ("h", "Putting the Three Together"),
            "Each source covers a gap in the others. Usage counts are steady and need no effort once set "
            "up, but they say nothing about value. Reader answers explain the counts, but readers may "
            "forget or be too polite to say a page is useless. The decision log shows value, but only for decisions someone wrote down.",
            ("point", "High views, in the log", "Keep and protect the page. Check its data first each "
             "month."),
            ("point", "High views, not in the log", "Ask readers what they use it for. It may support "
             "daily work that never reaches a meeting."),
            ("point", "Low views, in the log", "Valuable but hard to find. Move it, link it from page one, "
             "or mention it in the briefing."),
            ("point", "Low views, not in the log", "Ask whether anyone would miss it. If not, retire it."),
            ("h", "The Analyst’s First Month of Data"),
            "The analyst added the measurement ID, put the footer line on every page, and sent the "
            "three-question message. After a month, pages one and two had nearly all the visits. Page "
            "four, San Roque included, had a handful, most of them the analyst’s own. Two readers said "
            "they did not know there were more pages.",
            "The analyst moved a small barangay summary onto page one, with a link to the full page four, "
            "and started the decision log at the next meeting. The first entry was the second notice to "
            "San Roque, decided while the head of office was looking at the new summary.",
            ("h", "Mistakes to Avoid"),
            ("point", "Building more pages before measuring", "Find out what is used first."),
            ("point", "Reading views as value", "Pair counts with readers’ answers and the decision log."),
            ("point", "Measuring quietly", "Tell readers in the footer that visits are counted."),
            ("point", "Counting your own visits", "The builder may be the top viewer."),
            ("h", "Key Takeaways"),
            ("point", "Google Analytics 4", "One measurement ID per report, set in File, Report settings."),
            ("point", "Counts show attention", "Which pages, and when."),
            ("point", "Readers explain why", "Three questions, once a month."),
            ("point", "The decision log shows value", "Pages that lead to action earn their place."),
            ("h", "Your Part 28 Action Plan"),
            ("point", "This week", "Create a Google Analytics 4 property, add its measurement ID to your "
             "report, and add the footer line."),
            ("point", "This month", "Send the three-question message and start the decision log at your "
             "next meeting."),
            ("point", "Next month", "Sort your pages into the four groups above, and choose one page to "
             "move, one to improve and one to question."),
            "Write down today’s guess about which page is used most. In a month, compare it with the "
            "counts. The gap between the two is what this part is for.",
            ("cta", "Read: Business Intelligence Series, Part 20: Your First Data Studio Dashboard, Connected to Live Data", "/blog/business-intelligence-part-20-first-data-studio-dashboard/"),
            ("cta", "Read: Business Intelligence Series, Part 17: Who Sees What, Sharing Dashboards Without Sharing Too Much", "/blog/business-intelligence-part-17-who-sees-what/"),
            ("cta", "Read: Business Intelligence Series, Part 11: The Five-Minute Briefing for Decision Makers", "/blog/business-intelligence-part-11-five-minute-briefing/"),
            ("cta", "Read: Project Management Series, Part 27: Meetings That Decide, Agendas, Minutes and Action Items", "/blog/project-management-part-27-meetings-that-decide/"),
            ("ask", "Which page of your report do you think is opened most, and what would surprise you?"),
        ],
    },
    {
        "date": "March 21, 2027",
        "title": "Business Intelligence Series, Part 27: Maps by Barangay, When Location Is the Point",
        "slug": "business-intelligence-part-27-maps-by-barangay",
        "category": "bi",
        "summary": "A map can show at a glance which barangays collect more and which lag behind, if it is "
                   "built carefully. This part covers when a map helps, which Data Studio map types fit "
                   "barangay data, how to supply locations, the limits in Google’s documentation, and the "
                   "privacy line a treasury map must not cross.",
        "publish_on": "2027-03-21 21:00",
        "body": [
            "A councilor asked for “a map of collections,” so the analyst built one. Every barangay got a "
            "bubble sized by its real property tax collections. The Poblacion bubble was enormous and covered "
            "half the town. Three small upland barangays disappeared under it. The councilor looked for his "
            "own barangay, could not find it, and asked for the table instead.",
            "(The town, its barangays and the councilor’s request are invented to teach the technique.)",
            "Part 26 made charts readable for every viewer. This part adds a different kind of chart, the "
            "map. When you finish reading, you will know when a map is the right choice and when a sorted "
            "bar chart is better, which map types Data Studio offers and which suit barangay data, how to "
            "give each barangay a location, what limits to expect, and how to keep a treasury map from "
            "exposing anyone’s private data.",
            ("photo", "blog/bi-map.jpg", "Maps by barangay: use a map when location matters, a bubble for "
             "each barangay center, size for amount, color for performance, and never a dot for a "
             "taxpayer. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "When a Map Helps, and When It Does Not"),
            "Google’s help for Sheets describes a geo chart as a way to show a map of a country, continent or "
            "region. A map earns its place when the question is about where.",
            ("point", "A map helps", "“Are the barangays behind target clustered in one area?” “Which "
             "barangays along the highway grew fastest?” The pattern depends on location."),
            ("point", "A bar chart is better", "“Which barangay collected the most?” “Rank them from highest to lowest.” A sorted bar chart answers these more directly, because the bars sit side by side on one baseline, while circles on a map are scattered and hard to line up."),
            ("point", "Both, side by side", "A map for the pattern, with a sorted bar chart or table beside it for "
             "the exact numbers."),
            ("quote", "Use a map when the answer depends on where. Use a bar chart when it depends on how "
             "much."),
            ("h", "Map Types in Data Studio"),
            "Google’s reference for its Google Maps charts in Data Studio lists bubble, filled area, heatmap, "
            "line, connection and combo maps.",
            ("point", "Bubble map", "A circle at each location, sized and colored by metrics."),
            ("point", "Filled area map", "Shaded regions, such as countries or provinces."),
            ("point", "Heatmap", "A color gradient showing density."),
            ("point", "Line and connection maps", "Paths, or pairs of points joined by lines."),
            "For barangays, the bubble map is the practical choice, for a reason explained next.",
            ("h", "Giving Each Barangay a Location"),
            "Google’s geo dimension reference lists the place types Data Studio recognizes, from continent "
            "and country down to country subdivisions, city and postal code. It also accepts a field of "
            "latitude and longitude.",
            ("point", "Barangays are not on that list", "There is no barangay geo type, so Data Studio cannot "
             "draw barangay boundaries from a name alone."),
            ("point", "Use a center point", "Add a column to your barangay table with each barangay’s "
             "latitude and longitude in one cell, separated by a comma, in the form 14.5995,120.9842 (an example only). In the data "
             "source, set that field’s type to Latitude, Longitude."),
            ("point", "Bubble maps only", "The reference says filled area maps do not support latitude and "
             "longitude. Shaded barangay shapes would need boundary data, such as a BigQuery geography field, "
             "which is beyond this series."),
            "Take the center points from the official map your planning office uses, and record the source "
            "in the data dictionary from Part 10, so the next analyst can check them.",
            ("h", "Size and Color"),
            "A bubble map has two channels: size and color. The reference says color can come from a "
            "dimension or a metric, but not both.",
            ("point", "Size for amount", "Collections in pesos. Larger bubbles, larger amounts."),
            ("point", "Color for performance", "Percent of target, on a single-hue scale from Part 26, so "
             "darker means further along."),
            ("point", "Do not use both for the same thing", "If size and color both show collections, the "
             "map says one thing twice and another thing not at all."),
            "This answers the opening problem. With size for collections and color for percent of target, "
            "a small upland barangay that reached 95 percent shows as a small, dark bubble: easy to see, and "
            "fairly judged.",
            ("h", "The Big-Bubble Problem"),
            ("point", "Look at the scale", "When one barangay dwarfs the rest, its bubble can hide its "
             "neighbors. Show percent of target or collections per taxpayer instead of raw totals, so the "
             "large barangay is not the whole story."),
            ("point", "Zoom in", "Set the default view to the town, not the province, so bubbles have room."),
            ("point", "Add the table", "A table chart with the same data lets readers find their barangay "
             "by name."),
            ("h", "Why Not a Heatmap?"),
            "A heatmap shows where points are dense. With one point per barangay, there is no density to show: every barangay is a single point, and the gradient would mainly reflect how close barangay centers are to each other. A heatmap suits many individual points, such as thousands of events, and that kind of point data is exactly what a treasury map should avoid, as the next section explains.",
            ("h", "Explain the Map"),
            "A map invites questions about why a cluster looks the way it does. Part 25’s advice applies here too: a short note under the map, with a date and a source, saves a round of guesses. “Upland barangays: collection days moved to the barangay hall from February” tells the reader why those bubbles darkened.",
            ("h", "The Privacy Line"),
            "A treasury map must show places, not people. A bubble for each taxpayer’s address would reveal "
            "who owns what and who has not paid, which is personal information under the Data Privacy Act, "
            "as Part 20 of the Cybersecurity series discussed.",
            ("point", "Aggregate first", "Map totals by barangay, never individual records."),
            ("point", "Watch small counts", "If a barangay has only two business taxpayers, its total may "
             "reveal each one’s payment. Combine such barangays or leave them off the business tax map."),
            ("point", "Check who can see it", "Part 17 set out who sees what. A map is a report, and the same "
             "rules apply."),
            ("h", "Check It Before Sharing"),
            ("point", "Count the bubbles", "One per barangay, no more, no fewer."),
            ("point", "Check three locations", "Pick three barangays and confirm each bubble sits where it "
             "should."),
            ("point", "Compare the totals", "The sum of the bubbles should match the dashboard’s grand "
             "total."),
            ("h", "Mistakes to Avoid"),
            ("point", "A map for a ranking question", "Use a sorted bar chart."),
            ("point", "Raw totals only", "Large barangays hide small ones; add a rate or percent."),
            ("point", "Mapping individuals", "Aggregate by barangay and watch small counts."),
            ("point", "Unchecked coordinates", "One typo can put a barangay in the sea."),
            ("h", "Key Takeaways"),
            ("point", "Maps answer where", "Bar charts answer how much."),
            ("point", "Bubbles for barangays", "Using a latitude and longitude field for each center."),
            ("point", "Size and color mean different things", "Amount and performance."),
            ("point", "Places, not people", "Aggregate, and protect small counts."),
            ("h", "Your Part 27 Exercise"),
            "Use the practice dashboard from your earlier exercises.",
            ("point", "Add locations", "A latitude and longitude column for five practice barangays."),
            ("point", "Build a bubble map", "Size by collections, color by percent of target."),
            ("point", "Add the table", "Beside the map, sorted by percent of target."),
            "Then ask a colleague one question about location and one about amount, and see which chart they "
            "use to answer each.",
            "The analyst rebuilt the map with color for percent of target and a table beside it. The "
            "councilor found his barangay in the table, then on the map: a small, dark bubble in the hills, "
            "at 95 percent. He asked for a printed copy to bring to his barangay assembly.",
            ("cta", "Read: Business Intelligence Series, Part 26: Colors Everyone Can Read, Contrast, Labels and the Red-Green Trap", "/blog/business-intelligence-part-26-accessible-colors/"),
            ("cta", "Read: Business Intelligence Series, Part 17: Who Sees What, Sharing Dashboards Without Sharing Too Much", "/blog/business-intelligence-part-17-who-sees-what/"),
            ("cta", "Read: Business Intelligence Series, Part 10: Keeping BI Honest With a Data Dictionary, Owners and a Change Log", "/blog/business-intelligence-part-10-keeping-bi-honest/"),
            ("cta", "Read: Cybersecurity Series, Part 20: Privacy at Work, and the Data Privacy Act at Your Desk", "/blog/cybersecurity-part-20-privacy-at-work/"),
            ("ask", "Which question in your office is really about where, and still answered with a table?"),
        ],
    },
    {
        "date": "March 16, 2027",
        "title": "Business Intelligence Series, Part 26: Colors Everyone Can Read, Contrast, Labels and the Red-Green Trap",
        "slug": "business-intelligence-part-26-accessible-colors",
        "category": "bi",
        "summary": "A dashboard that depends on telling red from green leaves some readers guessing. This "
                   "part covers how common color vision deficiency is, the contrast levels in the W3C’s "
                   "accessibility guidelines, and practical ways to choose colors, labels and checks so "
                   "every reader gets the same message.",
        "publish_on": "2027-03-16 21:00",
        "body": [
            "The barangay status chart was the pride of the dashboard: green dots for barangays on target, "
            "red dots for those behind. At the briefing, one councilor studied it for a long time, then "
            "asked which barangays were behind. He could not tell the dots apart. Neither, it turned out, "
            "could one of the clerks, who had never mentioned it because nobody had asked.",
            "(The briefing, the councilor and the clerk are fictional, created for this lesson.)",
            "Part 25 added lines and notes to explain a chart. This part makes sure every reader can see the "
            "chart in the first place. Read to the end and you will know how common color vision deficiency "
            "is, what the W3C’s guidelines say about color and contrast, how to choose colors that survive "
            "it, how to add labels so color is never the only clue, and how to test a dashboard before it "
            "goes out.",
            ("photo", "blog/bi-colors.jpg", "Accessible colors: do not rely on color alone, keep enough "
             "contrast, avoid red against green, and test before sharing. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "How Common Is It?"),
            "Colour Blind Awareness, a UK organization, says color vision deficiency affects about 1 in 12 "
            "men, or 8 percent, and about 1 in 200 women. It describes red-green deficiency as the most "
            "common group of types.",
            "Picture a council of ten men and two women. Using those rates, the chance that at least one of them has a color vision deficiency works out to about 58 percent. That person may see a red-green chart differently from the one who designed it, and may never say so.",
            ("quote", "If the meaning is only in the color, part of your audience gets no meaning."),
            ("h", "What the Guidelines Say"),
            "The W3C’s Web Content Accessibility Guidelines, WCAG, are written for web content, and a "
            "dashboard shared as a web page is web content. Three success criteria apply directly to charts.",
            ("point", "1.4.1 Use of Color", "Color should not be the only visual means of conveying "
             "information. Part 18 used this rule for alerts."),
            ("point", "1.4.3 Contrast (Minimum)", "Text needs a contrast ratio of at least 4.5 to 1 against "
             "its background, or 3 to 1 for large text."),
            ("point", "1.4.11 Non-text Contrast", "Parts of graphics needed to understand the content, such "
             "as each line in a graph or each slice of a pie chart, need a contrast of at least 3 to 1 "
             "against adjacent colors."),
            "The W3C’s explanation of 1.4.11 also names ways around the 3 to 1 rule for graphics: visible "
            "labels and values that carry the same information, the same data in another form such as a "
            "table, or darker borders that separate the shapes. Lines in a graph, it says, need to contrast "
            "with the background but not necessarily with each other when they rarely cross.",
            ("h", "Choosing Colors That Work"),
            ("point", "Avoid red against green", "For “good” and “bad,” choose a pair that differs in both hue and lightness, such as dark blue and orange, and confirm it with the tests below."),
            ("point", "Vary lightness, not just hue", "A dark color next to a light one stays distinct even "
             "in grayscale. Two colors of the same lightness can merge."),
            ("point", "Fewer colors", "The more series a chart has, the more colors a reader must tell apart. Group the small ones as “Others” or split the chart."),
            ("point", "Keep meaning consistent", "If blue means collections on one chart, do not make it "
             "mean expenses on the next."),
            "In Data Studio, series colors are set in the Style tab of each chart, and a report theme can "
            "set default colors for all charts at once. Setting them once in the theme keeps them consistent.",
            ("h", "Color Scales for Amounts"),
            "Maps and heat tables use color for amounts, such as collections by barangay. The choice of scale changes what readers see.",
            ("point", "One hue, light to dark", "For amounts that only go up, such as collections, use a single color from light for small values to dark for large ones. Darker reads as more, even in grayscale."),
            ("point", "Two hues for above and below", "For a figure that can be above or below a target, use one color for each side and a neutral middle, so the target itself stands out."),
            ("point", "Avoid the rainbow", "A scale that runs through many hues has no natural order: readers cannot tell whether yellow means more than green without checking the legend."),
            ("h", "Never Let Color Work Alone"),
            ("point", "Direct labels", "Write the barangay name at the end of its line, instead of a legend "
             "the reader must match by color."),
            ("point", "Data labels", "Show the value on bars when there are only a few, so the number does "
             "not depend on reading the color or the axis."),
            ("point", "Words and symbols for status", "“On target” and “Behind” in a column, or a check mark "
             "and a warning sign, carry the meaning without color."),
            ("point", "A table beside the chart", "The W3C counts the same data in another form as a valid "
             "alternative."),
            ("h", "Test Before You Share"),
            ("point", "Print it in grayscale", "If two series look the same in gray, they rely on hue alone."),
            ("point", "Simulate color deficiency", "Chrome’s developer tools include a setting that emulates "
             "several types of color vision deficiency on any page, including a dashboard."),
            ("point", "Check the contrast ratio", "A free contrast checker takes two color codes and reports "
             "the ratio, so you can confirm 4.5 to 1 for text and 3 to 1 for chart parts."),
            ("point", "Ask a reader", "Show it to someone who did not build it and ask them to name what is "
             "behind target, without hints."),
            ("h", "A Worked Fix"),
            "The analyst rebuilt the barangay status chart in four changes.",
            ("point", "Colors", "Dark blue for on target, orange for behind, both checked against the white "
             "background."),
            ("point", "Words", "A status column next to each barangay: “On target” or “Behind.”"),
            ("point", "Order", "Barangays behind target sorted to the top, so the answer to the councilor’s "
             "question comes first."),
            ("point", "Numbers", "Each bar labeled with its percentage of target."),
            "In grayscale, the chart still worked. In the color deficiency simulation, it still worked. The "
            "words alone would have been enough.",
            ("h", "Mistakes to Avoid"),
            ("point", "Red and green as the only signal", "Add words, symbols or position."),
            ("point", "Pale text on pale backgrounds", "Check the 4.5 to 1 ratio for text."),
            ("point", "A rainbow of series", "Fewer colors, more labels."),
            ("point", "Skipping the test", "Grayscale and simulation take only a few minutes."),
            ("h", "Key Takeaways"),
            ("point", "It affects real readers", "About 1 in 12 men and 1 in 200 women, per Colour Blind "
             "Awareness."),
            ("point", "Three WCAG rules", "Not color alone, 4.5 to 1 for text, 3 to 1 for chart parts."),
            ("point", "Labels carry the meaning", "Direct labels, values, words and tables."),
            ("point", "Test it", "Grayscale, simulation, contrast checker and a fresh reader."),
            ("h", "Your Part 26 Exercise"),
            "Open the practice dashboard from your earlier exercises.",
            ("point", "Find one chart that relies on color", "Status dots, a red-green scale, or a legend "
             "with many series."),
            ("point", "Fix it", "Change the colors, add words or values, and sort the important items first."),
            ("point", "Test it", "Print it in grayscale and run the simulation in your browser."),
            "If the chart still tells the same story with the color turned off, it is ready for every reader. If it does not, add a label before you change any color.",
            "At the next briefing, the councilor read the status column aloud before the analyst could "
            "explain it. Afterward, the clerk stopped by her desk. “That is the first time I could read that "
            "chart,” he said. “I thought it was just me.”",
            ("cta", "Read: Business Intelligence Series, Part 25: Annotating Charts, Lines, Bands and Notes That Explain the Bumps", "/blog/business-intelligence-part-25-annotating-charts/"),
            ("cta", "Read: Business Intelligence Series, Part 18: Thresholds and Alerts, Letting the Dashboard Say When to Look", "/blog/business-intelligence-part-18-thresholds-and-alerts/"),
            ("cta", "Read: Business Intelligence Series, Part 12: Fast and Readable on a Phone", "/blog/business-intelligence-part-12-fast-and-readable-on-a-phone/"),
            ("cta", "Read: Business Intelligence Series, Part 20: Your First Data Studio Dashboard, Connected to Live Data", "/blog/business-intelligence-part-20-first-data-studio-dashboard/"),
            ("ask", "Which chart in your office would still make sense if it were printed in black and white?"),
        ],
    },
    {
        "date": "March 11, 2027",
        "title": "Business Intelligence Series, Part 25: Annotating Charts, Lines, Bands and Notes That Explain the Bumps",
        "slug": "business-intelligence-part-25-annotating-charts",
        "category": "bi",
        "summary": "A chart shows what happened; a note tells the reader why. This part shows how to add "
                   "reference lines and bands in Data Studio, which kind of line to use for a target or an "
                   "average, the limits to know, and how to write short notes that keep a chart honest.",
        "publish_on": "2027-03-11 21:00",
        "body": [
            "At the quarterly review, a councilor pointed at the collections chart. “What happened in the "
            "second week of July? It nearly drops to nothing.” The analyst who built the chart had moved to "
            "another office. Someone guessed a system problem. Someone else guessed a holiday. It took a "
            "phone call to learn the truth: a typhoon had closed the office for three days. The chart had "
            "shown the drop perfectly and explained none of it.",
            "(The office, the review and every number below are made up for this lesson. No real town or "
            "taxpayer is described.)",
            "Part 24 drew a line through the noise to show direction. This part adds the lines, shaded "
            "areas and words that tell a reader what they are looking at. You will finish knowing when a "
            "reference line helps, how to add one in Data Studio, how to shade a period with a reference "
            "band, the limits Google’s documentation lists, and how to write notes that a reader can trust "
            "a year later.",
            ("photo", "blog/bi-annotate.jpg", "Annotating charts: a line for the target, a band for the "
             "period that matters, a label with the value, and a short note for the why. (Illustration: "
             "Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Why a Chart Needs Words"),
            "A chart answers “what” well. It does not answer “compared with what?” or “why?” When a chart leaves those gaps open, readers may fill them with guesses. Three small additions close them, and none of them changes the data.",
            ("point", "A reference line", "Shows a level to compare against: a target, an average, last "
             "year’s figure."),
            ("point", "A reference band", "Shades a range of values or a stretch of dates, such as a "
             "deadline period."),
            ("point", "A note", "One sentence of text that explains an event the data cannot."),
            ("quote", "If the reader has to ask why, the chart is not finished."),
            ("h", "Adding a Reference Line"),
            "Google’s documentation for Data Studio gives the steps: edit the report, select the chart, open "
            "the Style tab in the properties panel, and click Add a reference line. It lists three types.",
            ("point", "Constant value", "A number you type, such as a daily collection target of ₱50,000. "
             "For a percentage, the documentation says to enter a decimal, so 50 percent is 0.5."),
            ("point", "Metric", "A metric in the chart combined with a calculation: Average, Median, "
             "Percentile, Min, Max or Total. An average line shows at a glance which days were above or "
             "below the usual level for the period shown."),
            ("point", "Parameter", "A single numeric parameter, which lets a reader type a value, such as "
             "their own target, and see the line move."),
            "Each line can carry a label. Leave it blank and Data Studio uses a default, such as the name "
            "of the calculation. A check box adds the line’s value to the label, so the reader sees "
            "“Target ₱50,000” rather than a line with no number.",
            ("h", "Target or Average?"),
            ("point", "Use a constant for a promise", "A target set by the office, a budget estimate divided "
             "by working days, a legal threshold. It stays the same whatever the data does."),
            ("point", "Use a metric for context", "An average or median line moves with the data and the "
             "filters. It answers “Was this day high or low for this period?”"),
            ("point", "Prefer the median for lumpy data", "A few very large days, such as the deadline rush, can pull an average up. The median is the middle value, so it stays near the typical day."),
            ("h", "Shading a Period With a Reference Band"),
            "A reference band has a beginning value and an ending value, each with its own type. On a chart "
            "whose x-axis is a date, the documentation says a date-range selector appears instead, so you "
            "can shade a stretch of days.",
            "For collections, the first twenty days of January are an obvious band. Under the Local "
            "Government Code, business taxes are due within that period, as Part 24 noted. Shading those "
            "days tells the reader that the high bars inside the band are expected, not a surprise.",
            ("point", "Background color and opacity", "Keep the band light so the bars stay readable."),
            ("point", "A label", "Write what the band is: “Business tax deadline, Jan 1–20.”"),
            ("h", "Limits Worth Knowing"),
            "Google’s documentation lists a few limits that can surprise a first-time user.",
            ("point", "Up to 10 lines per chart", "Two or three are easier to read on a small chart. Ten is the hard limit, not a goal."),
            ("point", "Numeric axes only for lines", "A reference line works on a numeric axis, not a date "
             "axis. To mark a date, use a band with the date-range selector."),
            ("point", "Stacked charts", "Stacked column and bar charts support fewer line types, and 100 "
             "percent stacked charts support none."),
            ("point", "What the chart shows", "A metric line is calculated only from the values currently "
             "displayed. Change a filter, and the average line changes with it."),
            "The last point matters most. If a reader filters the dashboard to one barangay, an average line "
            "becomes that barangay’s average. Say so in the label, for example “Average for the selection,” so nobody mistakes one barangay’s average for the whole town’s.",
            ("h", "Writing Notes That Last"),
            "Lines and bands mark levels and periods. Events need words. A text box beside or under the "
            "chart is enough.",
            ("point", "Date and fact", "“July 12–14: office closed, typhoon signal.” Not “bad week.”"),
            ("point", "Source", "Who confirmed it: the memo number, the advisory, the person."),
            ("point", "Kept with the data", "Keep a short events list, with a date and a note per row, in the "
             "same file as the data, so the next analyst finds it."),
            ("point", "Short", "One line per event. If a note needs a paragraph, it belongs in the report "
             "that goes with the dashboard."),
            ("h", "Check It Before Sharing"),
            ("point", "Read the line’s value", "Turn on the value in the label and compare it with the table "
             "or with your own calculation."),
            ("point", "Change a filter", "Watch which lines move. Constants should stay; metric lines should "
             "move. Label them so the reader knows which is which."),
            ("point", "Open it on a phone", "Part 12 showed how small screens crowd labels. Shorten any label "
             "that wraps or overlaps."),
            ("h", "Mistakes to Avoid"),
            ("point", "Unlabeled lines", "A line without a name and value invites guesses."),
            ("point", "Too many lines", "Two or three per chart is easier to read than ten."),
            ("point", "Average lines that ignore filters", "Label them as calculated from the selection."),
            ("point", "Notes without dates or sources", "A note no one can check is another guess."),
            ("h", "Key Takeaways"),
            ("point", "Lines compare", "A constant for a target, a metric for context."),
            ("point", "Bands mark periods", "Use the date-range selector to shade deadlines and closures."),
            ("point", "Know the limits", "Numeric axes only for lines, and metric lines follow filters."),
            ("point", "Notes explain", "Date, fact and source, kept with the data."),
            ("h", "Your Part 25 Exercise"),
            "Open the practice dashboard from your earlier exercises.",
            ("point", "Add a target", "A constant reference line on the daily collections chart, labeled "
             "with its value."),
            ("point", "Add a band", "Shade January 1 to 20 on a date chart and label it."),
            ("point", "Write two notes", "Pick two unusual days in your data and write one line each: date, "
             "fact and source."),
            "Then hand the chart to someone who has not seen it and ask what happened on those two days. "
            "If they can answer without asking you, the annotations work.",
            "The analyst added a light band for July 12 to 14, labeled “Office closed, typhoon,” with the "
            "memo number in a note below. At the next review, the councilor glanced at the dip, read the "
            "label, and moved on to the next question.",
            ("cta", "Read: Business Intelligence Series, Part 24: Trend Lines and Moving Averages, Seeing the Direction Without Guessing", "/blog/business-intelligence-part-24-trend-lines-and-moving-averages/"),
            ("cta", "Read: Business Intelligence Series, Part 18: Thresholds and Alerts, Letting the Dashboard Say When to Look", "/blog/business-intelligence-part-18-thresholds-and-alerts/"),
            ("cta", "Read: Business Intelligence Series, Part 12: Fast and Readable on a Phone", "/blog/business-intelligence-part-12-fast-and-readable-on-a-phone/"),
            ("cta", "Read: Business Intelligence Series, Part 11: The Five-Minute Briefing for Decision Makers", "/blog/business-intelligence-part-11-five-minute-briefing/"),
            ("ask", "Which bump in your office’s charts does everyone ask about, and nobody remembers?"),
        ],
    },
    {
        "date": "March 6, 2027",
        "title": "Business Intelligence Series, Part 24: Trend Lines and Moving Averages, Seeing the Direction Without Guessing",
        "slug": "business-intelligence-part-24-trend-lines-and-moving-averages",
        "category": "bi",
        "summary": "Daily collections jump up and down, and a busy chart hides the direction. This part shows how "
                   "to add a trend line or a moving average in Data Studio, which type to choose, why missing "
                   "days can drag a line to zero, and why a trend is not a forecast.",
        "publish_on": "2027-03-06 21:00",
        "body": [
            "The daily collections chart looked like a saw blade. Up on Monday, down on Wednesday, up on "
            "Friday, flat on weekends. The head of office squinted at it and asked the only question that "
            "mattered: “Are we going up or down?” Nobody in the room could say for sure.",
            "(The office, its people and its figures are invented. No real town or taxpayer is described.)",
            "Part 23 joined two sources in one chart. This part helps readers see the direction inside a "
            "noisy one. By the last section, you will know what a trend line and a moving average each show, "
            "how to add them to a Data Studio chart, which type fits which question, why missing dates can "
            "make a line fall to zero, and why a trend line should never be read as a promise about next "
            "month.",
            ("photo", "blog/bi-trend.jpg", "Trend lines and moving averages: smooth the noise, handle missing "
             "dates on purpose, and never read a trend as a forecast. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "Two Tools, Two Questions"),
            ("point", "Trend line", "One line through the whole period that answers: over these months, "
             "has the series generally gone up or down?"),
            ("point", "Moving average", "A line that follows the data but smooths out the day-to-day "
             "jumps, answering: what is the level lately, without the noise?"),
            "Both leave the original data on the chart. They add a reading aid; they do not replace the "
            "numbers.",
            ("quote", "The dots tell you what happened. The line helps you see where it was heading."),
            ("h", "What Data Studio Offers"),
            "Google’s reference for time series charts lists the trend line options in the Style tab, under "
            "the series settings. The reference notes that trend lines are available only for time series "
            "and scatter charts.",
            ("point", "Linear", "A straight line that, in the reference’s words, most closely approximates "
             "the data in the chart."),
            ("point", "Exponential", "A curve for data that grows or shrinks by a steady percentage rather "
             "than a steady amount."),
            ("point", "Polynomial", "A curve that can bend, which the reference suggests for large, highly "
             "variable data."),
            ("point", "Moving average", "Available only on time series charts. You set the number of periods "
             "to average."),
            "To add one: select the chart, open the Style tab, find the series, and choose a type from the "
            "Trendline menu. Weight, style and color options then appear.",
            ("h", "A Moving Average, by Hand"),
            "Before trusting the line, it helps to see the arithmetic once. Say five working days brought in "
            "₱38,000, ₱41,000, ₱36,000, ₱52,000 and ₱43,000.",
            ("point", "Add them", "₱38,000 + ₱41,000 + ₱36,000 + ₱52,000 + ₱43,000 = ₱210,000."),
            ("point", "Divide by five", "₱210,000 ÷ 5 = ₱42,000. That is the 5-day average for the fifth "
             "day."),
            ("point", "Slide one day", "On the sixth day, drop the first day and add the new one, then "
             "divide again. The window moves, which is why it is called a moving average."),
            "A longer window gives a smoother line that reacts more slowly. A shorter window reacts faster "
            "but stays bumpier. For daily collections, a window that covers one full working week keeps "
            "the weekly pattern from shaking the line.",
            ("h", "The Missing Days Trap"),
            "Treasuries do not collect on weekends and holidays, so those dates have no rows. Google’s "
            "reference describes three settings for missing data in a time series chart, and the default "
            "matters.",
            ("point", "Line To Zero, the default", "The line drops to zero for the missing dates. A chart of "
             "collections then dives to zero every Saturday and Sunday, and any trend line drawn on it is "
             "pulled down."),
            ("point", "Line Breaks", "Missing dates show as gaps. Honest, though the line looks broken."),
            ("point", "Linear Interpolation", "The line connects the points on either side of the gap. "
             "Smooth, but the eye may read the joined line as real days."),
            "For collections, Line Breaks shows the plain truth: there was no collection day. "
            "Whichever you choose, choose it on purpose, and say so in a note on the chart.",
            ("h", "Which Type to Choose"),
            ("point", "For a quick “up or down?”", "Linear, over a period long enough to include several "
             "of the usual cycles."),
            ("point", "For the level lately", "A moving average, with a window of one working week for daily "
             "data or three months for monthly data."),
            ("point", "Use the curves with care", "Exponential and polynomial lines can fit the past "
             "nicely and still say little about what comes next. If you cannot explain why the data should "
             "curve, use linear."),
            ("h", "Seasons Break Straight Lines"),
            "Local collections follow the calendar. Under the Local Government Code, business taxes are due "
            "in the first twenty days of January or of each quarter, and real property tax installments fall "
            "due by the end of each quarter. Collections can bunch up around those dates. A linear trend "
            "drawn from January to June starts at a high point and may slope down even in a good year.",
            ("point", "Compare like with like", "Part 19 compared this January with last January. For "
             "seasonal data, that comparison says more than a trend line across different months."),
            ("point", "Pick the window with the season in mind", "A trend across whole years, or a moving "
             "average across a full quarter, is less fooled by the January rush."),
            ("h", "A Trend Is Not a Forecast"),
            "A trend line describes the past. Extending it into next month assumes nothing changes: the same "
            "taxpayers, the same rates, the same calendar. Ordinances change, businesses open and close, and "
            "a typhoon can close the office for days. If the dashboard shows a trend, label it “trend, "
            "past data” and keep it inside the dates you actually have.",
            ("h", "Labeling It So Readers Understand"),
            ("point", "Name the line", "In the legend or a text box: “7-day moving average” or “linear "
             "trend, January to June.”"),
            ("point", "Keep the raw data visible", "Use a lighter color for the daily values and a darker, "
             "thicker line for the trend."),
            ("point", "Note the missing-data setting", "One line under the chart: “Weekends and holidays "
             "shown as gaps.”"),
            ("h", "Check It Before Sharing"),
            ("point", "One average by hand", "Pick one point on the moving average and recompute it from "
             "the table, as above."),
            ("point", "Toggle the missing-data setting", "If the trend changes direction when you switch "
             "from Line To Zero to Line Breaks, the zeros were driving it."),
            ("point", "Change the window", "If a 5-day and a 10-day average tell opposite stories, the "
             "direction is not yet clear, and the chart should say so."),
            ("h", "Mistakes to Avoid"),
            ("point", "Leaving Line To Zero on for working-day data", "Weekends become fake crashes."),
            ("point", "Reading a trend as a forecast", "It describes the past only."),
            ("point", "Fitting curves without a reason", "Default to linear unless you can explain the curve."),
            ("point", "Hiding the raw data", "Show the daily values in a lighter color."),
            ("h", "Key Takeaways"),
            ("point", "Trend line and moving average answer different questions", "Overall direction versus "
             "recent level."),
            ("point", "Missing dates need a decision", "The default draws them as zero."),
            ("point", "Seasons matter", "Compare like periods, or use windows that cover full cycles."),
            ("point", "Label everything", "Name the line, the window and the missing-data choice."),
            ("h", "Your Part 24 Exercise"),
            "Use the practice dashboard from your earlier exercises.",
            ("point", "Add a moving average", "On the daily collections time series, with a window of five."),
            ("point", "Flip the missing-data setting", "Compare Line To Zero with Line Breaks and note what "
             "changes."),
            ("point", "Check one point", "Recompute one moving-average value by hand."),
            "Write one sentence under the chart that a reader can trust. If you cannot write it, the chart "
            "is not ready yet.",
            "The analyst switched the chart to Line Breaks, added a 5-day moving average and labeled both. "
            "The saw blade was still there in light gray, but a dark line now rose gently from March to May. "
            "The head of office read the label, then the line, and finally had an answer.",
            ("cta", "Read: Business Intelligence Series, Part 23: Blending Data, Two Sources in One Chart", "/blog/business-intelligence-part-23-blending-data/"),
            ("cta", "Read: Business Intelligence Series, Part 19: Fair Comparisons, This Month, Last Month and Last Year", "/blog/business-intelligence-part-19-fair-comparisons/"),
            ("cta", "Read: Business Intelligence Series, Part 14: The Date Table, a Calendar Your Dashboard Can Count On", "/blog/business-intelligence-part-14-the-date-table/"),
            ("cta", "Read: Business Intelligence Series, Part 20: Your First Data Studio Dashboard, Connected to Live Data", "/blog/business-intelligence-part-20-first-data-studio-dashboard/"),
            ("ask", "Which chart in your office would be easier to read with a moving average?"),
        ],
    },
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
            "(The office and the people in this story are invented, and so are the figures. No real town or "
            "taxpayer is described.)",
            "Part 22 built new measures from a single source. This part brings a second source into the same "
            "chart. Stay with me to the end, and you will know what a blend is in Data Studio, when to blend and "
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
            "One detail is easy to miss. The documentation explains that before merging, Data Studio groups "
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
            "(Everyone and everything in this story is fictional, including the numbers. No real town or "
            "taxpayer is described.)",
            "This part covers calculated fields in Data Studio. After this post, you will know what a "
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
            "(The office and the people in this story are invented, and so are the figures. No real town or "
            "taxpayer is described.)",
            "This part gathers the earlier parts of this series into one plan, in the order the work is "
            "actually done. Stay with me to the end, and you will have a four-week plan for a first treasury BI "
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
            "(Everyone and everything in this story is fictional, including the numbers. No real town or "
            "taxpayer is described.)",
            "This part builds that view in Data Studio, Google’s free web tool for reports and dashboards. It "
            "was called Looker Studio until April 2026, the name used in Part 17. After this post, you will know how to prepare a sheet for a dashboard, connect it, check its fields, add a scorecard, a "
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
            "(The office and the people in this story are invented, and so are the figures. No real town or "
            "taxpayer is described.)",
            "Part 14 built a date table, and Part 18 set thresholds on weekly totals. Both rely on comparing "
            "one period with another. Stay with me to the end, and you will know four questions to ask before any "
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
            "(Everyone and everything in this story is fictional, including the numbers. No real town or "
            "taxpayer is described.)",
            "Part 3 chose what to watch, and Part 16 added checks that stop bad data. This part adds "
            "thresholds: rules that point to the numbers that need attention. After this post, you will know four ways to set a threshold, why every alert needs an owner and an action, how to "
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
            "(The office and the people in this story are invented, and so are the figures. No real town or "
            "taxpayer is described.)",
            "Part 4 put an access line in the BI brief, and Part 13 planned where each reader’s drill path "
            "stops. This part is about the settings that carry out those decisions. Stay with me to the end, and you will know how file sharing settings work, why a separate file for sharing is safer than a "
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
            "(Everyone and everything in this story is fictional, including the numbers. No real town or "
            "taxpayer is described.)",
            "Part 7 explained what a pipeline does: extract, transform and load. Part 15 flattened the revenue "
            "account levels during that loading step. This part builds a small pipeline in Google Sheets, which is free to use with a Google account. After this post, you will know how to lay out a pipeline in one "
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
            "(The office and the people in this story are invented, and so are the figures. No real town or "
            "taxpayer is described.)",
            "Part 14 built the date table, one of the dimensions in the model. This part looks at dimensions "
            "that have levels inside them. Stay with me to the end, and you will know what makes a design a star or "
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
            "(Everyone and everything in this story is fictional, including the numbers. No real town or "
            "taxpayer is described.)",
            "Part 5 introduced facts and dimensions. This part builds a dimension that treasury "
            "models rely on: the date table. After this post, you will know what a date table is, which "
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
            "(The office and the people in this story are invented, and so are the figures. No real town or "
            "taxpayer is described.)",
            "Part 12 made the view readable on a phone. This part makes it useful for the second question. "
            "By the last section, you will know the difference between a filter and a drill-down, how to "
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
            "(The story is made up for teaching, and so are its office, people and figures. No real town or "
            "taxpayer is described.)",
            "Part 4 asked who reads each view and on what device. This part is about acting on the answer. "
            "By the end of this post, you will know how to lay out a BI view for a phone, which charts work "
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
            "(This is a teaching case: the office, its staff and its figures are fictional. No real town or "
            "taxpayer is described.)",
            "Parts 8 to 10 covered how BI views are built and kept trustworthy. This part is about the moment "
            "someone has to act on them. When you finish reading, you will have a five-minute structure, a way "
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
            "(The story is made up for teaching, and so are its office, people and figures. No real town or "
            "taxpayer is described.)",
            "Parts 7 to 9 made the pipeline reliable. This part is about keeping the meaning reliable. After this post, you will know how to write a data dictionary, which owners a small BI setup "
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
            "(This is a teaching case: the office, its staff and its figures are fictional. No real town or "
            "taxpayer is described.)",
            "Part 7 added four basic checks to the nightly pipeline: count, total, completeness and a run log. "
            "This part turns them into a full test plan. Read to the end and you will know five more kinds of tests, how to respond when a test fails, and how to try a "
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
            "(The story is made up for teaching, and so are its office, people and figures. No real town or "
            "taxpayer is described.)",
            "Parts 6 and 7 built the warehouse and the pipeline that fills it. This part is about the views "
            "people actually look at. By the last section, you will know the three kinds of BI views, what "
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
            "(This is a teaching case: the office, its staff and its figures are fictional. No real town or "
            "taxpayer is described.)",
            "Part 6 introduced the nightly copy from the working database to the warehouse. Stay with me to the end, and you will know the two main patterns for that copy, ETL and ELT, what each does well, which "
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
            "(The story is made up for teaching, and so are its office, people and figures. No real town or "
            "taxpayer is described.)",
            "In Part 5, we shaped the data into a star: facts in the middle, dimensions around them. This part "
            "is about where that star should live. By the end of this post, you will know the difference "
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
            "(This is a teaching case: the office, its staff and its figures are fictional. No real town or "
            "taxpayer is described.)",
            "In Part 4, the BI brief defined each measure in plain words. This part is about the tables that "
            "hold those measures. That design is called the data model, and it decides whether a dashboard "
            "gives the same answer as the cashier. When you finish reading, you will know the four ideas behind a sound model (facts, dimensions, grain and keys), and you will be able to sketch one for "
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
            "(The story is made up for teaching, and so are its office, people and figures. No real town or "
            "taxpayer is described.)",
            "In Part 3, I listed six measures a treasury could watch every day. This part goes one step earlier. Before you choose a single measure, find out who will use the dashboard and what they will decide with it, then write it down on one page. I call that page the BI brief. Read to the end and you will have five interview questions, a six-line template and a filled-in example you can copy.",
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
            "(This is a teaching case: the office, its staff and its figures are fictional. No "
            "real town or taxpayer is described.)",
            "In Part 1, I described BI as a service that keeps answers coming. This part is about"
            " choosing which answers deserve that treatment. The secret is to move from one-time "
            "questions to a short list of measures that are watched every day, each with a clear "
            "limit that tells you when to act. By the last section, you will be able to tell "
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
            "because each one fails in its own way and each one is fixed in its own way. By the end of this post, you will know the three kinds of BI work, how each one fails, and "
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
