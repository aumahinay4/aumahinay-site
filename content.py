"""All site content lives here. Edit this file to update the website.

Anything marked TODO is a placeholder waiting for real content.
"""

SITE = {
    "name": "Ambrosio U. Mahinay",
    "short_name": "Butch Mahinay",
    "title": "Ambrosio “Butch” U. Mahinay, MPA",
    "tagline": "Public finance professional who builds software for local government.",
    "email": "hello@aumahinay.dev",
    "domain": "aumahinay.dev",
    "brand": "aumahinay",  # shown in the browser tab
    # TODO: add real profile links (or leave empty to hide them)
    "github": "",
    "linkedin": "",
    "coursera": "",
}

ABOUT = {
    "intro": (
        "I am a public administration professional with over 15 years in "
        "government service, more than 13 of them in local government fiscal "
        "administration and treasury operations. I designed and built "
        "ALTOS, the Automated Local Treasury Operations System."
    ),
    "paragraphs": [
        (
            "I currently serve as Acting Municipal Treasurer of Sampaloc, Quezon, "
            "where I lead fiscal management, revenue forecasting, fund custody, and "
            "disbursement under RA 7160."
        ),
        (
            "My technical background started with Computer System Design & "
            "Programming at AMA Computer Learning Center. I began learning on "
            "Coursera through Google Career Certificates (GCC) in 2020, during the pandemic, in Mulanay, Quezon, where I was "
            "first designated Acting Municipal Treasurer and served for two years. "
            "In 2024 I committed to the GCC program fully, and I have since completed seven Google Professional Certificates and "
            "three Google Specializations, covering data analytics, AI, cybersecurity, "
            "IT support, business intelligence, and project management."
        ),
        (
            "ALTOS is where both worlds meet: a working treasury system built in a "
            "real municipal office, where every rule of collecting, disbursing and "
            "reporting public money is written into the software."
        ),
    ],
    "experience": [
        {
            "role": "Acting Municipal Treasurer",
            "org": "Municipality of Sampaloc, Quezon",
            "period": "Sep 2024 – Present",
            "points": [
                "Lead municipal fiscal management, revenue forecasting, fund custody and disbursement.",
                "Sign disbursement vouchers and checks.",
            ],
        },
        {
            "role": "Local Revenue Collection Officer III",
            "org": "Provincial Treasurer's Office, Province of Quezon",
            "period": "2019 – Present",
            "points": [
                "Performed LRCO IV supervisory duties (Sep 2022 – Sep 2024) over provincial cash receipts.",
                "Supervised Cash Receipt Division collectors and audited collection reports.",
            ],
        },
        {
            "role": "Acting Municipal Treasurer",
            "org": "Municipality of Mulanay, Quezon",
            "period": "Aug 2020 – Aug 2022",
            "points": [
                "Directed treasury operations and managed LGU depository funds under DOF-BLGF designation.",
                "Maintained the day-to-day treasury operations of the municipality.",
            ],
        },
        {
            "role": "Part-Time Lecturer",
            "org": "Manuel S. Enverga University Foundation, Catanauan, Quezon",
            "period": "2010",
            "points": [
                "Taught college courses as a part-time lecturer.",
            ],
        },
        {
            "role": "Punong Barangay",
            "org": "Barangay government",
            "period": "2002 – 2010",
            "points": [
                "Served as the elected head of the barangay government.",
            ],
        },
    ],
    "education": [
        ("Master in Public Administration (MPA)", "Manuel S. Enverga University Foundation", "2014"),
        ("BS Public Administration (ETEEAP)", "Manuel S. Enverga University Foundation", "2008"),
        ("Computer System Design & Programming", "AMA Computer Learning Center", "2000"),
    ],
    "eligibilities": [
        "Intermediate Competency on Local Treasury Examination (ICLTE) – 2018",
        "Basic Competency on Local Treasury Examination (BCLTE) – 2017",
        "Career Service Professional Eligibility – 2012",
    ],
    "skills": [
        "Python", "Flask", "SQLite / SQL", "pandas", "Tkinter", "openpyxl", "ReportLab",
        "React + TypeScript", "Tableau", "Spreadsheets", "Linux", "AI-assisted development",
        "Public fiscal administration", "Project management",
    ],
}

# The one featured project. Source: "360° Accountability – The ALTOS Principles" (draft, Oct 2026).
ALTOS = {
    "name": "ALTOS",
    "full_name": "Automated Local Treasury Operations System",
    "motto": "Every peso, every step, every officer: 360°.",
    "where": "For Philippine local treasuries",
    "years": "2024 – 2026",
    "summary": (
        "Much of the daily work in a Philippine local treasury is still done by hand, from "
        "receipts and cash books to monthly reports, so reporting is slow and errors are hard "
        "to catch. ALTOS is my answer to that gap. It automates the full cycle of public money: "
        "official receipts, remittances and deposits, checks and cash advances, the monthly "
        "reports of accountable officers, and collection targets and results. One database "
        "serves both a desktop application and a web application across the office network."
    ),
    "principle": (
        "Public money must be traceable in a full circle, from the moment it is collected to "
        "the moment it is reported, with a named officer answerable at every point. "
        "Accountability that covers 300 degrees leaves a gap, and money leaks through gaps."
    ),
    "movements": [
        ("Collect", "Taxes, fees and charges, each acknowledged by an official receipt from a bonded collector.", "OR · RCD · deposit"),
        ("Disburse", "Releases by check, cash advance or transfer, each resting on an appropriation and a voucher.", "Voucher · check · cash advance"),
        ("Report", "Every collection and release summarized, reconciled and reported on fixed dates.", "RAAF · CRAAF · RCI · BRS · SRE"),
    ],
    "features": [
        ("Built from the forms", "Every screen starts from an LTOM or COA form, so the system stays auditable."),
        ("Rules, not just records", "The next OR number is always the next in series, a check cannot predate its booklet, and the 20% Development Fund cannot be switched off."),
        ("Deadlines that count down", "RAAF and CRAAF reports are due on the 5th, and the days remaining are visible to the officer and the supervisor."),
        ("The sealed ledger", "Every activity-log entry carries an HMAC-SHA256 code chained to the one before it, so any deletion or change shows."),
        ("Security Center", "Organized by the NIST Cybersecurity Framework: hashed passwords (PBKDF2-SHA256), lock-out, 15-minute auto log-out, AES-256 encrypted backups and a restore drill."),
        ("Correction without concealment", "Posted records are corrected only through a logged Data Correction with a reason and an author."),
        ("Turnover built in", "Assembles and verifies the records and produces a certificate for the incoming treasurer."),
        ("Data Analytics and Insights", "Targets, forecasts and control checks that inform the treasurer's decisions, plus a quarterly ALTOS Framework self-assessment that prints as a signed report."),
    ],
    "principles": [
        ("Legality first", "Every collection and release traces to a law, ordinance or appropriation."),
        ("Every peso has a document", "No collection without a receipt, no release without a voucher."),
        ("Every document has an owner", "A named, bonded officer answers for each form and each peso."),
        ("Every owner has a deadline", "Reports fall due on fixed dates, and the days remaining are visible."),
        ("Every record has a seal", "Posted records change only through a visible, logged correction."),
        ("Separate the hands", "No one person both authorizes and releases public money."),
        ("Keep money in its fund", "Each peso stays in the fund the law assigns it, including SEF and the 20% DF."),
        ("The taxpayer is a citizen", "Assess fairly, collect conveniently and disclose fully."),
        ("Evidence before decision", "Targets and forecasts inform the treasurer's judgment but never replace it."),
        ("Build to outlast the builder", "Systems must work after the incumbent leaves."),
    ],
    "book": {
        "title": "360° Accountability: Public Fiscal Administration in Philippine Local Treasuries",
        "subtitle": "The ALTOS Principles",
        "status": "Draft edition, October 2026",
        "blurb": (
            "A book that joins public administration theory, from Wilson and Weber to New Public "
            "Governance, with Philippine treasury law and the lessons of building ALTOS. It ends "
            "with the ALTOS Framework: ten principles any local treasury can adopt, with or without software."
        ),
    },
    "stack": ["Python", "SQLite", "Desktop app", "Web app", "HMAC-SHA256 audit log", "AES-256 backups", "NIST CSF"],
}

# Subsystems of ALTOS (functioning and ready as of Oct 2026). ALTOS is the mother system.
SUBSYSTEMS = [
    {
        "code": "Treasury Collection System",
        "name": "Collections subsystem",
        "movement": "Collect + Report",
        "status": "Ready",
        "summary": "A subsystem of ALTOS for collections and their reports: official receipts, collectors and their OR series, remittances and deposits, the daily RCD, and the monthly RAAF and CRAAF.",
    },
    {
        "code": "Treasury Disbursement System",
        "name": "Disbursements subsystem",
        "movement": "Disburse + Report",
        "status": "Ready",
        "summary": "A subsystem of ALTOS for disbursements and their reports: vouchers, checks, cash advances and their liquidation, the check register and disbursement reports.",
    },
]

_VERIFY = "https://coursera.org/verify/"

CERTIFICATES = [
    {
        "name": "Google IT Support",
        "kind": "Professional Certificate",
        "date": "Oct 22, 2026",
        "courses": 5,
        "verify": _VERIFY + "professional-cert/CRZVFUULJNRE",
        "course_list": [
            "Technical Support Fundamentals",
            "The Bits and Bytes of Computer Networking",
            "Operating Systems and You: Becoming a Power User",
            "System Administration and IT Infrastructure Services",
            "IT Security: Defense against the digital dark arts",
        ],
    },
    {
        "name": "Google Data Analytics",
        "kind": "Professional Certificate",
        "date": "Jun 28, 2026",
        "courses": 9,
        "verify": _VERIFY + "professional-cert/E0JEW0NXIVVM",
        "course_list": [
            "Foundations: Data, Data, Everywhere",
            "Ask Questions to Make Data-Driven Decisions",
            "Prepare Data for Exploration",
            "Process Data from Dirty to Clean",
            "Analyze Data to Answer Questions",
            "Share Data Through the Art of Visualization",
            "Introduction to Data Analysis Using Python",
            "Google Data Analytics Capstone: Complete a Case Study",
            "Accelerate Your Job Search with AI",
        ],
    },
    {
        "name": "Google AI",
        "kind": "Professional Certificate",
        "date": "Feb 22, 2026",
        "courses": 7,
        "verify": _VERIFY + "professional-cert/2OOV8LM3C9J4",
        "course_list": [
            "AI Fundamentals",
            "AI for Brainstorming and Planning",
            "AI for Research and Insights",
            "AI for Writing and Communicating",
            "AI for Content Creation",
            "AI for Data Analysis",
            "AI for App Building",
        ],
    },
    {
        "name": "Google Business Intelligence",
        "kind": "Professional Certificate",
        "date": "Jan 20, 2026",
        "courses": 4,
        "verify": _VERIFY + "professional-cert/BZ7AH4CKWTWD",
        "course_list": [
            "Foundations of Business Intelligence",
            "The Path to Insights: Data Models and Pipelines",
            "Decisions, Decisions: Dashboards and Reports",
            "Accelerate Your Job Search with AI",
        ],
    },
    {
        "name": "Google Advanced Data Analytics",
        "kind": "Professional Certificate",
        "date": "Dec 8, 2025",
        "courses": 7,
        "verify": _VERIFY + "professional-cert/7EJJ9PUOQRYW",
        "course_list": [
            "Foundations of Data Science",
            "Go Beyond the Numbers: Translate Data into Insights",
            "The Power of Statistics",
            "Regression Analysis: Simplify Complex Data Relationships",
            "The Nuts and Bolts of Machine Learning",
            "Google Advanced Data Analytics Capstone",
            "Accelerate Your Job Search with AI",
        ],
    },
    {
        "name": "Google Cybersecurity",
        "kind": "Professional Certificate",
        "date": "Jun 12, 2025",
        "courses": 9,
        "verify": _VERIFY + "professional-cert/F3O4NGXZHEK9",
        "course_list": [
            "Foundations of Cybersecurity",
            "Play It Safe: Manage Security Risks",
            "Connect and Protect: Networks and Network Security",
            "Tools of the Trade: Linux and SQL",
            "Assets, Threats, and Vulnerabilities",
            "Sound the Alarm: Detection and Response",
            "Automate Cybersecurity Tasks with Python",
            "Put It to Work: Prepare for Cybersecurity Jobs",
            "Accelerate Your Job Search with AI",
        ],
    },
    {
        "name": "Google Project Management",
        "kind": "Professional Certificate",
        "date": "Jun 12, 2025",
        "courses": 7,
        "verify": _VERIFY + "professional-cert/EMINF7IAB67Y",
        "course_list": [
            "Foundations of Project Management",
            "Project Initiation: Starting a Successful Project",
            "Project Planning: Putting It All Together",
            "Project Execution: Running the Project",
            "Agile Project Management",
            "Capstone: Applying Project Management in the Real World",
            "Accelerate Your Job Search with AI",
        ],
    },
    {
        "name": "Google Stakeholder Management",
        "kind": "Specialization",
        "date": "Jul 2, 2026",
        "courses": 3,
        "verify": _VERIFY + "specialization/Z2D1F8QX3PFT",
        "course_list": [
            "Working Effectively with Stakeholders",
            "Organizing Communication and Documentation",
            "Leadership and Influencing Skills",
        ],
    },
    {
        "name": "Google AI Essentials",
        "kind": "Specialization",
        "date": "May 27, 2026",
        "courses": 5,
        "verify": _VERIFY + "specialization/JF8AXADZEAOU",
        "course_list": [
            "Introduction to AI",
            "Maximize Productivity With AI Tools",
            "Discover the Art of Prompting",
            "Use AI Responsibly",
            "Stay Ahead of the AI Curve",
        ],
    },
    {
        "name": "Google People Management Essentials",
        "kind": "Specialization",
        "date": "May 24, 2026",
        "courses": 4,
        "verify": _VERIFY + "specialization/NMUKBA0KYH3S",
        "course_list": [
            "Create a High-Performing Team",
            "Set and Achieve Team Goals",
            "Support Individual Growth and Development",
            "Grow as a Manager",
        ],
    },
]

# Government and professional trainings (non-Coursera)
TRAININGS = [
    ("Financial Education (10-hr Leadership & Management Training)", "Civil Service Institute, CSC", "Mar 2025"),
    ("Public Sector Employees' Organization Seminar (8 hrs)", "Civil Service Institute, CSC", "May 2025"),
    ("Orientation on the Local Road Management Performance Assessment Tool", "DILG Region IV-A", "Mar 2022"),
    ("1st Virtual Regional Conference of Local Assessors and Treasurers", "BLGF Region IV-A", "Dec 2021"),
    ("BLGF–PCOO Webinar on FOI Memorandum Circulars", "Bureau of Local Government Finance", "Nov 2021"),
]

# IT news, newest first. To add a story, copy one block below, paste it at the TOP of
# the list and change the words. Keep summaries short and in your own words, and always
# link to the original article.
NEWS = [
    {
        "date": "October 25, 2026",
        "topic": "Cybersecurity",
        "title": "DDoS attacks on Philippine telecom networks more than double",
        "summary": (
            "Data from security firm StormWall shows telecommunications accounted for a quarter of "
            "DDoS attacks in the Philippines from January to August 2026, with attacks on telecom "
            "networks up 118% from a year earlier and their average size about five times larger."
        ),
        "why": (
            "Government offices that serve citizens and accept payments online depend on these same networks, so stronger protection keeps public services running."
        ),
        "source": "The Manila Times",
        "url": "https://www.manilatimes.net/2026/10/25/business/sunday-business-it/ddos-attacks-on-ph-telecoms-surge/2453202",
    },
    {
        "date": "October 21, 2026",
        "topic": "Digital ID",
        "title": "DICT opens ₱496-million tender for National ID verification infrastructure",
        "summary": (
            "The Department of Information and Communications Technology is bidding out one year of "
            "cloud, security and identity-verification services for its National ID eVerify program, "
            "with a 99.5% uptime guarantee. Bids are due November 9, 2026."
        ),
        "why": (
            "Quick, reliable ID checks help government offices confirm who they are dealing with, which cuts paperwork and helps prevent fraud."
        ),
        "source": "Biometric Update",
        "url": "https://www.biometricupdate.com/202610/philippines-launches-7-8m-tender-for-national-digital-id-infrastructure",
    },
    {
        "date": "October 19, 2026",
        "topic": "E-government",
        "title": "Electronic notarization launches nationwide",
        "summary": (
            "The Philippines formally launched electronic notarization in Taguig City. The Supreme "
            "Court, the Land Registration Authority and the SEC issued joint guidelines for accepting "
            "e-notarized documents, with identities checked through the DICT's eVerify service. "
            "Linking it to the eGov platform is in final testing."
        ),
        "why": (
            "Documents that used to need a personal appearance before a notary can now be handled and verified online, saving citizens time and travel."
        ),
        "source": "Daily Tribune",
        "url": "https://tribune.net.ph/2026/10/19/philippines-launches-nationwide-electronic-notarization",
    },
    {
        "date": "September 21, 2026",
        "topic": "AI in government",
        "title": "eGovPH app gets an AI assistant",
        "summary": (
            "The DICT added eGovAI to the eGovPH Super App, including the \"Kuya AI\" assistant, "
            "to help citizens find information, navigate government services and complete "
            "transactions, with identity checks, document handling and translation built in."
        ),
        "why": (
            "An assistant that guides people step by step can mean fewer queues, fewer repeat visits and easier access to government services."
        ),
        "source": "Marketech APAC",
        "url": "https://marketech-apac.com/dict-brings-ai-powered-government-services-to-filipinos-through-egovai/",
    },
]


# Blog posts written by Butch, newest first. To add one, copy this shape:
# {
#     "date": "November 3, 2026",
#     "title": "Why local treasuries need automation",
#     "slug": "why-local-treasuries-need-automation",  # short, lowercase, hyphens
#     "summary": "One or two sentences shown above the post.",
#     "publish_on": "2026-11-03",  # optional: hidden until this date; None keeps it hidden
#     "body": [
#         "A paragraph.",
#         ("h", "A subheading"),
#         ("photo", "blog/photo.jpg", "Caption", "small"),  # file in static/blog/; size small/medium/omit for full; skipped until it exists
#         ("quote", "A highlighted line."),
#         ("source", "Text before ", "link text", "https://...", " text after."),  # small note with a link
#     ],
# },
BLOG = [
    {
        "date": "December 27, 2026",
        "title": "The ALTOS Framework, Principle 10: Build to Outlast the Builder",
        "publish_on": "2026-12-27",  # goes live on this date (Philippine time)
        "slug": "altos-framework-build-to-outlast-the-builder",
        "summary": "Records, rules and systems must keep working after the person who set them up has left. A reform "
                   "that leaves with its author was never an institution.",
        "body": [
            "Every treasurer eventually leaves. Some are transferred, some retire, and an acting treasurer's "
            "designation has a fixed end from the very first day. The question this last principle asks is "
            "uncomfortable but necessary: if I left tomorrow, what would stop working?",
            ("quote", "An institution is a set of rules and records strong enough that a stranger can take over "
             "tomorrow and carry on without loss."),
            ("h", "The File Outlives the Official"),
            "We have met Max Weber several times in this series, and he belongs at the end too. His point that the "
            "file outlives the official is the institutional heart of the treasury. Treasurers, mayors and collectors "
            "change. The obligations of the municipality and the rights of taxpayers do not.",
            "Our system already leans this way. The Local Treasury Operations Manual, 2nd Edition, issued under DOF "
            "Department Order No. 085-2019 of December 3, 2019, writes down standard procedures and forms so that every office does the "
            "work the same way, and so that a newly assigned treasurer does not have to start from zero. It is to "
            "the treasury what Frederick Taylor's instruction cards were to the factory. And because the treasurer "
            "is appointed by the Secretary of Finance, the office is meant to carry on professionally from one "
            "administration to the next.",
            ("h", "Rules That Last"),
            "Elinor Ostrom spent her career studying communities that managed shared resources for generations. What "
            "made their arrangements last was not one good leader but durable rules that people understood, "
            "monitored and accepted as their own. A treasury reform should aim for the same thing: rules that hold "
            "even after the person who wrote them is gone.",
            ("h", "Digital Change Done Right"),
            "Patrick Dunleavy and his colleagues described digital-era governance in 2006: bringing fragmented "
            "services back together, organizing them around citizens' needs, and using digital change as the "
            "engine. They also warned against simply digitizing a broken process. When I built ALTOS, I first "
            "redrew the paper flow, and only then automated it. Building it in a working treasury taught me several "
            "lessons that I believe apply to any local government:",
            ("point", "Start from the form", "Every page should begin with an official form, so the system stays "
             "auditable."),
            ("point", "Encode the rule, not just the record", "A rule in a manual depends on someone's memory. A rule "
             "built into the system applies even on the busiest day."),
            ("point", "One database, many doors", "ALTOS serves a desktop application and a web application from one "
             "database, so the two can never disagree. Two systems that each hold part of the truth are worse than "
             "one that holds all of it."),
            ("point", "Design for people who are not the developer", "Use the words of the treasury, not of "
             "programmers. Name buttons for the act, such as “Submit RAAF.” The test is whether a "
             "collecting officer with no computer training can use it correctly on the first day."),
            ("h", "Continuity Is a Public Obligation"),
            "When a treasury runs on one computer, that computer becomes a single point of failure. Closing one "
            "laptop can stop every collector in the office. A public system needs a continuity plan that answers "
            "three questions: where does the system run when the main machine is away, who can restore it, and how "
            "long can the office work on paper in the meantime?",
            "Executive Order 170 itself requires agencies that adopt digital payments to keep a business continuity "
            "plan. The options include a reserve machine, the municipality's own server run by its information "
            "technology office, or a documented fallback to manual forms with encoding afterward. Whatever the "
            "choice, the restore must be tested. A backup that has never been restored is a hope, not a control.",
            ("h", "Turnover Is Part of the Design"),
            "Turnover should not be a scramble in the last week. ALTOS includes a turnover function that gathers the "
            "office's records, checks them, and produces a certificate for the incoming officer. The goal is "
            "Weber's: the file outlives the official, and the next person receives a working office, not a puzzle.",
            ("h", "Settle Ownership Early"),
            "Software written by a public official raises a question that is easy to put off: who owns it, and who "
            "may use it after the author leaves? Under the Intellectual Property Code (RA 8293), there is no "
            "copyright in a work of the Government, meaning a work created as part of an official's regularly "
            "prescribed duties. For works made in the course of employment, the employer owns the copyright only "
            "when the work comes from regularly assigned duties, unless the parties agree otherwise. Writing "
            "software is not among the duties the law gives a local treasurer, but every case depends on its facts.",
            "So the practical advice is to settle it in writing, early. Keep a dated record of authorship. Register "
            "or deposit the work with the Intellectual Property Office of the Philippines where appropriate. Agree "
            "through a memorandum of agreement or license on how the local government may use, maintain and host "
            "the system after the developer leaves. And get legal advice before any commercial use. I wrote more "
            "about why this protects everyone in my earlier post, Why I Built ALTOS. Clear terms mean the "
            "municipality keeps a working system and its records, the developer keeps the authorship, and taxpayers "
            "keep uninterrupted service.",
            ("h", "The Practitioner Can Be the Builder"),
            "Local governments usually face two choices for treasury software: buy a package that does not quite fit "
            "their rules, or wait for a national system. ALTOS suggests a third path. Someone who knows the law and "
            "the forms, and who learns modern data and digital skills, can build a tool that fits the office "
            "exactly.",
            "Those skills are no longer locked inside universities. Much of what ALTOS needed I learned through six "
            "Google Professional Certificates, about 750 hours of online study: Cybersecurity, Project Management, "
            "Data Analytics, Advanced Data Analytics, Business Intelligence and AI. The courses supplied the method. "
            "The treasury supplied the problems. My Master in Public Administration supplied the reason: public "
            "value, accountability and the public interest. I believe future treasurers, budget officers and "
            "accountants should learn data skills as part of their training, not as an extra. The best person to "
            "digitize a process is often the one who has done it by hand.",
            ("h", "What Digital Transformation Is Not"),
            "It is not buying computers. It is not scanning paper. It is not a website. In a treasury, digital "
            "transformation means that the rules of public finance are carried out, recorded and reported by a "
            "system that any authorized person can check, and that keeps working when the people change.",
            ("h", "The Question to Ask"),
            "Would this work tomorrow without me? The evidence is a turnover certificate, a restore that has actually "
            "been tested, and written agreements on use and ownership. In the ALTOS Framework self-assessment, the "
            "age of the latest encrypted backup is one of the things the system shows before the treasurer gives a "
            "rating.",
            ("h", "Closing the Circle"),
            "That completes the ten. Looking back, you can see how each principle leans on the ones before it. "
            "Legality without documents cannot be proved. Documents without owners cannot be enforced. Owners "
            "without deadlines can delay forever. Deadlines without seals produce reports no one can trust. And all "
            "of it fails if it ends when the builder leaves.",
            ("quote", "Every peso, every step, every officer, and every year after I leave: that is the full "
             "circle, 360°."),
            "The framework works best as a self-assessment. Rate your office on each principle from 1, meaning "
            "absent, to 4, meaning practiced and backed by evidence. Find the two weakest, and start there. In ALTOS "
            "this lives under Sysadmin \u203a Analytics \u203a ALTOS Framework, on both the desktop and the web. For "
            "each principle the system first shows what its own records say. The treasurer then gives a rating with "
            "a note. Ratings are kept per quarter, the two weakest principles are named, and the whole assessment "
            "prints as a signed report. With or without software, these are the ten questions I ask myself:",
            ("point", "1", "Can I name the law or ordinance behind every account on our receipts?"),
            ("point", "2", "Is there any peso we receive or release without a form?"),
            ("point", "3", "Is every accountable officer bonded today, for the right amount?"),
            ("point", "4", "Which report is due next, and who is likely to be late?"),
            ("point", "5", "If someone changed a posted record last night, how would I know?"),
            ("point", "6", "Where in my office does one person act alone, and what makes up for it?"),
            ("point", "7", "Is every fund kept in its own account and shown separately in our reports?"),
            ("point", "8", "What would a farmer from our farthest barangay say about paying taxes here?"),
            ("point", "9", "What did the figures tell me this month, and what did I decide because of them?"),
            ("point", "10", "If I left tomorrow, what would stop working?"),
            "The principles can also serve as a teaching outline for public fiscal administration, pairing each one "
            "with its founding thinker and its Philippine law. And because they are a practitioner's theory, they "
            "should be tested. Does rule-enforcing collection raise local revenue in fourth- and fifth-class "
            "municipalities? Do visible deadlines reduce late RAAF, CRAAF and RCD submissions? Which delinquency "
            "notices, by timing and channel, lead to payment? Do statistical screening tools predict COA audit "
            "findings? How did the larger NTA after Mandanas-Garcia change local revenue effort and the use of the "
            "20% Development Fund? Do digital payment channels widen or narrow access for rural and elderly "
            "taxpayers? What makes a local digital reform survive a change of treasurer? How should local "
            "governments and developer-officials settle the ownership of in-house software? And how well do local "
            "treasuries protect taxpayer data under the Data Privacy Act? I hope graduate students and scholars "
            "will take these up.",
            "The founders of public administration built their theories by studying their own governments. Filipino "
            "practitioners and scholars can do the same with ours. Our records are rich, our rules are explicit, and "
            "our results can be measured. Every municipal treasury is a laboratory.",
            ("ask", "If you rated your own office on these ten principles, which two would come out weakest? I'd be "
             "glad to hear, and to compare notes."),
        ],
},
    {
        "date": "December 20, 2026",
        "title": "The ALTOS Framework, Principle 9: Evidence Before Decision",
        "publish_on": "2026-12-20",  # goes live on this date (Philippine time)
        "slug": "altos-framework-evidence-before-decision",
        "summary": "Targets, forecasts and control checks should inform the treasurer's judgment, never replace it. "
                   "Every number is a prompt for a human decision.",
        "body": [
            "A treasury produces a mountain of records for the sake of accountability: receipts, deposit reports, "
            "check registers, payment histories. It is easy to think of them only as things to file and submit. "
            "But there is another way to see them. The same records that prove we handled money correctly are also "
            "the best evidence we have for managing it well.",
            ("quote", "Every result is a prompt for a human decision, never an automatic action."),
            ("h", "The Question Every Budget Hearing Asks"),
            "In 1940, V. O. Key wrote a short article called “The Lack of a Budgetary Theory.” His question "
            "was simple and still unanswered: on what basis should money go to activity A instead of activity B? It "
            "is the central question of every budget hearing.",
            "The treasurer does not decide how money is allocated. But the treasurer's income estimate sets the "
            "ceiling for every allocation. An honest, evidence-based estimate of local revenue is the treasurer's "
            "contribution to Key's question.",
            "Aaron Wildavsky showed in 1964 that budgets are usually made by small adjustments to last year's base, "
            "through bargaining between “guardians” who protect the money and “advocates” who "
            "want to spend it. The treasurer is a guardian, and guardians earn trust by being right about the cash. A "
            "treasurer whose estimates are consistently realistic gains a voice in budget talks. One whose estimates "
            "keep missing loses it.",
            ("h", "Why We Measure"),
            "Robert Behn argued in 2003 that public managers measure performance for eight different purposes: to "
            "evaluate, control, budget, motivate, promote, celebrate, learn and improve. Each purpose needs a "
            "different measure. A treasurer who uses one number, such as total collections, for everything will "
            "misread the office. Collection efficiency tells you whether you are improving. The timeliness of RCDs "
            "tells you about control. A target met tells you when it is time to celebrate.",
            ("h", "From the Classroom to the Counter"),
            "The Google Data Analytics Professional Certificate, which I completed in 2025, teaches a six-phase "
            "process. I was surprised how naturally each phase fits treasury work:",
            ("point", "Ask", "Define a question that is specific, measurable, action-oriented, relevant and "
             "time-bound (SMART), and know who needs the answer. For example: will real "
             "property tax reach its target by December, and if not, which barangays are behind?"),
            ("point", "Prepare", "Find data that is reliable, original, comprehensive, current and cited (ROCCC). In a "
             "treasury that means receipts, RCDs, the assessment roll and payment histories, each with a known "
             "owner, drawn from the transactions themselves rather than typed in again."),
            ("point", "Process", "Clean the data by removing duplicates, filling or flagging gaps and checking "
             "outliers: duplicate tax declarations, missing owners, impossible values."),
            ("point", "Analyze", "Look for patterns: seasons, trends, who pays after receiving a notice."),
            ("point", "Share", "Present findings clearly to the people who decide, such as a monthly report to the "
             "mayor and the Sanggunian, or the posted statement of receipts and expenditures."),
            ("point", "Act", "Decide, follow through, and measure again: schedule barangay collection days, send "
             "notices, adjust targets."),
            "Two lessons from that training shaped ALTOS more than any other. First, the language of the data "
            "matters. ALTOS keeps its records in an SQL database and is written in Python, the same tools those "
            "courses teach, so any analyst trained in them can work with its data. Second, data ethics comes with "
            "data skills. When ALTOS exports data for analysis in tools like Jupyter or Google Colab, it removes "
            "names and addresses first, in keeping with the Data Privacy Act.",
            ("h", "Targets and Results"),
            "Targets came into the treasury with New Public Management, and income estimates are the treasurer's "
            "answer to Key. ALTOS keeps annual targets for eight revenue sources, following the grouping of the "
            "statement of receipts and expenditures: Real Property Tax – Basic, Special Education Tax, Tax on "
            "Business, Other Taxes, Regulatory Fees, Service and User Charges, Receipts from Economic Enterprises, and "
            "Other Receipts. Collections are compared with targets by month and by source, and each year is compared "
            "with the year before.",
            ("h", "Measures That Admit What They Do Not Know"),
            "Collection efficiency for real property tax sounds simple, but it hides a trap. ALTOS divides what was "
            "collected this year by the total of what was collected and what is still collectible, counting only "
            "properties whose payment history is recorded. Properties without a history are counted separately, with "
            "their annual tax as an estimate, so the office can see how complete its picture really is. A ratio that "
            "hides how much it covers invites false confidence.",
            "Forecasts follow the same spirit. Every budget season, someone asks the treasurer what the year will "
            "bring. ALTOS forecasts year-end collections from the seasonal pattern of up to three past years, or "
            "from a straight-line trend when there is not enough history, and it reports an 80% range along with the "
            "chance of reaching the target. A forecast with a range is honest about uncertainty. A single number "
            "pretends to know.",
            ("h", "What Deeper Analysis Can Show"),
            "The Google Advanced Data Analytics Professional Certificate taught hypothesis testing, regression and clustering. In "
            "ALTOS these methods are applied to the treasury's own records instead of a textbook dataset:",
            ("point", "Do notices work?", "A two-proportion z-test compares owners who paid within 30 days of a notice "
             "with delinquent owners who received none, to decide whether notices are worth the staff time."),
            ("point", "Who is likely to pay?", "A logistic regression on past notice results suggests which delinquent "
             "accounts to visit first. While history is thin, a simple, transparent rule is used instead."),
            ("point", "Taxpayer groups", "K-means clustering groups properties by payment behavior, so reminders and payment "
             "arrangements can be tailored."),
            ("point", "Internal control checks", "Statistical flags point to cancelled receipts, delays in preparing "
             "RCDs, unusual collection days, duplicates and amounts just under a threshold, showing where to look "
             "first in a surprise review."),
            ("point", "Assessment roll quality", "Checks for duplicates, missing data and outliers, to be corrected "
             "together with the assessor."),
            "One of these checks uses Benford's law. In many natural sets of financial figures, the leading digit 1 "
            "appears about 30% of the time, and 9 less than 5% of the time. Invented figures rarely follow this "
            "pattern. Auditors use it to decide where to look, not as proof of anything, and ALTOS uses it the same "
            "way.",
            ("h", "The Test of a Good Idea"),
            "Mark Moore's Creating Public Value (1995) asks public managers to think like entrepreneurs for the "
            "public. His strategic triangle tests any initiative against three questions. "
            "Is it valuable to the public? Is it legitimate and supported by those who authorize it? Is it "
            "operationally possible? I tested ALTOS against that triangle. Its value is faster, cleaner records and "
            "timely reports. Its legitimacy rests on following the Local Treasury Operations Manual, COA rules and "
            "the Data Privacy Act. Its operational capacity was the hardest test of all: one laptop, one office "
            "network, and a small staff.",
            ("h", "Why Good Records Matter Beyond the Audit"),
            "Evidence also shapes how a municipality is seen from outside. Under the Automatic Income Classification "
            "Act (RA 11964), signed on October 26, 2023, provinces, cities and municipalities are sorted into five income classes based on their average regular "
            "income over three years, with a general reclassification every three years. That class affects "
            "salaries, borrowing capacity and eligibility for programs. Accurate treasury records are therefore not "
            "only an audit matter. They help decide the municipality's class. The Seal of Good Local Governance, "
            "institutionalized by RA 11292 in 2019, likewise looks at financial administration and sustainability. "
            "Its indicators, such as growth in locally sourced revenue, compliance with full disclosure and the use "
            "of funds, are far easier to show when the treasury's records are complete and searchable.",
            ("h", "The Limits of Numbers"),
            "Herbert Simon's bounded rationality cuts both ways. Analytics narrows attention to what matters, but it "
            "also hides whatever is not measured. Campbell's law warns that the more an indicator is used to make "
            "decisions, the more it can distort the very work it was meant to measure. A treasurer who rewards "
            "collectors only on volume may get volume at the cost of the receipt. What gets measured gets managed, "
            "and what does not get measured gets neglected.",
            "The safeguard is to pair every target with a control measure. Track collections together with RCD "
            "timeliness. Track notices sent together with complaints received. And never let a number make the "
            "decision on its own.",
            ("h", "The Question to Ask"),
            "What do the figures say, and what will I decide? Or at the end of each month: what did the figures tell "
            "me this month, and what did I decide because of them? The evidence is targets, forecasts and findings "
            "reviewed every month. In the ALTOS Framework self-assessment, revenue targets that have not yet been "
            "set are among the first things flagged.",
            "Evidence helps a treasurer decide well today. The last principle asks a harder question: will any of "
            "this still work when that treasurer is gone? Build to outlast the builder.",
            ("ask", "Which number do you watch most closely in your office, and has it ever misled you? I'd like to "
             "hear your experience."),
        ],
},
    {
        "date": "December 13, 2026",
        "title": "The ALTOS Framework, Principle 8: The Taxpayer Is a Citizen",
        "publish_on": "2026-12-13",  # goes live on this date (Philippine time)
        "slug": "altos-framework-the-taxpayer-is-a-citizen",
        "summary": "Assess fairly, collect conveniently and disclose fully. The person at the counter is not a "
                   "customer buying a service but a citizen funding a shared project.",
        "body": [
            "The first seven principles are mostly about the inside of the treasury: laws, forms, officers, "
            "deadlines, seals, signatures and funds. The eighth turns around and looks at the person standing at the "
            "window. How we treat that person decides whether everything else feels like public service or like a "
            "wall.",
            ("quote", "What would a farmer from our farthest barangay say about paying taxes here?"),
            ("h", "Adam Smith's Four Tests"),
            "In The Wealth of Nations (1776), Adam Smith set out four maxims for a good tax. Two and a half "
            "centuries later they remain the best test I know of a collection system:",
            ("point", "Equality", "People pay in proportion to their ability. Our Local Government Code says the same: "
             "local taxes must be equitable and based, as far as practicable, on ability to pay."),
            ("point", "Certainty", "The amount and the due date are clear, not arbitrary. In practice this means a "
             "printed bill and a receipt that shows the legal basis of every charge."),
            ("point", "Convenience", "The tax is collected at a time and in a way that suits the payer: payment "
             "windows, barangay collection days, and payment through banks and e-wallets."),
            ("point", "Economy", "The cost of collecting a tax should be small compared with what it brings in. A fee "
             "that costs more to collect than it yields has failed this test."),
            "ALTOS computes real property tax from the assessed value and the ordinance rate, so the taxpayer and "
            "the collector see exactly the same figure. That is Smith's certainty in a single screen.",
            ("h", "Fairness Is Part of the Job"),
            "After the Second World War, public administration began asking a harder question than “how do we "
            "run things efficiently?” It asked “efficient for whom, and toward what end?” Dwight "
            "Waldo showed in 1948 that every choice about efficiency is also a choice about values. No administrator "
            "is merely a technician.",
            "This applies to the treasurer more than we usually admit. Deciding which delinquent taxpayers to pursue "
            "first, or when to schedule market collections, affects who carries the burden of government. Those are "
            "real choices, and the treasurer must be able to explain them in public terms.",
            "In 1968 the first Minnowbrook Conference, convened by Waldo, gathered young scholars who argued that "
            "government should pursue social equity, not only economy and efficiency. H. George Frederickson later "
            "called social equity the third pillar of public administration. In a treasury, equity looks very "
            "practical: payment points people can actually reach, receipts in plain language, and no informal "
            "“fixers.” A citizen from a distant barangay should face the same procedure and the same cost "
            "as someone who lives beside the municipal hall.",
            ("h", "The Same Rules for Everyone"),
            "Equity has an older ally in Max Weber's idea of impersonal treatment. The procedure is the same for every "
            "taxpayer, from the largest business in town to the smallest farm. The same rate table applies to "
            "everyone, whoever they know and whoever is mayor. Fair treatment is not a favor the office grants. It "
            "is the rule.",
            ("h", "Citizens, Not Customers"),
            "Public choice theory, associated with James Buchanan and Gordon Tullock, treated public officials like "
            "everyone else: as people who respond to incentives. In the 1980s and 1990s that thinking fed New Public "
            "Management, which Christopher Hood described in 1991 as hands-on professional management, explicit "
            "standards and measures of performance, a focus on outputs, and private-sector styles of management. "
            "David Osborne and Ted Gaebler popularized it in Reinventing Government (1992) as \u201csteering rather "
            "than rowing,\u201d and with it came the habit of calling taxpayers \u201ccustomers.\u201d Some of that "
            "was useful. The citizen's charter "
            "required by the Anti-Red Tape Act (RA 9485, amended by RA 11032) carries the mark of that era, "
            "along with collection targets and collection efficiency ratios.",
            "Robert and Janet Denhardt answered with what they called the New Public Service. Citizens are not "
            "customers. A customer buys something for personal use. A taxpayer funds a shared project. Treating "
            "taxpayers as citizens means explaining where their money goes: posting the statements of receipts and "
            "expenditures, answering questions patiently at the counter, and treating complaints as a form of "
            "participation rather than a nuisance.",
            ("h", "Rules People Accept as Their Own"),
            "Elinor Ostrom, who received the Nobel Memorial Prize in Economic Sciences in 2009, showed in Governing the "
            "Commons that communities can manage shared resources well through rules they make and monitor "
            "themselves. Her design principles, among them clear boundaries, monitoring, graduated sanctions and "
            "low-cost ways to settle disputes, read like a guide to good local revenue administration. Market fees, "
            "fishery rentals and the barangay share of real property tax all depend on rules that local people "
            "accept as fair. A rule people resent is a rule people avoid.",
            ("h", "Full Disclosure"),
            "Reports do not only go upward to COA and the national agencies. They also go outward, to the people who "
            "paid. The Full Disclosure Policy of the Department of the Interior and Local Government requires local "
            "governments to post key financial documents, including the annual budget, statements of receipts and "
            "expenditures, and procurement information, in conspicuous places and online. Philippine good governance "
            "is often summed up in four words: transparency, accountability, participation and predictability. "
            "Disclosure serves all four.",
            ("h", "Going Digital Without Leaving Anyone Behind"),
            "Executive Order 170 of 2022 encourages local governments to accept digital payments while keeping cash "
            "and traditional methods available. Both halves matter. E-payment is a real convenience for many "
            "taxpayers, but an elderly landowner in a remote barangay may still prefer to pay in cash on collection "
            "day. Whether digital channels widen or narrow access for rural and elderly taxpayers is a question I "
            "hope researchers will study closely.",
            "Stephen Osborne's New Public Governance (2006) describes a state that delivers services through networks "
            "of public, private and civic partners, and Patrick Dunleavy's digital-era governance asks that services "
            "be rebuilt around what citizens need. Payments through banks and payment channels, data exchange with "
            "the Bureau of Local Government Finance and online access to statements are that network at work. The "
            "test is whether our systems connect around the citizen, rather than making the citizen connect them.",
            "And one line should never be crossed:",
            ("quote", "Convenience for the citizen must never come at the cost of the receipt."),
            "Taxpayer records also deserve protection. Names, addresses, property holdings and payments are personal "
            "information under the Data Privacy Act. Respecting the citizen includes keeping their data safe. When "
            "ALTOS exports data for analysis, names and addresses are removed first.",
            ("h", "Paying Taxes as Local Citizenship"),
            "Own-source revenue measures how far a municipality funds itself. Every peso of local revenue widens the "
            "room for local choice, and it builds the habit of paying for local services that makes local democracy "
            "real. Even with a larger National Tax Allotment, I see local revenue effort as a measure of a town's "
            "fiscal citizenship. People who pay are entitled to a say, and to an account of what was done with their "
            "money.",
            ("h", "The Question to Ask"),
            "Is it fair, easy and public? The evidence is several ways to pay, including ones that reach the far "
            "barangays, and a statement of receipts and expenditures that is actually posted where people can see "
            "it.",
            "Treating taxpayers fairly requires knowing who pays, who does not, and why. That calls for evidence, "
            "and evidence calls for judgment. The ninth principle is about how to hold the two together: evidence "
            "before decision.",
            ("ask", "What is the one change that would make paying local taxes easier where you live? I'd love to "
             "hear it."),
        ],
},
    {
        "date": "December 6, 2026",
        "title": "The ALTOS Framework, Principle 7: Keep Money in Its Fund",
        "publish_on": "2026-12-06",  # goes live on this date (Philippine time)
        "slug": "altos-framework-keep-money-in-its-fund",
        "summary": "A peso raised for schools should reach schools. Each peso belongs to the fund the law assigns it, "
                   "and it should stay there.",
        "body": [
            "Money in a local treasury is not one big pile. It is divided into funds, and each fund exists because a "
            "law or an ordinance said what that money is for. Mixing them, even briefly and with good intentions, "
            "turns a legal promise into a guess.",
            ("quote", "Every peso has an address. The law decides which fund it lives in, and the treasury's job is "
             "to make sure it gets there and stays there."),
            ("h", "The Funds of a Municipality"),
            "A Philippine municipality's money sits in the funds that the Local Government Code and the budget "
            "create. The main ones are the General Fund, the Special Education Fund and the Trust Fund. Within the "
            "budget, the 20% Development Fund is set aside for development projects. Each fund should have its own "
            "accounts in the books and, where required, its own bank account.",
            ("h", "Why Funds Exist at All"),
            "The economist Richard Musgrave, in The Theory of Public Finance (1959), divided the fiscal role of "
            "government into three branches: allocation, which means providing public goods; distribution, which "
            "means adjusting how income is shared; and stabilization, which means smoothing the ups and downs of the "
            "economy. Local governments mostly do allocation: roads, health centers, markets, waste collection. "
            "Distribution and stabilization belong mainly to the national government.",
            "Funds are how allocation is kept honest. When a law says a certain tax must pay for schools, or a "
            "certain share must go to development, a separate fund is the bookkeeping that keeps that promise "
            "visible. Charles Tiebout argued in 1956 that people \u201cvote with their feet\u201d among local "
            "governments that offer different mixes of taxes and services. Wallace Oates followed in 1972 with the "
            "idea that each public service should be provided by the lowest level of government that covers the area "
            "it benefits. The Local Government Code of 1991 put that idea into practice by devolving health, "
            "agriculture, social welfare and other services. Funds tie the money to those services.",
            "Devolution also left a lasting gap between what local governments must spend and what they can raise "
            "on their own. Economists at the Philippine Institute for Development Studies, notably Rosario G. "
            "Manasan, documented this imbalance and how heavily many municipalities depend on national transfers. "
            "This is why the allotment from the national government exists: it moves money from where it is raised "
            "to where services are needed. And because that money arrives with conditions attached, keeping it in "
            "the right fund is how a town shows it kept those conditions.",
            ("h", "One Receipt, Two Funds"),
            "Real property tax is the clearest everyday example. The basic tax and the Special Education Fund levy "
            "under Section 235 are often paid together, on one receipt. But they belong to different funds. The SEF "
            "portion must be recorded in its own fund, deposited in its own account, and shown separately in the "
            "reports. In a province, the basic real property tax collected by the municipal treasurer is also "
            "shared among the province, the municipality and the barangays.",
            "In ALTOS, when one receipt carries charges for two funds, the system records one portion per fund. Each "
            "fund's RCD and bank account then receives exactly its own share, without anyone having to split the "
            "amount by hand at the end of the day.",
            ("h", "The 20% Development Fund"),
            "Section 287 of the Local Government Code requires each local government to set aside at least 20% of "
            "its annual allotment from the national government for development projects. The main guidelines are in "
            "DBM-DOF-DILG Joint Memorandum Circular No. 1 of November 4, 2020, with later circulars adding detail, "
            "for example on the Community-Based Monitoring System in 2023. A September 2026 news report said new "
            "guidelines would also allow energy-related projects; as with any circular, check its number and text "
            "before relying on it.",
            ("h", "What Mandanas-Garcia Changed"),
            "The 1987 Constitution, in Article X, Section 6, promises local governments a just share in national "
            "taxes, released to them automatically, and Section 7 adds an equitable share in the proceeds of national "
            "wealth found in their areas. For almost thirty years, that share was called the Internal Revenue "
            "Allotment, because it was computed only from internal revenue taxes. In the consolidated "
            "cases Mandanas v. Ochoa and Garcia v. Ochoa (G.R. Nos. 199802 and 208488), decided on July 3, 2018, the "
            "Supreme Court ruled that the just share must be computed from all national taxes, including customs "
            "collections, and struck down the words \u201cinternal revenue\u201d in Section 284 of the Code. Since "
            "fiscal year 2022 the share has been released as the National Tax Allotment (NTA).",
            "To match the bigger share with bigger responsibilities, Executive Order 138 of June 1, 2021 ordered the "
            "full devolution of certain national functions to local governments, and Executive Order 103 of "
            "November 6, 2025 extended the transition period.",
            "For the treasurer, this has two consequences. A larger NTA means a larger 20% Development Fund in pesos, "
            "and with it closer scrutiny of how that fund is used. The 20% Development Fund has become the clearest "
            "test of whether the bigger allotment turns into development or simply disappears into day-to-day "
            "operations. A larger allotment can also deepen a town's reliance on transfers. My own view is that a bigger allotment "
            "makes local revenue effort more important, not less.",
            ("h", "Keeping Inflows and Outflows Apart"),
            "Keeping money in its fund also means not short-circuiting the books. Collections should not be used to "
            "pay expenses directly at the window. Money comes in, is deposited intact in the right account, and only "
            "then goes out, from the fund that holds the appropriation, through that fund's own bank account. "
            "Electronic payments follow the same rule: they are recorded against the bank account the payment channel "
            "credited.",
            ("h", "Where ALTOS Helps"),
            "The 20% Development Fund, with its code 100-DF and its account, Share from National Tax Allotment – "
            "20% Development Fund, is built into every ALTOS database. It cannot be renamed, deactivated or separated, "
            "so it is always visible in collections, disbursements and reports. Check booklets are recorded by bank "
            "account, so every check is tied to the account it is drawn on. In the ALTOS Framework self-assessment, the system lists any fund that has no bank account and any "
            "bank account not yet reconciled.",
            ("h", "The Question to Ask"),
            "Is each peso in the right fund and the right bank account? Or, put as a monthly check: is every fund "
            "kept in its own account and shown separately in our reports? The evidence is the Special Education Fund "
            "and the 20% Development Fund appearing separately, every time, in every report.",
            "So far the principles have looked inward, at the law, the forms, the officers and the funds. The eighth "
            "principle turns to face the counter, and the person standing on the other side of it: the taxpayer is a "
            "citizen.",
            ("ask", "Has your office ever had to untangle money recorded in the wrong fund? I'd like to hear how you "
             "caught it."),
        ],
},
    {
        "date": "November 29, 2026",
        "title": "The ALTOS Framework, Principle 6: Separate the Hands",
        "publish_on": "2026-11-29",  # goes live on this date (Philippine time)
        "slug": "altos-framework-separate-the-hands",
        "summary": "No one person should both approve and release public money, or both hold it and record it. "
                   "Trust in a treasury has to be designed, not assumed.",
        "body": [
            "Segregation of duties sounds like a phrase from an auditor's checklist, and in a way it is. It is also "
            "the oldest internal control in public finance, and one of the kindest. The rule is simple: no single "
            "person should be able to start a transaction, approve it, record it and then hide it.",
            ("quote", "When every step has a second pair of eyes, no one has to carry suspicion alone."),
            ("h", "Why Trust Must Be Designed"),
            "Under the third principle we met principal–agent theory: the idea that the person doing the work "
            "usually knows more than the person relying on it. The theory does not assume that officers are "
            "dishonest. It assumes only that they know things others do not.",
            "Good people make mistakes. A mistake that one person can both make and conceal, even without meaning to, "
            "can grow quietly into a loss. A well-designed office protects honest staff just as much as it deters "
            "dishonest ones. Checks built into the work are not an accusation against anyone. They are what allow "
            "honest people to show that they are honest.",
            ("h", "Old Ideas, Modern Frameworks"),
            "Henri Fayol listed division of work among his principles of management more than a century ago, and in a "
            "treasury it begins with keeping collection apart from disbursement. Max Weber's "
            "bureaucracy splits authority among offices so that each checks the next. Today the international "
            "reference is the Internal Control – Integrated Framework of the Committee of Sponsoring "
            "Organizations of the Treadway Commission, usually called COSO. The International Organization of "
            "Supreme Audit Institutions adopted it for the public sector, and in the Philippines the Department of "
            "Budget and Management's National Guidelines on Internal Control Systems apply the same ideas to "
            "government. All of them describe five components:",
            ("point", "Control environment", "The tone at the top. A treasurer who follows the same rules as "
             "everyone else."),
            ("point", "Risk assessment", "Knowing where losses can happen: remote collection points, cash advances, "
             "bank accounts that are not reconciled."),
            ("point", "Control activities", "Approvals, segregation, physical custody and reconciliations, such as "
             "the four signatures on a voucher and the monthly bank reconciliation."),
            ("point", "Information and communication", "Reliable, timely records reaching the right people: RCDs, "
             "RAAFs, cash books and alerts."),
            ("point", "Monitoring", "Ongoing and separate checks, such as surprise cash counts, the COA audit and the "
             "review of exception reports."),
            ("h", "Four Signatures on Every Payment"),
            "The Local Government Code builds separation directly into spending. Under Section 344, no money may be "
            "paid unless the budget officer certifies that an appropriation exists, the accountant certifies that it "
            "has been obligated and the papers are complete, and the treasurer certifies that the cash is available. "
            "The local chief executive then approves the payment. Four officers, four different questions, and no "
            "single one of them can both authorize and release the money.",
            ("h", "What Must Be Kept Apart"),
            "In daily treasury work, four pairs of duties should never sit in the same hands without a check:",
            ("point", "Custody and recording", "The person who holds the cash should not be the only one who records "
             "it."),
            ("point", "Collection and disbursement", "Money coming in should not be used directly to pay money going "
             "out. It should pass through the bank and the books first."),
            ("point", "Authorization and release", "The officer who approves a payment should not be the one who "
             "hands over the check."),
            ("point", "Doing and correcting", "The officer who made an entry should not be able to change it quietly "
             "afterward."),
            ("h", "How ALTOS Divides the Work"),
            "ALTOS gives each user one of four roles, and each role sees only the pages its duties require:",
            ("point", "Collecting Officer", "Issues receipts from an assigned series and prepares and submits their "
             "own RCD and RAAF. Cannot change a posted receipt or RCD, and cannot act for another officer."),
            ("point", "Liquidating Officer", "Receives the collectors' RCDs, prepares the consolidated RCD and the "
             "CRAAF, and monitors RAAFs. Cannot submit another officer's RAAF or change posted records."),
            ("point", "Disbursing Officer", "Prepares checks from assigned booklets, records releases, and reports "
             "the RCI, RD and LR. Cannot change posted checks or reports."),
            ("point", "System Administrator", "Sets up funds, accounts, forms, officers and bonds, and makes "
             "corrections. Cannot correct a record without stating a reason that is logged."),
            "The most important rule in the whole system is a short one: only the System Administrator changes data "
            "that has already been encoded. Everyone else asks for a correction, and the request, the reason and the "
            "author are all recorded.",
            ("h", "The Small-Office Problem"),
            "Here is the honest difficulty. Many municipal treasuries have only a handful of people. Perfect "
            "separation is not always possible, and sometimes one person must wear two hats.",
            "When that happens, compensating controls take over. The treasurer reviews that person's work more "
            "often. Cash is counted by surprise. Someone outside the cash function reconciles the bank accounts every "
            "month. Exception reports highlight anything unusual. ALTOS can supply the exception reports, but it "
            "cannot supply the review. That part is still the treasurer's job.",
            ("h", "The Rule Must Bind the Top"),
            "The real test of segregation is whether it applies to the person with the most power. In ALTOS the "
            "System Administrator, often the treasurer, has the widest access, and for exactly that reason is the "
            "most completely logged. When the administrator opens another user's page to help, every action is "
            "recorded as the administrator acting for that user.",
            ("quote", "Power and visibility should grow together. The audit trail exists first for the person who "
             "could most easily do without it."),
            ("h", "The Question to Ask"),
            "Did anyone act alone? In an office review the question becomes: where in my office does one person act "
            "alone, and what makes up for it? The evidence is four certifications on every voucher and a bank "
            "reconciliation done by someone independent of the cash. In the ALTOS Framework self-assessment, bank "
            "accounts that have not yet been reconciled are among the first things the system shows.",
            "Separating the hands protects how money moves. The next principle protects where it rests: keep money "
            "in its fund.",
            ("ask", "How does your office handle segregation of duties with a small staff? I'd like to hear what "
             "compensating controls work for you."),
        ],
},
    {
        "date": "November 22, 2026",
        "title": "The ALTOS Framework, Principle 5: Every Record Has a Seal",
        "publish_on": "2026-11-22",  # goes live on this date (Philippine time)
        "slug": "altos-framework-every-record-has-a-seal",
        "summary": "Once a record is posted, it can be corrected, but only in the open: with a reason, a name and a "
                   "trace that anyone can check.",
        "body": [
            "Old cash books had a quiet virtue that we rarely talk about. They were bound, and their pages were "
            "numbered. If someone tore out a page or scraped away a figure, it showed. The book carried its own proof "
            "that it had not been tampered with.",
            "A database has no pages. Anyone with enough access can change a number and leave no mark at all. This "
            "is the uncomfortable truth about going digital: it removes an old safeguard, and unless something "
            "replaces it, an electronic record is actually weaker evidence than the paper it replaced.",
            ("quote", "A sealed record is not a frozen one. Mistakes can be fixed, but never silently."),
            ("h", "The File That Outlives the Official"),
            "Max Weber observed that in a modern bureaucracy the file outlives the official. Treasurers, mayors and "
            "clerks change. The records stay, and the next person must be able to trust them. That only works if the "
            "file does not depend on the honesty of whoever happens to hold it today. Any tampering must be visible "
            "to whoever reads it tomorrow.",
            ("h", "What the Law Expects"),
            "Four sets of laws and rules shape how treasury records must be protected:",
            ("point", "Data Privacy Act of 2012 (RA 10173)", "Taxpayer names, addresses, property holdings and "
             "payments are personal information. The municipality is a personal information controller and must "
             "protect them with organizational, physical and technical measures. The National Privacy Commission "
             "requires notice of certain breaches within 72 hours of discovery."),
            ("point", "Cybercrime Prevention Act of 2012 (RA 10175)", "Unauthorized access to, or interference with, "
             "a government system is a crime."),
            ("point", "Commission on Audit rules", "Accounting records and supporting documents must be preserved and "
             "made available to the auditor."),
            ("point", "Electronic Commerce Act of 2000 (RA 8792)", "Electronic documents can be accepted as evidence, "
             "but only if their integrity can be shown."),
            "The last point is the heart of this principle. A digital record that cannot prove it is unchanged may "
            "not hold up when it matters most.",
            ("h", "How a Seal Works"),
            "In ALTOS, every entry in the activity log carries a cryptographic code (an HMAC-SHA256) computed from two things: the entry itself and "
            "the code of the entry before it. Each entry is linked to the one before, like links in a chain. The key "
            "used to make these codes is kept outside the database. If anyone deletes or alters an entry, every code "
            "after it stops matching, and the integrity check reports exactly where the chain breaks.",
            "You do not need to understand the mathematics to understand the idea. It is the digital version of the "
            "numbered page. The difference is that a torn page only shows that something is missing, while a broken "
            "chain shows where.",
            ("h", "Correction Without Concealment"),
            "Errors still happen, and they must still be fixed. The rule is that a correction is a new event, with "
            "its own reason and its own author, not a silent overwrite of the old one. It is the same rule we have "
            "always followed for a spoiled official receipt: mark it, keep it, explain it.",
            "In ALTOS, posted receipts, RCDs and reports can be corrected only by the System Administrator, through a "
            "Data Correction page. The officer who found the mistake asks for the correction. The correction, its "
            "reason and the person who made it all go into the sealed log.",
            ("h", "Security as a Framework, Not a Feature"),
            "Protecting records is broader than the log. For the rest, I followed the Cybersecurity Framework of the "
            "U.S. National Institute of Standards and Technology (NIST), which I learned to use as a working tool in "
            "the Google Cybersecurity Professional Certificate I completed in 2025. Its original five functions organize the ALTOS Security "
            "Center. Version 2.0, released in 2024, added a sixth, Govern, which places security under the "
            "leadership of the organization. In a treasury, that responsibility rests with the treasurer.",
            ("point", "Identify", "A self-assessment of every safeguard, showing its current status."),
            ("point", "Protect", "Passwords stored only in scrambled, one-way form, so that no one, not even the "
             "administrator, can read them; passwords that expire and cannot be reused; lock-out after repeated wrong "
             "attempts; automatic log-out after 15 minutes idle for every user, administrator included; and "
             "backups encrypted with AES-256."),
            ("point", "Detect", "The tamper-evident log, plus security events such as failed log-ins, log-ins "
             "outside office hours, password resets, data corrections and changes to settings, and a check that the "
             "program files themselves have not been altered."),
            ("point", "Respond", "An incident register with step-by-step playbooks, including the 72-hour notice to "
             "the National Privacy Commission for personal data breaches."),
            ("point", "Recover", "Encrypted backups whose recovery key is kept on paper by the System Administrator, "
             "and a restore drill that actually decrypts and checks the latest backup."),
            ("h", "Five Lessons for Any Office Going Digital"),
            "Whatever system your local government uses, these lessons apply:",
            ("point", "Keep secrets apart", "Passwords, encryption keys and backups do not belong in shared folders or "
             "in copies of the program."),
            ("point", "Encrypt the connection", "Any link that carries taxpayer data across a network should be "
             "encrypted before the system goes live."),
            ("point", "Test the restore", "A backup that has never been restored is a hope, not a control."),
            ("point", "Write down who sees what", "Then make the system enforce it."),
            ("point", "Plan for bad days", "The lost laptop, the failed server, and the staff member who leaves."),
            ("h", "The Digital Fidelity Bond"),
            "Security is not something to add at the end, once the screens are done. I have come to think of it as "
            "the digital form of the fidelity bond we discussed under the third principle. The bond guarantees that "
            "public money will be made whole. Security guarantees that the public's money and the public's records "
            "will still be there, unchanged, tomorrow.",
            ("h", "The Question to Ask"),
            "Could anyone change this without leaving a trace? Or, as a treasurer might put it at the start of the "
            "day: if someone changed a posted record last night, how would I know? The evidence of this principle is "
            "an intact audit log and corrections that each carry a stated reason. In the ALTOS Framework "
            "self-assessment, the system checks the integrity of the sealed log and the age of the latest encrypted "
            "backup before the treasurer gives a rating.",
            "Without seals, even reports filed on time cannot be fully trusted. With seals in place, the next "
            "question is who was allowed to do what in the first place. The sixth principle answers it: separate the "
            "hands.",
            ("ask", "If your office moved from paper to a computer system, what took the place of the bound, numbered "
             "cash book? I'd like to hear how you handled it."),
        ],
},
    {
        "date": "November 15, 2026",
        "title": "The ALTOS Framework, Principle 4: Every Owner Has a Deadline",
        "publish_on": "2026-11-15",  # goes live on this date (Philippine time)
        "slug": "altos-framework-every-owner-has-a-deadline",
        "summary": "A deadline is not paperwork. It sets a limit on how long a mistake or a shortage can stay hidden.",
        "body": [
            "Every treasury officer knows the feeling of the 5th of the month approaching. It is easy to treat "
            "deadlines as a burden imposed from above, one more thing that gets in the way of the real work. I want "
            "to argue the opposite. In a treasury, the deadline is one of the most useful controls we have.",
            ("quote", "A shortage found on the 5th of the next month is at most five weeks old. A shortage found at "
             "the year-end audit can be thirteen months old."),
            ("h", "A Record Is Not Yet a Report"),
            "There is a difference between keeping a record and making a report. A record shows that something "
            "happened. A report shows that someone stood up and answered for it. Until the report is made, what the "
            "officer knows stays private. The report is the moment that private knowledge becomes the institution's "
            "knowledge, open to the treasurer, the accountant, the auditor and, eventually, the public.",
            "Luther Gulick saw this in 1937 when he summed up an executive's work in the acronym POSDCORB: Planning, "
            "Organizing, Staffing, Directing, Coordinating, Reporting and Budgeting. Two of those seven letters, "
            "Reporting and Budgeting, are about money and records. If you want to see Gulick's list in its most "
            "concrete form, visit a municipal treasury.",
            ("h", "The Calendar of a Treasury"),
            "Each report has a form, an owner, a deadline and a reader. These are the regular ones:",
            ("point", "Report of Collections and Deposits (RCD)", "Prepared by each collecting officer, and by the "
             "liquidating officer for consolidated collections, every time collections are deposited or remitted, "
             "usually daily. It lists every receipt issued and every deposit made, by fund and bank account."),
            ("point", "Cash books", "Kept by the treasurer and by the collecting, liquidating and disbursing officers, "
             "posted daily and closed monthly."),
            ("point", "RAAF and CRAAF", "The Report of Accountability for Accountable Forms (Annex 16 of Book II of "
             "the Local Treasury Operations Manual) is prepared by each accountable officer, and the consolidated "
             "CRAAF (Annex 17) by the liquidating officer. Both are due on or before the 5th of the following month."),
            ("point", "Disbursement reports", "The Report of Checks Issued is prepared as checks are issued. The "
             "Report of Disbursements and the Liquidation Report are prepared as each cash advance is used and "
             "settled, within the period the Commission on Audit prescribes."),
            ("point", "Bank reconciliation", "Every month the accountant, working with the treasury, matches the book "
             "balance of every bank account against the bank statement."),
            ("point", "Statement of Receipts and Expenditures (SRE)", "Prepared by the treasurer and sent quarterly to "
             "the Bureau of Local Government Finance."),
            ("point", "Daily cash position", "Cash available by fund, needed every day before the treasurer can "
             "certify that funds are available."),
            "Collection itself has seasons too. January brings business permit renewals, the first-quarter or "
            "full-year payment of real property tax, and most community tax certificates. Real property tax "
            "installments fall due every quarter, and market fees come in daily. A treasurer who plans staff and cash "
            "handling around that calendar is applying Gulick's Planning and Staffing to the most practical task in "
            "government.",
            ("h", "Why We Need the Days Counted for Us"),
            "Herbert Simon, who later received the Nobel Memorial Prize in Economic Sciences, showed in his 1947 book Administrative "
            "Behavior that people make decisions with limited time, information and attention. He called this "
            "bounded rationality. A treasurer cannot personally read every receipt in the office, and no amount of "
            "extra effort will change that.",
            "Simon's lesson is that the answer is not more effort but better design of information. Show people only "
            "what needs their attention now: exception reports, alerts and simple counters. A screen that says "
            "“your RAAF is due in two days” does more for compliance than a memo reminding everyone that "
            "reports are due on the 5th.",
            ("h", "Visible to Both the Officer and the Supervisor"),
            "A deadline works best when two people can see it: the officer who owes the report and the supervisor who "
            "is waiting for it. If only the officer knows, it is easy to let it slide. If only the supervisor knows, "
            "the officer is caught by surprise. When both see the same count of days, the conversation happens "
            "before the deadline, not after.",
            ("h", "Where ALTOS Helps"),
            "ALTOS computes the RAAF and CRAAF deadline for every month. Each officer's home page shows how many days "
            "are left, or “due today,” or how many days overdue. The liquidating officer sees which RAAFs "
            "have not yet arrived. Each submission is recorded with its date, and a late one is marked with the "
            "number of days it was late. Only the System Administrator can cancel a submission recorded by mistake, "
            "and only by stating a reason.",
            "The system also gathers the office's recurring deadlines into one compliance calendar. Some items come "
            "straight from the records and clear themselves once done: RAAFs and CRAAFs for each officer and month, "
            "fidelity bonds expiring or missing, official receipts not yet included in an RCD, and cash advances not "
            "yet liquidated. Others are standing deadlines the System Administrator can edit, such as the last day "
            "to pay the quarter's real property tax without interest, the posting of the notice of delinquency, "
            "business permit renewals and quarterly business tax installments, the SRE to the Bureau of Local "
            "Government Finance, and the monthly bank reconciliation.",
            "Each default deadline names its legal basis. Where a date depends on a circular that may have changed, "
            "the calendar says so and asks the user to verify it. I think that honesty matters. A calendar that "
            "admits it might be out of date is safer than one that pretends to know everything.",
            ("h", "Reports Built From the Same Records"),
            "One more rule makes deadlines meaningful. A report should be prepared from the same records that "
            "produced the transactions, not retyped from a separate list. Otherwise the report can drift away from "
            "the facts, and meeting the deadline only means delivering the wrong numbers on time.",
            ("h", "Late Reporting Breaks the Loop"),
            "The three movements of public money (collect, disburse and report) form a loop rather than a line. "
            "Reports feed the next round of targets and budgets, which shape the next round of collections. An "
            "office that collects well but reports late breaks the loop just as surely as one that reports on time "
            "but collects poorly.",
            ("h", "The Question to Ask"),
            "What is due, and by when? And the harder follow-up: which report is due next, and who is likely to be "
            "late? The evidence of this principle in practice is RAAFs and CRAAFs submitted on time and RCDs prepared "
            "without lag.",
            "Deadlines make officers report. But a report is only worth something if its numbers cannot be quietly "
            "changed after it is filed. That brings us to the fifth principle: every record has a seal.",
            ("ask", "Which report in your office is most often late, and why? I'd be interested to hear what has "
             "helped."),
        ],
},
    {
        "date": "November 8, 2026",
        "title": "The ALTOS Framework, Principle 3: Every Document Has an Owner",
        "publish_on": "2026-11-08",  # goes live on this date (Philippine time)
        "slug": "altos-framework-every-document-has-an-owner",
        "summary": "A receipt that belongs to everyone belongs to no one. Every form in custody and every peso in hand "
                   "needs a named, bonded officer who answers for it.",
        "body": [
            "Imagine a booklet of official receipts lying on a desk that three clerks share. One page is missing. "
            "Who explains it? If the honest answer is “we are not sure,” the office has a problem, and it "
            "is not a problem about honesty. It is a problem about ownership.",
            ("quote", "Accountability needs a name. Every form in custody and every peso in hand should have one "
             "person who answers for it, and that person should be bonded."),
            ("h", "Why a Name Matters: The Principal and the Agent"),
            "Economists have a useful way of describing this. Principal–agent theory, developed by Michael "
            "Jensen, William Meckling and others, looks at any relationship in which one party, the principal, "
            "relies on another, the agent, who knows more and whose interests may differ. The usual remedies are "
            "contracts, monitoring and incentives that narrow the gap in information.",
            "Local government is a long chain of such relationships. Citizens elect the mayor and the Sanggunian. "
            "The mayor and the Sanggunian rely on the treasurer. The treasurer relies on the collecting officers. At every link, the person "
            "doing the work knows more than the person who depends on it. The theory does not assume anyone is "
            "dishonest. It only assumes that information is uneven.",
            "Accountable forms, fidelity bonds, reports with deadlines and audit trails are all tools for closing that "
            "gap. And none of them works unless each one is tied to a specific person. This is the economic logic "
            "behind what I call 360° accountability: a named officer answerable at every point of the circle.",
            ("h", "One Officer, One Superior"),
            "Henri Fayol, writing in 1916, listed unity of command among his principles of management: each person "
            "should take orders from one superior. In a treasury this means each collecting officer answers to one "
            "liquidating officer, who answers to the treasurer. Max Weber would recognize the rest. A collector is "
            "assigned to a particular market or barangay, which is a fixed jurisdiction, and the hierarchy runs "
            "upward from collector to liquidating officer to treasurer.",
            "When two people share one booklet, or a collector reports to whoever happens to be around, the chain "
            "breaks, and with it the ability to say who is responsible.",
            "Luther Gulick's list of an executive's duties points the same way. In a treasury, Staffing means "
            "designating bonded collecting, liquidating and disbursing officers, and Directing means assigning each "
            "one a collection area and putting it in an office order. Ownership starts with a written assignment.",
            ("h", "Who Holds What"),
            "An accountable officer is any official or employee whose duties require custody of government funds, "
            "property or accountable forms. In a municipal treasury the main roles are:",
            ("point", "Collecting officer", "Holds official receipts and the cash collected, and answers for every "
             "receipt in custody, used or unused, and every peso until it is deposited or remitted."),
            ("point", "Liquidating officer", "Receives the collectors' remittances and reports, checks each "
             "collector's RCD, consolidates collections, and prepares the monthly CRAAF."),
            ("point", "Disbursing officer", "Holds cash advances for payroll or petty expenses and answers for "
             "liquidating each one within the required period."),
            ("point", "Treasurer", "Has overall custody of funds, checks and forms, and answers for the whole "
             "treasury, including the acts of subordinates where supervision failed."),
            "That last line deserves attention. The treasurer's accountability is not only for what the treasurer "
            "personally touches. It extends to what the treasurer should have been watching.",
            ("h", "What the Government Auditing Code Says"),
            "Presidential Decree 1445 puts this into law. Every officer whose duties involve the possession or "
            "custody of government funds or property is accountable for them and liable for their safekeeping. The "
            "head of the agency carries primary responsibility for all funds and property under it, and those who "
            "handle them are directly accountable to the head. And under Section 101, every accountable officer must "
            "be properly bonded.",
            ("h", "The Fidelity Bond"),
            "A fidelity bond stands behind the officer: if public money in that officer's care is lost through the officer's "
            "fault, the government has a way to be made whole. Both Section 101 of PD 1445 and Section 305 of the Local Government "
            "Code require it. The Bureau of the Treasury administers the bonding system under its Revised Omnibus "
            "Regulations, Treasury Circular No. 02-2009, as later amended.",
            "Two details are easy to forget. First, the amount of the bond should follow the size of the "
            "accountability. A collector who now handles far more cash than when the bond was first set may be "
            "bonded for far too little without anyone noticing. Second, bonds expire. An officer whose bond lapsed last month is, "
            "on paper, holding public money with no guarantee behind it.",
            ("h", "Distance Calls for Stronger Ownership"),
            "Money is collected at the treasury windows, but also at markets and terminals, on barangay collection "
            "days, and through banks. Every one of these points needs a named collecting officer with forms in custody. The "
            "farther a collection point is from the office, the stronger the controls must be, because supervision "
            "there is weaker. Ownership is the control that travels with the collector.",
            ("h", "Accountability in Four Directions"),
            "Public administration usually describes accountability in three directions: upward to superiors and "
            "oversight bodies, downward to citizens, and sideways to peer offices and auditors. ALTOS adds a fourth "
            "direction: across time. A record must be just as trustworthy five years from now, under a different "
            "treasurer, as it is today. That is only possible if the record still says, years later, exactly who was "
            "responsible.",
            ("h", "Where ALTOS Helps"),
            "In ALTOS, every series of receipts and every check booklet is assigned to a named officer, and each user "
            "has one role that shows only the pages that role needs. An officer cannot act for another officer. When "
            "the System Administrator opens another user's page to help, every action there is recorded as done by "
            "the administrator acting for that user, so the name on the record is always the true one.",
            "The system also keeps each officer's bond amount and expiry date. By default it warns 60 days before a "
            "bond lapses. It compares each bond with the cash the officer actually handled and flags any bond that "
            "is missing, expired or too low. A rule that used to live in a filing cabinet has become a daily reminder "
            "on the screen.",
            ("h", "The Question to Ask"),
            "Who is answerable, and are they bonded? Put more sharply: is every accountable officer bonded today, for "
            "the right amount? The evidence is a current bond for every accountable officer, matched to what each "
            "one actually handles.",
            "Owners give documents their force. But an owner with no due date can always say “I will get to it "
            "later,” and later can stretch for months. The fourth principle closes that gap: every owner has a "
            "deadline.",
            ("ask", "When did your office last check every accountable officer's bond against what they actually "
             "handle? I'd be glad to hear what you found."),
        ],
},
    {
        "date": "November 1, 2026",
        "title": "The ALTOS Framework, Principle 2: Every Peso Has a Document",
        "publish_on": "2026-11-01",  # goes live on this date (Philippine time)
        "slug": "altos-framework-every-peso-has-a-document",
        "summary": "No collection without an accountable form, no release without a voucher. A peso that leaves no paper "
                   "behind cannot be accounted for.",
        "body": [
            "The first principle asked whether the law allows a transaction. The second asks a plainer question: "
            "where is the paper? A collection that was perfectly legal but never receipted looks, a year later, exactly "
            "like a collection that never happened. A payment that was properly approved but has no voucher looks "
            "exactly like money that simply disappeared.",
            ("quote", "If a peso moved and nothing was written, then as far as the public can tell, it never moved, or "
             "it moved for the wrong reasons."),
            ("h", "Why the Law Insists on a Form"),
            "The Government Auditing Code of the Philippines, Presidential Decree 1445 of 1978, is the backbone of "
            "accountability for public money. It requires every collection to be acknowledged, and it forbids paying "
            "any claim without the required documents and certifications. The official receipt you get at the "
            "treasury window exists because of that rule. So does the stack of papers attached to every check.",
            "The idea is older than our law. The German sociologist Max Weber described modern bureaucracy as "
            "authority that rests on written rules rather than on persons, and one of its marks is the written file. "
            "Officials come and go; the file stays. In a treasury the file is very concrete: the official receipt, "
            "the Report of Collections and Deposits, the cash book, the voucher and the check register.",
            ("h", "Accountable Forms: Paper That Counts Itself"),
            "Not every form is equal. An accountable form is a serially numbered form, such as an official receipt "
            "or a community tax certificate, for which the person holding it must answer. Real property tax is "
            "usually receipted on Accountable Form 56. Business taxes, fees and charges usually go on Accountable "
            "Form 51. The community tax has its own certificates for individuals and corporations.",
            "Serial numbers are what make these forms powerful. Because every receipt has a place in a sequence, a "
            "missing one is noticed. A gap in the series is a question someone must answer.",
            ("h", "The Life of an Official Receipt"),
            "Follow a single booklet of receipts through the office and you will see the principle at work at every "
            "step:",
            ("point", "Custody", "The forms arrive from the supplier and are recorded in the stock of accountable "
             "forms by serial number, before anyone uses them."),
            ("point", "Assignment", "A booklet or series is issued to a named collecting officer and recorded against "
             "that officer's accountability."),
            ("point", "Assessment", "The amount due is computed from the ordinance or the tax declaration, not agreed "
             "upon at the counter."),
            ("point", "Issue", "The receipt is issued in serial order and in date order, with every charge placed on "
             "its proper income account and fund."),
            ("point", "Deposit", "Collections are deposited intact, usually on the same or the next banking day, and "
             "listed in the Report of Collections and Deposits (RCD)."),
            ("point", "Accounting for the forms", "Every month, used, unused and cancelled forms are reported in the "
             "Report of Accountability for Accountable Forms (RAAF)."),
            "Notice that the paper trail begins before the first peso is collected. A receipt is accounted for from "
            "the moment it enters the stock room, not from the moment it is used. Henri Fayol, one of the early "
            "writers on management, listed “order” among his principles: a place for everything, and "
            "everything in its place. The stock room of accountable forms, where every booklet has a serial range and "
            "a custodian, is Fayol's order in its most literal form.",
            ("h", "One Best Way, but Not a Machine"),
            "Frederick Taylor's Principles of Scientific Management (1911) searched for the one best way to do each "
            "task through measurement and standardization. Standard forms, standard codes for income accounts and "
            "standard steps for issuing a receipt all come from that tradition, and so does measuring how long "
            "money takes to travel from the counter to the bank.",
            "The danger in Taylor's approach is treating people as parts of a machine. A good system standardizes the record, not "
            "the officer's judgment. ALTOS fixes how a receipt must be filled in, but it still leaves the officer "
            "free to decide the case in front of them, such as whether a taxpayer qualifies for a discount the "
            "ordinance allows.",
            ("h", "A Spoiled Receipt Is Never Thrown Away"),
            "Mistakes happen. A wrong amount is written, a name is misspelled, a carbon slips. The rule for this is "
            "one of the oldest controls in public finance: the spoiled receipt is never destroyed. It is marked "
            "cancelled, kept with all its copies, and reported. A correction is a new and visible act with a stated "
            "reason, never an erasure.",
            "This is worth stressing because it runs against instinct. The natural reaction to a mistake is to make "
            "it disappear. In a treasury, a missing receipt is far more alarming than a cancelled one.",
            ("h", "Going Out: The Voucher Behind Every Check"),
            "The same principle governs money leaving the treasury. There are three main ways it leaves, and each has "
            "its own paper:",
            ("point", "By check", "Checks come from a booklet in the custody of a disbursing officer, are prepared in "
             "serial and date order against an approved disbursement voucher, and are listed in the Report of Checks "
             "Issued (RCI)."),
            ("point", "By cash advance", "A disbursing officer receives an advance for a specific purpose, such as "
             "payroll, reports each payment in the Report of Disbursements (RD), and settles the advance through a "
             "Liquidation Report (LR), returning any balance."),
            ("point", "By electronic transfer", "Executive Order 170 of 2022 allows payment straight into a payee's "
             "bank or e-money account, but the same documents must stand behind it."),
            "Electronic collections follow the same logic. When a taxpayer pays through a bank or a payment channel, "
            "the receipt is issued once the credit to the municipality's account is confirmed, and the payment is "
            "recorded against the bank account that received it. A new channel does not mean a new exception to the "
            "rule.",
            ("h", "Start From the Form, Not the Screen"),
            "When I designed ALTOS, every page began with a form that already existed in the Local Treasury "
            "Operations Manual or in the rules of the Commission on Audit: the official receipt, the RCD, the RAAF, "
            "the check register, the liquidation report. The screen is only a way of filling in the form correctly. "
            "A system built around screens slowly drifts away from the law. A system built around forms stays "
            "auditable, because an auditor can lay the printout beside the paper version and see the same thing.",
            ("h", "Where ALTOS Helps"),
            "ALTOS turns several of these paper rules into things the computer simply will not allow:",
            ("point", "No skipped numbers", "The next official receipt number is always the next one in the series."),
            ("point", "No backdating", "A receipt cannot be dated before its series was issued, or before the last "
             "receipt in that series."),
            ("point", "No late additions", "Once an RCD has been prepared for a date, no receipt can be added on or "
             "before that date for the same officer and account."),
            ("point", "Cancellations stay visible", "A cancelled receipt remains in the series with its status and "
             "reason, the cancellation is logged under the user's name, and a receipt already included in an RCD can "
             "no longer be cancelled."),
            ("point", "Checks follow their booklets", "Check booklets are recorded by bank account and serial range, "
             "ranges may not overlap, checks are prepared in date order and cannot predate their booklet, and each "
             "check shows its voucher, whether it was released and to whom, and whether it is already in an RCI."),
            "In the ALTOS Framework self-assessment, one of the first things the system shows for this principle is "
            "any check that has no voucher number.",
            ("h", "The Question to Ask"),
            "For this principle the self-check is short: is there any peso we receive or release without a form? The "
            "evidence that the answer is no is just as short: no gaps in the official receipt series, and a voucher "
            "behind every check.",
            "Documents prove that something happened. But a document on its own does not say who must answer for it. "
            "A pile of receipts with no one responsible for them is still a pile of paper. That is the subject of the "
            "third principle: every document has an owner.",
            ("ask", "Does your office still keep its cancelled receipts, or have you seen them go missing? I'd like to "
             "hear how your office handles spoiled forms."),
        ],
},
    {
        "date": "October 29, 2026",
        "title": "360 Degrees: My First Post as Acting Municipal Treasurer",
        "slug": "first-post-as-acting-treasurer",
        "summary": "Two years, two Mayors, a pandemic, a typhoon and an election: what my first post as Acting "
                   "Municipal Treasurer of Mulanay, Quezon, taught me.",
        "body": [
            "Some assignments arrive with a job description. Mine arrived with a microphone, a restaurant full of "
            "masked faces, and a turnover that took two full days.",
            "I received my first designation as Acting Municipal Treasurer of Mulanay, Quezon, at a time when I was "
            "the only ICLTE passer in the Provincial Treasurer's Office. That credential opened a door I had not "
            "expected to walk through so soon. On the road to Mulanay, one quiet question kept me company: am I "
            "ready for this?",
            "Mulanay sits on the Bondoc Peninsula in southern Quezon, a short trip from my hometown of San Andres. "
            "It is a town of 28 barangays and 55,576 people, according to the 2020 Census. The place was not new "
            "to me, but the office was. What followed, from 2020 to 2022, were two of the most demanding and "
            "meaningful years of my career, spent in the middle of the COVID-19 pandemic. This is the story of "
            "that first post.",
            ("h", "A Welcome I Did Not Expect"),
            "I arrived in Mulanay at around two in the afternoon, ready for paperwork. I was not ready for the "
            "warmth that waited for me that evening.",
            "We gathered at a local restaurant for my welcome. Around the tables sat the Municipal Mayor, the Vice "
            "Mayor, every member of the Sangguniang Bayan, the Municipal Administrator, the department heads and "
            "the employees of the municipality. The outgoing Municipal Treasurer was there too, the officer whose "
            "desk I was about to take.",
            "The room was full, yet every face was half hidden behind a mask. It was the pandemic, and I learned "
            "to read smiles in people's eyes. Among them was a familiar one: the Municipal Assessor, my friend and "
            "former co-worker at the Provincial Treasurer's Office. In a room full of new colleagues, one friendly "
            "face made all the difference.",
            "Then someone handed me the microphone. I thanked everyone for receiving me, and I told them the truth:",
            ("quote", "This is a challenge for me. My comfort zone has always been one division. Here, I will have "
             "to work and decide in 360 degrees."),
            "The next two days belonged to the turnover, formally conducted by a team from the Provincial "
            "Treasurer's Office. In treasury work, a turnover is more than a handshake. It is the moment "
            "accountability changes hands, as cash, records and responsibility pass from one officer to the next.",
            ("h", "From One Division to 360 Degrees"),
            "Until then, my work had clear borders. I belonged to a single division with a defined set of tasks, "
            "and I knew that ground well.",
            "Mulanay erased those borders. As head of the treasury office, I suddenly owned the whole circle: "
            "collections, disbursements, cash management, reports, people, and the decisions that tie them "
            "together. Problems no longer came from one direction. They came from every side, often at once, and "
            "the final call was mine.",
            "That shift is the real test of a first designation. It is not about knowing more rules. It is about "
            "seeing the whole office at once and still deciding with care.",
            ("h", "Home Was a Container House"),
            "The pandemic shaped every part of those years. Travel was restricted, offices ran on skeleton "
            "schedules, and going home was rarely an option.",
            "For two years, my home was the municipal container house in Mulanay. It was small and simple, but it "
            "kept me close to the office and the work. It stood near the sea, and every night I fell asleep to the "
            "sound of the waves. I wore a face mask every working day, until it felt as much a part of my uniform "
            "as my ID.",
            "Those nights by the sea taught me something about public service: you cannot always choose your "
            "conditions, but you can choose how you show up in them. I am deeply grateful to the people of "
            "Mulanay who made those years easier. They checked on me, helped me settle in, and treated the new "
            "treasurer like one of their own.",
            ("h", "Three Days in Boracay"),
            "In those years we could hardly go anywhere. Lockdowns and travel restrictions kept most of us within "
            "town limits for months at a time.",
            "So when the first Mayor I served approved my travel to Boracay for a three-day official training, it "
            "felt like a rare gift. The training sharpened my skills as a new treasurer, and the short change of "
            "scenery sent me back to Mulanay with fresh energy. I remain thankful for that trust, at a time when "
            "every trip had to be justified.",
            ("h", "When the Typhoon Came"),
            "As if a pandemic were not enough, a strong typhoon struck Mulanay during my term. Homes were damaged, "
            "livelihoods were lost, and families waited for help.",
            "In a disaster, the treasury is where help becomes cash in people's hands. My staff and I visited all "
            "28 barangays to distribute financial assistance to the affected families. It took about a week, and "
            "I could not have done it without the responsible, hardworking team beside me.",
            "I came to know the town not from behind a desk, but from its roads, its coastline and its upland "
            "villages. Those trips changed how I understand my job.",
            ("quote", "Every peso we safeguard in the vault exists for moments like that: a family receiving help "
             "when they need it most."),
            ("h", "Election Duty: Neutral by Mandate"),
            "I also served through an election in Mulanay. I will leave the politics to others; that is not my "
            "place, and it never should be.",
            "What I can say is this: the law gives the municipal treasurer a role in the election, including the "
            "counting and canvassing of votes. It is one of the least visible parts of the job, and one of the "
            "most serious. On those days, neutrality is not just good manners. It is the duty itself.",
            ("h", "Two Mayors, One Team"),
            "During my term I served under two Mayors: the first for one year and ten months, and the second for "
            "my final two months. Leadership changed, but the work never paused.",
            "What made that possible was the people. We worked well together across the whole municipality, from "
            "the department heads to the frontline staff. In the middle of a pandemic, that kind of teamwork is "
            "not a bonus. It is how a town keeps running.",
            ("h", "What the Job Taught Me"),
            "The work of a municipal treasurer is not easy, and the accountability is high. Every collection, "
            "every disbursement and every signature carries your name, and you answer for all of it. Mulanay "
            "taught me three lessons I still carry:",
            ("point", "Leadership begins outside your comfort zone", "I grew the most when I had to see the whole "
             "office, not just one division."),
            ("point", "Public money has a human face", "A week on the road to all 28 barangays after the typhoon "
             "made that real for me."),
            ("point", "No one serves alone", "A pandemic, a typhoon and an election were easier to face because of "
             "the people beside me."),
            ("h", "Thank You, Mulanay"),
            "Looking back, I am truly happy for the experience and the work. To the two Mayors I served, the Vice "
            "Mayor, the Sangguniang Bayan, the Municipal Administrator, the department heads, my treasury staff, "
            "my friend the Municipal Assessor, and the people of Mulanay: thank you for welcoming a neighbor from "
            "San Andres and making me one of your own.",
            "And to anyone receiving a first designation today: say yes to the challenge. The comfort zone is "
            "safe, but the growth is out there, all 360 degrees of it.",
            ("source", "Population and barangay figures: ", "PhilAtlas, Mulanay, Province of Quezon",
             "https://philatlas.com/luzon/r04a/quezon/mulanay.html", ", based on the 2020 Census."),
        ],
    },
    {
        "date": "October 28, 2026",
        "title": "The ALTOS Framework, Principle 1: Legality First",
        "publish_on": "2026-10-28",  # goes live on this date (Philippine time)
        "slug": "altos-framework-legality-first",
        "summary": "Before we ask how a peso was handled, we should ask whether the law allowed it at all.",
        "body": [
            "Ask any treasury clerk what their job is, and most will say they receive payments and release checks. "
            "That is true, but it skips a step. Behind every peso that crosses the counter, in or out, there should be "
            "a rule that says it may. The ALTOS Framework has ten principles, and this first one is about that "
            "unseen step.",
            "A word about the series before we begin. The framework is the closing part of my book, 360° "
            "Accountability. Each of its ten principles pairs an idea from one of the thinkers who shaped public "
            "administration with a Philippine law, and then with a habit a treasury office can start using tomorrow, "
            "with or without a computer. I will take them one at a time, in order, because each one rests on the one "
            "before it.",
            "Why principles, and not just another manual? The Philippines already has good manuals. Manuals tell an "
            "officer what to do when the case is ordinary. Principles tell the officer what to do when the case is "
            "new. What is often missing is a shared understanding of why the manuals say what they say. Without it, "
            "procedures slowly turn into rituals, and rituals are the first thing dropped when the office gets "
            "busy. The emblem of ALTOS is a full 360\u00b0 ring for the same reason: accountability that covers only "
            "300 degrees leaves a gap, and money leaks through gaps.",
            ("quote", "No legal basis, no transaction. If a peso cannot point to the rule that allows it, it should not "
             "move."),
            ("h", "Two Roles, One Line Between Them"),
            "Local government works because two groups do two different jobs. The Sanggunian, as the local "
            "lawmaking body, chooses what to tax, what to charge, and what to spend on. The treasury carries out those "
            "choices. In 1900 the American scholar Frank Goodnow described this as the difference between expressing "
            "the will of the public and executing it. Later writers argued that the two can never be fully separated, "
            "and they had a point, but as a division of labor the idea still holds. In a treasury office it is not "
            "theory: it is the daily difference between doing your job and overstepping it.",
            "A treasurer can recommend a new rate, point out a fee that no longer makes sense, or warn that a budget "
            "line is running low. What a treasurer cannot do is make up a charge on the spot, or pay for something the "
            "council never funded, however reasonable it may seem at the time.",
            "Woodrow Wilson, writing even earlier, in 1887, observed that running a constitution is harder than "
            "framing one, and argued that administration deserves to be studied as a business-like field of its own, "
            "apart from the making of policy. Our law reflects that view too. Under Section 470 of the Local "
            "Government Code, the treasurer is appointed by the Secretary of Finance from a list of at least three nominees of the mayor, and "
            "works under the mayor's administrative supervision. The arrangement keeps the collection of revenue "
            "professional and uniform from one town to the next, and it lets the treasurer serve each administration "
            "the same way. The tax ordinance is applied identically to every taxpayer, whoever is in office.",
            "The Code also spells out the treasurer's duties: taking custody of and managing local funds; taking "
            "charge of their disbursement; collecting taxes, fees and charges, and inspecting businesses for "
            "compliance with tax ordinances; keeping tax information up to date; advising the mayor and the "
            "Sanggunian on fiscal matters, including the income estimates used for the budget; and certifying "
            "whether cash is available for an obligation. Every one of these duties carries out decisions that "
            "others wrote into law. None of them gives the power to make new ones.",
            ("h", "Where the Authority Comes From"),
            "It helps to picture legal authority as a chain with several links. At the top is the 1987 Constitution. "
            "Article X, Section 5 lets each local government create its own sources of revenue and levy taxes, fees "
            "and charges, but only within guidelines that Congress sets. Article IX-D creates the Commission on Audit "
            "and gives it power over every government peso, earned or spent. So local fiscal autonomy is real, but "
            "it is autonomy under audit, never autonomy from it.",
            "The next link is the Local Government Code of 1991 (RA 7160), which turns those constitutional grants "
            "into working rules. Then come the municipality's own ordinances: the revenue code that sets rates and "
            "fees, and the annual appropriation ordinance that sets what may be spent. For a municipality, the "
            "Sangguniang Panlalawigan reviews both the tax ordinances and the annual budget. The last link is the "
            "official receipt or the check itself. A transaction is legal only when every link above it holds.",
            ("h", "What the Code Requires on the Collection Side"),
            "Section 130 of the Code lists the ground rules for local taxes. They must be uniform and equitable. They "
            "should be based, as far as practicable, on the taxpayer's ability to pay. They must serve a public "
            "purpose. They must not be unjust or confiscatory. And they must be collected by the local government "
            "itself, never by a private person.",
            "Each source of revenue also has its own legal home. Real property tax comes from Title II of Book II of "
            "the Code, and the Special Education Fund levy from Section 235. Business taxes rest on Section 143, and "
            "the community tax on Sections 156 to 158. Regulatory fees and service charges, such as market stall "
            "rentals or slaughterhouse fees, come from the municipality's own revenue code, and regulatory fees in "
            "particular must stay in line with the actual cost of regulating.",
            "This is also why the amount due is computed, not negotiated. It comes from the ordinance rate or the tax "
            "declaration, the same way for everyone. Adam Smith called this certainty: a good tax is one whose amount "
            "and timing are clear to the person paying it, not left to the mood of the collector.",
            ("h", "What the Code Requires on the Spending Side"),
            "On the spending side, Section 305 starts with a flat ban: nothing leaves the local treasury without an "
            "appropriation ordinance or a law behind it. The same section goes on to say that public money is held "
            "in trust, may be spent only for public purposes, and must be properly documented and accounted for. I "
            "consider Section 305 the legal root of the whole ALTOS idea: in one section, the law draws the full "
            "circle that ALTOS is named for.",
            "Section 344 then adds a series of checks before any payment, with each officer answering a different "
            "question:",
            ("point", "Budget officer", "Is there an appropriation for this purpose? In other words, did the "
             "Sanggunian authorize this kind of spending?"),
            ("point", "Accountant", "Has the appropriation been obligated, and are the supporting documents "
             "complete? Is this a valid claim against it?"),
            ("point", "Treasurer", "Is the cash actually there, in the right fund?"),
            ("point", "Local chief executive", "Does the head of the local government approve the payment and accept "
             "responsibility for it?"),
            "Many large payments also follow a procurement. The New Government Procurement Act (RA 12009), signed in "
            "July 2024, replaced RA 9184. The treasurer does not run the bidding, but a contract that skipped the "
            "required procurement is a payment the treasurer should not make.",
            ("h", "Why Spending Needs Extra Care"),
            "A mistake at the collection window and a mistake at the disbursing desk are not equal. Over-collecting "
            "or under-collecting is serious, but it usually involves money the government never had, and it can be "
            "corrected with the taxpayer. Money paid out without authority is different: it was already in the "
            "people's keeping, and once it leaves, recovering it is slow, costly and sometimes impossible. The "
            "Commission on Audit can disallow such a payment, and the officers who signed can be made to answer for "
            "it. That is why the law puts more locks on the door going out than on the door coming in.",
            ("h", "A Simple Daily Test"),
            "This principle can be checked in seconds, at any counter, on any day:",
            ("quote", "Which ordinance or appropriation allows this?"),
            "If the answer is a specific section of the revenue code or a specific line in the approved budget, go "
            "ahead. If the answer is “we have always done it this way,” stop and look it up. Old habits are "
            "often right, but they are not a legal basis.",
            "For the office as a whole, the question is a little bigger: can I name the law or ordinance behind "
            "every account that appears on our receipts? The proof that an office lives by this principle is simple "
            "to describe. The revenue code and the appropriation for every account are on file, and anyone who asks "
            "can be shown them.",
            ("h", "Rules Change, So Keep Checking"),
            "Legality is not a box ticked once. Laws, circulars and manuals change often. The Local Treasury "
            "Operations Manual, the rules of the Commission on Audit, and the issuances of the Bureau of Local "
            "Government Finance (BLGF) are all revised from time to time. The Real Property Valuation and Assessment Reform "
            "Act (RA 12001) of 2024, for example, requires a single Schedule of Market Values in each local "
            "government, prepared by the assessor and approved by the Department of Finance through the BLGF. Many "
            "local governments are now preparing revised schedules, which will change the very base the treasurer "
            "collects on. An office that is legal today can drift out of line next year without "
            "changing a thing. Before relying on any procedure, confirm that the text you are following is still "
            "the current one.",
            ("h", "Where ALTOS Helps"),
            "In ALTOS, an official receipt cannot be issued for an item that is not linked to an income account in "
            "the office's chart of accounts, so every amount collected has a home in the books. The ALTOS Framework "
            "self-assessment goes further and lists fee items that have no revenue code reference, so gaps surface "
            "before an auditor finds them. The office then rates itself from 1 to 4 on each principle and starts "
            "with its two weakest areas.",
            ("h", "The Foundation for the Other Nine"),
            "The next principles in the framework deal with forms, officers, deadlines and records. All of them assume "
            "the transaction was allowed in the first place. A perfectly filed receipt for a fee the law never "
            "created is still a wrong collection, just a well-documented one. So legality comes first, and everything "
            "else is built on top of it.",
            "But legality has a weakness of its own: it cannot prove itself. Saying a payment was authorized is not "
            "the same as showing it. That is where the second principle comes in: every peso has a document.",
            ("ask", "Have you ever found a fee or a payment in your office with no clear legal basis? I'd love to hear "
             "how you handled it."),
        ],
},
    {
        "date": "October 27, 2026",
        "title": "Why I Built ALTOS: Bringing Automation to Philippine Local Treasuries",
        "slug": "why-i-built-altos",
        "summary": "A treasury system built around one idea: every peso should be accounted for from the moment it arrives to the moment it is reported.",
        "body": [
            ("photo", "altos-screen.jpg", "ALTOS sign-in page", "small"),
            "Walk into many local treasury offices in the Philippines and you will still see stacks of receipts, "
            "hand-ruled cash books and monthly reports added up with a calculator. The people doing this work are "
            "careful and dedicated, but paper has limits. Reports take days to prepare, and a single wrong figure can "
            "hide for months before anyone notices.",
            "I have spent more than 13 years in local government fiscal administration, and I kept asking the same "
            "question: what if the office's own rules were built into the tools it uses every day? That question "
            "became ALTOS, the Automated Local Treasury Operations System.",
            ("h", "The Idea Behind It: Close the Circle"),
            "Picture the life of a single peso in a local treasury. It is received, recorded, deposited, perhaps paid "
            "out, and finally reported. At each of those stops, someone should be responsible for it. If even one "
            "stop has no clear owner, that is where errors and losses tend to happen.",
            ("quote", "Accountability has to go all the way around. A circle with a missing piece is not a circle, "
             "and public money slips out through the missing piece."),
            "This is why I describe ALTOS as 360° accountability. Treasury work moves in a cycle of three steps: "
            "money comes in, money goes out, and both are reported. The reports then guide next year's targets and "
            "budget, and the cycle begins again.",
            ("photo", "altos-loop.png", "The ALTOS loop: collect, disburse, report", "medium"),
            ("h", "Starting From Forms People Already Know"),
            "I did not want treasury staff to learn a strange new way of working. So every screen in ALTOS follows an "
            "official form they already fill out, from the LTOM and the COA. An auditor looking at the system sees "
            "the same documents they would see on paper.",
            "The system also enforces the rules quietly in the background. Receipts are numbered strictly in "
            "sequence, so none can go missing. A check cannot carry a date earlier than its checkbook. The 20% "
            "Development Fund and other Trust Funds are always set aside. And because the RAAF and CRAAF "
            "are due on the 5th of each month, "
            "ALTOS shows a countdown so the officer and the supervisor both know how many days are left.",
            ("h", "Two Subsystems, Both Ready"),
            "ALTOS is the main system, and it now has two working subsystems. The Treasury Collection System covers "
            "everything on the receiving side: official receipts, collectors and their receipt series, remittances, "
            "bank deposits, the daily report of collections, and the monthly accountability reports. The Treasury "
            "Disbursement System covers the paying side: vouchers, checks, cash advances and their liquidation, "
            "the check register, and disbursement reports. Both share one database, which can be used from a desktop "
            "application or a web browser anywhere on the office network.",
            ("h", "A Record You Can Trust"),
            "A treasury's records are only as good as their protection against tampering. In ALTOS, each entry in "
            "the activity log is digitally linked to the one before it, much like links in a chain. If anyone "
            "deletes or alters an entry, the break in the chain shows. Mistakes can still be fixed, but only through "
            "a recorded correction that states who made it and why.",
            "Security follows the NIST Cybersecurity Framework, an internationally used guide. Passwords are stored "
            "in scrambled form, accounts lock after repeated wrong attempts, idle sessions close on their own, "
            "and backups are encrypted and tested to make sure they can actually be restored.",
            ("h", "Made to Last Beyond Its Builder"),
            "Treasurers are transferred, retire or move on. A good system should keep working after they leave. "
            "That is why ALTOS has a turnover feature that gathers and checks the office's records and prepares a "
            "certificate for the next treasurer.",
            ("h", "Adoption Needs a Policy That Protects the Builder"),
            "ALTOS is not a demo or a school project. It runs on real collections and real disbursements, and the "
            "reports it produces are the ones an office signs and submits. When an office adopts a system like this, "
            "the system becomes part of how public money is handled, and that calls for clear rules on paper.",
            "Without those rules, the builder carries risks that nobody else sees. The system can be copied or "
            "changed without the builder's knowledge. The builder can be expected to fix problems at any hour, for "
            "free, long after leaving the office. Credit for the work can quietly disappear. And if something goes "
            "wrong because of a change someone else made, the builder can still be the one blamed.",
            "There is also a legal question. Under the Intellectual Property Code (RA 8293), there is no copyright in "
            "a work of the Government, meaning a work an official creates as part of regularly prescribed duties. "
            "Writing software is not among a treasurer's duties under the law, but the answer in each case depends "
            "on the facts and on what the parties agree in writing. That is exactly why the agreement has to come "
            "first.",
            ("h", "What a Good Adoption Policy Covers"),
            ("point", "Proof of authorship", "A dated record of the source files, design notes and versions that shows who built "
            "the system and when."),
            ("point", "Registration", "Where appropriate, registration or deposit of the work with the Intellectual Property "
            "Office of the Philippines (IPOPHL)."),
            ("point", "A written agreement", "A memorandum of agreement or license that states what the office may and may not "
            "do with the system: how it may be used, who maintains and hosts it, who may change it, and what happens "
            "when the builder is transferred, retires or resigns."),
            ("point", "Clear ownership of the data", "The office's records belong to the office and must always be available to "
            "it and to auditors, while the software itself remains the builder's work."),
            ("point", "Fair responsibility", "The builder answers for the system as delivered, not for changes made by others "
            "or for how it is operated after turnover."),
            ("point", "Legal review", "Advice from legal counsel before signing, and before any commercial use."),
            ("quote", "A clear agreement is not a sign of distrust. It is how both sides keep their promises: the "
             "office keeps a working system and its records, the builder keeps the authorship, and taxpayers keep "
             "uninterrupted service."),
            "I am also putting the thinking behind ALTOS into a book, 360° Accountability: Public Fiscal "
            "Administration in Philippine Local Treasuries. It closes with ten principles that any local treasury "
            "can follow, whether or not it uses software. I will write about each of them here.",
            ("quote", "Every peso, every step, every officer: 360°."),
        ],
    },
    {
        "date": "October 27, 2026",
        "title": "200 Kilometers and Five Years Later: Coming Home to a Farm Full of Fruit",
        "publish_on": None,  # hidden; set to "YYYY-MM-DD" to go live on that date
        "slug": "coming-home-to-a-farm-full-of-fruit",
        "body": [
            ("photo", "blog/farm-1.jpg", "The farm under the trees", "medium"),
            "Five years. That is how long it had been since I last set foot on my 3-hectare farm.",
            "Life has a way of keeping us busy. Between work, daily responsibilities, and the constant rush of routine, "
            "the years slip by faster than we realize. Recently, I finally made the time to take the 200-kilometer "
            "journey back.",
            ("h", "The Long Road Home"),
            "A trip that long gives you plenty of time to think. As the busy town centers slowly gave way to open roads "
            "and greener horizons, I found myself wondering how much the land had changed.",
            "When you are away from a place for five years, you hold on to a mental picture of how you left it: the "
            "young trees, the wide open spaces, the quiet promise of what it could become.",
            "Nothing quite prepared me for the moment I arrived.",
            ("h", "A Farm Full of Fruit"),
            "Stepping onto those three hectares after half a decade felt like greeting old friends who had grown tall, "
            "strong, and generous in my absence. My coconut, mango, santol, and langka (jackfruit) trees had not only "
            "matured into a lush sanctuary; they were laden with fruit.",
            ("photo", "blog/farm-2.jpg", "Coconut clusters beneath the fronds", "medium"),
            "Everywhere I looked, the farm was overflowing with life. Clusters of coconuts hung high beneath the swaying "
            "fronds, and the mango and santol branches bowed with ripening fruit.",
            "Walking past the langka trees, I marveled at the huge, bumpy jackfruits growing straight out of their "
            "sturdy trunks. Five years of sun, rain, and quiet patience had turned a simple planting into a true season "
            "of abundance.",
            ("photo", "blog/farm-3.jpg", "Jackfruit growing on the trunk", "medium"),
            ("h", "Shade, Breeze, and Childhood Memories"),
            "Standing among the trees, I was struck by how beautiful and deeply relaxing the place had become. The thick "
            "canopy of mango, santol, and langka filtered the harsh sunlight into soft patches of gold on the ground, "
            "while a gentle breeze rustled through the coconut leaves above.",
            "As I looked out across the wide spaces beneath the trees, a wave of nostalgia washed over me. The quiet land "
            "brought back vivid memories of my childhood: raising carabaos, cows, and goats, and the familiar sight and "
            "sound of native chickens roaming freely across the yard.",
            "There was a special rhythm and joy to that way of life, tending the animals from early morning until dusk. "
            "Being back on the farm made me realize how much I missed those simpler days.",
            ("h", "A Sip of Gratitude"),
            "To top off the welcome, I sat down in the cool shade beneath the loaded branches and drank fresh coconut "
            "water straight from my own trees. After a 200-kilometer drive, that first sip\u2014cool, naturally sweet, "
            "and refreshing\u2014tasted like pure gratitude.",
            ("photo", "blog/farm-4.jpg", "Fresh coconut, opened for drinking", "medium"),
            "Looking up at the fruit waiting to be harvested, and remembering where my love for farming began, I felt "
            "the weight of everyday stress melt away.",
            ("h", "What Five Years Taught Me"),
            "Visiting the farm after five years taught me something simple but important:",
            ("quote", "Growth takes time, patience bears the sweetest fruit, and our roots are always waiting for us if "
             "we are willing to make the journey back."),
            "I left with a full heart, a refreshed mind, and a renewed dream of hearing native chickens and livestock "
            "under these trees once again.",
            "One thing is for sure: I won't wait another five years for my next visit.",
            ("ask", "Have you ever returned to a place after years away and found it changed? I'd love to hear your "
             "story."),
        ],
    },
]
