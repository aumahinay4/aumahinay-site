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
            "Anyone who reads the bulletin board now knows what her business paid, and from that, roughly how "
            "much it earns. No name appeared on the chart. It still pointed to one person.",
            "(As always in this series, the office, the people and the numbers are made up. No real town or "
            "taxpayer is described.)",
            "Part 5 touched on privacy when choosing tools. This part goes further, because analysts make "
            "privacy decisions every time they choose what to collect, what to keep and what to show. By the "
            "end of this post you will know the three principles the Data Privacy Act asks every analysis to "
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
            "(As always in this series, the office, the people and the numbers are made up. No real town or "
            "taxpayer is described.)",
            "In Part 4, a whole analysis was done in a spreadsheet. This part widens the view to five kinds "
            "of free tools, what each one is good for, and where each one stops. By the end of this post you "
            "will be able to pick the right free tool for a task, know the limits to watch for, and set up a "
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
            "(As always in this series, the office, the people and the numbers are made up. No "
            "real town or taxpayer is described.)",
            "This part is about what happens next in an office that thinks like an analyst. It is"
            " not about fancy tools. It is about a habit: checking what the records say before "
            "deciding, and being honest about what they cannot say. By the end of this post, you "
            "will know how to weigh experience against records, five thinking habits analysts "
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
            "the final decision. By the end of this post, you will know the six steps of every "
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
