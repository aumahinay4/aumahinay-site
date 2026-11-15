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
        "date": "January 22, 2027",
        "title": "Project Management Series, Part 15: Why Estimates Run Short, and Four Ways to Fix Them",
        "slug": "project-management-part-15-estimating-time",
        "category": "pm",
        "summary": "People tend to underestimate how long their own work will take, even when they know their "
                   "past projects ran late. This part explains why, then gives four practical fixes: ask the "
                   "doer, estimate from the WBS, compare with the past, and use three-point estimates.",
        "publish_on": "2027-01-22 21:00",
        "body": [
            "The revenue clerk looks at the work breakdown structure for the notices project and fills in the "
            "estimates quickly. Checking the account list: two days. Notice template: one day. Printing: one "
            "day. Delivery: a week. Six weeks in total looks generous, and the head of office is pleased.",
            "Eight weeks later, the notices are still being delivered. Nothing dramatic went wrong. The list "
            "took longer to check because some ledger cards were unclear. The legal review came back with "
            "changes. Two collectors were pulled to the counter during a busy week. Each delay was small. "
            "Together they used up the whole margin and more.",
            "The clerk is not careless. Underestimating one’s own work is a well-studied human tendency, "
            "and it has a name.",
            "(As in every part of this series, the office, the people and the numbers are made up. No real "
            "town, employee or taxpayer is described.)",
            "Part 14 broke the project into work packages. This part puts time on them. By the end of this "
            "post you will know why estimates tend to run short, four ways to make them better, and how to "
            "present an estimate honestly to a sponsor.",
            ("photo", "blog/pm-estimates.jpg", "Four ways to better estimates: ask the doer, build from the "
             "WBS, compare with the past and use three points. (Illustration: Butch Mahinay, aumahinay.dev)",
             "medium"),
            ("h", "The Planning Fallacy"),
            "Psychologists Daniel Kahneman and Amos Tversky coined the term “planning fallacy” in 1979 for "
            "the tendency to underestimate how long a task will take. Later studies by Roger Buehler and his "
            "colleagues found a telling pattern in university students: they admit that past assignments were "
            "finished close to the deadline, yet they expect to finish the next one well ahead of it.",
            "Part of the reason is where attention goes. When we picture a task, we picture it going "
            "smoothly: the steps we know, done one after another. The interruptions, the rework and the "
            "waiting for other people are hard to picture in advance, so they are left out of the estimate.",
            ("quote", "An estimate pictures the plan. The calendar meets the real week."),
            ("h", "Fix 1: Ask the Person Who Will Do the Work"),
            "The clerk estimated the delivery from the office. The collectors who deliver notices know how far "
            "the farthest barangays are, which households are hard to find, and which days the roads are "
            "worse.",
            ("point", "Ask, do not tell", "Instead of “Can you finish delivery in a week?”, ask “How long would "
             "delivery take you?” The first question invites a yes."),
            ("point", "Ask about the last time", "“How long did it take last time?” is easier to answer "
             "honestly than a guess about the future."),
            ("point", "Ask what could slow it", "Each answer is a risk to write down."),
            ("h", "Fix 2: Estimate From the Work Packages"),
            "A single estimate for the whole project hides its parts. An estimate built from each work "
            "package in the WBS from Part 14 is easier to check, because each piece is small enough to "
            "picture.",
            ("point", "Estimate each package", "Write a time beside every work package, not just beside the "
             "main deliverables."),
            ("point", "Include the small things", "Approvals, reviews, waiting for signatures and the weekly "
             "updates take time too."),
            ("point", "Effort is not duration", "Two days of work done two afternoons a week takes two weeks "
             "on the calendar. Estimate the work, then place it on the calendar based on when people are "
             "actually free."),
            ("h", "Fix 3: Compare With the Past"),
            "Kahneman later described a remedy he called the outside view: before trusting your own plan, "
            "look at how long similar projects actually took.",
            ("point", "Find a comparable project", "Last year’s notices, a past collection drive, any "
             "project with similar steps."),
            ("point", "Look at the actual dates", "Not the planned ones. Emails, logbooks and the tracker "
             "from Part 12 can show when things really finished."),
            ("point", "Adjust for differences", "More accounts, fewer staff or a new step all change the "
             "number. Start from the past, then adjust."),
            "If past projects of this kind ran about a third over their plan, an estimate that assumes this "
            "one will not deserves a second look.",
            ("h", "Fix 4: Use Three Points, Not One"),
            "A single number hides how uncertain it is. A three-point estimate asks for three numbers for each "
            "work package.",
            ("point", "O, optimistic", "How long it takes if things go well."),
            ("point", "M, most likely", "How long it takes in a normal week."),
            ("point", "P, pessimistic", "How long it takes if the likely problems happen."),
            "Two common ways to combine them are a simple average, (O + M + P) ÷ 3, and the PERT or beta "
            "formula, (O + 4M + P) ÷ 6, which gives the most likely value more weight.",
            ("point", "Example", "Checking the account list: optimistic 2 days, most likely 4, pessimistic 9. "
             "The simple average is 5 days. The PERT formula gives (2 + 16 + 9) ÷ 6 = 4.5 days. Either is "
             "very different from the 2 days the clerk first wrote."),
            "The gap between O and P is useful by itself. A wide gap marks a package that needs attention, a "
            "risk owner, or a closer look before the plan is approved.",
            ("h", "Watch Out for the First Number"),
            "Tversky and Kahneman also described anchoring: estimates tend to stay close to a starting number, "
            "even when that number is arbitrary. In a project, the anchor can be the deadline someone "
            "mentioned first.",
            ("point", "Estimate before you hear the deadline", "Ask the team for estimates before telling them "
             "the date the sponsor hopes for."),
            ("point", "Write it down first", "Have each person write their estimate privately, then compare, "
             "so the first voice in the room does not set the number for everyone."),
            ("h", "Presenting an Estimate Honestly"),
            ("point", "Give a range", "“Eight to ten weeks, most likely nine” is more honest than “six weeks,” "
             "and it helps the sponsor plan."),
            ("point", "Say what it depends on", "“Assuming the legal review takes no more than a week and two "
             "collectors are available on Tuesdays and Thursdays.”"),
            ("point", "Do not trade accuracy for approval", "A short estimate can win a quick yes and still "
             "lead to a missed date. A realistic one protects everyone."),
            ("point", "Update it", "As packages finish, replace estimates with actual times and revise the "
             "rest."),
            ("h", "The Notices Project, Estimated Again"),
            "For the next round of notices, the clerk asked each collector for their own estimate, built the "
            "total from the work packages, compared it with how the first round actually went, and used three "
            "points for the packages with the most uncertainty. The result was a range of eight to ten weeks.",
            "The head of office was less pleased at first. But the notices went out in nine weeks, inside the "
            "range, and the plan held without a single extension request.",
            ("h", "Mistakes to Avoid"),
            ("point", "Estimating for someone else", "The person doing the work should help estimate it."),
            ("point", "One number for everything", "Estimate each package, and show a range for the total."),
            ("point", "Forgetting the waiting", "Reviews, approvals and signatures take calendar time."),
            ("point", "Never comparing with actuals", "Record how long things really took, so the next "
             "estimate starts from facts."),
            ("h", "Key Takeaways"),
            ("point", "We tend to underestimate", "The planning fallacy affects careful people too."),
            ("point", "Four fixes", "Ask the doer, build from the WBS, compare with the past, use three "
             "points."),
            ("point", "Effort is not duration", "Place the work on the calendar people actually have."),
            ("point", "Present a range", "With the assumptions written beside it."),
            ("h", "Your Part 15 Exercise"),
            "Take the work breakdown structure from your Part 14 exercise, or any plan you are working on.",
            ("point", "Ask", "For three work packages, ask the person doing the work for their estimate."),
            ("point", "Three points", "Write O, M and P for each, and work out the PERT value."),
            ("point", "Compare", "Find one past project with similar steps and note how long it actually took."),
            "Then compare your new total with your first guess. The difference is a measure of how much the "
            "planning fallacy was shaping your plan.",
            ("cta", "Read: Project Management Series, Part 14", "/blog/project-management-part-14-work-breakdown-structure/"),
            ("cta", "Read: Project Management Series, Part 12", "/blog/project-management-part-12-choosing-pm-software/"),
            ("cta", "Read: Project Management Series, Part 10", "/blog/project-management-part-10-business-case/"),
            ("cta", "Read: Data Analytics Series, Part 13", "/blog/data-analytics-part-13-bias-in-data/"),
            ("ask", "Which task in your office always takes longer than anyone plans for?"),
        ],
    },
    {
        "date": "January 17, 2027",
        "title": "Project Management Series, Part 14: The Work Breakdown Structure, One Bite at a Time",
        "slug": "project-management-part-14-work-breakdown-structure",
        "category": "pm",
        "summary": "A project that feels too big to plan becomes manageable once it is broken into pieces. "
                   "This part explains the work breakdown structure, the 100% rule, work packages and the WBS "
                   "dictionary, and breaks down a treasury project from a single goal to tasks people can own.",
        "publish_on": "2027-01-17 21:00",
        "body": [
            "The encoding project is done, and the head of office approves the next one: sending notices to "
            "taxpayers with unpaid real property tax from past years. The revenue clerk is asked for a plan "
            "and a timeline by Friday.",
            "The clerk opens a blank page and writes “Send delinquency notices.” Then nothing. The goal is "
            "clear, but it is one big lump. How long will it take? Who does what? What does it cost? None of "
            "those can be answered while the work is still a single line.",
            "The way forward is to break the lump into pieces small enough to answer those questions. That is "
            "what a work breakdown structure does.",
            "(As in every part of this series, the office, the people and the numbers are made up. No real "
            "town, employee or taxpayer is described.)",
            "Part 13 closed the first stage of this series with a pre-launch checklist. This part starts the "
            "planning stage. By the end of this post you will know what a work breakdown structure is, the "
            "rule that keeps it complete, how far to break the work down, and how to write a WBS dictionary "
            "that makes each piece clear.",
            ("photo", "blog/pm-wbs.jpg", "A work breakdown structure: the project at the top, the main "
             "deliverables below it, and work packages at the bottom. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "What a Work Breakdown Structure Is"),
            "PMI describes a work breakdown structure, or WBS, as a deliverable-oriented, hierarchical "
            "breakdown of the total scope of a project into smaller, manageable components. In plain words: "
            "start with the whole project, split it into the main things it must produce, and keep splitting "
            "until each piece is small enough to plan.",
            "It can be drawn as a tree, like an organization chart, or written as a numbered outline. "
            "Both show the same thing: what the project will deliver, piece by piece.",
            ("quote", "You cannot schedule a lump. You can schedule its pieces."),
            ("h", "Deliverables, Not Activities"),
            "The upper levels of a WBS name things the project produces, not actions. “Notices” is a "
            "deliverable. “Printing” is an activity that helps produce it.",
            "Naming deliverables first keeps attention on results. A list of activities can look busy and "
            "still leave out something the project must hand over. A list of deliverables makes the gaps "
            "easier to see.",
            ("h", "The 100% Rule"),
            "PMI’s guidance includes a simple test: the WBS includes 100% of the work in scope, and the "
            "pieces under any element add up to exactly that element.",
            ("point", "Nothing missing", "If a piece of work is in the scope from Part 4, it must appear "
             "somewhere in the WBS."),
            ("point", "Nothing extra", "If something is in the WBS but not in the scope, it is either a "
             "scope change for the sponsor to approve or it comes out."),
            ("point", "Nothing counted twice", "Each piece of work sits in one place. If two branches both "
             "include “print the notices,” one of them is wrong."),
            ("h", "Work Packages: Where to Stop"),
            "The lowest level of a WBS is the work package. PMI describes it as a piece with a single point of "
            "responsibility that can be estimated, managed and measured.",
            ("point", "One owner", "One person is answerable for it, as in the RACI matrix from Part 8."),
            ("point", "Can be estimated", "You can say roughly how long it will take and what it will cost."),
            ("point", "Can be checked", "Anyone can tell whether it is done."),
            "If a piece fails any of these, break it down further. If breaking it further would only add "
            "paperwork without making the plan clearer, stop. PMI’s advice puts it simply: stop when each "
            "package is small enough to estimate and track, but before the detail costs more to manage than it tells you.",
            ("h", "The Notices Project, Broken Down"),
            ("point", "1. Account list", "1.1 List of accounts with unpaid past-year tax, taken from the "
             "ledger. 1.2 List checked against the assessor’s records. 1.3 Final list approved by the head of "
             "office."),
            ("point", "2. Notices", "2.1 Notice template, reviewed by the office’s legal adviser. 2.2 "
             "Notices filled in from the final list. 2.3 Notices printed and signed."),
            ("point", "3. Delivery", "3.1 Delivery routes by barangay. 3.2 Notices delivered, with "
             "proof of receipt. 3.3 List of notices that could not be delivered, with the reason."),
            ("point", "4. Counter readiness", "4.1 Cashier and counter staff briefed on the notices. 4.2 A "
             "short guide for answering taxpayers’ questions."),
            ("point", "5. Project management", "5.1 Plan and schedule. 5.2 Weekly updates. 5.3 Closing report."),
            "Notice that project management has its own branch. Planning, updates and the closing report take "
            "real time. Leaving them out of the WBS leaves them out of the schedule.",
            ("h", "The WBS Dictionary"),
            "A short label such as “2.1 Notice template” can mean different things to different people. A WBS "
            "dictionary is a companion document that describes each element. PMI lists what it covers: the "
            "element’s scope, milestones, responsible party, resources and acceptance criteria.",
            ("point", "Scope", "One notice template for unpaid real property tax, in English and Filipino, on "
             "one page."),
            ("point", "Owner", "The revenue clerk."),
            ("point", "Resources", "Two days of the clerk’s time and one review session with the legal "
             "adviser."),
            ("point", "Milestone", "Approved by February 5."),
            ("point", "Acceptance", "Approved in writing by the head of office after the legal adviser’s "
             "review."),
            "Write entries only for the work packages that need them. A one-line package everyone understands "
            "does not need a page of explanation.",
            ("h", "How the WBS Feeds the Rest of the Plan"),
            ("point", "Schedule", "Each work package gets a start, a finish and an order. Packages that "
             "depend on each other are lined up."),
            ("point", "Budget", "Each package gets a cost. Added up, they give the project budget."),
            ("point", "Responsibility", "Each package gets one owner, which feeds the RACI matrix."),
            ("point", "Tracking", "Each package becomes a line in the tracker from Part 12."),
            ("h", "When the WBS Changes"),
            "A WBS is written at the start, but it is not frozen. If the sponsor approves a change to the "
            "scope, the WBS changes with it, and so do the schedule and the budget that come from it.",
            ("point", "Add, then renumber carefully", "Add the new package under the right deliverable. Keep "
             "existing numbers where possible, so earlier reports still make sense."),
            ("point", "Record why", "Note the date and the approved change beside the new package."),
            ("point", "Check the 100% rule again", "Make sure the new work is not already covered elsewhere."),
            ("h", "Building One With the Team"),
            ("point", "Start from the scope", "Write the project name at the top and the main deliverables "
             "below it, taken from the scope statement."),
            ("point", "Use sticky notes", "Give the team notes and a wall. Each person writes the pieces "
             "they know. Group them under the deliverables."),
            ("point", "Check the 100% rule", "Read each branch aloud and ask: is anything missing, extra or "
             "counted twice?"),
            ("point", "Number it", "Number every element, such as 2.1 and 2.2, so it can be referred to "
             "without confusion."),
            ("h", "Mistakes to Avoid"),
            ("point", "A to-do list in disguise", "Start with deliverables, then the work under them."),
            ("point", "Forgetting project management", "Plans, updates and reports are work too."),
            ("point", "Going too deep", "Packages of an hour each can create tracking work without adding clarity."),
            ("point", "Building it alone", "The people doing the work know the pieces the planner forgets."),
            ("h", "Key Takeaways"),
            ("point", "Break the lump", "A WBS splits the whole scope into manageable pieces."),
            ("point", "The 100% rule", "Nothing missing, nothing extra, nothing counted twice."),
            ("point", "Work packages", "One owner, can be estimated, can be checked."),
            ("point", "A dictionary for clarity", "Scope, owner, resources, milestone and acceptance for each "
             "package that needs it."),
            ("h", "Your Part 14 Exercise"),
            "Take a project you are about to plan, or one that feels too big to start.",
            ("point", "Write the deliverables", "List three to six main things the project must produce."),
            ("point", "Break them down", "Split each into work packages that pass the one-owner, estimate and "
             "check tests."),
            ("point", "Test it", "Apply the 100% rule against your scope statement."),
            "Then write a dictionary entry for the work package you are least sure about. Writing it can "
            "show what still needs to be decided.",
            ("cta", "Read: Project Management Series, Part 13", "/blog/project-management-part-13-pre-launch-checklist/"),
            ("cta", "Read: Project Management Series, Part 4", "/blog/project-management-part-4-defining-scope/"),
            ("cta", "Read: Project Management Series, Part 8", "/blog/project-management-part-8-raci-matrix/"),
            ("cta", "Read: Project Management Series, Part 12", "/blog/project-management-part-12-choosing-pm-software/"),
            ("ask", "Which part of your current project is still one big lump that nobody has broken down?"),
        ],
    },
    {
        "date": "January 12, 2027",
        "title": "Project Management Series, Part 13: The Pre-Launch Checklist, a Review of Parts 1 to 12",
        "slug": "project-management-part-13-pre-launch-checklist",
        "category": "pm",
        "summary": "Before the real work starts, one short review can catch the gaps that cause trouble later. "
                   "This part turns the first twelve parts of the series into a pre-launch checklist, shows "
                   "how to run it in one meeting, and applies it to the treasury encoding project.",
        "publish_on": "2027-01-12 21:00",
        "body": [
            "The encoding project is about to move from planning into full execution. The charter is signed, "
            "the team is named, the tracker is set up. The revenue clerk who leads it feels ready, and the "
            "head of office is eager to begin.",
            "Then, in a short review meeting, one question stops the room: “Who checks the encoded records "
            "against the tax declarations once the assessor’s staff member goes back to year-end work?” "
            "Nobody has an answer. The checking was in the charter, and the assessor’s support was in the "
            "charter, but the plan for that busy period was not written anywhere.",
            "Finding that gap in a meeting cost twenty minutes. Finding it in the middle of the work could "
            "have cost weeks.",
            "(As in every part of this series, the office, the people and the numbers are made up. No real "
            "town or employee is described.)",
            "This is the last part of the series’ first stage, which covered how a project starts. By the end "
            "of this post you will have a pre-launch checklist built from Parts 1 to 12, a way to run it in "
            "one meeting, a simple rating for each item, and a plan for what to do with the gaps you find.",
            ("photo", "blog/pm-pre-launch.jpg", "A pre-launch checklist in four groups: purpose, boundaries, "
             "people and ways of working. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Why a Checklist Before Launch"),
            "A project’s early decisions are spread across many documents and meetings: a charter, a list of "
            "stakeholders, a scope, a RACI matrix, a communication plan. Each was done well on its own day. A "
            "checklist puts them side by side and asks whether they still fit together.",
            "It also gives the team one moment to say what worries them before the work speeds up. Questions "
            "that feel awkward in the middle of the project can be easier to ask before it starts.",
            ("quote", "Check the plan while changing it is still cheap."),
            ("h", "Group 1: Purpose and Authority"),
            ("point", "Is this a project? (Part 1)", "It has a start, an end and a result that did not exist "
             "before. If it is really ongoing work, it needs a routine, not a project plan."),
            ("point", "Is there a signed charter? (Part 2)", "One page, approved by the sponsor, with the "
             "purpose, scope, milestones, people, money and risks."),
            ("point", "Is the business case still true? (Part 10)", "The reasons for approving the project "
             "still hold. If costs or benefits have changed since approval, the sponsor should know."),
            ("point", "Are the objectives measurable? (Part 6)", "Each objective names a real outcome, a "
             "starting point and a target everyone can check."),
            ("h", "Group 2: Boundaries"),
            ("point", "Is the scope written down? (Part 4)", "What is included and, just as clearly, what is "
             "not. Everyone on the team can say where the line is."),
            ("point", "Are the requirements agreed? (Part 9)", "The must-haves are listed and approved. Each "
             "one can be tested when the work is done."),
            ("point", "Is there a way to handle new requests? (Part 4)", "Requests that fall outside the scope "
             "go to a list for the sponsor to decide, not straight into the work."),
            ("h", "Group 3: People"),
            ("point", "Are the stakeholders mapped? (Part 3)", "Everyone the project affects is on the list, "
             "including people outside the team whose staff or time it uses."),
            ("point", "Was there a kickoff? (Part 7)", "Everyone heard the same answers to why, what, "
             "who, how and next, and open questions went to a parking list with owners."),
            ("point", "Does every task have one owner? (Part 8)", "The RACI matrix names one Accountable "
             "person for each main piece of work."),
            ("point", "Does everyone know who hears what? (Part 11)", "The communication plan lists who gets "
             "which update, how and how often, and who sends it."),
            ("h", "Group 4: Ways of Working"),
            ("point", "Is the way of working chosen? (Part 5)", "The team knows whether the work runs in "
             "planned stages, short cycles or a mix, and why."),
            ("point", "Is the tracker working? (Part 12)", "The stages, owners, update rule and one place "
             "for tasks are agreed, and the tracker shows the true status today."),
            ("point", "Are the risks named with an owner? (Parts 2 and 10)", "Each main risk from the charter and the business case has a "
             "person watching it and a first step if it happens."),
            ("h", "Rating Each Item"),
            "Rate each item with one of three words. Keep it simple enough to do in the meeting.",
            ("point", "Ready", "Done, written down, and the people involved agree."),
            ("point", "Partly", "Started, but missing a piece, an approval or a name."),
            ("point", "Missing", "Not done, or nobody is sure."),
            "“Not sure” always counts as Missing. If the team cannot point to where something is written, "
            "treat it as not written.",
            ("h", "Running the Review in One Meeting"),
            ("point", "Who attends", "The project lead, the sponsor or someone who can decide for them, and "
             "one person from each group doing the work."),
            ("point", "How long", "Plan for about an hour. Go through the groups in order, rating each item "
             "aloud."),
            ("point", "One rule", "Rate first, discuss later. If an item needs a long discussion, mark it "
             "Partly or Missing, name an owner for the fix, and move on."),
            ("point", "One output", "A list of every item rated Partly or Missing, each with an owner and a "
             "date."),
            ("h", "What to Do With the Gaps"),
            ("point", "Fix before starting", "Gaps that could stop the work or cause rework: no owner for a "
             "main task, an unapproved scope, a sponsor who has not signed."),
            ("point", "Fix in the first two weeks", "Gaps that slow the work but do not stop it: a missing "
             "line in the communication plan, a risk without a first step."),
            ("point", "Accept and note", "Small gaps the team agrees to live with. Write them down, so the "
             "choice is visible later."),
            "The sponsor then makes one decision: start now, start once the first group of fixes is done, or "
            "hold. Write the decision and the date into the project record.",
            ("h", "The Encoding Project, Checked"),
            "Here is how the review went for the encoding project. Most items were Ready. Three were not.",
            ("point", "Checking during the busy period: Missing", "The charter named the assessor’s staff "
             "member for checking, but not who would cover when year-end work pulled them away. Fix before "
             "starting: the head of office agreed with the assessor on one backup name and two fixed "
             "afternoons."),
            ("point", "Sample bills review: Partly", "The milestone said the head of office would review "
             "sample bills, but not what “reviewed” meant. Fix in two weeks: a short list of what each "
             "bill must show, signed off by the head of office."),
            ("point", "Open kickoff questions: Partly", "Two questions on the kickoff parking list still had no "
             "answer. Fix in two weeks: each was given an owner and a due date."),
            "The sponsor chose to start once the backup checker was named. That took two days. The project "
            "began with every main gap either closed or scheduled.",
            ("h", "Mistakes to Avoid"),
            ("point", "Treating it as a formality", "If every item is rated Ready in ten minutes, ask for the "
             "document behind each one."),
            ("point", "Leaving the sponsor out", "Only the sponsor can decide whether to start with gaps open."),
            ("point", "Gaps without owners", "A gap with no name and no date can easily stay a gap."),
            ("point", "Never looking again", "Run a shorter version of the checklist at each major milestone."),
            ("h", "Key Takeaways"),
            ("point", "One list, four groups", "Purpose, boundaries, people and ways of working."),
            ("point", "Three ratings", "Ready, Partly or Missing. “Not sure” counts as Missing."),
            ("point", "Every gap gets an owner", "With a date, and a decision on when it must be fixed."),
            ("point", "The sponsor decides", "Start, start after fixes, or hold."),
            ("h", "Your Part 13 Exercise"),
            "Take a project your office is about to start, or one that started recently.",
            ("point", "Rate it", "Go through the fourteen items and rate each one Ready, Partly or Missing."),
            ("point", "Pick the top three", "Choose the three gaps most likely to cause trouble."),
            ("point", "Name the fixes", "Write an owner and a date beside each of the three."),
            "If you rated everything Ready, choose the three items you are least sure of and find the "
            "document for each. That alone is a useful review.",
            ("cta", "Read: Project Management Series, Part 12", "/blog/project-management-part-12-choosing-pm-software/"),
            ("cta", "Read: Project Management Series, Part 2", "/blog/project-management-part-2-project-charter/"),
            ("cta", "Read: Project Management Series, Part 8", "/blog/project-management-part-8-raci-matrix/"),
            ("cta", "Read: Project Management Series, Part 1", "/blog/project-management-part-1-accidental-project-manager/"),
            ("ask", "Which item on this checklist would your current project rate as Missing?"),
        ],
    },
    {
        "date": "January 7, 2027",
        "title": "Project Management Series, Part 12: Choosing PM Software, and Why Tools Don’t Fix Broken Processes",
        "slug": "project-management-part-12-choosing-pm-software",
        "category": "pm",
        "summary": "A new project tool does not fix a process nobody has agreed on. This part shows how to get the "
                   "process working on paper first, what a PM tool actually needs to do, how to compare "
                   "options fairly, and how to try one without moving the whole office at once.",
        "publish_on": "2027-01-07 21:00",
        "body": [
            "A month into the encoding project, the team is frustrated. Tasks are scattered across a group "
            "chat, a spreadsheet and two notebooks. Someone suggests the answer: “Let’s get a proper project "
            "management app.” A free tool is set up that same afternoon. Boards are created, tasks are typed "
            "in, and everyone is invited.",
            "Two weeks later, the board is half empty. Some people update it; most do not. Tasks still get "
            "assigned in the group chat, and the board shows work as “in progress” that was finished days "
            "ago. The head of office asks for a status update, and the project lead ends up asking each "
            "person by phone, just as before.",
            "The tool was not the problem. Nobody had agreed on how tasks are assigned, who updates them, or "
            "what “done” means. The app simply gave the old confusion a new home.",
            "(As in every part of this series, the office, the people and the tools are made up. No real "
            "town, employee or product is described or recommended.)",
            "Part 11 settled who hears what and when. This part is about the place where the work is tracked. "
            "By the end of this post you will know how to check a process before choosing a tool, the five "
            "jobs a PM tool needs to do, how to compare options with a simple scoring sheet, and how to run a "
            "short trial before committing.",
            ("photo", "blog/pm-process-first.jpg", "Process first, then tool: agree on the stages, the owner, the update rule and the one place where tasks live. "
             "(Illustration: Butch Mahinay, aumahinay.dev)",
             "medium"),
            ("h", "Why a Tool Does Not Fix the Process"),
            "A project tool records decisions people have already made: who owns a task, when it is due, "
            "what stage it is in. If those decisions are not being made, the tool has nothing true to record.",
            ("point", "No owner, no update", "A task without one named owner sits on a board just as it sat "
             "in a notebook. Part 8’s RACI matrix answers this, not the software."),
            ("point", "No definition of done", "If one person marks a task done when it is drafted and "
             "another when it is approved, the board can show a different picture from the real work."),
            ("point", "No single place", "If tasks can still be assigned in the group chat, the board can fall behind. The team has to agree that the board is where tasks live."),
            ("quote", "A tool can carry a working process. It does not create one."),
            ("h", "Get the Process Working on Paper First"),
            "Before comparing any software, run the project for two weeks with the simplest tracker you have: "
            "a shared spreadsheet or a whiteboard. Use it to settle four things.",
            ("point", "1. The stages", "Name the few stages a task moves through, such as To do, Doing, For "
             "review and Done. Write one sentence for what each stage means."),
            ("point", "2. The owner", "Every task has one name beside it. If two people share a task, split "
             "it into two tasks."),
            ("point", "3. The update rule", "Agree when the tracker is updated, for example before leaving "
             "the office each day, and by whom: the task owner."),
            ("point", "4. The one place", "New tasks are added to the tracker, not assigned by message. A "
             "request that arrives by chat is copied in by the person who receives it."),
            "If the team can keep a spreadsheet accurate for two weeks, the process works, and a tool can make "
            "it easier. If the spreadsheet falls behind, the "
            "problem is the habit, not the tool, so fix the habit first.",
            ("h", "Five Jobs a PM Tool Needs to Do"),
            "Write down what the tool must do for this team, in plain words, before looking at any product.",
            ("point", "Show the tasks", "Every task, its owner, its due date and its stage, in one view."),
            ("point", "Show what is late", "A way to see quickly which tasks are past their due date."),
            ("point", "Keep the history", "Who changed what, and when, so a question about a task can be "
             "answered later."),
            ("point", "Hold the files and notes", "A place to attach the document or comment that belongs to "
             "a task, so it is not lost in a chat."),
            ("point", "Work where the team works", "If collectors are in the field with phones, the tool "
             "must work well on a phone and on a slow connection."),
            "Anything beyond these five is a nice-to-have. Long feature lists make tools look powerful, but "
            "every extra feature is something the team has to learn.",
            ("h", "Questions a Treasury Office Should Ask"),
            ("point", "Where is the data stored?", "Project notes can include taxpayer names and amounts. "
             "Personal information is covered by the Data Privacy Act of 2012 (Republic Act No. 10173). Ask "
             "your data protection officer before putting such details in any outside service, and keep "
             "personal data out of task titles."),
            ("point", "Who owns the account?", "Set the account up under an office email, not a personal "
             "one, so the records stay with the office when someone transfers or retires."),
            ("point", "Can we get our data out?", "Check that tasks and history can be exported to a file. "
             "If the tool is ever dropped, the project record should not go with it."),
            ("point", "What does it cost, and who approves it?", "A free plan may have limits on users, "
             "storage or history. A paid plan needs a budget and has to go through your office’s "
             "procurement rules. Find out both before the team starts depending on it."),
            ("h", "Compare Options With a Simple Scoring Sheet"),
            "Choose two or three options, and include the one you already have, such as the shared "
            "spreadsheet. Score each from 1 to 3 on the same list.",
            ("point", "The five jobs", "One score for each job above."),
            ("point", "Ease for the least technical member", "Ask that person to add and update a task, and "
             "score how easily it went."),
            ("point", "Data and ownership", "Storage, office account and export."),
            ("point", "Cost and approval", "What it costs now, what it may cost as the team grows, and how "
             "long approval would take."),
            "Add up the scores, but read the low scores too. A tool that scores well overall but fails on data "
            "privacy is not one a treasury office should choose.",
            ("h", "Run a Short Trial"),
            ("point", "One project, one month", "Try the tool on a single project with a small team, not on "
             "the whole office."),
            ("point", "Same rules", "Use the same stages, owners and update rule that worked on paper."),
            ("point", "Measure it", "At the end, ask: Is the board accurate today? Did status updates get "
             "faster? Did anyone stop using it, and why?"),
            ("point", "Decide on purpose", "Keep it, drop it, or go back to the spreadsheet. Going back is a "
             "valid result."),
            "In the encoding project, the team went back to the shared spreadsheet for two weeks and agreed on "
            "the four rules. Only then did they try a board again, with the same rules. This time, the head "
            "of office could read the status without calling anyone.",
            ("h", "Mistakes to Avoid"),
            ("point", "Buying before agreeing", "Settle the process first, then choose the tool."),
            ("point", "Choosing for the most technical person", "The tool has to work for the person who "
             "will find it hardest."),
            ("point", "Running two trackers", "If the old spreadsheet and the new board both stay in use, "
             "people may not know which one to trust. Pick one."),
            ("point", "Moving everything at once", "Try it on one project before rolling it out."),
            ("h", "Key Takeaways"),
            ("point", "Process before tool", "Agree on stages, owners, the update rule and one place."),
            ("point", "Five jobs", "Show tasks, show what is late, keep history, hold files, work where the "
             "team works."),
            ("point", "Ask the treasury questions", "Data privacy, office ownership, export and approval."),
            ("point", "Trial, then decide", "One project, one month, with a clear review."),
            ("h", "Your Part 12 Exercise"),
            "Look at how your current project tracks its tasks today.",
            ("point", "Write the four rules", "Stages, owner, update rule and one place. Mark any you have "
             "not agreed on."),
            ("point", "Check the tracker", "Pick five tasks at random and ask each owner whether the "
             "tracker shows the true status."),
            ("point", "Decide what to fix", "If fewer than five match, fix the rules before changing the "
             "tool."),
            "If all five match, you already have a working process, and any tool you choose has a fair chance "
            "of helping.",
            ("cta", "Read: Project Management Series, Part 11", "/blog/project-management-part-11-communication-plan/"),
            ("cta", "Read: Project Management Series, Part 8", "/blog/project-management-part-8-raci-matrix/"),
            ("cta", "Read: Project Management Series, Part 5", "/blog/project-management-part-5-waterfall-agile-hybrid/"),
            ("cta", "Read: Data Analytics Series, Part 6", "/blog/data-analytics-part-6-data-ethics-privacy/"),
            ("ask", "What rule does your team need to agree on before any new tool could help?"),
        ],
    },
    {
        "date": "January 2, 2027",
        "title": "Project Management Series, Part 11: The Communication Plan, Who Hears What, When",
        "slug": "project-management-part-11-communication-plan",
        "category": "pm",
        "summary": "A project can stall when the right people hear the wrong things, or nothing at all. This part "
                   "shows how to build a one-page communication plan: who needs what, how, how often and "
                   "from whom, with a rule for bad news and the treasury encoding project as the example.",
        "publish_on": "2027-01-02 21:00",
        "body": [
            "Three weeks into the encoding project, the assessor calls the head of office. “Why are your "
            "collectors asking my staff for tax declarations every afternoon? Nobody told me this was "
            "happening.” The project had been approved, the kickoff was held, and the assessor’s staff "
            "member was part of the team. But the assessor, who decides what that staff member works on, had "
            "never been told how much of their time the project needed.",
            "Nobody had hidden anything. Each person had simply assumed someone else would tell the assessor. "
            "A communication plan exists to stop that assumption.",
            "(As in every part of this series, the office, the people and the numbers are made up. No real "
            "town or employee is described.)",
            "Part 8 settled who does each task. This part settles who needs to know about it. By the end of "
            "this post you will have a five-column communication plan, a filled-in example, a rule for "
            "delivering bad news, and a way to keep updates short enough that people read them.",
            ("photo", "blog/pm-communication-plan.jpg", "A communication plan answers five questions: who, "
             "what, how, how often and from whom. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "What a Communication Plan Is"),
            "A communication plan is a short table that lists everyone who needs information about the "
            "project and says what each one gets, through which channel, how often and from whom. It turns "
            "“keep people informed” into specific promises.",
            "For a small office project, it fits on one page. Its value is not the document. It is the "
            "five minutes of thinking about each person before something goes wrong.",
            ("quote", "If a message has no owner, assume nobody will send it."),
            ("h", "The Five Columns"),
            ("point", "1. Who", "Each person or group. Start from the stakeholder map in Part 3 and the RACI "
             "matrix in Part 8: everyone marked C or I needs a row."),
            ("point", "2. What", "The information they need, in their terms. A sponsor needs progress against "
             "the date and budget. A team member needs this week’s tasks. An affected office head needs to know "
             "what their staff will be asked to do."),
            ("point", "3. How", "The channel: a short meeting, a one-page note, a message in a group chat, a "
             "printed notice at the window. Match the channel to how the person already works."),
            ("point", "4. How often", "Weekly, at each milestone, or only when something changes. More often "
             "is not always better."),
            ("point", "5. From whom", "One named sender for each row. Shared responsibility for a message is "
             "how the assessor in the opening story was missed."),
            ("h", "The Encoding Project’s Plan"),
            ("point", "Head of office (sponsor)", "What: progress against the January 4 date, any risk to it, "
             "and decisions needed. How: a five-line note and a ten-minute talk. How often: weekly, Fridays. "
             "From: the revenue clerk."),
            ("point", "Project team", "What: this week’s tasks, problems found, changes to the schedule. How: "
             "the fifteen-minute check-in from Part 7, plus a shared task list. How often: weekly, Tuesdays. "
             "From: the revenue clerk."),
            ("point", "Assessor", "What: the hours their staff member is needed, the records being checked "
             "and any change to either. How: a short note before work starts, then a call when anything "
             "changes. How often: at the start and at each change. From: the head of office, then the revenue "
             "clerk."),
            ("point", "Cashier and counter staff", "What: when the new bills start, what changes at the "
             "window, and when training happens. How: a short meeting and a printed one-page guide. How often: "
             "two weeks before go-live and the day before. From: the revenue clerk."),
            ("point", "Taxpayers", "What: that bills will look different from January 4. How: a notice at "
             "the window and on the office’s public page, if it has one. How often: once in December, again "
             "on January 4. From: the head of office."),
            "Five rows. With this table on the wall, the assessor could have heard about the project before "
            "the first afternoon of record checks.",
            ("h", "Choosing the Channel"),
            "Each channel is good at some things and poor at others. Match the channel to what the message "
            "needs to do.",
            ("point", "Meetings", "For decisions, disagreements and anything that needs discussion. Keep them "
             "short, and write down what was decided."),
            ("point", "Written notes", "For status, facts and anything that must be kept as a record. A note "
             "can be read later and forwarded without changing."),
            ("point", "Group chats", "For quick coordination, such as “The records are ready.” Decisions made "
             "in a chat can scroll away, so copy them into the weekly note."),
            ("point", "Printed notices", "For the public at the window. Keep them short, dated and signed by "
             "the office."),
            "When a message is both urgent and important, use two channels: a call so it is heard today, and a "
            "note so it is on record.",
            ("h", "Writing Updates People Read"),
            "A plan only works if people read what you send. For a weekly update to a busy sponsor, keep to "
            "five lines.",
            ("point", "Status", "One word for each: on track, at risk or off track, for the date and the "
             "budget."),
            ("point", "Done this week", "The milestones reached, in one line."),
            ("point", "Next week", "What will be done, in one line."),
            ("point", "Risks or issues", "Anything that could move the date, with what you are doing about it."),
            ("point", "Decisions needed", "What you need from the reader, and by when. Write “none” if there "
             "are none."),
            "The last line is the one the sponsor most needs to act on. If it says “none” every week, the update can stay "
            "short. If it asks for something, the sponsor knows exactly what to do.",
            ("h", "A Rule for Bad News"),
            "Bad news can get harder to deliver the longer it waits. Agree on a rule at the start: anything that "
            "could move the go-live date or the budget is reported to the sponsor within one working day, "
            "in person or by phone, not saved for the weekly note.",
            "Bring three things with the bad news: what happened, what it affects, and at least one option. "
            "“The assessor’s staff member is on leave for a week. That puts the records check five days "
            "behind. We can add one afternoon a week for three weeks, or move the sample bill review by five "
            "days. I recommend the extra afternoons.”",
            ("h", "Listening Is Part of the Plan"),
            "Communication runs both ways. Give each group a clear way to raise problems: a standing question "
            "at the weekly check-in, a named person to message, or a box on the counter guide for questions "
            "from the cashier’s staff.",
            "When someone raises a concern, answer it and say what happened as a result, even if the answer is "
            "no. An answered question tells people that it was worth asking.",
            ("h", "Mistakes to Avoid"),
            ("point", "Forgetting the bosses of team members", "If someone’s time is borrowed, their head of "
             "office needs a row in the plan."),
            ("point", "One message for everyone", "The sponsor and the counter staff need different details. "
             "Write for each reader."),
            ("point", "Long updates", "A page of detail is easy to skip. Lead with status and decisions needed."),
            ("point", "Silence when things go well", "A short “on track, no decisions needed” still tells the "
             "sponsor the project is alive."),
            ("h", "Key Takeaways"),
            ("point", "Five columns", "Who, what, how, how often and from whom."),
            ("point", "One sender per message", "When a message belongs to everyone, someone can be missed."),
            ("point", "Short updates", "Status, done, next, risks and decisions needed."),
            ("point", "Bad news within a day", "With what happened, what it affects and an option."),
            ("h", "Your Part 11 Exercise"),
            "List everyone your current project affects, including people outside the team whose staff or "
            "resources it uses.",
            ("point", "Fill the five columns", "One row per person or group."),
            ("point", "Find the gaps", "Mark any row where you are not sure who sends the message. Assign a "
             "name."),
            ("point", "Send one update", "Write this week’s five-line update to your sponsor."),
            "Then ask the sponsor one question: “Is this what you need to see each week?” Adjust the plan to "
            "the answer.",
            ("cta", "Read: Project Management Series, Part 8", "/blog/project-management-part-8-raci-matrix/"),
            ("cta", "Read: Project Management Series, Part 3", "/blog/project-management-part-3-stakeholder-mapping/"),
            ("cta", "Read: Project Management Series, Part 7", "/blog/project-management-part-7-kickoff-meeting/"),
            ("cta", "Read: Business Intelligence Series, Part 11", "/blog/business-intelligence-part-11-five-minute-briefing/"),
            ("ask", "Who is the one person your current project has forgotten to tell?"),
        ],
    },
    {
        "date": "December 28, 2026",
        "title": "Project Management Series, Part 10: Writing a Business Case That Gets a Yes",
        "slug": "project-management-part-10-business-case",
        "category": "pm",
        "summary": "A good idea still needs a reason to spend time and money on it. This part walks through "
                   "the six parts of a business case, a worked treasury example with simple numbers, and how to present it so a decision maker can say yes or no quickly.",
        "publish_on": "2026-12-28 21:00",
        "body": [
            "The revenue clerk asks the head of office for a second receipt printer and a part-time encoder "
            "for the January rush. The answer is a polite no: “The budget is tight this year.” The clerk is "
            "sure the request would pay for itself, but has nothing on paper to show it.",
            "A month later, the clerk asks again, this time with one page. It shows how long taxpayers waited "
            "last January, how many left the line without paying, what the printer and encoder would cost, and "
            "three options side by side. The head of office reads it twice, asks two questions and approves the printer.",
            "(As in every part of this series, the office, the people and the numbers are made up. No real "
            "town or employee is described.)",
            "The request did not change. The case for it did. By the end of this post you will know the six "
            "parts of a business case, how to compare options honestly, including doing nothing, how to work "
            "out a simple payback, and how to present it so a busy decision maker can say yes or no quickly.",
            ("photo", "blog/pm-business-case.jpg", "Six parts of a business case: the problem, the options, "
             "the costs, the benefits, the risks and the recommendation. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "What a Business Case Is For"),
            "A business case answers one question: is this worth doing, compared with the other ways we could "
            "use the same time and money? It comes before the charter from Part 2. The charter authorizes a "
            "project. The business case is the reason to authorize it.",
            "It does not need to be long. For a small office request, one or two pages can be enough, as long "
            "as every number in it can be traced to a record or a stated assumption.",
            ("quote", "A business case does not argue for a project. It compares choices and lets the numbers "
             "speak."),
            ("h", "The Six Parts"),
            ("point", "1. The problem", "What is wrong today, in measurable terms, and what it costs the office "
             "or the public."),
            ("point", "2. The options", "Two to four realistic ways to respond, always including “do nothing.”"),
            ("point", "3. The costs", "For each option: money, staff time and anything else it uses up, "
             "one-time and recurring."),
            ("point", "4. The benefits", "For each option: what improves, by how much and by when. Separate "
             "benefits you can count from those you can only describe."),
            ("point", "5. The risks", "What could stop each option from working, and what the office would do "
             "about it."),
            ("point", "6. The recommendation", "Which option, why, and what decision you need from the reader."),
            ("h", "The Clerk’s Case, Worked Through"),
            ("point", "The problem", "Last January, the average wait at the real property tax window was 52 "
             "minutes on the busiest days. Office counts show about 40 taxpayers a day left the line without "
             "paying in the first two weeks. Some returned later; some did not return until interest had "
             "started."),
            ("point", "Option A: do nothing", "Cost: none. Result: the same lines next January."),
            ("point", "Option B: second printer only", "One-time cost: ₱18,000 for the printer, plus "
             "supplies. Result: a second window can print receipts, but only when a second staff member is "
             "free."),
            ("point", "Option C: printer and part-time encoder", "One-time cost: ₱18,000. Recurring cost: "
             "₱16,000 a month for an encoder during January and February, or ₱32,000 a year. Result: a second "
             "window open every day of the rush."),
            "Every number above comes from the office’s own records or from a quoted price, and the page says "
            "which is which.",
            ("h", "Counting the Benefits Honestly"),
            "The benefit the clerk can count is collections that arrive earlier instead of later or not at "
            "all. The clerk estimates it carefully and says how.",
            ("point", "The assumption", "If the second window cuts the busiest-day wait to about 25 minutes, "
             "half of the taxpayers who used to leave the line will stay and pay."),
            ("point", "The estimate", "20 taxpayers a day, for 10 busy days, at an average of ₱1,500 each, is "
             "₱300,000 collected in January instead of later."),
            ("point", "What it is not", "This is not new revenue. Some or all of it might have arrived later anyway. The "
             "gain is that it arrives sooner, with less follow-up work, and with fewer taxpayers paying "
             "interest for being late."),
            "Some benefits cannot be counted in pesos: shorter lines, fewer complaints and staff who are not "
            "exhausted by the end of January. List them, but do not turn them into made-up numbers.",
            ("h", "A Simple Payback"),
            "For a small request, a payback comparison can be enough: how long until the "
            "benefit covers the cost?",
            ("point", "Option B", "Cost ₱18,000. Without a second staff member, the clerk cannot claim much "
             "benefit, so the payback is unclear."),
            ("point", "Option C", "First-year cost ₱50,000. The counted benefit is earlier collection, not new "
             "money, so the clerk does not claim the ₱300,000 as savings. Instead, the case shows that the "
             "cost is about one sixth of the collections that would otherwise arrive late, plus the staff time "
             "saved on follow-up."),
            "Being honest about what a benefit is, earlier money rather than new money, makes the case "
            "stronger. A reader who catches an inflated number may stop trusting the rest of the page.",
            ("h", "Risks and the Recommendation"),
            ("point", "Risks", "The encoder may not be hired in time. The printer may arrive late. Mitigation: "
             "start hiring as soon as the case is approved, and order the printer the same week."),
            ("point", "Recommendation", "Option C, with a check after January: if the busiest-day wait did not "
             "fall below 30 minutes, do not renew the encoder for next year."),
            ("point", "Decision needed", "Approval of ₱50,000 from the office’s budget by December 1."),
            "In the opening story, the head of office approved Option B first, the cheaper one, and asked for "
            "a staffing plan before deciding on the encoder. That is a good outcome too. A business case gives "
            "the decision maker real choices, and sometimes they choose differently.",
            ("h", "Presenting It"),
            ("point", "Lead with the decision", "The first line says what you are asking for, how much it "
             "costs and by when you need an answer."),
            ("point", "Show the options in a table", "Options across, costs, benefits and risks down. The reader "
             "can compare in one look."),
            ("point", "Put the assumptions in writing", "Every estimate says what it is based on, so the reader "
             "can disagree with a specific number instead of the whole page."),
            ("point", "Keep it short", "Move details to an attachment. The main page should be readable in "
             "five minutes."),
            ("h", "Mistakes to Avoid"),
            ("point", "Leaving out “do nothing”", "Without it, the reader has nothing to compare the project against."),
            ("point", "Only one real option", "A case with one sensible option and two weak ones can look like a sales pitch."),
            ("point", "Counting the same benefit twice", "Earlier collections and fewer follow-up visits may "
             "be the same taxpayers. Count them once."),
            ("point", "No check afterward", "Say how you will know, after the project, whether the benefit "
             "really came."),
            ("h", "Key Takeaways"),
            ("point", "Compare, do not argue", "A business case weighs options, always including doing "
             "nothing."),
            ("point", "Six parts", "Problem, options, costs, benefits, risks and recommendation."),
            ("point", "Be honest about benefits", "Say what is counted, how, and what is earlier money rather "
             "than new money."),
            ("point", "Ask for a clear decision", "Name the amount, the option and the date."),
            ("h", "Your Part 10 Exercise"),
            "Think of one request your office has turned down or postponed.",
            ("point", "Problem", "Write the problem in one sentence with a number from your records."),
            ("point", "Options", "List three options, including doing nothing, with a cost for each."),
            ("point", "Benefit", "Estimate one benefit and write the assumption behind it."),
            "Then read it as the decision maker would. If you would not say yes to your own page, find the "
            "number or assumption that is holding it back.",
            ("cta", "Read: Project Management Series, Part 2", "/blog/project-management-part-2-project-charter/"),
            ("cta", "Read: Project Management Series, Part 9", "/blog/project-management-part-9-gathering-requirements/"),
            ("cta", "Read: Project Management Series, Part 6", "/blog/project-management-part-6-writing-objectives/"),
            ("cta", "Read: Data Analytics Series, Part 3", "/blog/data-analytics-part-3-deciding-with-data/"),
            ("ask", "What request in your office deserves a second try with a one-page business case?"),
        ],
    },
    {
        "date": "December 23, 2026",
        "title": "Project Management Series, Part 9: Gathering Requirements When Nobody Knows What They Want",
        "slug": "project-management-part-9-gathering-requirements",
        "category": "pm",
        "summary": "“Make the daily report faster” is a wish, not a requirement. This part shows five ways to "
                   "find out what people really need, the questions that get useful answers, and how to write "
                   "requirements that can be checked and agreed on.",
        "publish_on": "2026-12-23 21:00",
        "body": [
            "The cashier stops the revenue clerk in the hallway. “Can you make something that makes the daily "
            "report faster? It takes me forever every afternoon.” The clerk says yes, and two weeks later "
            "shows a spreadsheet that totals the day’s receipts by account in one click.",
            "The cashier looks at it politely and says it is nice. The totals were never the slow part. The "
            "slow part was finding the three or four receipts each day that did not match the cash count, and "
            "the spreadsheet does nothing about that.",
            "(As in every part of this series, the office, the people and the numbers are made up. No real "
            "town or employee is described.)",
            "The cashier did know what the problem was. What nobody had done was ask the questions that would "
            "bring it out. By the end of this post you will know five ways to gather requirements, the "
            "questions that get past the first answer, how to write a requirement that can be tested, and how "
            "to get it agreed before the work begins.",
            ("photo", "blog/pm-requirements-methods.jpg", "Five ways to gather requirements: interview, "
             "observe, read the documents, hold a workshop and show a prototype. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "What a Requirement Is"),
            "A requirement is a statement of what the finished result must do, or how well it must do it, "
            "written so that someone can check whether it was met.",
            ("point", "Functional requirements", "What the result must do. For example: “The sheet lists every "
             "receipt whose amount differs from the cash count for that receipt.”"),
            ("point", "Quality requirements", "How well it must do it: speed, accuracy, security, ease of "
             "use. These are also called non-functional requirements. For example: “The cashier can finish "
             "the daily report within 15 minutes after the last receipt.”"),
            "“Make the report faster” is neither. It is a wish. Turning wishes into requirements is the work "
            "this part is about.",
            ("h", "Why People Ask for Solutions"),
            "A request can arrive as a solution instead of a problem. “Make it faster” and “put it in a spreadsheet” are guesses at a "
            "solution. The project manager’s job is to work backward from the guess to the need.",
            ("quote", "Listen to the request, then ask about the work. Look for the need in the work."),
            ("h", "Five Ways to Gather Requirements"),
            ("point", "1. Interview", "Sit with one person and ask about their work, not about the system. "
             "Ask them to walk you through the last time they did the task, step by step."),
            ("point", "2. Observe", "Watch the task being done on a real day. In the opening story, ten "
             "minutes beside the cashier at closing time would have shown where the time really went."),
            ("point", "3. Read the documents", "Look at the forms, reports and rules the work must follow, "
             "such as the daily report of collections and deposits and the office’s cash-handling rules. "
             "Documents can show requirements that people take for granted and forget to mention."),
            ("point", "4. Hold a workshop", "Bring the people who share a process into one room, such as the "
             "collectors, the cashier and the revenue clerk, and map the steps together on a board. "
             "A workshop can bring out disagreements that one-on-one interviews miss."),
            ("point", "5. Show a prototype", "Sketch the screen or report on paper, or build a rough version, "
             "and ask people to try it. Reacting to something visible can be easier than "
             "describing something that does not exist yet."),
            "Use more than one. Interviews tell you what people say they do. Observation shows what they "
            "actually do. Documents show what they are required to do. The requirements sit where all three "
            "agree, and the risks sit where they do not.",
            ("h", "Questions That Get Past the First Answer"),
            ("point", "“Walk me through the last time.”", "A real example gives details that a general "
             "description leaves out."),
            ("point", "“Which part takes the longest?”", "In the opening story, this question would have pointed "
             "straight to the mismatched receipts."),
            ("point", "“What goes wrong?”", "Problems and workarounds point straight at needs."),
            ("point", "“What happens if it is late or wrong?”", "The answer tells you how much each need "
             "matters."),
            ("point", "“Who else uses what you produce?”", "The daily report is used by other people too. "
             "Their needs may become requirements."),
            ("h", "Writing Requirements That Can Be Tested"),
            "A good requirement passes four checks.",
            ("point", "One idea", "Each requirement says one thing. Split “fast and accurate” into two."),
            ("point", "Specific", "Name the user, the action and the result. Avoid words like “easy,” “quick” "
             "and “user-friendly” unless you say how they will be measured."),
            ("point", "Testable", "Someone can check it with a yes or no. “Within 15 minutes after the last "
             "receipt” can be timed. “Faster” cannot."),
            ("point", "Traceable", "Note who asked for it and why, so that when it is questioned later, you "
             "know whom to ask."),
            ("h", "The Cashier’s Requirements, Rewritten"),
            ("point", "R1", "The sheet lists every receipt whose recorded amount differs from the cash count "
             "for that receipt, with the receipt number and the collector. Source: interview with the cashier."),
            ("point", "R2", "The daily report can be finished within 15 minutes after the last receipt on an "
             "ordinary day. Source: interview with the cashier."),
            ("point", "R3", "The day’s totals by account match the official receipts issued, with no manual "
             "retyping. Source: interview with the cashier."),
            ("point", "R4", "Only the cashier and the head of office can change a recorded amount, and every "
             "change is logged. Source: the workshop, raised by the head of office."),
            "R1 is the need the first spreadsheet missed. R3 is the part it did well. R4 came from someone "
            "who never asked for anything, which is why the workshop matters.",
            ("h", "Sorting What Matters Most"),
            "When the requirements do not all fit the time and budget, sort them into four groups, a method known as MoSCoW. The capital letters come from Must, Should, Could and Won’t; the two o’s are added so it reads as a word.",
            ("point", "Must have", "Without it, the result fails. R1 and R4."),
            ("point", "Should have", "Important, but the result still works without it for a while. R2."),
            ("point", "Could have", "Nice if time allows. A chart of mismatches by week."),
            ("point", "Won’t have this time", "Agreed and written down as out of scope, as in the scope "
             "statement from Part 4."),
            ("h", "Getting Agreement"),
            "Read the list back to everyone who gave input. Ask each person whether it says what they need "
            "and whether anything is missing. Then ask the sponsor to approve it.",
            "The approved list becomes the base for the scope statement and its acceptance tests. When "
            "someone later asks for something new, you can point to the list and offer the same choice as in "
            "Part 4: move the date, add people, or plan it for the next phase.",
            ("h", "Mistakes to Avoid"),
            ("point", "Asking only the boss", "The head of office knows the goal. The people at the counter "
             "know the work. You need both."),
            ("point", "Writing solutions as requirements", "“Use a spreadsheet” is a design choice. Write the "
             "need first, then choose the tool."),
            ("point", "Gathering once", "New needs appear as people see the work take shape. Plan a short "
             "check-in to review the list."),
            ("h", "Key Takeaways"),
            ("point", "A wish is not a requirement", "A requirement says what or how well, and can be checked."),
            ("point", "Use several methods", "Interview, observe, read the documents, hold a workshop and "
             "show a prototype."),
            ("point", "Ask about the work", "Ask “Which part takes the longest?” as well as “What do you want?”"),
            ("point", "Sort and agree", "Group requirements by priority, read them back and get the sponsor’s "
             "approval."),
            ("h", "Your Part 9 Exercise"),
            "Pick one request someone made to you recently that sounded like “make it better” or “make it "
            "faster.”",
            ("point", "Ask", "Spend ten minutes with the person and ask the five questions above."),
            ("point", "Watch", "If you can, watch them do the task once."),
            ("point", "Write", "Write three requirements that pass the four checks, and sort them into must, "
             "should and could."),
            "Then show the list to the person. If they say, “Yes, that is exactly it,” you have found the "
            "need. If they say, “Well, not really,” you have saved yourself two weeks.",
            ("cta", "Read: Project Management Series, Part 4", "/blog/project-management-part-4-defining-scope/"),
            ("cta", "Read: Project Management Series, Part 8", "/blog/project-management-part-8-raci-matrix/"),
            ("cta", "Read: Project Management Series, Part 3", "/blog/project-management-part-3-stakeholder-mapping/"),
            ("cta", "Read: Business Intelligence Series, Part 4", "/blog/business-intelligence-part-4-the-bi-brief/"),
            ("ask", "What is the vaguest request you have ever received, and what was the real need behind it?"),
        ],
    },
    {
        "date": "December 18, 2026",
        "title": "Project Management Series, Part 8: Who Does What? Building a RACI Matrix",
        "slug": "project-management-part-8-raci-matrix",
        "category": "pm",
        "summary": "When everyone thinks someone else is handling a task, it can go undone. This part explains "
                   "the four RACI roles, walks through a RACI matrix for the treasury encoding project, and "
                   "gives four checks that help catch gaps early.",
        "publish_on": "2026-12-18 21:00",
        "body": [
            "Two weeks into the encoding project, the revenue clerk asks for the list of records that did not "
            "match the assessor’s tax declarations. One collector thought the assessor’s staff member was "
            "keeping it. The assessor’s staff member thought the collectors were writing it down as they "
            "encoded. Each had done careful work on their own part. Nobody had kept the list.",
            "The kickoff had named who works on which afternoons. What it had not settled was who owns each "
            "task: who does it, who answers for it, who must be asked first and who only needs to be told. "
            "A simple grid called a RACI matrix settles exactly that.",
            "(As in every part of this series, the office, the people and the numbers are made up. No real "
            "town or employee is described.)",
            "Part 7 ran the kickoff. This part turns its decisions into a written map of roles. By the end of "
            "this post you will know the four RACI roles, how to build a matrix for a small office project, "
            "four checks that expose gaps and overlaps, and how to keep the matrix useful after the first "
            "week.",
            ("photo", "blog/pm-raci-roles.jpg", "The four RACI roles: Responsible does the work, Accountable "
             "owns the result, Consulted gives input before, and Informed is told after. (Illustration: "
             "Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "The Four Roles"),
            "RACI is named after the four roles a person can have on a task. The descriptions below follow the Project Management Institute’s definitions, with the encoding project as the example.",
            ("point", "R: Responsible", "The person who does the work. A task can have more than one, such as "
             "the two collectors who share the encoding."),
            ("point", "A: Accountable", "The one person who owns the result and answers for it. Each task has "
             "exactly one, even when several people share the work."),
            ("point", "C: Consulted", "People whose input is needed before the work is finished. They are "
             "asked first, while their answer can still change the work."),
            ("point", "I: Informed", "People who are kept up to date after decisions are made or "
             "progress happens. The work does not wait for them."),
            "The difference between C and I is the difference between “ask before” and “tell after.” Getting it wrong can cost time in both directions. Too many Cs can make every step wait for someone’s "
            "opinion. Too few can mean someone with needed knowledge finds out when it is too late to help.",
            ("quote", "Many hands can share the work. Only one person can own the result."),
            ("h", "Why Only One A?"),
            "When no one, or more than one person, is named as accountable for a task, each person can reasonably "
            "assume someone else is watching it. That is how the mismatch list went missing. Naming one person does not mean that "
            "person does the work alone. It means there is always one name to ask, “Is this done, and is it "
            "right?”",
            "The accountable person and the responsible person can be the same, especially on a small team. "
            "The revenue clerk may both run the training session for the counter staff and answer for it. "
            "What matters is that every task has an A, and only one.",
            ("h", "Building the Matrix in Five Steps"),
            ("point", "1. List the tasks", "Use the deliverables from the scope statement and the milestones "
             "under the objective. Write each task as a verb and a thing: “encode the records,” not "
             "“encoding.”"),
            ("point", "2. List the people", "Put each person or role across the top. Use the stakeholder map "
             "from Part 3 so nobody who matters is left off."),
            ("point", "3. Fill in A first", "For each task, decide the single person who answers for it. If the "
             "team cannot agree, the sponsor decides."),
            ("point", "4. Fill in R, then C and I", "Name who does the work, who must be asked first and who "
             "only needs to be told."),
            ("point", "5. Review it with the team", "Walk through the grid row by row, the way the kickoff "
             "walked through the schedule. Each person confirms their letters, or says plainly that they "
             "cannot do what is written."),
            ("h", "The Encoding Project’s RACI Matrix"),
            "Here is the matrix for the encoding project, written one task at a time. The people are the "
            "head of office (the sponsor), the revenue clerk (the project manager), the two collectors, the "
            "cashier and the assessor’s staff member.",
            ("point", "Encode the property records", "R: the two collectors. A: the revenue clerk. C: the "
             "assessor’s staff member, when a record is unclear. I: the head of office, through the weekly "
             "check-in."),
            ("point", "Check records against tax declarations", "R: the assessor’s staff member. A: the revenue "
             "clerk. C: the collectors who encoded the record. I: the head of office."),
            ("point", "Keep the mismatch list", "R: the assessor’s staff member, who writes each mismatch and "
             "its reason on the same afternoon it is found. A: the revenue clerk. I: the collectors."),
            ("point", "Approve the sample bills", "R: the revenue clerk, who prints them. A: the head of "
             "office, who checks twenty against the ledger cards. C: the cashier. I: the collectors."),
            ("point", "Train the counter staff", "R and A: the revenue clerk. C: the cashier, on how the "
             "counter runs today. I: the head of office."),
            ("point", "Start using the system at the counter", "R: the revenue clerk and the cashier. A: the "
             "head of office. C: the collectors. I: the assessor’s staff member."),
            "The missing list from the opening now has an owner on paper: one person writes it, one person "
            "answers for it, and the people who need it know where it lives.",
            ("h", "Four Checks Before You Share It"),
            "Read the finished grid down each column and across each row, and run these four checks.",
            ("point", "Every row has exactly one A", "No A means nobody owns the result. Two As means each one "
             "may wait for the other."),
            ("point", "Every row has at least one R", "A task with an owner but no doer can sit still until the owner notices."),
            ("point", "No column is full of Rs and As", "If one person carries most of the work and most of "
             "the accountability, the project depends on that person never being absent. Look for a task "
             "that someone else could take."),
            ("point", "Cs are few and real", "For each C, ask what decision their input changes. If the answer "
             "is none, make them an I and save everyone a wait."),
            ("h", "Keeping the Matrix Alive"),
            "A matrix written at the start and never opened again can drift away from the project as tasks "
            "and people change. Three habits keep it current.",
            ("point", "Bring it to the weekly check-in", "When a new task appears, add a row and fill in its "
             "letters before anyone starts on it."),
            ("point", "Change it when people change", "If a collector is moved to another assignment, every R "
             "in their column needs a new name that same week."),
            ("point", "Use it to settle confusion", "When two people disagree about who should do something, "
             "open the matrix instead of arguing from memory. If the matrix does not answer it, the row needs "
             "to be clearer."),
            ("h", "Mistakes to Avoid"),
            ("point", "Giving the A to a group", "“The treasury” or “the team” cannot answer for a task. Write a "
             "person’s role."),
            ("point", "Making the sponsor the A for everything", "Keep the sponsor’s A for the decisions only the sponsor "
             "can make, such as approving the sample bills. Give the other tasks to the person closest to the work."),
            ("point", "Rows that are too large", "“Do the project” is not a task. If a row needs more than one "
             "A, split it into smaller tasks."),
            ("point", "Writing it without the team", "A matrix filled in alone is a guess about other people’s "
             "time. Agreement in the room helps the letters stick."),
            ("h", "Key Takeaways"),
            ("point", "Four roles", "Responsible does, Accountable owns, Consulted is asked before, and "
             "Informed is told after."),
            ("point", "One A per task", "Many people can share the work, but exactly one person answers for "
             "each result."),
            ("point", "Check the grid", "Look for rows with no A or no R, overloaded columns and Cs that change "
             "nothing."),
            ("point", "Keep it current", "Review the matrix at each check-in and update it when tasks or "
             "people change."),
            ("h", "Your Part 8 Exercise"),
            "Build a RACI matrix for your own project on one page:",
            ("point", "Rows", "List six to ten tasks, each written as a verb and a thing."),
            ("point", "Columns", "List every person or role who touches those tasks."),
            ("point", "Letters", "Fill in one A per row first, then the Rs, Cs and Is."),
            "Then run the four checks. If any row fails, fix it before you show the matrix to the team, and "
            "ask each person to confirm their column.",
            ("cta", "Read: Project Management Series, Part 7", "/blog/project-management-part-7-kickoff-meeting/"),
            ("cta", "Read: Project Management Series, Part 3", "/blog/project-management-part-3-stakeholder-mapping/"),
            ("cta", "Read: Project Management Series, Part 4", "/blog/project-management-part-4-defining-scope/"),
            ("cta", "Read: Business Intelligence Series, Part 2", "/blog/business-intelligence-part-2-the-bi-team/"),
            ("ask", "Which task in your office has two people who each think the other one owns it?"),
        ],
    },
    {
        "date": "December 13, 2026",
        "title": "Project Management Series, Part 7: The Kickoff Meeting Blueprint",
        "slug": "project-management-part-7-kickoff-meeting",
        "category": "pm",
        "summary": "A kickoff meeting can launch a project or waste an hour. This part gives a one-hour "
                   "agenda, what to prepare beforehand, how to run each segment, and what to send afterward, "
                   "using the treasury encoding project as the example.",
        "publish_on": "2026-12-13 21:00",
        "body": [
            "The revenue clerk calls the first meeting of the encoding project for 2 p.m. At 2:20, three of "
            "the seven people have arrived. The head of office speaks for twenty minutes about how important "
            "the project is. Someone asks who will be encoding on Thursdays. Nobody knows. The meeting ends "
            "at 3:30 with no decisions, and two collectors leave unsure whether the project is starting this "
            "week or next month.",
            "The charter was signed. The scope was clear. The objective was measurable. What was missing was "
            "one well-run hour that turned those documents into a shared plan that every person in the room "
            "understood the same way.",
            "(As in every part of this series, the office, the people and the numbers are made up. No real "
            "town or employee is described.)",
            "This part is about that hour. By the end of this post you will have a one-hour kickoff agenda, a "
            "list of what to prepare beforehand, a way to run each segment so it ends in a decision, and a "
            "short follow-up note you can send the same afternoon.",
            ("photo", "blog/pm-kickoff-agenda.jpg", "A one-hour kickoff in five segments: why, what, who, how "
             "and next. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "What a Kickoff Is For"),
            "A kickoff meeting has one job: everyone leaves knowing the same answers to five questions. Why "
            "are we doing this? What exactly will we deliver? Who does what? How will we work together? What "
            "happens next?",
            "It is not the place to write the plan. The charter, the scope statement and the objective should "
            "already exist. The kickoff explains them, tests them against the people who will do the work, "
            "and fixes the gaps that only those people can see.",
            ("h", "Before the Meeting"),
            "Prepare these four things before anyone sits down.",
            ("point", "Confirm the right people", "The sponsor, the project manager, every team member, and "
             "one person from each office whose help is needed. For the encoding project: the head of office, "
             "the revenue clerk, the two collectors, the cashier and the assessor’s staff member."),
            ("point", "Send the documents two days ahead", "The one-page charter, the scope statement and the "
             "objective. Ask people to read them and bring one question each."),
            ("point", "Brief the sponsor", "Agree on the five minutes the sponsor will speak and the one "
             "message they will give. A sponsor who knows their part can keep the opening short."),
            ("point", "Prepare a draft schedule", "Bring a draft of who works when, so the meeting can correct "
             "it rather than build it from nothing."),
            ("h", "The One-Hour Agenda"),
            ("point", "1. Why (10 minutes)", "The sponsor explains the problem and the outcome in plain "
             "words: taxpayers wait too long at the real property tax window, and the goal is to bring the "
             "average wait down. Then the sponsor says, in front of everyone, that the revenue clerk leads the "
             "project. That one sentence makes the project manager’s role clear to everyone at once."),
            ("point", "2. What (10 minutes)", "The project manager walks through the deliverables, the "
             "acceptance tests and the exclusions. Read the exclusions out loud. Past-year taxes are not in "
             "this project, and saying so now prevents a request in week three."),
            ("point", "3. Who (15 minutes)", "Go through the draft schedule person by person. Each person "
             "confirms their days and hours, or says plainly that they cannot. This is the segment that "
             "would have answered “who encodes on Thursdays?”"),
            ("point", "4. How (15 minutes)", "Agree on working rules: where files are saved, how mistakes are "
             "reported, how progress is shared, and how often the team meets. For a small project, a "
             "fifteen-minute weekly check-in can be enough."),
            ("point", "5. Next (10 minutes)", "Read back every decision and every task with a name and a date. "
             "Ask each person to repeat their first task. End on time."),
            ("quote", "If a kickoff ends without names and dates, it was a briefing, not a kickoff."),
            ("h", "A Sample Opening for the Sponsor"),
            "A short script helps the sponsor keep to five minutes. The project manager can draft "
            "it for them to adjust:",
            "“Every January, taxpayers wait too long at the real property tax window. This project puts the ledger "
            "records of the four poblacion barangays into our system so bills can be printed and checked quickly. "
            "Our goal is to bring the average wait down from 38 minutes to 20 or less. The revenue clerk leads this "
            "project, and I have approved the time each of you will give to it. Please bring problems to her early. "
            "I would rather hear about a delay in week two than in December.”",
            "In six sentences, the sponsor has named the problem, the outcome, the leader, the commitment of time "
            "and the expected behavior. Everything after that builds on it.",
            ("h", "Running the Room"),
            ("point", "Start on time", "Start at the stated time even if someone is missing. Waiting can teach people that the time on the invitation is only a suggestion."),
            ("point", "Keep a parking list", "When a question comes up that the meeting cannot settle, write "
             "it on a visible list with a name beside it. Then move on."),
            ("point", "Invite the quiet ones", "Ask the collectors directly: “What could stop this from "
             "working?” The people closest to the work can see risks the planners missed."),
            ("point", "Write as you go", "Keep notes on the screen or on a board where everyone can see them. "
             "Disagreements about what was decided can then be settled in the room, not a week later."),
            ("h", "The Follow-Up Note"),
            "Send a short note the same day, while the meeting is fresh. It should fit on one screen.",
            ("point", "Decisions", "For example: encoding happens Tuesday and Thursday afternoons; the "
             "assessor’s staff member checks records on the same days."),
            ("point", "Tasks", "Each with one name and one date."),
            ("point", "Parking list", "Each open question with its owner and when an answer is due."),
            ("point", "Next meeting", "Day, time and place of the first weekly check-in."),
            "Ask everyone to reply within a day if anything in the note is wrong. Treat silence after that "
            "as agreement, and keep the note as the record.",
            ("h", "When One Meeting Is Not Enough"),
            "A large project may need more than one kickoff: one for the sponsor and office heads, another for "
            "the people doing the work, and a short new kickoff when a major phase begins. The five questions "
            "stay the same. Only the level of detail changes.",
            "For a small office project like the encoding work, one well-prepared hour can be enough, "
            "followed by short weekly check-ins.",
            ("h", "Mistakes to Avoid"),
            ("point", "Speeches instead of decisions", "Keep the opening to the sponsor’s five minutes. Every "
             "other segment should end in something agreed."),
            ("point", "Inviting everyone", "Invite the people who must act or decide. Others can receive the "
             "follow-up note."),
            ("point", "No pre-reading", "If people see the scope for the first time in the meeting, the hour "
             "goes to reading instead of discussing."),
            ("point", "No follow-up", "Without a written note, each person remembers a slightly different "
             "meeting."),
            ("h", "Key Takeaways"),
            ("point", "Five questions, one hour", "Why, what, who, how and next, each with a fixed time."),
            ("point", "Prepare more than you present", "Send the documents early and bring a draft schedule "
             "to correct."),
            ("point", "Let the sponsor give authority", "One sentence from the sponsor in front of the team "
             "settles who leads."),
            ("point", "Close with names and dates", "Then put them in writing the same day."),
            ("h", "Your Part 7 Exercise"),
            "Plan the kickoff for your own project on one page:",
            ("point", "Attendees", "Who must be there, and why each one?"),
            ("point", "Pre-reading", "Which documents will you send, and on what date?"),
            ("point", "Agenda", "Write the five segments with times and the decision each one should reach."),
            "Then draft the follow-up note before the meeting, with blanks for the decisions. If you cannot "
            "imagine what would go in a blank, that segment needs more preparation.",
            ("cta", "Read: Project Management Series, Part 6", "/blog/project-management-part-6-writing-objectives/"),
            ("cta", "Read: Project Management Series, Part 3", "/blog/project-management-part-3-stakeholder-mapping/"),
            ("cta", "Read: Project Management Series, Part 2", "/blog/project-management-part-2-project-charter/"),
            ("cta", "Read: Business Intelligence Series, Part 4", "/blog/business-intelligence-part-4-the-bi-brief/"),
            ("ask", "What is the one thing your last project kickoff left unclear?"),
        ],
    },
    {
        "date": "December 8, 2026",
        "title": "Project Management Series, Part 6: Writing Objectives That Actually Mean Something",
        "slug": "project-management-part-6-writing-objectives",
        "category": "pm",
        "summary": "“Improve billing” is a wish, not an objective. This part shows where the SMART idea came "
                   "from, why a SMART objective can still miss the point, and how to write objectives that "
                   "name a real outcome, a starting point and a target everyone can check.",
        "publish_on": "2026-12-08 21:00",
        "body": [
            "At the end of the encoding project, the team reports success. Every record in the four poblacion "
            "barangays is in the system. Fifty sample bills were printed and checked. The deadline was met. "
            "By every line of the plan, the project is done.",
            "Then January comes, and the line at the real property tax window is as long as last year’s. "
            "The bills print faster, but taxpayers still wait while staff look up past payments on ledger "
            "cards. The project delivered exactly what it promised. It just never promised the thing the "
            "head of office actually wanted: shorter waiting time at the counter.",
            "(As in every part of this series, the office, the people and the numbers are made up. No real "
            "town or employee is described.)",
            "This part is about closing that gap. By the end of this post you will know where the SMART "
            "checklist came from, the difference between an output and an outcome, and a five-part pattern "
            "for objectives that tell everyone what success looks like before the work begins.",
            ("photo", "blog/pm-objective-parts.jpg", "A useful objective has five parts: the outcome, how it "
             "is measured, where it starts, the target, and the date. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "Where SMART Came From"),
            "The SMART checklist is often traced to a 1981 article by George T. Doran in Management Review, "
            "titled “There’s a S.M.A.R.T. way to write management’s goals and objectives.” In Doran’s "
            "version, the letters stood for Specific, Measurable, Assignable, Realistic and Time-related.",
            "Other versions use different words for some letters, such as Attainable, Relevant or Timely, "
            "which is why lists differ from one book to another. The idea is the same: an objective should be clear enough that two "
            "people would agree on whether it was met.",
            "Notice the A in the original. Assignable means someone specific is responsible. An objective that "
            "nobody owns is easy to forget when the work gets busy.",
            ("h", "Output or Outcome?"),
            "The encoding project shows the gap clearly. Its objective was about "
            "an output, not an outcome.",
            ("point", "Output", "What the project produces: records encoded, bills printed, staff trained. "
             "Outputs are within the team’s control and easy to count."),
            ("point", "Outcome", "The change that should happen because of those outputs: shorter waiting "
             "time, fewer billing errors, more taxpayers paying on time. Outcomes are what the sponsor really "
             "wants."),
            "An objective can be perfectly SMART and still be about the wrong thing. “Encode all records in "
            "four barangays by December 11” is specific, measurable, assigned, realistic and dated. It says "
            "nothing about whether anyone will wait less.",
            ("quote", "Outputs are what you deliver. Outcomes are why anyone asked you to deliver them."),
            ("h", "A Five-Part Pattern"),
            "A useful objective answers five questions. Writing them as separate lines makes gaps easy to "
            "spot.",
            ("point", "1. Outcome", "What should be different for the people the project serves?"),
            ("point", "2. Measure", "How will the change be counted, and from which record?"),
            ("point", "3. Baseline", "Where does the measure stand today? Without a starting point, no one "
             "can tell whether it improved."),
            ("point", "4. Target", "What value will count as success?"),
            ("point", "5. Date", "By when, and when will it be checked?"),
            "Add an owner to the whole objective, the A from Doran’s list, and you have something a sponsor "
            "can approve and a team can aim at.",
            ("h", "The Encoding Project, Rewritten"),
            ("point", "Outcome", "Taxpayers paying real property tax at the counter wait less."),
            ("point", "Measure", "Minutes from joining the line to receiving an official receipt, timed for "
             "a sample of taxpayers at the real property tax window."),
            ("point", "Baseline", "Timed on five busy mornings during last year’s January rush: an "
             "average of 38 minutes."),
            ("point", "Target", "An average of 20 minutes or less."),
            ("point", "Date", "Measured again on five busy mornings during the January rush after the new "
             "system is in use."),
            ("point", "Owner", "The revenue clerk, reporting to the head of office."),
            "With this objective, the team would have seen early that encoding alone was not enough. Looking "
            "up past payments was part of the wait, so bringing past-year records into the system, or "
            "printing them on the bill, belonged in the plan too.",
            ("h", "Keep Outputs Too, as Milestones"),
            "Outputs still matter. They are the steps that lead to the outcome, and they are easier to track "
            "week by week. Keep them in the plan as milestones under the objective.",
            ("point", "Objective (outcome)", "Average waiting time at the real property tax window down from "
             "38 to 20 minutes or less."),
            ("point", "Milestones (outputs)", "Records encoded by December 11. Sample bills approved by "
             "December 18. System at the counter by January 4."),
            "When a milestone slips, the team can ask the right question: does this still lead to the "
            "outcome, or do we need a different step?",
            ("h", "Choosing a Good Measure"),
            "The measure needs the most care of the five parts. Before agreeing to one, test it against four "
            "questions.",
            ("point", "Is it tied to the outcome?", "Waiting time is the outcome itself. The number of records "
             "encoded is only a step toward it."),
            ("point", "Does a record exist, or can one be made cheaply?", "Timing a sample of taxpayers with a "
             "stopwatch costs a few mornings. A measure that needs a new system before it can be counted may never "
             "be counted at all."),
            ("point", "Can it be checked by someone else?", "A clear method, written down, lets another person "
             "repeat the count and get the same answer."),
            ("point", "Is it hard to game?", "If the number can improve without the work improving, pair it with a "
             "second measure, such as billing errors alongside waiting time."),
            ("h", "Agree on It Before the Work Starts"),
            "An objective only guides the work if the sponsor has agreed to it. Put the five parts and the owner in "
            "the charter, show them to the head of office, and ask one direct question: “If we hit this target by "
            "this date, will you consider the project a success?”",
            "If the answer is “not quite,” the conversation that follows is the most useful one in the whole "
            "project. It is far cheaper to change an objective on paper in November than to discover in January "
            "that the team was aiming at the wrong thing.",
            "Once agreed, review progress against the objective at every milestone, not only at the end. Check the "
            "measure partway through if you can. A small sample in the middle of the project tells you early "
            "whether the outputs are moving the outcome at all.",
            ("h", "Mistakes to Avoid"),
            ("point", "No baseline", "“Reduce waiting time” cannot be judged if nobody measured it before. "
             "Time it first, even with a stopwatch and a notebook."),
            ("point", "Targets nobody can measure", "If the office has no record of a measure, either plan "
             "how to collect it or choose a measure it already keeps."),
            ("point", "Too many objectives", "Three clear objectives are easier to steer by than ten. If "
             "everything is a priority, nothing is."),
            ("point", "Objectives that punish honesty", "A target that staff can meet by recording numbers "
             "differently, rather than by improving the work, invites exactly that. Part 3 of the Business "
             "Intelligence series covered the same trap for dashboards."),
            ("h", "Key Takeaways"),
            ("point", "SMART is a start, not the finish", "A SMART objective can still describe the wrong "
             "thing."),
            ("point", "Aim at outcomes", "Write the change people should feel, then list the outputs as "
             "milestones."),
            ("point", "Measure the starting point", "No baseline, no proof of improvement."),
            ("point", "Name one owner", "Doran’s original A, assignable, is worth keeping."),
            ("h", "Your Part 6 Exercise"),
            "Take one objective from your project charter and rewrite it in the five-part pattern: outcome, "
            "measure, baseline, target and date, plus one owner.",
            "If you cannot fill in the baseline, your first task is clear. Spend one week measuring where "
            "things stand today. That number will make every later report about the project more honest.",
            ("cta", "Read: Project Management Series, Part 5", "/blog/project-management-part-5-waterfall-agile-hybrid/"),
            ("cta", "Read: Project Management Series, Part 2", "/blog/project-management-part-2-project-charter/"),
            ("cta", "Read: Business Intelligence Series, Part 3", "/blog/business-intelligence-part-3-what-to-watch/"),
            ("cta", "Read: Data Analytics Series, Part 3", "/blog/data-analytics-part-3-deciding-with-data/"),
            ("ask", "What is one objective in your current project that describes an output instead of an outcome?"),
        ],
    },
    {
        "date": "December 3, 2026",
        "title": "Project Management Series, Part 5: Waterfall, Agile or Hybrid? Choosing How to Run the Work",
        "slug": "project-management-part-5-waterfall-agile-hybrid",
        "category": "pm",
        "summary": "Some projects should be planned in full before work begins. Others should be built in short "
                   "cycles and shown to users early. Some need a little of both. Here is how "
                   "to tell which is which, with two treasury projects as examples.",
        "publish_on": "2026-12-03 21:00",
        "body": [
            "Two projects land on the revenue clerk’s desk in the same month. The first is the encoding "
            "project from earlier parts: a fixed deadline of January 4, a signed scope statement, and rules "
            "for computing the tax that will not change before then. The second is new. The head of office "
            "wants a simple screen where counter staff can tell a taxpayer, in one glance, whether a "
            "property has unpaid balances. Nobody is sure yet what that screen should show.",
            "The clerk plans both the same way, with every task written out in advance. The first project "
            "runs smoothly. The second produces a carefully built screen that the counter staff find "
            "confusing on the first morning they use it, and most of the plan has to be redone.",
            "(As in every part of this series, the office, the people and the numbers are made up. No real "
            "town or employee is described.)",
            "The problem was not the plan. It was the choice of approach. By the end of this post you will "
            "know the difference between the predictive, adaptive and hybrid ways of running a project, the "
            "questions that tell you which one fits, and how to mix them on a real office project.",
            ("photo", "blog/pm-three-approaches.jpg", "Three ways to run a project: predictive (plan, then "
             "build), adaptive (build, show, adjust) and hybrid (choose by part). (Illustration: Butch "
             "Mahinay, aumahinay.dev)", "medium"),
            ("h", "Predictive: Plan First, Then Build"),
            "In a predictive approach, often called waterfall, the work moves through stages in order: "
            "define what is needed, design it, build it, test it and hand it over. Scope, schedule and cost "
            "are set early, and changes go through a formal decision, the way Part 4 handled the three extra "
            "requests.",
            "The name has a curious history. A 1970 paper by Winston Royce, “Managing the Development of "
            "Large Software Systems,” is often cited as the origin of the waterfall picture. Royce never used "
            "the word waterfall in that paper, and the paper itself called the simple step-by-step version risky. "
            "The label came later.",
            ("point", "It fits when", "The requirements are clear and stable, the rules are fixed, the "
             "deadline cannot move, and the result must work completely on the first day it is used."),
            ("point", "It struggles when", "Users cannot say what they need until they see something, or "
             "when the goal is likely to change while the work is under way."),
            ("h", "Adaptive: Build a Little, Show It, Adjust"),
            "An adaptive approach, the family that includes agile methods, delivers the work in short "
            "cycles. Each cycle produces something people can try. Their reaction shapes the next cycle.",
            "The word agile comes from the Manifesto for Agile Software Development, written in February "
            "2001 by seventeen software practitioners who met at the Snowbird ski resort in Utah. It states "
            "four values:",
            ("point", "Individuals and interactions", "over processes and tools."),
            ("point", "Working software", "over comprehensive documentation."),
            ("point", "Customer collaboration", "over contract negotiation."),
            ("point", "Responding to change", "over following a plan."),
            "Read the word “over” carefully. The manifesto itself says the items on the right still have "
            "value; the items on the left are valued more. Agile does not mean no plan and no documents. It "
            "means the plan is expected to change as people learn.",
            "Scrum, one widely known agile framework, organizes work into sprints. The Scrum Guide sets the "
            "longest sprint at one month, and each sprint aims to produce a usable piece of the product that "
            "can be shown and discussed.",
            ("point", "It fits when", "Users can try partial results, the best answer is not known at the "
             "start, and changing direction midway is cheap."),
            ("point", "It struggles when", "Nothing useful can be delivered in parts, or the people who must "
             "give feedback cannot spare time for it every few weeks."),
            ("h", "Hybrid: Choose by Part"),
            "A project does not have to be purely one or the other. A hybrid approach "
            "uses a predictive frame for the parts that are fixed and short adaptive cycles for the parts "
            "that are uncertain.",
            "Public offices have good reasons to keep a predictive frame. Budgets are approved ahead of time, "
            "purchases follow procurement rules, and records must be ready for audit. Inside that frame, "
            "the parts that people will see and use every day can still be built in cycles.",
            ("quote", "Plan in detail what you already know. Build in short cycles what you can only learn "
             "by trying."),
            ("h", "Five Questions That Point the Way"),
            "Before choosing, answer these five questions about the project, or about each part of it.",
            ("point", "1. How clear are the requirements?", "Clear and written down points to predictive. "
             "“We will know it when we see it” points to adaptive."),
            ("point", "2. Are the rules fixed?", "Work governed by a law, an ordinance or a set formula is "
             "best planned in full. Its requirements are already written."),
            ("point", "3. Can people try part of it?", "If a first version can be put in front of users "
             "within a few weeks, short cycles will show problems early."),
            ("point", "4. How costly is a late change?", "If a change near the end would mean redoing most "
             "of the work, invest more in planning up front."),
            ("point", "5. Who can give feedback, and how often?", "Adaptive work needs users who will look at "
             "each version. Without them, the cycles have nothing to learn from."),
            ("h", "The Two Treasury Projects, Revisited"),
            ("point", "The encoding project: predictive", "The rules for the bill are fixed, the deliverables "
             "and acceptance tests are written, and the January 4 date cannot move. Planning it in full was "
             "the right call."),
            ("point", "The balance screen: adaptive", "Nobody knew what the counter staff needed to see. A "
             "better plan would have been two-week cycles: a paper sketch first, then a rough screen with "
             "real records from one barangay, each shown to two counter staff for a morning and adjusted "
             "before the next cycle."),
            ("point", "The two together: hybrid", "If the balance screen is treated as part of the larger "
             "billing program, the program keeps a fixed budget and a fixed go-live date, while the screen "
             "itself is shaped in short cycles inside that frame."),
            "Run this way, the counter staff would have seen the confusing screen in week two, on paper, "
            "instead of on the first busy morning at the counter.",
            ("h", "Running Your First Short Cycle"),
            "If you have never worked in cycles, keep the first one small and simple.",
            ("point", "Pick something you can show", "One screen, one form or one report, not the whole system."),
            ("point", "Set a fixed end date", "Two weeks is a reasonable length to start with. The Scrum Guide’s "
             "upper limit for a sprint is one month."),
            ("point", "Show it to real users", "Sit with two people who will use it and watch them try it. Note "
             "where they hesitate or ask a question."),
            ("point", "Decide what changes", "End the cycle with a short list of what to keep, change and drop. "
             "That list becomes the plan for the next cycle."),
            ("h", "Common Myths"),
            ("point", "“Agile means no planning.”", "Agile teams plan in smaller pieces, at the start of every cycle. The "
             "manifesto values responding to change more than following a plan, not instead of having one."),
            ("point", "“Waterfall means no feedback.”", "A predictive project can and should check its work "
             "at each milestone, as Part 4’s acceptance tests did."),
            ("point", "“We must pick one for the whole office.”", "The approach is chosen per project, and "
             "often per part of a project."),
            ("h", "Key Takeaways"),
            ("point", "Match the approach to what is known", "Predictive for fixed, clear work; adaptive for "
             "work that must be discovered."),
            ("point", "Hybrid is a deliberate choice", "Keep a predictive frame for budget, deadline and "
             "audit, and build the uncertain parts in short cycles."),
            ("point", "Agile still plans", "It plans in smaller pieces and expects to adjust."),
            ("point", "Show early, fix cheaply", "A problem found on paper in week two is cheaper to fix than "
             "one found at the counter on launch day."),
            ("h", "Your Part 5 Exercise"),
            "Take the project from your charter and scope statement and split it into its main parts. For "
            "each part, answer the five questions above and mark it predictive or adaptive.",
            "Then pick one adaptive part and plan just its first cycle: what you will show, to whom, and on "
            "what date. If you can name the date, you have already started working in a hybrid way.",
            ("cta", "Read: Project Management Series, Part 4", "/blog/project-management-part-4-defining-scope/"),
            ("cta", "Read: Project Management Series, Part 1", "/blog/project-management-part-1-accidental-project-manager/"),
            ("cta", "Read: Business Intelligence Series, Part 4", "/blog/business-intelligence-part-4-the-bi-brief/"),
            ("cta", "Read: Data Analytics Series, Part 2", "/blog/data-analytics-part-2-six-steps/"),
            ("ask", "Which part of your current project would you rather show on paper first?"),
        ],
    },
    {
        "date": "November 28, 2026",
        "title": "Project Management Series, Part 4: Drawing the Line Before Work Begins",
        "slug": "project-management-part-4-defining-scope",
        "category": "pm",
        "summary": "The charter says what a project is for. The scope statement says exactly what it will deliver, "
                   "how everyone will know it is done, and what it will not do. Here is how to write one, using "
                   "the treasury encoding project as the example.",
        "publish_on": "2026-11-28 21:00",
        "body": [
            "The encoding project has a charter and a stakeholder map. The work is under way. Then, in the same "
            "week, three small requests arrive. The assessor’s office asks whether the team could also add the "
            "owners’ mobile numbers. A collector suggests printing the bills in two languages. The head of office "
            "wonders aloud whether the system could also show which properties have never been visited.",
            "Each idea is reasonable. Each would take only “a little extra time.” Together, they could push the "
            "January deadline into March. The revenue clerk needs a clear way to say what the project includes, "
            "and a calm way to handle everything else.",
            "(As in every part of this series, the office, the people and the numbers are made up. No real "
            "town or employee is described.)",
            "That clear way is the scope statement. In Part 2, the charter gave a short list of what was in and "
            "out. The scope statement goes one level deeper: it names each deliverable, says how everyone will know it is done, and becomes the page everyone checks when a new idea arrives. By the end of this post you will have a five-part template, a filled-in example and a calm way to answer extra requests.",
            ("h", "Two Kinds of Scope"),
            "Project management guides separate two ideas that are easy to mix up.",
            ("point", "Product scope", "The features and functions of the result. For the encoding project: "
             "a record for each taxable property in the four poblacion barangays, with the details needed to "
             "print a bill."),
            ("point", "Project scope", "The work needed to deliver that result. Encoding, checking against the "
             "assessor’s tax declarations, printing sample bills, training the counter staff."),
            "Keeping them apart helps. A request to add mobile numbers changes the product scope. A request to "
            "train the collectors as well as the counter staff changes the project scope. Both need a decision, "
            "but they affect different things. The first changes what the office receives at the end. The "
            "second changes how much work the team must do to get there, and who must be available to do it.",
            ("h", "The Five Parts of a Scope Statement"),
            "Guides list the contents in slightly different ways, but a practical scope statement usually opens with a short description of the result and then covers these five parts.",
            ("photo", "blog/pm-scope-statement.jpg", "A scope statement in five parts: the deliverables, the "
             "acceptance criteria, the exclusions, the assumptions and the constraints. (Illustration: Butch "
             "Mahinay, aumahinay.dev)", "medium"),
            ("point", "1. Deliverables", "What the project will hand over at the end, named so that anyone "
             "could check whether it exists."),
            ("point", "2. Acceptance criteria", "How the sponsor will judge that each deliverable is finished "
             "and good enough."),
            ("point", "3. Exclusions", "What the project will not do, written plainly."),
            ("point", "4. Assumptions", "What the plan takes for granted. If an assumption turns out to be "
             "wrong, the plan has to change."),
            ("point", "5. Constraints", "The fixed limits: deadlines, budget, people and rules that cannot be "
             "moved."),
            ("h", "The Encoding Project’s Scope Statement"),
            ("point", "Deliverables", "Property records for the four poblacion barangays in the new system. A "
             "list of records that did not match the assessor’s tax declarations, with the reason for each. "
             "Fifty printed sample bills. A hands-on session for the counter staff on printing and checking a bill."),
            ("point", "Acceptance criteria", "Every record matches the assessor’s tax declaration or appears "
             "on the mismatch list. The head of office checks twenty sample bills chosen at random against the "
             "ledger cards and finds no error in the amount due. The counter staff can print a bill without "
             "help."),
            ("point", "Exclusions", "Unpaid taxes from past years and their interest. The remaining barangays. "
             "Owners’ contact details. Bills in a second language. Any change to how payments are received."),
            ("point", "Assumptions", "The assessor’s office can spare one person on Tuesday and Thursday "
             "afternoons. The ledger cards for the four barangays are complete. The system can print bills on "
             "the office’s current printer."),
            ("point", "Constraints", "Ready at the counter on January 4. A budget of ₱18,000. Only two "
             "collectors available, two afternoons a week. Personal data handled under the office’s data "
             "privacy rules."),
            ("h", "Acceptance Criteria Do the Heavy Lifting"),
            "Of the five parts, acceptance criteria deserve the most care, because they decide when the "
            "project is finished. “Records are encoded correctly” sounds clear until someone asks how anyone would know.",
            "Good criteria can be checked by someone other than the person who did the work. Twenty bills chosen "
            "at random and compared with the ledger cards is a test anyone can run. It also tells the team, "
            "from the first day, what standard their work will be held to.",
            ("quote", "If you cannot say how you will know it is done, you do not yet know what you are building."),
            ("h", "Write Assumptions Down, Then Watch Them"),
            "Assumptions feel obvious when you write them, which is exactly why they are worth writing. Suppose "
            "that in the third week the team finds that one barangay’s ledger cards are incomplete. Because "
            "“the ledger cards are complete” was written as an assumption, nobody has to argue about whether "
            "the problem is serious. A written assumption has failed, so the plan must be reviewed with the "
            "sponsor.",
            "Read the assumptions again at each milestone. Finding a wrong one early leaves more time "
            "to adjust the plan.",
            ("h", "Handling the Three Requests"),
            "Now go back to the three ideas from the start. With a scope statement, each one gets the same calm "
            "answer: it is a good idea, it is not in the current scope, and here is what adding it would cost.",
            ("point", "Mobile numbers", "Excluded. Collecting contact details raises data privacy questions "
             "that need their own decision. Added to a list for a later phase."),
            ("point", "Bills in two languages", "Excluded. It would need a translation, a new bill layout and "
             "another round of checking. Added to the later list."),
            ("point", "Properties never visited", "Excluded from this project, but a useful question. It "
             "could become a report once all barangays are encoded."),
            "When someone asks in person, the clerk uses the same few sentences each time: “That is a good idea. It is not in the scope we agreed, so I have added it to the list for the next phase. If you need it now, the January 4 date would move or we would need another encoder. Shall I ask the head of office?”",
            "The clerk does not say no to anyone. She says “not in this project,” writes each idea down, and "
            "lets the sponsor decide whether any of them is worth moving the deadline for.",
            ("h", "Who Signs Off on the Scope"),
            "A scope statement only works if the sponsor has agreed to it. The clerk drafts it, shows it to the "
            "people whose work it describes, and then asks the head of office to approve it in writing, the same "
            "way the charter was approved.",
            "This step can feel like paperwork, but it changes every later conversation. When a new request "
            "arrives, the clerk is no longer defending her own opinion. She is pointing to a page the head of "
            "office signed. If the head of office decides to add something, that is a decision the sponsor is "
            "entitled to make, and the scope statement is updated, along with the deadline or the budget if "
            "they need to change.",
            "Keep each version of the scope statement, with its date. At the end of the project, the versions "
            "show exactly how the work grew and why, which is useful for the lessons-learned meeting and for "
            "planning the next phase.",
            ("h", "Scope Creep and Gold Plating"),
            "Two terms are worth knowing. Scope creep is work added to a project while it is under way, often one "
            "small request at a time. Gold plating is giving the customer extras that were never asked for, "
            "such as a team member adding a feature they think would be nice.",
            "Both have the same cost: time and effort spent outside the agreed scope, which puts the agreed "
            "work at risk. The scope statement is the reference that makes both visible.",
            ("h", "Key Takeaways"),
            ("point", "Write what is out as clearly as what is in", "A plain list of what is out settles many requests before they become arguments."),
            ("point", "Make acceptance checkable by someone else", "If nobody can test it, nobody can agree it is finished."),
            ("point", "Answer extra requests with the scope, not your opinion", "Log the idea, state the cost, and let the sponsor decide."),
            ("h", "Your Part 4 Exercise"),
            "Take the project from your charter and write a short scope statement:",
            ("point", "Three deliverables", "Name each one so that anyone could check whether it exists."),
            ("point", "One acceptance test for each", "How would someone else confirm it is done?"),
            ("point", "Three assumptions", "What are you taking for granted about people, data and tools?"),
            "Then look at the last request someone made about your project. Is it inside the scope you just "
            "wrote? If not, put it on a list and let your sponsor decide.",
            ("cta", "Read: Project Management Series, Part 3", "/blog/project-management-part-3-stakeholder-mapping/"),
            ("cta", "Read: Project Management Series, Part 2", "/blog/project-management-part-2-project-charter/"),
            ("cta", "Read: Business Intelligence Series, Part 4", "/blog/business-intelligence-part-4-the-bi-brief/"),
            ("cta", "Read: Your Data at the Treasury Counter", "/blog/your-data-at-the-treasury-counter/"),
            ("ask", "What was the last “small extra” that ended up costing your project more than expected?"),
        ],
    },
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
            "The real property tax encoding project now has a signed one-page charter. The "
            "revenue clerk feels ready. Then, a week later, a message arrives from the office of "
            "the local chief executive. The mayor heard that “the treasury is changing the tax "
            "bills” and wants to know why nobody told the mayor’s office before taxpayers started"
            " asking.",
            "Nothing has gone wrong with the work. The encoding is on schedule. But someone with "
            "a great deal of power over the project was not on the clerk’s list, and now she must"
            " spend a day explaining instead of a minute informing.",
            "(As in every part of this series, the office, the people and the numbers are made "
            "up. No real town or employee is described.)",
            "This part is about avoiding that day. It is about stakeholders: the people and "
            "groups who can affect a project or are affected by it. Finding them early, and "
            "deciding how to work with each one, is time well spent. By the end of this post, you"
            " will be able to list a project's stakeholders, place them on a power and interest "
            "grid, and plan how each one hears from you.",
            ("h", "Who Counts as a Stakeholder"),
            "It is tempting to think stakeholders are only the people who approve or pay for a "
            "project. The real list is wider. A stakeholder is anyone who can help the project, "
            "block it, or feel its results.",
            "For the encoding project, a first list might look like this:",
            ("point",
             "Inside the treasury",
             "The head of office as sponsor, the collectors doing the encoding, the cashier, and "
             "the staff at the counter who will use the new bills."),
            ("point",
             "Other offices",
             "The assessor’s office, whose tax declarations are the source of truth; the "
             "information technology staff who keep the system running; the accounting office, "
             "which relies on correct collection reports."),
            ("point",
             "Leadership",
             "The local chief executive and, depending on the town, members of the local council "
             "who field complaints from residents."),
            ("point",
             "Oversight",
             "The government auditors, who will later examine the records and the controls around them."),
            ("point",
             "The public",
             "Property owners who will receive the new bills and bring questions to the counter."),
            "Write the list with the team, not alone. The collectors may remember people the "
            "clerk would never think of, such as the staff at the information desk who hear "
            "taxpayers’ questions first.",
            ("h", "The Power and Interest Grid"),
            "Once the list is written, place each stakeholder on a simple grid. One side asks how"
            " much power they have over the project: can they approve, stop, fund or slow it? The"
            " other asks how much interest they have: how much do they care, or how much will the"
            " result affect them?",
            ("photo",
             "blog/pm-power-interest.jpg",
             "The power and interest grid: place each stakeholder by how much power they have "
             "over the project and how much they care about it, then engage them to match. "
             "(Illustration: Butch Mahinay, aumahinay.dev)",
             "medium"),
            ("point",
             "High power, high interest: manage closely",
             "These are the key players. Involve them in decisions, meet them regularly and never"
             " let them be surprised. For the encoding project, this is the head of office and "
             "the assessor."),
            ("point",
             "High power, lower interest: keep satisfied",
             "They can stop the project but are not following it day to day. Give them short, "
             "timely updates before they hear news from someone else. The local chief executive "
             "belongs here, which is exactly the clerk’s missed step."),
            ("point",
             "Lower power, high interest: keep informed",
             "They care a great deal and will feel the results, but cannot approve or stop the "
             "work. Tell them what is changing and listen to their concerns. The collectors and "
             "counter staff belong here, and so, in a different way, do the taxpayers."),
            ("point",
             "Lower power, lower interest: monitor",
             "Check now and then whether their position has changed. A bank where the office "
             "deposits collections may sit here unless the project changes how deposits are "
             "recorded."),
            "Positions are not fixed. The auditors may show little interest while the encoding is"
            " under way, then a great deal once the new records are used to produce official "
            "reports. Look at the grid again at each milestone in the charter.",
            ("h", "From Grid to Plan"),
            "The grid is only useful if it changes what you do. For each stakeholder, write one "
            "line: what they need to know, how they will hear it, and how often.",
            ("point",
             "Head of office",
             "A ten-minute update every Friday, plus a call the same day if a milestone is at risk."),
            ("point",
             "Local chief executive",
             "A short memo from the head of office before the project starts showing on bills, "
             "and a one-paragraph note when the system goes live."),
            ("point",
             "Assessor’s office",
             "A shared list of records with questions, checked on the agreed Tuesday and Thursday"
             " afternoons."),
            ("point",
             "Collectors and counter staff",
             "A fifteen-minute briefing before the January rush on what the new bill looks like "
             "and how to answer the three most common questions."),
            ("point",
             "Taxpayers",
             "A plain notice at the counter and on the office’s page explaining that bills are "
             "now printed, and who to ask if something looks wrong."),
            "Notice that the plan respects the chain of command. In this example, the clerk does "
            "not write to the mayor directly; the head of office does. Knowing who should speak "
            "to whom is part of stakeholder work, especially in government.",
            ("h", "Four Questions for Each Key Stakeholder"),
            "For the people in the top two boxes, a short conversation early in the project is "
            "worth more than any document. Ask each of them four questions, and write down the "
            "answers.",
            ("point",
             "What does success look like to you?",
             "The assessor may care most about matching records; the head of office about shorter"
             " lines in January. Both answers matter."),
            ("point",
             "What worries you about this project?",
             "Worries spoken early become risks you can plan for. Worries kept quiet become "
             "objections later."),
            ("point",
             "How would you like to hear from us?",
             "Some people want a short message, others a printed memo, others a two-minute talk "
             "in the hallway. Match their habit, not yours."),
            ("point",
             "Who else should we talk to?",
             "This question finds the stakeholders your list missed. It is how the clerk would "
             "have learned that the mayor’s office wanted to be told first."),
            ("h", "Influence Without Authority"),
            "In Part 1, the clerk discovered that nobody on her list reported to her. The grid "
            "does not change that, but it shows her where her influence will come from.",
            "With high-power stakeholders, influence comes through the sponsor. A request from "
            "the head of office carries weight that a request from the clerk does not. With "
            "high-interest stakeholders, influence comes from listening. Collectors who were "
            "asked how to make the encoding easier have helped shape the schedule, so part of it "
            "is theirs.",
            ("quote",
             "You cannot command the people on your map. You can make sure none of them is surprised."),
            ("h", "Common Mistakes"),
            ("point",
             "Mapping once and filing it",
             "People move around the grid. A new head of office or an election can change everything."),
            ("point",
             "Forgetting the quiet ones",
             "Ask the people with low power and high interest early. They may not speak up until "
             "something has gone wrong for them."),
            ("point",
             "Treating everyone the same",
             "Sending every stakeholder the same long weekly report wastes their time and hides "
             "the message that matters to each."),
            ("point",
             "Leaving the map lying around",
             "A stakeholder map is a working note. Keep it respectful and factual, and share it "
             "only with the project team."),
            ("h", "Key Takeaways"),
            ("point",
             "Stakeholders are wider than approvers",
             "Anyone who can help, block or feel the project belongs on the list."),
            ("point",
             "Use the power and interest grid",
             "Manage closely, keep satisfied, keep informed or monitor, and look again at each milestone."),
            ("point",
             "Plan each message",
             "For each key stakeholder, decide what they need to know, from whom and how often."),
            ("point",
             "Ask who else to talk to",
             "That one question finds the people your list missed, before they are surprised."),
            ("h", "Your Part 3 Exercise"),
            "Take the project from your one-page charter and do this:",
            ("point",
             "List",
             "Write every person or group who can help, block or feel the project. Aim for at least ten."),
            ("point",
             "Place",
             "Put each one in a box of the grid: manage closely, keep satisfied, keep informed or monitor."),
            ("point",
             "Plan",
             "For the people in the top two boxes, write what they need to hear, from whom and how often."),
            "Then ask yourself one question: who would be most upset to hear about this project "
            "from someone other than you? Inform that person this week.",
            ("cta",
             "Read: Project Management Series, Part 2",
             "/blog/project-management-part-2-project-charter/"),
            ("cta",
             "Read: Project Management Series, Part 1",
             "/blog/project-management-part-1-accidental-project-manager/"),
            ("cta",
             "Read: Business Intelligence Series, Part 2",
             "/blog/business-intelligence-part-2-the-bi-team/"),
            ("cta",
             "Read: The ALTOS Framework, Principle 3: Every Document Has an Owner",
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
            "Three weeks into the real property tax encoding project from Part 1, the revenue "
            "clerk is called into a meeting she did not expect. The assessor’s office says its "
            "staff cannot spare two afternoons a week after all. One collector asks why he was "
            "never told he would be helping. The head of office asks whether the bills for "
            "January will include unpaid taxes from past years, with their interest, or only the "
            "current year’s tax.",
            "Nobody in the room is being difficult. Each person simply remembers the assignment "
            "differently, because nobody ever wrote it down. The clerk now spends an hour "
            "defending decisions that were never really made.",
            "(As in every part of this series, the office, the people and the numbers are made "
            "up. No real town or employee is described.)",
            "This is the problem a project charter solves. It is the first document of a project,"
            " and in a small office it may be the only one you need. By the end of this post, you"
            " will know the six parts of a one-page charter, see one written for a treasury "
            "project, and know how to handle changes without arguments.",
            ("h", "What a Project Charter Is"),
            "A project charter is a short, signed document that officially starts a project. It "
            "records why the project exists, what it will deliver, when, with what money and "
            "people, and who is in charge. Most importantly, it is approved by the person with "
            "the authority to start the project, often called the sponsor. The same signature "
            "gives the project manager the authority to use the office’s people and resources for"
            " the work.",
            "That approval is what gives the charter its power. In Part 1, the clerk discovered "
            "that nobody on her list reported to her. A signed charter does not change the "
            "organization chart, but it does show everyone that the head of office has given the "
            "project a goal, a deadline and a leader. When the assessor’s staff are asked for "
            "time, the request is no longer a favor to the clerk. It is part of a project the "
            "head of office approved.",
            "Large organizations use long charters with many sections. A small office does not "
            "need that. One page, read in five minutes, is enough if it answers the right "
            "questions.",
            ("photo",
             "blog/pm-charter.jpg",
             "A one-page project charter answers six things before work begins: why, what, when, "
             "who, money and risks, and who signed. (Illustration: Butch Mahinay, aumahinay.dev)",
             "medium"),
            ("h", "The Six Parts of a One-Page Charter"),
            ("point",
             "1. Why: the purpose",
             "One or two sentences on the problem the project solves and the result it should "
             "bring. Write it so a taxpayer could understand it."),
            ("point",
             "2. What: the scope, in and out",
             "The main things the project will deliver, followed by a short list of what it will "
             "not do. The “not included” list prevents more arguments than any other line on the "
             "page."),
            ("point",
             "3. When: the milestones",
             "Three to five dates that mark real progress, ending with the date the project is "
             "finished. Not every task, only the checkpoints."),
            ("point",
             "4. Who: the roles",
             "The sponsor, the project manager, the team members and the offices whose help is "
             "needed. Name the people, not only the units."),
            ("point",
             "5. Money and risks",
             "The budget, even if it is small, where it comes from, and the three biggest things "
             "that could go wrong."),
            ("point",
             "6. Sign: the approval",
             "The sponsor’s name, signature and date, and the date the charter will next be reviewed."),
            ("h", "The Encoding Project, Written as a Charter"),
            "Here is how the clerk’s project could look on one page. Notice how many of the "
            "questions from that difficult meeting are answered before anyone asks them.",
            ("point",
             "Why",
             "Bills for real property tax are still written by hand from ledger cards, which is "
             "slow and leads to errors at the counter. This project puts the ledger records into "
             "the office’s new system, so bills can be printed and checked before the January "
             "rush."),
            ("point",
             "What is included",
             "Encoding the ledger records of all taxable properties in the four poblacion (town "
             "center) barangays, checking each record against the assessor’s tax declarations, "
             "and printing a sample of bills for review."),
            ("point",
             "What is not included",
             "Unpaid taxes from past years and their interest (a separate project in February), "
             "the remaining barangays (next phase), and any change to how payments are received "
             "at the counter."),
            ("point",
             "Milestones",
             "Records of the first two barangays encoded and checked by November 27. All four "
             "barangays by December 11. Sample bills reviewed by the head of office by December "
             "18. System ready at the counter on January 4."),
            ("point",
             "Who",
             "Sponsor: the head of office. Project manager: the revenue clerk. Team: two "
             "collectors for encoding, two afternoons a week. Support: the assessor’s office, one"
             " staff member for checking, Tuesday and Thursday afternoons."),
            ("point",
             "Money and risks",
             "₱18,000 from the office budget for paper, toner and a backup drive, bought through "
             "the usual procurement steps. Risks: the assessor’s staff may be pulled away by "
             "year-end work; old ledger cards may be hard to read; the system may slow down when "
             "many records are added at once."),
            ("point", "Sign", "Approved by the head of office, with a review set for December 11."),
            "Now the assessor’s time is written down and approved. The collector can be shown the"
            " page. And the question about past-year taxes has a clear answer: not in this "
            "project. None of these lines is complicated. Each one prevents a meeting.",
            ("h", "Five Mistakes That Weaken a Charter"),
            ("point",
             "Writing it alone",
             "A charter written by the project manager and simply handed out is a wish list. "
             "Draft it with the sponsor, then show it to the people whose time it asks for."),
            ("point",
             "Leaving out what is not included",
             "If the page lists only what the project will do, people will assume it does "
             "everything they hoped for."),
            ("point",
             "Vague success",
             "“Improve billing” cannot be checked. “Bills for the four poblacion barangays "
             "printed from the system by January 4” can."),
            ("point",
             "No real signature",
             "A charter nobody signed is just a note. In a government office, the head’s "
             "signature or a short office order is what turns the page into a commitment."),
            ("point",
             "Filing it and forgetting it",
             "Read the charter again at each milestone. If the project has changed, update the "
             "page and have it signed again."),
            ("h", "When the Plan Changes"),
            "A charter is not a promise that nothing will change. Projects meet surprises. The "
            "value of the charter is that every change becomes a clear decision instead of a slow"
            " drift.",
            "Suppose in December the head of office decides that past-year taxes must be included"
            " after all. With a charter, the clerk can answer calmly: “We can add them. That "
            "means more records to check, so either the January 4 date moves, or we get one more "
            "encoder, or we do the poblacion now and the past years in February. Which would you "
            "prefer?” This is the triangle of scope, time and cost from Part 1, now written on "
            "paper where everyone can see it.",
            ("quote", "A charter does not stop change. It makes every change a decision."),
            ("h", "A Note for Software Projects"),
            "The same page works when the project is a piece of software. Before building a tool,"
            " even a small collection app, write down what it will do, what it will not do, and "
            "who decides when it is ready. Software invites endless small additions, and the “not"
            " included” list is what lets the first version ever be finished. Everything else can"
            " wait for the next version, with its own page.",
            ("h", "Key Takeaways"),
            ("point",
             "One page, signed",
             "A short charter approved by the sponsor gives the project a goal, a deadline and a leader."),
            ("point",
             "List what is not included",
             "The out-of-scope line prevents more arguments than any other part of the page."),
            ("point",
             "Make success checkable",
             "Write a result someone can confirm with a date, not a hope such as “improve billing.”"),
            ("point",
             "Every change becomes a decision",
             "With a charter, a new request comes with clear trade-offs for the sponsor to choose from."),
            ("h", "Your Part 2 Exercise"),
            "Take the assignment you looked at in Part 1. On one sheet of paper or one screen, write:",
            ("point", "One sentence of purpose", "Why does this project exist?"),
            ("point", "Three things in, three things out", "What it delivers, and what it will not touch."),
            ("point", "Three dates", "Two checkpoints and a finish line."),
            ("point", "Names", "The sponsor, yourself and everyone whose time you need."),
            "Then take it to your sponsor and ask one question: “Is this what you meant?” Their "
            "answer is worth more than a week of work done in the wrong direction.",
            ("cta",
             "Read: Project Management Series, Part 1",
             "/blog/project-management-part-1-accidental-project-manager/"),
            ("cta",
             "Read: The ALTOS Framework, Principle 3: Every Document Has an Owner",
             "/blog/altos-framework-every-document-has-an-owner/"),
            ("cta",
             "Read: The ALTOS Framework, Principle 4: Every Owner Has a Deadline",
             "/blog/altos-framework-every-owner-has-a-deadline/"),
            ("cta",
             "Read: Business Intelligence Series, Part 2",
             "/blog/business-intelligence-part-2-the-bi-team/"),
            ("ask",
             "Have you ever worked on a project where everyone remembered the goal differently? "
             "What would a one-page charter have changed?"),
        ],
    },
    {
        "date": "November 13, 2026",
        "title": "Project Management Series, Part 1: The Accidental Project Manager in the Treasury",
        "slug": "project-management-part-1-accidental-project-manager",
        "category": "pm",
        "summary": (
            (
                "A project can land on your desk without the title. Here is how a project differs"
                " from daily work, the three limits every project lives with, and four moves to "
                "make in your first two weeks."
            )
        ),
        "publish_on": "2026-11-13",
        "body": [
            "It is the second week of October. The head of the treasury calls a revenue clerk "
            "into the office. “You are good with computers. Before the January rush, I want our "
            "real property tax ledger cards encoded into the new system, so we can print bills "
            "instead of writing them by hand. Work with the assessor’s office and the collectors."
            " Can you handle it?”",
            "The clerk says yes. Of course she says yes. Then she walks back to her desk and "
            "realizes three things at once. Nobody on that list reports to her. Every one of them"
            " already has a full day of work. And she has never run anything like this before.",
            "(As in every part of this series, the office, the people and the numbers are made "
            "up. No real town or employee is described.)",
            "If that scene feels familiar, welcome. You have just become what people in the field"
            " call an accidental project manager.",
            ("h", "Why I Am Writing This Series"),
            "I completed the Google Project Management Professional Certificate on Coursera, and "
            "later the Google Stakeholder Management specialization. My own biggest project so "
            "far is ALTOS, a treasury system for Philippine local treasuries. It has been built "
            "and tested on the developer side only. Building software is not part of my official "
            "duties, so before any office can put it to real use, the documents must come first, "
            "beginning with a memorandum of agreement. That order, paperwork before launch, is "
            "itself a project management lesson.",
            "Project management lessons online can lean on product launches, marketing campaigns "
            "and software companies. The ideas are good, but those examples can feel far from a "
            "municipal hall. This series explains the same ideas in plain words, with examples "
            "from treasury work: tax campaigns, new systems, year-end closing, audits and the "
            "people at the counter. By the end of this post, you will be able to tell a project "
            "from daily work, explain the three limits every project lives with, and make four "
            "moves that set up your first two weeks.",
            ("h", "Is It a Project, or Is It Just Work?"),
            "Start with the most useful question in the whole field. Not everything you do at "
            "work is a project, and mixing the two up causes a lot of stress.",
            ("point",
             "Operations",
             "The work that repeats. Issuing official receipts, preparing the daily report of "
             "collections and deposits, answering taxpayers at the window, filing monthly "
             "reports. It never finishes. Tomorrow you do it again, and the office has a routine "
             "for it."),
            ("point",
             "A project",
             "Work with a start, an end and a result that did not exist before. Encoding the "
             "ledger cards, setting up a new collection system, holding a one-month tax campaign "
             "in the far barangays, or moving the records room. When the result is delivered, the"
             " project is over."),
            "The Project Management Institute, the group behind the widely used PMBOK Guide, puts"
            " it simply: a project is a temporary effort to create a unique product, service or "
            "result. Two words matter there. Temporary means it ends. Unique means the office has"
            " not done this exact thing before, so there is no routine to follow.",
            "Here is a quick test you can use on any new assignment. Does it have a finish line? "
            "Will something exist afterward that does not exist now? Will you need people from "
            "outside your own desk to get there? If the answer to all three is yes, you are "
            "holding a project.",
            "Why does the label matter? Because operations run on habit, and projects cannot. The"
            " daily routine has an established way of doing things. A project has surprises, gaps"
            " and questions nobody has answered yet. If you try to run it like routine work, "
            "squeezing it into the spare minutes between taxpayers, it will drift for months. A "
            "project needs its own plan, its own time and someone whose job is to steer it.",
            ("h", "The Three Limits Every Project Lives With"),
            "Every project is held in place by three limits. Textbooks call them the triple "
            "constraint, and many people draw them as a triangle.",
            ("point",
             "Scope",
             "What you will deliver. In our example: which ledger cards get encoded, which "
             "fields, and which bills the system must print."),
            ("point",
             "Time",
             "When it must be done. Here, before the January rush, when owners line up to pay and"
             " the office has no spare hands."),
            ("point",
             "Cost",
             "What you can spend, including people’s hours. Two encoders for six weeks is a cost,"
             " even if no one is paid extra."),
            "In the middle of the triangle sits quality: whether the result is accurate and "
            "actually works. The rule is simple and unforgiving. You cannot pull one side without"
            " moving another. If you add to the scope, you need more time or more people. If you "
            "cut the time, you must cut the scope or add people. If you refuse to change anything"
            " else, the middle gives way, and quality is what breaks.",
            ("photo",
             "blog/pm-triple-constraint.jpg",
             "Scope, time and cost hold each other in place. Push one side and another must move,"
             " or quality in the middle pays the price. (Illustration: Butch Mahinay, "
             "aumahinay.dev)",
             "medium"),
            "Picture this in our office. Halfway through, someone says, “While you are at it, "
            "encode the business records too.” If the deadline and the two encoders stay the "
            "same, the team will rush. Assessed values get typed wrong, a few hundred cards get "
            "skipped, and in January a property owner is billed for land she sold years ago. "
            "Nobody decided to lower quality. It simply happened because the triangle was "
            "ignored.",
            "The fix is not to refuse. It is to offer a clear choice. “Yes, we can add the "
            "business records. We can push the finish by three weeks, borrow one more encoder "
            "from another unit, or finish the property cards first and do business records as a "
            "second phase. Which do you prefer?” That one sentence turns a complaint into a "
            "decision, and it puts the decision with the person who has the authority to make it.",
            ("quote",
             "You cannot add to a project for free. Something always pays: time, people, or quality."),
            ("h", "The Life of a Project, From Start to Finish"),
            "Projects move through stages. The Google course teaches four: initiate, plan, "
            "execute and close. The PMBOK Guide also names a fifth kind of work, monitoring and "
            "controlling, which is not a separate stage but runs alongside the doing. Here are "
            "all five in plain words, using our ledger project.",
            ("point",
             "Initiate",
             "Agree on why the project exists and what success looks like. For example: all "
             "active property accounts encoded and checked, so bills print from the system by "
             "January."),
            ("point",
             "Plan",
             "Break the work into tasks, decide who does each one and in what order, and list "
             "what could go wrong, such as missing cards or a printer that fails."),
            ("point",
             "Execute",
             "Do the work. Encoders type, collectors check accounts in their area, and the "
             "project manager removes whatever is blocking them."),
            ("point",
             "Monitor and control",
             "Compare the plan with what is really happening, every week. Are we on pace? Are new"
             " requests sneaking in? Adjust early, while problems are still small."),
            ("point",
             "Close",
             "Hand the result to the people who will use it every day, store the records, and sit"
             " down for half an hour to talk about what to keep and what to change next time."),
            "A project can fail before the doing even starts, because nobody agreed on what "
            "“done” means, or at the very end, because the work was never handed over properly "
            "and slowly slid back to the old way.",
            ("h", "Your First Two Weeks: Four Moves"),
            "When a project lands on your desk, the temptation is to start working right away. "
            "Resist it for a few days. These four moves will save you weeks later.",
            ("point",
             "1. Talk to the person who asked",
             "In project language, this is the sponsor: the head of office or official who owns "
             "the result. Ask three questions. What will tell you this was a success? What is not"
             " included? And if something has to give, which matters most: the deadline, the "
             "scope or the budget?"),
            ("point",
             "2. Put it on one page",
             "Write down the goal, the deadline, the people involved and what is left out. Send "
             "it back to the sponsor and ask them to confirm. This short page will settle many "
             "arguments before they start."),
            ("point",
             "3. Ask the people doing the work before you promise a date",
             "The collectors and clerks know their busy weeks. In a treasury, the days before "
             "each quarterly real property tax deadline (March 31, June 30, September 30 and "
             "December 31) are not the time to borrow anyone. A schedule built with the people "
             "who will follow it is a schedule they will defend."),
            ("point",
             "4. Keep one place for everything",
             "One shared folder or one board for the task list, the decisions and the files. Not "
             "five chat groups, three notebooks and a stack of memos. Agree on a simple rule: if "
             "a decision is not written there, it was not made."),
            ("h", "The Dispatcher, Not the Driver"),
            "Capable people can fall into a trap when they lead their first project. When an "
            "encoder falls behind, they stay late and encode the cards themselves. When the "
            "system shows an error, they spend two days fixing it alone. Meanwhile, nobody is "
            "watching the schedule, the sponsor hears nothing, and the project quietly stalls.",
            "Think of a jeepney dispatcher at a busy terminal. The dispatcher does not drive any "
            "of the jeeps. Yet without someone keeping the line moving, calling the next trip and"
            " sorting out the jam at the gate, the whole terminal grinds to a halt. That is the "
            "project manager’s job. Your value is not the number of tasks you finish with your "
            "own hands. It is how clearly everyone knows the goal, how quickly blocks are "
            "cleared, and whether the project reaches the end.",
            "You may still do some of the work, especially in a small office. Just know which hat"
            " you are wearing at any moment, and never let the doing crowd out the steering.",
            ("h", "Key Takeaways"),
            ("point",
             "Projects are not operations",
             "A project has a finish line and a new result. Running it like routine work lets it drift."),
            ("point",
             "The triangle always holds",
             "Scope, time and cost move together. Ignore that, and quality pays the price."),
            ("point",
             "Offer choices, not refusals",
             "When more work is added, give the sponsor clear options and let the person with "
             "authority choose."),
            ("point",
             "Steer, do not just drive",
             "Your value is a clear goal, cleared blocks and a project that reaches the end."),
            ("h", "Your Part 1 Exercise"),
            "Pick one assignment you are carrying now, big or small. This week, write one line "
            "for each of these:",
            ("point", "Project or operations?", "Does it have a finish line and a new result at the end?"),
            ("point", "Who decides it is done?", "Name the one person whose approval ends the project."),
            ("point", "Which limit is tightest?", "Scope, time or cost. Which one can you not move?"),
            "If you cannot answer one of them, that is your first task: a fifteen-minute talk "
            "with the person who gave you the assignment.",
            ("cta", "Read: Why I Built ALTOS", "/blog/why-i-built-altos/"),
            ("cta",
             "Read: The ALTOS Framework, Principle 4: Every Owner Has a Deadline",
             "/blog/altos-framework-every-owner-has-a-deadline/"),
            ("cta", "Read: Year-End in the Treasury", "/blog/year-end-in-the-treasury/"),
            ("cta", "Read: Data Analytics Series, Part 1", "/blog/data-analytics-part-1-what-it-is/"),
            ("ask",
             "Have you ever been handed a project at work without being told it was one? How did it go?"),
        ],
    },
]
