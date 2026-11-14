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
        "date": "November 16, 2026",
        "title": "Business Intelligence Series, Part 2: The BI Team, Role by Role",
        "slug": "business-intelligence-part-2-the-bi-team",
        "category": "bi",
        "summary": "Behind every dashboard that people trust are three kinds of work: building the pipes, building "
                   "the screens and explaining what the numbers mean. Here is each BI role in plain words, and "
                   "how one person in a small treasury can wear all three hats.",
        "publish_on": "2026-11-16 21:00",
        "body": [
            "A head of office opens a collections dashboard on a Monday morning and sees that market fees are "
            "down by a third compared with the same week last year. She calls the person who made the "
            "dashboard. “Is this real?”",
            "That question has three possible answers, and each one belongs to a different kind of work. Maybe "
            "the data never arrived because the evening export failed. That is a pipeline problem. Maybe the "
            "chart is adding the wrong field, or the filter is stuck on one barangay. That is a dashboard "
            "problem. Or maybe the numbers are correct, and something really did happen at the market. That is "
            "a question of meaning, and somebody has to go and find out what it was.",
            "(As always in this series, the office, the people and the numbers are made up. No real town or "
            "taxpayer is described.)",
            "In a large organization, three different people would take that call. In a small treasury, it is "
            "often one person. Either way, it helps to know the three jobs apart, because each one fails in its "
            "own way and each one is fixed in its own way.",
            ("photo", "blog/bi-roles.jpg", "The BI loop: people bring questions, an engineer builds the pipes, a "
             "developer builds the screens, and an analyst explains what the numbers mean. (Illustration: "
             "Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Start With the People Who Ask"),
            "Every BI system exists because somebody needs to know something, again and again. In BI language, "
            "these people are the stakeholders. In a local treasury, they include the head of office, the "
            "revenue and cash divisions, the collectors in the field, the budget and accounting offices, and the "
            "local chief executive who asks how the town is doing against its revenue target.",
            "Stakeholders do not need to know how the data moves. They need to say clearly what they want to "
            "watch and what they will do when the number changes. A head of office who says “I want to see "
            "everything” has not yet asked a question. One who says “I want to know by noon each day whether "
            "yesterday’s collections were deposited in full” has asked a very good one.",
            "That is why every BI role, whatever the title, begins by listening. The rest of the team turns "
            "those questions into something that answers itself every day.",
            ("h", "The BI Engineer: Building the Pipes"),
            "The BI engineer makes sure the right data arrives in the right place, on time and in good shape. "
            "If BI is a road from the payment counter to the decision maker, the engineer builds and maintains "
            "the road.",
            ("point", "What the work looks like", "Connecting to the sources, such as the collection system, "
             "the cashbook or the list of business permits. Writing the steps that copy the data out on a "
             "schedule. Combining it into clean tables. Setting up checks so that a missing day or a repeated "
             "receipt number is caught before anyone builds a chart on top of it."),
            ("point", "The tools", "Usually SQL, often a scripting language such as Python, and a database or "
             "data warehouse. Small offices can do the same work with a spreadsheet, a free database such as "
             "SQLite, and a scheduled task on one computer."),
            ("point", "How it fails", "Quietly. The dashboard still shows numbers, but they are a day old, half "
             "complete or counted twice. Nobody notices until a total does not match the official report."),
            "When the head of office asks “Is this real?”, the engineer’s first move is to check that "
            "yesterday’s data actually arrived and passed its checks. It is not glamorous work, but every "
            "other role depends on it.",
            ("h", "The BI Developer: Building the Screens"),
            "The BI developer turns clean tables into something people can read and use: dashboards, reports, "
            "filters and alerts. If the engineer builds the road, the developer builds the place where people "
            "stop and look.",
            ("point", "What the work looks like", "Deciding which measures go on the screen and how each one "
             "is calculated. Choosing the right chart for each measure. Adding date controls and filters so "
             "users can ask follow-up questions. Making sure the layout still works on a phone, because that is "
             "where many busy officials will see it."),
            ("point", "The tools", "Dashboard tools such as Looker Studio, Power BI or Tableau, plus a good "
             "working knowledge of SQL so the developer can shape the data the screens need."),
            ("point", "How it fails", "Loudly but misleadingly. A chart that sums when it should count, a "
             "filter that silently hides half the data, or two screens that define “collections” in "
             "two different ways. Each looks fine on its own, and together they start arguments."),
            "In the market fee example, the developer checks that the chart is reading the right field, that no "
            "filter is left on, and that “this week” on the dashboard means the same days as "
            "“this week” in the head of office’s mind.",
            ("h", "The BI Analyst: Explaining What It Means"),
            "The BI analyst stands between the numbers and the people. The analyst helps stakeholders turn "
            "vague worries into clear questions, decides with them which measures matter, and explains what a "
            "change on the dashboard really means.",
            ("point", "What the work looks like", "Interviewing stakeholders about the decisions they make. "
             "Writing down each measure in plain words, so “collections” always means the same "
             "thing. Spotting unusual patterns, digging into them and reporting the cause. Suggesting "
             "improvements to the dashboard when people keep asking the same follow-up question."),
            ("point", "The tools", "A spreadsheet, SQL, the dashboard tool itself and, most of all, good "
             "conversation and clear writing."),
            ("point", "How it fails", "By staying at the desk. An analyst who never asks the collectors or the "
             "market supervisor what happened will report a drop without explaining it."),
            "In our example, the engineer and the developer both confirm that the data is complete and the "
            "chart is correct. So the analyst calls the market supervisor and learns that one row of stalls "
            "was closed for repairs for two weeks. The drop is real, it has a cause, and it will end. The head "
            "of office now knows not to send collectors out to chase payments that cannot happen yet.",
            ("quote", "The engineer makes the number arrive. The developer makes it visible. The analyst makes "
             "it mean something."),
            ("h", "Titles Vary, the Work Does Not"),
            "Job titles in BI are not standard. One organization’s BI engineer is another’s data "
            "engineer. Some companies call the dashboard builder a BI analyst, others a report developer. In "
            "smaller teams, one person often does the analyst and developer work together. Do not worry about "
            "the labels. Look at the three kinds of work, because those stay the same everywhere.",
            "BI work also connects with nearby roles. Database administrators keep the systems that hold the "
            "data running and secure. Data analysts, the subject of my other series, take on one-time questions "
            "that may later grow into something a dashboard should watch every day. Records officers and data "
            "protection officers decide who may see what, which matters a great deal when the data includes "
            "taxpayers’ names and properties.",
            ("h", "One Person, Three Hats"),
            "Most local treasuries will never hire a BI team. That is fine. What matters is that someone in the "
            "office knows when to switch hats.",
            ("point", "Monday morning: engineer hat", "Before opening the dashboard, check that the weekend’s "
             "files arrived and the totals match the cashbook. Five minutes here saves an hour of confusion later."),
            ("point", "Midweek: developer hat", "Fix the chart someone found confusing. Add the filter the "
             "collectors keep asking for. Remove a measure nobody uses."),
            ("point", "Any time a number moves: analyst hat", "Ask what happened before reporting that "
             "something did. Talk to the people closest to the money."),
            "Keeping the three hats separate also helps when something goes wrong. Instead of saying “the "
            "dashboard is broken”, you can say which part failed: the data, the screen or the "
            "explanation. That makes the fix faster and the conversation calmer.",
            ("h", "Skills That Matter in Every Role"),
            "Whatever hat you wear, a few skills carry across all three.",
            ("point", "Curiosity about the work behind the data", "Knowing how an official receipt is issued, "
             "cancelled or reported tells you more about the data than any tool can."),
            ("point", "Care with definitions", "Agree in writing on what each measure means and keep that "
             "list where everyone can see it."),
            ("point", "Respect for privacy", "Show totals, not names, unless a person truly needs to see "
             "individual records for their work."),
            ("point", "Plain communication", "Explain what changed, why it matters and what to do, in words a "
             "busy official can read in one minute."),
            ("h", "Your Part 2 Exercise"),
            "Take the repeated report you circled in Part 1, or pick one now. Then write three short lines:",
            ("point", "Engineer", "Where does the data for this report come from, and how would you know if "
             "one day’s data were missing?"),
            ("point", "Developer", "If this report became a single screen, which three measures would go at "
             "the top?"),
            ("point", "Analyst", "Who reads this report, and what decision do they make with it?"),
            "If you cannot answer the last line, talk to the reader before changing anything else. A report "
            "that drives no decision is the first one to simplify.",
            ("cta", "Read: Business Intelligence Series, Part 1", "/blog/business-intelligence-part-1-same-data-different-jobs/"),
            ("cta", "Read: Data Analytics Series, Part 2", "/blog/data-analytics-part-2-six-steps/"),
            ("cta", "Read: Project Management Series, Part 1", "/blog/project-management-part-1-accidental-project-manager/"),
            ("cta", "Read: Your Data at the Treasury Counter", "/blog/your-data-at-the-treasury-counter/"),
            ("ask", "In your office, which hat do you wear most often: the pipes, the screens or the meaning?"),
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
            "On the first working day of every month, a clerk in a municipal treasury starts the same task. "
            "She opens last month's file, copies in the new receipts, fixes the formulas that broke, and "
            "rebuilds the collections report for the head of office. It takes two days. By the time the "
            "report is printed, the numbers are already a week old, and next month she will do it all again.",
            "(As always on this blog, the office, the people and the numbers are made up. No real town or "
            "taxpayer is described.)",
            "Nothing is wrong with the clerk's work. The totals are correct. The problem is that the same "
            "questions are asked every month, and every month the answers are built from scratch. Business "
            "intelligence, or BI, is the discipline that fixes exactly this kind of problem, and it is the "
            "subject of this series.",
            ("h", "Why a Second Series?"),
            "My Data Analytics series walks through the full craft of analysis: asking a good "
            "question, preparing and cleaning data, analyzing it and sharing what you found. That series already "
            "covers spreadsheet formulas, pivot tables, SQL basics and choosing the right chart.",
            "After finishing the Google Data Analytics certificate, I went on to the Google Business "
            "Intelligence certificate. It made me see the same data from a different angle. Analytics taught "
            "me how to answer a question. BI taught me how to make sure the answer keeps arriving, correct and "
            "on time, without anyone rebuilding it by hand. Both matter in a local treasury, so each gets its "
            "own series.",
            ("h", "Same Data, Different Jobs"),
            "The simplest way to tell the two apart is to look at what each one delivers.",
            ("point", "A data analyst delivers an answer", "Someone asks a question, such as whether the office "
             "needs a second payment window. The analyst gathers the data, studies it and reports a finding. "
             "The work has a beginning and an end."),
            ("point", "A BI professional delivers a system", "Someone needs to watch the same measures again and "
             "again, such as daily collections by revenue source. The BI professional builds the data flow, the "
             "model and the dashboard that keep those answers up to date for everyone who needs them."),
            "In other words, analytics is usually a project, while BI is usually a service. An analyst might "
            "discover that business tax payments drop sharply in the second half of January. A BI system would "
            "show that drop every day, as it happens, so the office can act before the month ends.",
            "The two overlap a great deal. Good BI depends on the habits of analysis: clear questions, clean "
            "data and honest measures. Good analysis, in turn, often starts with a pattern someone noticed on a "
            "BI dashboard.",
            ("quote", "Analytics answers a question once. BI keeps the answer coming."),
            ("h", "Where the Name Came From"),
            "The phrase is older than computers. In 1865, Richard Millar Devens used “business intelligence” "
            "in a book of commercial stories to describe a banker, Sir Henry Furnese, who profited by gathering "
            "news about events in Europe and acting on it before his competitors. The idea was simple: whoever "
            "has better information, sooner, makes better decisions.",
            "In 1958, Hans Peter Luhn, a researcher at IBM, published a paper titled “A Business Intelligence "
            "System.” He described a machine that would automatically sort incoming documents and send each "
            "one to the people in an organization who needed it. He thought of intelligence as the ability to "
            "understand how facts relate to each other well enough to guide action toward a goal. That is still "
            "a good definition today.",
            "The modern meaning took shape around 1989, when Howard Dresner, who later worked as an analyst at "
            "the research firm Gartner, proposed business intelligence as an umbrella term for concepts and "
            "methods that improve decisions using fact-based support systems. Since then the tools have changed "
            "many times, from printed reports to data warehouses to live dashboards on a phone. The goal has "
            "not changed at all.",
            ("h", "What a BI System Is Made Of"),
            "A BI system sounds expensive, but its parts are easy to understand. Think of it as a road from the "
            "payment counter to the decision maker.",
            ("photo", "blog/bi-system-flow.jpg", "A BI system is a road from the records to the decision: data "
             "comes from its sources, a pipeline moves and checks it, a model organizes it, a dashboard shows "
             "it, and people decide. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("point", "Sources", "Where the records are born: the collection system, the cashbook, the "
             "real property tax roll, the list of business permits."),
            ("point", "Pipeline", "The steps that copy data out of each source on a schedule, check it, and "
             "combine it. In BI language this is called ETL, for extract, transform and load."),
            ("point", "Model", "The organized store where the data waits, arranged so questions are fast and "
             "totals always agree. In larger offices this is a data warehouse."),
            ("point", "Dashboard", "The screen or report where people see the measures they care about, "
             "usually with filters so they can ask their own follow-up questions."),
            ("point", "People", "The head of office, the collectors and the budget officer who read the numbers "
             "and decide what to do. Without this last step, the rest is decoration."),
            "Each of these parts can be built in a small version with free tools, which is what makes BI "
            "practical even for a small office.",
            ("h", "Back to the Monthly Report"),
            "Let us return to the clerk and her two-day report. Here is how the same work looks with even a "
            "very simple BI setup.",
            "The collection system exports the day's receipts into a shared folder every evening. A small, "
            "scheduled step reads the file, checks that no receipt number is missing or repeated, and adds the "
            "new rows to one clean table. A free dashboard tool, such as Looker Studio, is connected to that "
            "table. It shows collections by revenue source, by month and against target, and it updates itself.",
            "The head of office now opens the dashboard on a phone whenever she wants. The clerk no longer "
            "rebuilds the report. Instead, she spends her time on the questions the dashboard raises, such as "
            "why market fees in one barangay are lower than last year. That is analysis, and it is a far better "
            "use of a skilled person's day.",
            "Notice that nothing in this example needs a large budget. It needs clear measures, clean data and "
            "someone who knows how the pieces fit together.",
            ("h", "What BI Is Not"),
            "Three misunderstandings are worth clearing up early.",
            ("point", "It is not just pretty charts", "A dashboard built on messy data spreads wrong numbers "
             "faster. Most of the real work in BI happens before anything is drawn."),
            ("point", "It is not expensive software", "Commercial tools exist, but a treasury can start with a "
             "spreadsheet, a small database and a free dashboard tool."),
            ("point", "It does not replace judgment", "A dashboard can show that collections dropped. It cannot "
             "tell you whether to send notices, extend a deadline or fix the encoding backlog. People still decide."),
            "That last point is the same one I made when I built ALTOS: every number the system produces is a "
            "prompt for a person to look and decide, never an automatic action.",
            ("h", "How This Series Works"),
            "The series has five modules. The first explains what BI is and who does it. The second covers "
            "data models, the way tables are arranged so totals are fast and always agree. The third covers "
            "pipelines, which move data from the counter to the report and test it along the way. The fourth "
            "builds dashboards and reports people actually use. The fifth covers privacy, keeping a BI system "
            "honest over time, presenting to executives, and a final project that puts everything together.",
            "Where a topic is already explained in the Data Analytics series, the posts link to it instead of "
            "repeating it. All examples use made-up data, and every tool used is free.",
            ("h", "Your Part 1 Exercise"),
            "Take ten minutes and do this:",
            ("point", "List your repeated reports", "Write down every report your office prepares again and "
             "again, daily, weekly, monthly or quarterly."),
            ("point", "Time them", "Next to each one, estimate how many hours it takes to prepare and how old "
             "the numbers are by the time someone reads them."),
            ("point", "Circle one", "Pick the report that costs the most time and is read most often. That is "
             "your first BI candidate: the place where a simple BI setup would save the most time."),
            ("cta", "Read: Data Analytics Series, Part 1", "/blog/data-analytics-part-1-what-it-is/"),
            ("cta", "Read: Why I Built ALTOS", "/blog/why-i-built-altos/"),
            ("cta", "Read: The ALTOS Framework, Principle 9: Evidence Before Decision",
             "/blog/altos-framework-evidence-before-decision/"),
            ("ask", "Which report in your office would you most like to stop rebuilding by hand? Tell me, and "
             "it may become an example in this series."),
        ],
    },
]
