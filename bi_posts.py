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
