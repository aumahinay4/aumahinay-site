"""Data Analytics blog series (Butch 2026-11-13 PH): Part 1 live Nov 13, 2026 (Butch: "post this first part today"),
then one part every Tuesday at 9 pm PH ("YYYY-MM-DD 21:00"), a year or more.

The series teaches the whole craft in plain words, from asking a good question to acting on the answer,
with examples from local treasury work. Every number, office and taxpayer in an example is made up.
The wording is the blog's own, not the course's or the ALTOS book's. Facts are checked privately
before each part is approved; per Butch, posts show no Sources section and no "coming next" teaser.
Newest first, like BLOG in content.py.
"""

SERIES = "Data Analytics Series"

DATA_POSTS = [
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
            "Every week, someone in a government office opens a spreadsheet, scrolls through a few thousand "
            "rows, makes a chart and sends it to the boss. Sometimes it helps. Often it does not, and nobody can "
            "say exactly why. The chart was correct. The numbers added up. Yet no decision came out of it.",
            "Most of the time, the problem is not the math. It is the order of the work. The person started with "
            "the data and hoped a question would appear. Good analysis runs the other way around, and it follows "
            "a set of steps that experienced analysts repeat almost without thinking.",
            "In Part 1, we described data analytics as the craft of turning everyday records into answers people "
            "can act on. This part "
            "lays out the road from the first question to the final decision. The rest of the series walks down "
            "that road one step at a time.",
            ("h", "Six Steps, in Plain Words"),
            "The Google Data Analytics Professional Certificate teaches the process as six phases: Ask, Prepare, "
            "Process, Analyze, Share and Act. Other courses and companies use different names. An older and "
            "widely used model called CRISP-DM, developed in the late 1990s, also has six phases, starting with "
            "understanding the business problem and ending with putting the results to use. The labels differ, "
            "but the logic is the same everywhere. Here is that logic in my own words.",
            ("point", "Ask", "Decide exactly what you need to know, who needs to know it, and what they will "
             "do with the answer."),
            ("point", "Prepare", "Find the data that can answer the question, and check where it came from and "
             "whether it can be trusted."),
            ("point", "Process", "Clean the data: fix errors, remove duplicates, handle blanks and make the "
             "format consistent."),
            ("point", "Analyze", "Organize the clean data, calculate, compare and look for patterns that answer "
             "the question."),
            ("point", "Share", "Show the findings to the people who decide, in a form they can understand "
             "quickly."),
            ("point", "Act", "Make the decision, carry it out, and measure again to see whether it worked."),
            ("quote", "Start with the question, not the spreadsheet."),
            ("photo", "blog/data-six-steps.jpg", "The six steps of an analysis form a loop: after Act, you measure "
             "again and, if needed, start over with a sharper question. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            "The best way to understand the six steps is to watch them at work. So let us follow one ordinary "
            "office problem from beginning to end.",
            ("h", "A Worked Example: Do We Need a Second Window?"),
            "Imagine a municipal treasury with one payment window for walk-in taxpayers. (As always in this "
            "series, the office and the numbers are made up.) Every few weeks someone complains about the long "
            "line. A staff member suggests opening a second window. The head of office cannot simply say yes, "
            "because a second window means moving a person away from other work. She wants evidence first.",
            ("h", "Step 1: Ask"),
            "The first version of the question is “Are the lines too long?” That sounds reasonable, but "
            "it cannot be answered. Too long for whom? Every day, or only on some days? Compared with what?",
            "A better question is specific and tied to a decision: “On which days and hours does the wait at "
            "the payment window go beyond 30 minutes, and would a second window on those days alone fix it?”",
            "Now everyone knows what a good answer looks like. It also tells us who the answer is for, the head "
            "of office, and what she will do with it: decide whether to open a second window, and when. Notice "
            "that the question already hints at a cheaper option than a full-time window. Good questions often "
            "do.",
            ("h", "Step 2: Prepare"),
            "Next, find the data. Every payment produces an official receipt with a date and, in many systems, "
            "a time. That gives us when each transaction was finished. It does not tell us when each person "
            "joined the line, which is what waiting time really is.",
            "So the analyst has two choices: use the receipt times as a stand-in, or collect new data. In our "
            "example, the office does both. It pulls a full year of receipt times from its records. Then, for two "
            "weeks that include the busy days before the March 31 real property tax deadline, a staff member "
            "writes down the time each person takes a queue number and the time the person "
            "is served.",
            "This step is also where we check the data. Who recorded it? Is it complete, or are some days "
            "missing? Were the receipt clocks set correctly? A receipt system whose clock runs ten minutes "
            "fast will quietly distort every result that follows.",
            ("h", "Step 3: Process"),
            "Real records are messy. When our analyst opens the files, the problems appear quickly:",
            ("point", "Duplicates", "A few receipts were printed twice after a printer jam and appear twice in "
             "the export."),
            ("point", "Cancelled receipts", "Some receipts were cancelled and reissued, so counting them would "
             "inflate the number of transactions."),
            ("point", "Inconsistent times", "The handwritten log mixes “2:15 PM” with “14:15” "
             "and, on one page, just “2:15”."),
            ("point", "Gaps", "One afternoon has no handwritten entries at all because the staff member was "
             "called to a meeting."),
            "Cleaning means removing the duplicates, leaving out cancelled receipts, writing every time in one "
            "format and marking the afternoon with no entries as missing instead of pretending it was quiet. "
            "Each change is written down, so anyone can see what was done and why. This step is rarely exciting, "
            "but it is where many analyses are won or lost.",
            ("h", "Step 4: Analyze"),
            "With clean data, the analyst can finally count and compare. The two-week log shows how long each "
            "person waited, and it reveals a simple link: once one window gets more than about 25 payers in an "
            "hour, the wait climbs past 30 minutes. The analyst then counts receipts by day and by hour across "
            "the whole year to find every hour above that level. Three patterns stand out:",
            ("point", "The rush is predictable", "Most long waits happen in the first three weeks of January "
             "and in the days just before each quarterly real property tax deadline."),
            ("point", "Mornings are worse", "On busy days, the line peaks between 9 and 11 in the morning. "
             "Afternoons are usually calm."),
            ("point", "Ordinary days are fine", "On most days, the window serves well under 25 payers an "
             "hour, and the log shows typical waits of under ten minutes."),
            "The answer to the question is now clear. Waits go beyond 30 minutes on about twenty-five "
            "mornings a year, all of them predictable. A second window every day would sit idle most of the "
            "time. A second window on those mornings would cover nearly all the long waits.",
            ("h", "Step 5: Share"),
            "The head of office does not need the spreadsheet. She needs the answer, the evidence and a "
            "recommendation, on one page. The analyst prepares a simple bar chart showing, for each month, how "
            "many morning hours had more than 25 payers, a short table of the peak days and hours, and three sentences:",
            "“Long waits are not an everyday problem. They happen on about twenty-five predictable "
            "mornings a year, mostly in January and before quarterly deadlines. Opening a second window on those "
            "mornings only would cover nearly all of them, without taking a person away from other work for the "
            "rest of the year.”",
            "Notice what is left out: the cleaning details, the formulas and the dozens of other charts the "
            "analyst made while exploring. Those stay in the analyst's notes in case someone asks. Sharing is about "
            "what the decision maker needs, not about showing how hard the analyst worked.",
            ("h", "Step 6: Act"),
            "The head of office approves a second window on peak mornings and posts the schedule at the "
            "entrance and on the town's page. That is the decision. But the process is not finished.",
            "After the next January, the office keeps the two-week waiting log again, and the analyst compares "
            "the new numbers with the old ones. Did waits drop below 30 minutes? Did "
            "the second window get used? If the answer is yes, the change stays. If not, the office goes back to "
            "Step 1 with a sharper question. This loop is the quiet strength of the process. Every decision "
            "becomes a small experiment, and every experiment teaches the office something.",
            ("h", "What Goes Wrong When a Step Is Skipped"),
            "Each step protects against a common mistake. It helps to know them by name.",
            ("point", "Skipping Ask", "You produce a beautiful report that answers nothing. Everyone nods, and "
             "nothing changes."),
            ("point", "Skipping Prepare", "You trust data you should not. The clock was wrong, half the days "
             "were missing, or the file was last month's."),
            ("point", "Skipping Process", "Duplicates and cancelled receipts inflate the totals, and a correct "
             "formula gives a wrong answer."),
            ("point", "Skipping Analyze", "You jump from a hunch to a conclusion. “Everyone knows "
             "January is busy” is true, but it does not tell you how many staff you need or when."),
            ("point", "Skipping Share", "The findings stay in the analyst's head or laptop, and the "
             "people who decide never see them."),
            ("point", "Skipping Act", "The report is filed, the meeting ends, and the same problem returns next "
             "year."),
            ("h", "The Steps Are a Loop, Not a Ladder"),
            "In practice, analysts move back and forth. While cleaning, you may discover that a key field was "
            "never recorded, which sends you back to Prepare. While analyzing, you may find that the question "
            "was too narrow, which sends you back to Ask. That is normal. The six steps are a guide for "
            "thinking, not a form to fill in from top to bottom.",
            "What matters is that each step happens at least once, and that Ask comes first. A clear question "
            "makes every later step easier, because it tells you which data to look for, what to clean, what "
            "to calculate and what to show.",
            ("h", "Where the Six Steps Live in a Treasury System"),
            "A good information system can make some steps much lighter. When I designed ALTOS for Philippine "
            "local treasuries, I tried to support the steps that usually take the most effort. Receipts and "
            "deposits are recorded as they happen, with their dates and amounts, so the Prepare step does not "
            "start with a box of paper. Checks for duplicates and missing details help the Process step. Reports "
            "and charts make Share faster.",
            "But no system can do Ask or Act for you. Choosing the right question and making the decision remain "
            "human work, and that is exactly as it should be.",
            ("h", "Your Part 2 Exercise"),
            "Take the question you wrote down after Part 1. If you did not do it yet, choose one now. Then "
            "write one or two lines for each step:",
            ("point", "Ask", "Rewrite your question so it is specific and names the decision it supports."),
            ("point", "Prepare", "List the data you would need, and where each piece comes from."),
            ("point", "Process", "Guess the three most likely problems in that data."),
            ("point", "Analyze", "Write the calculation or comparison that would answer the question."),
            ("point", "Share", "Name the person who needs the answer, and the one chart you would show them."),
            ("point", "Act", "Write what would change, and how you would know if it worked."),
            "If you can fill in all six, you already have the plan for a real analysis.",
            ("cta", "Read: Data Analytics Series, Part 1", "/blog/data-analytics-part-1-what-it-is/"),
            ("cta", "Read: The ALTOS Framework, Principle 9: Evidence Before Decision",
             "/blog/altos-framework-evidence-before-decision/"),
            ("cta", "Read: Year-End in the Treasury", "/blog/year-end-in-the-treasury/"),
            ("cta", "Try the free Python lesson: Build a simple RCD summary with pandas",
             "/tutorials/rcd-summary-with-pandas/"),
            ("ask", "Which step do you find hardest in your own work: asking the right question, finding the "
             "data, cleaning it, or getting people to act on it?"),
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
            "Picture a Monday morning in a municipal treasury office. The mayor calls and asks a simple "
            "question: “Will we reach our real property tax target this year?” Someone opens a "
            "logbook. Someone else starts adding up receipt stubs from the past months. By lunchtime, the office "
            "has a total, but not yet an answer.",
            "(As in all my examples, the office and the numbers are made up. No real taxpayer or town is "
            "described.)",
            "The answer was in the office all along. It was written, line by line, on thousands of official "
            "receipts: who paid, how much, for what, and on which day. What was missing was a way to turn those "
            "records into something the mayor could decide on. That way has a name. It is data analytics, and "
            "this post starts a long series about it.",
            ("h", "Why I Am Writing This Series"),
            "I completed the Google Data Analytics Professional Certificate on Coursera, and later the Google "
            "Advanced Data Analytics Professional Certificate. What I learned there did not stay in the classroom. It shaped how I think "
            "about treasury records, and it became one of the foundations of ALTOS, the system I built for "
            "Philippine local treasuries.",
            "Most data analytics lessons online use examples from online shops, streaming apps or bike rentals. "
            "Those are fine, but they can feel far from a town hall in the province. In this series, I will "
            "explain the same ideas in plain words, with examples from the work I know: collections, "
            "disbursements, targets, deadlines and the people at the counter. My goal is simple. By the end, "
            "you should be able to take a real question at work and answer it with data, step by step.",
            ("h", "Data, Information and Insight"),
            "Three words are often mixed up, so let us start there. Think of them as three steps on a ladder.",
            ("point", "Data", "Raw facts, recorded one at a time. A single official receipt is data: receipt "
             "number 1234567, dated March 3, ₱2,450.00, real property tax, paid by a named owner, "
             "received by a named collector. On its own, one receipt tells you very little."),
            ("point", "Information", "Data that has been organized so it means something. “We collected "
             "₱1.8 million in real property tax in the first quarter” is information. It came from "
             "hundreds of receipts, added up and grouped by period."),
            ("point", "Insight", "Information that explains something and points to an action. “Most of "
             "the shortfall comes from three barangays where no collection day was held this year” is an "
             "insight. It tells the office where to look and what to do next."),
            "Data analytics is the work of climbing that ladder on purpose: from scattered records, to organized "
            "information, to an insight that someone can act on.",
            ("quote", "Data is what happened. Insight is what you can do about it."),
            ("h", "So What Is Data Analytics?"),
            "Here is a working definition in plain words. Data analytics is the practice of collecting, "
            "cleaning, organizing and examining data in order to answer questions and support decisions.",
            "Notice the last part. Analytics is not about producing more reports or prettier charts. It exists "
            "to help a person decide something: where to send collectors, when to open an extra window, which "
            "accounts to follow up first, or whether a new procedure is working.",
            "You will also hear two related terms. A data analysis is one investigation, such as checking why "
            "collections dropped in May. Data analytics is the whole discipline around it: the process, the "
            "tools, the habits and the people. Data science is a wider field still. It includes building new "
            "statistical models and machine learning systems. A good analyst borrows from it, but most "
            "everyday questions in an office can be answered without it.",
            ("h", "A Cholera Outbreak and a Famous Map"),
            "One of the most famous stories in this field happened long before computers. On August 31, 1854, "
            "cholera broke out in Soho, a crowded neighborhood in London. Hundreds of people died within days. "
            "Most doctors at the time believed the disease spread through foul air.",
            "A physician named John Snow suspected the water instead. He went through the records of who had "
            "died and where they had lived, and he asked families where they drew their water. Again and again, "
            "the answer led to one public pump on Broad Street. He also studied the exceptions. A brewery stood "
            "nearby, but none of its workers was recorded as dying of cholera. They drank the beer they were "
            "given, and the brewery had its own deep well.",
            "On September 7, Snow presented his findings to the local parish board. The next day, the handle of "
            "the pump was removed so no one could use it. Snow himself noted that the outbreak was already "
            "slowing by then, and that many residents had fled. That honesty is part of the lesson. His "
            "evidence was strong enough to act on, and he did not claim more than it showed.",
            "A few months later, Snow drew the picture that made the case famous. On a street map of the area, "
            "he placed a small mark for each death at its address. The marks pile up around the Broad Street "
            "pump and thin out farther away. Anyone could see the pattern in seconds, even without reading his "
            "tables.",
            "Snow had no spreadsheet, no database and no software. He had a clear question, carefully collected "
            "records, the courage to bring his evidence to the people who could act, and a simple picture that "
            "made the pattern plain to everyone. Those four things are still the heart of data analytics today.",
            ("h", "Four Kinds of Questions"),
            "Analysts often sort their work into four types, each answering a different question. Here they are "
            "with treasury examples.",
            ("point", "Descriptive: What happened?", "Total collections last month by revenue source. This is "
             "the most common kind of analysis, and the base for everything else."),
            ("point", "Diagnostic: Why did it happen?", "Business tax collections fell 12% compared with last "
             "January. Was it fewer businesses, smaller declared sales, or simply that more owners chose to pay "
             "in quarterly installments instead of the full year at once?"),
            ("point", "Predictive: What is likely to happen?", "Based on the pattern of the past three years, "
             "where will real property tax collections probably end by December, and how wide is the range of "
             "likely results?"),
            ("point", "Prescriptive: What should we do?", "Given the forecast, which barangays should get a "
             "collection day first, and which delinquent accounts deserve a personal visit rather than a "
             "letter?"),
            "Each type builds on the one before it. You cannot explain a drop you have not measured, and you "
            "cannot plan around a forecast you do not trust. That is why this series spends a lot of time on "
            "the first steps, which many people rush through.",
            ("h", "You Do Not Need Expensive Software"),
            "A common worry is that analytics needs costly tools or a degree in mathematics. It does not. Most "
            "useful analysis in a small office can be done with tools that are free or already installed:",
            ("point", "A spreadsheet", "Google Sheets, LibreOffice Calc or Excel. Sorting, filtering, "
             "formulas and pivot tables will take you remarkably far."),
            ("point", "A database and SQL", "When records grow into tens of thousands of rows, a database such "
             "as SQLite keeps them organized, and SQL is the language for asking it questions."),
            ("point", "A charting tool", "A good chart can make a pattern obvious in seconds, as Snow's map did. "
             "Spreadsheets and free tools such as Looker Studio can do this."),
            ("point", "A programming language", "Python, later on, for work that is repeated every month or is "
             "too large for a spreadsheet. My free Python tutorials already cover some of this."),
            "The tool matters less than the thinking. A clear question answered with a simple spreadsheet is "
            "worth more than a beautiful dashboard that answers nothing.",
            ("h", "The Analyst's Mindset"),
            "Good analysts share a few habits. They are curious and keep asking why. They learn the context, "
            "because a number means nothing until you know how it was recorded. A dip in collections may be a "
            "real problem, or it may be a week of encoding that has not been posted yet. They are healthy "
            "skeptics who check their own results before trusting them. And they remember that behind every "
            "row there is a person.",
            "That last habit matters a great deal in government. Treasury records hold names, addresses, "
            "property details and amounts paid. In the Philippines, the Data Privacy Act of 2012 (Republic Act "
            "No. 10173) sets the rules for handling personal information. An analyst should work with the "
            "least personal data the question needs. Totals by barangay, for example, rarely need anyone's "
            "name. I wrote about this in more detail in a separate post on data at the treasury counter.",
            ("h", "Where ALTOS Fits"),
            "When I built ALTOS, I kept one lesson from analytics in front of me: an answer is only as good as "
            "the records behind it. So ALTOS records each receipt and each deposit as the transaction happens, "
            "instead of copying figures later from paper. Collections can then be compared with targets by "
            "month and by revenue source, and year-end results can be forecast with an honest range rather than "
            "a single hopeful number.",
            "Just as important, every result in ALTOS is treated as a prompt for a person to decide, never as "
            "an automatic action. Data can point to where a problem might be. People still have to look, judge "
            "and act. That idea runs through this whole series.",
            ("h", "How This Series Works"),
            "This is a long series, with one part every Tuesday evening for a year and more. It follows the "
            "path of a complete analysis: asking the right question, finding and preparing the data, cleaning "
            "it, analyzing it, sharing what you found, and acting on it. Along the way it covers spreadsheets, "
            "SQL, charts, dashboards, basic statistics, forecasting and Python, always with examples you can "
            "try yourself. Each part stands on its own, so you can start anywhere, but reading in order will "
            "make the most sense.",
            ("h", "Your Part 1 Exercise"),
            "Analytics is learned by doing. Before you read any further in this series, try these three small "
            "steps:",
            ("point", "Write down one question", "Pick a real question from your work that you wish you could "
             "answer with numbers. For example: Which month brings in the most collections? Or: How many days "
             "does it take for a voucher to be paid?"),
            ("point", "List the records that already exist", "Write down every logbook, register, report or "
             "file that holds part of the answer. You will probably find more than you expect."),
            ("point", "Name the decision", "Write down who would use the answer and what they would do "
             "differently. If no one would act on it, choose a better question."),
            "Keep that page. It will be useful again and again as the series goes on.",
            ("cta", "Read: Your Data at the Treasury Counter", "/blog/your-data-at-the-treasury-counter/"),
            ("cta", "Read: Why I Built ALTOS", "/blog/why-i-built-altos/"),
            ("cta", "Read: The ALTOS Framework, Principle 9: Evidence Before Decision",
             "/blog/altos-framework-evidence-before-decision/"),
            ("cta", "Try the free Python lesson: Add up a day's collections", "/tutorials/add-up-daily-collections/"),
            ("ask", "What question at your office would you most like to answer with data? Tell me, and it may "
             "become an example in this series."),
        ],
    },
]
