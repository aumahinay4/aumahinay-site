"""Data Analytics blog series (Butch 2026-11-13 PH): one part every Tuesday at 9 pm PH, a year or more.

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
        "title": "Data Analytics Series, Part 1: What Data Analytics Really Is, and Why Every Office Already Has the Data",
        "slug": "data-analytics-part-1-what-it-is",
        "category": "data",
        "summary": "Data analytics is the craft of turning everyday records into answers people can act on. "
                   "Here is what it means, the four kinds of questions it can answer, a famous map from 1854, "
                   "and why a local treasury is already sitting on a mountain of useful data.",
        "publish_on": "2026-11-17 21:00",
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
            "I completed the Google Data Analytics Professional Certificate on Coursera, and later the advanced "
            "course that followed it. What I learned there did not stay in the classroom. It shaped how I think "
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
            ("h", "A Map That Saved Lives"),
            "One of the most famous stories in this field happened long before computers. On August 31, 1854, "
            "cholera broke out in Soho, a crowded neighborhood in London. Hundreds of people died within days. "
            "Most doctors at the time believed the disease spread through foul air.",
            "A physician named John Snow suspected the water instead. He gathered the addresses of the people "
            "who had died and marked each death on a street map. The marks crowded around one public water pump "
            "on Broad Street. He also checked the exceptions. Workers at a nearby brewery, who drank beer and "
            "water from the brewery's own well, were largely spared.",
            "On September 7, Snow presented his findings to the local parish board. The next day, the handle of "
            "the pump was removed so no one could use it. Snow himself noted that the outbreak was already "
            "slowing by then, partly because many residents had fled. That honesty is part of the lesson. His "
            "evidence was strong enough to act on, and he did not claim more than it showed.",
            "Snow had no spreadsheet, no database and no software. He had a clear question, carefully collected "
            "records, a simple picture that made the pattern obvious, and the courage to bring it to the people "
            "who could act. Those four things are still the heart of data analytics today.",
            ("h", "Four Kinds of Questions"),
            "Analysts often sort their work into four types, each answering a different question. Here they are "
            "with treasury examples.",
            ("point", "Descriptive: What happened?", "Total collections last month by revenue source. This is "
             "the most common kind of analysis, and the base for everything else."),
            ("point", "Diagnostic: Why did it happen?", "Business tax collections fell 12% compared with last "
             "January. Was it fewer businesses, smaller declared sales, or simply that the deadline fell on a "
             "weekend and payments slipped into February?"),
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
