"""Project Management blog series (Butch 2026-11-13 PH): Part 1 live Nov 13, 2026 (Butch: "post part 1 of the
series today"), then one part every few days at 9 pm PH ("YYYY-MM-DD 21:00") in the daily blog rotation
(Butch 2026-11-14), 52 parts in all.

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
        "date": "November 23, 2026",
        "title": "Project Management Series, Part 3: Mapping Who Holds the Power",
        "slug": "project-management-part-3-stakeholder-mapping",
        "category": "pm",
        "summary": "Every project has people who can help it, stop it or simply be affected by it. Here is how to "
                   "list them, place them on a power and interest grid, and decide how to work with each one, "
                   "using the treasury encoding project as the example.",
        "publish_on": "2026-11-23 21:00",
        "body": [
            "The real property tax encoding project now has a signed one-page charter. The revenue clerk feels "
            "ready. Then, a week later, a message arrives from the office of the local chief executive. "
            "The mayor heard that “the treasury is changing the tax bills” and wants to know why nobody told "
            "the mayor’s office before taxpayers started asking.",
            "Nothing has gone wrong with the work. The encoding is on schedule. But someone with a great deal "
            "of power over the project was not on the clerk’s list, and now she must spend a day explaining "
            "instead of a minute informing.",
            "(As in every part of this series, the office, the people and the numbers are made up. No real "
            "town or employee is described.)",
            "This part is about avoiding that day. It is about stakeholders: the people and groups who can "
            "affect a project or are affected by it. Finding them early, and deciding how to work with each "
            "one, is one of the most valuable hours a project manager will ever spend.",
            ("h", "Who Counts as a Stakeholder"),
            "Many people think stakeholders are only the people who approve or pay for a project. The real list "
            "is wider. A stakeholder is anyone who can help the project, block it, or feel its results.",
            "For the encoding project, a first list might look like this:",
            ("point", "Inside the treasury", "The head of office as sponsor, the collectors doing the encoding, "
             "the cashier, and the staff at the counter who will use the new bills."),
            ("point", "Other offices", "The assessor’s office, whose tax declarations are the source of truth; "
             "the information technology staff who keep the system running; the accounting office, which "
             "relies on correct collection reports."),
            ("point", "Leadership", "The local chief executive and, depending on the town, members of the "
             "local council who field complaints from residents."),
            ("point", "Oversight", "The government auditors, who will later examine the records and the controls "
             "around them."),
            ("point", "The public", "Property owners who will receive the new bills and bring questions to the "
             "counter."),
            "Write the list with the team, not alone. The collectors will remember people the clerk would never "
            "think of, such as the staff at the information desk who hear taxpayers’ questions first.",
            ("h", "The Power and Interest Grid"),
            "Once the list is written, place each stakeholder on a simple grid. One side asks how much power they "
            "have over the project: can they approve, stop, fund or slow it? The other asks how much interest "
            "they have: how much do they care, or how much will the result affect them?",
            ("photo", "blog/pm-power-interest.jpg", "The power and interest grid: place each stakeholder by how "
             "much power they have over the project and how much they care about it, then engage them to "
             "match. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("point", "High power, high interest: manage closely", "These are the key players. Involve them in "
             "decisions, meet them regularly and never let them be surprised. For the encoding project, this is "
             "the head of office and the assessor."),
            ("point", "High power, lower interest: keep satisfied", "They can stop the project but are not "
             "following it day to day. Give them short, timely updates before they hear news from someone "
             "else. The local chief executive belongs here, which is exactly the clerk’s missed step."),
            ("point", "Lower power, high interest: keep informed", "They care a great deal and will feel the "
             "results, but cannot approve or stop the work. Tell them what is changing and listen to their "
             "concerns. The collectors and counter staff belong here, and so, in a different way, do the "
             "taxpayers."),
            ("point", "Lower power, lower interest: monitor", "Check now and then whether their position has "
             "changed. A bank where the office deposits collections may sit here unless the project changes "
             "how deposits are recorded."),
            "Positions are not fixed. The auditors may show little interest while the encoding is under way, then "
            "a great deal once the new records are used to produce official reports. Look at the grid again at "
            "each milestone in the charter.",
            ("h", "From Grid to Plan"),
            "The grid is only useful if it changes what you do. For each stakeholder, write one line: what they "
            "need to know, how they will hear it, and how often.",
            ("point", "Head of office", "A ten-minute update every Friday, plus a call the same day if a "
             "milestone is at risk."),
            ("point", "Local chief executive", "A short memo from the head of office before the project starts "
             "showing on bills, and a one-paragraph note when the system goes live."),
            ("point", "Assessor’s office", "A shared list of records with questions, checked on the agreed "
             "Tuesday and Thursday afternoons."),
            ("point", "Collectors and counter staff", "A fifteen-minute briefing before the January rush on what "
             "the new bill looks like and how to answer the three most common questions."),
            ("point", "Taxpayers", "A plain notice at the counter and on the office’s page explaining that bills "
             "are now printed, and who to ask if something looks wrong."),
            "Notice that the plan respects the chain of command. In this example, the clerk does not "
            "write to the mayor directly; the head of office does. Knowing who should speak to whom is part of stakeholder "
            "work, especially in government.",
            ("h", "Four Questions for Each Key Stakeholder"),
            "For the people in the top two boxes, a short conversation early in the project is worth more than "
            "any document. Ask each of them four questions, and write down the answers.",
            ("point", "What does success look like to you?", "The assessor may care most about matching "
             "records; the head of office about shorter lines in January. Both answers matter."),
            ("point", "What worries you about this project?", "Worries spoken early become risks you can plan "
             "for. Worries kept quiet become objections later."),
            ("point", "How would you like to hear from us?", "Some people want a short message, others a "
             "printed memo, others a two-minute talk in the hallway. Match their habit, not yours."),
            ("point", "Who else should we talk to?", "This question finds the stakeholders your list missed. "
             "It is how the clerk would have learned that the mayor’s office wanted to be told first."),
            "These conversations also build trust. People support projects they were asked about, and they "
            "forgive small delays from a project manager who listened to them at the start.",
            ("h", "Influence Without Authority"),
            "In Part 1, the clerk discovered that nobody on her list reported to her. The grid does not change "
            "that, but it shows her where her influence will come from.",
            "With high-power stakeholders, influence comes through the sponsor. A request from the head of "
            "office carries weight that a request from the clerk does not. With high-interest stakeholders, "
            "influence comes from listening. Collectors who were asked how to make the encoding easier will "
            "defend the schedule, because part of it is theirs.",
            ("quote", "You cannot command the people on your map. You can make sure none of them is surprised."),
            ("h", "Common Mistakes"),
            ("point", "Mapping once and filing it", "People move around the grid. A new head of office or an "
             "election can change everything."),
            ("point", "Forgetting the quiet ones", "The people with low power and high interest rarely complain "
             "loudly until something has gone wrong for them. Ask them early."),
            ("point", "Treating everyone the same", "Sending every stakeholder the same long weekly report "
             "wastes their time and hides the message that matters to each."),
            ("point", "Leaving the map lying around", "A stakeholder map is a working "
             "note. Keep it respectful and factual, and share it only with the project team."),
            ("h", "Your Part 3 Exercise"),
            "Take the project from your one-page charter and do this:",
            ("point", "List", "Write every person or group who can help, block or feel the project. Aim for at "
             "least ten."),
            ("point", "Place", "Put each one in a box of the grid: manage closely, keep satisfied, keep "
             "informed or monitor."),
            ("point", "Plan", "For the people in the top two boxes, write what they need to hear, from whom "
             "and how often."),
            "Then ask yourself one question: who would be most upset to hear about this project from someone "
            "other than you? Inform that person this week.",
            ("cta", "Read: Project Management Series, Part 2", "/blog/project-management-part-2-project-charter/"),
            ("cta", "Read: Project Management Series, Part 1", "/blog/project-management-part-1-accidental-project-manager/"),
            ("cta", "Read: Business Intelligence Series, Part 2", "/blog/business-intelligence-part-2-the-bi-team/"),
            ("cta", "Read: The ALTOS Framework, Principle 3: Every Document Has an Owner",
             "/blog/altos-framework-every-document-has-an-owner/"),
            ("ask", "Who is the stakeholder you are most likely to forget on your next project?"),
        ],
    },
    {
        "date": "November 18, 2026",
        "title": "Project Management Series, Part 2: The Project Charter on One Page",
        "slug": "project-management-part-2-project-charter",
        "category": "pm",
        "summary": "A project charter is a short document that says why a project exists, what it will deliver, "
                   "who is in charge and who approved it. Here is how to write one on a single page, using a "
                   "treasury encoding project as the example.",
        "publish_on": "2026-11-18 21:00",
        "body": [
            "Three weeks into the real property tax encoding project from Part 1, the revenue clerk is called "
            "into a meeting she did not expect. The assessor’s office says its staff cannot spare two "
            "afternoons a week after all. One collector asks why he was never told he would be helping. The "
            "head of office asks whether the bills for January will include unpaid taxes from past years, with "
            "their interest, or only the current year’s tax.",
            "Nobody in the room is being difficult. Each person simply remembers the assignment differently, "
            "because nobody ever wrote it down. The clerk now spends an hour defending decisions that were "
            "never really made.",
            "(As in every part of this series, the office, the people and the numbers are made up. No real "
            "town or employee is described.)",
            "This is the problem a project charter solves. It is the first document of a project, and in "
            "small offices it is often the only one that matters.",
            ("h", "What a Project Charter Is"),
            "A project charter is a short, signed document that officially starts a project. It records why the "
            "project exists, what it will deliver, when, with what money and people, and who is in charge. Most "
            "importantly, it is approved by the person with the authority to start the project, often called "
            "the sponsor. The same signature gives the project manager the authority to use the office’s "
            "people and resources for the work.",
            "That approval is what gives the charter its power. In Part 1, the clerk discovered that nobody on "
            "her list reported to her. A signed charter does not change the organization chart, but it does "
            "show everyone that the head of office has given the project a goal, a deadline and a leader. "
            "When the assessor’s staff are asked for time, the request is no longer a favor to the clerk. It "
            "is part of a project the head of office approved.",
            "Large organizations use long charters with many sections. A small office does not need that. One "
            "page, read in five minutes, is enough if it answers the right questions.",
            ("photo", "blog/pm-charter.jpg", "A one-page project charter answers six things before work begins: "
             "why, what, when, who, money and risks, and who signed. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "The Six Parts of a One-Page Charter"),
            ("point", "1. Why: the purpose", "One or two sentences on the problem the project solves and the "
             "result it should bring. Write it so a taxpayer could understand it."),
            ("point", "2. What: the scope, in and out", "The main things the project will deliver, followed by "
             "a short list of what it will not do. The “not included” list prevents more arguments than "
             "any other line on the page."),
            ("point", "3. When: the milestones", "Three to five dates that mark real progress, ending with the "
             "date the project is finished. Not every task, only the checkpoints."),
            ("point", "4. Who: the roles", "The sponsor, the project manager, the team members and the "
             "offices whose help is needed. Name the people, not only the units."),
            ("point", "5. Money and risks", "The budget, even if it is small, where it comes from, and the "
             "three biggest things that could go wrong."),
            ("point", "6. Sign: the approval", "The sponsor’s name, signature and date, and the date the "
             "charter will next be reviewed."),
            ("h", "The Encoding Project, Written as a Charter"),
            "Here is how the clerk’s project could look on one page. Notice how many of the questions from "
            "that difficult meeting are answered before anyone asks them.",
            ("point", "Why", "Bills for real property tax are still written by hand from ledger cards, which "
             "is slow and leads to errors at the counter. This project puts the ledger records into the "
             "office’s new system, so bills can be printed and checked before the January rush."),
            ("point", "What is included", "Encoding the ledger records of all taxable properties in the "
             "four poblacion (town center) barangays, checking each record against the assessor’s tax "
             "declarations, and printing "
             "a sample of bills for review."),
            ("point", "What is not included", "Unpaid taxes from past years and their interest (a separate project in "
             "February), the remaining barangays (next phase), and any change to how payments are received at "
             "the counter."),
            ("point", "Milestones", "Records of the first two barangays encoded and checked by November 27. All "
             "four barangays by December 11. Sample bills reviewed by the head of office by December 18. "
             "System ready at the counter on January 4."),
            ("point", "Who", "Sponsor: the head of office. Project manager: the revenue clerk. Team: two "
             "collectors for encoding, two afternoons a week. Support: the assessor’s office, one staff "
             "member for checking, Tuesday and Thursday afternoons."),
            ("point", "Money and risks", "₱18,000 from the office budget for paper, toner and a backup "
             "drive, bought through the usual procurement steps. Risks: the assessor’s staff may be pulled away by year-end work; old ledger cards may "
             "be hard to read; the system may slow down when many records are added at once."),
            ("point", "Sign", "Approved by the head of office, with a review set for December 11."),
            "Now the assessor’s time is written down and approved. The collector can be shown the page. And the "
            "question about past-year taxes has a clear answer: not in this project. None of these lines is "
            "complicated. Each one prevents a meeting.",
            ("h", "Five Mistakes That Weaken a Charter"),
            ("point", "Writing it alone", "A charter written by the project manager and simply handed out is a "
             "wish list. Draft it with the sponsor, then show it to the people whose time it asks for."),
            ("point", "Leaving out what is not included", "If the page lists only what the project will do, "
             "people will assume it does everything they hoped for."),
            ("point", "Vague success", "“Improve billing” cannot be checked. “Bills for the four "
             "poblacion barangays printed from the system by January 4” can."),
            ("point", "No real signature", "A charter nobody signed is just a note. In a government office, "
             "the head’s signature or a short office order is what turns the page into a commitment."),
            ("point", "Filing it and forgetting it", "Read the charter again at each milestone. If the project "
             "has changed, update the page and have it signed again."),
            ("h", "When the Plan Changes"),
            "A charter is not a promise that nothing will change. Projects meet surprises. The value of the "
            "charter is that every change becomes a clear decision instead of a slow drift.",
            "Suppose in December the head of office decides that past-year taxes must be included after "
            "all. With a charter, the clerk can answer calmly: “We can add them. That means more records "
            "to check, so either the January 4 date moves, or we get one more encoder, or we do the poblacion "
            "now and the past years in February. Which would you prefer?” This is the triangle of scope, "
            "time and cost from Part 1, now written on paper where everyone can see it.",
            ("quote", "A charter does not stop change. It makes every change a decision."),
            ("h", "A Note for Software Projects"),
            "The same page works when the project is a piece of software. Before building a tool, even a small "
            "collection app, write down what it will do, what it will not do, and who decides when it is "
            "ready. Software invites endless small additions, and the “not included” list is what lets "
            "the first version ever be finished. Everything else can wait for the next version, with its own "
            "page.",
            ("h", "Your Part 2 Exercise"),
            "Take the assignment you looked at in Part 1. On one sheet of paper or one screen, write:",
            ("point", "One sentence of purpose", "Why does this project exist?"),
            ("point", "Three things in, three things out", "What it delivers, and what it will not touch."),
            ("point", "Three dates", "Two checkpoints and a finish line."),
            ("point", "Names", "The sponsor, yourself and everyone whose time you need."),
            "Then take it to your sponsor and ask one question: “Is this what you meant?” Their answer "
            "is worth more than a week of work done in the wrong direction.",
            ("cta", "Read: Project Management Series, Part 1", "/blog/project-management-part-1-accidental-project-manager/"),
            ("cta", "Read: The ALTOS Framework, Principle 3: Every Document Has an Owner",
             "/blog/altos-framework-every-document-has-an-owner/"),
            ("cta", "Read: The ALTOS Framework, Principle 4: Every Owner Has a Deadline",
             "/blog/altos-framework-every-owner-has-a-deadline/"),
            ("cta", "Read: Business Intelligence Series, Part 2", "/blog/business-intelligence-part-2-the-bi-team/"),
            ("ask", "Have you ever worked on a project where everyone remembered the goal differently? What "
             "would a one-page charter have changed?"),
        ],
    },
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
