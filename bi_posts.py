"""Business Intelligence Sunday series (Butch 2026-11-13 PH): 20 parts, one every Sunday from
March 14 to July 25, 2027, after "Inside the Local Treasury" ends on March 7.

The series follows what Butch learned in the Google Business Intelligence certificate, retold in the
blog's own words with made-up treasury examples. It links to the Tuesday Data Analytics series for
spreadsheet formulas, pivot tables, SQL basics and chart choice instead of teaching them again.
Facts are checked privately before each part is approved; per Butch, posts show no Sources section
and no "coming next" teaser. Category "data" so the Blog filter pills stay on one line on phones.
Newest first, like BLOG in content.py.
"""

SERIES = "Business Intelligence Series"

BI_POSTS = [
    {
        "date": "March 14, 2027",
        "title": "Business Intelligence Series, Part 1: Same Data, Different Jobs",
        "slug": "business-intelligence-part-1-same-data-different-jobs",
        "category": "data",
        "summary": "Business intelligence and data analytics use the same records but do different jobs. "
                   "Here is what BI really means, where the name came from, what a BI system is made of, "
                   "and how a monthly treasury report can stop being rebuilt by hand.",
        "publish_on": "2027-03-14",
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
