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
        "title": "Project Management Series, Part 52: The Whole Series on One Page, From First Idea to Lessons Learned",
        "slug": "project-management-part-52-series-on-one-page",
        "category": "pm",
        "date": "June 7, 2028",
        "summary": "This is the last part of the Project Management Series. It arranges the 51 earlier parts "
                   "into the order a real project needs them, from the first idea to the benefits review, with "
                   "one question to ask at each stage and a short list of the parts to reread when that "
                   "question comes up.",
        "publish_on": "2028-06-07 21:00",
        "body": [
            "A colleague from the assessor’s office stopped by the treasury with a printed memo. She had just "
            "been named to lead the digitization of the property records, a project with a budget, a deadline "
            "and six people from three offices. “I have never run a project,” she said. “Where do I even "
            "start?”",
            "Fifty-one parts of this series had tried to answer that question one piece at a time. What she "
            "needed was the whole map, in the order she would use it.",
            "(The colleague and her project are invented for this post. The parts listed are the earlier "
            "posts in this series, which explain each idea in full.)",
            "This is the closing part of the Project Management Series. It does not add a new technique. When "
            "you finish reading, you will have the series arranged into seven stages, a question to ask at "
            "each stage, the parts to reread when that question comes up, and a short plan for your next "
            "project.",
            ("photo", "blog/pm-series-map.jpg", "The series in seven stages, from deciding whether to start "
             "to checking whether the benefits arrived. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Stage 1: Should We Do This at All?"),
            ("quote", "Is this worth doing, and is it worth doing now?"),
            "Some projects that run into trouble were not clearly chosen. Someone had an idea, and work "
            "started before anyone compared it with the other things the office could do.",
            ("point", "Part 1", "The accidental project manager: recognizing that a piece of work is a "
             "project at all."),
            ("point", "Part 10", "The business case: the problem, the options and the cost of doing nothing."),
            ("point", "Part 29", "The scoring matrix: choosing among several requests when the office cannot "
             "do them all."),
            ("h", "Stage 2: What Exactly Are We Doing?"),
            ("quote", "What is in, what is out, and how will we know we are done?"),
            ("point", "Part 2", "The one-page charter: purpose, sponsor, scope, deadline and budget."),
            ("point", "Part 4", "Drawing the line: writing down what is out of scope as clearly as what is in."),
            ("point", "Part 6", "Objectives with a number and a date, not just good intentions."),
            ("point", "Part 9", "Requirements, gathered from the people who will use the result."),
            ("point", "Part 5", "Waterfall, agile or hybrid: choosing how the work will run."),
            ("h", "Stage 3: Who Is Involved?"),
            ("quote", "Who decides, who does the work, and who needs to hear about it?"),
            ("point", "Part 3", "Mapping who holds power and who is affected."),
            ("point", "Part 8", "The RACI matrix: one person accountable for each piece of work."),
            ("point", "Part 11", "The communication plan: who hears what, when and how."),
            ("point", "Part 51", "Partner agencies: putting the agreement in writing."),
            ("point", "Part 7", "The kickoff meeting that brings everyone onto the same page."),
            ("h", "Stage 4: How Will We Get There?"),
            ("quote", "What are the pieces, how long will they take, and what will they cost?"),
            ("point", "Part 14", "The work breakdown structure, one bite at a time."),
            ("point", "Parts 15 and 21", "Estimates that allow for reality, and buffers instead of hidden "
             "padding."),
            ("point", "Parts 16 and 20", "Dependencies and the critical path that sets the finish date."),
            ("point", "Part 41", "A Gantt chart in Google Sheets that anyone can read."),
            ("point", "Parts 17, 18 and 22", "The budget, the people and the things the project must buy."),
            ("point", "Parts 19 and 49", "The risk register, and the pre-mortem that finds risks the "
             "register missed."),
            ("point", "Part 23", "Quality planning: deciding what good enough means before the work starts."),
            ("point", "Part 13", "The pre-launch checklist that reviews all of the above."),
            ("h", "Stage 5: Keeping It on Track"),
            ("quote", "Are we where we said we would be, and if not, what do we do?"),
            ("point", "Parts 25 and 35", "The one-page status report, and earned value for budget and "
             "schedule."),
            ("point", "Parts 26 and 48", "The issue log and the decision log."),
            ("point", "Part 24", "Change control: saying yes to a change without losing the plan."),
            ("point", "Parts 27 and 36", "Meetings that decide, and Kanban boards that limit work in "
             "progress."),
            ("point", "Part 40", "Retrospectives while the work is still running."),
            ("point", "Part 43", "A recovery plan when the project is in trouble."),
            ("point", "Part 44", "Several projects at once without dropping any."),
            ("h", "Stage 6: The People Doing the Work"),
            ("quote", "Does the team have what it needs to keep going?"),
            ("point", "Parts 45 and 46", "Delegating without losing track, and bringing in a new person."),
            ("point", "Parts 31 and 47", "Covering for absences, and negotiating with other offices for "
             "people and time."),
            ("point", "Parts 38 and 50", "Handling conflict, and keeping morale up through a long project."),
            ("point", "Part 34", "Presenting to decision makers in ten minutes."),
            ("h", "Stage 7: Finishing and Checking"),
            ("quote", "Did it work, will people use it, and what did we learn?"),
            ("point", "Parts 32 and 42", "A pilot before going big, and acceptance testing by the people who "
             "will use the result."),
            ("point", "Parts 33 and 37", "Getting people to adopt the new process, and a procedure they "
             "actually follow."),
            ("point", "Part 28", "Closing the project: handover and lessons learned."),
            ("point", "Part 39", "The benefits review, months after the project ends."),
            ("point", "Part 30", "The project kit: templates so the next project starts faster."),
            ("point", "Part 12", "Software, chosen after the process is clear, not before."),
            ("photo", "blog/pm-series-map-questions.jpg", "One question for each stage. When the question "
             "comes up, reread the parts listed under it. (Illustration: Butch Mahinay, aumahinay.dev)",
             "medium"),
            ("h", "Not Every Project Needs Every Part"),
            "A two-week task with three people does not need earned value or a formal change control board. "
            "A two-year system rollout with several offices probably needs most of the list.",
            ("point", "For a small project", "A charter, a task list with owners and dates, a short risk list, "
             "and a closing note on what was learned."),
            ("point", "For a medium project", "Add a RACI, a Gantt chart, a status report and an issue log."),
            ("point", "For a large project", "Add the budget by work package, change control, earned value, "
             "a pilot, acceptance testing and a benefits review."),
            "The size of the paperwork should match the size of the risk. Too little, and problems surface "
            "late. Too much, and the team spends its time filling in forms instead of doing the work.",
            ("h", "If You Read Only Five Parts"),
            "Some readers will not have time for the whole series. These five cover the most ground for "
            "the least reading.",
            ("point", "Part 2, the charter", "It forces the early decisions onto one page."),
            ("point", "Part 8, the RACI", "It ends arguments about who was supposed to do what."),
            ("point", "Part 19, the risk register", "It turns worry into a list with owners."),
            ("point", "Part 25, the status report", "It tells the truth early, while there is still time."),
            ("point", "Part 28, closing", "It makes sure the lessons survive the project."),
            ("h", "Back to the Assessor’s Office"),
            "The colleague left with three things: the seven questions on one sheet, the list of parts for "
            "Stages 1 and 2, and an appointment to review her charter the following week. She did not try to "
            "read all fifty-one parts. She read the ones her project needed, when it needed them.",
            ("h", "Mistakes to Avoid"),
            ("point", "Starting with the software", "Settle the scope and the process first."),
            ("point", "Skipping Stage 1", "A project nobody chose has nobody to defend it later."),
            ("point", "Using every tool on every project", "Match the paperwork to the size and the risk."),
            ("point", "Stopping at the handover", "Check later whether the benefits arrived."),
            ("h", "Quick Recap"),
            ("point", "Seven stages", "Choose, define, involve, plan, track, support the team, finish and "
             "check."),
            ("point", "One question per stage", "Ask it, then reread the parts listed under it."),
            ("point", "Scale the method", "Small projects need a few tools; large ones need more."),
            ("point", "People make it work", "Plans succeed when the team, partners and users are on board."),
            ("h", "Your Part 52 Action Plan"),
            ("point", "Pick one project", "A real one in your office, starting soon or already running."),
            ("point", "Find its stage", "Which of the seven questions is it facing now?"),
            ("point", "Reread two parts", "Choose two from that stage and apply one idea from each this week."),
            ("point", "Save a kit", "Keep the templates you used, as Part 30 suggested, for the next one."),
            ("cta", "Read: Project Management Series, Part 1: The Accidental Project Manager in the Treasury", "/blog/project-management-part-1-accidental-project-manager/"),
            ("cta", "Read: Project Management Series, Part 2: The Project Charter on One Page", "/blog/project-management-part-2-project-charter/"),
            ("cta", "Read: Project Management Series, Part 13: The Pre-Launch Checklist, a Review of Parts 1 to 12", "/blog/project-management-part-13-pre-launch-checklist/"),
            ("cta", "Read: Project Management Series, Part 30: The Project Kit, Reusable Templates So the Next Project Starts Faster", "/blog/project-management-part-30-project-kit/"),
            ("ask", "Which part of this series helped your work the most?"),
        ],
    },
    {
        "title": "Project Management Series, Part 51: Working With a Partner Agency, Putting the Agreement in Writing",
        "slug": "project-management-part-51-memorandum-of-agreement",
        "category": "pm",
        "date": "June 2, 2028",
        "summary": "When a project depends on another agency, such as a state university, a national office or a "
                   "bank, a handshake is not enough. This part shows what a memorandum of agreement should "
                   "cover, who has to approve it before the local chief executive signs, and how to manage "
                   "the partnership once the work starts.",
        "publish_on": "2028-06-02 21:00",
        "body": [
            "The filing room project had a new idea. A state university nearby offered to send six "
            "information technology students as interns for eight weeks to help scan the indexed real "
            "property records. The dean and the revenue officer shook hands on it at a meeting in March.",
            "By May, nothing had happened. The university wanted to know who would supervise the students, "
            "whether they would be insured, and who would own the scanned files. The treasury wanted to know "
            "how the students would handle taxpayers’ personal data. Nobody had written any of it down.",
            "(The office, the university and the people are invented, continuing the treasury examples of "
            "this series. The rule on contracts quoted below comes from the Local Government Code of 1991 "
            "as quoted by the Supreme Court. Ask your legal officer how it applies to a specific agreement.)",
            "Part 47 negotiated with offices inside the same local government. This part goes outside it. "
            "Stay with me to the end, and you will know when a partnership needs a written agreement, what a "
            "memorandum of agreement should contain, who must approve it, how to handle personal data and "
            "costs, and how to manage the partnership after signing.",
            ("photo", "blog/pm-moa.jpg", "Working with a partner agency: agree on the purpose, divide the "
             "duties, settle costs and data, and get the right approvals before signing. (Illustration: "
             "Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "When a Handshake Is Not Enough"),
            "A written agreement is worth the effort when any of these is true.",
            ("point", "Another organization commits people or equipment", "Interns, trainers, servers or "
             "software from outside the local government."),
            ("point", "Money moves", "Either side pays for anything, including allowances, insurance or "
             "transport."),
            ("point", "Data is shared", "Especially taxpayers’ personal data."),
            ("point", "The work runs for weeks or longer", "People change jobs. A written agreement outlasts "
             "the people who shook hands."),
            "In the Philippine public sector, a common form is a memorandum of agreement, often shortened to "
            "MOA. It records what each side will do, for how long, and under what conditions.",
            ("h", "What the Agreement Should Contain"),
            ("point", "The parties and signatories", "The full names of both organizations and who signs for "
             "each."),
            ("point", "Purpose", "One paragraph: what the partnership is for. “To scan indexed real property "
             "records of the municipal treasury, with student interns of the university.”"),
            ("point", "Each side’s duties", "A list for each party. Who supervises, who trains, who provides "
             "computers and scanners, who prepares the work schedule."),
            ("point", "Duration and schedule", "Start date, end date and working hours."),
            ("point", "Costs", "Who pays for what, such as allowances, insurance and supplies, and from "
             "which budget."),
            ("point", "Data and confidentiality", "What data the partner will see, how it will be protected, "
             "and what happens to copies at the end."),
            ("point", "Ownership of outputs", "Who owns the scanned files, reports or software produced."),
            ("point", "Changes and ending early", "How either side can amend or end the agreement, with "
             "notice."),
            ("point", "Contacts", "One named coordinator on each side."),
            ("h", "Who Must Approve It"),
            "Section 22(c) of the Local Government Code, as quoted by the Supreme Court, provides that "
            "“no contract may be entered into by the local chief executive in behalf of the local government "
            "unit” without prior authorization by the sanggunian concerned, unless the Code provides "
            "otherwise.",
            "In Quisumbing v. Garcia, G.R. No. 175527, decided on December 8, 2008, the Court explained that "
            "“the appropriation passed by the sanggunian may validly serve as the authorization required "
            "under Sec. 22(c)” when it specifically covers the project or contract. Whether a separate "
            "authorization is needed depends on the facts.",
            ("point", "Ask the legal officer early", "Whether this MOA needs a sanggunian resolution, and how "
             "long that takes."),
            ("point", "Build the time into the plan", "A sanggunian session may come only once a week. Part "
             "16’s critical path should include the approval."),
            ("point", "The partner has its own approvals", "A university may need its president or board. "
             "Ask early."),
            ("photo", "blog/pm-moa-path.jpg", "From handshake to signed agreement: draft, review by both legal "
             "offices, approvals including any sanggunian authorization, signing, then a kickoff. The path "
             "is a guide. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Handling Personal Data"),
            "Real property records hold names, addresses and other personal details. A partner who handles "
            "them takes on responsibilities too.",
            ("point", "Share only what is needed", "Interns scanning documents need the documents, not access "
             "to the whole tax system."),
            ("point", "Write the rules in the MOA", "No copies on personal devices, work only on office "
             "computers, and return or delete files at the end."),
            ("point", "Brief every person", "A short session on confidentiality before the first day, with a "
             "signed acknowledgment."),
            ("point", "Ask the data protection officer", "The local government’s data protection officer can "
             "check the arrangement against the Data Privacy Act, as Part 6 of the Data Analytics Series "
             "discussed."),
            ("h", "Managing the Partnership After Signing"),
            "A signed agreement starts the work. It does not run it.",
            ("point", "Hold a joint kickoff", "Both coordinators, the supervisors and the interns, using "
             "Part 7’s kickoff agenda."),
            ("point", "Meet on a schedule", "A short check-in every two weeks between the two "
             "coordinators."),
            ("point", "Track the MOA’s duties", "Turn each party’s duties into tasks in the project plan, "
             "with owners and dates."),
            ("point", "Raise problems early", "If one side cannot meet a duty, say so and amend the agreement "
             "in writing, rather than letting it drift."),
            ("point", "Close properly", "At the end, confirm that files were returned or deleted, thank the "
             "partner in writing, and record lessons, as Part 28 described."),
            ("h", "A One-Page Summary for the Team"),
            "Few people on a project team will read a four-page agreement. They still need to know what it "
            "says about their own work.",
            ("point", "Summarize the duties", "One page listing what the partner will do, what the office "
             "will do, and who the two coordinators are."),
            ("point", "Highlight the limits", "Working hours, the data rules and anything the partner’s "
             "people may not do."),
            ("point", "Add the dates", "Start, end, check-ins and any report due under the agreement."),
            ("point", "Keep the signed copy safe", "File the original with the legal officer or the records "
             "unit, and keep a scanned copy in the project folder."),
            "When a question comes up in the middle of the work, the team can check the summary first and "
            "go to the full agreement only when the summary does not answer it.",
            ("h", "Back to the Interns"),
            "The revenue officer and the dean’s office drafted a four-page MOA in two weeks. The university "
            "would supervise and insure the students; the treasury would provide two scanning stations, a "
            "work schedule and a daily supervisor. Scanned files would belong to the municipality, and no "
            "data would leave the office computers.",
            "The legal officer advised that the agreement needed a sanggunian resolution authorizing the "
            "mayor to sign. It passed at the next regular session. The interns started in July, a term "
            "later than first hoped, and scanned more than 9,000 records in eight weeks.",
            ("h", "Mistakes to Avoid"),
            ("point", "Starting on a handshake", "Write it down before people or data move."),
            ("point", "Forgetting approvals", "Ask the legal officer whether sanggunian authorization is "
             "needed."),
            ("point", "Vague duties", "List each side’s tasks, not just shared goals."),
            ("point", "No data rules", "Say what can be seen, copied and kept."),
            ("h", "Quick Recap"),
            ("point", "Write it when it matters", "People, money, data or a long time frame."),
            ("point", "Cover the essentials", "Purpose, duties, duration, costs, data, outputs, changes, "
             "contacts."),
            ("point", "Plan for approvals", "Section 22(c) may require sanggunian authorization."),
            ("point", "Manage it after signing", "Kickoff, regular check-ins and a proper close."),
            ("h", "Your Part 51 Action Plan"),
            ("point", "Today", "List every outside partner your project depends on, and whether there is a "
             "written agreement."),
            ("point", "This week", "Ask the legal officer for the office’s usual MOA template and approval "
             "steps."),
            ("point", "Before any data moves", "Add data and confidentiality rules to the agreement."),
            ("cta", "Read: Project Management Series, Part 47: Negotiating With Other Offices for People, Equipment and Time", "/blog/project-management-part-47-negotiating-with-other-offices/"),
            ("cta", "Read: Project Management Series, Part 22: Procurement and Suppliers, Planning What You Must Buy", "/blog/project-management-part-22-procurement-and-suppliers/"),
            ("cta", "Read: Project Management Series, Part 8: Who Does What? Building a RACI Matrix", "/blog/project-management-part-8-raci-matrix/"),
            ("cta", "Read: Data Analytics Series, Part 6: Data Ethics and the Data Privacy Act for Analysts", "/blog/data-analytics-part-6-data-ethics-privacy/"),
            ("ask", "Which partner does your project rely on without a written agreement?"),
        ],
    },
    {
        "title": "Project Management Series, Part 50: Keeping a Team Going Through a Long Project",
        "slug": "project-management-part-50-team-morale",
        "category": "pm",
        "date": "May 29, 2028",
        "summary": "Long projects lose energy in the middle, when the start is forgotten and the finish is far "
                   "away. This part uses research on daily work life to show how to make progress visible, "
                   "remove small obstacles, handle setbacks without blame, protect people from overload, and "
                   "recognize work in ways that fit a government office.",
        "publish_on": "2028-05-29 21:00",
        "body": [
            "Eight months into the filing room project, the boxes of real property records had been moved, "
            "but only a third had been indexed. The weekly meeting had gone from lively to quiet. Two of the "
            "four team members came late. The revenue officer heard one of them say, on the way out, that "
            "the project would “never end.”",
            "Nothing had gone badly wrong. The work was simply long, repetitive and mostly invisible. Each "
            "week looked like the week before.",
            "(The office, the project and the people are invented, continuing the treasury examples of this "
            "series. The research quoted below comes from Teresa Amabile and Steven Kramer, authors of the "
            "2011 book The Progress Principle, as quoted in an interview published by the American "
            "Management Association.)",
            "Part 49 looked for failure before it happened. This part looks at a quieter risk: a team that "
            "slowly runs out of energy. By the last section, you will know why the middle of a project is "
            "the hardest stretch, what research says matters most to people’s daily motivation, how to make "
            "progress visible, how to handle setbacks, how to guard against overload, and how to recognize "
            "good work in a government office.",
            ("photo", "blog/pm-team-morale.jpg", "Keeping a team going: make progress visible, clear small "
             "obstacles, treat setbacks as lessons, and recognize the work. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "Why the Middle Is Hardest"),
            ("point", "The start has energy", "A new project has a kickoff, a clear purpose and attention "
             "from the sponsor, as Part 7 described."),
            ("point", "The finish has a deadline", "The last weeks bring urgency and a visible end."),
            ("point", "The middle has neither", "The work repeats, the sponsor’s attention moves elsewhere, "
             "and the end is too far to feel."),
            ("point", "Regular duties compete", "Many treasury project members also carry counter work, so "
             "the project can start to feel like an extra burden."),
            "None of this means the team is lazy. It means the lead has to supply what the calendar does "
            "not: a sense that the work is moving.",
            ("h", "What Research Says Matters Most"),
            "Amabile and Kramer studied “nearly 12,000” daily diary entries “from 238 people working on 26 "
            "creative teams in seven companies.” They found that “the single most important contributor to "
            "positive inner work life was simply making progress on meaningful work.” They called this the "
            "progress principle.",
            ("point", "Catalysts", "Actions that directly support the work, such as clear goals and enough "
             "resources."),
            ("point", "Nourishers", "In their words, “the human connections at work that provide people with "
             "emotional support and encouragement.”"),
            ("point", "Setbacks", "The best leaders they studied “did not punish people for setbacks.” They "
             "asked what could be learned."),
            "The study was of creative teams in companies, not local governments. The idea still applies to a "
            "treasury team indexing records: people work better when they can see that today moved the work "
            "forward.",
            ("h", "Make Progress Visible"),
            ("point", "Break the work into small, countable pieces", "Not “index the records” but “index "
             "barangay 4,” a piece that can be finished in a week."),
            ("point", "Show the count", "A simple chart on the wall: boxes indexed, by week. A rising line "
             "is easier to feel than a percentage in a report."),
            ("point", "Mark milestones out loud", "When half the boxes are done, say so in the meeting, and "
             "tell the sponsor."),
            ("point", "Connect the work to its purpose", "Share the first time a taxpayer’s record was found "
             "in two minutes instead of two days."),
            ("photo", "blog/pm-team-morale-chart.jpg", "Making progress visible: boxes indexed each week, "
             "with a milestone marked when half were done. The figures are invented. (Illustration: Butch "
             "Mahinay, aumahinay.dev)", "medium"),
            ("h", "Remove the Small Obstacles"),
            "Big problems get attention. Small, daily ones wear people down quietly.",
            ("point", "Ask what slowed them down this week", "A missing ladder, a broken scanner, a shared "
             "computer that is always taken."),
            ("point", "Fix one thing quickly", "A small fix within days shows that raising problems is worth "
             "it."),
            ("point", "Protect project time", "If counter duty keeps pulling people away, agree on set "
             "project hours with their supervisor, as Part 18 suggested for workloads."),
            ("h", "Handle Setbacks Without Blame"),
            "Every long project has bad weeks: a lost box, a wrong label, a batch that must be redone.",
            ("point", "Ask what happened, not who", "Focus on the step that failed and how to change it."),
            ("point", "Turn the fix into a small win", "“We found the mislabeled boxes and added a check. "
             "None since.”"),
            ("point", "Use the retrospective", "Part 40’s regular retrospectives are a natural place to talk "
             "about setbacks calmly."),
            ("h", "Watch for Overload"),
            "Tiredness looks like low morale but needs a different fix.",
            ("point", "Look at the hours", "If the same two people carry most of the work, spread it, as "
             "Part 45 described for delegation."),
            ("point", "Watch the signs", "Missed meetings, short answers, mistakes from people who rarely "
             "make them."),
            ("point", "Plan breaks around peak season", "Do not schedule heavy project work during the "
             "January rush at the counter."),
            ("point", "Ask privately", "A five-minute talk often reveals what a meeting will not."),
            ("h", "Recognize the Work, Within the Rules"),
            "Government offices have rules on gifts, awards and spending, so recognition has to fit them. "
            "Some of the most valued recognition costs nothing.",
            ("point", "Say it specifically", "“Your index for barangay 4 had no errors when we checked it” "
             "means more than “good job.”"),
            ("point", "Say it in front of the sponsor", "Name the person when progress is reported upward."),
            ("point", "Put it in writing", "A short memo or note in the person’s file, if office practice "
             "allows, can count at performance review time."),
            ("point", "Use formal channels", "Many offices have an awards and recognition program. Nominate "
             "people when the work deserves it."),
            ("h", "Keep the Sponsor in the Story"),
            "A sponsor who stops asking about a project sends a message, even without meaning to. The team "
            "reads silence as a sign that the work no longer matters.",
            ("point", "Send a short update", "Two or three lines every two weeks, with one number that "
             "moved, using the status report format from Part 25."),
            ("point", "Invite a visit", "Ten minutes in the filing room says more than a page of figures."),
            ("point", "Ask for one specific thing", "A decision, a signature or a word at the staff meeting. "
             "Sponsors respond better to a clear request than to a general plea for support."),
            ("point", "Share the sponsor’s reply", "When the sponsor says something encouraging, pass it on to "
             "the team in their words."),
            "The sponsor does not need to manage the project. A small, regular sign of attention is often "
            "enough to remind the team that someone above them is watching the work and values it.",
            ("h", "Back to the Filing Room"),
            "The revenue officer broke the remaining work into one barangay a week and put a chart on the "
            "wall. At the next meeting, she asked each member what had slowed them down. Two answers took a "
            "day to fix: a second step ladder and a fixed time for the shared scanner.",
            "When the chart passed the halfway mark, she told the sponsor, who walked down to the filing room "
            "to see it. Attendance at the weekly meeting returned to full, and the indexing finished three "
            "weeks earlier than the revised plan.",
            ("h", "Mistakes to Avoid"),
            ("point", "Waiting for the finish to celebrate", "Mark progress along the way."),
            ("point", "Ignoring small obstacles", "They drain energy every day."),
            ("point", "Blaming people for setbacks", "Fix the step, not the person."),
            ("point", "Mistaking overload for low morale", "Check the hours before giving a pep talk."),
            ("h", "Quick Recap"),
            ("point", "Progress matters most", "Help people see that the work moved today."),
            ("point", "Clear the small obstacles", "Ask weekly, fix quickly."),
            ("point", "Setbacks are lessons", "Ask what happened and turn the fix into a win."),
            ("point", "Recognize specifically", "In person, in front of the sponsor, and in writing."),
            ("h", "Your Part 50 Action Plan"),
            ("point", "This week", "Break the current work into pieces that can be finished in a week, and "
             "start a progress chart."),
            ("point", "At the next meeting", "Ask each person what slowed them down, and fix one thing within "
             "three days."),
            ("point", "This month", "Name one person’s specific contribution when you report to the sponsor."),
            ("cta", "Read: Project Management Series, Part 45: Delegating Work Without Losing Track of It", "/blog/project-management-part-45-delegating-work/"),
            ("cta", "Read: Project Management Series, Part 18: Assigning People Without Overloading Them", "/blog/project-management-part-18-resource-allocation/"),
            ("cta", "Read: Project Management Series, Part 40: The Retrospective, Improving While the Work Is Still Running", "/blog/project-management-part-40-retrospectives/"),
            ("cta", "Read: Project Management Series, Part 38: When the Team Disagrees, Five Ways to Handle Conflict", "/blog/project-management-part-38-handling-conflict/"),
            ("ask", "What is one small obstacle your team has stopped mentioning because nobody fixed it?"),
        ],
    },
    {
        "title": "Project Management Series, Part 49: The Pre-Mortem, Imagining Failure Before It Happens",
        "slug": "project-management-part-49-pre-mortem",
        "category": "pm",
        "date": "May 24, 2028",
        "summary": "A post-mortem explains why a project failed after it is too late to help. A pre-mortem asks "
                   "the team to imagine the failure first, while the plan can still change. This part shows how "
                   "to run one in under an hour, how to turn its list into actions, and why it helps quiet "
                   "team members speak up.",
        "publish_on": "2028-05-24 21:00",
        "body": [
            "The plan to extend text reminders to real property owners looked ready. The phone list had been "
            "cleaned, the message was drafted, and the sponsor had approved a start date in August. At the "
            "last planning meeting, the revenue officer asked whether anyone had concerns. Nobody did.",
            "Two weeks after launch, the treasury counter was crowded with owners holding reminders for "
            "taxes they had already paid. One of the clerks said later that she had wondered about it. The "
            "payment records were updated only every Friday, so a reminder sent on Wednesday could miss "
            "three days of payments. She had not wanted to slow things down by saying so.",
            "(The office, the project and the people are invented, continuing the treasury examples of this "
            "series. The method and the research quoted below come from Gary Klein’s article “Performing a "
            "Project Premortem,” published in Harvard Business Review in September 2007.)",
            "Part 48 kept a record of why decisions were made. This part looks forward instead. When you "
            "finish reading, you will know what a pre-mortem is, why it surfaces risks that ordinary "
            "planning meetings miss, how to run one step by step, how to turn its results into changes to "
            "the plan, and when it is worth the time.",
            ("photo", "blog/pm-pre-mortem.jpg", "The pre-mortem: imagine the project has already failed, list "
             "the reasons, and fix the plan while there is still time. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "What a Pre-Mortem Is"),
            "Klein, a psychologist who studies how people make decisions, calls the pre-mortem “the "
            "hypothetical opposite of a postmortem.” A post-mortem asks why something failed after the fact. "
            "A pre-mortem asks the same question before work begins, by imagining that the failure has "
            "already happened.",
            "The difference sounds small. It changes the conversation. “What could go wrong?” invites people "
            "to defend the plan. “It failed. Why?” invites them to explain a failure, and people are often "
            "better at that.",
            ("point", "The research behind it", "Klein cites a 1989 study by Deborah Mitchell, Jay Russo and "
             "Nancy Pennington, which found that imagining an event has already happened “increases the "
             "ability to correctly identify reasons for future outcomes by 30%.”"),
            ("point", "Safe to dissent", "Klein writes that the method works by “making it safe for "
             "dissenters who are knowledgeable about the undertaking” to voice their concerns."),
            ("point", "Not a risk register replacement", "It feeds the risk register from Part 19 with "
             "risks that might not otherwise come up."),
            ("h", "Why Ordinary Planning Meetings Miss Things"),
            ("point", "Momentum", "Once a plan has a date and a sponsor’s approval, questioning it can feel "
             "like disloyalty."),
            ("point", "Rank", "Junior staff may hesitate to contradict the lead in front of others."),
            ("point", "The question itself", "“Any concerns?” at the end of a long meeting is easy to answer "
             "with silence."),
            ("point", "Front-line knowledge", "The people who know where things break, such as counter staff, "
             "are often not the ones presenting the plan."),
            ("h", "How to Run a Pre-Mortem in Under an Hour"),
            "Klein describes the steps. Adapted for a treasury project, they look like this.",
            ("point", "1. Gather the right people (5 minutes)", "The core team, plus one or two people who "
             "will live with the result, such as a counter clerk. Make sure everyone knows the plan."),
            ("point", "2. Declare the failure (2 minutes)", "“Imagine it is three months after launch. The "
             "project has failed badly. Taxpayers are complaining, and the sponsor wants to stop it.”"),
            ("point", "3. Write reasons alone (10 minutes)", "Each person writes every reason they can think "
             "of, without talking. Writing alone keeps the first idea spoken from steering the rest."),
            ("point", "4. Share one at a time (15 minutes)", "Go around the table. Each person reads one "
             "reason, then the next person, until every reason is on the board. Klein suggests the project "
             "manager starts."),
            ("point", "5. Pick the ones that matter (10 minutes)", "Mark each reason for how likely it is and "
             "how much damage it would do, as in Part 19."),
            ("point", "6. Change the plan (15 minutes)", "For the top few, decide what to do: change a step, "
             "add a check, assign an owner or accept the risk knowingly."),
            ("photo", "blog/pm-pre-mortem-steps.jpg", "Six steps of a pre-mortem, in under an hour: gather, "
             "declare the failure, write alone, share one at a time, rank, and change the plan. The timings "
             "are a guide. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Turning the List Into Action"),
            "A pre-mortem that ends with a list on a whiteboard has done half its job. Every serious reason "
            "should leave the room as a change, a task or a conscious decision.",
            ("point", "Change the plan", "If the reason is a gap in the plan, fix the plan. “Payments are "
             "updated weekly” becomes “update payments daily before any reminder is sent.”"),
            ("point", "Add a check", "If the risk cannot be removed, add an early warning. “Count complaints "
             "at the counter in the first week.”"),
            ("point", "Name an owner", "Each action gets one person and a date, recorded in the issue log "
             "from Part 26."),
            ("point", "Record what you accept", "Some risks are worth taking. Write them in the decision log "
             "from Part 48 with the reason."),
            ("h", "Back to the Reminders"),
            "After the complaints, the revenue officer paused the reminders and ran a pre-mortem on the "
            "relaunch. She asked the team to imagine that the relaunch had also failed.",
            "The list took twenty minutes and filled the whiteboard. The clerk’s point about weekly updates "
            "came first, from the clerk herself, now that she had been asked directly. Others followed: some "
            "owners had sold their property and the numbers belonged to the new owners’ relatives; the "
            "message did not say what to do if the tax was already paid; and the counter had not been told "
            "when the reminders would go out.",
            "The team changed four things. Payments were updated every morning before reminders went out. "
            "The message added one line: “If you have already paid, please ignore this message.” Numbers on "
            "properties transferred in the last year were checked first. The counter received the schedule a "
            "week ahead. The relaunch drew few complaints.",
            ("h", "When a Pre-Mortem Is Worth the Time"),
            ("point", "Before a launch", "A new system, a new process, or anything taxpayers will see."),
            ("point", "Before a big commitment", "Signing a contract, buying equipment or changing a deadline "
             "in an ordinance."),
            ("point", "When the plan feels too smooth", "If nobody has raised a concern, that can be a "
             "reason to ask in a different way."),
            ("point", "Not for small routine tasks", "A weekly report does not need one."),
            ("h", "Mistakes to Avoid"),
            ("point", "Skipping the silent writing", "Without it, the first loud voice sets the list."),
            ("point", "Leaving out the front line", "Invite at least one person who will use the result."),
            ("point", "Defending the plan during sharing", "Record each reason without arguing. Discuss "
             "later."),
            ("point", "No actions afterward", "Every serious reason needs a change, a check or a recorded "
             "decision."),
            ("h", "Quick Recap"),
            ("point", "Imagine the failure", "“It failed. Why?” surfaces more than “What could go wrong?”"),
            ("point", "Write alone, share in turn", "So every person’s reasons reach the board."),
            ("point", "Rank and act", "Change the plan, add a check, name an owner, or accept knowingly."),
            ("point", "Make it safe to doubt", "The person with the key worry may be the quietest one."),
            ("h", "Your Part 49 Action Plan"),
            ("point", "Before your next launch", "Book 45 minutes for a pre-mortem with the team and one "
             "front-line user."),
            ("point", "During it", "Keep the silent writing to ten minutes, and share one reason at a time."),
            ("point", "Within a day", "Turn the top reasons into tasks, checks or decision log entries."),
            ("cta", "Read: Project Management Series, Part 48: The Decision Log, Remembering Why the Project Chose What It Chose", "/blog/project-management-part-48-decision-log/"),
            ("cta", "Read: Project Management Series, Part 19: The Risk Register, Planning for What Could Go Wrong", "/blog/project-management-part-19-risk-register/"),
            ("cta", "Read: Project Management Series, Part 40: The Retrospective, Improving While the Work Is Still Running", "/blog/project-management-part-40-retrospectives/"),
            ("cta", "Read: Project Management Series, Part 26: The Issue Log, Turning Problems Into Next Steps", "/blog/project-management-part-26-issue-log/"),
            ("ask", "What would your team write down if you asked them today why your current project failed?"),
        ],
    },
    {
        "title": "Project Management Series, Part 48: The Decision Log, Remembering Why the Project Chose What It Chose",
        "slug": "project-management-part-48-decision-log",
        "category": "pm",
        "date": "May 19, 2028",
        "summary": "Months into a project, someone asks why it was done this way, and often nobody remembers. A "
                   "decision log keeps one short record per important choice: the context, the options, the "
                   "decision, who made it and what follows. This part shows what to record, when, and how to "
                   "change a decision without erasing the old one.",
        "publish_on": "2028-05-19 21:00",
        "body": [
            "In March, the new treasurer asked why the text reminders went out only to business taxpayers and "
            "not to real property owners. It looked like an obvious gap.",
            "The project lead remembered that there had been a reason, discussed at a meeting the year before. "
            "She could not remember what it was. The minutes said only: “Agreed to start with business tax.” "
            "The team spent two weeks rediscovering the reason: the real property owner list had too many "
            "missing and outdated phone numbers to use safely, and cleaning it had been planned for a later "
            "phase.",
            "(The office, the project and the people are invented, continuing the treasury examples of this "
            "series. The format described below draws on the architecture decision record, a practice from "
            "software teams.)",
            "Part 47 negotiated with other offices. This part looks at what a project should remember about its "
            "own choices. Stay with me to the end, and you will know what a decision log is, which decisions "
            "belong in it, what to write for each, how to change a decision without erasing the old one, and "
            "how to keep the log small enough that people actually use it.",
            ("photo", "blog/pm-decision-log.jpg", "A decision log: one short entry per important choice, with "
             "the context, the options considered, the decision, who made it and what follows. (Illustration: "
             "Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Where the Idea Comes From"),
            "Software teams have kept records like this for years. Martin Fowler, a well-known writer on "
            "software design, describes an architecture decision record as “a short document that captures and "
            "explains a single decision.” He credits Michael Nygard with coining the term in a 2011 article, "
            "and notes that Nygard “did not originate the idea of a decision log.”",
            "The idea works well outside software. Any project that makes choices other people will later "
            "question can use it.",
            ("point", "Minutes record that something was decided", "Part 27’s minutes capture the decision and "
             "the action items."),
            ("point", "A decision log records why", "The context and the options that lost, which minutes "
             "rarely have room for."),
            ("point", "The issue log records problems", "Part 26’s log tracks problems to fix. Some issues end "
             "in a decision, which then gets its own entry."),
            ("h", "Which Decisions Belong in the Log"),
            "Not every choice needs an entry. A log with 200 entries is as hard to use as none.",
            ("point", "Hard to reverse", "Choosing a supplier, a system, or which taxpayers come first."),
            ("point", "Likely to be questioned", "Anything a new sponsor, an auditor or the council may ask "
             "about later."),
            ("point", "Trading one goal against another", "Speed against completeness, cost against quality."),
            ("point", "Changes to the charter or plan", "Approved changes from Part 24’s change control."),
            "A useful test: if someone asked about this choice a year from now, would the team need more than "
            "one sentence to explain it? If yes, log it.",
            ("h", "What to Write for Each Decision"),
            "Fowler says a record should contain “the decision, the context for making it, and significant "
            "ramifications.” For a treasury project, six short fields are enough.",
            ("point", "Number and date", "D-07, April 2."),
            ("point", "Context", "What problem needed a choice, and what was true at the time. “Only 58 percent "
             "of real property owners have a usable phone number on file.”"),
            ("point", "Options considered", "Including the ones not chosen. “Start with both groups. Start with "
             "business tax only. Delay until both lists are clean.”"),
            ("point", "Decision and reason", "“Start with business tax, where 91 percent of numbers are usable. "
             "Clean the real property list in phase 2.”"),
            ("point", "Who decided", "The sponsor, the project lead or the team, and who was consulted."),
            ("point", "Consequences and review", "What follows from it, and what would make the team look again. "
             "“Revisit when the real property list reaches 85 percent usable numbers.”"),
            "Most entries fit in half a page. Write them within a day of the decision, while the reasons are "
            "fresh.",
            ("photo", "blog/pm-decision-log-entry.jpg", "One decision log entry: context, options, decision, who "
             "decided and when to review it. A later entry can supersede it, while the original stays in the "
             "log. The entry is invented. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Changing a Decision Without Erasing It"),
            "Decisions change. The temptation is to edit the old entry. Fowler advises against it: once accepted, a record “should never be reopened or changed.” Instead, he writes, it “should be superseded.”",
            ("point", "Write a new entry", "D-15: Extend reminders to real property owners. Give its own "
             "context and reason."),
            ("point", "Link the two", "Mark D-07 as “superseded by D-15,” and have D-15 refer back to D-07."),
            ("point", "Keep the old one", "The history shows the project learned, not that it was wrong."),
            "This matters for audits. A record that shows the reasoning at the time, and when and why it "
            "changed, is easier to defend than a single entry rewritten after the fact.",
            ("h", "Keeping the Log Alive"),
            ("point", "One place", "A single sheet or document in the project folder, next to the issue log."),
            ("point", "One owner", "The project lead, or a team member named to keep it current."),
            ("point", "A standing agenda item", "At each weekly or Friday review, ask: did we decide anything "
             "worth logging?"),
            ("point", "Read it when people join", "Part 46’s new member learns more from ten decision entries "
             "than from a hundred old emails."),
            ("point", "Hand it over at closing", "Part 28’s handover should include the log, so the office that "
             "runs the result knows why it was built this way."),
            ("h", "Who Reads the Log"),
            "A decision log earns its keep when someone outside the team needs an answer quickly.",
            ("point", "A new sponsor or official", "After an election or a transfer, the people who approved the "
             "early choices may be gone. The log explains them."),
            ("point", "Auditors", "Part 9 of Inside the Local Treasury described how audit questions can arrive "
             "months later. A dated entry with its reasons is a ready answer."),
            ("point", "The team itself", "When a decision is questioned in a meeting, the log settles what was "
             "known at the time, so the discussion moves to whether the facts have changed."),
            ("point", "The next project", "Part 30’s project kit can include the log as an example, so the "
             "next team starts with the habit."),
            ("h", "Back to the Treasurer’s Question"),
            "After the two lost weeks, the project lead started a decision log. Among her first entries, written "
            "from the rediscovered facts, was D-07: the choice to start with business tax, with 85 percent usable "
            "numbers on the real property list as the condition for revisiting it.",
            "When the list cleanup reached that level in May, the team wrote a new entry extending the "
            "reminders and marked the old one as superseded. When the new treasurer asked a follow-up question "
            "in June, the answer took two minutes.",
            ("h", "Mistakes to Avoid"),
            ("point", "Logging everything", "Keep it to choices that are hard to reverse or likely to be "
             "questioned."),
            ("point", "Recording only the winner", "Write down the options that lost and why."),
            ("point", "Editing old entries", "Supersede them with a new entry and link the two."),
            ("point", "Writing weeks later", "Record the decision within a day, while the reasons are fresh."),
            ("h", "Quick Recap"),
            ("point", "Minutes say what, the log says why", "Context, options, decision and consequences."),
            ("point", "Log what will be questioned", "Hard-to-reverse choices and trade-offs."),
            ("point", "Supersede, do not edit", "Keep the history of how thinking changed."),
            ("point", "Use it", "For new members, audits, sponsors and the handover."),
            ("h", "Your Part 48 Action Plan"),
            ("point", "Today", "Start a decision log with six columns in your project folder."),
            ("point", "This week", "Write entries for the three most important decisions already made, while "
             "people still remember why."),
            ("point", "Every Friday", "Ask the team whether anything decided that week belongs in the log."),
            ("cta", "Read: Project Management Series, Part 27: Meetings That Decide, Agendas, Minutes and Action Items", "/blog/project-management-part-27-meetings-that-decide/"),
            ("cta", "Read: Project Management Series, Part 26: The Issue Log, Turning Problems Into Next Steps", "/blog/project-management-part-26-issue-log/"),
            ("cta", "Read: Project Management Series, Part 24: Change Control, Saying Yes to a Change Without Losing the Plan", "/blog/project-management-part-24-change-control/"),
            ("cta", "Read: Project Management Series, Part 28: Closing the Project, Handover and Lessons Learned", "/blog/project-management-part-28-closing-the-project/"),
            ("ask", "Which decision in your current project would nobody be able to explain a year from now?"),
        ],
    },
    {
        "title": "Project Management Series, Part 47: Negotiating With Other Offices for People, Equipment and Time",
        "slug": "project-management-part-47-negotiating-with-other-offices",
        "category": "pm",
        "date": "May 15, 2028",
        "summary": "Many treasury projects need people, rooms or equipment that belong to another office. This "
                   "part uses the four principles of principled negotiation to prepare for the conversation, "
                   "find what the other office needs, offer options both sides can accept, and write the "
                   "agreement down.",
        "publish_on": "2028-05-15 21:00",
        "body": [
            "The filing room project needed two things it did not own: the general services office’s pickup "
            "truck for one Saturday, to move 140 boxes of real property records, and two days of help from the "
            "assessor’s records clerk, who knew where every folder belonged.",
            "The revenue officer sent a memo asking for both. The general services chief replied that the truck "
            "was fully booked. The assessor said the clerk could not be spared. The project stopped for two "
            "weeks while each side waited for the other to give in.",
            "(The offices, the people and the dates are invented, continuing the treasury examples of this "
            "series. The principles quoted below come from Getting to Yes, by Roger Fisher, William Ury and "
            "Bruce Patton of the Harvard Negotiation Project.)",
            "Part 46 brought a new person into a project. This part is about borrowing from people who do not "
            "report to you. When you finish reading, you will know why a request often meets a quick no, how to "
            "prepare for a negotiation inside your own local government, how to find what the other office "
            "needs, how to offer options instead of one demand, and how to record what was agreed.",
            ("photo", "blog/pm-negotiation.jpg", "Negotiating with another office: separate the people from the "
             "problem, focus on interests, offer several options, and use fair standards. (Illustration: Butch "
             "Mahinay, aumahinay.dev)", "medium"),
            ("h", "Why the First Answer Is Often No"),
            ("point", "Your project is not their priority", "Each office has its own deadlines and its own head "
             "to answer to."),
            ("point", "A memo invites a position", "“Please lend us the truck on June 26” can only be answered "
             "yes or no. No is safer."),
            ("point", "Hidden costs", "Lending the clerk means the assessor’s counter is short. The request did "
             "not say who would cover that."),
            "A quick no is often an opening position, not a final answer. The way forward is a conversation "
            "about what each side actually needs.",
            ("h", "Four Principles From Getting to Yes"),
            "The book sets out four principles of what it calls principled negotiation. They work as well "
            "between two offices of the same local government as between companies.",
            ("point", "“Separate the People from the Problem”", "The general services chief is not the obstacle. "
             "The fully booked truck is. Talk about the schedule, not about whether the chief is helpful."),
            ("point", "“Focus on Interests, Not Positions”", "“The truck is booked” is a position. The interest "
             "behind it may be that the truck is needed for a market cleanup every Saturday morning."),
            ("point", "“Invent Options for Mutual Gain”", "Saturday afternoon instead of morning. A Sunday with "
             "the driver’s overtime paid from the project budget. Two trips on weekday evenings."),
            ("point", "“Insist on Using Objective Criteria”", "Use fair standards both sides can accept: the vehicle "
             "request rules, the actual booking log, the cost of fuel and overtime."),
            "The book also offers a useful idea for preparation: your BATNA, short for “Best Alternative to a "
            "Negotiated Agreement.” It is what you will do if no agreement is reached.",
            ("h", "Step 1: Prepare Before You Ask"),
            ("point", "Know your own interests", "What do you really need? For the filing room, the need was "
             "140 boxes moved safely within the month, not that particular truck on that particular day."),
            ("point", "Guess their interests", "What does the other office worry about? Its own deadlines, its "
             "staff, its budget, and being blamed if something goes wrong."),
            ("point", "Know your BATNA", "If general services says no, could you rent a truck? At what cost? "
             "Knowing that keeps you calm and realistic."),
            ("point", "Bring the facts", "Dates, hours needed, costs, and who will cover them. Part 17’s budget "
             "may already hold money for such costs."),
            ("h", "Step 2: Talk, Do Not Only Write"),
            "A memo is good for recording an agreement. It is a poor way to reach one. Ask for 15 minutes in "
            "person.",
            ("point", "Start with their situation", "“How is the truck schedule this month?” Listen before "
             "asking."),
            ("point", "Explain the project briefly", "Why the filing room matters: records that taxpayers and "
             "the assessor’s own staff will find faster."),
            ("point", "Ask about constraints", "“What would make it possible?” is better than “Can you or can’t "
             "you?”"),
            ("photo", "blog/pm-negotiation-options.jpg", "From one demand to several options: each one checked "
             "against what both offices need. The options are invented. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "Step 3: Offer Options, Then Choose Together"),
            "Bring two or three possible arrangements, and invite theirs.",
            ("point", "Timing", "Use the truck when it is free, even if that is less convenient for you."),
            ("point", "Cost", "Offer to cover fuel or overtime from the project budget."),
            ("point", "Exchange", "Offer something the other office values, such as treasury help with its own "
             "collections report."),
            ("point", "Smaller ask", "One day of the clerk instead of two, with a treasury clerk shadowing to "
             "learn the folder system."),
            "Check each option against both sides’ interests. The best option is often one neither side "
            "proposed at first.",
            ("h", "Step 4: Write It Down"),
            "Once you agree, send a short note the same day.",
            ("point", "What was agreed", "The truck and driver, Saturday June 26, 1:00 to 5:00 p.m."),
            ("point", "Who covers what", "Fuel and the driver’s overtime from the project budget."),
            ("point", "What happens if plans change", "Notice by Wednesday of the same week."),
            ("point", "Copy the right people", "The sponsor, and anyone who must approve under office rules."),
            "If the agreement needs approval from the local chief executive or a department head, get it in "
            "writing. Part 27 covered minutes that record decisions.",
            ("h", "When You Cannot Agree"),
            ("point", "Use your BATNA", "Rent the truck, if the budget allows and the rules permit."),
            ("point", "Escalate with options, not complaints", "Take the matter to the person above both offices, "
             "with the options already discussed, as Part 44 advised for conflicts between projects."),
            ("point", "Keep the relationship", "You will need the same office again next quarter."),
            ("h", "Back to the Filing Room"),
            "The revenue officer asked for 15 minutes with the general services chief. The truck was booked for "
            "the Saturday market cleanup, which ended at noon. They agreed on Saturday afternoon, with fuel and "
            "overtime paid from the project budget.",
            "With the assessor, she learned the real worry: the clerk ran the records counter alone on Mondays "
            "and Tuesdays. They agreed on Wednesday and Thursday, with a treasury clerk shadowing so the "
            "assessor’s office would also gain a second person who knew the filing system. The boxes moved two "
            "weeks later than first planned, but the project was moving again.",
            ("h", "Inside One Local Government"),
            "Negotiating with a sister office is different from bargaining with a supplier. Both offices serve "
            "the same public and answer to the same chief executive.",
            ("point", "Shared goals help", "Point to what the local government as a whole gains, not only your "
             "project."),
            ("point", "Rules still apply", "Lending vehicles, staff or rooms usually follows office rules. Check "
             "them before offering anything."),
            ("point", "Return the favor", "Help the other office when it asks. Goodwill is built before it is "
             "needed."),
            ("h", "Mistakes to Avoid"),
            ("point", "Asking by memo only", "Talk first, then write down the agreement."),
            ("point", "Arguing positions", "Ask about the interests behind them."),
            ("point", "One demand, no options", "Bring two or three arrangements."),
            ("point", "No written record", "Send a short note the same day."),
            ("h", "Quick Recap"),
            ("point", "Four principles", "People apart from the problem, interests over positions, options, "
             "fair standards."),
            ("point", "Know your BATNA", "Your best alternative if no agreement is reached."),
            ("point", "Talk, then write", "Agree in person, record it the same day."),
            ("point", "Protect the relationship", "Other offices are partners in the next project too."),
            ("h", "Your Part 47 Action Plan"),
            ("point", "Before your next request", "Write your interest, their likely interest and your BATNA "
             "on one page."),
            ("point", "At the meeting", "Bring three options and ask what would make it possible."),
            ("point", "After the meeting", "Send a short note of what was agreed."),
            ("cta", "Read: Project Management Series, Part 3: Mapping Who Holds the Power", "/blog/project-management-part-3-stakeholder-mapping/"),
            ("cta", "Read: Project Management Series, Part 38: When the Team Disagrees, Five Ways to Handle Conflict", "/blog/project-management-part-38-handling-conflict/"),
            ("cta", "Read: Project Management Series, Part 44: Leading Several Projects at Once Without Dropping Any", "/blog/project-management-part-44-several-projects-at-once/"),
            ("cta", "Read: Project Management Series, Part 27: Meetings That Decide, Agendas, Minutes and Action Items", "/blog/project-management-part-27-meetings-that-decide/"),
            ("ask", "What do you most often need to borrow from another office, and how do you usually ask?"),
        ],
    },
    {
        "title": "Project Management Series, Part 46: Bringing a New Person Into a Running Project",
        "slug": "project-management-part-46-new-team-member",
        "category": "pm",
        "date": "May 10, 2028",
        "summary": "A new team member halfway through a project can speed it up or slow it down for weeks. This "
                   "part shows how to prepare before the person arrives, what to cover in the first day and the "
                   "first two weeks, how to pick a first task, and why adding people to a late project needs "
                   "care.",
        "publish_on": "2028-05-10 21:00",
        "body": [
            "The online payment project from Part 43 had recovered, and the department head sent help: a "
            "young programmer transferred from the assessor’s office, starting Monday.",
            "On Monday, nobody had prepared a desk, a login or a task. The project lead spent the morning "
            "explaining the project from memory, between phone calls. By Wednesday, the new programmer was "
            "reading old emails to understand why the system worked the way it did. By the end of the second "
            "week, the team was slower than before, because the two senior members kept stopping to answer "
            "questions.",
            "(The office, the project and the people are invented, continuing the treasury examples of this "
            "series. The law quoted below comes from Fred Brooks’s 1975 book The Mythical Man-Month.)",
            "Part 45 handed work to people already on the team. This part looks at a person who is new to it. "
            "By the last section, you will know why a new member can slow a project down at first, how to "
            "prepare before the first day, what to cover in the first day and the first two weeks, how to "
            "choose a good first task, and how to tell when the person is fully up to speed.",
            ("photo", "blog/pm-new-member.jpg", "Bringing someone into a running project: prepare before they "
             "arrive, give one guide, start with a small real task, and check in on a set schedule. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Why a New Member Can Slow Things Down at First"),
            "Fred Brooks, who managed a large software project at IBM in the 1960s, put it bluntly in The "
            "Mythical Man-Month: “adding manpower to a late software project makes it later.” The idea is now "
            "often called Brooks’s law. It is a warning about timing and setup, not a rule against adding "
            "people.",
            ("point", "Learning takes time", "The new person needs days or weeks to understand the work before "
             "they add to it."),
            ("point", "Teaching takes time too", "Someone on the team has to explain things, and that person’s "
             "own work slows while they do."),
            ("point", "More people, more conversations", "Each new member adds new pairs of people who need to "
             "keep each other informed."),
            "None of this means a project should refuse help. It means the help should arrive early enough, and "
            "be prepared well enough, that the slowdown is short.",
            ("h", "Before the First Day"),
            "Most of the slowdown can be cut before the person walks in.",
            ("point", "Access ready", "Desk, computer, logins to the shared folder, the test system and the "
             "group chat, requested at least a week ahead."),
            ("point", "One guide, not fifty emails", "A short document with the charter from Part 2, the current "
             "plan, the status report from Part 25 and a list of who does what."),
            ("point", "A named buddy", "One team member who answers questions for the first two weeks. Lighten "
             "that person’s own tasks a little to make room."),
            ("point", "A first task chosen", "See the section below. Waiting for something to do is the worst "
             "start."),
            ("point", "Tell the team", "Who is coming, when, and what they will work on, so nobody is "
             "surprised."),
            ("h", "The First Day"),
            "Keep the first day short on detail and long on context.",
            ("point", "The why", "What problem the project solves and for whom. Ten minutes with the project lead "
             "is enough."),
            ("point", "The people", "Introduce the team, the sponsor if possible, and the counter staff who will "
             "use the result."),
            ("point", "The rules of the road", "When the team meets, where files live, how decisions are "
             "recorded, and how to raise a problem."),
            ("point", "The first task", "Hand it over before the day ends, with the briefing from Part 45: "
             "result, reason, limits, level and date."),
            ("photo", "blog/pm-new-member-plan.jpg", "A two-week plan for a new team member: context on day one, "
             "a small real task in week one, a larger task in week two, and short check-ins on set days. The "
             "plan is invented. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Choosing the First Task"),
            "A good first task is small, real and close to the center of the work.",
            ("point", "Small", "Something that can be finished in two to three days."),
            ("point", "Real", "It goes into the actual project, not a practice exercise. Finishing real work "
             "builds confidence quickly."),
            ("point", "Close to the center", "It touches the main parts of the system or process, so the person "
             "learns how they fit together."),
            ("point", "Checked by the buddy", "Review the result together and explain anything the person "
             "could not have known."),
            "For the payment project, a good first task would be fixing a small known bug in the receipt "
            "screen. It is small, it matters, and it leads straight into the code the team works on every day.",
            ("h", "The First Two Weeks"),
            ("point", "Check in on set days", "A 15-minute talk on day 2, day 5 and day 10. Ask what is clear, "
             "what is confusing, and what they would change."),
            ("point", "Fresh eyes are useful", "A new person often notices what the team has stopped seeing. "
             "Write down their questions. Some will point to gaps in the documents or the procedure."),
            ("point", "Increase the size of tasks", "Week one, a task of two or three days. Week two, a task of "
             "a week, at a higher level of delegation."),
            ("point", "Update the guide", "Most questions the new person had to ask point to a line the guide was missing."),
            ("h", "When Is the Person Up to Speed?"),
            "There is no fixed number of days. Look for signs instead.",
            ("point", "They estimate their own tasks", "And the estimates are close to what actually happens."),
            ("point", "They answer questions", "Other members start asking them."),
            ("point", "They spot problems early", "They raise risks before being asked."),
            "When these signs appear, end the buddy arrangement and treat the person like any other member.",
            ("h", "Back to the Programmer"),
            "The project lead started again on the third week. He wrote a four-page guide in an afternoon, "
            "named one senior member as the buddy, and gave the programmer the receipt screen bug, with a "
            "check-in on day 2.",
            "The fix was done in three days. In the second week, the programmer took on the payment history "
            "page that had been moved to phase 2 in Part 43. By the end of the month, the team was completing "
            "more work each week than before he arrived, and his questions had added nine lines to the guide.",
            ("h", "When a Member Leaves Instead"),
            "The same guide helps in the opposite case. When someone leaves the project, a guide that already "
            "exists makes the handover faster.",
            ("point", "Ask the leaver to update it", "In their last week, the person adds what only they know."),
            ("point", "Pair before they go", "The person who will take over sits with the leaver for a few "
             "days, as Part 31 suggested for absences."),
            ("point", "Move their open items", "Every open item in the issue log gets a new owner before the "
             "last day."),
            ("h", "Mistakes to Avoid"),
            ("point", "No access on day one", "Request logins and equipment a week ahead."),
            ("point", "Explaining everything from memory", "Write one short guide and keep it current."),
            ("point", "Practice tasks only", "Give a small real task in the first days."),
            ("point", "Adding people too late", "Help that arrives in the last weeks can slow the finish."),
            ("h", "Quick Recap"),
            ("point", "Expect a short slowdown", "Learning and teaching both take time."),
            ("point", "Prepare before day one", "Access, one guide, a buddy and a first task."),
            ("point", "Small, real first task", "Checked with the buddy, then larger tasks."),
            ("point", "Watch for the signs", "Own estimates, answering questions, raising risks early."),
            ("h", "Your Part 46 Action Plan"),
            ("point", "Today", "Start a one-page guide for your current project."),
            ("point", "Before the next new member", "Pick a buddy and a first task in advance."),
            ("point", "After two weeks", "Ask the new member what the guide was missing, and add it."),
            ("cta", "Read: Project Management Series, Part 45: Delegating Work Without Losing Track of It", "/blog/project-management-part-45-delegating-work/"),
            ("cta", "Read: Project Management Series, Part 2: The Project Charter on One Page", "/blog/project-management-part-2-project-charter/"),
            ("cta", "Read: Project Management Series, Part 31: Covering for Absences, a Backup Plan So the Work Does Not Stop", "/blog/project-management-part-31-covering-absences/"),
            ("cta", "Read: Project Management Series, Part 26: The Issue Log, Turning Problems Into Next Steps", "/blog/project-management-part-26-issue-log/"),
            ("ask", "What do you wish someone had given you on your first day in a project?"),
        ],
    },
    {
        "title": "Project Management Series, Part 45: Delegating Work Without Losing Track of It",
        "slug": "project-management-part-45-delegating-work",
        "category": "pm",
        "date": "May 5, 2028",
        "summary": "A project lead who does every task alone becomes the bottleneck. This part shows how to choose "
                   "what to hand over, how much authority to give with it, how to brief the person so the result "
                   "comes back right, and how to follow up without hovering or disappearing.",
        "publish_on": "2028-05-05 21:00",
        "body": [
            "The revenue officer had a new rule for herself after Part 44: one page, one order of priority, "
            "protected blocks. It helped. But the page also showed something she had not wanted to see. Of the "
            "52 hours of project work on it, she had written her own name beside 41.",
            "Her two clerks were capable. One had built the stall list spreadsheet from scratch. The other knew "
            "every taxpayer on the reminder list by name. Yet both were waiting for her to tell them what to do "
            "next, and she was staying late doing tasks either of them could have done.",
            "(The office, the people and the hours are invented, continuing the treasury examples of this "
            "series.)",
            "Part 44 put several projects on one page. This part looks at the next step: getting some of that "
            "work off the lead’s desk without losing control of it. When you finish reading, you will know how "
            "to choose what to delegate, how to match the authority to the person, how to brief a task so it "
            "comes back right, how to follow up at the right distance, and what to do when a delegated task "
            "goes wrong.",
            ("photo", "blog/pm-delegation.jpg", "Delegating well: choose the task, set the level of authority, "
             "brief it clearly, and agree on check-in points before letting go. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "Why Leads Hold On"),
            "Most project leads know they should delegate. Many still do not, for reasons that feel sensible in "
            "the moment.",
            ("point", "“It is faster if I do it”", "True for one task, once. False for the tenth time the same "
             "task comes up."),
            ("point", "“They might get it wrong”", "Sometimes they will, the first time. A lead who never lets anyone try keeps that risk and never builds the team’s skill."),
            ("point", "“I do not want to burden them”", "Often the opposite is true. Capable staff who are "
             "given nothing but small errands tend to lose interest."),
            ("point", "“I need to know everything”", "A lead needs to know the status of everything, not to do "
             "everything. Those are different jobs."),
            "Delegation is not dumping. It is a deliberate choice to grow the team’s capacity, with the lead "
            "still answerable for the result.",
            ("h", "Step 1: Choose What to Hand Over"),
            "Go down the one page and mark each task with one of three labels.",
            ("point", "Only I can do this", "Decisions that need your authority, conversations with the "
             "sponsor, and work that depends on information only you hold. Keep these."),
            ("point", "Someone else could do this with a short briefing", "Data gathering, drafting, updating "
             "the issue log, preparing a schedule, following up with suppliers. These are the best candidates."),
            ("point", "Someone else could do this better", "The clerk who knows every taxpayer may write a "
             "better reminder message than the lead. Hand these over first."),
            "Repeating tasks are the best place to start. A task that comes up every week pays back the "
            "briefing many times.",
            ("h", "Step 2: Match the Authority to the Person"),
            "The most common delegation failure is a mismatch: the person thinks they may decide, and the lead "
            "thinks they were only asked to look into it. Say the level out loud.",
            ("point", "Level 1: Find out and report", "“Look into why the stall list has 14 duplicates and tell "
             "me what you find.” The lead decides what happens next."),
            ("point", "Level 2: Recommend", "“Find the duplicates and propose which record to keep for each.” "
             "The lead approves before anything changes."),
            ("point", "Level 3: Act, then tell me", "“Clean up the duplicates using the rule we agreed, and send "
             "me the list of changes.” The person decides within the rule."),
            ("point", "Level 4: Act on your own", "“The stall list is yours. Keep it accurate.” The lead hears "
             "about it in the weekly review."),
            "Start a new person at level 1 or 2, and move up as trust grows. The same person can be at level 4 "
            "for one task and level 1 for another. Part 8’s RACI matrix records who is responsible. The level "
            "records how far that responsibility goes.",
            ("photo", "blog/pm-delegation-levels.jpg", "Four levels of delegation, from finding out and "
             "reporting to acting alone. Say the level when you hand over the task. Examples are invented. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Step 3: Brief the Task So It Comes Back Right"),
            "A good briefing takes five to ten minutes and saves hours of rework. Cover five points.",
            ("point", "The result", "What “done” looks like. “A clean list of 212 stalls, one row each, in the "
             "shared folder.”"),
            ("point", "The reason", "Why it matters. “The market supervisor will use it to bill rentals from "
             "July.” People make better small decisions when they know the purpose."),
            ("point", "The limits", "Budget, time and anything that must not change. “Do not delete any "
             "record. Mark duplicates instead.”"),
            ("point", "The level", "From Step 2. “Act, then tell me.”"),
            ("point", "The date and the check-in", "“Due Thursday. Let us look at it together Tuesday "
             "afternoon.”"),
            "Then ask the person to say the task back in their own words. If the summary misses something, the "
            "briefing missed it too. Write the agreed points in one or two lines in the issue log from Part 26 "
            "or the team’s task list.",
            ("h", "Step 4: Follow Up at the Right Distance"),
            "Two mistakes sit on either side of good follow-up. Hovering means checking so often that the "
            "person cannot work. Disappearing means handing over and hearing nothing until the deadline.",
            ("point", "Agree the check-ins at the start", "One check-in halfway for a short task, weekly for a "
             "long one. Then keep to them."),
            ("point", "Ask about progress, not about method", "“How far along are you? Anything blocking you?” "
             "Let the person choose how to do it, within the limits."),
            ("point", "Make it easy to raise problems early", "Say during the briefing: “If you get stuck for "
             "more than a day, tell me. That is not a failure.”"),
            ("point", "Look at a sample", "For data work, check ten records instead of all of them. If ten are "
             "right, the method is probably sound."),
            ("h", "Step 5: When a Delegated Task Goes Wrong"),
            "Sooner or later, something comes back late or wrong. How the lead reacts decides whether anyone "
            "accepts the next task willingly.",
            ("point", "Look at the briefing first", "Was the result, the limit or the date clear? Many "
             "delegated tasks fail at the handover, not in the work."),
            ("point", "Fix it together, not over their head", "Taking the task back silently teaches the person "
             "that delegated work is not really theirs."),
            ("point", "Adjust the level, not the person’s worth", "Move the task back one level for a while. "
             "“Next time, show me the plan before you start.”"),
            ("point", "Own it upward", "To the sponsor, the lead says “we missed this,” not “my clerk missed "
             "this.” The lead remains answerable."),
            ("h", "Back to the Revenue Officer"),
            "She marked her 41 hours. Fourteen hours were tasks only she could do. Nineteen were tasks the "
            "clerks could do with a briefing, and eight were tasks the clerks could probably do better.",
            "She handed the stall list cleanup to the first clerk at level 3, with a rule for duplicates and a "
            "Tuesday check-in. She asked the second clerk to draft the reminder messages at level 2. Within a "
            "month, her own project hours had dropped to about 20 a week, and the reminder messages, written by "
            "someone who knew the taxpayers, drew more replies than her drafts had.",
            ("h", "Delegation and Growth"),
            "Delegation is also how people learn. A clerk who cleaned up the stall list now knows how the "
            "rental records fit together. That knowledge stays in the office if the lead is transferred, which "
            "is the same concern Part 31 raised about absences.",
            ("point", "Stretch a little, not too far", "Choose tasks slightly beyond what the person has done "
             "before."),
            ("point", "Give the credit in public", "When the sponsor praises the cleaned list, name the person "
             "who did it."),
            ("point", "Write down what worked", "If a delegated task becomes routine, turn it into a short "
             "procedure, as Part 37 described."),
            ("h", "Mistakes to Avoid"),
            ("point", "Delegating only the dull work", "People notice. Mix in tasks that build skills."),
            ("point", "No level stated", "Say whether the person reports, recommends, acts and tells, or acts "
             "alone."),
            ("point", "No check-in agreed", "Agree it at the start, or the lead ends up hovering or "
             "disappearing."),
            ("point", "Taking the task back silently", "Fix it together and adjust the level."),
            ("h", "Quick Recap"),
            ("point", "Choose with three labels", "Only I can, someone could with a briefing, someone could do "
             "it better."),
            ("point", "Say the level", "Find out, recommend, act and tell, or act alone."),
            ("point", "Brief five points", "Result, reason, limits, level and date, then have it said back."),
            ("point", "Stay answerable", "Follow up at agreed points, and own the result to the sponsor."),
            ("h", "Your Part 45 Action Plan"),
            ("point", "Today", "Mark every task with your name on it using the three labels."),
            ("point", "This week", "Hand over one repeating task, with the level and a check-in date."),
            ("point", "After a month", "Move one person up one level on a task they handled well."),
            ("cta", "Read: Project Management Series, Part 44: Leading Several Projects at Once Without Dropping Any", "/blog/project-management-part-44-several-projects-at-once/"),
            ("cta", "Read: Project Management Series, Part 8: Who Does What? Building a RACI Matrix", "/blog/project-management-part-8-raci-matrix/"),
            ("cta", "Read: Project Management Series, Part 18: Assigning People Without Overloading Them", "/blog/project-management-part-18-resource-allocation/"),
            ("cta", "Read: Project Management Series, Part 37: Writing a Standard Operating Procedure People Actually Follow", "/blog/project-management-part-37-standard-operating-procedure/"),
            ("ask", "Which task on your desk could someone else do better than you?"),
        ],
    },
    {
        "title": "Project Management Series, Part 44: Leading Several Projects at Once Without Dropping Any",
        "slug": "project-management-part-44-several-projects-at-once",
        "category": "pm",
        "date": "May 1, 2028",
        "summary": "In a small office, the same person often leads three projects while doing a regular job. This "
                   "part shows how to put every project on one page, get a clear order of priority from the "
                   "people who set it, protect blocks of time instead of switching all day, run one weekly "
                   "review, and say early when something has to give.",
        "publish_on": "2028-05-01 21:00",
        "body": [
            "The revenue officer led three projects that year: the text reminders for business tax, the cleanup "
            "of the market stall list, and the new filing room for real property records. She also ran the "
            "business tax section every day.",
            "Each project had its own folder, its own group chat and its own Monday meeting. By March, she was "
            "answering messages from all three during counter hours, and each project lead above her thought "
            "their project was her first priority. Two deadlines landed in the same week, and both slipped.",
            "(The office, the projects and the people are invented, continuing the treasury examples of this "
            "series.)",
            "Part 43 recovered a single project in trouble. This part looks at a more common problem: one "
            "person leading several projects at once, alongside regular work. After this post, you will know "
            "how to see all the work on one page, how to get a clear order of priority, how to plan the week "
            "in blocks, how to run one weekly review for everything, and how to raise a conflict before it "
            "becomes a missed date.",
            ("photo", "blog/pm-several-projects.jpg", "Several projects at once: one list of everything, one "
             "order of priority agreed with the sponsors, protected blocks of time, and one weekly review. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Why Several Projects Are Harder Than One Big One"),
            ("point", "Hidden totals", "Each project looks reasonable on its own. Often nobody sees the sum."),
            ("point", "Switching costs", "Moving between projects means finding the file, remembering where you "
             "stopped, and getting back into the problem. Many short switches can eat a large part of the day."),
            ("point", "Competing sponsors", "Each sponsor sees only their own project and may assume it comes "
             "first."),
            ("point", "Regular work does not stop", "Counter duty, reports and deadlines still come first on "
             "most days."),
            ("h", "Step 1: One Page for Everything"),
            "Make one list of every project and every regular duty that takes real time.",
            ("point", "For each project", "Name, sponsor, next milestone and its date, and hours needed per week "
             "for the next month."),
            ("point", "For regular work", "The hours it really takes, including the busy weeks such as January "
             "and the quarterly deadlines."),
            ("point", "Add it up", "Compare the total with the hours you actually have. Part 18 warned that "
             "someone who also works a counter does not have eight hours a day for a project."),
            "If the total is more than the hours available, the page shows it before a deadline does.",
            ("h", "Step 2: Get the Order of Priority From the People Who Set It"),
            "You cannot settle priorities between sponsors yourself. Take the one page to the person above all "
            "of them, often the department head.",
            ("point", "Ask for an order, not a ranking of importance", "“If two of these collide in the same "
             "week, which one goes first?”"),
            ("point", "Write it down", "Put the order at the top of the page and share it with every sponsor."),
            ("point", "Revisit it monthly", "Priorities change, but they should change in the open."),
            "Part 29 used a scoring matrix to choose which project to start. The same thinking helps when "
            "deciding which running project goes first.",
            ("h", "Step 3: Plan the Week in Blocks"),
            ("point", "Give each project a block", "For example, Tuesday afternoon for the stall list, Thursday "
             "morning for the reminders."),
            ("point", "Protect the blocks", "Treat them like a meeting with the sponsor. Turn off group chats "
             "that belong to other projects during that time."),
            ("point", "Leave slack", "Keep a few hours a week unassigned for surprises, in the spirit of the "
             "visible buffer from Part 21."),
            ("point", "Batch the small things", "Answer messages from all projects at set times, such as "
             "11:30 and 4:30, instead of all day."),
            ("photo", "blog/pm-several-projects-week.jpg", "One week in blocks: counter duty first, one "
             "protected block per project, two short message windows and some slack. The schedule is invented. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Step 4: One Weekly Review for Everything"),
            "Replace three Monday meetings in your head with one 30-minute review on Friday afternoon.",
            ("point", "Each project in turn", "What moved this week, what is due next week, and what is blocked."),
            ("point", "Look across projects", "Do two milestones land in the same week? Does one person appear "
             "in two projects at the same time?"),
            ("point", "Update the one page", "Dates, hours and any change in priority."),
            ("point", "Send short notes", "One or two lines to each sponsor, in the shape of the status report "
             "from Part 25."),
            ("h", "Step 5: Raise Conflicts Early"),
            "When two projects need the same week, say so as soon as you see it.",
            ("point", "Bring options, not only a problem", "“The filing room delivery and the reminder launch "
             "both fall on March 15. I can move the filing room by one week or ask for help on the reminders.”"),
            ("point", "Use the agreed order", "Point back to the order of priority from Step 2."),
            ("point", "Record the decision", "In the one page and in the next note to each sponsor."),
            "A conflict raised three weeks ahead is a scheduling choice. Raised the day before, it becomes a "
            "missed date.",
            ("h", "When to Say No"),
            "Sometimes the honest answer to a fourth project is “not now.”",
            ("point", "Show the page", "Let the requester see the hours already committed."),
            ("point", "Offer a date", "“I can start it in August, after the stall list closes.”"),
            ("point", "Offer a trade", "“If this one comes first, which of the others should wait?”"),
            "Part 31 covered planning for absences. The same one page shows who could take over a project if "
            "the lead is away.",
            ("h", "Back to the Revenue Officer"),
            "She made the one page in an afternoon. The total came to 52 hours a week against about 35 she "
            "could really give. The department head set the order: reminders first, stall list second, filing "
            "room third, with its date moved by six weeks.",
            "She blocked Tuesday and Thursday afternoons, moved project chats to two set times a day, and "
            "replaced the three Monday meetings with one Friday review. By June, all three projects were on "
            "their new dates, and the business tax section had stopped losing her to messages during counter "
            "hours.",
            ("h", "Leaving Each Project Easy to Pick Up"),
            "Switching costs less when each project is left in a state that is easy to return to.",
            ("point", "End each block with a note", "Two lines at the top of the project file: where you stopped "
             "and the very next step."),
            ("point", "One folder, one log", "Keep each project’s files, issue log and decisions in one place, "
             "so nothing has to be searched for."),
            ("point", "Tell the team your blocks", "If people know when you work on their project, they save "
             "questions for that time."),
            "These habits also make it easier for someone else to step in, which matters when one person "
            "carries several projects.",
            ("h", "Mistakes to Avoid"),
            ("point", "Keeping separate lists", "The total often stays hidden until it is too late."),
            ("point", "Settling priorities alone", "Ask the person above the sponsors."),
            ("point", "Switching all day", "Use blocks and set times for messages."),
            ("point", "Raising conflicts at the last minute", "Say it when you first see it."),
            ("h", "Quick Recap"),
            ("point", "One page", "Every project and regular duty, with hours and next dates."),
            ("point", "One order of priority", "Set by the person above the sponsors, written down."),
            ("point", "Blocks, not switching", "Protected time per project and set times for messages."),
            ("point", "One weekly review", "Look across projects, update the page, raise conflicts early."),
            ("h", "Your Part 44 Action Plan"),
            ("point", "Today", "List every project and regular duty with the hours each really takes."),
            ("point", "This week", "Ask your department head for an order of priority, in writing."),
            ("point", "Every Friday", "Hold a 30-minute review across all your projects."),
            ("cta", "Read: Project Management Series, Part 18: Assigning People Without Overloading Them", "/blog/project-management-part-18-resource-allocation/"),
            ("cta", "Read: Project Management Series, Part 29: Too Many Requests? Choosing the Next Project With a Scoring Matrix", "/blog/project-management-part-29-scoring-matrix/"),
            ("cta", "Read: Project Management Series, Part 36: Kanban Boards and Limits on Work in Progress", "/blog/project-management-part-36-kanban-boards/"),
            ("cta", "Read: Project Management Series, Part 25: The Status Report, One Page That Tells the Truth Early", "/blog/project-management-part-25-status-reports/"),
            ("ask", "How many projects are you leading right now, and does anyone above you know the total?"),
        ],
    },
    {
        "title": "Project Management Series, Part 43: When a Project Is in Trouble, a Recovery Plan in Five Steps",
        "slug": "project-management-part-43-project-recovery",
        "category": "pm",
        "date": "April 26, 2028",
        "summary": "Some projects slide from amber to red and stay there. This part shows how to pause and take "
                   "stock, find the few real causes, decide what to cut, keep or move, reset the plan with the "
                   "sponsor, and watch the first weeks closely, without hunting for someone to blame.",
        "publish_on": "2028-04-26 21:00",
        "body": [
            "The online payment project was six weeks behind. The status report had been amber for two months "
            "and red for three weeks. The test site worked on some days and not on others, the bank’s "
            "requirements had changed twice, and the two people doing most of the work had stopped coming to "
            "the weekly meeting because there was no time.",
            "The sponsor asked the project lead a direct question: “Can this still be saved, and what will it "
            "take?” The lead did not know. Nobody had stepped back long enough to find out.",
            "(The project and the people are invented, continuing the treasury examples of this series.)",
            "Part 42 tested a new system with its users before launch. This part is for the project that may "
            "never reach that point without help. After this post, you will know the signs that a project "
            "needs more than another push, a five-step way to recover it, how to talk to the sponsor about it, "
            "and when stopping is the better choice.",
            ("photo", "blog/pm-recovery.jpg", "A project recovery: pause and take stock, find the few real "
             "causes, decide what to cut, keep or move, reset the plan with the sponsor, and watch the first "
             "weeks closely. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Signs That a Push Is Not Enough"),
            "Most projects have bad weeks. A project in trouble shows a pattern.",
            ("point", "Red that does not move", "The status report from Part 25 has stayed red for several "
             "reports in a row, and each new date slips again."),
            ("point", "Earned value keeps falling", "Part 35’s schedule and cost indexes drop month after month, "
             "not just once."),
            ("point", "The issue log only grows", "Part 26’s log has more open issues each week than closed ones."),
            ("point", "People avoid the project", "Meetings are skipped, messages go unanswered, and team members "
             "quietly return to their regular work."),
            "One of these is a warning. Two or more together usually call for a deliberate recovery, not more "
            "overtime.",
            ("h", "Step 1: Pause and Take Stock"),
            "Stop adding new work for a few days. That feels wasteful, but working harder on a broken plan "
            "usually makes it worse.",
            ("point", "What is really done", "Not “almost done.” Count only what has been finished and accepted."),
            ("point", "What is left", "List every remaining piece of work from the work breakdown structure of "
             "Part 14."),
            ("point", "What has been spent", "Money and staff time, against the budget from Part 17."),
            ("point", "Talk to the people doing the work", "One by one, ask what is blocking them. They usually "
             "know before the reports do."),
            ("h", "Step 2: Find the Few Real Causes"),
            "Write down every problem people mention, then group them. Most lists shrink to two or three root "
            "causes.",
            ("point", "Ask why more than once", "The test site fails. Why? It runs on an old office computer. "
             "Why? No budget was set aside for a test server. That is the cause to fix."),
            ("point", "Separate causes from symptoms", "Missed dates are a symptom. Unclear requirements, too "
             "little time from key people, or a supplier who keeps changing terms are causes."),
            ("point", "No blame", "The goal is a plan that works, not a name. People hide problems when they "
             "expect blame, which is how the project got here."),
            ("photo", "blog/pm-recovery-triage.jpg", "Sorting the remaining work: keep what the main objective "
             "needs, move what can wait for a second phase, and cut what no one will miss. Tasks are invented. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Step 3: Decide What to Keep, Move or Cut"),
            "Go back to the objective in the charter. Then sort every remaining piece of work.",
            ("point", "Keep", "Work the main objective cannot do without."),
            ("point", "Move", "Useful work that can wait for a second phase after launch."),
            ("point", "Cut", "Work that no one will miss, or that was added without going through change "
             "control."),
            "Part 24 described how to handle changes properly. A recovery often reveals changes that slipped in "
            "without that process.",
            ("h", "Step 4: Reset the Plan With the Sponsor"),
            "A recovery plan is a new baseline. It needs the sponsor’s agreement, in writing.",
            ("point", "Tell the truth early", "Bring the stock-take, the causes and the options, not only a new "
             "date."),
            ("point", "Offer real choices", "For example: a smaller first release in eight weeks, or the full "
             "scope in sixteen weeks with one more staff member."),
            ("point", "Ask for what you need", "Protected time from key people, a decision on the supplier, or "
             "money for the test server."),
            ("point", "Record the decision", "In the minutes, with the new dates, scope and budget, as Part 27 "
             "described."),
            "Part 34 offered a ten-minute shape for presenting to decision makers. It works well here.",
            ("h", "Step 5: Watch the First Weeks Closely"),
            "A new plan needs proof that it is working, quickly.",
            ("point", "Shorter check-ins", "Fifteen minutes twice a week instead of one long meeting."),
            ("point", "Small, visible wins", "Pick early milestones that can be finished in the first two weeks."),
            ("point", "Same honest status", "Report against the new plan with the same green, amber and red "
             "rules."),
            ("point", "Clear the blocks fast", "The project lead’s main job now is removing whatever stops the "
             "team."),
            ("h", "When Stopping Is the Better Choice"),
            "Sometimes the honest answer to “Can this be saved?” is no, or not at a price worth paying.",
            ("point", "The need has gone", "A national system now does what the project was building."),
            ("point", "The cost has outgrown the benefit", "Part 10’s business case no longer holds."),
            ("point", "A key condition cannot be met", "The bank will not support the setup the project needs."),
            "Stopping is a decision, not a failure, when it is made on evidence. Close the project properly, as "
            "Part 28 described, and keep what was learned.",
            ("h", "Back to the Payment Project"),
            "The lead paused new work for three days and talked to each team member. Three causes came out: no "
            "proper test server, no single contact at the bank, and the two key staff members still carrying "
            "their full counter duties.",
            "The sponsor chose a smaller first release: payments for business tax only, with real property tax "
            "moved to a second phase. The office bought a modest test server, the bank named one contact, and "
            "the two staff members were relieved of counter duty for two afternoons a week. The status turned "
            "amber within a month and green two months later.",
            ("h", "Keeping It From Happening Again"),
            ("point", "Agree the warning rules early", "Decide at the start how many red reports in a row trigger "
             "a stock-take."),
            ("point", "Protect key people from the start", "Write their project hours into the plan, not on top "
             "of full regular duties."),
            ("point", "Review causes at closing", "Bring the recovery’s causes to the lessons-learned review."),
            ("h", "Mistakes to Avoid"),
            ("point", "Pushing harder on the same plan", "Find the causes first."),
            ("point", "Hiding the trouble", "A sponsor told early has more choices."),
            ("point", "Looking for someone to blame", "It drives problems underground."),
            ("point", "Resetting without cutting", "A new date with the same scope often fails again."),
            ("h", "Quick Recap"),
            ("point", "Know the signs", "Steady red, falling earned value, a growing issue log, absent people."),
            ("point", "Five steps", "Pause, find causes, keep or move or cut, reset with the sponsor, watch "
             "closely."),
            ("point", "Real choices for the sponsor", "Scope, time and resources, with honest numbers."),
            ("point", "Stopping can be right", "When the need, the benefit or a key condition is gone."),
            ("h", "Your Part 43 Action Plan"),
            ("point", "For a project in trouble", "Book three days to take stock before promising any new date."),
            ("point", "For every project", "Agree now on what the sponsor wants to hear, and when, if the status "
             "stays red."),
            ("point", "After a recovery", "Add the causes you found to the project kit from Part 30."),
            ("cta", "Read: Project Management Series, Part 25: The Status Report, One Page That Tells the Truth Early", "/blog/project-management-part-25-status-reports/"),
            ("cta", "Read: Project Management Series, Part 35: Earned Value Made Simple, Are We on Budget and on Schedule?", "/blog/project-management-part-35-earned-value/"),
            ("cta", "Read: Project Management Series, Part 24: Change Control, Saying Yes to a Change Without Losing the Plan", "/blog/project-management-part-24-change-control/"),
            ("cta", "Read: Project Management Series, Part 34: Presenting a Project to Decision Makers in Ten Minutes", "/blog/project-management-part-34-presenting-in-ten-minutes/"),
            ("ask", "What was the first sign that your last troubled project needed more than a push?"),
        ],
    },
    {
        "title": "Project Management Series, Part 42: User Acceptance Testing, Letting the People Who Will Use It Say Yes",
        "slug": "project-management-part-42-user-acceptance-testing",
        "category": "pm",
        "date": "April 21, 2028",
        "summary": "Before a new system or process goes live, the people who will use it every day should try it on "
                   "real work and say whether it is ready. This part explains what user acceptance testing is, "
                   "how to write simple test cases from the requirements, who should test, how to record "
                   "results, and how to decide whether to go live.",
        "publish_on": "2028-04-21 21:00",
        "body": [
            "The new collection screen passed every check the developer ran. Totals added up. Receipts printed. "
            "The project lead scheduled the switch for the first Monday of the month.",
            "On the Friday before, a cashier sat down to try it with a real line of taxpayers in mind. Her first "
            "payment was a business tax with a surcharge, paid partly in cash and partly by check. The screen "
            "had no way to split the payment. She tried three more common cases and found two more gaps. None "
            "of them had been in the developer’s tests, because the developer had never worked a counter.",
            "(The project, the system and the people are invented, continuing the treasury examples of this "
            "series. The definition quoted below comes from the glossary of the International Software Testing "
            "Qualifications Board.)",
            "Part 41 made the schedule easy to read. This part looks at the last check before launch. After "
            "this post, you will know what user acceptance testing is, how it differs from the checks in Part "
            "23, how to write test cases from the requirements, who should test, how to log what fails, and "
            "how to make the go-live decision.",
            ("photo", "blog/pm-uat.jpg", "User acceptance testing: the people who will use the new system try "
             "it on real cases, record what passes and fails, and decide with the sponsor whether it is ready. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "What User Acceptance Testing Is"),
            "The International Software Testing Qualifications Board’s glossary describes user acceptance "
            "testing as acceptance testing “conducted in a real or simulated operational environment by "
            "intended users.” In plain words: the people who will use the thing every day try it on the kind of "
            "work they really do, and then say whether they accept it.",
            ("point", "Not the developer’s test", "The developer checks that the system works as built. Users "
             "check that it works for the job."),
            ("point", "Not only for software", "A new form, a new counter layout or a new procedure can be "
             "tested the same way."),
            ("point", "Ends with a decision", "Accept, accept with conditions, or not yet."),
            "Part 23 set quality standards and chose checks for each deliverable. User acceptance testing is "
            "the final check, done by the people the deliverable is for.",
            ("h", "Start From the Requirements"),
            "Part 9 asked for requirements that can be tested. This is where that pays off. Each requirement "
            "becomes one or more test cases.",
            ("point", "Requirement", "The cashier can accept one payment in cash and check together."),
            ("point", "Test case", "Business tax of ₱18,450 with surcharge. Pay ₱10,000 in cash and ₱8,450 by "
             "check. Expected: one official receipt showing both modes, and the check recorded for the deposit "
             "slip."),
            ("point", "Pass or fail", "The tester writes what actually happened and marks it."),
            "Include the ordinary cases that fill most of the day and the awkward ones that cause most of the "
            "trouble: partial payments, corrections, cancelled receipts, a power interruption, a taxpayer with "
            "two businesses.",
            ("h", "Who Should Test"),
            ("point", "The people who will use it", "Cashiers, collectors, the clerk who prepares the report of "
             "collections. Not only their supervisor."),
            ("point", "A mix of experience", "One person who knows every exception, and one who joined recently "
             "and follows the screen literally."),
            ("point", "Not the builder", "The developer can sit nearby to watch and take notes, but should not "
             "touch the keyboard."),
            ("point", "A sponsor who signs", "The person from Part 2’s charter who can say yes for the office."),
            ("h", "Set Up a Safe Place to Test"),
            ("point", "A copy, not the live data", "Test on a copy of the records, so mistakes do not change real "
             "accounts."),
            ("point", "Realistic data", "Use real kinds of cases, with names and personal details replaced, as "
             "Part 6 of the Data Analytics Series advised."),
            ("point", "The real equipment", "The same printer, the same screen size and the same internet "
             "connection the counter will have."),
            ("point", "Set the time aside", "Testing squeezed between taxpayers rarely gets done. Block two "
             "afternoons."),
            ("photo", "blog/pm-uat-log.jpg", "A test log on one sheet: each case, the expected result, what "
             "happened, and pass, fail or the rank of the failure. Cases are invented. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "Record Every Result"),
            "A shared sheet is enough. One row per test case.",
            ("point", "Columns", "Case number, what to do, expected result, actual result, pass or fail, tester, "
             "date, and notes."),
            ("point", "Describe failures exactly", "Write the steps, the amount and what appeared on screen. "
             "“It doesn’t work” cannot be fixed."),
            ("point", "Rank each failure", "Blocker: the counter cannot work without a fix. Major: there is a "
             "workaround, but it is slow or risky. Minor: cosmetic."),
            ("point", "Retest after each fix", "A fixed case is tested again by the same tester, and the result "
             "is added to the log."),
            "Failures go into the issue log from Part 26 with an owner and a date, so none are lost between "
            "testing and launch.",
            ("h", "The Go-Live Decision"),
            "Agree on the rules before testing starts, so the decision is not argued from scratch on the last "
            "day.",
            ("point", "Accept", "Every case passed, or only minor failures remain."),
            ("point", "Accept with conditions", "No blockers. Each major failure has a workaround written down "
             "and a fix date."),
            ("point", "Not yet", "Any blocker remains. Set a new date after the fix is retested."),
            "Record the decision and the sponsor’s signature in the minutes, as Part 27 described. A written "
            "yes protects both the team and the users.",
            ("h", "Back to the Split Payment"),
            "The cashier’s three failures went into the log: the split payment as a blocker, and two others as "
            "major. The switch moved two weeks. The developer fixed the split payment, and the cashier retested "
            "it with five variations.",
            "The second round passed with one minor issue, a misaligned label on the printed receipt. The "
            "sponsor accepted the system with that condition noted, and the first Monday on the new screen "
            "went quietly.",
            ("h", "Questions Testers Should Ask"),
            ("point", "Can I undo a mistake?", "Cancel a receipt, correct an amount, reverse a wrong posting."),
            ("point", "What happens at the end of the day?", "Does the report of collections match the receipts "
             "issued?"),
            ("point", "What if the power or internet goes out?", "Is there a manual fallback, and can the "
             "records be entered later?"),
            ("point", "Is it faster than the old way?", "If not, Part 33 explained why people will drift back."),
            ("h", "Testing Also Trains"),
            "User acceptance testing has a useful side effect. The cashiers who tested the screen became the "
            "first people who knew it well.",
            ("point", "Use testers as helpers", "On launch day, seat one tester near the counters to answer "
             "questions from the others."),
            ("point", "Turn test cases into training", "The awkward cases make good practice exercises for the "
             "rest of the staff."),
            ("point", "Feed the procedure", "Steps that confused testers belong in the standard operating "
             "procedure from Part 37."),
            ("h", "Mistakes to Avoid"),
            ("point", "Letting the builder test alone", "Builders test what they built, not what the users need."),
            ("point", "Testing only the easy cases", "The awkward ones cause most of the trouble."),
            ("point", "No written pass rules", "Decide what counts as ready before testing begins."),
            ("point", "Testing on live records", "Use a copy with personal details replaced."),
            ("h", "Quick Recap"),
            ("point", "Users decide", "The people who will use it test it on real kinds of work."),
            ("point", "Cases come from requirements", "Each testable requirement becomes a test case."),
            ("point", "Log every result", "Expected, actual, pass or fail, and a rank for each failure."),
            ("point", "Agree the go-live rule early", "Accept, accept with conditions, or not yet."),
            ("h", "Your Part 42 Action Plan"),
            ("point", "Today", "List the five most common cases and the five most awkward cases at your counter."),
            ("point", "Before the next launch", "Turn each requirement into a test case with an expected result."),
            ("point", "At the test", "Seat the real users, keep the builder’s hands off the keyboard, and log "
             "everything."),
            ("cta", "Read: Project Management Series, Part 23: Quality Planning, Deciding What Good Enough Means", "/blog/project-management-part-23-quality-planning/"),
            ("cta", "Read: Project Management Series, Part 9: Gathering Requirements When Nobody Knows What They Want", "/blog/project-management-part-9-gathering-requirements/"),
            ("cta", "Read: Project Management Series, Part 26: The Issue Log, Turning Problems Into Next Steps", "/blog/project-management-part-26-issue-log/"),
            ("cta", "Read: Project Management Series, Part 33: Getting People to Use the New Process, Not Just Install It", "/blog/project-management-part-33-adopting-the-new-process/"),
            ("ask", "Who in your office should have tested the last new system before it went live?"),
        ],
    },
    {
        "title": "Project Management Series, Part 41: A Timeline Anyone Can Read, Building a Gantt Chart in Google Sheets",
        "slug": "project-management-part-41-gantt-chart-in-sheets",
        "category": "pm",
        "date": "April 17, 2028",
        "summary": "A list of tasks with start and end dates is hard to read. The same list drawn as bars on a "
                   "calendar shows at a glance what overlaps, what is late and what comes next. This part builds "
                   "a simple Gantt chart in Google Sheets with conditional formatting, adds a line for today, and "
                   "notes the built-in timeline view where it is available.",
        "publish_on": "2028-04-17 21:00",
        "body": [
            "The project schedule lived in a sheet with forty rows: task, owner, start date, end date. Every "
            "Monday, the lead read it aloud at the team meeting, row by row. By the tenth row, nobody was really listening.",
            "Then the lead added colored bars beside the dates, one column per week. The next Monday, a clerk "
            "pointed at the screen before the lead had said a word: “Those three bars all land on the same week, "
            "and they all belong to me.”",
            "(The project, the tasks and the dates are invented, continuing the treasury examples of this series. "
            "The Google Sheets features described are real.)",
            "Part 40 held retrospectives while the work was running. This part makes the schedule itself easy to "
            "read. After this post, you will know what a Gantt chart shows, how to build one in Google Sheets "
            "with conditional formatting, how to mark today and late tasks, and what the built-in timeline view "
            "offers.",
            ("photo", "blog/pm-gantt.jpg", "A Gantt chart: one row per task, one column per week, and a colored "
             "bar from each task’s start to its end, so overlaps and delays are visible at a glance. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "What a Gantt Chart Shows"),
            ("point", "Rows are tasks", "Here, the work packages from the work breakdown structure in Part 14."),
            ("point", "Columns are time", "Days, weeks or months, depending on the length of the project."),
            ("point", "Bars are durations", "Each bar starts on the task’s start date and ends on its finish "
             "date."),
            "Read across a row, and you see how long each single task takes. Read down a single week, and you see everything "
            "happening at the same time, which is where overloads hide. Part 18 covered assigning people "
            "without overloading them.",
            ("h", "Step 1: The Task Table"),
            "Set up four columns, with headers in row 2 and tasks from row 3:",
            ("point", "Column A", "Task, such as “Scan market contracts.”"),
            ("point", "Column B", "Owner."),
            ("point", "Column C", "Start date."),
            ("point", "Column D", "End date."),
            "Use real dates, not text, so the formulas can compare them correctly. Part 29 of the Data Analytics Series "
            "covered dates in Google Sheets.",
            ("h", "Step 2: The Calendar Row"),
            ("point", "First week", "In F2, type the Monday of the project’s first week, such as March 1, 2027."),
            ("point", "Next weeks", "In G2, type =F2+7 and fill to the right for as many weeks as the project "
             "runs."),
            ("point", "Format", "Show the dates as day and month, and narrow the columns so the weeks fit on "
             "one screen."),
            ("h", "Step 3: The Bars"),
            "Select the grid from F3 to the last week and the last task. Open Format, then Conditional "
            "formatting, and choose “Custom formula is.”",
            ("point", "Formula", "=AND(F$2+6>=$C3, F$2<=$D3)"),
            ("point", "What it means", "Color the cell if any day of that week falls between the task’s start "
             "and end dates."),
            ("point", "The dollar signs", "F$2 keeps the row of week dates fixed. $C3 and $D3 keep the date "
             "columns fixed. Everything else moves as the rule is applied across the grid."),
            ("point", "Choose a fill color", "One calm color for all bars is enough to start."),
            "Part 31 of the Data Analytics Series introduced conditional formatting. This is the same tool, "
            "used to draw.",
            ("photo", "blog/pm-gantt-sheet.jpg", "The sheet behind the chart: a task table on the left, week "
             "dates across the top, and one conditional formatting rule that colors each bar. Dates are "
             "invented. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Step 4: Mark Today"),
            "Add a rule to the row of week dates, F2 to the last week, so the current week stands out:",
            ("point", "Formula", "=AND(TODAY()>=F$2, TODAY()<F$2+7)"),
            ("point", "Format", "Bold text and a gold fill on the date of the current week."),
            "Now the chart answers the Monday question without anyone reading it aloud: what should be "
            "happening this week?",
            ("h", "Step 5: Show Late Tasks"),
            ("point", "Add a Status column", "In column E, mark each task Done, In progress or Not started."),
            ("point", "A third rule for the bars", "=AND(F$2+6>=$C3, F$2<=$D3, $D3<TODAY(), $E3<>\"Done\")"),
            ("point", "Format", "A red fill. Bars of tasks past their end date and not done turn red."),
            ("point", "Put it first", "Google’s help explains that rules are evaluated in the order listed, "
             "and the first rule found to be true defines the format. Drag the late rule above the bar rule."),
            "The red bars become the first items of the status report from Part 25.",
            ("h", "Keeping It Readable"),
            ("point", "Group by phase", "Put a bold phase row, such as “Preparation” or “Rollout,” above its "
             "tasks, and leave its bar cells blank."),
            ("point", "Freeze the left columns", "Freeze columns A to E, so task names stay visible while you "
             "scroll across the weeks."),
            ("point", "One screen if possible", "If the project runs longer than a screen of weeks, show the "
             "next eight weeks in detail and the rest by month on a second tab."),
            ("point", "Print for the wall", "Some teams still read best from paper. A printed chart taped near "
             "the work, updated each Monday, can work as well as a screen."),
            ("h", "Dependencies and the Critical Path"),
            "A simple Gantt chart in Sheets does not draw arrows between tasks. Keep the dependencies in a column "
            "instead, such as “after Task 3,” and set each start date from the predecessor’s end. Part 20 "
            "explained dependencies, and Part 16 the critical path that sets the finish date. Color the "
            "critical tasks differently, so a delay on them is noticed first.",
            ("h", "The Built-In Timeline View"),
            "Google Sheets also has a timeline view. Google’s help describes it as an interactive visual layer "
            "in Sheets, created from the Insert menu, that needs a card title, a start date and an end date for "
            "each task. The same help page lists only Google Workspace editions as eligible, so it may not "
            "appear in every account.",
            ("point", "If you have it", "It is quicker to set up and can group cards by owner."),
            ("point", "If you do not", "The conditional formatting chart works in any version of Sheets."),
            ("h", "Back to the Clerk’s Three Bars"),
            "The three tasks in the same week were scanning contracts, updating the stall list and preparing "
            "the first batch of notices. The lead moved the notices two weeks later, because they depended on "
            "the updated list anyway, and asked a second clerk to take half the scanning.",
            "The schedule had held those facts for a month, in plain dates that everyone had heard every Monday. The bars made them visible in a second, to everyone at once.",
            ("h", "Mistakes to Avoid"),
            ("point", "Dates typed as text", "The rules will not color anything."),
            ("point", "Too fine a scale", "Daily columns for a six-month project make the chart too wide to read."),
            ("point", "Never updating it", "A chart that shows last month’s plan misleads."),
            ("point", "Hiding the owner", "Keep the owner column visible, so overloads show by name."),
            ("h", "Quick Recap"),
            ("point", "Tasks down, weeks across", "One bar per task from start to end."),
            ("point", "One rule draws the bars", "=AND(F$2+6>=$C3, F$2<=$D3)"),
            ("point", "Two more rules add meaning", "A column for today and red for late tasks."),
            ("point", "Timeline view where available", "Conditional formatting everywhere else."),
            ("h", "Your Part 41 Action Plan"),
            ("point", "Today", "Copy your project’s task list into a sheet with owner, start and end dates."),
            ("point", "This week", "Add the calendar row and the bar rule, then the today and late rules."),
            ("point", "Every Monday", "Update the status column before the meeting and start with the red bars."),
            "The Monday meeting got shorter. The lead stopped reading the schedule aloud and started each "
            "meeting with the same question: “Any red bars, and any weeks with too many bars for one person?”",
            ("cta", "Read: Project Management Series, Part 14: The Work Breakdown Structure, One Bite at a Time", "/blog/project-management-part-14-work-breakdown-structure/"),
            ("cta", "Read: Project Management Series, Part 16: The Critical Path, Finding the Work That Sets the Finish Date", "/blog/project-management-part-16-critical-path/"),
            ("cta", "Read: Project Management Series, Part 20: Understanding Dependencies, When Task B Is Waiting on Task A", "/blog/project-management-part-20-dependencies/"),
            ("cta", "Read: Data Analytics Series, Part 31: Conditional Formatting, Letting the Sheet Point at the Problems", "/blog/data-analytics-part-31-conditional-formatting/"),
            ("ask", "How does your team see the schedule today: a list, a chart or someone’s memory?"),
        ],
    },
    {
        "title": "Project Management Series, Part 40: The Retrospective, Improving While the Work Is Still Running",
        "slug": "project-management-part-40-retrospectives",
        "category": "pm",
        "date": "April 12, 2028",
        "summary": "A lessons-learned review at the end helps the next project. A retrospective every few weeks "
                   "helps the current one. This part explains what a retrospective is, a simple three-question "
                   "format, how to keep it short and blame-free, and how to make sure its actions actually happen.",
        "publish_on": "2028-04-12 21:00",
        "body": [
            "The market records project was in its second month. The team was busy, the work was moving, and "
            "the same small problems kept coming back: scanned contracts saved under different names, a shared "
            "sheet that two people edited at once, and a weekly meeting that ran long every time.",
            "Each problem was mentioned in passing, then forgotten until it happened again. Nobody had set aside "
            "time to fix the way the team worked, only the work itself.",
            "(The project and the team are invented, continuing the treasury examples of this series. The "
            "description of a retrospective is quoted from Scrum.org.)",
            "Part 39 looked at benefits after a project ends. This part looks inside a running project, at how "
            "a team gets better while there is still time to use what it learns. After this post, you will "
            "know what a retrospective is, how it differs from lessons learned, a simple format, how to run one "
            "in under an hour, and how to make its decisions stick.",
            ("photo", "blog/pm-retro.jpg", "A retrospective: every few weeks, the team looks at how it worked, "
             "not only what it produced, and picks one or two changes to try. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "What a Retrospective Is"),
            "The retrospective comes from Scrum, the agile method mentioned in Part 5. Scrum.org states that "
            "“the purpose of the Sprint Retrospective is to plan ways to increase quality and effectiveness.” "
            "The team inspects how the last cycle went with regard to individuals, interactions, processes, "
            "tools and its definition of done.",
            "A treasury project does not need to run Scrum to borrow the idea. Every two to four weeks, the team "
            "stops for a short meeting about how it is working.",
            ("point", "About the way of working", "Not a status report. Part 25 already covered status."),
            ("point", "Short and regular", "Scrum.org timeboxes it to a maximum of three hours for a one-month "
             "cycle. A small treasury team can do it in 45 minutes."),
            ("point", "Ends with actions", "One or two changes to try before the next one."),
            ("h", "Retrospective or Lessons Learned?"),
            ("point", "Lessons learned", "Part 28 held it at closing. It helps the next project."),
            ("point", "Retrospective", "Held during the project. It helps this project, while the lessons can "
             "still change the outcome."),
            "The two work well together. Notes from each retrospective make the final lessons-learned review "
            "faster and more accurate.",
            ("h", "A Simple Format: Three Questions"),
            ("point", "What helped us?", "Things to keep doing."),
            ("point", "What got in the way?", "Problems with the process, tools or handoffs, not with people."),
            ("point", "What will we try next?", "One or two specific changes, each with an owner."),
            "Some teams use other labels, such as keep, stop and start. The labels matter less than ending with "
            "a short list of actions.",
            ("photo", "blog/pm-retro-board.jpg", "One sheet, three columns: what helped, what got in the way, "
             "and what we will try next, with an owner and a date for each action. (Illustration: Butch "
             "Mahinay, aumahinay.dev)", "medium"),
            ("h", "Running One in 45 Minutes"),
            ("point", "5 minutes: check last time’s actions", "Did they happen? Did they help? Start here, or "
             "the meeting turns into a list of wishes."),
            ("point", "10 minutes: write silently", "Each person writes notes for the first two questions on a "
             "shared sheet or sticky notes. Writing first lets quieter members be heard."),
            ("point", "15 minutes: group and discuss", "Put similar notes together. Talk about the biggest "
             "groups first."),
            ("point", "10 minutes: choose actions", "Pick one or two. Give each an owner and a date."),
            ("point", "5 minutes: record", "Copy the actions into the issue log from Part 26 or the minutes from "
             "Part 27."),
            ("h", "Keeping It Blame-Free"),
            "A retrospective works only if people say what really happened.",
            ("point", "Talk about the process", "“Files were saved under different names” instead of “Ana saves "
             "files wrong.”"),
            ("point", "The lead speaks last", "If the most senior person speaks first, others may simply agree."),
            ("point", "What is said stays useful, not personal", "Notes record problems and actions, not who "
             "complained."),
            "Part 38 covered conflict about the work. A retrospective is a regular, calm place to raise it "
            "before it grows.",
            ("h", "Back to the Market Records Project"),
            "The first retrospective took 40 minutes, a little under the time set aside. Three problems got the most notes.",
            ("point", "File names", "Action: one naming pattern, written at the top of the folder, owned by the "
             "records clerk. Part 15 of the Data Analytics Series suggested a pattern."),
            ("point", "Two people editing one sheet", "Action: each person works in their own tab, and one "
             "person merges on Fridays."),
            ("point", "Long weekly meeting", "Not chosen this time. Two actions were enough."),
            "Two weeks later, the second retrospective began by checking both actions. File names were "
            "consistent. The tab system worked but the Friday merge took an hour, so it became the next "
            "problem to solve. The long meeting was finally addressed in the third retrospective, with a "
            "written agenda.",
            ("h", "Questions That Open the Discussion"),
            "When the notes are thin, a few extra questions help people remember.",
            ("point", "Where did we wait?", "For a signature, a file, an answer or a person."),
            ("point", "What did we do twice?", "Rework can be a sign of an unclear step."),
            ("point", "What surprised us?", "A surprise is a gap in the plan or the procedure."),
            ("point", "What would we tell a new member?", "The answer is a lesson worth writing down."),
            ("h", "A Team of Two or Three"),
            "Small treasury teams may think a retrospective is too formal. It does not have to be.",
            ("point", "Fifteen minutes", "Over coffee at the end of every second Friday."),
            ("point", "One shared sheet", "Three columns, the date at the top, kept for the whole project."),
            ("point", "One action", "Even a single small change every two weeks adds up to more than twenty in "
             "a year."),
            "The format matters less than the habit of stopping, looking and changing one thing.",
            ("h", "Making Actions Stick"),
            ("point", "Few actions", "One or two that get done beat ten that never do."),
            ("point", "An owner and a date", "Every action, no exceptions."),
            ("point", "Check them first next time", "That one habit keeps retrospectives from becoming "
             "complaint sessions."),
            ("point", "Change the procedure", "When an action works, write it into the SOP from Part 37."),
            ("point", "Make results visible", "Keep a running list of every change the team has made, with the "
             "date. Seeing the list grow shows the team that the meetings are worth the time."),
            ("point", "Drop what did not help", "If an action made things worse, say so at the next meeting and "
             "undo it. A failed experiment is still useful information."),
            ("h", "Mistakes to Avoid"),
            ("point", "Turning it into a status meeting", "Talk about how you work, not what you finished."),
            ("point", "Too many actions", "Pick one or two."),
            ("point", "Skipping it when busy", "Busy periods are when a weak process hurts."),
            ("point", "Naming and blaming", "Describe the process, not the person."),
            ("h", "Quick Recap"),
            ("point", "A short, regular review", "Every two to four weeks, about how the team works."),
            ("point", "Three questions", "What helped, what got in the way, what we will try next."),
            ("point", "Check last time’s actions first", "So each meeting builds on the last."),
            ("point", "Blame-free", "Process, not people."),
            ("h", "Your Part 40 Action Plan"),
            ("point", "This week", "Book 45 minutes with your team for a first retrospective."),
            ("point", "At the meeting", "Use the three questions and leave with no more than two actions."),
            ("point", "Next time", "Open by checking those actions."),
            "By the end of the project, the team had held six retrospectives and made nine small changes. The "
            "final lessons-learned review took half the usual time, because most of the lessons had already "
            "been written down, and several had already been applied.",
            ("cta", "Read: Project Management Series, Part 28: Closing the Project, Handover and Lessons Learned", "/blog/project-management-part-28-closing-the-project/"),
            ("cta", "Read: Project Management Series, Part 5: Waterfall, Agile or Hybrid? Choosing How to Run the Work", "/blog/project-management-part-5-waterfall-agile-hybrid/"),
            ("cta", "Read: Project Management Series, Part 26: The Issue Log, Turning Problems Into Next Steps", "/blog/project-management-part-26-issue-log/"),
            ("cta", "Read: Project Management Series, Part 38: When the Team Disagrees, Five Ways to Handle Conflict", "/blog/project-management-part-38-handling-conflict/"),
            ("ask", "When did your team last stop to talk about how it works, not just what it finished?"),
        ],
    },
    {
        "title": "Project Management Series, Part 39: After the Project Ends, Checking Whether the Benefits Arrived",
        "slug": "project-management-part-39-benefits-review",
        "category": "pm",
        "date": "April 3, 2028",
        "summary": "A project can finish on time and on budget and still fail to deliver what it promised. A "
                   "benefits review, held months after closing, checks whether the promised improvement really "
                   "happened. This part explains outputs, outcomes and benefits, who owns the review, how to "
                   "measure against a baseline, and what to do when the numbers fall short.",
        "publish_on": "2028-04-03 21:00",
        "body": [
            "The text reminder project had closed in good order. Every barangay was enrolled, the procedure was "
            "written, and the lessons-learned review was filed. At the year-end meeting, a council member asked "
            "a question nobody had prepared for: “So did more people pay on time?”",
            "The project lead knew the pilot numbers by heart. Nobody had checked the whole municipality since "
            "the rollout.",
            "(The project and the figures continue the invented example of earlier parts. The definitions "
            "quoted below come from a published Project Management Institute paper.)",
            "Part 38 settled disagreements inside the team. This part steps outside the project, after it has "
            "ended, to ask whether it did what it was for. After this post, you will know the difference "
            "between an output, an outcome and a benefit, who should own the benefits, how to measure them "
            "against a baseline, when to check, and what to do if the benefits did not arrive.",
            ("photo", "blog/pm-benefits.jpg", "A benefits review: compare the measure after the project with "
             "the baseline before it, at set times, and name an owner who keeps checking after the team "
             "disbands. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Finished Is Not the Same as Successful"),
            "Part 28 closed the project: handover, sign-off and lessons learned. Closing confirms that the work "
            "was delivered. It does not prove that anyone is better off.",
            "A paper on benefits realization published by the Project Management Institute defines a benefit "
            "as a “measurable improvement resulting from the outcome which is perceived as an advantage by a "
            "stakeholder.” The same paper notes that benefits can be realized significantly after the project "
            "has closed. That is why the check has to happen later, and why someone has to remember to do it.",
            ("h", "Output, Outcome, Benefit"),
            ("point", "Output", "What the project made. Here: a list of business owners’ mobile numbers and a "
             "procedure for sending reminders."),
            ("point", "Outcome", "What changed because of it. Here: owners receive a reminder before every "
             "quarterly deadline."),
            ("point", "Benefit", "The measurable improvement someone values. Here: more owners pay the "
             "quarterly business tax on time, and fewer delinquency notices need to be printed and served."),
            "A project can deliver every output and still miss the benefit, for example if the reminders go to "
            "old numbers that nobody answers.",
            ("h", "The Benefit Owner"),
            "The project team disbands at closing. The benefit stays with the office that runs the work.",
            ("point", "Name an owner", "A position in the operating office, such as the head of the license "
             "and permits section, not the project lead."),
            ("point", "Write it in the handover", "Part 28’s handover note should list each benefit, its measure "
             "and its owner."),
            ("point", "Set the review dates", "Put them on the office calendar before the team leaves."),
            ("h", "Start From the Baseline"),
            "A benefit can only be measured against what came before. Part 6 asked for objectives with a "
            "number and a date. The baseline is the starting number.",
            ("point", "Before the rollout", "About 60 percent of quarterly business tax payments were on time "
             "across the municipality."),
            ("point", "Pilot result", "Part 32’s pilot barangay reached 78 percent, while the comparison "
             "barangays moved only from 59 to 61 percent."),
            ("point", "The promised benefit", "On-time payment of at least 70 percent across the municipality "
             "within a year of rollout."),
            ("h", "When to Check"),
            ("point", "Three months", "Is the outcome happening? Are reminders going out and arriving?"),
            ("point", "Six months", "Is the benefit appearing in the numbers?"),
            ("point", "Twelve months", "Has it lasted through a full cycle of deadlines?"),
            "Each check takes an hour if the measure was defined at the start. It takes a week if someone has "
            "to work out what to count.",
            ("photo", "blog/pm-benefits-chart.jpg", "On-time payment before and after the rollout, checked at "
             "three, six and twelve months against the baseline and the target. Figures are invented. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Back to the Council Member’s Question"),
            "The head of the license and permits section, named as the owner in the handover, ran the numbers "
            "the following week.",
            ("point", "Three months", "96 percent of reminders delivered. The outcome was happening."),
            ("point", "Six months", "On-time payment 72 percent, up from about 60."),
            ("point", "Twelve months", "74 percent. The target of 70 was met and held."),
            ("point", "Printed notices", "Delinquency notices served in the year fell from 410 to 260, which "
             "saved paper, postage and collectors’ time."),
            "The answer to the council member was yes, with numbers.",
            ("h", "Is It Really the Project?"),
            "Other things change too. A new online payment option, a busy year for the market or a new "
            "ordinance can lift payments without any reminder.",
            ("point", "Compare with the pilot", "The pilot’s comparison barangays showed how much on-time "
             "payment moved without reminders."),
            ("point", "List other changes", "Write down anything else that changed in the same period, and "
             "say so in the report."),
            ("point", "Be modest", "Say “the reminders likely account for most of the gain,” not “the reminders "
             "caused all of it.” Part 35 of the Data Analytics Series explained why two numbers moving "
             "together is not proof."),
            ("h", "Watch for Disbenefits"),
            "Some results are unwelcome. Name them too.",
            ("point", "Reminders after payment", "Owners who had already paid still received a reminder, and "
             "some called to complain."),
            ("point", "More calls to the counter", "Owners phoned to ask how much they owed."),
            "The office fixed the first by removing paid accounts from the list on the morning of each send, "
            "a new step in the procedure from Part 37.",
            ("h", "When the Benefit Falls Short"),
            ("point", "Find the weak step", "Were reminders sent? Delivered? Read? Acted on?"),
            ("point", "Fix the operation, not the history", "The project is closed. Improvements now go through "
             "the operating office’s normal routine."),
            ("point", "Report honestly", "A shortfall reported early is a lesson. A shortfall hidden becomes a "
             "surprise at the next audit."),
            ("point", "Feed the next project", "Add what was learned to the project kit from Part 30, so the "
             "next business case promises what can be measured."),
            ("h", "A One-Page Benefits Report"),
            "Part 25 kept project status on one page. A benefits report can be just as short.",
            ("point", "The promise", "The benefit, its measure and its target, copied from the business case."),
            ("point", "The numbers", "Baseline, target and the latest result, with the date of each."),
            ("point", "Other changes", "Anything else that could have moved the measure in the same period."),
            ("point", "Disbenefits", "Unwanted effects and what was done about them."),
            ("point", "Next review", "The date and the owner."),
            "One page is easy to file with the project records and easy to hand to a council member who asks.",
            ("h", "Mistakes to Avoid"),
            ("point", "Stopping at closing", "Delivery is not the same as benefit."),
            ("point", "No baseline", "Without a starting number, nobody can show improvement."),
            ("point", "No owner", "If the project lead owns the benefit, it ends when the team does."),
            ("point", "Claiming every gain", "Note other changes that could explain the numbers."),
            ("h", "Quick Recap"),
            ("point", "Outputs, outcomes, benefits", "What was made, what changed, and what improved."),
            ("point", "An owner in the operating office", "Named in the handover, with review dates."),
            ("point", "Baseline and target", "Measured at three, six and twelve months."),
            ("point", "Honest attribution", "Compare, list other changes, and report disbenefits too."),
            ("h", "Your Part 39 Action Plan"),
            ("point", "For a closed project", "Write down what it promised, find the baseline, and measure "
             "today’s number."),
            ("point", "For a running project", "Name the benefit owner now and put three review dates in the "
             "calendar."),
            ("point", "For the next business case", "Part 10 asked what a project would gain. Add how and when "
             "that gain will be measured."),
            "The twelve-month review took one page. The council member kept a copy, and at the next budget "
            "hearing asked the same question of two other projects that had closed the year before.",
            ("cta", "Read: Project Management Series, Part 28: Closing the Project, Handover and Lessons Learned", "/blog/project-management-part-28-closing-the-project/"),
            ("cta", "Read: Project Management Series, Part 32: Running a Pilot, Testing Small Before Going Big", "/blog/project-management-part-32-running-a-pilot/"),
            ("cta", "Read: Project Management Series, Part 6: Writing Objectives That Actually Mean Something", "/blog/project-management-part-6-writing-objectives/"),
            ("cta", "Read: Data Analytics Series, Part 35: Correlation Is Not Causation, When Two Numbers Move Together", "/blog/data-analytics-part-35-correlation-and-causation/"),
            ("ask", "Which finished project in your office has never been checked for its benefits?"),
        ],
    },
    {
        "title": "Project Management Series, Part 38: When the Team Disagrees, Five Ways to Handle Conflict",
        "slug": "project-management-part-38-handling-conflict",
        "category": "pm",
        "date": "March 24, 2028",
        "summary": "Disagreements in a project are normal: over priorities, people, time and methods. Handled "
                   "well, they improve the work. Left alone, they stall it. This part explains five common ways "
                   "people respond to conflict, when each one fits, and a short process for settling a work "
                   "disagreement before it grows.",
        "publish_on": "2028-03-24 21:00",
        "body": [
            "The meeting was supposed to take fifteen minutes. It took an hour and settled nothing. The records "
            "clerk wanted the reminder list cleaned before every round. The collector wanted to send on time and "
            "fix wrong numbers afterward. Each was sure the other was slowing the project down.",
            "By the next week they were not speaking, and the reminder round was three days late.",
            "(The project, the people and the disagreement continue the invented example of earlier parts. The "
            "five conflict-handling modes described below come from the cited source.)",
            "Part 37 wrote a procedure so a routine could run without depending on one person. This part deals "
            "with what happens when the people running it disagree. After this post, you will know why "
            "conflict in a project is not always bad, five ways people respond to it, when each one fits, and "
            "a short process a project lead can use to settle a disagreement about the work.",
            ("photo", "blog/pm-conflict.jpg", "Five ways to handle conflict, placed by how much each one pursues "
             "your own concerns and how much it meets the other person’s. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "Why Conflict Is Not Always Bad"),
            "Both people in the story cared about the project. The clerk cared about accuracy. The collector "
            "cared about timing. Their disagreement exposed a real trade-off the plan had not settled.",
            ("point", "Useful conflict", "About the work: what to do first, how to do it, what good enough "
             "means. It can lead to a better plan."),
            ("point", "Harmful conflict", "About the person: blame, tone, old grudges. It slows everything and "
             "does nothing for the work."),
            "The lead’s job is to keep the first kind and stop it from turning into the second.",
            ("h", "Five Ways People Respond"),
            "The Thomas-Kilmann Conflict Mode Instrument describes behavior in conflict along two dimensions. "
            "Assertiveness is the extent to which a person tries to satisfy their own concerns. Cooperativeness "
            "is the extent to which they try to satisfy the other person’s concerns. From these come five "
            "modes.",
            ("point", "Competing", "Assertive and uncooperative. A person pursues their own concerns at the other "
             "person’s expense."),
            ("point", "Accommodating", "Unassertive and cooperative. The person neglects their own concerns to satisfy the other’s."),
            ("point", "Avoiding", "Unassertive and uncooperative. Neither side’s concerns are pursued, at least "
             "for now."),
            ("point", "Collaborating", "Working with the other person to find a solution that fully satisfies "
             "both."),
            ("point", "Compromising", "Finding an expedient, mutually acceptable solution that partially "
             "satisfies both."),
            "The instrument’s publisher presents these as behaviors with appropriate uses, not as personality "
            "types where one is always right. People can use all five.",
            ("h", "When Each One Fits"),
            ("point", "Competing", "When a rule or the law decides it. A collector cannot skip an official "
             "receipt because a taxpayer is in a hurry."),
            ("point", "Accommodating", "When the issue matters far more to the other person than to you, or "
             "when you realize you were wrong."),
            ("point", "Avoiding", "When tempers are high and a short pause will help, or the issue is minor. "
             "Avoiding a real issue for weeks lets it grow."),
            ("point", "Collaborating", "When both concerns are important and there is time to find a better "
             "answer. This was the reminders case."),
            ("point", "Compromising", "When time is short and a partial answer is better than none."),
            ("photo", "blog/pm-conflict-steps.jpg", "A short process for settling a disagreement about the work: "
             "meet early, state the facts, name each need, list options, decide, and write it down. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "A Short Process for Work Disagreements"),
            ("point", "1. Meet early and in private", "The first day it shows, not after a week of silence. "
             "Not in the group chat."),
            ("point", "2. Start with the facts", "“The last round went out three days late. Forty messages "
             "failed.” Facts are easier to agree on than opinions."),
            ("point", "3. Name each person’s need", "The clerk needs accurate numbers. The collector needs to "
             "send on the date taxpayers expect. Say both out loud."),
            ("point", "4. List options together", "At least three, before judging any of them."),
            ("point", "5. Decide, or take it to whoever decides", "If the two cannot agree, the person "
             "accountable in the RACI matrix from Part 8 decides."),
            ("point", "6. Write it down", "Record the decision and the reason in the minutes, as Part 27 "
             "described, or close it in the issue log from Part 26."),
            ("h", "Back to the Reminders"),
            "The project lead met the two of them on Monday morning. The facts were not in dispute: late rounds "
            "and failed messages both hurt the project. The options they listed were cleaning everything first, "
            "sending first and fixing later, and cleaning only the numbers that failed last time.",
            "They chose a fourth one that came up while talking: clean the numbers that failed last round two "
            "days before each send, and send on schedule. The clerk got accuracy where it mattered, and the "
            "collector got his date. That is collaborating: neither side gave up what mattered most to them.",
            ("h", "When the Conflict Is About People"),
            ("point", "Keep it private", "Talk about behavior, not character: “You raised your voice in the "
             "meeting,” not “You are rude.”"),
            ("point", "Listen fully first", "Let each person finish before responding."),
            ("point", "Know when to refer", "Harassment, threats or misconduct are not project issues. They go "
             "to the supervisor or human resources under the office’s rules."),
            ("point", "Look at the workload", "Some friction is tiredness. Part 18 covered assigning people "
             "without overloading them."),
            ("h", "When the Disagreement Crosses Offices"),
            "Some conflicts are not between two people in the team but between two offices, such as the "
            "treasury and the assessor’s office over whose list of property owners is correct.",
            ("point", "Neither lead can decide alone", "Each office answers to its own head, so the RACI matrix "
             "of one project may not bind the other."),
            ("point", "Agree on one shared fact first", "For example, take ten properties and check them "
             "together against the tax declarations. A small shared check calms a large argument."),
            ("point", "Take it up together", "If the two leads cannot settle it, bring it to both heads at "
             "once, with the facts and the options on one page, as Part 34 did for decision makers."),
            ("point", "Put the result in writing", "A short memo signed by both heads keeps the agreement "
             "alive after the people who made it move on."),
            ("h", "Your Own Habits"),
            "Each person leans toward some modes more than others. Think back to your last two disagreements at "
            "work. Did you compete, avoid or accommodate? A lead who notices their own habit can choose a "
            "different mode when the situation calls for it.",
            ("h", "Mistakes to Avoid"),
            ("point", "Waiting for it to pass", "Avoiding a real issue lets it grow."),
            ("point", "Settling it in a group chat", "Talk in person, then write the decision down."),
            ("point", "Always compromising", "Splitting the difference can leave both concerns half met."),
            ("point", "Letting work turn personal", "Keep the talk on facts and needs."),
            ("h", "Quick Recap"),
            ("point", "Conflict about the work can help", "It exposes trade-offs the plan missed."),
            ("point", "Five modes", "Competing, accommodating, avoiding, collaborating and compromising."),
            ("point", "Each has its place", "Match the mode to the situation."),
            ("point", "Six steps", "Early, facts, needs, options, decide, write it down."),
            ("h", "Your Part 38 Action Plan"),
            ("point", "This week", "Think of one disagreement in your section and name which mode each person "
             "used."),
            ("point", "Next disagreement", "Meet early, start with the facts and name each person’s need."),
            ("point", "For your project", "Make sure the RACI matrix names who decides when two people disagree."),
            "The next reminder round went out on its date, with eight failed messages instead of forty. The "
            "clerk and the collector now review the failures together every Friday, which is how the project "
            "lead knew the disagreement was really over.",
            ("cta", "Read: Project Management Series, Part 8: Who Does What? Building a RACI Matrix", "/blog/project-management-part-8-raci-matrix/"),
            ("cta", "Read: Project Management Series, Part 27: Meetings That Decide, Agendas, Minutes and Action Items", "/blog/project-management-part-27-meetings-that-decide/"),
            ("cta", "Read: Project Management Series, Part 26: The Issue Log, Turning Problems Into Next Steps", "/blog/project-management-part-26-issue-log/"),
            ("cta", "Read: Project Management Series, Part 18: Assigning People Without Overloading Them", "/blog/project-management-part-18-resource-allocation/"),
            ("ask", "Which of the five modes do you fall back on most at work?"),
        ],
    },
    {
        "title": "Project Management Series, Part 37: Writing a Standard Operating Procedure People Actually Follow",
        "slug": "project-management-part-37-standard-operating-procedure",
        "category": "pm",
        "date": "March 15, 2028",
        "summary": "When a project ends, some of its work becomes a routine that someone must repeat every month "
                   "or quarter. A standard operating procedure keeps that routine running when people change. "
                   "This part explains what to put in one, how to write steps anyone can follow, how to test "
                   "it, and how to keep it current.",
        "publish_on": "2028-03-15 21:00",
        "body": [
            "The text reminders had worked. On-time payments rose in every barangay, and the project closed "
            "with a handover note, a thank-you and a lessons-learned review. Then, in February, the collector "
            "who had sent every round was moved to the market office.",
            "The March reminders never went out. Nobody had forgotten them. Nobody else knew the small "
            "steps between the taxpayer list and the “Send” button.",
            "(The office, the reminders and the people continue the invented example of earlier parts. The "
            "requirements of the Ease of Doing Business Act cited below are real.)",
            "Part 36 used a Kanban board to keep routine work flowing. This part is about writing that routine "
            "down so it survives a transfer, a leave or a busy month. After this post, you will know how a "
            "standard operating procedure differs from a handover note, what belongs in one, how to write steps "
            "that a newcomer can follow, how to test it, and how to keep it from going stale.",
            ("photo", "blog/pm-sop.jpg", "A standard operating procedure: one routine task, written as numbered "
             "steps with an owner, a trigger, checks and a review date. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "What a Standard Operating Procedure Is"),
            "A standard operating procedure, or SOP, is a written set of steps for one task that is done the "
            "same way every time. It is meant to be followed by whoever is assigned, not only by the person who "
            "wrote it.",
            ("point", "Not a handover note", "Part 28 handed over what continues, and Part 31 kept a one-page "
             "note of where each task stands. A note describes the present. An SOP describes how the task is "
             "done, every time."),
            ("point", "Not a manual", "An SOP covers one task. A binder of everything is rarely opened."),
            ("point", "Not a Citizen’s Charter", "The charter is for the public. The SOP is for the staff "
             "doing the work behind it."),
            ("h", "How It Relates to the Citizen’s Charter"),
            "Republic Act No. 11032, the Ease of Doing Business Act, requires government agencies to keep an "
            "updated Citizen’s Charter. A primer on the law lists what it must show for each service: the "
            "checklist of requirements, the person responsible for each step, the fees, the procedure, the "
            "maximum time to complete the process, and the procedure for filing complaints.",
            "If the public is promised a procedure and a time limit, the staff need a way to deliver it. An SOP "
            "for each charter service turns the public promise into steps someone can follow on a busy day.",
            ("h", "What Goes Into an SOP"),
            ("point", "Title and purpose", "One line each. “Quarterly payment reminders by text: to remind "
             "business owners of the deadline ten days ahead.”"),
            ("point", "Owner", "The position responsible for running it, and a named backup."),
            ("point", "Trigger", "When it runs: a date, a request, or an event."),
            ("point", "What you need", "Files, access, forms and approvals, with where to find each."),
            ("point", "Steps", "Numbered, in order, one action each."),
            ("point", "Checks", "What to verify before moving on, such as a count or a test message."),
            ("point", "Records", "What to save, where, and under what file name."),
            ("point", "What if", "The two or three problems that come up, and what to do."),
            ("point", "Version and review date", "So a reader knows whether it is current."),
            ("h", "Writing Steps People Can Follow"),
            ("point", "Start with a verb", "“Open,” “Filter,” “Copy,” “Send.” Each step is an action."),
            ("point", "One action per step", "“Export the list and remove duplicates” is two steps."),
            ("point", "Use the exact words on the screen", "If the button says “Download as,” write that."),
            ("point", "Give the number to expect", "“The list should have about 600 rows.” A check catches "
             "errors early."),
            ("point", "Add a picture where words fail", "A screenshot of one tricky screen helps more than a "
             "paragraph. Blur any personal data first."),
            ("point", "Write for a newcomer", "Assume the reader knows the office but has never done this task."),
            ("photo", "blog/pm-sop-steps.jpg", "Part of the reminders SOP: each step starts with a verb, does one "
             "thing, and some steps carry a check. Figures are invented. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "The Reminders SOP, Shortened"),
            ("point", "Trigger", "Ten working days before each quarterly deadline."),
            ("point", "Step 1", "Open the business list in the shared drive, file “Business list – current.”"),
            ("point", "Step 2", "Filter to businesses with an unpaid balance for the quarter."),
            ("point", "Step 3", "Check the count against last quarter. A difference of more than a fifth needs "
             "a second look."),
            ("point", "Step 4", "Copy the reference number and mobile number columns to the sending sheet."),
            ("point", "Step 5", "Send a test message to the office phone and read it."),
            ("point", "Step 6", "Get the treasurer’s approval of the message text, in writing."),
            ("point", "Step 7", "Send the round."),
            ("point", "Step 8", "Save the sending report as “Reminders – year – quarter.”"),
            ("point", "What if", "If more than a tenth of messages fail, stop and tell the owner before sending "
             "again."),
            ("h", "Test It With Someone Who Has Never Done It"),
            "An SOP is not finished until someone else has followed it.",
            ("point", "Pick a newcomer", "Someone who knows the office but not this task."),
            ("point", "Watch silently", "Let them follow the steps. Note every question and every pause."),
            ("point", "Fix the gaps", "Each question is a missing step or an unclear word."),
            ("point", "Test again", "Until a person can finish without asking."),
            "The first test of the reminders SOP found four gaps, including the password to the sending "
            "service, which was in the old collector’s notebook. Rule 1 of the baseline in Part 18 of the "
            "Cybersecurity Series, one person, one account, is why the SOP now says who grants access instead "
            "of passing a password along.",
            ("h", "Keeping It Current"),
            ("point", "Give it an owner", "The owner updates it when anything changes."),
            ("point", "Set a review date", "Once a year at least, or after any change in the system it uses."),
            ("point", "Keep a short change log", "Date, what changed, who changed it, as Part 24 did for "
             "project changes."),
            ("point", "Store one copy", "In the shared project kit from Part 30, not in personal folders. "
             "Print copies carry their version date, so an old one is easy to spot."),
            ("h", "Getting People to Use It"),
            "Part 33 showed how to make a new way of working easier than the old one. The same thinking "
            "applies to an SOP.",
            ("point", "Keep it short", "One or two pages. Anything longer is split into smaller SOPs."),
            ("point", "Put it where the work happens", "A link in the shared sheet, or a printed copy at the "
             "desk."),
            ("point", "Use it in training", "New staff learn the task from the SOP, which tests it again."),
            ("h", "Mistakes to Avoid"),
            ("point", "Writing from memory alone", "Write while doing the task, then test it."),
            ("point", "Steps that hide several actions", "One verb, one step."),
            ("point", "No owner or review date", "It will drift out of date unnoticed."),
            ("point", "Passwords in the document", "Name the role that grants access instead."),
            ("h", "Quick Recap"),
            ("point", "One routine, one SOP", "Written so anyone assigned can follow it."),
            ("point", "Verb first, one action, a check", "Steps a newcomer can follow."),
            ("point", "Test with a newcomer", "Every question is a gap to fix."),
            ("point", "Owner and review date", "So it stays current."),
            ("h", "Your Part 37 Action Plan"),
            ("point", "This week", "List the routine tasks in your section that only one person knows how to do."),
            ("point", "Pick one", "Write its SOP while doing the task the next time it runs."),
            ("point", "Test it", "Ask a co-worker to follow it while you watch, then fix the gaps."),
            ("point", "Store it", "Put it in the shared folder with an owner and a review date."),
            "The June reminders went out on time, sent by a clerk who had never done it before. She followed "
            "the eight steps, stopped once at the check in Step 3, found that a filter had been left on, and "
            "fixed it herself. The collector at the market office only heard about it afterward.",
            ("cta", "Read: Project Management Series, Part 28: Closing the Project, Handover and Lessons Learned", "/blog/project-management-part-28-closing-the-project/"),
            ("cta", "Read: Project Management Series, Part 31: Covering for Absences, a Backup Plan So the Work Does Not Stop", "/blog/project-management-part-31-covering-absences/"),
            ("cta", "Read: Project Management Series, Part 30: The Project Kit, Reusable Templates So the Next Project Starts Faster", "/blog/project-management-part-30-project-kit/"),
            ("cta", "Read: Project Management Series, Part 33: Getting People to Use the New Process, Not Just Install It", "/blog/project-management-part-33-adopting-the-new-process/"),
            ("ask", "Which routine in your office would stop if one person were transferred tomorrow?"),
        ],
    },
    {
        "title": "Project Management Series, Part 36: Kanban Boards and Limits on Work in Progress",
        "slug": "project-management-part-36-kanban-boards",
        "category": "pm",
        "date": "March 6, 2028",
        "summary": "Some work never stops arriving: certifications, refund requests, corrections, letters. A "
                   "Kanban board shows that work on one wall, and a limit on work in progress keeps the team "
                   "finishing instead of only starting. This part explains how to set up a simple board, how to "
                   "choose limits, and which four numbers to watch.",
        "publish_on": "2028-03-06 21:00",
        "body": [
            "Every desk in the section had a pile. Each pile held requests that had been started: a "
            "certification half typed, a refund request waiting for a signature, a correction waiting for a "
            "record from another office. Nobody was idle. Yet a taxpayer who asked about a certification filed "
            "two weeks earlier was told, again, “It is being processed.”",
            "The section chief counted. Twenty-three requests were in progress. Four had been finished that "
            "week.",
            "(The section, the requests and the counts are made up for this lesson. The Kanban practices "
            "described below come from the cited guide.)",
            "Part 35 tracked a project with earned value. Not all work is a project with a start and an end. "
            "Some of it is a steady stream of requests. After this post, you will know what a Kanban board is, "
            "how to set one up for a treasury section, why a limit on work in progress speeds things up, and "
            "which four numbers tell you whether the flow is healthy.",
            ("photo", "blog/pm-kanban.jpg", "A Kanban board: columns for each step, one card per request, and "
             "a limit on how many cards each step may hold. Stop starting, start finishing. (Illustration: Butch "
             "Mahinay, aumahinay.dev)", "medium"),
            ("h", "What Kanban Is"),
            "Kanban is a way of managing a flow of work by making it visible and controlling how much is in "
            "progress at once. The Kanban Guide, edition 2025.5 from kanbanguides.org, describes three "
            "practices.",
            ("point", "Defining and visualizing a workflow", "The guide calls the visualization a Kanban board."),
            ("point", "Actively managing items in a workflow", "This includes control of work in progress: Kanban system members “must explicitly control the number "
             "of work items in a workflow from started to finished.”"),
            ("point", "Improving a workflow", "Watch a few measures and adjust how the work flows."),
            "Part 5 compared waterfall, agile and hybrid approaches. Kanban fits work that arrives "
            "continuously, where a fixed plan made months ahead would be wrong by next week.",
            ("h", "Setting Up the Board"),
            "A whiteboard, a wall with sticky notes, or a shared sheet all work. Start with the steps the work "
            "actually goes through.",
            ("point", "Received", "Requests logged but not yet started."),
            ("point", "Checking records", "Someone is pulling the tax declaration, receipts or ledger."),
            ("point", "Waiting", "Blocked by someone outside the section: another office, the taxpayer, a "
             "signature."),
            ("point", "For signature", "Prepared and waiting for the treasurer or an authorized signatory."),
            ("point", "Released", "Done and given to the taxpayer."),
            "One card per request. Write the request type, the taxpayer’s reference number, the date "
            "received and the person working on it. Keep personal details off a board others can see, in "
            "line with the privacy habits in Part 20 of the Cybersecurity Series.",
            ("h", "A Board in a Shared Sheet"),
            "If the section works across two rooms, a shared sheet can stand in for the wall.",
            ("point", "One row per request", "Columns for reference number, request type, current step, "
             "person, date received, date started and date released."),
            ("point", "A count per step", "=COUNTIF(C:C, \"Checking records\"), counting the step column, beside each step’s limit shows "
             "when a column is full."),
            ("point", "Age at a glance", "=TODAY()-F2 in a new column gives each open item’s age. Part 31 of the "
             "Data Analytics Series showed how conditional formatting can color the old ones."),
            ("h", "Why Limit Work in Progress"),
            "Starting feels productive. Finishing is what the taxpayer notices.",
            ("point", "Switching costs time", "A person juggling eight requests spends part of each day "
             "remembering where each one stood."),
            ("point", "Waiting hides", "When half the pile is waiting for another office, nobody sees it as "
             "a problem until a taxpayer complains."),
            ("point", "Queues grow quietly", "If more work starts than finishes, the pile grows every week "
             "even though everyone is busy."),
            "A limit is a simple rule: a column may hold no more than a set number of cards. When it is full, "
            "nobody starts a new request. They help finish one, or clear a blocker, first.",
            ("h", "Choosing the Limits"),
            ("point", "Start from today", "Count the cards now in each column, then set limits a little below "
             "that number."),
            ("point", "Think per person", "With three staff checking records, a limit of four leaves room for "
             "one item that needs two people."),
            ("point", "Limit Waiting too", "A cap on Waiting forces someone to chase the other office instead "
             "of letting requests sit."),
            ("point", "Adjust monthly", "If a column is always empty, the limit may be too low. If the queue "
             "keeps growing, it may be too high."),
            ("photo", "blog/pm-kanban-board.jpg", "The section’s board with limits on each column: when "
             "Checking is full, the next person helps finish instead of starting something new. Figures are "
             "invented. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Four Numbers to Watch"),
            "The Kanban Guide names four flow measures. Each takes a minute to compute from a log of start and "
            "finish dates.",
            ("point", "Work in progress", "The number of items started but not finished. In the story: 23."),
            ("point", "Throughput", "The number finished per unit of time. In the story: 4 a week."),
            ("point", "Work item age", "How long since an unfinished item was started. The certification "
             "from two weeks ago was 14 days old."),
            ("point", "Cycle time", "How long a finished item took from start to finish."),
            "These four connect. If 23 items are in progress and 4 finish each week, a new request can expect "
            "to wait more than five weeks, unless something changes.",
            ("h", "A Short Daily Look"),
            "Once a day, the section stands at the board for ten minutes.",
            ("point", "Read from right to left", "Start with For signature, then Waiting. What is closest to "
             "done gets attention first."),
            ("point", "Ask about the oldest cards", "Any card older than the section’s promise, for example "
             "five working days, is discussed first."),
            ("point", "Name the blockers", "For each card in Waiting, who will follow up, and by when?"),
            "This is not a status meeting. Part 27 described meetings that decide. The daily look decides one "
            "thing: what to finish today.",
            ("h", "What Changed in the Section"),
            ("point", "Limits set", "Checking: 4. Waiting: 5. For signature: 6."),
            ("point", "A signing time", "The treasurer agreed to sign at 11 a.m. and 3 p.m., so cards did not "
             "wait all day."),
            ("point", "A follow-up owner", "One staff member called other offices about every card in Waiting "
             "each morning."),
            ("h", "Kanban Inside a Project"),
            "Kanban is not only for routine requests. A project team can put its work packages from Part 14 on "
            "a board too, with the same limits. The project plan still sets the scope and the dates, and the "
            "board shows what is moving this week.",
            ("h", "Mistakes to Avoid"),
            ("point", "A board nobody updates", "Move the cards when the work moves, or the board lies."),
            ("point", "No limits", "A board without limits only shows the pile more clearly."),
            ("point", "Hiding Waiting inside Checking", "Blocked work needs its own column."),
            ("point", "Personal data on a visible board", "Use reference numbers, not names."),
            ("h", "Quick Recap"),
            ("point", "Make the work visible", "One card per request, one column per step."),
            ("point", "Limit work in progress", "Stop starting, start finishing."),
            ("point", "Watch four numbers", "Work in progress, throughput, age and cycle time."),
            ("point", "Look daily", "Right to left, oldest first, blockers named."),
            ("h", "Your Part 36 Action Plan"),
            ("point", "Today", "List your section’s steps and count what sits in each one."),
            ("point", "This week", "Put up a board, even on paper, and set one limit on the busiest column."),
            ("point", "Next week", "Record start and finish dates, and compute throughput and the oldest item’s "
             "age."),
            "Six weeks later, the section had eleven requests in progress and finished nine a week. The "
            "certification that once waited two weeks now took four working days. Nobody worked longer hours. "
            "They had simply stopped starting more than they could finish.",
            ("cta", "Read: Project Management Series, Part 5: Waterfall, Agile or Hybrid? Choosing How to Run the Work", "/blog/project-management-part-5-waterfall-agile-hybrid/"),
            ("cta", "Read: Project Management Series, Part 26: The Issue Log, Turning Problems Into Next Steps", "/blog/project-management-part-26-issue-log/"),
            ("cta", "Read: Project Management Series, Part 27: Meetings That Decide, Agendas, Minutes and Action Items", "/blog/project-management-part-27-meetings-that-decide/"),
            ("cta", "Read: Project Management Series, Part 35: Earned Value Made Simple, Are We on Budget and on Schedule?", "/blog/project-management-part-35-earned-value/"),
            ("ask", "How many requests are in progress in your section right now, and how many finished last week?"),
        ],
    },
    {
        "title": "Project Management Series, Part 35: Earned Value Made Simple, Are We on Budget and on Schedule?",
        "slug": "project-management-part-35-earned-value",
        "category": "pm",
        "date": "February 25, 2028",
        "summary": "Money spent and days passed do not tell you whether a project is on track. Earned value "
                   "compares three numbers, planned value, earned value and actual cost, to show both schedule "
                   "and budget status. This part explains each one with a treasury example and shows how to "
                   "forecast the final cost.",
        "publish_on": "2028-02-25 21:00",
        "body": [
            "Four weeks into the eight-week rollout, the project lead gave her update to the department head. "
            "“We have spent ₱21,000 of the ₱48,000 budget. That is less than half. We are fine.”",
            "The department head asked how many barangays were finished. Three out of eight. The plan had said "
            "four by now. Spending less than half sounded good, but less than half of the work was done, and "
            "the work done had cost more than planned.",
            "(The project, the office and the figures continue the invented example from Parts 29 to 34. They "
            "describe no real local government.)",
            "Part 34 took a project to decision makers and came back with ₱48,000 approved. This part is about "
            "watching that money once the work starts. By the last section, you will know the three numbers of "
            "earned value, how to compute the two variances and the two indexes, how to measure work fairly, "
            "and how to forecast what the project will cost by the end.",
            ("photo", "blog/pm-earned.jpg", "Earned value: compare what you planned to do, what you actually "
             "did, and what it cost, to see schedule and budget at the same time. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "Why Spending Alone Misleads"),
            "Comparing money spent with the budget answers only one question: how much is left? It cannot "
            "say whether the money bought the work it was supposed to buy.",
            ("point", "Underspending can be bad news", "If the work is behind, less money goes out simply "
             "because less work has been done."),
            ("point", "Overspending can be fine", "If the team is ahead of schedule, spending more than planned "
             "by this date may be expected."),
            "Earned value adds the missing piece: the value of the work actually completed.",
            ("h", "The Three Numbers"),
            "The Project Management Institute describes earned value with three basic measures.",
            ("point", "Planned value (PV)", "The budgeted cost of the work scheduled to be done by now."),
            ("point", "Earned value (EV)", "The budgeted cost of the work actually completed by now. It is "
             "measured at planned cost, not by hours worked or money spent."),
            ("point", "Actual cost (AC)", "What was really spent on the work performed."),
            "All three are in pesos, at the same date. That is what lets you compare them.",
            ("h", "The Example"),
            "The rollout sends text reminders to businesses in eight barangays. Each barangay is one work "
            "package: check and clean its phone list, load it into the texting service, and send the first "
            "round. Each package is budgeted at ₱6,000, for a total budget of ₱48,000. The plan finishes one "
            "barangay a week.",
            ("point", "Planned value at week 4", "Four barangays scheduled × ₱6,000 = ₱24,000."),
            ("point", "Earned value at week 4", "Three barangays finished × ₱6,000 = ₱18,000. The fourth is "
             "half done, but it is not counted yet. More on that below."),
            ("point", "Actual cost at week 4", "₱21,000, from the purchase records and the overtime sheet."),
            ("h", "Two Variances"),
            ("point", "Schedule variance = EV − PV", "₱18,000 − ₱24,000 = −₱6,000. Negative means behind "
             "schedule: one barangay’s worth of work."),
            ("point", "Cost variance = EV − AC", "₱18,000 − ₱21,000 = −₱3,000. Negative means over budget: "
             "the finished work cost ₱3,000 more than planned."),
            ("h", "Two Indexes"),
            "Variances are in pesos. Indexes turn them into ratios, which are easier to compare across "
            "projects of different sizes.",
            ("point", "Schedule performance index, SPI = EV ÷ PV", "₱18,000 ÷ ₱24,000 = 0.75. The team is "
             "completing work at 75 percent of the planned pace."),
            ("point", "Cost performance index, CPI = EV ÷ AC", "₱18,000 ÷ ₱21,000 = 0.86. Each peso spent is "
             "producing about 86 centavos of planned work."),
            "In PMI’s guide to reading the numbers, an index at or above 1.0 is favorable, and below 1.0 is a "
            "warning.",
            "Read the two indexes together, because each tells half the story.",
            ("point", "Both at 1.0 or above", "On schedule and within budget. Keep measuring."),
            ("point", "SPI low, CPI fine", "The work is slow but not expensive. Look for waiting, missing "
             "people or blocked tasks."),
            ("point", "SPI fine, CPI low", "The work is moving but costing too much. Look at overtime, prices "
             "and rework."),
            ("point", "Both low", "The rollout’s case. Find the shared cause first."),
            ("photo", "blog/pm-earned-chart.jpg", "Week 4 of the rollout: planned value, earned value and "
             "actual cost on one chart, with the gaps that show schedule and cost variance. Figures are "
             "invented. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Forecasting the Final Cost"),
            "If the work keeps costing what it has cost so far, the project will not finish at ₱48,000.",
            ("point", "Estimate at completion", "One simple forecast divides the total budget by the CPI: "
             "₱48,000 ÷ (₱18,000 ÷ ₱21,000) = ₱56,000."),
            ("point", "What it means", "At the current rate, the project needs about ₱8,000 more than "
             "approved."),
            ("point", "What it does not mean", "It is a forecast, not a fate. If the cause of the overrun has "
             "been fixed, the rest of the work may cost what was planned."),
            "This is the number that turns a vague worry into a decision: find savings, ask for more money, or "
            "cut scope, using the change control process from Part 24.",
            ("h", "Measuring Work Fairly"),
            "Earned value depends on how you count “done.” Generous guesses make every project look healthy "
            "until the last week.",
            ("point", "Use the 0/100 rule for small packages", "A package earns nothing until it is finished, "
             "then earns its full budget. The half-done fourth barangay earns ₱0 today."),
            ("point", "Use 50/50 if packages are long", "Half the budget when the work starts, the other half "
             "when it finishes. Choose one rule and keep it."),
            ("point", "Keep packages small", "Part 14 broke work into packages. Small packages make earned "
             "value honest, because few things sit at “90 percent done” for weeks."),
            ("point", "Record actual cost by package", "Purchases, overtime and load for the texting service, "
             "each tagged to its barangay, as Part 17 set up the budget."),
            ("h", "What the Numbers Told the Team"),
            "Looking at the three finished barangays, the team found the cause. Phone lists in the first two "
            "had many outdated numbers, which took extra overtime to clean. The stale-list risk from Part 32 had "
            "come true.",
            ("point", "Schedule", "Two collectors now clean the next barangay’s list a week ahead, so loading "
             "and sending is not delayed."),
            ("point", "Cost", "The overtime rate was replaced by work during regular hours on two quiet "
             "afternoons a week."),
            ("point", "Report", "The status report from Part 25 now shows SPI and CPI each week, beside the "
             "plain-language summary."),
            ("h", "Mistakes to Avoid"),
            ("point", "Comparing spending only with the budget", "Add the value of work done."),
            ("point", "Counting half-finished work generously", "Pick the 0/100 or 50/50 rule."),
            ("point", "Waiting until the end to compute", "Earned value is useful only while there is time to "
             "act."),
            ("point", "Hiding a bad CPI", "Report it early, with the cause and the fix."),
            ("h", "Quick Recap"),
            ("point", "Three numbers", "Planned value, earned value and actual cost, all in pesos."),
            ("point", "Two variances", "EV − PV for schedule, EV − AC for cost."),
            ("point", "Two indexes", "SPI and CPI, where below 1.0 is a warning."),
            ("point", "One forecast", "Budget ÷ CPI estimates the final cost."),
            ("h", "Your Part 35 Action Plan"),
            ("point", "Pick one current project", "Write its total budget and its work packages with "
             "budgets."),
            ("point", "Compute this week’s PV, EV and AC", "Use the 0/100 rule."),
            ("point", "Find SPI and CPI", "If either is below 1.0, find the cause before the next meeting."),
            ("point", "Forecast the final cost", "Share it with your sponsor, with one line on what you are "
             "doing about it."),
            "At week 8, the rollout finished all eight barangays at a total cost of ₱52,500. That was over "
            "budget, but ₱3,500 less than the week-4 forecast, and the department head had known about it for "
            "a month instead of a day.",
            ("cta", "Read: Project Management Series, Part 17: The Project Budget, Built Package by Package", "/blog/project-management-part-17-project-budget/"),
            ("cta", "Read: Project Management Series, Part 25: The Status Report, One Page That Tells the Truth Early", "/blog/project-management-part-25-status-reports/"),
            ("cta", "Read: Project Management Series, Part 14: The Work Breakdown Structure, One Bite at a Time", "/blog/project-management-part-14-work-breakdown-structure/"),
            ("cta", "Read: Project Management Series, Part 24: Change Control, Saying Yes to a Change Without Losing the Plan", "/blog/project-management-part-24-change-control/"),
            ("ask", "Does your office compare spending with the work actually finished, or only with the budget?"),
        ],
    },
    {
        "date": "February 16, 2028",
        "title": "Project Management Series, Part 34: Presenting a Project to Decision Makers in Ten Minutes",
        "slug": "project-management-part-34-presenting-in-ten-minutes",
        "category": "pm",
        "summary": "A project may get only ten minutes on a crowded agenda. This part shows how "
                   "to open with the decision you need, build a short presentation around one question, "
                   "prepare for the hard questions, and leave with a recorded decision instead of “let’s "
                   "discuss next time.”",
        "publish_on": "2028-02-16 21:00",
        "body": [
            "The project lead had twenty slides. They covered the background, the method, the pilot, the "
            "adoption numbers and a timeline for the whole year. The council committee gave her ten minutes, "
            "the fourth item on a long agenda.",
            "By slide nine, two members were checking their phones. At minute ten, the chair thanked her and "
            "moved to the next item. Nobody had decided anything, and the funding for text reminders in the "
            "other barangays waited another month.",
            "(The office, the committee and the project continue the invented example from Parts 29 to 33. "
            "They describe no real local government.)",
            "Part 33 made sure people actually use a new process. This part is about the meeting where a "
            "project asks for something: money, people, approval or a change. You will learn how to start "
            "with the decision, how to fit the story into ten minutes, what to put on each slide or page, "
            "how to prepare for questions, and how to make sure the decision is recorded.",
            ("photo", "blog/pm-present.jpg", "Presenting in ten minutes: start with the ask, show the "
             "evidence, name the risk, and leave with a recorded decision. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "Start With the Decision You Need"),
            "Before making a single slide, write one sentence: “I am asking the committee to …” If you cannot "
            "finish that sentence, the presentation is not ready.",
            ("point", "A clear ask", "“Approve ₱48,000 to extend text reminders to all barangays from July.”"),
            ("point", "Not a clear ask", "“Update the committee on the reminders project.” An update without "
             "an ask can end with nothing decided."),
            ("point", "Say it first", "Put the ask in the first minute, not at the end. Decision makers then "
             "listen to the rest as evidence for or against it."),
            "Part 10 built a business case for approval. A ten-minute presentation is that business case, "
            "spoken, with the least important parts taken out.",
            ("h", "Know Who Is Listening"),
            "A committee is a group of people with different concerns and different questions. Spend fifteen minutes before the "
            "meeting thinking about each one.",
            ("point", "What each member cares about", "One watches the budget. One hears complaints from "
             "market vendors. One asks about the barangays in a particular district. Part 3 mapped "
             "stakeholders this way."),
            ("point", "What they already know", "If they approved the pilot, they do not need the background "
             "again. Start where they left off."),
            ("point", "Talk to one or two beforehand", "A short visit to the chair or the member who asks the "
             "hardest questions can surface a concern you can answer before the meeting, not during it."),
            "Shape the evidence around those concerns. A member worried about cost hears the cost early. A "
            "member worried about complaints hears that the pilot had one complaint, and why.",
            ("h", "A Ten-Minute Shape"),
            "Five parts, in this order, work for a typical request.",
            ("point", "1. The ask (1 minute)", "What you want, how much, and by when."),
            ("point", "2. The problem (2 minutes)", "In the listeners’ terms. “Last year, in the pilot barangay, 42 "
             "percent of businesses paid the quarter late.”"),
            ("point", "3. The evidence (3 minutes)", "What you tried and what happened. The pilot from "
             "Part 32: on-time payment rose from 58 to 78 percent in one barangay, while the others barely "
             "moved."),
            ("point", "4. The cost and the risk (2 minutes)", "What it costs, what could go wrong, and how "
             "you will handle it. The stale phone list, and the fix."),
            ("point", "5. The ask again (1 minute)", "Repeat the decision you need, with the date."),
            "That leaves one minute of slack. Use it. Meetings run late, and the committee may give you "
            "eight minutes instead of ten.",
            ("photo", "blog/pm-present-plan.jpg", "Ten minutes, five parts: the ask comes first and last, "
             "and the evidence gets the most time. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "One Page, or Five Slides"),
            "Fewer slides force clearer thinking. For ten minutes, five slides or a one-page handout is "
            "enough.",
            ("point", "One message per slide", "Write the message as the slide title: “Reminders raised "
             "on-time payment by 20 points,” not “Pilot Results.”"),
            ("point", "One chart, not three", "Part 27 of the Data Analytics Series explained how to choose "
             "the right chart. Pick the one that proves the message."),
            ("point", "Numbers they can check", "Give the start and the end, as Part 30 of the Data "
             "Analytics Series recommended: “from 58 to 78 percent,” not only “up 20 points.”"),
            ("point", "A one-page handout", "Some members prefer paper. The same five parts on one page let "
             "them read ahead or follow along."),
            ("h", "Prepare for the Hard Questions"),
            "The questions decide more than the slides do. Write down the five questions you least want to "
            "hear, and answer each in two sentences.",
            ("point", "“Why not do it for all barangays at once?”", "Because the pilot showed the phone list "
             "needed fixing first."),
            ("point", "“What if it doesn’t work elsewhere?”", "The rollout has a check after one quarter, "
             "with the same targets."),
            ("point", "“Where does the money come from?”", "Know the budget line, and whether it needs a "
             "supplemental appropriation. If you are not sure, say who will confirm it and by when."),
            ("point", "“What happens if we say no?”", "Be honest. The office continues as before, with the "
             "late payment rate it had last year."),
            "If you do not know an answer, say so, and promise a written reply by a specific date. A guess "
            "that turns out wrong costs more trust than “I will confirm and send it by Friday.”",
            ("h", "Rehearse With a Timer"),
            ("point", "Say it aloud", "Ten minutes in your head can easily become fifteen out loud."),
            ("point", "Cut, then cut again", "If it runs long, remove detail from the evidence, never the ask."),
            ("point", "Practice with a colleague", "Ask them to interrupt with one hard question halfway "
             "through."),
            ("h", "Leave With a Recorded Decision"),
            "Part 27 showed how minutes turn a meeting into decisions and action items. Before you sit "
            "down, make sure the decision has a place in them.",
            ("point", "Ask for the decision directly", "“May I ask the committee to approve, defer or "
             "decline today?”"),
            ("point", "If it is deferred, ask what is missing", "And when it will be taken up again."),
            ("point", "Confirm it in writing", "Send a short note the same day: what was decided, by whom, "
             "and the next step."),
            ("quote", "If the decision is not in the minutes, it was not made."),
            ("h", "Mistakes to Avoid"),
            ("point", "Saving the ask for the end", "Say it in the first minute."),
            ("point", "Twenty slides for ten minutes", "Five slides, one message each."),
            ("point", "Guessing at a hard question", "Promise a written answer by a date."),
            ("point", "Leaving without a decision", "Ask for approve, defer or decline, and confirm in writing."),
            ("h", "Quick Recap"),
            ("point", "Ask first", "One sentence, said in the first minute."),
            ("point", "Five parts", "Ask, problem, evidence, cost and risk, ask again."),
            ("point", "Prepare the hard questions", "Two-sentence answers, written in advance."),
            ("point", "Get it recorded", "In the minutes, and in a same-day note."),
            ("h", "Your Part 34 Action Plan"),
            ("point", "Write the sentence", "“I am asking … to …” for your next project request."),
            ("point", "Fill the five parts", "On one page, with the minutes beside each."),
            ("point", "List five hard questions", "And answer each in two sentences."),
            ("point", "Rehearse once with a timer", "And cut until it fits in nine minutes."),
            "A month later, the project lead returned to the committee with five slides and a one-page "
            "handout. She stated the ask in the first sentence. The chair asked about the phone list, and "
            "she had the answer ready. At minute eight, the committee approved the funding, and the "
            "secretary read the decision back for the minutes.",
            ("cta", "Read: Project Management Series, Part 10: Writing a Business Case That Gets a Yes", "/blog/project-management-part-10-business-case/"),
            ("cta", "Read: Project Management Series, Part 27: Meetings That Decide, Agendas, Minutes and Action Items", "/blog/project-management-part-27-meetings-that-decide/"),
            ("cta", "Read: Project Management Series, Part 32: Running a Pilot, Testing Small Before Going Big", "/blog/project-management-part-32-running-a-pilot/"),
            ("cta", "Read: Data Analytics Series, Part 27: Choosing the Right Chart, Starting From the Question", "/blog/data-analytics-part-27-choosing-the-right-chart/"),
            ("ask", "What is the one sentence you would say first if you had ten minutes with your decision makers?"),
        ],
    },
    {
        "date": "February 7, 2028",
        "title": "Project Management Series, Part 33: Getting People to Use the New Process, Not Just Install It",
        "slug": "project-management-part-33-adopting-the-new-process",
        "category": "pm",
        "summary": "A new process can be finished, approved and launched, and still not be used. This part "
                   "covers why people hold on to the old way, how to make the new way easier than the old, "
                   "how to support people in the first weeks, how to measure real use, and when to retire "
                   "the old way.",
        "publish_on": "2028-02-07 21:00",
        "body": [
            "The new payment plan register went live on a Monday. It was a shared sheet with one row per "
            "stallholder, the agreed terms written out, and a column for each installment. It replaced the "
            "notebook in the market supervisor’s drawer, the one that had caused trouble in Part 31.",
            "Three weeks later, the project lead checked the register against the receipts. Only half of the "
            "installments paid that month had been entered. The rest were still in the notebook, which was "
            "back in the drawer.",
            "(The office, the people and the register continue the invented example from Parts 29 to 32. "
            "They describe no real local government.)",
            "Part 32 tested a change with a pilot. This part deals with what comes after the decision to "
            "use it: getting people to change how they work. You will learn why people hold on to the old "
            "way, how to make the new way easier, who to involve early, how to support the first weeks, how "
            "to measure whether the change is really being used, and when to retire the old way.",
            ("photo", "blog/pm-adopt.jpg", "Adopting a new process: explain why, make it easier than the old "
             "way, support the first weeks, measure real use, and set a date for the old way to end. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Launched Is Not the Same as Used"),
            "A project plan can say “register launched, March 1” and mark the task done. But the benefit the "
            "project promised, payment plans anyone can look up, arrives only when people use the register "
            "every day. Part 28 closed projects with a handover. This part is about the weeks after the "
            "handover, when the new way either becomes normal or quietly fades.",
            ("h", "Why People Hold On to the Old Way"),
            "When the project lead asked, the reasons were ordinary and fair.",
            ("point", "It was more work", "Staff wrote the payment in the notebook out of habit, then had to "
             "type it into the register too. Two entries for one payment."),
            ("point", "Nobody asked them", "The collectors had not seen the register before launch day, and "
             "one column used a term they did not use."),
            ("point", "Fear of mistakes", "A notebook entry can be crossed out quietly. A shared sheet shows "
             "every edit, and one collector worried about being blamed for a typo."),
            ("point", "The old way still worked", "The notebook was still there. As long as it was, it was "
             "the easier choice."),
            "None of these is stubbornness. Each is a problem the project can fix.",
            ("h", "Step 1: Explain the Why in Their Terms"),
            "“The register improves transparency” means little at a busy counter. “When you are on leave, "
            "nobody has to call you about a stallholder’s plan” means a lot. Explain the change by what it "
            "does for the person doing the work, and for the taxpayer at the window.",
            ("h", "Step 2: Make the New Way Easier Than the Old"),
            "If the new way takes more effort, the old way wins. Look for every extra step and remove it.",
            ("point", "Remove double entry", "The project lead agreed that payments go into the register "
             "only. The notebook stopped being a required record."),
            ("point", "Fix the confusing parts", "The column the collectors did not understand was renamed "
             "in their words."),
            ("point", "Put it where the work happens", "A shortcut to the register was added to the "
             "market office computer, under each collector’s own sign-in."),
            ("h", "Step 3: Involve People Early, and Use Champions"),
            "Ask one or two people who will use the process to try it before launch and suggest changes. "
            "They become champions: colleagues others can ask without feeling they are bothering the boss.",
            ("point", "Pick respected users", "Not necessarily the most senior, but people others go to for "
             "help."),
            ("point", "Give them time", "Being a champion is extra work. Say so, and adjust their load, as "
             "Part 18 recommended."),
            ("h", "Step 4: Support the First Weeks"),
            ("point", "Train by doing", "Short sessions at the actual counter, with real entries, are worth "
             "more than a long talk in the conference room."),
            ("point", "A one-page guide", "The steps, with pictures, taped where the work happens."),
            ("point", "A person to ask", "Name who answers questions during the first month, and when they "
             "are available."),
            ("point", "Treat mistakes kindly", "Correct an entry together, without blame. Fear of being "
             "blamed was one of the reasons for the notebook."),
            ("h", "Step 5: Tell People What Changed, and Listen"),
            "Part 11 built a communication plan for the project. Adoption needs its own short version.",
            ("point", "Before launch", "Who is affected, what changes for them, from what date, and who to ask."),
            ("point", "Each week of the first month", "A two-line update: what was fixed, and what is next. "
             "When people see their complaints turn into fixes, they learn that speaking up works."),
            ("point", "A place for feedback", "A sheet or a box where anyone can write what is hard. Read it "
             "every week, and answer each item, even if the answer is “not yet.”"),
            ("h", "Step 6: Measure Real Use"),
            "Ask whether the new process is used, not only whether it is installed. Pick one number you can "
            "check each week.",
            ("point", "The measure", "The share of installments paid that week that appear in the register, "
             "checked against the official receipts."),
            ("point", "The target", "At least 95 percent by week 8."),
            ("point", "Look for the stall", "In this example, use rose to about half by week 3 and stopped. A "
             "flat line is a signal to ask why, not a reason to give up."),
            ("photo", "blog/pm-adopt-curve.jpg", "Weekly use of the new register: a stall at week 3, a jump "
             "after double entry was removed, and the old notebook retired at week 8. Figures are invented. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Step 7: Retire the Old Way, With a Date"),
            "As long as the old way is still available, some people will use it. Once the new way works and "
            "people have had support, set a date and announce it.",
            ("point", "Announce the date", "“From May 1, the register is the only record of payment plans.”"),
            ("point", "Move what is left", "Copy any remaining plans from the notebook into the register, and "
             "have a second person check them."),
            ("point", "Keep the old record safely", "Store the notebook as a record, following your office’s "
             "rules on keeping documents. Do not throw it away."),
            ("quote", "If the old way is still easier, it will still be used."),
            ("h", "Mistakes to Avoid"),
            ("point", "Calling it done at launch", "Measure use for at least the first two months."),
            ("point", "Adding work without removing any", "Every new step should replace an old one."),
            ("point", "Blaming people for resisting", "Ask for reasons, and fix them."),
            ("point", "Keeping the old way forever", "Set a date to retire it."),
            ("h", "Quick Recap"),
            ("point", "Launched is not used", "The benefit comes only with daily use."),
            ("point", "Easier wins", "Remove double entry and confusing steps."),
            ("point", "Support and measure", "Champions, a guide, a person to ask, one weekly number."),
            ("point", "Retire the old way", "With a date, a careful transfer and a stored record."),
            ("h", "Your Part 33 Action Plan"),
            ("point", "Pick one change", "A process your office launched in the last year."),
            ("point", "Measure it", "Find one number that shows whether it is really used."),
            ("point", "Ask three users", "What makes the new way harder than the old one? Write down the answers."),
            ("point", "Fix one thing", "Remove the biggest extra step, then measure again in two weeks."),
            "In week 8, the market supervisor came back from a seminar and asked the clerk about a "
            "stallholder’s plan. She opened the register on the office computer and read it to him. He asked where his "
            "notebook was. It was in the records room, labeled and boxed, and he did not ask for it again.",
            ("cta", "Read: Project Management Series, Part 32: Running a Pilot, Testing Small Before Going Big", "/blog/project-management-part-32-running-a-pilot/"),
            ("cta", "Read: Project Management Series, Part 31: Covering for Absences, a Backup Plan So the Work Does Not Stop", "/blog/project-management-part-31-covering-absences/"),
            ("cta", "Read: Project Management Series, Part 28: Closing the Project, Handover and Lessons Learned", "/blog/project-management-part-28-closing-the-project/"),
            ("cta", "Read: Project Management Series, Part 11: The Communication Plan, Who Hears What, When", "/blog/project-management-part-11-communication-plan/"),
            ("ask", "What new process in your office was launched but never quite used, and why?"),
        ],
    },
    {
        "date": "January 28, 2028",
        "title": "Project Management Series, Part 32: Running a Pilot, Testing Small Before Going Big",
        "slug": "project-management-part-32-running-a-pilot",
        "category": "pm",
        "summary": "A pilot tries a new way of working with a small group, for a fixed time, against targets "
                   "set in advance. This part shows how to choose the pilot group, write the success "
                   "criteria before the start, compare fairly, and decide at the end whether to scale, "
                   "adjust or stop.",
        "publish_on": "2028-01-28 21:00",
        "body": [
            "The phone numbers had been cleaned, and the text reminders were ready to go. The councilor who "
            "had asked for them wanted every business in town to get a reminder before the next quarterly "
            "deadline. The project lead asked for something smaller first: one barangay, one deadline, and "
            "a written answer at the end to the question “did it work?”",
            "The councilor agreed, a little impatiently. Three weeks later, the pilot found a problem that "
            "would have reached every business in town.",
            "(The office, the reminders and every number below continue the invented example from Part 29. "
            "They describe no real local government.)",
            "Part 31 kept a project moving when someone is away. This part covers a way to start a change "
            "without betting everything on it. You will learn what a pilot is and when it helps, how to "
            "choose where to run it, why the targets must be written before the start, how to compare "
            "fairly, and how to make the decision to scale, adjust or stop.",
            ("photo", "blog/pm-pilot.jpg", "Running a pilot: a small group, a fixed time, targets written "
             "first, and a clear decision at the end. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "What a Pilot Is"),
            "A pilot is a small, time-limited trial of a new process, tool or service, run with real people "
            "in real conditions, to learn whether it works before it is used everywhere.",
            ("point", "Small", "One barangay, one section of the market, one window, one kind of permit."),
            ("point", "Time-limited", "A start date and an end date, set in advance."),
            ("point", "Real", "Actual taxpayers and actual deadlines, not a demonstration in the conference room."),
            ("point", "Decided", "It ends with a written decision, not with the trial quietly becoming the "
             "new normal."),
            "A pilot is not a test of whether the software runs. Part 23 covered quality checks of that kind. A "
            "pilot tests whether the change does what it was meant to do for the people it serves.",
            ("h", "When a Pilot Helps"),
            ("point", "The change affects many people", "A mistake in a reminder sent to every business "
             "costs more than one sent to a hundred."),
            ("point", "Nobody knows how people will react", "Will taxpayers read a text? Will they call the "
             "office instead? Only trying will tell."),
            ("point", "It costs money or time to undo", "Printed forms, new equipment, a changed procedure."),
            "A pilot is not needed for every change. Moving a sign or fixing a typo on a form can simply be "
            "done.",
            ("h", "Step 1: Write the Question and the Targets First"),
            "Before the first reminder went out, the project lead wrote a one-page pilot plan. It answered "
            "one question: “Do text reminders three days before the deadline increase on-time payment of the "
            "quarterly business tax?”",
            ("point", "On-time payment", "Last year, 70 of the 120 businesses in the pilot barangay paid the "
             "same quarter on time, or 58 percent. Target: at least 90 of 120, or 75 percent."),
            ("point", "Delivery", "No more than 5 percent of messages failing to reach a working number."),
            ("point", "Staff time", "No more than three hours of staff time for the whole pilot."),
            ("point", "Complaints", "No more than two complaints about the messages."),
            "The targets were written and signed before the start, for the same reason Part 29 set the "
            "weights before scoring: a target chosen after the results are in can be bent to fit them.",
            ("h", "Step 2: Choose Where, and Who to Compare With"),
            ("point", "Choose a typical group", "The project lead chose a barangay with a mix of small "
             "stores and larger businesses, not the one with the best payment record. A pilot run where it is "
             "easiest can succeed and still fail everywhere else."),
            ("point", "Keep a comparison group", "The other barangays got no reminders during the pilot. If "
             "on-time payment rose everywhere, the reminders could not take the credit. Part 13 of the Data "
             "Analytics Series explains how bias can creep into a comparison like this."),
            ("point", "Respect consent and privacy", "Messages went only to numbers that business owners had "
             "given the office for notices, and contained no amounts or account details."),
            ("h", "Step 3: Run It, and Write Things Down"),
            "During the pilot, the clerk kept a simple log: messages sent, messages that failed, calls "
            "received, and anything unexpected. The issue log from Part 26 works for this.",
            "On the second day, the log showed something the plan had not expected. Nine of the 120 messages "
            "had failed. Some numbers had been changed since the cleanup, and two belonged to former owners "
            "of businesses that had closed.",
            "The project lead resisted the urge to fix the list in the middle of the pilot. Changing the "
            "process halfway would have made the results hard to read. Instead, the failures were logged, the "
            "affected owners were reached by phone or by a visit so nobody missed the deadline because of the "
            "pilot, and the fix waited for the decision.",
            ("h", "Step 4: Compare the Results With the Targets"),
            ("photo", "blog/pm-pilot-results.jpg", "The pilot scorecard: targets written before the start, "
             "results after, and the decision that follows. Figures are invented. (Illustration: Butch "
             "Mahinay, aumahinay.dev)", "medium"),
            ("point", "On-time payment", "94 of 120, or 78 percent. Target met. In the comparison barangays, "
             "on-time payment moved from 59 to 61 percent, so most of the gain in the pilot barangay is "
             "likely due to the reminders, not to the season."),
            ("point", "Delivery", "9 of 120 messages failed, or 7.5 percent. Target missed."),
            ("point", "Staff time", "Two and a half hours. Target met."),
            ("point", "Complaints", "One, from a former owner whose business had closed. Target met."),
            ("h", "Step 5: Decide: Scale, Adjust or Stop"),
            "A pilot ends with one of three decisions, written down with the reason.",
            ("point", "Scale", "The targets were met. Roll it out, with the lessons learned."),
            ("point", "Adjust", "The idea works, but something needs fixing first. Fix it, and if the fix is "
             "large, run a second, shorter pilot."),
            ("point", "Stop", "The targets were clearly missed, or the cost was too high. Stopping is a "
             "valid result. The pilot saved the office from a larger failure."),
            "The decision here was to adjust. The reminders worked, but the phone list was going stale. The "
            "office added a step: each business owner confirms the number when renewing the permit, and the "
            "closure process from Part 14 of Inside the Local Treasury now removes the number. The reminders "
            "were scheduled for all barangays at the next quarter.",
            ("quote", "A pilot that finds a problem has done its job. The failure it prevents is the one you "
             "never see."),
            ("h", "Mistakes to Avoid"),
            ("point", "Setting targets after the results", "Write them down and sign them first."),
            ("point", "Choosing the easiest site", "Pick a typical one."),
            ("point", "No comparison group", "Without one, you can’t tell the pilot from the season."),
            ("point", "A pilot with no end date", "It drifts into permanent use without a decision."),
            ("h", "Quick Recap"),
            ("point", "Small, short and real", "One group, a fixed period, real conditions."),
            ("point", "Targets first", "Written before the start, on one page."),
            ("point", "Compare fairly", "A typical site, and a group without the change."),
            ("point", "End with a decision", "Scale, adjust or stop, with the reason."),
            ("h", "Your Part 32 Action Plan"),
            ("point", "Pick a change", "Choose one change your office is considering."),
            ("point", "Write the question", "In one sentence, with the result you hope to see."),
            ("point", "Set three or four targets", "Each with a number, and the baseline you will compare it with."),
            ("point", "Set the dates", "A start, an end, and the day the decision will be made."),
            "When the councilor saw the results, he asked why the office had not simply sent the reminders "
            "to everyone at once. The project lead showed him the nine failed messages. Across the whole "
            "town, it would have been dozens, and some would have gone to people who had closed their "
            "businesses years ago.",
            ("cta", "Read: Project Management Series, Part 29: Too Many Requests? Choosing the Next Project With a Scoring Matrix", "/blog/project-management-part-29-scoring-matrix/"),
            ("cta", "Read: Project Management Series, Part 26: The Issue Log, Turning Problems Into Next Steps", "/blog/project-management-part-26-issue-log/"),
            ("cta", "Read: Project Management Series, Part 23: Quality Planning, Deciding What Good Enough Means", "/blog/project-management-part-23-quality-planning/"),
            ("cta", "Read: Data Analytics Series, Part 13: Bias in Data, and How to Catch It", "/blog/data-analytics-part-13-bias-in-data/"),
            ("ask", "What change in your office would you test with a small group first?"),
        ],
    },
    {
        "date": "January 19, 2028",
        "title": "Project Management Series, Part 31: Covering for Absences, a Backup Plan So the Work Does Not Stop",
        "slug": "project-management-part-31-covering-absences",
        "category": "pm",
        "summary": "When the one person who knows a task goes on leave, the task can stop with them. This part "
                   "shows how to find those single points of failure, build a simple cross-training grid, "
                   "write a handover note, give a backup the right access without sharing passwords, and test "
                   "the plan before anyone is away.",
        "publish_on": "2028-01-19 21:00",
        "body": [
            "The arrears drive was in its third week when the market supervisor’s daughter was rushed to the "
            "hospital. He was on leave for five days. On the second day, three stallholders came to the "
            "treasury to settle their arrears under the payment plans he had arranged. Nobody else knew the "
            "terms. The plans were in a notebook in his drawer, and the drawer was locked.",
            "The stallholders went home. Two of them did not come back that month.",
            "(The office, the people and the arrears drive continue the invented example from Part 29. They "
            "describe no real local government.)",
            "Part 30 built a project kit so the next project starts faster. This part keeps a running project "
            "moving when someone is away. You will learn how to find the tasks that depend on one person, how "
            "to map who can cover what, what a good handover note contains, how to give a backup access "
            "safely, and how to test the plan while everyone is still at work.",
            ("photo", "blog/pm-backup.jpg", "Covering for absences: find the one-person tasks, name a backup "
             "for each, write it down, and practice before anyone leaves. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "Why Absences Stop Projects"),
            "People get sick, take leave, attend trainings and get reassigned. None of that is a surprise. "
            "What causes the trouble is a task that only one person can do.",
            ("point", "Knowledge in one head", "The payment plan terms were agreed in conversations and kept "
             "in one notebook."),
            ("point", "Access in one account", "Only one person can open the folder, the system or the drawer."),
            ("point", "Decisions waiting for one person", "Nobody else is allowed to approve, so the work "
             "waits."),
            ("quote", "A task that only one person can do is a risk, even when that person is excellent."),
            "Part 19 introduced the risk register. “Key person unavailable” belongs on it, with this part as "
            "the response.",
            ("h", "Step 1: Find the One-Person Tasks"),
            "Take the project’s task list or work breakdown structure from Part 14. For each task that will "
            "run in the next month, ask two questions.",
            ("point", "Who can do this today?", "Write every name, not only the person assigned."),
            ("point", "What happens if it waits a week?", "Some tasks can wait. Collecting from a stallholder "
             "who came in person cannot."),
            "Any task with one name and a high cost of waiting is a single point of failure. In the arrears "
            "drive, the clerk found three: applying the payment plan terms, updating the arrears list, and "
            "signing the weekly summary.",
            ("h", "Step 2: Build a Cross-Training Grid"),
            "Draw a small table. Tasks go down the side, people across the top. In each cell, write P for the "
            "primary person, B for the backup, and leave it blank if that person has not learned the task.",
            ("point", "Every important task needs a B", "One backup per task is the minimum."),
            ("point", "Spread the backups", "If one person is the backup for everything, that person becomes "
             "the next single point of failure."),
            ("point", "Look at the columns too", "A column full of P’s shows a person carrying too much, the "
             "overload that Part 18 warned about."),
            "The arrears drive grid showed the supervisor as P on four tasks and nobody as B on three of them. "
            "The clerk became B for the payment plans, a market collector became B for the arrears list, and "
            "the head of office agreed to sign the weekly summary whenever the supervisor was away.",
            ("photo", "blog/pm-backup-grid.jpg", "The arrears drive grid after the review: every task has a "
             "named backup. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Step 3: Write the Handover Note Before It Is Needed"),
            "A handover note is one page that lets the backup continue without calling the person on leave. "
            "Keep it updated weekly, not only when leave is filed.",
            ("point", "Status", "Where each task stands today, in one or two lines."),
            ("point", "Next steps", "What must happen this week, with dates."),
            ("point", "Where things are", "The folder, the file names, the logbook, the drawer and who holds "
             "its key."),
            ("point", "Rules and agreements", "The payment plan terms, written out, not only remembered."),
            ("point", "Pending decisions", "What is waiting, and who may decide in the person’s absence."),
            ("point", "Contacts", "The stallholders, suppliers or offices the backup may need to call."),
            "Store it where the project files are, as Part 30 suggested, not in a personal email or chat.",
            ("h", "Step 4: Give Access the Right Way"),
            "The quickest fix can seem to be sharing a password. It is also the wrong one.",
            ("point", "Do not share passwords", "Shared passwords make it impossible to tell who did what, and "
             "they keep working after the person who borrowed them has moved on. Rule 1 of the one-page "
             "baseline in Part 18 of the Cybersecurity Series is “one person, one account.”"),
            ("point", "Give the backup their own access", "Add the backup to the shared folder or system "
             "with their own account, in advance, at the level the task needs."),
            ("point", "Follow the turnover rules for accountable items", "Cash, official receipts and accountable "
             "forms are not handed over informally. Follow your office’s procedure for turning them over, with "
             "a count and a signed record. Parts 11 and 12 of Inside the Local Treasury explain why these items "
             "are tracked so closely, and what a shortage means for the person accountable."),
            ("h", "Step 5: Agree Who Decides"),
            "Some tasks are not blocked by knowledge but by authority. Before anyone is away, agree in "
            "writing who may decide what.",
            ("point", "Routine decisions", "The backup may apply agreed rules, such as an existing payment "
             "plan."),
            ("point", "New decisions", "A new payment plan or an exception goes to a named alternate, or waits."),
            ("point", "Signatures", "If a document needs a specific officer’s signature, check your office’s "
             "rules on who may sign in that officer’s absence. Do not assume."),
            ("h", "Step 6: Test the Plan While Everyone Is Present"),
            "A backup who has never done the task is a name on paper. Test the plan before it is needed.",
            ("point", "Let the backup do it once", "With the primary person nearby to answer questions."),
            ("point", "Use the handover note only", "If the backup gets stuck, the note is missing something. "
             "Fix the note."),
            ("point", "Repeat after changes", "When the task changes, the backup practices again."),
            "The clerk applied two payment plans with the supervisor watching. She found that the notebook "
            "did not say what happened when a stallholder paid more than the installment. That rule went into "
            "the handover note the same day.",
            ("h", "Mistakes to Avoid"),
            ("point", "Waiting for the leave form", "Write the backup plan before anyone files for leave."),
            ("point", "Sharing passwords", "Give each backup their own access."),
            ("point", "One backup for everything", "Spread the backups across the team."),
            ("point", "Never testing", "Let each backup do the task once while the primary is present."),
            ("h", "Quick Recap"),
            ("point", "Find the one-person tasks", "One name plus a high cost of waiting."),
            ("point", "Use a P-and-B grid", "Every important task needs a backup."),
            ("point", "Keep a handover note", "Status, next steps, locations, rules, decisions, contacts."),
            ("point", "Test it", "A backup who has practiced is a real backup."),
            ("h", "Your Part 31 Exercise"),
            "Take the work you are responsible for this month.",
            ("point", "List your tasks", "Mark each one that only you can do today."),
            ("point", "Pick a backup for one", "The task that would hurt most if it waited a week."),
            ("point", "Write the note and practice", "One page, then let your backup do the task once with you "
             "nearby."),
            "Then ask your backup what was unclear. Their questions are the gaps in your note. Fill "
            "them in, and do the same for the next task on your list next month. One task at a time, "
            "the grid fills in over the following months, without a big training program.",
            "Two months later, the supervisor took a week of vacation leave. When a stallholder came in to "
            "pay, the clerk opened the handover note, applied the plan, and sent the stallholder to the cashier for the official receipt. The "
            "supervisor heard about it on his return, from the stallholder, who said the treasury had been "
            "easy to deal with.",
            ("cta", "Read: Project Management Series, Part 30: The Project Kit, Reusable Templates So the Next Project Starts Faster", "/blog/project-management-part-30-project-kit/"),
            ("cta", "Read: Project Management Series, Part 18: Assigning People Without Overloading Them", "/blog/project-management-part-18-resource-allocation/"),
            ("cta", "Read: Project Management Series, Part 19: The Risk Register, Planning for What Could Go Wrong", "/blog/project-management-part-19-risk-register/"),
            ("cta", "Read: Cybersecurity Series, Part 18: A One-Page Security Baseline for a Small Office", "/blog/cybersecurity-part-18-small-office-baseline/"),
            ("ask", "Which task in your office stops when one person is on leave?"),
        ],
    },
    {
        "date": "January 10, 2028",
        "title": "Project Management Series, Part 30: The Project Kit, Reusable Templates So the Next Project Starts Faster",
        "slug": "project-management-part-30-project-kit",
        "category": "pm",
        "summary": "Every project in this series produced a document worth keeping. This part shows how to "
                   "turn them into a small project kit: which templates to include, how to strip and label "
                   "them, where to keep them, who looks after them, and how to scale the kit down for a "
                   "small project.",
        "publish_on": "2028-01-10 21:00",
        "body": [
            "The day after the head of office approved two new projects, the clerk opened a blank document "
            "to write the first charter. Then she stopped. Somewhere on the shared drive was the charter "
            "from the notices project, with headings she had argued over for an afternoon. There was also a "
            "risk register, an issue log, a status report everyone had learned to read, and a closing "
            "report. She spent forty minutes searching folders named “New Folder (3)” and “FINAL final” "
            "before she found most of them.",
            "The market supervisor, starting the arrears drive the same week, did not search at all. He "
            "started from blank pages.",
            "(The office, its people and its projects are invented for this series. They describe no real "
            "local government.)",
            "Part 29 chose the next projects. This part makes sure they do not start from zero. By the end, "
            "you will know which documents from Parts 1 to 29 belong in a project kit, how to turn a used "
            "document into a clean template, how to name and store the kit so people can find it, who "
            "should look after it, and how to use only part of it when a project is small.",
            ("photo", "blog/pm-kit.jpg", "The project kit: a small set of templates, one shared folder, one "
             "owner, and a note on which pieces a small project needs. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "What a Project Kit Is"),
            "A project kit is a short set of blank, ready-to-use documents that every new project in the "
            "office starts from. It is not a manual and not a software purchase. It is a folder.",
            ("point", "It saves time", "The headings, the columns and the examples are already there. A "
             "new project fills in blanks instead of designing a form."),
            ("point", "It keeps documents comparable", "When every status report has the same layout, the "
             "head of office can read three projects in the time it once took to read one."),
            ("point", "It carries lessons forward", "The closing report in Part 28 listed what to repeat. "
             "A template is one of the easiest places to put a lesson where the next team will see it."),
            ("quote", "A good template is a lesson learned that nobody has to remember."),
            ("h", "Step 1: Gather What You Already Have"),
            "Start with the documents your last project actually used, not with a list from a textbook. "
            "The clerk’s list, matched to the parts of this series, came to ten.",
            ("point", "Before the work", "Project charter (Part 2), stakeholder map (Part 3), scope "
             "statement (Part 4), RACI matrix (Part 8) and business case (Part 10)."),
            ("point", "Planning", "Work breakdown structure and schedule (Parts 14 to 16), budget (Part 17) "
             "and risk register (Part 19)."),
            ("point", "While the work runs", "Status report (Part 25), issue log (Part 26), change request "
             "(Part 24) and meeting agenda with minutes (Part 27)."),
            ("point", "At the end", "Closing report with lessons learned (Part 28)."),
            "That is more than ten if you count every one. She merged the scope statement into the charter "
            "and the budget into the schedule sheet, which brought the kit to ten files.",
            ("h", "Step 2: Strip Each Document Into a Template"),
            "A used document is full of one project’s details. A template keeps the structure and removes "
            "the content.",
            ("point", "Keep the headings and columns", "These were the hard part, and they are what the "
             "next project needs."),
            ("point", "Replace content with prompts", "Instead of the old objective, write “One sentence: "
             "what will be different, by how much, by when (see Part 6).”"),
            ("point", "Keep one short example", "A single sample row in the risk register or the issue log "
             "shows how much detail is expected. Mark it clearly as an example."),
            ("point", "Remove personal data", "Names of taxpayers, phone numbers and account details from "
             "the old project must not travel into a template. Part 20 of the Cybersecurity Series covers "
             "privacy at work."),
            ("h", "Step 3: Name Files So People Can Find Them"),
            "A file named “charter final v2 revised” helps nobody six months later. Agree on one pattern "
            "and use it everywhere.",
            ("point", "Number the templates in order of use", "“01 Charter”, “02 Stakeholder map” and so on "
             "up to “10 Closing report”. Sorting by name then shows them in the order a project needs them."),
            ("point", "Name project copies with the project and date", "For example, “Arrears drive – 03 "
             "RACI – 2027-04”. Writing the date as year, month and day keeps files in date order when "
             "sorted."),
            ("point", "Put a version on the template itself", "A line at the top such as “Template version "
             "2, April 2027” tells a user whether they have the latest one."),
            ("h", "Step 4: Store It in One Place"),
            ("point", "One shared folder", "On the office drive or the cloud storage your office already "
             "uses. Two copies of a kit soon become two different kits."),
            ("point", "Templates are read-only", "Users make a copy for their project and work on the copy. "
             "If anyone can edit the template, someone eventually will, by accident."),
            ("point", "A short read-me file", "Half a page: what each template is for, which part of a "
             "project uses it, and who to ask."),
            ("h", "Step 5: Give the Kit an Owner"),
            "A kit with no owner slowly goes out of date. Name one person, with a backup.",
            ("point", "Collects suggestions", "Anyone who finds a missing column or a confusing heading "
             "tells the owner, not just their own team."),
            ("point", "Updates after each closing report", "When a project closes, the owner reads its "
             "lessons learned and asks one question: should a template change because of this?"),
            ("point", "Announces changes", "A one-line message is enough: “Status report template, version 3: "
             "added a row for decisions needed from the head of office.”"),
            ("h", "Step 6: Scale It to the Project"),
            "Not every project needs ten documents. Forcing a one-month task through every template can make people avoid the kit.",
            ("point", "Small project, a few weeks, one team", "Charter, task list with dates, issue log and a "
             "short closing note. Four files."),
            ("point", "Medium project, a few months, two or more units", "Add the stakeholder map, RACI, "
             "risk register, status report and meeting minutes."),
            ("point", "Large or costly project", "Use all ten, including the business case, the budget and "
             "the change request."),
            "Write these three levels in the read-me file, so that the decision is quick and does not "
            "depend on who is asked.",
            ("h", "Mistakes to Avoid"),
            ("point", "Building templates nobody used", "Start from documents that worked on a real project."),
            ("point", "Leaving old project data inside", "Strip names, numbers and taxpayer details."),
            ("point", "Letting everyone edit the master", "Keep the templates read-only and work on copies."),
            ("point", "Requiring every file for every project", "Match the kit to the size of the work."),
            ("h", "Quick Recap"),
            ("point", "A kit is a folder", "Ten or so templates from your own past project."),
            ("point", "Structure stays, content goes", "Headings, columns, prompts and one marked example."),
            ("point", "One place, one owner", "Read-only templates, a read-me and someone who updates them."),
            ("point", "Scale to size", "Four files for a small project, all ten for a large one."),
            ("h", "Your Part 30 Exercise"),
            "Find the documents from the last project you worked on, finished or not.",
            ("point", "Pick three", "The charter, the issue log and the status report are a good start."),
            ("point", "Strip them", "Keep the headings, replace the content with prompts, remove personal "
             "data, and add one marked example."),
            ("point", "Name and store them", "Number them, put them in one shared folder, and make them "
             "read-only."),
            "Then give the folder to the next person who starts a project, and ask what was missing. Their "
            "answer is the first update to your kit.",
            "The market supervisor received the kit link on a Tuesday and copied the charter template that "
            "afternoon. It took him one hour instead of the morning he had spent on a blank page. At the "
            "bottom of the issue log template, he found a line the clerk had added from the last closing "
            "report: “Agree on who closes an issue before you open the first one.” He did.",
            ("cta", "Read: Project Management Series, Part 29: Too Many Requests? Choosing the Next Project With a Scoring Matrix", "/blog/project-management-part-29-scoring-matrix/"),
            ("cta", "Read: Project Management Series, Part 28: Closing the Project, Handover and Lessons Learned", "/blog/project-management-part-28-closing-the-project/"),
            ("cta", "Read: Project Management Series, Part 2: The Project Charter on One Page", "/blog/project-management-part-2-project-charter/"),
            ("cta", "Read: Project Management Series, Part 26: The Issue Log, Turning Problems Into Next Steps", "/blog/project-management-part-26-issue-log/"),
            ("ask", "Which document from your last project would save the next team the most time if it were already a template?"),
        ],
    },
    {
        "date": "December 31, 2027",
        "title": "Project Management Series, Part 29: Too Many Requests? Choosing the Next Project With a Scoring Matrix",
        "slug": "project-management-part-29-scoring-matrix",
        "category": "pm",
        "summary": "After one project closes, five more ideas arrive at once. This part shows how to choose "
                   "among them with a simple scoring matrix: agree on criteria and weights, score each idea, "
                   "check the result against capacity, and explain the choice to the people whose ideas wait.",
        "publish_on": "2027-12-31 21:00",
        "body": [
            "A week after the notices project closed, the head of office had five new ideas on her desk. A "
            "councilor wanted the text reminders that had been delayed to this year. The market supervisor "
            "wanted a drive to collect stall arrears. The records clerk wanted the old property tax cards "
            "scanned. Someone had suggested an online appointment system for permits, and the cashiers "
            "wanted queue numbers at the windows. Each idea had a supporter, and each supporter believed "
            "theirs should go first.",
            "The office had people for two projects at most.",
            "(The office, its ideas and every score below are invented for this lesson. They describe no "
            "real local government.)",
            "Part 28 closed a project. This part chooses the next one. By the end, you will know why "
            "choosing needs a written method, how to build a scoring matrix with criteria and weights, how "
            "to score honestly, how to check the result against the people you have, and how to explain "
            "the decision so the ideas that wait are not simply forgotten.",
            ("photo", "blog/pm-scoring.jpg", "Choosing the next project: agree on the criteria, weigh them, "
             "score each idea, then check capacity before deciding. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "Why Choosing Needs a Method"),
            "Without a method, the next project can be chosen by whoever asks loudest, most recently or "
            "most senior. That is not always the idea that helps the office most.",
            ("point", "It makes the reasons visible", "Everyone can see why one idea went first."),
            ("point", "It separates the idea from the person", "The scores judge the work, not the one who "
             "proposed it."),
            ("point", "It can be repeated", "Next quarter, the same criteria rank the next set of ideas."),
            ("quote", "Saying yes to everything is the same as saying no to finishing anything."),
            ("h", "Step 1: Agree on the Criteria"),
            "Choose three to five questions that matter to your office, and agree on them before looking at "
            "any idea. The head of office and the clerk chose four.",
            ("point", "Benefit", "How much does it help taxpayers or collections? 5 means a large, clear "
             "benefit; 1 means a small one."),
            ("point", "Urgency", "Is there a deadline, a legal requirement or a cost of waiting? 5 means it "
             "cannot wait; 1 means it can."),
            ("point", "Effort", "How much work and money does it take? Scored in reverse: 5 means little "
             "effort, 1 means a great deal, so that a higher score is always better."),
            ("point", "Readiness", "Are the data, people and approvals already in place? 5 means ready to "
             "start; 1 means much is missing."),
            "Write a one-line meaning for 1, 3 and 5 on each criterion. Without them, two people can give "
            "the same idea a 2 and a 4 and both be right.",
            ("h", "Step 2: Give Each Criterion a Weight"),
            "Not every criterion matters equally. A weight says how much.",
            ("point", "The office’s weights", "Benefit 3, Urgency 2, Effort 2, Readiness 1. The weights add "
             "up to 8, so the highest possible score is 8 times 5, or 40."),
            ("point", "Set them first", "Agree on the weights before scoring. Changing them afterward to "
             "move a favorite idea up defeats the purpose."),
            ("point", "Link them to the goals", "If the office’s plan for the year stresses collections, "
             "benefit to collections deserves the heaviest weight."),
            ("h", "Step 3: Score Each Idea"),
            "Each idea gets a score from 1 to 5 on each criterion. Multiply each score by its weight and add.",
            ("point", "Clean phone numbers, then text reminders", "Benefit 4, Urgency 4, Effort 4, Readiness "
             "5. Weighted: 12 + 8 + 8 + 5 = 33. The change request from Part 24 had already measured it."),
            ("point", "Market arrears drive", "Benefit 5, Urgency 3, Effort 3, Readiness 4. Weighted: "
             "15 + 6 + 6 + 4 = 31."),
            ("point", "Queue numbers at the windows", "Benefit 3, Urgency 3, Effort 4, Readiness 4. Weighted: "
             "9 + 6 + 8 + 4 = 27."),
            ("point", "Scan the old property tax cards", "Benefit 5, Urgency 2, Effort 1, Readiness 3. "
             "Weighted: 15 + 4 + 2 + 3 = 24."),
            ("point", "Online appointments for permits", "Benefit 4, Urgency 2, Effort 2, Readiness 2. "
             "Weighted: 12 + 4 + 4 + 2 = 22."),
            "Score with at least two people, separately, then compare. Where the scores differ by more than "
            "one point, talk about why. The discussion can teach more than the number.",
            ("h", "Step 4: Check Against Capacity"),
            "A ranking is not a plan until it meets the people available. Part 18 showed how to assign "
            "people without overloading them.",
            ("point", "Count the people", "The office could spare one encoder and the clerk for one project, "
             "and the market staff for another."),
            ("point", "Check for clashes", "The phone number project needs the encoder; the arrears drive "
             "needs the market collectors. They do not compete for the same people, so both can run."),
            ("point", "Watch the calendar", "Avoid starting a project that needs the cashiers during the "
             "January rush described in Part 2 of Inside the Local Treasury."),
            ("h", "Step 5: Decide, and Look Again at the Numbers"),
            "The matrix informs the decision. It does not make it. The head of office looked at the top "
            "two and asked three questions.",
            ("point", "Does the order make sense?", "If the top idea feels wrong, find out which score or "
             "weight is causing it. Either the score is wrong, or the feeling is."),
            ("point", "Are any ideas linked?", "Clean phone numbers could later help the appointment "
             "system send reminders. Doing the first now makes the fifth easier later."),
            ("point", "Is anything required by law or audit?", "An item required by a rule or an audit "
             "finding may need to go first, whatever its score. Mark it that way rather than bending the "
             "scores."),
            "She approved the phone number project and the arrears drive. Each got a one-page charter, as "
            "in Part 2.",
            ("h", "Step 6: Tell Everyone, Including Those Who Wait"),
            ("point", "Share the matrix", "Send the scores and the decision to everyone who proposed an idea."),
            ("point", "Say what waits, and until when", "“Queue numbers: next review in July.” An idea with a "
             "date is waiting; an idea without one has been dropped."),
            ("point", "Invite corrections", "If someone thinks a score is wrong, ask for the facts. A better "
             "estimate can change the order next time."),
            ("h", "Keep the Matrix Small"),
            ("point", "Few criteria", "Three to five. More than that, and every idea scores about the same."),
            ("point", "One sheet", "A row per idea, a column per criterion, a weighted total, and a notes "
             "column for the reasons."),
            ("point", "Review on a schedule", "Once a quarter, add new ideas, rescore the waiting ones, and "
             "decide again."),
            ("h", "Mistakes to Avoid"),
            ("point", "Choosing weights after scoring", "Agree on the weights first."),
            ("point", "Scoring alone", "Two people, scoring separately, then compare."),
            ("point", "Ignoring capacity", "The top two must have people to do them."),
            ("point", "Silence for the ideas that wait", "Give each one a review date."),
            ("h", "Quick Recap"),
            ("point", "Criteria first", "Three to five, each with a meaning for 1, 3 and 5."),
            ("point", "Weights before scores", "So the result cannot be steered."),
            ("point", "Capacity decides how many", "The ranking decides which."),
            ("point", "Explain the choice", "Share the matrix and give waiting ideas a date."),
            ("h", "Your Part 29 Exercise"),
            "List every idea or request waiting in your office, even the informal ones.",
            ("point", "Pick criteria and weights", "Use the four here, or your own, and agree on them with "
             "your head of office."),
            ("point", "Score them", "With one colleague, separately, then compare."),
            ("point", "Check capacity", "Choose only as many as you have people for."),
            "Then send the result to the people who proposed each idea. Notice how the conversation changes "
            "when the reasons are written down.",
            "The councilor saw his text reminders at the top of the list and called the clerk the same day. "
            "The cashiers saw queue numbers in third place, with a July review date, and asked what would "
            "move the score. They came back a week later with a quote from a supplier, and a better "
            "readiness score.",
            ("cta", "Read: Project Management Series, Part 28: Closing the Project, Handover and Lessons Learned", "/blog/project-management-part-28-closing-the-project/"),
            ("cta", "Read: Project Management Series, Part 10: Writing a Business Case That Gets a Yes", "/blog/project-management-part-10-business-case/"),
            ("cta", "Read: Project Management Series, Part 18: Assigning People Without Overloading Them", "/blog/project-management-part-18-resource-allocation/"),
            ("cta", "Read: Project Management Series, Part 24: Change Control, Saying Yes to a Change Without Losing the Plan", "/blog/project-management-part-24-change-control/"),
            ("ask", "How was the last project in your office chosen, and could anyone explain why it went first?"),
        ],
    },
    {
        "date": "December 22, 2027",
        "title": "Project Management Series, Part 28: Closing the Project, Handover and Lessons Learned",
        "slug": "project-management-part-28-closing-the-project",
        "category": "pm",
        "summary": "A project that simply stops is not closed. This part shows how to finish properly: "
                   "confirm the objectives against the charter, hand over what continues, close the logs "
                   "and the budget, hold a lessons-learned review that changes the next project, and thank "
                   "the people who did the work.",
        "publish_on": "2027-12-22 21:00",
        "body": [
            "The last batch of notices went out on a Friday. On Monday, the runners were back at their "
            "regular work, the clerk was at the counter, and the project folder sat on a shelf. Six "
            "weeks later, a taxpayer came in with a notice in hand and asked to settle. Nobody could say "
            "which list the notice came from, who had kept the returned envelopes, or whether the "
            "eleven wrong addresses had ever been corrected in the records.",
            "The work had been done. The project had never been closed.",
            "(The project, the office and every number in this story are imagined for teaching. No real "
            "office or taxpayer appears here.)",
            "This series has followed one project, the round of delinquency notices, from its charter in "
            "Part 2 through change requests, status reports, issues and meetings. This part is about the "
            "end. You will learn how to check the results against the charter, hand over the work that "
            "continues, close the logs and the budget, run a lessons-learned review, and write a short "
            "closing report that the next project manager can actually use.",
            ("photo", "blog/pm-closing.jpg", "Closing a project: check the objectives, hand over what "
             "continues, close the logs, and learn from the work before the team moves on. "
             "(Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Why Closing Matters"),
            "When the main work ends, people return to their usual jobs, and the project’s loose ends "
            "become nobody’s job. Closing is a short set of steps that ties them off.",
            ("point", "Someone owns what continues", "Payments arriving because of the notices, returned "
             "envelopes, and corrections to addresses all need an owner after the project."),
            ("point", "The records can be found", "The list used, the delivery log, and the decisions made "
             "should be in one place, under a name anyone can search for."),
            ("point", "The sponsor signs off", "A formal end tells the office the resources are free and "
             "the objectives were met, or were not."),
            ("point", "The next project starts smarter", "What went well and what did not is written down "
             "while people still remember."),
            ("quote", "A project ends twice: once when the work stops, and again when someone writes down "
             "what it taught."),
            ("h", "Step 1: Check the Results Against the Charter"),
            "Take out the one-page charter from Part 2 and the objectives from Part 6. For each objective, "
            "write what was planned, what happened, and the evidence.",
            ("point", "Delivered on time?", "Planned: all 1,800 notices delivered by the end date in the "
             "approved 45-working-day schedule from Part 18. Result: 1,789 delivered, two days after that "
             "date because of the San Roque delay, and 11 listed as undelivered with a reason. Evidence: "
             "the delivery log."),
            ("point", "Within budget?", "Compare the budget from Part 17 with the actual spending, "
             "including the overtime approved in the meeting from Part 27."),
            ("point", "Quality met?", "Use the checks from Part 23. Here, eleven notices came back with "
             "wrong addresses, and the quality plan’s limit decides whether that was acceptable."),
            ("point", "Approved changes", "List every change from the change log in Part 24, so the "
             "results are judged against the plan as it was finally approved, not the first draft."),
            "Be honest where the result fell short. An objective missed by two days, with the reason "
            "written down, is more useful to the next project than a report that says everything went "
            "well.",
            ("h", "Step 2: Hand Over What Continues"),
            "Some work does not end with the project. It moves to the people who do it every day.",
            ("point", "List it", "Payments that will arrive because of the notices, the eleven addresses "
             "to correct, the returned envelopes to file, and taxpayers who asked for a payment plan."),
            ("point", "Name an owner for each", "The cashier for payments, the records clerk for "
             "addresses, and so on. Use the RACI matrix from Part 8 to check nobody was forgotten."),
            ("point", "Hand over in writing", "A one-page note to each owner: what is left, where the "
             "files are, and whom to ask. Ask each owner to confirm they received it."),
            ("h", "Step 3: Close the Logs and the Budget"),
            ("point", "Risk register", "Close the risks that can no longer happen. Any that still could, "
             "such as complaints about the notices, go to the owner who will handle them."),
            ("point", "Issue log", "Every open issue from Part 26 is either closed, with how it was "
             "resolved, or handed over with a named owner."),
            ("point", "Change log", "Mark it final. It explains why the project ended differently from "
             "the first plan."),
            ("point", "Budget", "Record the final cost, return or cancel what was not used, and make "
             "sure all claims are settled under the office’s usual rules."),
            ("point", "Files", "Put everything in one folder named with the project and the end date, "
             "following the naming habits from Part 15 of the Data Analytics series. Taxpayer lists hold "
             "personal data, so keep them only where access is limited."),
            ("h", "Step 4: The Lessons-Learned Review"),
            "A lessons-learned review is a short meeting, held soon after the work ends, while the details "
            "are fresh. Invite the people who did the work, not only those who managed it. The runners "
            "know things the clerk does not.",
            ("point", "Three questions", "What went well and should be repeated? What went wrong, and why? "
             "What would we do differently next time?"),
            ("point", "Facts before opinions", "Start with the timeline: planned dates, actual dates, and "
             "the issues that caused the gaps. Opinions are easier to agree on once the facts are on the "
             "table."),
            ("point", "Problems, not people", "Ask what in the plan, the process or the tools allowed a "
             "problem to happen. If a runner fell sick, the lesson is about backup, not about the runner."),
            ("point", "Turn each lesson into an action", "“Address data was poor” is a complaint. “Check "
             "a sample of addresses against the assessor’s records before printing” is a lesson someone "
             "can use."),
            "Use the meeting habits from Part 27: an agenda written as questions, a timekeeper, and "
            "minutes sent the same day. Keep the list of lessons short. Five that change the next project "
            "are worth more than thirty that nobody reads.",
            ("h", "Step 5: The Closing Report on One Page"),
            ("point", "Objectives and results", "The table from Step 1, with evidence."),
            ("point", "Cost and time", "Planned against actual."),
            ("point", "Handover", "What continues, and who owns each item."),
            ("point", "Top lessons", "Three to five, each written as an action."),
            ("point", "Sign-off", "The sponsor’s signature and date, confirming the project is closed."),
            "File it with the charter, so the next person who opens the folder sees the beginning and the "
            "end side by side.",
            ("h", "Step 6: Thank the People"),
            "The runners walked to every barangay. The encoders corrected addresses. The cashier took the "
            "extra payments. A short note from the sponsor naming what each group did costs nothing and "
            "is remembered. If the office has a regular meeting, say it there too.",
            ("h", "The Clerk’s Closing"),
            "In this version of the story, the clerk closed the project properly. She checked the results "
            "against the charter: 1,789 of 1,800 notices delivered, two days late, within the budget "
            "after the approved overtime. She handed the eleven addresses to the records clerk and the "
            "returned envelopes to the files. The lessons-learned review took forty minutes and produced "
            "four lessons. The first one read: “Check addresses before printing, not after delivery.” "
            "The head of office signed the one-page closing report the same week.",
            "Six weeks later, when the taxpayer came in with a notice, the cashier opened the project "
            "folder, found the list and the delivery date in a minute, and took the payment.",
            ("h", "Mistakes to Avoid"),
            ("point", "Letting the project fade out", "Set a closing date and a sign-off."),
            ("point", "No owner for what continues", "Hand each item over in writing."),
            ("point", "A review that blames people", "Look for causes in the process and the plan."),
            ("point", "Lessons nobody reads", "Write them as actions, and read them at the next kickoff."),
            ("h", "Quick Recap"),
            ("point", "Check against the charter", "Planned, actual and evidence, including approved changes."),
            ("point", "Hand over in writing", "Every continuing task gets a named owner."),
            ("point", "Close every log", "Risks, issues, changes, budget and files."),
            ("point", "Learn and thank", "A short review, a one-page report, and credit to the people who did the work."),
            ("h", "Your Part 28 Exercise"),
            "Pick a project or task force your office finished in the last year, even an informal one.",
            ("point", "Find the loose ends", "List anything still open from it, and who, if anyone, owns "
             "each item."),
            ("point", "Write three lessons", "Each as an action someone could take on the next project."),
            ("point", "Draft the one-page report", "Objectives, results, handover and lessons."),
            "Then put a closing step into the plan of your current project, with a date, so it is "
            "scheduled before the work ends.",
            ("cta", "Read: Project Management Series, Part 2: The Project Charter on One Page", "/blog/project-management-part-2-project-charter/"),
            ("cta", "Read: Project Management Series, Part 27: Meetings That Decide, Agendas, Minutes and Action Items", "/blog/project-management-part-27-meetings-that-decide/"),
            ("cta", "Read: Project Management Series, Part 26: The Issue Log, Turning Problems Into Next Steps", "/blog/project-management-part-26-issue-log/"),
            ("cta", "Read: Project Management Series, Part 6: Writing Objectives That Actually Mean Something", "/blog/project-management-part-6-writing-objectives/"),
            ("ask", "What is still open from the last project your office finished, and who owns it?"),
        ],
    },
    {
        "date": "December 13, 2027",
        "title": "Project Management Series, Part 27: Meetings That Decide, Agendas, Minutes and Action Items",
        "slug": "project-management-part-27-meetings-that-decide",
        "category": "pm",
        "summary": "A project meeting is worth its hour only if something is decided or unblocked. This part "
                   "shows how to decide whether to meet at all, write an agenda that ends in decisions, run "
                   "the hour, and send short minutes with owners and dates the same day.",
        "publish_on": "2027-12-13 21:00",
        "body": [
            "The weekly project meeting started at two and ended at four. Six people attended. Everyone gave "
            "an update, the encoders described their week in detail, and a long discussion about envelope "
            "colors went nowhere. As the room emptied, the head of office asked the clerk, “So, did we approve the overtime for the address corrections or not?” Nobody was sure. Two hours, six people, twelve "
            "person-hours, and the one decision that mattered was still open.",
            "(The office, the meeting and the people in it are invented. They stand for no real workplace.)",
            "Part 26 kept problems in one log. This part is about the hour when people gather to deal with "
            "them. By the end, you will know how to decide whether a meeting is needed, how to write an "
            "agenda that leads to decisions, how to run the meeting so it ends on time, and how to write "
            "minutes that people act on.",
            ("photo", "blog/pm-meetings.jpg", "Meetings that decide: a reason to meet, an agenda of "
             "questions, a timekeeper, and minutes with owners and dates sent the same day. (Illustration: "
             "Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "First, Should You Meet?"),
            "A meeting can be a costly way to share information, because everyone’s time is spent at once. Before calling one, ask what it is for.",
            ("point", "To share status", "A written report can do this. The one-page status report from Part 25 shares status, and people read it when they can."),
            ("point", "To decide", "A meeting can help when several people must weigh options together and "
             "agree."),
            ("point", "To solve a problem", "A meeting can help when an issue in the log from Part 26 needs "
             "several people’s knowledge at once."),
            ("point", "To start or close", "The kickoff from Part 7 and the closing review are worth meeting "
             "for, because people need to hear the same thing at the same time."),
            ("quote", "If nothing needs to be decided, it may not need to be a meeting."),
            ("h", "An Agenda Written as Questions"),
            "An agenda that lists topics invites discussion. An agenda that lists questions invites answers.",
            ("point", "Topic", "“Delivery schedule.” People talk until the time runs out."),
            ("point", "Question", "“Do we approve four hours of overtime for two encoders to finish the address corrections, yes or no?” The item ends when the question is answered."),
            "For each item, write the question, who presents it, how many minutes it gets, and what the group "
            "should leave with: a decision, a list of options, or an owner. Send the agenda at least a day "
            "ahead, with any papers attached, so people arrive having read them.",
            ("h", "Who Should Be There"),
            ("point", "The decider", "If the meeting is for a decision, the person with the authority from "
             "the charter must attend, or the decision waits."),
            ("point", "The people with the facts", "For each item, whoever knows the numbers."),
            ("point", "Not everyone", "People who only need the outcome can read the minutes. The RACI matrix "
             "from Part 8 helps: those marked Informed can read the minutes instead."),
            ("h", "Running the Hour"),
            ("point", "Start on time", "Waiting for latecomers punishes the people who came on time."),
            ("point", "Decisions first", "Put the items that need the decider at the top, in case they must "
             "leave early."),
            ("point", "A timekeeper", "One person watches the minutes per item and says when time is up."),
            ("point", "A parking lot", "Good ideas that are off the agenda go on a list for later, not into "
             "the current item. The envelope colors belonged there."),
            ("point", "Say the decision aloud", "Before moving on, the chair states what was decided, who "
             "owns it and by when. If nobody can say it in one sentence, it was not decided."),
            ("point", "Read back the actions", "In the last five minutes, the note-taker reads every action item aloud with its owner and date. Owners confirm or correct on the spot."),
            ("point", "End when you are done", "If the questions are answered in twenty minutes, end in twenty. The time returned goes to the action items."),
            ("h", "Minutes People Act On"),
            "Minutes do not need to record who said what. They need to record what was decided and what "
            "happens next.",
            ("point", "Header", "Meeting name, date, attendees and absences."),
            ("point", "Decisions", "One line each, numbered: “D-07: Four hours of overtime for two encoders on Thursday. Approved by the head of office.”"),
            ("point", "Action items", "What, who, by when: “Clerk to inform the two encoders and the personnel office by 4 p.m. today.”"),
            ("point", "Parking lot", "Items moved to a later meeting, with the date."),
            "Send the minutes the same day, while memories agree. Decisions that change the plan go to the "
            "change log from Part 24; new problems go to the issue log from Part 26.",
            ("h", "Online and Mixed Meetings"),
            "Some meetings happen by video call, or with a few people in the room and others on a screen. The same rules apply, with three additions.",
            ("point", "Share the agenda on screen", "Keep the current question visible, so remote attendees know where the discussion is."),
            ("point", "Call on remote people by name", "Those on a screen can be drowned out by the room. The chair asks them directly before each decision."),
            ("point", "Type the decision in the chat", "Writing it where everyone can see it confirms the wording before the meeting moves on."),
            ("h", "Check Your Standing Meetings"),
            "A weekly meeting set up at the start of a project can outlive its purpose. Once a month, look at the last four sets of minutes.",
            ("point", "Count the decisions", "If three of the four ended without one, shorten the meeting, make it every two weeks, or replace it with the status report."),
            ("point", "Count the attendees", "If some people never speak or own an action, ask whether they need to be there."),
            ("point", "Check the parking lot", "Items that stay parked for a month need an owner or a decision to drop them."),
            ("h", "The Clerk’s Rebuilt Meeting"),
            "The next week, the clerk sent this agenda the afternoon before, for a thirty-minute meeting.",
            ("point", "1. Five minutes", "Status: read the one-page report beforehand. Questions only."),
            ("point", "2. Ten minutes", "Do we approve overtime for two encoders to clear the address "
             "corrections by Friday? Decision needed from the head of office."),
            ("point", "3. Ten minutes", "Which barangay goes first in the next round, and why? Options from "
             "the clerk."),
            ("point", "4. Five minutes", "Action items and parking lot."),
            "It ended in twenty-eight minutes, with two decisions and five action items. Four people "
            "attended; two others read the minutes.",
            ("h", "Mistakes to Avoid"),
            ("point", "Meeting to share status", "Send the report instead."),
            ("point", "Topics instead of questions", "Write each item as a question to answer."),
            ("point", "No decider in the room", "Reschedule, or the decision waits anyway."),
            ("point", "Minutes a week later", "Send them the same day."),
            ("h", "Quick Recap"),
            ("point", "Meet to decide or solve", "Not to read status aloud."),
            ("point", "Questions, times and outcomes", "On an agenda sent a day ahead."),
            ("point", "Say each decision aloud", "With an owner and a date."),
            ("point", "Same-day minutes", "Decisions and actions, linked to the change and issue logs."),
            ("h", "Your Part 27 Exercise"),
            "Take your next project meeting.",
            ("point", "Ask the first question", "What must be decided or solved? If nothing, send a report "
             "instead."),
            ("point", "Rewrite the agenda", "Each item as a question, with minutes and an expected outcome."),
            ("point", "Write the minutes", "Decisions and action items only, sent before the end of the day."),
            "Afterward, count the person-hours spent and the decisions made. Try to raise the second number "
            "while lowering the first.",
            "At the end of the thirty minutes, the head of office stood up and said, “That was the first "
            "meeting this month where I knew what I had approved.” The clerk’s minutes were in everyone’s "
            "inbox by three.",
            ("cta", "Read: Project Management Series, Part 26: The Issue Log, Turning Problems Into Next Steps", "/blog/project-management-part-26-issue-log/"),
            ("cta", "Read: Project Management Series, Part 25: The Status Report, One Page That Tells the Truth Early", "/blog/project-management-part-25-status-reports/"),
            ("cta", "Read: Project Management Series, Part 7: The Kickoff Meeting Blueprint", "/blog/project-management-part-7-kickoff-meeting/"),
            ("cta", "Read: Project Management Series, Part 8: Who Does What? Building a RACI Matrix", "/blog/project-management-part-8-raci-matrix/"),
            ("ask", "What was decided at the last meeting you attended? Could everyone in the room say it?"),
        ],
    },
    {
        "date": "December 3, 2027",
        "title": "Project Management Series, Part 26: The Issue Log, Turning Problems Into Next Steps",
        "slug": "project-management-part-26-issue-log",
        "category": "pm",
        "summary": "Risks are what might happen; issues are what already did. This part shows how to keep an "
                   "issue log on one page: what to record, how to rate urgency, who owns each issue, when to "
                   "escalate to the sponsor, and how to close an issue so it stays closed.",
        "publish_on": "2027-12-03 21:00",
        "body": [
            "By the second week of delivery, the clerk had problems written in four places. A sticky note on "
            "her monitor said “San Roque runner sick.” A message in the team chat said two notices came back "
            "with the wrong address. Her notebook had “ask assessor re: duplicate lots.” And the head of "
            "office had told her, in passing, that a councilor wanted to know why one barangay got its "
            "notices later. Each problem was known to someone. Nobody could see all of them at once.",
            "(This project, its staff and its problems are fictional, drawn up to teach the method.)",
            "Part 25 reported problems upward in a status report. This part is about where those problems "
            "live between reports. When you finish, you will know the difference between a risk and an "
            "issue, what an issue log records, how to set urgency and ownership, when an issue goes to the "
            "sponsor, and how to close one properly.",
            ("photo", "blog/pm-issues.jpg", "The issue log: one list, one owner per issue, a next step with a "
             "date, and a clear line for when the sponsor must decide. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "Risk or Issue?"),
            "Part 19 drew the line. A risk is uncertain and in the future: “The legal review may take longer "
            "than a week.” An issue has already happened: “The legal review is late.” A risk that happens "
            "becomes an issue.",
            "The risk register plans for what might happen. The issue log manages what is happening now. "
            "Keeping them separate keeps each one short enough to read.",
            ("quote", "A problem everyone knows about and nobody owns is still unsolved."),
            ("h", "What the Issue Log Records"),
            "One row per issue, with these columns.",
            ("point", "Number and date raised", "I-01, I-02 and so on, with the date it was first reported."),
            ("point", "Description", "What is wrong, in one or two sentences, with a number if there is one: "
             "“Two notices returned, wrong address, San Isidro.”"),
            ("point", "Impact", "What it affects: a milestone, the budget, quality or a stakeholder."),
            ("point", "Urgency", "High, medium or low, by the rules below."),
            ("point", "Owner", "One person who makes sure it is resolved. Not a team, not “all.”"),
            ("point", "Next step and due date", "The very next action, not the whole solution."),
            ("point", "Status", "Open, in progress, escalated or closed, with the closing date and how it "
             "was resolved."),
            ("h", "Setting Urgency"),
            "As with the colors in Part 25, write the rules down before the first issue arrives.",
            ("point", "High", "Will move a milestone or the budget within a week if nothing is done."),
            ("point", "Medium", "Will affect a deliverable or a stakeholder, but there is more than a week "
             "to act."),
            ("point", "Low", "Worth fixing, but the project finishes on time and within budget even if it "
             "waits."),
            "Urgency decides the order of work and how often the issue is reviewed. High issues are looked at "
            "daily; the rest at the weekly update.",
            ("h", "One Owner Each"),
            "The owner is not always the person who fixes the problem. The owner is the person who makes sure "
            "it gets fixed, and who answers when someone asks about it.",
            ("point", "Close to the work", "The runner problem was owned by the clerk, who assigns runners."),
            ("point", "With the authority", "The duplicate lots belonged to the assessor’s office, so an "
             "assessor’s clerk owned that issue, with the clerk as the contact."),
            ("point", "Agreed, not assigned in absence", "Tell the owner and get a yes. An owner who does not "
             "know is not an owner."),
            ("h", "When to Escalate"),
            "Some issues need a decision the project team cannot make. The charter from Part 2 and the change "
            "limit from Part 24 already say what the clerk can decide alone.",
            ("point", "Escalate when", "The fix needs more money, more people or a later date than the clerk "
             "can approve, or it involves another office that has not responded."),
            ("point", "How", "In the status report under “Decisions needed,” with the options and a date."),
            ("point", "Not a complaint", "Escalating is a request for a decision. Bring the facts and a "
             "recommendation."),
            ("h", "The Clerk’s First Log"),
            "She moved the four problems into one table that afternoon.",
            ("point", "I-01, runner on sick leave", "High: San Roque delivery slipping. Owner: the clerk. Next "
             "step: request a borrowed runner, decision by Wednesday. Escalated through the status report."),
            ("point", "I-02, two notices with wrong addresses", "Medium. Owner: the encoder. Next step: check "
             "the two records against the tax declarations by Friday."),
            ("point", "I-03, duplicate lots in the list", "Medium. Owner: the assessor’s clerk. Next step: "
             "confirm which entries are duplicates by next Tuesday."),
            ("point", "I-04, councilor asking about timing", "Low. Owner: the clerk. Next step: send the "
             "delivery schedule by barangay, with the reason for the order."),
            "Four problems, four owners, four dates. For the first time, the head of office could see the "
            "whole list in a minute.",
            ("h", "Closing an Issue Properly"),
            ("point", "Confirm the fix", "The wrong addresses are corrected and the notices delivered, not "
             "just “sent to encoding.”"),
            ("point", "Write how it was resolved", "One line. It becomes evidence for the lessons-learned "
             "review."),
            ("point", "Check for a cause", "Two wrong addresses may point to a problem in the source list. If "
             "so, add it to the risk register for next time, or raise a change request."),
            ("point", "Keep closed issues", "Move them to the bottom or a second tab. Do not delete them."),
            ("h", "How the Log Connects to the Other Documents"),
            "The issue log does not replace anything built earlier in this series. It feeds it.",
            ("point", "To the status report", "The top three open issues, with owners and next steps, go straight into the report from Part 25."),
            ("point", "To change control", "If fixing an issue changes scope, the finish date or the budget, it becomes a change request, as in Part 24."),
            ("point", "To the risk register", "An issue that could happen again becomes a risk for the next round, with a response written in advance."),
            ("point", "From the RACI matrix", "Part 8’s matrix already shows who is responsible for each task. Start there when choosing an issue’s owner."),
            ("h", "Reviewing the Log"),
            "Five minutes in the weekly update, in a fixed order: new issues, high issues, overdue next steps, "
            "and issues ready to close. Any issue whose next step is overdue twice gets a new next step or a "
            "new owner.",
            ("h", "Mistakes to Avoid"),
            ("point", "Problems in many places", "Chat, notes and memory all feed one log."),
            ("point", "A team as owner", "One name per issue."),
            ("point", "A solution instead of a next step", "Write the very next action and its date."),
            ("point", "Closing without checking", "Confirm the fix, then record it."),
            ("h", "Quick Recap"),
            ("point", "Issues have happened", "Risks might; keep them in separate lists."),
            ("point", "One row, one owner, one next step", "With a due date and an urgency set by rules."),
            ("point", "Escalate with options", "Through the status report, with a decision date."),
            ("point", "Close with evidence", "And look for the cause, so it does not come back."),
            ("h", "Your Part 26 Exercise"),
            "Use the project from your earlier exercises.",
            ("point", "Gather", "List every open problem you know about, from chats, notes and memory."),
            ("point", "Log", "Give each one a number, an urgency, an owner and a next step with a date."),
            ("point", "Escalate one", "If any needs the sponsor, write the decision request with options."),
            "Then ask each owner to confirm. The log is real when every name on it has said yes.",
            "Two weeks later, all four issues were closed. I-02 had led to one more line in the risk register: "
            "addresses in the source list to be checked against the tax declarations before the next round. "
            "The sticky note came off the clerk’s monitor, and nothing replaced it.",
            ("cta", "Read: Project Management Series, Part 25: The Status Report, One Page That Tells the Truth Early", "/blog/project-management-part-25-status-reports/"),
            ("cta", "Read: Project Management Series, Part 19: The Risk Register, Planning for What Could Go Wrong", "/blog/project-management-part-19-risk-register/"),
            ("cta", "Read: Project Management Series, Part 24: Change Control, Saying Yes to a Change Without Losing the Plan", "/blog/project-management-part-24-change-control/"),
            ("cta", "Read: Project Management Series, Part 8: Who Does What? Building a RACI Matrix", "/blog/project-management-part-8-raci-matrix/"),
            ("ask", "Where do the problems in your current project live right now: one list, or many places?"),
        ],
    },
    {
        "date": "November 24, 2027",
        "title": "Project Management Series, Part 25: The Status Report, One Page That Tells the Truth Early",
        "slug": "project-management-part-25-status-reports",
        "category": "pm",
        "summary": "A status report should let the sponsor see a problem while there is still time to act. "
                   "This part gives a one-page format, a green, amber and red rating with written rules, "
                   "and a worked example from the notices project.",
        "publish_on": "2027-11-24 21:00",
        "body": [
            "The clerk’s weekly update said what it had said for three weeks: “All on track.” Then a "
            "councilor mentioned to the head of office that no notices had reached San Roque yet, though "
            "two other barangays had theirs. The head of office called the clerk in. The clerk had known "
            "about the delay for five days. She had expected to catch up, so she had not reported it.",
            "(The project, its people and every figure here are invented for teaching. No real office, "
            "employee or taxpayer is described.)",
            "Part 24 handled changes that someone asks for. This part handles the news that nobody asks for. "
            "Here you will learn what a status report is for, a one-page format, how to rate a project green, "
            "amber or red with rules written in advance, and how to write the report so the sponsor can act "
            "on it.",
            ("photo", "blog/pm-status.jpg", "The status report: one page, the same format each time, a "
             "rating backed by rules, and the decision the sponsor needs to make. (Illustration: Butch "
             "Mahinay, aumahinay.dev)", "medium"),
            ("h", "What a Status Report Is For"),
            "A status report is not a diary of what the team did. It answers four questions for the people "
            "who must make decisions.",
            ("point", "Where are we?", "Against the plan: the schedule, the budget and the deliverables."),
            ("point", "What changed?", "Since the last report, including approved changes from the change "
             "log."),
            ("point", "What could go wrong?", "The top risks and any problems already happening."),
            ("point", "What do you need from me?", "The decision or help the sponsor must give, and by when."),
            ("quote", "Bad news reported early is a problem. Bad news reported late is a crisis."),
            ("h", "Green, Amber and Red"),
            "Some organizations, governments among them, rate projects with three colors. The United Kingdom’s Infrastructure and "
            "Projects Authority, which reviews that government’s major projects, defined its ratings in its "
            "2022–23 annual report.",
            ("point", "Green", "Successful delivery on time, budget and quality appears highly likely, with "
             "no major unresolved issues that seem likely to threaten it."),
            ("point", "Amber", "Successful delivery appears feasible, but significant issues already exist "
             "and need management attention."),
            ("point", "Red", "Successful delivery appears to be unachievable, with major problems that seem unmanageable at this stage. The project may need to be re-scoped or reviewed."),
            "A treasury project of a few weeks can borrow the idea. The colors work only if everyone agrees "
            "in advance what moves a project from one to the next.",
            ("h", "Write the Rules Before You Need Them"),
            "The clerk added a short table to the communication plan from Part 11, approved by the head of "
            "office.",
            ("point", "Green", "Every milestone on its planned date, or late by no more than half of its "
             "buffer from Part 21; spending within the budget from Part 17."),
            ("point", "Amber", "A milestone has used more than half of its buffer, or a risk in the register "
             "from Part 19 has started to happen, or spending is above plan."),
            ("point", "Red", "A milestone will miss its date even after using the whole buffer, or the "
             "budget will be exceeded without a decision from the sponsor."),
            "With rules like these, the color is not a feeling. Anyone reading the facts reaches the same "
            "color, including the head of office.",
            ("h", "The One-Page Format"),
            ("point", "Header", "Project name, report date, period covered, prepared by."),
            ("point", "Overall rating", "Green, amber or red, with one sentence saying why."),
            ("point", "Milestones", "Each one with its planned date, its forecast date and its status. "
             "Progress is counted in finished deliverables, not hours worked."),
            ("point", "Budget", "Spent so far against the plan to date."),
            ("point", "Changes", "Requests logged or decided this period, by number."),
            ("point", "Top risks and issues", "No more than three, each with its owner and next step."),
            ("point", "Decisions needed", "What, from whom, and the date after which it is too late."),
            ("point", "Next period", "The two or three most important things that will happen."),
            "Use the same layout every time. A reader who knows where to look can find the change from last "
            "week in seconds.",
            ("h", "A Worked Example"),
            "Here is the report the clerk should have sent in week 3. Delivery to San Roque was planned to "
            "finish on Friday. Its buffer was four working days.",
            ("point", "Overall rating", "Amber. San Roque delivery is two days behind, using two of its four "
             "buffer days."),
            ("point", "Milestones", "Poblacion delivery: done, on plan. San Isidro: done, one day late, "
             "inside its buffer. San Roque: forecast two days late."),
            ("point", "Budget", "₱14,200 spent against ₱15,000 planned to date."),
            ("point", "Top issue", "One of two runners for San Roque is on sick leave. Owner: the clerk. Next "
             "step: borrow a runner from the assessor’s office for three days."),
            ("point", "Decision needed", "Approval to borrow the runner, by Wednesday. After Wednesday, the "
             "rest of the buffer is at risk."),
            "That report takes ten minutes to write. Sent on time, it gives the head of office a choice "
            "while there is still room to choose.",
            ("h", "Writing It So It Gets Read"),
            ("point", "Lead with the rating and the reason", "Put the most important line first, where a busy reader starts."),
            ("point", "Use dates and numbers", "“Two days behind, two of four buffer days used,” not "
             "“slightly delayed.”"),
            ("point", "Ask clearly", "“Please approve X by Wednesday” is easier to act on than “for your "
             "information.”"),
            ("point", "Send it on schedule", "Even when nothing changed. A report that arrives every week is easier to trust when it finally says something new."),
            ("h", "Same Facts, Different Readers"),
            "The communication plan from Part 11 named who hears what. The status report follows it. The head of office receives the full page. The councilors who asked about the project receive three lines taken from it: the rating, the reason and the next milestone. The team sees the full page too, so nobody learns about a problem in their own work from someone else. Every version uses the same facts and the same color, so no reader hears a different story.",
            ("h", "When the News Is Bad"),
            "The hardest report to send is the first amber one. Hoping to catch up before anyone notices is a "
            "gamble with the sponsor’s options. The clerk’s five days of silence took away the time the head "
            "of office could have used.",
            ("point", "Report the fact", "What happened, with the number."),
            ("point", "Report the plan", "What you are doing about it."),
            ("point", "Report the ask", "What you need, and by when."),
            ("h", "Mistakes to Avoid"),
            ("point", "Green by habit", "Check the rules each week before choosing the color."),
            ("point", "Activity instead of progress", "Report finished deliverables, not busy days."),
            ("point", "A long report", "One page, the same layout every time."),
            ("point", "No decision requested", "If you need something, ask for it with a date."),
            ("h", "Quick Recap"),
            ("point", "Four questions", "Where are we, what changed, what could go wrong, what do you need?"),
            ("point", "Colors with rules", "Agree in advance what makes a project amber or red."),
            ("point", "Numbers and dates", "Replace adjectives with facts."),
            ("point", "Early beats perfect", "An amber report on time is worth more than a green one that "
             "hides a problem."),
            ("h", "Your Part 25 Exercise"),
            "Use the project from your earlier exercises.",
            ("point", "Write the rules", "One line each for green, amber and red, using your milestones, "
             "buffers and budget."),
            ("point", "Fill the page", "Write this week’s report in the one-page format."),
            ("point", "Find the ask", "Name one decision you need from your sponsor, and the date after "
             "which it is too late."),
            "Send it, even if the rating is green. The habit is what makes the amber report possible when "
            "it is needed.",
            "The head of office approved the borrowed runner that afternoon. San Roque had its notices by "
            "Tuesday, one buffer day to spare. The clerk’s next report was green, and this time the head of "
            "office believed it.",
            ("cta", "Read: Project Management Series, Part 24: Change Control, Saying Yes to a Change Without Losing the Plan", "/blog/project-management-part-24-change-control/"),
            ("cta", "Read: Project Management Series, Part 11: The Communication Plan, Who Hears What, When", "/blog/project-management-part-11-communication-plan/"),
            ("cta", "Read: Project Management Series, Part 21: Buffers, Not Padding, Adding Safety to a Schedule Honestly", "/blog/project-management-part-21-buffers-not-padding/"),
            ("cta", "Read: Project Management Series, Part 19: The Risk Register, Planning for What Could Go Wrong", "/blog/project-management-part-19-risk-register/"),
            ("ask", "When did a status report last tell you something early enough to act on it?"),
        ],
    },
    {
        "date": "November 15, 2027",
        "title": "Project Management Series, Part 24: Change Control, Saying Yes to a Change Without Losing the Plan",
        "slug": "project-management-part-24-change-control",
        "category": "pm",
        "summary": "New requests can arrive at any point once a project starts. This part shows a simple way to "
                   "handle them: write the request down, measure what it does to scope, time, cost, risk "
                   "and quality, let the right person decide, and update the plan and the change log.",
        "publish_on": "2027-11-15 21:00",
        "body": [
            "Two weeks into the round of notices from Part 23, a councilor stopped the clerk in the hallway. “Can you also "
            "send a text message to every taxpayer before the notice arrives? It would only take a minute.” "
            "The clerk said she would look into it. Back at her desk, she counted: 1,800 taxpayers, a phone "
            "number on file for only some of them, and nobody in the plan assigned to send anything. It "
            "would not take a minute.",
            "(This case, its people and its numbers are made up for teaching. They do not describe any real "
            "office or taxpayer.)",
            "Part 23 decided what good enough means. This part deals with what happens when someone wants "
            "the plan to change after it was approved. By the end, you will know what change control is, "
            "how to write a change request, how to measure its impact, who should decide, and how to keep a "
            "change log that shows how the project grew and why.",
            ("photo", "blog/pm-change.jpg", "Change control: write the request down, measure its impact, "
             "let the sponsor decide, then update the plan and the log. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "Why Changes Need a Process"),
            "Part 4 named the problem: scope creep, the work that gets added to a project one small request "
            "at a time. A single request may be reasonable. The trouble starts when requests are accepted in "
            "hallways and chat messages, and nobody adds up what they cost.",
            "Change control is not a way to say no. It is a way to make sure that each yes is made by the "
            "right person, with the cost in front of them, and written where the team can see it.",
            ("point", "Without it", "The plan says one thing, the team does another, and the deadline slips "
             "without anyone deciding that it should."),
            ("point", "With it", "Every change has a record: who asked, what it costs, who approved it, and "
             "what in the plan moved because of it."),
            ("quote", "A change is not the problem. An unrecorded change is."),
            ("h", "Who Decides"),
            "The Project Management Institute’s glossary describes a change control board as a formally "
            "constituted group of stakeholders responsible for reviewing, evaluating, approving, delaying or "
            "rejecting changes to the project, with its decisions recorded.",
            "A treasury project of a few weeks does not need a board with a schedule of meetings. It needs a "
            "named person with the authority to accept a change, written down before the first request "
            "arrives.",
            ("point", "The sponsor", "In this series, the head of office signed the charter in Part 2, so the "
             "head of office decides on changes to scope, deadline and budget."),
            ("point", "The project lead", "The clerk can approve small changes that stay inside an agreed "
             "limit, such as moving a task by a day within its buffer from Part 21."),
            ("point", "Written in the charter", "Add one line: who approves changes, and up to what limit "
             "the project lead may decide alone."),
            ("h", "Step 1: Write the Request Down"),
            "Every request starts the same way, no matter who asks or how important they are. It goes on a "
            "one-page change request form.",
            ("point", "What is asked", "In plain words: send a text reminder to each taxpayer three days "
             "before the notice is delivered."),
            ("point", "Who asked, and when", "The councilor, on the date of the hallway conversation."),
            ("point", "Why", "The reason given: taxpayers would be ready for the notice and less likely to "
             "ignore it."),
            ("point", "A number", "CR-03, so it can be found and referred to later."),
            "Writing it down does two things. It shows the person asking that the request was taken "
            "seriously, and it turns a passing idea into something specific enough to measure.",
            ("h", "Step 2: Measure the Impact"),
            "The clerk then checked the request against each part of the plan built in this series. For "
            "CR-03, she found the following.",
            ("point", "Scope", "A new deliverable, text reminders, outside the scope statement from Part 4. "
             "Phone numbers were on file for only part of the 1,800 taxpayers."),
            ("point", "Time", "Cleaning and checking the phone numbers would take an encoder about four days. "
             "That work would sit on the critical path from Part 16, before delivery could start."),
            ("point", "Cost", "Four days of staff time, costed as in Part 17, plus the cost of sending the "
             "messages."),
            ("point", "Risk", "A new risk for the register from Part 19: a message sent to the wrong number, "
             "with a taxpayer’s name and amount on it, which would raise a privacy concern."),
            ("point", "Quality", "A new standard for Part 23’s quality plan: each message matches the record, "
             "and goes only to the number on file."),
            "She wrote the impact in a short paragraph at the bottom of the form, with two options. "
            "Option A: approve as asked and move the delivery start by four days. Option B: approve a "
            "smaller version, a general reminder posted on the office’s public page and read at barangay "
            "assemblies, with no change to the dates.",
            ("h", "Step 3: Decide, and Say Why"),
            "The head of office read the form the next morning. The decision options are the ones the "
            "glossary lists: approve, reject, or delay.",
            ("point", "Approve", "The change goes into the plan, and the plan is updated."),
            ("point", "Reject", "The request is closed, with the reason written down."),
            ("point", "Delay", "The idea is kept for a later round or the next project, and the requester is "
             "told when it will be looked at again."),
            "The head of office chose Option B for this round and delayed the text reminders to next year, "
            "when the phone numbers could be cleaned before the project started. The clerk told the "
            "councilor the same day, with the reason.",
            ("h", "Step 4: Update the Plan and the Log"),
            "An approved change is not finished when it is approved. It is finished when every document it "
            "touches says the same thing.",
            ("point", "Scope statement", "Version 3, with the public reminder added and the date of the "
             "change, as Part 4 advised."),
            ("point", "Schedule and budget", "Only where the change moved them. Option B did not."),
            ("point", "Communication plan", "From Part 11: who posts the reminder, and when."),
            ("point", "Risk register", "Updated if the change adds or removes a risk."),
            "Then the change log gets one line per request: number, date, requester, short description, "
            "impact, decision, decided by, and date closed. CR-03 took one line. At the end of the project, "
            "that log becomes one of the main inputs to the lessons-learned review.",
            ("h", "Small Changes Still Count"),
            "Not every request needs a meeting. A fixed limit keeps small changes moving.",
            ("point", "Inside the limit", "A change that uses no more than the agreed buffer and adds no "
             "deliverable: the project lead decides and logs it."),
            ("point", "Outside the limit", "Anything that changes scope, the finish date or the budget goes "
             "to the sponsor."),
            ("point", "Always logged", "Even a one-day shift gets a line. Several small changes together can "
             "add up to a large one."),
            ("h", "Mistakes to Avoid"),
            ("point", "Saying yes in the hallway", "Write it down first, then answer."),
            ("point", "Measuring only the time", "Check scope, cost, risk and quality too."),
            ("point", "Approving without updating the plan", "The documents must match the decision."),
            ("point", "Rejecting without a reason", "The requester should hear why, and when it may come "
             "back."),
            ("h", "Quick Recap"),
            ("point", "Changes are normal", "Change control makes each one a decision, not an accident."),
            ("point", "Four steps", "Write it down, measure the impact, decide, then update."),
            ("point", "One named decider", "The sponsor, with a small limit for the project lead."),
            ("point", "The change log", "One line per request, kept until the lessons-learned review."),
            ("h", "Your Part 24 Exercise"),
            "Take the project from your earlier exercises.",
            ("point", "Name the decider", "Add a line to your charter: who approves changes, and the limit "
             "for the project lead."),
            ("point", "Make the form", "A one-page change request with the five fields from Step 1, plus a "
             "space for impact and decision."),
            ("point", "Log one request", "Take the last extra request your project received and run it "
             "through the four steps."),
            "If the request was already done without a decision, log it anyway. The point is to see what it "
            "really cost, so the next one is decided with the numbers in front of you.",
            "A week later, the councilor saw the reminder read out at a barangay assembly and sent the clerk "
            "a short message: “That worked. Put my text messages on next year’s list.” She already had. It "
            "was CR-03, marked delayed, with a date to look at it again.",
            ("cta", "Read: Project Management Series, Part 23: Quality Planning, Deciding What Good Enough Means", "/blog/project-management-part-23-quality-planning/"),
            ("cta", "Read: Project Management Series, Part 4: Drawing the Line Before Work Begins", "/blog/project-management-part-4-defining-scope/"),
            ("cta", "Read: Project Management Series, Part 19: The Risk Register, Planning for What Could Go Wrong", "/blog/project-management-part-19-risk-register/"),
            ("cta", "Read: Project Management Series, Part 2: The Project Charter on One Page", "/blog/project-management-part-2-project-charter/"),
            ("ask", "What was the last request that changed your project without anyone deciding it should?"),
        ],
    },
    {
        "date": "November 5, 2027",
        "title": "Project Management Series, Part 23: Quality Planning, Deciding What Good Enough Means",
        "slug": "project-management-part-23-quality-planning",
        "category": "pm",
        "summary": "Quality is easier to plan than to inspect at the end. This part shows how to write what "
                   "“good” means for each deliverable, decide how and when it will be checked, weigh what "
                   "quality costs against what mistakes cost, and fit the checks into the schedule.",
        "publish_on": "2027-11-05 21:00",
        "body": [
            "In the last round of notices, a sample check caught wrong amounts on part of the first printed "
            "batch. Only that part had to be reprinted, for ₱800, and the project still stayed within its budget. "
            "Everyone agreed the check had saved the round.",
            "At the planning meeting for next year, the clerk asked a harder question. “The check found the "
            "mistakes. What made them?” The answer was in the risk register from Part 19: the notices were "
            "filled in from a list that had been edited by hand. The check was good. Not needing it would "
            "have been better.",
            "(Like every case in this series, this one is invented, from the office down to the last peso. No real "
            "town, employee or taxpayer is described.)",
            "Parts 14 to 22 planned the work, time, money, risks and purchases. This part plans quality. When you finish reading, you will know what quality means in a project, how to write a standard for "
            "each deliverable, how to choose the right check, what the cost of quality is, and how to put "
            "quality work into the schedule and the budget.",
            ("photo", "blog/pm-quality.jpg", "Quality planning: define good for each deliverable, prevent "
             "errors at the source, check at the right point, and record the result. (Illustration: Butch "
             "Mahinay, aumahinay.dev)", "medium"),
            ("h", "What Quality Means in a Project"),
            "In this series, quality means that a deliverable meets the requirements agreed at the start. It "
            "does not mean the most expensive version, or perfection. A notice printed on heavy paper with a "
            "color seal is not better quality if the amount on it is wrong.",
            ("point", "Good enough, written down", "Every deliverable needs a short statement of what “good” "
             "means, agreed with the sponsor before the work begins."),
            ("point", "Measurable", "“Accurate” is a wish. “The amount on each notice matches the ledger to "
             "the centavo” can be checked."),
            ("point", "Linked to requirements", "The standards come from the requirements gathered in Part 9, "
             "not from the team’s taste."),
            ("quote", "Decide what good looks like while it is still cheap to change."),
            ("h", "Prevention Before Inspection"),
            "The quality pioneer W. Edwards Deming put it as the third of his fourteen points for management, "
            "in his book Out of the Crisis: cease dependence on inspection to achieve quality, and build "
            "quality into the product in the first place.",
            "For the notices, inspection had found the wrong amounts. Prevention meant removing the reason "
            "they appeared. The clerk proposed filling the notices directly from the ledger export, with no "
            "hand-edited list in between. The sample check stayed, but its job changed from catching "
            "expected errors to confirming that none were made.",
            ("h", "Step 1: A Standard for Each Deliverable"),
            "Go through the work breakdown structure from Part 14 and write one or two standards for each "
            "deliverable. For the notices project:",
            ("point", "The notice template", "Approved in writing by the legal adviser, with the legal basis "
             "and the payment deadline stated."),
            ("point", "Each printed notice", "Name, address and barangay match the taxpayer record; the amount "
             "matches the ledger to the centavo; the notice is signed."),
            ("point", "Delivery", "Each notice is either received, with a signature or a recorded refusal, or "
             "listed as undelivered with a reason."),
            ("point", "The envelopes", "The specification from Part 22: size, color and quantity, checked on "
             "delivery."),
            ("h", "Step 2: Choose the Check"),
            "A standard needs a check that tells you whether it was met. For each one, decide how, how much, "
            "by whom and when.",
            ("point", "Every item, or a sample", "Amounts can be compared for all 1,800 notices by a formula, "
             "matching each notice’s amount against the ledger. Signatures are checked by eye, so a sample "
            "of each batch is practical."),
            ("point", "By someone else", "A second person does the check, so it does not depend on the person "
             "who prepared the work reading it again with the same eyes."),
            ("point", "As early as possible", "Check the first batch before printing the rest, and the "
             "template before filling any notice. A mistake found at the first step costs one page."),
            ("point", "Recorded", "Each check gets a line: date, what was checked, how many, what was found, "
             "who checked."),
            ("h", "Step 3: Count the Cost of Quality"),
            "The American Society for Quality describes the cost of quality in four groups. They help a "
            "project see where its quality money goes.",
            ("point", "Prevention", "Spent to stop problems before they start, such as writing standards and "
             "training. Here: setting up the direct fill from the ledger, and a short briefing for the "
             "encoders."),
            ("point", "Appraisal", "Spent on measuring and checking. Here: the formula comparison, the "
             "signature sample and the inspection of the envelopes."),
            ("point", "Internal failure", "Spent fixing defects found before they reach the customer. Here: "
             "the ₱800 reprint from the last round."),
            ("point", "External failure", "Spent fixing defects found after delivery. Here: a taxpayer who "
             "receives a notice with the wrong amount, comes to the office to complain, and needs a corrected "
             "notice, plus the time of the staff who handle it and the trust that is lost."),
            "Prevention and appraisal are planned costs. The two failure costs are the price of skipping them, "
            "and the external one falls partly on the taxpayer, outside the project’s budget.",
            ("h", "Step 4: Put Quality Into the Plan"),
            ("point", "In the schedule", "The checks take time. The clerk placed the first-batch check inside "
             "the printing days, so the dates in the plan from Part 21 did not move."),
            ("point", "In the budget", "Setting up the direct fill took two days of staff time, "
             "costed like any other staff time, as in Part 17."),
            ("point", "In the register", "R2, wrong amounts on printed notices, was updated. With the cause "
             "removed, its probability dropped, and the response now pointed to the new standard."),
            ("h", "The Quality Plan on One Page"),
            "The clerk kept the whole plan to one table with five columns.",
            ("point", "Deliverable", "What is being produced."),
            ("point", "Standard", "What good means, in a form that can be checked."),
            ("point", "Check", "How, how many, and by whom."),
            ("point", "When", "The step in the schedule where it happens."),
            ("point", "Record", "Where the result is written."),
            "The head of office signed it with the rest of the plan. From then on, “Is it good enough?” had a "
            "written answer.",
            ("h", "How the Round Went"),
            "The formula compared all 1,800 amounts with the ledger and found none that differed. The "
            "signature sample found two unsigned notices in the third batch, signed the same afternoon. No "
            "notice had to be reprinted. The check that had saved the last round became, this time, the "
            "proof that the work was right.",
            ("h", "Mistakes to Avoid"),
            ("point", "“High quality” as a goal", "Write a standard that can be checked."),
            ("point", "Relying only on the final check", "Remove the causes of errors first."),
            ("point", "Checking your own work", "Give the check to someone else."),
            ("point", "Leaving checks out of the plan", "They need time, money and an owner."),
            ("h", "Quick Recap"),
            ("point", "Quality is agreed", "Meeting the requirements, written down before the work starts."),
            ("point", "Prevent, then check", "Build it in at the source, and confirm with a check."),
            ("point", "Four costs", "Prevention, appraisal, internal and external failure."),
            ("point", "One page", "Deliverable, standard, check, when and record."),
            ("h", "Your Part 23 Exercise"),
            "Take the work breakdown structure from your Part 14 exercise.",
            ("point", "Write standards", "For three deliverables, write what good means in a way that can be "
             "checked."),
            ("point", "Choose checks", "For each one, decide how, how many, by whom and when."),
            ("point", "Find one cause", "Pick the error your office sees most in this kind of work, and write "
             "one way to stop it at the source."),
            "Then show the page to the person who will receive the work, and ask whether it describes what "
            "they expect. If it does not, you found the gap before it cost anything.",
            ("cta", "Read: Project Management Series, Part 19", "/blog/project-management-part-19-risk-register/"),
            ("cta", "Read: Project Management Series, Part 9", "/blog/project-management-part-9-gathering-requirements/"),
            ("cta", "Read: Project Management Series, Part 22", "/blog/project-management-part-22-procurement-and-suppliers/"),
            ("cta", "Read: Project Management Series, Part 14", "/blog/project-management-part-14-work-breakdown-structure/"),
            ("ask", "What does “good enough” mean for the main deliverable of your current project, and is it written down?"),
        ],
    },
    {
        "date": "October 27, 2027",
        "title": "Project Management Series, Part 22: Procurement and Suppliers, Planning What You Must Buy",
        "slug": "project-management-part-22-procurement-and-suppliers",
        "category": "pm",
        "summary": "In a government office, anything a project buys has to go through procurement, and "
                   "procurement takes time. This part shows how to find what must be bought, put it in the plan "
                   "early, write a clear specification, work with the procurement team, and manage a supplier "
                   "until the goods are accepted.",
        "publish_on": "2027-10-27 21:00",
        "body": [
            "The plan for next year’s round of notices looked ready. The critical path was clear, the buffer "
            "was visible, and the budget was approved. Then the clerk asked a simple question at the weekly "
            "check-in: “Who is buying the envelopes, and when?”",
            "Nobody had an answer. The envelopes were in the budget from Part 17, ₱3,600 for 1,800 of them, costed under package 2.3, printing and signing. But nobody had been named to buy them, and in a government office, money in the budget does not put "
            "envelopes on a desk. A purchase has to go through procurement first.",
            "(As in every part of this series, the office, the people and the numbers are made up. No real "
            "town, employee or taxpayer is described.)",
            "Parts 14 to 21 planned the work, the time, the money and the risks. This part adds the things a "
            "project must buy. By the last section, you will know how to list what must be procured, why "
            "procurement belongs in the schedule, how to write a specification a supplier cannot misread, how "
            "to work with your procurement team, and how to manage a supplier from order to acceptance.",
            ("photo", "blog/pm-procurement.jpg", "Procurement in a project: list what to buy, plan the lead "
             "time, specify clearly and accept against the specification. (Illustration: Butch Mahinay, "
             "aumahinay.dev)", "medium"),
            ("h", "The Rules Come First"),
            "Government buying in the Philippines follows the procurement law. Today that is Republic Act No. 12009, the New Government Procurement Act, signed "
            "in July 2024, which revised the earlier law, Republic Act No. 9184. A project manager does not need to master the law, but a few of its provisions shape every "
            "project plan.",
            ("point", "The annual plan", "Section 7 says no government procurement shall be undertaken unless "
             "it is in accordance with the approved Annual Procurement Plan. An item that is not in the plan "
             "cannot simply be bought when the project needs it."),
            ("point", "The committee", "Section 41 requires each procuring entity to establish one or more "
             "Bids and Awards Committees. In practice, this is the team to talk to early."),
            ("point", "The modes", "Section 26 lists the modes of procurement, from competitive bidding to "
             "small value procurement. Section 34 describes small value procurement as asking for at least "
             "three price quotations, for amounts that do not exceed two million pesos."),
            "Which mode applies, and which forms are needed, is decided by the procurement rules and the "
            "office’s Bids and Awards Committee, not by the project. The project’s job is to ask early and "
            "plan for the answer.",
            ("quote", "In public work, buying is a task with its own duration, not an errand."),
            ("h", "Step 1: List What Must Be Bought"),
            "Go through the work breakdown structure from Part 14, package by package, and ask: what does this "
            "package need that the office does not already have?",
            ("point", "For the notices project", "Envelopes for delivery, and paper and toner for printing."),
            ("point", "Check what is on hand", "Supplies already in the office’s stock may be enough. Ask the "
             "supply officer before treating an item as a purchase."),
            ("point", "Check the plan", "Ask whether each item is already in the office’s Annual Procurement "
             "Plan. If it is not, the process to add it is a task of its own."),
            ("h", "Step 2: Put Procurement in the Schedule"),
            "A purchase is a chain of steps: a request, the procurement process, the order, delivery, and "
            "acceptance. Each step takes time, and much of that time is outside the project team’s control. It "
            "is an external dependency, the kind described in Part 20.",
            ("point", "Ask for the lead time", "The office’s procurement staff can say how long a purchase of "
             "this size usually takes from request to delivery. Use their number, not a guess."),
            ("point", "Work backward", "If the envelopes must be on hand on day 14, when printing and signing begin, the "
             "request must go in early enough for the whole chain to finish before then."),
            ("point", "Add it to the network", "Procurement becomes a work package with its own owner, and the "
             "package that needs the goods depends on it. Run the passes from Part 16 again."),
            "In this office, the procurement staff advised allowing about four weeks for a small purchase of "
            "envelopes. That meant the request had to go in before the project formally started, so the clerk "
            "added a pre-start task: submit the purchase request.",
            ("h", "Step 3: Write a Clear Specification"),
            "A supplier delivers what is written, not what was meant. A vague request invites the wrong item, "
            "and the wrong item invites a delay.",
            ("point", "Vague", "“Envelopes, 1,800 pieces.”"),
            ("point", "Clear", "“Envelopes, white, plain, large enough for an A4 notice folded in three, "
             "1,800 pieces, delivered to the treasury office.” Check that the size "
             "matches the printed notice before submitting."),
            ("point", "Include what will be checked", "Quantity, size, color, and anything the notice depends "
             "on. These become the checklist for acceptance in Step 5."),
            ("h", "Step 4: Work With the Procurement Team"),
            ("point", "Talk early", "Bring the list of items to the procurement staff at the planning stage, "
             "not when the item is needed."),
            ("point", "Follow their process", "Use the forms and steps they require. A shortcut that skips a "
             "step can stop the purchase later, or create an audit finding."),
            ("point", "Keep one contact", "One person on the project follows up on each purchase, so the "
             "procurement staff are not answering the same question three times."),
            ("point", "Do not promise suppliers anything", "Only the authorized process can commit the office. "
             "A project member who tells a supplier “you will get the order” creates a problem for everyone."),
            ("h", "Step 5: Manage the Supplier to Acceptance"),
            ("point", "Track the delivery date", "Put it on the tracker from Part 12, with the person "
             "following it up."),
            ("point", "Inspect before accepting", "Check the delivered goods against the specification, "
             "following the office’s inspection and acceptance procedure. A box of the wrong size found on day "
             "14 is a problem; found on delivery day, it is a phone call."),
            ("point", "Write changes down", "If anything about the order changes, it goes through the "
             "procurement process in writing, not by a text message to the supplier."),
            ("point", "Note how it went", "On time, complete, correct? A short note helps the next project "
             "plan the next purchase."),
            ("h", "Procurement Risks in the Register"),
            "The risk register from Part 19 gained two new lines.",
            ("point", "R6. Late delivery of envelopes", "Response: mitigate by submitting the request before "
             "the project starts. Trigger: no delivery date confirmed two weeks before printing."),
            ("point", "R7. Wrong item delivered", "Response: mitigate with a clear specification and inspection "
             "on delivery. Owner: the clerk."),
            ("h", "The Envelopes, This Time"),
            "The clerk checked with the supply officer, found the envelopes were already in the office’s "
            "procurement plan, and submitted the request with a clear specification before the project began. "
            "The envelopes arrived a week before printing. One box held the wrong size, caught at inspection "
            "and replaced through the supplier before day 14. Nobody on the critical path ever knew.",
            ("h", "Mistakes to Avoid"),
            ("point", "Treating budget as stock", "Money in the budget still has to go through procurement."),
            ("point", "Leaving procurement out of the schedule", "It has a duration and an owner like any task."),
            ("point", "Vague specifications", "Write what will be checked on delivery."),
            ("point", "Side deals with suppliers", "Only the authorized process commits the office."),
            ("h", "Quick Recap"),
            ("point", "List early", "Go through the WBS and ask what must be bought."),
            ("point", "Schedule it", "Procurement is an external dependency with real lead time."),
            ("point", "Specify clearly", "The specification is also the acceptance checklist."),
            ("point", "Follow the process", "Work with the procurement team, and inspect before accepting."),
            ("h", "Your Part 22 Exercise"),
            "Take the work breakdown structure from your Part 14 exercise.",
            ("point", "List the purchases", "Write every item a package needs that is not already on hand."),
            ("point", "Ask the lead time", "For each item, ask your procurement staff how long it usually takes."),
            ("point", "Work backward", "Write the latest date each request must go in."),
            "Then compare those dates with today. If any request should already have been submitted, that is "
            "the first task for tomorrow morning.",
            ("cta", "Read: Project Management Series, Part 17", "/blog/project-management-part-17-project-budget/"),
            ("cta", "Read: Project Management Series, Part 20", "/blog/project-management-part-20-dependencies/"),
            ("cta", "Read: Project Management Series, Part 19", "/blog/project-management-part-19-risk-register/"),
            ("cta", "Read: Project Management Series, Part 14", "/blog/project-management-part-14-work-breakdown-structure/"),
            ("ask", "Which item in your current project still has to be bought, and does anyone know how long that takes?"),
        ],
    },
    {
        "date": "October 18, 2027",
        "title": "Project Management Series, Part 21: Buffers, Not Padding, Adding Safety to a Schedule Honestly",
        "slug": "project-management-part-21-buffers-not-padding",
        "category": "pm",
        "summary": "Most schedules already hold extra time, hidden inside each estimate where nobody can see or "
                   "manage it. This part shows how to bring that safety into the open as a visible buffer, who "
                   "should own it, and how to watch it week by week.",
        "publish_on": "2027-10-18 21:00",
        "body": [
            "When the clerk asked Collector Lim how long delivery would take for next year’s round, the answer "
            "came quickly: “Twenty-five days.” Later, over coffee, Lim added, “Twenty, most likely. I put in five extra, just in case.”",
            "The clerk checked the other estimates on the critical path. The legal review date had been "
            "agreed with the adviser in advance, and filling and printing had been timed in the second round. "
            "But the undelivered list, two days, turned out to be one day plus one “just in case.” None of this "
            "was dishonest. People protect their own tasks. The question was what that hidden time was doing.",
            "(Like every case in this series, this one is invented, from the office down to the last peso. No real "
            "town, employee or taxpayer is described.)",
            "Part 15 showed why estimates tend to run short, and Part 17 set money aside for risks in a "
            "contingency reserve. This part does the same for time. When you finish reading, you will know the "
            "difference between padding and a buffer, why hidden safety tends to get used up anyway, how to "
            "move it into one visible buffer, and how to watch that buffer while the project runs.",
            ("photo", "blog/pm-buffers.jpg", "Buffers, not padding: safety time moved out of each task into one "
             "visible buffer that the project manager owns. (Illustration: Butch Mahinay, aumahinay.dev)",
             "medium"),
            ("h", "Padding and Buffers"),
            ("point", "Padding", "Extra time added quietly inside a task’s estimate. Nobody else knows it is "
             "there, and the person who added it treats it as part of the task."),
            ("point", "A buffer", "Extra time placed in the schedule openly, as a line of its own, with a "
             "name, an owner and a rule for using it."),
            "Both come from the same honest worry: things go wrong. The difference is who can see the safety, "
            "and who decides when it is used.",
            ("quote", "Safety you can see is safety you can manage."),
            ("h", "Why Hidden Safety Disappears"),
            "Padding seems safe, but three patterns can use it up before it is needed.",
            ("point", "Parkinson’s law", "In a 1955 essay in The Economist, the historian C. Northcote "
             "Parkinson wrote that work expands so as to fill the time available for its completion. A task "
             "given twenty-five days can take twenty-five, even when twenty would have done."),
            ("point", "Starting late", "When a deadline feels comfortable, the work can start later than it "
             "could. Eliyahu Goldratt’s business novel Critical Chain, published in 1997, calls this "
             "the student syndrome, after students who begin an assignment just before it is due. Then a problem near the "
             "end has no time left to absorb it."),
            ("point", "Early finishes are lost", "If the next task is planned to start on a fixed date, finishing the "
             "task before it early changes nothing. Finishing it late pushes the next one back."),
            "Put together, each task’s safety is spent on that task, and the project as a whole still runs "
            "late. The safety was real, but it was in the wrong place.",
            ("h", "Moving the Safety Into the Open"),
            ("point", "1. Ask for two numbers", "For each task on the critical path, ask for a likely duration "
             "and a safe one, as in the three-point estimates of Part 15. The gap between them is the padding."),
            ("point", "2. Plan with the likely number", "Put the likely duration in the schedule, so each task "
             "has a target that is achievable but not loose."),
            ("point", "3. Gather the gaps into one buffer", "Add the removed time as one buffer at the end of "
             "the critical path, before the finish date."),
            ("point", "4. Give the buffer an owner", "The project manager holds it. A task that runs over draws "
             "from it openly, and the draw is written down."),
            "This changes how lateness is seen. A task that takes longer than its likely number is not a "
            "failure. It is exactly what the buffer is for, and the only question is whether the buffer is "
            "being used faster than the work is getting done.",
            ("h", "Why One Buffer Can Be Smaller Than the Sum"),
            "Not every task will need all its safety at once. One task runs late, another runs early, and a "
            "third uses half its margin. A shared buffer can absorb the late ones with time that would have "
            "sat unused inside the others.",
            "Critical chain methods use rules of thumb to size the shared buffer. A first project does not "
            "need one. "
            "Keeping the full amount as a buffer still gains the main benefits: the safety is visible, it has "
            "an owner, and early finishes can be passed on.",
            ("h", "Feeding Buffers for the Side Paths"),
            "Where a side path joins the critical path, a delay on the side path can hold up the critical work. "
            "A small buffer at that joining point, called a feeding buffer, protects the critical path from "
            "it.",
            "In the notices plan from Part 20, counter readiness (H) finishes on day 14, and delivery may start "
            "two days later because of the lag the cashiers asked for. Delivery starts on day 17, so there is "
            "one day to spare. That day is a small feeding buffer, and it is worth naming as one, so nobody "
            "spends it without noticing.",
            ("h", "The Notices Plan, With a Visible Buffer"),
            "The clerk asked for likely and safe numbers on the critical path and wrote both down.",
            ("point", "Template and legal review (C)", "10 days. The review date is agreed in advance, "
             "so no gap."),
            ("point", "Fill, print and sign (E, F)", "4 days each, timed in the second round. No gap."),
                        ("point", "Delivery (I)", "Safe 25 days, likely 20. Gap: 5."),
            ("point", "Undelivered list (J)", "Safe 2 days, likely 1. Gap: 1."),
            "The gaps add up to six days. The schedule now shows delivery from day 17 to 37 and the "
            "undelivered list from day 37 to 38, followed by a six-day project buffer. The finish date the head of office approved, day 44, did not "
            "move. What changed is that the six days now sit in one place, with one owner, where everyone can "
            "see them.",
            ("h", "Watching the Buffer"),
            ("point", "One weekly check", "Compare how much of the critical work is done with how much of the "
             "buffer is used."),
            ("point", "Healthy, for example", "Half the work done and a quarter of the buffer used: on course."),
            ("point", "Warning, for example", "A third of the work done and half the buffer used: find the cause and plan a "
             "response."),
            ("point", "Act early", "If the buffer is being used faster than the work moves, raise it in the "
             "weekly update from Part 11 before it runs out, not after."),
            ("h", "Mistakes to Avoid"),
            ("point", "Cutting estimates and dropping the safety", "Removing padding without adding a buffer "
             "only makes the schedule tighter."),
            ("point", "Treating the buffer as spare time", "It belongs to the whole project, not to the first "
             "task that wants it."),
            ("point", "Blaming people for using it", "A draw on the buffer is information, not a fault."),
            ("point", "Hiding the buffer from the sponsor", "Show it, explain it, and report its use."),
            ("h", "Quick Recap"),
            ("point", "Padding hides", "Safety inside tasks tends to be used up where it sits."),
            ("point", "Buffers show", "One visible buffer, with an owner and a rule."),
            ("point", "Plan at likely", "Tasks get achievable targets; the buffer absorbs what goes wrong."),
            ("point", "Watch the rate", "Buffer used against work done, every week."),
            ("h", "Your Part 21 Exercise"),
            "Take the critical path from your Part 16 exercise.",
            ("point", "Two numbers", "For each task on it, ask the person doing it for a likely and a safe "
             "duration."),
            ("point", "Build the buffer", "Add up the gaps and place them as one buffer before the finish date."),
            ("point", "Set the check", "Decide what “healthy” and “warning” mean for your project."),
            "Then show the plan to your sponsor with the buffer on its own line. Explaining it takes a few "
            "minutes, and from then on, everyone can see how much safety is left.",
            ("cta", "Read: Project Management Series, Part 15", "/blog/project-management-part-15-estimating-time/"),
            ("cta", "Read: Project Management Series, Part 17", "/blog/project-management-part-17-project-budget/"),
            ("cta", "Read: Project Management Series, Part 20", "/blog/project-management-part-20-dependencies/"),
            ("cta", "Read: Project Management Series, Part 16", "/blog/project-management-part-16-critical-path/"),
            ("ask", "Where in your current plan is the safety hidden, and who knows it is there?"),
        ],
    },
    {
        "date": "October 8, 2027",
        "title": "Project Management Series, Part 20: Understanding Dependencies, When Task B Is Waiting on Task A",
        "slug": "project-management-part-20-dependencies",
        "category": "pm",
        "summary": "Every schedule is a chain of “this waits for that.” This part explains the four kinds of "
                   "links between tasks, the difference between links you must keep and links you chose, "
                   "leads and lags, and what to do when a task is stuck waiting on someone else.",
        "publish_on": "2027-10-08 21:00",
        "body": [
            "On day 7 of the second round, Collector Reyes stopped by the clerk’s desk. “Can I start the "
            "routes now? I know where most of these households are already.” The clerk checked the schedule: "
            "routes wait for the approved list, due on day 9. “Not yet,” the clerk said. But the question "
            "stayed with the clerk. Did the routes really need the approved list, or had the "
            "schedule only said so?",
            "Every line in a schedule that says “waits for” is a decision. Some are forced by the work itself. "
            "Others were chosen, and a choice can be made again.",
            "(As in every part of this series, the office, the people and the numbers are made up. No real "
            "town, employee or taxpayer is described.)",
            "Part 16 put the work packages in order and found the critical path, using only the simplest kind "
            "of link. This part looks at the links themselves. By the last section, you will know the four "
            "kinds of links between tasks, how to tell a link you must keep from one you chose, what leads and "
            "lags are, and what to do when a task is stuck waiting on someone else.",
            ("photo", "blog/pm-dependencies.jpg", "Dependencies: the four kinds of links between tasks, the "
             "reasons behind them, and leads and lags. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Predecessors and Successors"),
            "A dependency is a link between two tasks. The task that comes first is the predecessor, and the "
            "one that depends on it is the successor. In the notices project, filling the notices (E) is the "
            "successor of the notice template (C): nobody can fill in a notice before its wording is final.",
            ("quote", "A schedule is only as honest as the links between its tasks."),
            ("h", "Four Kinds of Links"),
            "Project scheduling describes four ways two tasks can be linked. Each one names which end of the "
            "first task controls which end of the second.",
            ("point", "Finish-to-start", "B cannot start until A finishes. Printing and signing (F) cannot start "
             "until the notices are filled (E). Every link in Part 16 was of this kind."),
            ("point", "Start-to-start", "B cannot start until A starts. Checking the account list (B) could "
             "begin once pulling the list (A) has begun, working through each batch as it comes out, instead "
             "of waiting for the whole list."),
            ("point", "Finish-to-finish", "B cannot finish until A finishes. The list of undelivered notices (J) "
             "could be kept up to date during delivery, but it cannot be finished until delivery (I) is "
             "finished."),
            ("point", "Start-to-finish", "B cannot finish until A starts. It is the least common of the four, "
             "and this project has none. An example from elsewhere: when a new collection system replaces an "
             "old one, the old system’s daily work cannot stop until the new system has started."),
            "Changing the kind of link changes the schedule. A start-to-start link lets two tasks overlap, which "
            "can shorten the project, but only when the overlap is on the critical path. The list (A, B) has one "
            "day of float, so overlapping its tasks would not move the finish date.",
            ("h", "Why the Link Exists"),
            "Each link also has a reason, and the reason decides whether it can change. PMI’s PMBOK Guide describes two pairs: mandatory or discretionary, and external or internal. A link can be one of each, such as mandatory and external.",
            ("point", "Mandatory", "Required by the nature of the work, or by law or contract. A notice cannot "
             "be printed before it is filled. This link stays."),
            ("point", "Discretionary", "Chosen because of a good practice, past experience or a preference. "
             "Routes waiting for the approved list (D) is one: the office prefers routes drawn from a final "
             "list, but a collector could sketch them from the checked list. Such a link can be changed if "
             "there is a reason, as long as the risk is understood."),
            ("point", "External", "Depends on someone or something outside the project team. The legal "
             "adviser’s review in package C is external: the adviser serves other offices, as risk R1 in "
             "Part 19 noted."),
            ("point", "Internal", "Between tasks the team controls itself, such as filling, then printing."),
            "Writing the reason beside each link takes a minute and saves an argument later. When the schedule "
            "is under pressure, the discretionary links are the first ones to look at, and the mandatory ones "
            "are left alone.",
            ("h", "Leads and Lags"),
            ("point", "A lead", "The successor starts before the predecessor finishes. Delivery (I) could start "
             "one day before all notices are printed and signed (F), beginning with the barangays whose notices "
             "are ready. That is a finish-to-start link with a one-day lead. Part 16 called this kind of overlap "
             "fast-tracking."),
            ("point", "A lag", "The successor waits a set time after the predecessor. The cashiers asked to "
             "receive the counter guide at least two days before the first notices reach taxpayers, so they "
             "have time to read it. Counter readiness (H) to delivery (I) is a finish-to-start link with a "
             "two-day lag."),
            "A lag is not the same as float. Float is time a task may slip without harm. A lag is waiting that "
            "the plan requires, and it should be written into the link so nobody treats it as spare time.",
            ("h", "When Task B Is Stuck Waiting on Task A"),
            ("point", "Check the link", "Is it mandatory or discretionary? If it was a choice, ask whether part "
             "of B can start now."),
            ("point", "Ask for part of A", "A predecessor does not always have to be finished in full. The first "
             "barangays’ notices, the first pages of a list, or a draft for early comments may be enough to "
             "begin."),
            ("point", "Talk to A’s owner", "Ask when A will finish, not whether it is late. A date can be planned "
             "around."),
            ("point", "Confirm external dates early", "For work outside the team, agree on the date in advance "
             "and set a trigger, as with risk R1 in Part 19."),
            ("point", "Raise it on time", "If the wait threatens the finish date, report it to the sponsor "
             "within a working day, as the communication plan in Part 11 set out, with at least one option."),
            ("h", "The Third Round, Planned With Better Links"),
            "For next year’s round, the clerk reviewed every link in the network with the team. Most stayed as "
            "they were. Two changed.",
            ("point", "A one-day lead on delivery", "Delivery starts on day 17 instead of day 18, with the "
             "notices printed and signed so far, while the last batch is finished. Delivery runs from day 17 to 42 and the undelivered list "
             "from 42 to 44. The project finishes on day 44 instead of 45."),
            ("point", "A two-day lag before delivery", "Counter readiness still finishes on day 14, three "
             "days before delivery begins, so the two-day wait is met with a day to spare."),
            "The lead had a cost, and the clerk found it by running the forward and backward pass again, as Part "
            "16 advised. The routes (G) run from day 14 to 17 and must now be ready for delivery on day 17. The "
            "one day of float they had left after Part 18 is gone. The routes are now on the critical path, so "
            "Collector Reyes knows that a day lost there is a day lost for the whole project.",
            ("h", "Mistakes to Avoid"),
            ("point", "Linking everything finish-to-start", "Ask whether some tasks can overlap."),
            ("point", "Treating every link as fixed", "Write down why each link exists."),
            ("point", "Hiding lags as float", "Write required waiting into the link."),
            ("point", "Adding a lead without rechecking", "Run the passes again and see what became critical."),
            ("h", "Quick Recap"),
            ("point", "Four kinds", "Finish-to-start, start-to-start, finish-to-finish and start-to-finish."),
            ("point", "Two pairs of reasons", "Mandatory or discretionary, external or internal."),
            ("point", "Leads and lags", "Start early, or wait on purpose, and write it into the link."),
            ("point", "Stuck tasks", "Check the link, ask for part of the work, and raise it on time."),
            ("h", "Your Part 20 Exercise"),
            "Take the network you drew for your Part 16 exercise.",
            ("point", "Label each link", "Write the kind of link and the reason: mandatory, discretionary, "
             "external or internal."),
            ("point", "Find one change", "Pick one discretionary link on the critical path and ask whether a "
             "lead or a start-to-start link would be safe."),
            ("point", "Recalculate", "Run the forward and backward pass again and note what became critical."),
            "Then list the external links and the person who owns each one. Those are the dates to confirm "
            "first.",
            ("cta", "Read: Project Management Series, Part 16", "/blog/project-management-part-16-critical-path/"),
            ("cta", "Read: Project Management Series, Part 18", "/blog/project-management-part-18-resource-allocation/"),
            ("cta", "Read: Project Management Series, Part 19", "/blog/project-management-part-19-risk-register/"),
            ("cta", "Read: Project Management Series, Part 11", "/blog/project-management-part-11-communication-plan/"),
            ("ask", "Which “waits for” in your current plan was a choice, not a rule?"),
        ],
    },
    {
        "date": "September 29, 2027",
        "title": "Project Management Series, Part 19: The Risk Register, Planning for What Could Go Wrong",
        "slug": "project-management-part-19-risk-register",
        "category": "pm",
        "summary": "Every project has things that might go wrong. The difference is whether they are written "
                   "down with an owner and a plan before they happen. This part builds a risk register for a "
                   "treasury project, scores each risk, and explains the four classic ways to respond.",
        "publish_on": "2027-09-29 21:00",
        "body": [
            "During the first round of notices, three things went wrong. The legal "
            "review came back late. A batch of notices had to be reprinted. A collector was out sick during "
            "delivery. Each problem was handled, but each one was handled as a surprise, in a hurry, by "
            "whoever happened to be there.",
            "Looking back, none of them was truly unexpected. Anyone on the team could have named all three "
            "before the project started. Nobody had asked.",
            "(Like every case in this series, this one is invented, from the office down to the last peso. No real "
            "town, employee or taxpayer is described.)",
            "Parts 15 to 18 kept pointing to risks: uncertain estimates, near-critical paths, contingency "
            "reserves and single points of failure. This part gathers them in one place. When you finish reading, you will know how to write a risk clearly, score it, choose a response, give it an owner "
            "and a trigger, and keep the register alive while the project runs.",
            ("photo", "blog/pm-risks.jpg", "The risk register: each risk written clearly, scored, given an "
             "owner, a response and a trigger. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "What a Risk Is, and What It Is Not"),
            "A risk is something uncertain that, if it happens, would affect the project. It has not happened "
            "yet, and it might not happen at all.",
            ("point", "A risk", "“The legal review may take longer than a week.” Uncertain, and in the future."),
            ("point", "An issue", "“The legal review is late.” It has already happened, and now it needs "
             "action, not a probability."),
            ("point", "A fact", "“The office has one printer.” Not uncertain. It is a constraint to plan "
             "around, though it can cause risks."),
            "Keeping these apart keeps the register useful. A risk that happens becomes an issue and moves "
            "into the weekly update from Part 11.",
            ("quote", "A risk written down is a problem you can still prepare for."),
            ("h", "Writing a Risk Clearly"),
            "A vague risk such as “printing problems” is hard to act on. A clearer form names the cause, the "
            "event and the effect.",
            ("point", "The pattern", "Because of a cause, an event may happen, which would lead to an effect."),
            ("point", "Example", "Because the notices are filled in from a list that was edited by hand, "
             "some printed notices may show wrong amounts, which would mean reprinting and a delay of up to "
             "two days."),
            "Written this way, the cause points to prevention, and the effect points to how much it matters.",
            ("h", "Finding the Risks"),
            ("point", "Ask the team", "The people doing the work know what has gone wrong before. Ask each "
             "of them, as in Part 15."),
            ("point", "Read the last project", "Look at how the first round actually went, as Part 15 did."),
            ("point", "Walk the schedule", "Go through each package in the critical path from Part 16 and "
             "ask what could delay it."),
            ("point", "Check the people", "The resource grid from Part 18 shows who is overloaded or "
             "irreplaceable."),
            ("h", "Scoring: Probability and Impact"),
            "Not every risk deserves the same attention. A simple score helps decide where to look first.",
            ("point", "Probability", "How likely is it? Low, medium or high, scored 1, 2 or 3."),
            ("point", "Impact", "If it happens, how much would it hurt the date, the cost or the quality? "
             "Low, medium or high, scored 1, 2 or 3."),
            ("point", "Score", "Probability times impact, from 1 to 9. Write down what each level means for "
             "this project, so two people score the same risk the same way."),
            "The score is a way to sort the list, not a precise measurement. Its main job is to start a "
            "conversation about which risks matter most.",
            ("h", "Four Ways to Respond to a Threat"),
            "PMI’s PMBOK Guide describes several responses to threats. This post uses these four.",
            ("point", "Avoid", "Change the plan so the risk cannot happen or cannot affect the project. If "
             "mailing notices risks delays in the post, delivering by hand avoids that risk."),
            ("point", "Mitigate", "Reduce the probability or the impact. Checking a sample of the first "
             "printed batch before printing the rest keeps an error from reaching every notice."),
            ("point", "Transfer", "Shift the impact to someone else, for example by contract. If an outside "
             "supplier printed the notices, a term requiring it to redo faulty prints at its own cost would "
             "transfer that cost. Transfer does not remove the risk itself."),
            ("point", "Accept", "Acknowledge the risk and take no special action, or set money or time aside "
             "in case it happens, like the contingency reserve in Part 17."),
            "Every response has a cost. Mitigating a low-score risk can cost more than the risk would. "
            "Accepting a high-score risk without a plan can be a decision nobody meant to make.",
            ("h", "Owners and Triggers"),
            ("point", "One owner per risk", "The person who watches it and starts the response. A good choice is the owner of the package it affects."),
            ("point", "A trigger", "A sign that the risk is about to happen or has started. “No comments from "
             "the legal adviser by day 8” is a trigger. When it fires, the owner acts without waiting for a "
             "meeting."),
            ("h", "The Notices Project Risk Register"),
            ("point", "R1. Legal review runs late", "Because the legal adviser serves other offices, the review "
             "may take more than a week, which would delay the critical path. Probability 2, impact 3, score 6. "
             "Response: mitigate by having the clerk draft it on days 3 to 5 and send it on day 5, as planned in Part 18, and by agreeing the review "
             "date in advance. Owner: the clerk. Trigger: no comments by day 8."),
            ("point", "R2. Wrong amounts on printed notices", "Probability 2, impact 2, score 4. Response: "
             "mitigate by checking a random sample of the first printed batch before printing the rest, as "
             "in Part 17 of the Data Analytics series, and accept the rest with the ₱1,000 reprint reserve. Owner: the clerk. "
             "Trigger: any error found in the sample."),
            ("point", "R3. The clerk is absent", "Because the clerk holds several packages, an absence would "
             "stop critical work. Probability 1, impact 3, score 3. Response: mitigate by having a second "
             "person shadow the filling of notices, as in Part 18. Owner: the head of office."),
            ("point", "R4. Hard-to-find households", "Probability 3, impact 1, score 3. Response: accept, with "
             "the ₱1,500 reserve for extra trips from Part 17. Owner: Collector Reyes. Trigger: more than ten "
             "notices returned in one week."),
            ("point", "R5. The printer breaks down", "Probability 1, impact 2, score 2. Response: mitigate by "
             "agreeing in advance to borrow another office’s printer if needed. Owner: the clerk."),
            "Sorted by score, the register puts the legal review at the top. That matches what Part 16 found: "
            "the template, not the list, sets the finish date.",
            ("h", "Keeping the Register Alive"),
            ("point", "Review it weekly", "Five minutes in the weekly update: any new risks, any scores that "
             "changed, any triggers that fired."),
            ("point", "Close what has passed", "Once printing is done, R2 and R5 can be closed."),
            ("point", "Move what happened", "A risk that happens becomes an issue, with its response already "
             "written."),
            ("point", "Record the lessons", "At the end, note which risks happened and whether the responses "
             "worked. The next project’s register starts from that."),
            ("h", "The Second Round, With a Register"),
            "This time, the register was tested twice. The legal adviser was called away for two days, but the trigger fired on day 8, the clerk called the adviser’s office the same morning, and the comments arrived on day 10, still on time. Then a sample check of the first printed batch found wrong amounts before the rest were printed, so only part of that batch was reprinted: the ₱800 reprint described in Part 17, the one risk that drew on the budget.",
            "Neither problem became a surprise, and the project finished inside its schedule and its budget.",
            ("h", "Mistakes to Avoid"),
            ("point", "Vague risks", "Name the cause, the event and the effect."),
            ("point", "Risks without owners", "Every risk needs one person to watch it."),
            ("point", "Writing it once", "Review the register every week."),
            ("point", "Mixing risks and issues", "A risk might happen; an issue already has."),
            ("h", "Quick Recap"),
            ("point", "Write it clearly", "Cause, event and effect."),
            ("point", "Score it", "Probability times impact, to decide what to look at first."),
            ("point", "Four responses", "Avoid, mitigate, transfer or accept."),
            ("point", "Owner and trigger", "Someone watches, and a clear sign starts the response."),
            ("h", "Your Part 19 Exercise"),
            "Take the project you have been planning through this series.",
            ("point", "List five risks", "Ask the people doing the work, and write each as cause, event and "
             "effect."),
            ("point", "Score and respond", "Give each a probability, an impact and one of the four responses."),
            ("point", "Name owners and triggers", "One person and one clear sign for each."),
            "Then compare your top risk with your critical path. If they are in different places, ask whether "
            "you are watching the right part of the project.",
            ("cta", "Read: Project Management Series, Part 18", "/blog/project-management-part-18-resource-allocation/"),
            ("cta", "Read: Project Management Series, Part 17", "/blog/project-management-part-17-project-budget/"),
            ("cta", "Read: Project Management Series, Part 16", "/blog/project-management-part-16-critical-path/"),
            ("cta", "Read: Data Analytics Series, Part 17", "/blog/data-analytics-part-17-samples-margin-of-error/"),
            ("ask", "Which risk in your current project has everyone noticed but nobody written down?"),
        ],
    },
    {
        "date": "September 20, 2027",
        "title": "Project Management Series, Part 18: Assigning People Without Overloading Them",
        "slug": "project-management-part-18-resource-allocation",
        "category": "pm",
        "summary": "A schedule can be correct on paper and impossible in practice, because one person is "
                   "needed in two places at once. This part shows how to list who is really available, "
                   "assign the work, spot overloads, and fix them with float before the finish date has to "
                   "move.",
        "publish_on": "2027-09-20 21:00",
        "body": [
            "The schedule for the notices project is approved: 45 working days, with the critical path "
            "worked out in Part 16 and the budget from Part 17. On paper, everything fits.",
            "Then the clerk writes names beside the packages. Collector Reyes knows the far barangays best, "
            "so Reyes plans the delivery routes. Reyes also wrote the counter guide in the first round, so "
            "Reyes is down for counter readiness too. Both packages fall in the same week of the schedule.",
            "The plan says both will be done on time. Reyes cannot be in two places at once.",
            "(As in every part of this series, the office, the people and the numbers are made up. No real "
            "town, employee or taxpayer is described.)",
            "Parts 14 to 17 described what the work is, how long it takes, in what order it runs and what it "
            "costs. This part asks who will do it, and whether they can. By the last section, you will "
            "know how to list people’s real availability, assign work packages, find overloads with a simple "
            "chart, and fix them using float before the finish date has to move.",
            ("photo", "blog/pm-resources.jpg", "Assigning people: real availability, assignments, overloads "
             "spotted early and fixed with float. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "What Resource Allocation Means"),
            "In project management, resources are the people, equipment and materials the work needs. "
            "Allocating them means deciding who or what does each work package, and checking that no one "
            "is given more than they can actually do.",
            "In this treasury office, the main resource is people, and each of them has a regular job that "
            "does not stop for the project. The counter still opens every morning.",
            ("quote", "A schedule is a promise about people’s time. Check that they can keep it."),
            ("h", "Step 1: Write Down When People Are Really Available"),
            "A resource calendar lists when each person can work on the project. It can be less than the office calendar suggests.",
            ("point", "Regular duties", "The cashier keeps the counter open. Collectors have field "
             "collections. In Part 15, two collectors were available for delivery only on Tuesdays and "
             "Thursdays."),
            ("point", "Leave and holidays", "Approved leave, training days and holidays during the project."),
            ("point", "Busy periods", "Weeks near tax deadlines, when the counter needs everyone."),
            ("point", "People outside the office", "The legal adviser and the head of office have their own "
             "schedules. A signature can wait days."),
            "Plan project work for less than a full day. A clerk who also answers the counter phone does not have eight hours a day for the project, and the plan should not pretend otherwise.",
            ("h", "Step 2: Assign Each Package"),
            "Use the RACI matrix from Part 8 for who is accountable. Here the question is narrower: who does "
            "the work, on which days. For the second round of notices, the clerk wrote this list, using the "
            "earliest dates from Part 16.",
            ("point", "Pull and check the list (A, B)", "The clerk, days 0 to 3; then a revenue staff member, "
             "days 3 to 7."),
            ("point", "Approve the list (D)", "The head of office, days 7 to 9."),
            ("point", "Notice template (C)", "Days 0 to 10. The clerk drafts it on days 3 to 5, after pulling the list, and the legal adviser reviews it on days 5 to 10, within the week assumed in Part 15."),
            ("point", "Fill, print and sign (E, F)", "The clerk, days 10 to 18, with the head of office "
             "signing."),
            ("point", "Delivery routes (G)", "Collector Reyes, days 9 to 12."),
            ("point", "Counter readiness (H)", "The cashier and Collector Reyes, days 10 to 14."),
            ("point", "Delivery and undelivered list (I, J)", "Collectors Reyes and Lim, days 18 to 43; then "
             "the clerk, days 43 to 45."),
            ("h", "Step 3: Find the Overloads"),
            "A simple chart shows what a list hides. Make a grid with one row per person and one column per "
            "working day. Mark each day a person is assigned to a package. Any day with two marks for the "
            "same person is an overload.",
            "For Collector Reyes, the routes run from day 9 to day 12 and counter readiness from day 10 to day "
            "14. The two overlap for two working days, and on those days the schedule asks for two full jobs "
            "from one person.",
            "The same grid can be built in a spreadsheet: people down the side, days across the top, and an "
            "X in each assigned cell. =COUNTIF(B2:B10, \"X\") under a day counts how many packages share it, "
            "and a rule that flags anything above one does the rest.",
            ("h", "Step 4: Fix the Overload"),
            "There are several ways to remove an overload. Try them in this order, because the first ones "
            "protect the finish date.",
            ("point", "Move work within its float", "In Part 16, the routes had six days of float: they could "
             "start as late as day 15 without moving the finish. Moving them to start after counter "
             "readiness solves the clash."),
            ("point", "Give the work to someone else", "Another collector could plan some of the routes, if "
             "they know those barangays."),
            ("point", "Split the work", "The counter guide could be written by the cashier, with Reyes "
             "reviewing it for an hour instead of writing it."),
            ("point", "Add help", "A staff member from another unit for a few days, if the head of office "
             "agrees."),
            ("point", "Extend the schedule", "If none of the above works, the package waits until the person "
             "is free, and the finish date may move."),
            "PMI’s guidance has names for the two ends of this list. Resource smoothing adjusts the schedule "
            "so demand stays within limits by moving work only within its float, so the critical path and the "
            "finish date stay the same. Resource leveling lets the schedule change when people are simply not "
            "available, and the finish date can move later.",
            ("h", "The Overload, Fixed"),
            "The clerk moved the routes to start on day 14, after counter readiness finishes. They now run "
            "from day 14 to day 17, and delivery still starts on day 18. The finish stays at day 45.",
            ("point", "The cost of the fix", "The routes used five of their six days of float. Their latest "
             "start is still day 15, so only one day of float is left. A package that had room to spare is "
             "now nearly critical."),
            ("point", "What changed in the plan", "The routes now go on the list of near-critical work from "
             "Part 16, and Reyes knows the new dates."),
            "This is the hidden price of smoothing. Float used to solve one problem is no longer available "
            "for the next one.",
            ("h", "Do Not Forget Equipment and Signatures"),
            ("point", "The one printer", "If the office has one printer for 1,800 notices and daily work, "
             "printing competes with the counter’s own printing."),
            ("point", "The signing", "If every notice needs the head of office’s signature, that time belongs "
             "in the head’s calendar, not just in the clerk’s plan."),
            ("point", "Vehicles", "If two collectors share one motorcycle, they cannot deliver in two "
             "directions on the same day."),
            ("h", "When One Person Holds Too Much"),
            "Look down the chart for a person whose row is full while everyone else’s is light. In the notices "
            "project, the clerk appears in more packages than anyone else. If the clerk is absent for a week, "
            "several packages stop at once, some of them on the critical path.",
            ("point", "Share the knowledge", "Have a second person shadow the clerk on filling the notices, "
             "so the work can continue during leave."),
            ("point", "Write it down", "A short guide for each of the clerk’s packages makes a handover "
             "possible."),
            ("point", "Record it as a risk", "Name the risk, its owner and the response, so it is managed "
             "rather than hoped away."),
            ("h", "Mistakes to Avoid"),
            ("point", "Planning people at full time", "Leave room for regular duties."),
            ("point", "Checking dates but not names", "A schedule can fit while one person is double-booked."),
            ("point", "Using float without noticing", "Note how much float each fix uses up."),
            ("point", "Ignoring people outside the team", "Signatures, reviews and shared equipment take time "
             "too."),
            ("h", "Quick Recap"),
            ("point", "Real availability", "A resource calendar shows when people can actually work on the "
             "project."),
            ("point", "Find overloads early", "A person-by-day grid shows double bookings."),
            ("point", "Fix with float first", "Smoothing keeps the finish date; leveling may move it."),
            ("point", "Watch single points", "Spread knowledge so one absence does not stop the project."),
            ("h", "Your Part 18 Exercise"),
            "Take the schedule from your Part 16 exercise.",
            ("point", "Add names", "Write who does each package, and on which days."),
            ("point", "Draw the grid", "One row per person, one column per day or week, and a mark for each "
             "assignment."),
            ("point", "Fix one overload", "Use float first, and note how much float the fix uses."),
            "Then look for the person whose row is fullest, and ask what would happen to the project if they "
            "were away for a week.",
            ("cta", "Read: Project Management Series, Part 16", "/blog/project-management-part-16-critical-path/"),
            ("cta", "Read: Project Management Series, Part 17", "/blog/project-management-part-17-project-budget/"),
            ("cta", "Read: Project Management Series, Part 8", "/blog/project-management-part-8-raci-matrix/"),
            ("cta", "Read: Project Management Series, Part 15", "/blog/project-management-part-15-estimating-time/"),
            ("ask", "Who in your office is assigned to more work than their calendar can hold?"),
        ],
    },
    {
        "date": "September 10, 2027",
        "title": "Project Management Series, Part 17: The Project Budget, Built Package by Package",
        "slug": "project-management-part-17-project-budget",
        "category": "pm",
        "summary": "“How much will it cost?” deserves a better answer than a guess at the biggest purchase. "
                   "This part builds a project budget from the work packages, explains three ways to "
                   "estimate cost, separates cash from staff time, and shows how contingency and management "
                   "reserves protect the plan.",
        "publish_on": "2027-09-10 21:00",
        "body": [
            "The head of office approves the nine-week schedule for the notices project. Then comes the next "
            "question: “How much will this cost, and do we have the funds?”",
            "The revenue clerk remembers the first round. Asked the same question then, the clerk answered "
            "quickly: “Mostly the printing.” The printing quote was about ₱6,500, so that went into the plan. "
            "Three weeks into that round, the envelopes had not been counted, "
            "the collectors were asking about their transport for the far barangays, and the toner ran out "
            "halfway through the run.",
            "None of these costs was a surprise. They were simply never written down, because the estimate "
            "started from the biggest purchase instead of from the work.",
            "(Like every case in this series, this one is invented, from the office down to the last peso. No real "
            "town, employee or taxpayer is described.)",
            "Part 14 broke the project into work packages, Part 15 estimated their time, and Part 16 put them "
            "in order. This part puts a cost on them. When you finish reading, you will know how to build a "
            "budget package by package, three ways to estimate a cost, why staff time belongs in the plan, "
            "how reserves work, and how to place spending on the calendar.",
            ("photo", "blog/pm-budget.jpg", "A project budget built from the work packages, with reserves for "
             "risks and spending placed on the calendar. (Illustration: Butch Mahinay, aumahinay.dev)",
             "medium"),
            ("h", "Start From the Work Packages"),
            "The WBS from Part 14 is already a list of everything the project must deliver. A bottom-up "
            "budget goes through it one package at a time and asks: what does this package need that costs "
            "money?",
            "Working this way makes forgotten costs easier to spot. The envelopes belong to package 2.3, "
            "printing and signing. The collectors’ transport belongs to package 3.2, delivery. Each one has "
            "a place to be written down.",
            ("quote", "A budget built from the work leaves fewer costs out."),
            ("h", "Three Ways to Estimate a Cost"),
            ("point", "Bottom-up", "Estimate each package, then add them up. It takes more effort than the other two ways and gives more detail."),
            ("point", "From a past project", "Start from what a similar project actually spent, then adjust "
             "for differences, the same outside view used for time in Part 15."),
            ("point", "From a unit cost", "Multiply a known rate by a quantity: 1,800 envelopes at ₱2 each is "
             "₱3,600. This works well wherever a price per item is known."),
            "These can be mixed. In the notices project, the clerk is using unit costs for envelopes and "
            "transport, a supplier quote for printing, and last year’s supply records to check the total.",
            ("h", "Cash Costs and Staff Time"),
            "Much of the work in an office project is done by staff who are already paid. That time does not "
            "need new funds, but it is not free: an hour spent checking the account list is an hour not spent "
            "at the counter.",
            ("point", "Cash costs", "Things the office must pay for: paper, toner, envelopes, transport. These "
             "need funds in the office’s budget."),
            ("point", "Staff time", "Person-days from each package’s estimate. These need people to be "
             "available, which ties back to the effort and duration point in Part 15."),
            "Keeping the two side by side shows the full cost of the project, and it helps the sponsor see "
            "what the office is giving up to do it.",
            ("h", "The Notices Project Budget"),
            ("point", "1. Account list (1.1 to 1.3)", "No cash cost. Staff time: about 9 person-days of the clerk’s and a checker’s time."),
            ("point", "2.1 Notice template", "No cash cost. Staff time: 2 person-days, plus one review session "
             "with the legal adviser."),
            ("point", "2.3 Printing and signing", "Paper and toner from the supplier quote, ₱6,500. Envelopes, "
             "1,800 at ₱2, ₱3,600."),
            ("point", "3.2 Delivery", "Transport allowance for the delivery trips: 50 trips at ₱150 = ₱7,500."),
            ("point", "4.2 Counter guide", "Printed copies for the counter, ₱500."),
            ("point", "5.3 Closing report", "Printing, ₱300."),
            "Cash total: ₱6,500 + ₱3,600 + ₱7,500 + ₱500 + ₱300 = ₱18,400. That is almost three times the "
            "clerk’s first answer.",
            ("h", "Reserves: Planning for What Might Go Wrong"),
            "No estimate is exact, as Part 15 showed. Reserves set money aside for that uncertainty, in two "
            "layers. A PMI paper on contingency reserves describes them this way.",
            ("point", "Contingency reserve", "Money set aside for identified risks, the ones already written in "
             "the risk list with a response planned. It is added to the estimates to form the cost baseline."),
            ("point", "Management reserve", "Money held back for problems nobody foresaw. It sits on top of the "
             "cost baseline, and the cost baseline plus the management reserve is the project budget."),
            "For the notices project, two identified risks were costed.",
            ("point", "Reprinting", "If errors such as a wrong amount are found after printing, part of the run must be redone. The clerk set aside ₱1,000."),
            ("point", "Longer delivery", "If hard-to-find households need extra visits, 10 more trips at ₱150 cost ₱1,500."),
            "Contingency reserve: ₱2,500. Cost baseline: ₱18,400 + ₱2,500 = ₱20,900. The head of office held a "
            "management reserve of ₱1,000, bringing the project budget to ₱21,900.",
            "The difference matters in practice. In this office, the clerk may use the contingency reserve "
            "when a listed risk happens, while the management reserve stays with the head of office, who decides whether an "
            "unexpected problem deserves it.",
            ("h", "Placing Spending on the Calendar"),
            "A budget also has a timeline. The critical path from Part 16 shows when each package runs, so it "
            "also shows when money is needed.",
            ("point", "Weeks 1 to 2", "Almost no cash. The list and the template are staff time."),
            ("point", "Weeks 3 to 4", "Printing, envelopes and the counter guide: about ₱10,600."),
            ("point", "Weeks 4 to 9", "Delivery transport, spread across the delivery weeks: ₱7,500."),
            "Knowing this helps the office arrange purchases in time. Buying supplies through the office’s "
            "usual process takes calendar time too, so ask the supply staff early how long it takes.",
            ("h", "Checking the Funds"),
            "For a government office, an estimate is only the first step. The 1987 Constitution provides that "
            "no money shall be paid out of the Treasury except in pursuance of an appropriation made by law. "
            "In practice, that means every cash cost must be covered by the office’s approved budget.",
            ("point", "Ask the budget officer early", "Show the cash costs by item and ask which part of the "
             "office’s approved budget can cover each one."),
            ("point", "Follow the purchasing rules", "Supplies are bought through the office’s procurement "
             "process. The supply or procurement staff can say what documents are needed."),
            ("point", "Write it in the plan", "Record where the funds come from beside each cost, so nobody "
             "has to ask again mid-project."),
            ("h", "Tracking Actual Spending"),
            ("point", "Record each cost when it happens", "Use the tracker from Part 12 and add the actual "
             "amount to the package it belongs to."),
            ("point", "Compare weekly", "For each package, compare the budget with what was actually spent so "
             "far, and note the difference."),
            ("point", "Explain the gaps", "A package over budget needs a reason and a decision: use the "
             "contingency reserve, cut elsewhere, or ask the sponsor."),
            ("point", "Close with actuals", "The closing report should record what each package actually "
             "cost, so the next estimate starts from facts."),
            ("h", "The Notices Project, Budgeted Again"),
            "This time, the clerk presented the budget package by package, with staff time beside "
            "the cash costs and the two reserves explained. The budget officer confirmed which items of the "
            "office’s approved budget would cover the supplies and the transport.",
            "One risk did happen: a checker found wrong amounts on part of the first printed batch. The reprint cost ₱800, paid from the contingency reserve, and the project finished "
            "inside its budget without a single request for more funds.",
            ("h", "Mistakes to Avoid"),
            ("point", "Starting from the biggest purchase", "Start from the work packages instead."),
            ("point", "Ignoring staff time", "Record person-days even when no new money is needed."),
            ("point", "One pot for everything", "Keep contingency and management reserves separate, with "
             "different owners."),
            ("point", "Checking funds too late", "Ask the budget officer before the plan is approved."),
            ("h", "Quick Recap"),
            ("point", "Bottom-up", "A budget built from each work package leaves fewer costs out."),
            ("point", "Cash and time", "Show both, so the full cost of the project is visible."),
            ("point", "Two reserves", "Contingency for listed risks; management reserve for the unforeseen."),
            ("point", "Funds and timing", "Confirm the funds early, and place spending on the calendar."),
            ("h", "Your Part 17 Exercise"),
            "Take the work packages from your Part 14 exercise.",
            ("point", "Cost each one", "Write the cash cost and the person-days beside every package."),
            ("point", "Add reserves", "Pick two risks, put a cost on each, and add them as a contingency "
             "reserve."),
            ("point", "Place it in time", "Use your Part 16 schedule to show which weeks need the money."),
            "Then compare your total with the first figure that came to mind. The gap shows how much the "
            "project would have cost beyond what anyone planned for.",
            ("cta", "Read: Project Management Series, Part 16", "/blog/project-management-part-16-critical-path/"),
            ("cta", "Read: Project Management Series, Part 15", "/blog/project-management-part-15-estimating-time/"),
            ("cta", "Read: Project Management Series, Part 14", "/blog/project-management-part-14-work-breakdown-structure/"),
            ("cta", "Read: Project Management Series, Part 10", "/blog/project-management-part-10-business-case/"),
            ("ask", "Which cost in your last project was never written down until it had to be paid?"),
        ],
    },
    {
        "date": "September 1, 2027",
        "title": "Project Management Series, Part 16: The Critical Path, Finding the Work That Sets the Finish Date",
        "slug": "project-management-part-16-critical-path",
        "category": "pm",
        "summary": "Some tasks can slip a little without moving the finish date. Others cannot slip at all. This "
                   "part explains the critical path method in plain words, works through the forward and "
                   "backward pass on a treasury project, and shows how float helps you decide where to watch "
                   "and where to act.",
        "publish_on": "2027-09-01 21:00",
        "body": [
            "The revenue clerk has estimates for every work package in the notices project. Now the head of "
            "office wants to know two things: when the notices will be out, and which part of the work to "
            "keep an eye on.",
            "The clerk is sure the answer to the second question is the account list. It is the largest "
            "piece of checking, and it caused delays in the first round. But when the packages are "
            "lined up in order, the list turns out to have a day to spare. The package with no room at all is "
            "the notice template waiting for legal review.",
            "That is what the critical path shows: not which work is biggest or hardest, but which work sets "
            "the finish date.",
            "(As in every part of this series, the office, the people and the numbers are made up. No real "
            "town, employee or taxpayer is described.)",
            "Part 14 broke the project into work packages, and Part 15 put time estimates on them. This part "
            "puts them in order. By the last section, you will know how to line up packages by what they "
            "depend on, find the critical path with a forward and a backward pass, read float, and choose "
            "carefully when the finish date has to move earlier.",
            ("photo", "blog/pm-critical-path.jpg", "The critical path: the chain of dependent work that takes "
             "longest and sets the finish date. (Illustration: Butch Mahinay, aumahinay.dev)", "medium"),
            ("h", "Where the Method Came From"),
            "The critical path method, or CPM, grew out of scheduling work that began at the chemical company DuPont in late 1956. According to a history published by PMI, Morgan Walker of DuPont and James Kelley of Remington Rand developed it, and in 1959 it was given its name and presented in a paper by the two of them. It began with large engineering and construction projects, but the idea works for a small office project too.",
            "The idea is this. When some work must wait for other work, the packages form chains. The longest "
            "chain from start to finish is the critical path, and its length is the shortest time in which "
            "the whole project can be done.",
            ("quote", "The longest chain of waiting sets the earliest finish."),
            ("h", "Step 1: List What Each Package Waits For"),
            "A dependency is a rule that one piece of work cannot start until another is finished. This post uses only the finish-to-start kind: the notices cannot be printed until they are filled in.",
            "For the second round of notices, the clerk listed each work package from the WBS, its most likely "
            "duration in working days from the Part 15 estimates, and what it waits for.",
            ("point", "A. Pull the account list (1.1)", "3 days. Waits for nothing."),
            ("point", "B. Check the list against the assessor’s records (1.2)", "4 days. Waits for A."),
            ("point", "C. Notice template with legal review (2.1)", "10 days. Waits for nothing."),
            ("point", "D. Final list approved (1.3)", "2 days. Waits for B."),
            ("point", "E. Fill in the notices (2.2)", "4 days. Waits for C and D."),
            ("point", "F. Print and sign the notices (2.3)", "4 days. Waits for E."),
            ("point", "G. Delivery routes (3.1)", "3 days. Waits for D."),
            ("point", "H. Counter readiness (4.1 and 4.2)", "4 days. Waits for C, and must be done before "
             "delivery starts."),
            ("point", "I. Deliver the notices (3.2)", "25 days. Waits for F, G and H."),
            ("point", "J. List of undelivered notices (3.3)", "2 days. Waits for I."),
            "The project management branch, with its plan, weekly updates and closing report, runs alongside "
            "the whole project, so it is left out of the chains.",
            "Drawing the packages as boxes with arrows from each package to the ones that wait for it makes "
            "the chains easy to see. A sheet of paper is enough.",
            ("h", "Step 2: The Forward Pass"),
            "The forward pass finds the earliest each package can start and finish. Count in working days from "
            "the start of the project, which is day 0.",
            ("point", "Rule 1", "A package with nothing to wait for starts at day 0."),
            ("point", "Rule 2", "Earliest finish = earliest start + duration."),
            ("point", "Rule 3", "A package that waits for several others starts when the last of them "
             "finishes, so take the largest earliest finish among them."),
            ("point", "The list chain", "A runs from day 0 to 3. B runs from 3 to 7. D runs from 7 to 9."),
            ("point", "The template", "C runs from day 0 to 10."),
            ("point", "Filling in", "E waits for C (day 10) and D (day 9), so it starts at day 10 and finishes "
             "at day 14. F then runs from 14 to 18."),
            ("point", "Routes and counter", "G runs from day 9 to 12. H runs from 10 to 14."),
            ("point", "Delivery", "I waits for F (day 18), G (day 12) and H (day 14), so it starts at day 18 "
             "and finishes at day 43. J runs from 43 to 45."),
            "The project can finish at day 45 at the earliest: 45 working days, or nine weeks of five working "
            "days, which matches the most likely value in the range from Part 15.",
            ("h", "Step 3: The Backward Pass"),
            "The backward pass works from the finish back to the start. It finds the latest each package can "
            "start and finish without moving the finish date.",
            ("point", "Rule 1", "The last package’s latest finish is the project finish, day 45."),
            ("point", "Rule 2", "Latest start = latest finish − duration."),
            ("point", "Rule 3", "A package that others wait for must finish by the earliest of their latest "
             "starts, so take the smallest."),
            ("point", "From the end", "J: latest start 43. I: latest finish 43, latest start 18. F: 14 to 18. "
             "E: 10 to 14."),
            ("point", "Routes and counter", "G must finish by 18, so its latest start is 15. H must also "
             "finish by 18, so its latest start is 14."),
            ("point", "The template", "C must finish by E’s latest start (10) and H’s (14). The smaller is 10, "
             "so its latest start is 0."),
            ("point", "The list chain", "D must finish by the smaller of E’s latest start (10) and G’s (15), "
             "which is 10, so its latest start is 8. B then runs latest from 4 to 8, and A from 1 to 4."),
            ("h", "Step 4: Read the Float"),
            "Float, also called slack, is how long a package can slip without moving the project finish. It "
            "is the latest start minus the earliest start.",
            ("point", "C, E, F, I and J", "Zero float. This chain is the critical path: 10 + 4 + 4 + 25 + 2 = "
             "45 days. A day lost on any of these is a day added to the project."),
            ("point", "A, B and D", "One day of float. The account list can slip one day and no more."),
            ("point", "H", "Four days of float."),
            ("point", "G", "Six days of float."),
            "This is what surprised the clerk. The legal review, not the list, sets the date. The list is "
            "still worth watching, because with only one day of float it is a near-critical path: a two-day "
            "delay there makes it the new critical path.",
            ("h", "Using the Critical Path"),
            ("point", "Watch the zero-float work first", "In the weekly update, report the critical packages "
             "by name, with their owners from the RACI matrix in Part 8."),
            ("point", "Start critical work early", "The legal review can begin on day 0, so the template "
             "should be sent to the legal adviser in the first week, not after the list is done."),
            ("point", "Use float to plan people", "The routes have six days to spare. If a collector is needed "
             "at the counter that week, the routes can wait a little without harm."),
            ("point", "Check the near-critical paths", "List any chain with only a day or two of float, and "
             "give it the same attention when its packages are running."),
            ("h", "When the Date Has to Move Earlier"),
            "Suppose the head of office needs the notices out a week sooner. There are two common ways to "
            "shorten a schedule, and both carry a price.",
            ("point", "Crashing", "Add people or other resources to a critical package. Two more collectors "
             "for delivery could shorten it, but they are taken from other work, and the cost goes up."),
            ("point", "Fast-tracking", "Overlap packages that were planned one after the other. Delivery could "
             "start with the first barangays as soon as their notices are printed and signed, instead of "
             "waiting for the last notice. This adds risk: a mistake found late may affect notices already "
             "delivered."),
            ("point", "Shorten only critical work", "Cutting two days from the routes would not move the "
             "finish at all, because the routes already have float."),
            ("point", "Recalculate after each change", "When a critical package gets shorter, another chain "
             "may become the longest. Run the forward and backward pass again."),
            ("h", "Estimates, Uncertainty and the Path"),
            "The critical path is only as good as the estimates under it. The calculation above uses the most "
            "likely durations from Part 15. If the pessimistic value for the legal review comes true, the "
            "finish date moves with it.",
            "A practical habit is to look at the packages on the critical path that also had a wide gap "
            "between their optimistic and pessimistic estimates. Those are the places where a risk owner and "
            "a closer look are most useful.",
            "Project management software, such as the tools compared in Part 12, can calculate the passes once "
            "dependencies are entered. Working through one small network by hand first makes it easier to "
            "check what the software shows.",
            ("h", "Mistakes to Avoid"),
            ("point", "Confusing big with critical", "The largest package is not always on the critical path."),
            ("point", "Missing dependencies", "A forgotten dependency, such as counter readiness before "
             "delivery, can hide the real critical path."),
            ("point", "Ignoring near-critical paths", "One day of float can disappear in one bad week."),
            ("point", "Calculating once", "Update the passes when packages finish early or late."),
            ("h", "Quick Recap"),
            ("point", "Critical path", "The longest chain of dependent work sets the earliest finish."),
            ("point", "Two passes", "Forward for earliest dates, backward for latest dates."),
            ("point", "Float", "Latest start minus earliest start; zero float means critical."),
            ("point", "Shorten with care", "Crashing costs more, fast-tracking adds risk, and only critical "
             "work moves the date."),
            ("h", "Your Part 16 Exercise"),
            "Take the work packages and estimates from your Part 14 and Part 15 exercises.",
            ("point", "List the dependencies", "For each package, write what it waits for."),
            ("point", "Run both passes", "Work out the earliest and latest start for each package."),
            ("point", "Find the path", "Mark the packages with zero float, and any with one or two days."),
            "Then ask yourself whether the work you were most worried about is on the critical path. If it is "
            "not, you may have been watching the wrong part of the project.",
            ("cta", "Read: Project Management Series, Part 15", "/blog/project-management-part-15-estimating-time/"),
            ("cta", "Read: Project Management Series, Part 14", "/blog/project-management-part-14-work-breakdown-structure/"),
            ("cta", "Read: Project Management Series, Part 8", "/blog/project-management-part-8-raci-matrix/"),
            ("cta", "Read: Project Management Series, Part 12", "/blog/project-management-part-12-choosing-pm-software/"),
            ("ask", "Which task in your current project has no room to slip, and does everyone know it?"),
        ],
    },
    {
        "date": "August 23, 2027",
        "title": "Project Management Series, Part 15: Why Estimates Run Short, and Four Ways to Fix Them",
        "slug": "project-management-part-15-estimating-time",
        "category": "pm",
        "summary": "People tend to underestimate how long their own work will take, even when they know their "
                   "past projects ran late. This part explains why, then gives four practical fixes: ask the "
                   "doer, estimate from the WBS, compare with the past, and use three-point estimates.",
        "publish_on": "2027-08-23 21:00",
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
            "(Like every case in this series, this one is invented, from the office down to the last peso. No real "
            "town, employee or taxpayer is described.)",
            "Part 14 broke the project into work packages. This part puts time on them. When you finish reading, you will know why estimates tend to run short, four ways to make them better, and how to "
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
            ("h", "Quick Recap"),
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
        "date": "August 13, 2027",
        "title": "Project Management Series, Part 14: The Work Breakdown Structure, One Bite at a Time",
        "slug": "project-management-part-14-work-breakdown-structure",
        "category": "pm",
        "summary": "A project that feels too big to plan becomes manageable once it is broken into pieces. "
                   "This part explains the work breakdown structure, the 100% rule, work packages and the WBS "
                   "dictionary, and breaks down a treasury project from a single goal to tasks people can own.",
        "publish_on": "2027-08-13 21:00",
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
            "planning stage. By the last section, you will know what a work breakdown structure is, the "
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
            ("h", "Quick Recap"),
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
        "date": "August 4, 2027",
        "title": "Project Management Series, Part 13: The Pre-Launch Checklist, a Review of Parts 1 to 12",
        "slug": "project-management-part-13-pre-launch-checklist",
        "category": "pm",
        "summary": "Before the real work starts, one short review can catch the gaps that cause trouble later. "
                   "This part turns the first twelve parts of the series into a pre-launch checklist, shows "
                   "how to run it in one meeting, and applies it to the treasury encoding project.",
        "publish_on": "2027-08-04 21:00",
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
            "(Like every case in this series, this one is invented, from the office down to the last peso. No real "
            "town or employee is described.)",
            "This is the last part of the series’ first stage, which covered how a project starts. By the end of this post, you will have a pre-launch checklist built from Parts 1 to 12, a way to run it in "
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
            ("h", "Quick Recap"),
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
        "date": "July 26, 2027",
        "title": "Project Management Series, Part 12: Choosing PM Software, and Why Tools Don’t Fix Broken Processes",
        "slug": "project-management-part-12-choosing-pm-software",
        "category": "pm",
        "summary": "A new project tool does not fix a process nobody has agreed on. This part shows how to get the "
                   "process working on paper first, what a PM tool actually needs to do, how to compare "
                   "options fairly, and how to try one without moving the whole office at once.",
        "publish_on": "2027-07-26 21:00",
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
            "After this post, you will know how to check a process before choosing a tool, the five "
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
            ("h", "Quick Recap"),
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
        "date": "July 16, 2027",
        "title": "Project Management Series, Part 11: The Communication Plan, Who Hears What, When",
        "slug": "project-management-part-11-communication-plan",
        "category": "pm",
        "summary": "A project can stall when the right people hear the wrong things, or nothing at all. This part "
                   "shows how to build a one-page communication plan: who needs what, how, how often and "
                   "from whom, with a rule for bad news and the treasury encoding project as the example.",
        "publish_on": "2027-07-16 21:00",
        "body": [
            "Three weeks into the encoding project, the assessor calls the head of office. “Why are your "
            "collectors asking my staff for tax declarations every afternoon? Nobody told me this was "
            "happening.” The project had been approved, the kickoff was held, and the assessor’s staff "
            "member was part of the team. But the assessor, who decides what that staff member works on, had "
            "never been told how much of their time the project needed.",
            "Nobody had hidden anything. Each person had simply assumed someone else would tell the assessor. "
            "A communication plan exists to stop that assumption.",
            "(Everyone and everything in this story is fictional, including the numbers. No real "
            "town or employee is described.)",
            "Part 8 settled who does each task. This part settles who needs to know about it. Read to the end and you will have a five-column communication plan, a filled-in example, a rule for "
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
            ("h", "Quick Recap"),
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
        "date": "July 7, 2027",
        "title": "Project Management Series, Part 10: Writing a Business Case That Gets a Yes",
        "slug": "project-management-part-10-business-case",
        "category": "pm",
        "summary": "A good idea still needs a reason to spend time and money on it. This part walks through "
                   "the six parts of a business case, a worked treasury example with simple numbers, and how to present it so a decision maker can say yes or no quickly.",
        "publish_on": "2027-07-07 21:00",
        "body": [
            "The revenue clerk asks the head of office for a second receipt printer and a part-time encoder "
            "for the January rush. The answer is a polite no: “The budget is tight this year.” The clerk is "
            "sure the request would pay for itself, but has nothing on paper to show it.",
            "A month later, the clerk asks again, this time with one page. It shows how long taxpayers waited "
            "last January, how many left the line without paying, what the printer and encoder would cost, and "
            "three options side by side. The head of office reads it twice, asks two questions and approves the printer.",
            "(The office and the people in this story are invented, and so are the figures. No real "
            "town or employee is described.)",
            "The request did not change. The case for it did. By the last section, you will know the six "
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
            ("h", "Quick Recap"),
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
        "date": "June 28, 2027",
        "title": "Project Management Series, Part 9: Gathering Requirements When Nobody Knows What They Want",
        "slug": "project-management-part-9-gathering-requirements",
        "category": "pm",
        "summary": "“Make the daily report faster” is a wish, not a requirement. This part shows five ways to "
                   "find out what people really need, the questions that get useful answers, and how to write "
                   "requirements that can be checked and agreed on.",
        "publish_on": "2027-06-28 21:00",
        "body": [
            "The cashier stops the revenue clerk in the hallway. “Can you make something that makes the daily "
            "report faster? It takes me forever every afternoon.” The clerk says yes, and two weeks later "
            "shows a spreadsheet that totals the day’s receipts by account in one click.",
            "The cashier looks at it politely and says it is nice. The totals were never the slow part. The "
            "slow part was finding the three or four receipts each day that did not match the cash count, and "
            "the spreadsheet does nothing about that.",
            "(Everyone and everything in this story is fictional, including the numbers. No real "
            "town or employee is described.)",
            "The cashier did know what the problem was. What nobody had done was ask the questions that would "
            "bring it out. Stay with me to the end, and you will know five ways to gather requirements, the "
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
            ("h", "Quick Recap"),
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
        "date": "June 18, 2027",
        "title": "Project Management Series, Part 8: Who Does What? Building a RACI Matrix",
        "slug": "project-management-part-8-raci-matrix",
        "category": "pm",
        "summary": "When everyone thinks someone else is handling a task, it can go undone. This part explains "
                   "the four RACI roles, walks through a RACI matrix for the treasury encoding project, and "
                   "gives four checks that help catch gaps early.",
        "publish_on": "2027-06-18 21:00",
        "body": [
            "Two weeks into the encoding project, the revenue clerk asks for the list of records that did not "
            "match the assessor’s tax declarations. One collector thought the assessor’s staff member was "
            "keeping it. The assessor’s staff member thought the collectors were writing it down as they "
            "encoded. Each had done careful work on their own part. Nobody had kept the list.",
            "The kickoff had named who works on which afternoons. What it had not settled was who owns each "
            "task: who does it, who answers for it, who must be asked first and who only needs to be told. "
            "A simple grid called a RACI matrix settles exactly that.",
            "(The office and the people in this story are invented, and so are the figures. No real "
            "town or employee is described.)",
            "Part 7 ran the kickoff. This part turns its decisions into a written map of roles. By the end of this post, you will know the four RACI roles, how to build a matrix for a small office project, "
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
            ("h", "Quick Recap"),
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
        "date": "June 9, 2027",
        "title": "Project Management Series, Part 7: The Kickoff Meeting Blueprint",
        "slug": "project-management-part-7-kickoff-meeting",
        "category": "pm",
        "summary": "A kickoff meeting can launch a project or waste an hour. This part gives a one-hour "
                   "agenda, what to prepare beforehand, how to run each segment, and what to send afterward, "
                   "using the treasury encoding project as the example.",
        "publish_on": "2027-06-09 21:00",
        "body": [
            "The revenue clerk calls the first meeting of the encoding project for 2 p.m. At 2:20, three of "
            "the seven people have arrived. The head of office speaks for twenty minutes about how important "
            "the project is. Someone asks who will be encoding on Thursdays. Nobody knows. The meeting ends "
            "at 3:30 with no decisions, and two collectors leave unsure whether the project is starting this "
            "week or next month.",
            "The charter was signed. The scope was clear. The objective was measurable. What was missing was "
            "one well-run hour that turned those documents into a shared plan that every person in the room "
            "understood the same way.",
            "(Everyone and everything in this story is fictional, including the numbers. No real "
            "town or employee is described.)",
            "This part is about that hour. When you finish reading, you will have a one-hour kickoff agenda, a "
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
            ("h", "Quick Recap"),
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
        "date": "May 31, 2027",
        "title": "Project Management Series, Part 6: Writing Objectives That Actually Mean Something",
        "slug": "project-management-part-6-writing-objectives",
        "category": "pm",
        "summary": "“Improve billing” is a wish, not an objective. This part shows where the SMART idea came "
                   "from, why a SMART objective can still miss the point, and how to write objectives that "
                   "name a real outcome, a starting point and a target everyone can check.",
        "publish_on": "2027-05-31 21:00",
        "body": [
            "At the end of the encoding project, the team reports success. Every record in the four poblacion "
            "barangays is in the system. Fifty sample bills were printed and checked. The deadline was met. "
            "By every line of the plan, the project is done.",
            "Then January comes, and the line at the real property tax window is as long as last year’s. "
            "The bills print faster, but taxpayers still wait while staff look up past payments on ledger "
            "cards. The project delivered exactly what it promised. It just never promised the thing the "
            "head of office actually wanted: shorter waiting time at the counter.",
            "(The office and the people in this story are invented, and so are the figures. No real "
            "town or employee is described.)",
            "This part is about closing that gap. After this post, you will know where the SMART "
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
            ("h", "Quick Recap"),
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
        "date": "May 21, 2027",
        "title": "Project Management Series, Part 5: Waterfall, Agile or Hybrid? Choosing How to Run the Work",
        "slug": "project-management-part-5-waterfall-agile-hybrid",
        "category": "pm",
        "summary": ("Some projects should be planned in full before work begins. Others should be built in short "
                   "cycles and shown to users early. Some need a little of both. Two treasury projects show how "
                   "to tell which is which."),
        "publish_on": "2027-05-21 21:00",
        "body": [
            "Two projects land on the revenue clerk’s desk in the same month. The first is the encoding "
            "project from earlier parts: a fixed deadline of January 4, a signed scope statement, and rules "
            "for computing the tax that will not change before then. The second is new. The head of office "
            "wants a simple screen where counter staff can tell a taxpayer, in one glance, whether a "
            "property has unpaid balances. Nobody is sure yet what that screen should show.",
            "The clerk plans both the same way, with every task written out in advance. The first project "
            "runs smoothly. The second produces a carefully built screen that the counter staff find "
            "confusing on the first morning they use it, and most of the plan has to be redone.",
            "(Everyone and everything in this story is fictional, including the numbers. No real "
            "town or employee is described.)",
            "The problem was not the plan. It was the choice of approach. Read to the end and you will "
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
            ("h", "Quick Recap"),
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
        "date": "May 12, 2027",
        "title": "Project Management Series, Part 4: Drawing the Line Before Work Begins",
        "slug": "project-management-part-4-defining-scope",
        "category": "pm",
        "summary": ("The charter says what a project is for. The scope statement says exactly what it will "
                   "deliver, how everyone will know it is done, and what it will not do. This post shows how to "
                   "write one, using the treasury encoding project as the example."),
        "publish_on": "2027-05-12 21:00",
        "body": [
            "The encoding project has a charter and a stakeholder map. The work is under way. Then, in the same "
            "week, three small requests arrive. The assessor’s office asks whether the team could also add the "
            "owners’ mobile numbers. A collector suggests printing the bills in two languages. The head of office "
            "wonders aloud whether the system could also show which properties have never been visited.",
            "Each idea is reasonable. Each would take only “a little extra time.” Together, they could push the "
            "January deadline into March. The revenue clerk needs a clear way to say what the project includes, "
            "and a calm way to handle everything else.",
            "(The office and the people in this story are invented, and so are the figures. No real "
            "town or employee is described.)",
            "That clear way is the scope statement. In Part 2, the charter gave a short list of what was in and "
            "out. The scope statement goes one level deeper: it names each deliverable, says how everyone will know it is done, and becomes the page everyone checks when a new idea arrives. By the last section, you will have a five-part template, a filled-in example and a calm way to answer extra requests.",
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
            ("h", "Quick Recap"),
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
        "date": "May 3, 2027",
        "title": "Project Management Series, Part 3: Mapping Who Holds the Power",
        "slug": "project-management-part-3-stakeholder-mapping",
        "category": "pm",
        "summary": ("Every project has people who can help it, stop it or simply be affected by it. List them, "
                   "place them on a power and interest grid, and decide how to work with each one, with the "
                   "treasury encoding project as the example."),
        "publish_on": "2027-05-03 21:00",
        "body": [
            "The real property tax encoding project now has a signed one-page charter. The "
            "revenue clerk feels ready. Then, a week later, a message arrives from the office of "
            "the local chief executive. The mayor heard that “the treasury is changing the tax "
            "bills” and wants to know why nobody told the mayor’s office before taxpayers started"
            " asking.",
            "Nothing has gone wrong with the work. The encoding is on schedule. But someone with "
            "a great deal of power over the project was not on the clerk’s list, and now she must"
            " spend a day explaining instead of a minute informing.",
            "(Everyone and everything in this story is fictional, including the numbers. No real town or employee is described.)",
            "This part is about avoiding that day. It is about stakeholders: the people and "
            "groups who can affect a project or are affected by it. Finding them early, and "
            "deciding how to work with each one, is time well spent. By the end of this post, you will be able to list a project's stakeholders, place them on a power and interest "
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
            ("h", "Quick Recap"),
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
        "summary": ("A project charter is a short document that says why a project exists, what it will deliver, "
                   "who is in charge and who approved it. This post shows how to write one on a single page, "
                   "using a treasury encoding project as the example."),
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
            "(The office and the people in this story are invented, and so are the figures. No real town or employee is described.)",
            "This is the problem a project charter solves. It is the first document of a project,"
            " and in a small office it may be the only one you need. After this post, you will know the six parts of a one-page charter, see one written for a treasury "
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
            ("h", "Quick Recap"),
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
                ("A project can land on your desk without the title. Learn how a project differs from daily "
                "work, the three limits every project lives with, and four moves to make in your first two "
                "weeks.")
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
            ("h", "Quick Recap"),
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
