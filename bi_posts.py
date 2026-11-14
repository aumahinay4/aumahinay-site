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
            "A pipeline can fail in two ways. A loud failure stops the run with an error, and someone notices "
            "the missing data. A quiet failure finishes normally but loads something wrong. The opening story "
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
