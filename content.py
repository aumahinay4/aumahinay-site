"""All site content lives here. Edit this file to update the website.

Anything marked TODO is a placeholder waiting for real content.
"""

SITE = {
    "name": "Ambrosio U. Mahinay",
    "short_name": "Butch Mahinay",
    "title": "Ambrosio “Butch” U. Mahinay, MPA",
    "tagline": "Public finance professional who builds software for local government.",
    "email": "contact@aumahinay.dev",
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
                "Designed and built ALTOS, the Automated Local Treasury Operations System.",
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
#     "body": [
#         "A paragraph.",
#         ("h", "A subheading"),
#         ("photo", "blog/photo.jpg", "Caption", "small"),  # file in static/blog/; size small/medium/omit for full; skipped until it exists
#         ("quote", "A highlighted line."),
#     ],
# },
BLOG = [
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
            "Development Fund is always set aside. And because the RAAF and CRAAF are due on the 5th of each month, "
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
            "ALTOS is not a classroom exercise. It is a working system that handles real money and produces real "
            "reports, so adopting it is a serious step for any office, and it should never rest on a handshake.",
            "Building software is not part of a treasurer's legal duties, and under the Intellectual Property Code "
            "(RA 8293) the question of who owns such work depends on the facts and on what the parties agree. That "
            "is why clear terms must come before adoption, not after. In practice, that means:",
            "First, a dated record of authorship: the source files, design notes and version history that show who "
            "built the system and when. Second, registration or deposit of the work with the Intellectual Property "
            "Office of the Philippines (IPOPHL) where appropriate. Third, a written memorandum of agreement or "
            "license that spells out how the office may use, maintain and host the system, including after the "
            "builder leaves. And fourth, advice from legal counsel before any commercial use.",
            ("quote", "Good terms protect everyone. The office keeps a working system and its records, the builder "
             "keeps the authorship, and taxpayers keep uninterrupted service."),
            "I am also putting the thinking behind ALTOS into a book, 360° Accountability: Public Fiscal "
            "Administration in Philippine Local Treasuries. It closes with ten principles that any local treasury "
            "can follow, whether or not it uses software. I will write about each of them here, starting with the "
            "first: Legality First.",
            ("quote", "Every peso, every step, every officer: 360°."),
            ("ask", "Do you work in a local treasury, or build tools for government offices? I'd love to hear from "
             "you."),
        ],
    },
    {
        "date": "October 27, 2026",
        "title": "The ALTOS Framework, Principle 1: Legality First",
        "slug": "altos-framework-legality-first",
        "summary": "Before we ask how a peso was handled, we should ask whether the law allowed it at all.",
        "body": [
            "Ask any treasury clerk what their job is, and most will say they receive payments and release checks. "
            "That is true, but it skips a step. Behind every peso that crosses the counter, in or out, there should be "
            "a rule that says it may. The ALTOS Framework has ten principles, and this first one is about that "
            "unseen step.",
            ("quote", "No legal basis, no transaction. If a peso cannot point to the rule that allows it, it should not "
             "move."),
            ("h", "Two Roles, One Line Between Them"),
            "Local government works because two groups do two different jobs. The Sanggunian, as the local "
            "lawmaking body, chooses what to tax, what to charge, and what to spend on. The treasury carries out those "
            "choices. Scholars of public administration have written about this split for more than a century, and in "
            "a treasury office it is not theory: it is the daily difference between doing your job and overstepping it.",
            "A treasurer can recommend a new rate, point out a fee that no longer makes sense, or warn that a budget "
            "line is running low. What a treasurer cannot do is make up a charge on the spot, or pay for something the "
            "council never funded, however reasonable it may seem at the time.",
            ("h", "What the Local Government Code Requires"),
            "The rule is written into the Local Government Code of 1991 (RA 7160). On the collection side, Section 130 "
            "lists the ground rules for local taxes: they must be fair and uniform, fit the taxpayer's ability to pay, "
            "serve a public purpose, and be collected only by the local government itself.",
            "On the spending side, Section 305 starts with a flat ban: nothing leaves the local treasury without an "
            "appropriation ordinance or a law behind it. Section 344 then adds a series of checks before any payment, "
            "with the budget officer, the accountant and the treasurer each certifying their part.",
            ("h", "Why Spending Needs Extra Care"),
            "A mistake at the collection window and a mistake at the disbursing desk are not equal. Over-collecting "
            "or under-collecting is serious, but it can usually be corrected with the taxpayer. Money paid out "
            "without authority has already left the people's account, and recovering it is slow, costly and "
            "sometimes impossible. That is why the law puts more locks on the door going out than on the door "
            "coming in.",
            ("h", "A Simple Daily Test"),
            "This principle can be checked in seconds, at any counter, on any day:",
            ("quote", "Which ordinance or appropriation allows this?"),
            "If the answer is a specific section of the revenue code or a specific line in the approved budget, go "
            "ahead. If the answer is \u201cwe have always done it this way,\u201d stop and look it up. Old habits are "
            "often right, but they are not a legal basis.",
            ("h", "Where ALTOS Helps"),
            "In ALTOS, an official receipt cannot be issued for an item that is not linked to an income account, so "
            "every amount collected has a home in the books. The ALTOS Framework self-assessment goes further and "
            "flags fee items that have no revenue code reference, so gaps surface before an auditor finds them. "
            "The office then scores itself on each principle and starts with its weakest areas.",
            ("h", "The Foundation for the Other Nine"),
            "The next principles in the framework deal with forms, officers, deadlines and records. All of them assume "
            "the transaction was allowed in the first place. A perfectly filed receipt for a fee the law never "
            "created is still a wrong collection, just a well-documented one. So legality comes first, and everything "
            "else is built on top of it.",
            ("ask", "Have you ever found a fee or a payment in your office with no clear legal basis? I'd love to hear "
             "how you handled it."),
        ],
    },
    {
        "date": "October 27, 2026",
        "title": "200 Kilometers and Five Years Later: Coming Home to a Farm Full of Fruit",
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
