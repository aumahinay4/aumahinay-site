"""Project Management blog series (Butch 2026-11-13 PH): Part 1 live Nov 13, 2026 (Butch: "post part 1 of the
series today"), then one part every Thursday at 9 pm PH ("YYYY-MM-DD 21:00"), 52 parts in all (last part
November 11, 2027).

The outline follows Butch's own 52-week plan in Google Drive (four quarters of 13: starting a project; time and
money; people and problems; delivery and closing). Every part is told through local treasury work: real property
tax drives, collection systems, accountable forms, year-end closing. Every office, person and number in an example
is made up. The wording is the blog's own, not the course's or the Drive drafts'. Per Butch: no Sources section,
no "coming next" teaser, "Read:" links checked, one own-made white picture with ALTOS colour rings.
Newest first, like BLOG in content.py.
"""

SERIES = "Project Management Series"

PM_POSTS = [
    {
        "date": "November 13, 2026",
        "title": "Project Management Series, Part 1: The Accidental Project Manager in the Treasury",
        "slug": "project-management-part-1-accidental-project-manager",
        "category": "pm",
        "summary": "Nobody in a local treasury applies to be a project manager, yet many of us end up as one. "
                   "Here is how a project differs from daily work, the three limits every project lives with, "
                   "and four moves to make in your first two weeks.",
        "publish_on": "2026-11-13",
        "body": [
            "It is the second week of October. The head of the treasury calls a revenue clerk into the office. "
            "“You are good with computers. Before the January rush, I want our real property tax "
            "ledger cards encoded into the new system, so we can print bills instead of writing them by hand. "
            "Work with the assessor’s office and the collectors. Can you handle it?”",
            "The clerk says yes. Of course she says yes. Then she walks back to her desk and realizes three things "
            "at once. Nobody on that list reports to her. Every one of them already has a full day of work. And "
            "she has never run anything like this before.",
            "(As in every part of this series, the office, the people and the numbers are made up. No real "
            "town or employee is described.)",
            "If that scene feels familiar, welcome. You have just become what people in the field call an "
            "accidental project manager. It happens all the time in government offices, and almost nobody "
            "applies for the role.",
            ("h", "Why I Am Writing This Series"),
            "I completed the Google Project Management Professional Certificate on Coursera, and later the Google "
            "Stakeholder Management specialization. My own biggest project so far is ALTOS, a treasury "
            "system for Philippine local treasuries. It has been built and tested on the developer side only. "
            "Building software is not part of my official duties, so before any office can put it to real use, the "
            "documents must come first, beginning with a memorandum of agreement. That order, paperwork before "
            "launch, is itself a project management lesson.",
            "Most project management lessons online talk about product launches, marketing campaigns and "
            "software companies. The ideas are good, but the examples feel far from a municipal hall. In this "
            "series, I will explain the same ideas in plain words, with examples from treasury work: tax "
            "campaigns, new systems, year-end closing, audits and the people at the counter. The goal is simple: "
            "to help you take any assignment like the one above and run it with confidence.",
            ("h", "Is It a Project, or Is It Just Work?"),
            "Start with the most useful question in the whole field. Not everything you do at work is a project, "
            "and mixing the two up causes a lot of stress.",
            ("point", "Operations", "The work that repeats. Issuing official receipts, preparing the daily "
             "report of collections and deposits, answering taxpayers at the window, filing monthly reports. "
             "It never finishes. Tomorrow you do it again, and the office has a routine for it."),
            ("point", "A project", "Work with a start, an end and a result that did not exist before. Encoding "
             "the ledger cards, setting up a new collection system, holding a one-month tax campaign in the "
             "far barangays, or moving the records room. When the result is delivered, the project is over."),
            "The Project Management Institute, the group behind the widely used PMBOK Guide, puts it "
            "simply: a project is a temporary effort to create a unique product, service or result. Two words "
            "matter there. Temporary means it ends. Unique means the office has not done this exact thing "
            "before, so there is no routine to follow.",
            "Here is a quick test you can use on any new assignment. Does it have a finish line? Will something "
            "exist afterward that does not exist now? Will you need people from outside your own desk to get "
            "there? If the answer to all three is yes, you are holding a project.",
            "Why does the label matter? Because operations run on habit, and projects cannot. The daily routine "
            "has an established way of doing things. A project has surprises, gaps and questions nobody has "
            "answered yet. If you try to run it like routine work, squeezing it into the spare minutes between "
            "taxpayers, it will drift for months. A project needs its own plan, its own time and someone whose "
            "job is to steer it.",
            ("h", "The Three Limits Every Project Lives With"),
            "Every project is held in place by three limits. Textbooks call them the triple constraint, and many "
            "people draw them as a triangle.",
            ("point", "Scope", "What you will deliver. In our example: which ledger cards get encoded, which "
             "fields, and which bills the system must print."),
            ("point", "Time", "When it must be done. Here, before the January rush, when owners line up to pay "
             "and the office has no spare hands."),
            ("point", "Cost", "What you can spend, including people’s hours. Two encoders for six weeks is a "
             "cost, even if no one is paid extra."),
            "In the middle of the triangle sits quality: whether the result is accurate and actually works. The "
            "rule is simple and unforgiving. You cannot pull one side without moving another. If you add to the "
            "scope, you need more time or more people. If you cut the time, you must cut the scope or add "
            "people. If you refuse to change anything else, the middle gives way, and quality is what breaks.",
            ("photo", "blog/pm-triple-constraint.jpg", "Scope, time and cost hold each other in place. Push one "
             "side and another must move, or quality in the middle pays the price. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            "Picture this in our office. Halfway through, someone says, “While you are at it, encode the "
            "business records too.” If the deadline and the two encoders stay the same, the team will rush. "
            "Assessed values get typed wrong, a few hundred cards get skipped, and in January a property owner is "
            "billed for land she sold years ago. Nobody decided to lower quality. It simply happened because the "
            "triangle was ignored.",
            "The fix is not to refuse. It is to offer a clear choice. “Yes, we can add the business records. "
            "We can push the finish by three weeks, borrow one more encoder from another unit, or finish the "
            "property cards first and do business records as a second phase. Which do you prefer?” That "
            "one sentence turns a complaint into a decision, and it puts the decision with the person who has "
            "the authority to make it.",
            ("quote", "You cannot add to a project for free. Something always pays: time, people, or quality."),
            ("h", "The Life of a Project, From Start to Finish"),
            "Projects move through stages. The Google course teaches four: initiate, plan, execute and close. "
            "The PMBOK Guide also names a fifth kind of work, monitoring and controlling, which is not a "
            "separate stage but runs alongside the doing. Here are all five in plain words, using our ledger "
            "project.",
            ("point", "Initiate", "Agree on why the project exists and what success looks like. For example: "
             "all active property accounts encoded and checked, so bills print from the system by January."),
            ("point", "Plan", "Break the work into tasks, decide who does each one and in what order, and list "
             "what could go wrong, such as missing cards or a printer that fails."),
            ("point", "Execute", "Do the work. Encoders type, collectors check accounts in their area, and "
             "the project manager removes whatever is blocking them."),
            ("point", "Monitor and control", "Compare the plan with what is really happening, every week. "
             "Are we on pace? Are new requests sneaking in? Adjust early, while problems are still small."),
            ("point", "Close", "Hand the result to the people who will use it every day, store the records, "
             "and sit down for half an hour to talk about what to keep and what to change next time."),
            "Many projects do not fail at the doing. They fail at the very beginning, "
            "because nobody agreed on what “done” means, or at the very end, because the work was never "
            "handed over properly and slowly slid back to the old way.",
            ("h", "Your First Two Weeks: Four Moves"),
            "When a project lands on your desk, the temptation is to start working right away. Resist it for a "
            "few days. These four moves will save you weeks later.",
            ("point", "1. Talk to the person who asked", "In project language, this is the sponsor: the head "
             "of office or official who owns the result. Ask three questions. What will tell you this was a "
             "success? What is not included? And if something has to give, which matters most: the deadline, "
             "the scope or the budget?"),
            ("point", "2. Put it on one page", "Write down the goal, the deadline, the people involved and what "
             "is left out. Send it back to the sponsor and ask them to confirm. This short page will settle "
             "many arguments before they start."),
            ("point", "3. Ask the people doing the work before you promise a date", "The collectors and clerks "
             "know their busy weeks. In a treasury, the days before each quarterly real property tax deadline "
             "(March 31, June 30, September 30 and December 31) are not the time to borrow anyone. A schedule "
             "built with the people who will follow it is a schedule they will defend."),
            ("point", "4. Keep one place for everything", "One shared folder or one board for the task list, "
             "the decisions and the files. Not five chat groups, three notebooks and a stack of memos. Agree on "
             "a simple rule: if a decision is not written there, it was not made."),
            ("h", "The Dispatcher, Not the Driver"),
            "Capable people often fall into the same trap when they lead their first project. When an encoder "
            "falls behind, they stay late and encode the cards themselves. When the system shows an error, they "
            "spend two days fixing it alone. Meanwhile, nobody is watching the schedule, the sponsor hears "
            "nothing, and the project quietly stalls.",
            "Think of a jeepney dispatcher at a busy terminal. The dispatcher does not drive any of the jeeps. "
            "Yet without someone keeping the line moving, calling the next trip and sorting out the jam at the "
            "gate, the whole terminal grinds to a halt. That is the project manager’s job. Your value is "
            "not the number of tasks you finish with your own hands. It is how clearly everyone knows the goal, "
            "how quickly blocks are cleared, and whether the project reaches the end.",
            "You may still do some of the work, especially in a small office. Just know which hat you are "
            "wearing at any moment, and never let the doing crowd out the steering.",
            ("h", "Your Part 1 Exercise"),
            "Pick one assignment you are carrying now, big or small. This week, write one line for "
            "each of these:",
            ("point", "Project or operations?", "Does it have a finish line and a new result at the end?"),
            ("point", "Who decides it is done?", "Name the one person whose approval ends the project."),
            ("point", "Which limit is tightest?", "Scope, time or cost. Which one can you not move?"),
            "If you cannot answer one of them, that is your first task: a fifteen-minute talk with the person "
            "who gave you the assignment.",
            ("cta", "Read: Why I Built ALTOS", "/blog/why-i-built-altos/"),
            ("cta", "Read: The ALTOS Framework, Principle 4: Every Owner Has a Deadline",
             "/blog/altos-framework-every-owner-has-a-deadline/"),
            ("cta", "Read: Year-End in the Treasury", "/blog/year-end-in-the-treasury/"),
            ("cta", "Read: Data Analytics Series, Part 1", "/blog/data-analytics-part-1-what-it-is/"),
            ("ask", "Have you ever been handed a project at work without being told it was one? How did it go?"),
        ],
    },
]
