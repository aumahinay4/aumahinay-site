"""All site content lives here. Edit this file to update the website.

Anything marked TODO is a placeholder waiting for real content.
"""

SITE = {
    "name": "Ambrosio U. Mahinay",
    "short_name": "Butch Mahinay",
    "title": "Ambrosio “Butch” U. Mahinay, MPA",
    "tagline": "Public finance professional who builds software for local government.",
    "email": "aumahinay4@gmail.com",
    "domain": "aumahinay.dev",
    "brand": "aumahinay",  # shown in the browser tab
    # TODO: add real profile links (or leave empty to hide them)
    "github": "",
    "linkedin": "",
    "coursera": "",
}

ABOUT = {
    "intro": (
        "I am a public administration professional with over 14 years of career "
        "service in local government fiscal administration and treasury "
        "operations. I designed and built "
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
            "Programming at AMA Computer Learning Center. I started studying on "
            "Coursera in 2020, during the pandemic, in Mulanay, Quezon, where I was "
            "first designated Acting Municipal Treasurer and served for two years. "
            "In 2024 I committed to it fully, and I have since completed seven Google Professional Certificates and "
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
        "code": "ALTOS Collect",
        "name": "Collections subsystem",
        "movement": "Collect + Report",
        "status": "Ready",
        "summary": "A subsystem of ALTOS for collections and their reports: official receipts, collectors and their OR series, remittances and deposits, the daily RCD, and the monthly RAAF and CRAAF.",
    },
    {
        "code": "ALTOS Disburse",
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
