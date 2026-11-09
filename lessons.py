"""Python for Treasury Work: the tutorial lessons shown on /tutorials/.

Each lesson's code lives in tutorials/<folder>/. The page shows those exact files,
and the printed output comes from <script>.out, written by `python run_lessons.py`.
So whatever a reader sees under "Output" is what the code really prints.

A lesson body is a list of blocks:
    "text"                      a paragraph
    ("h", "Heading")            a section heading
    ("file", "data.csv")        show a data file from the lesson folder
    ("code", "script.py")       show a script, with Copy and Download buttons
    ("output", "script.py")     show what that script printed (script.out)
    ("point", "Label", "text")  a short explained step
    ("line", "code", "text")    one line of code with its plain-words explanation below it
    ("tip", "text")             a highlighted note
    ("try", "text")             a practice exercise
    ("answer", "script.py")     its worked answer: code and output, hidden behind "Show answer"
    ("terminal", "commands")    commands to type in Command Prompt or Terminal
    ("steps", ["a", "b"])       a numbered list of steps
    ("list", ["a", "b"])        a bullet list

To add a lesson: make a folder under tutorials/, put the scripts and data in it,
run `python run_lessons.py`, then add a block to LESSONS below (oldest first).
"""

TUTORIAL = {
    "title": "Python for Treasury Work",
    "intro": (
        "Short, practical Python lessons built around the daily work of a local treasury office: "
        "receipts, collections, penalties, reports and audit trails. Every example uses made-up "
        "data, runs as written, and shows the output it really prints. I am learning alongside "
        "you, so the lessons grow from simple scripts to the tools I use in building software."
    ),
    "setup": (
        "New to Python? Start with Lesson 0. It shows how to install Python, run a script, and fix the "
        "errors almost everyone meets on the first day. Then take the lessons in order; each one builds "
        "on the one before."
    ),
    # A promise we can keep and show (no "easiest" or "most updated" claims)
    "pledge": (
        "Every lesson is checked before it goes live: the code is run, the output you see is what it "
        "really prints, the facts and laws are checked against sources, and the page is reviewed on "
        "phone and computer. Each lesson shows the month it was last checked."
    ),
}

# Shown at the bottom of the Tutorials page
GLOSSARY = [
    ("Script", "A text file of Python code, saved with the .py ending, that you run from start to finish."),
    ("Variable", "A name that holds a value, like receipts = 10. You can change it later."),
    ("Loop", "Code that repeats for each item, written with for. It is how a script goes through every row of a file."),
    ("Function", "A named set of steps you can reuse, written with def. You give it inputs and it gives back a result."),
    ("Module", "A file of ready-made code you bring in with import, such as csv or decimal."),
    ("CSV", "Comma-separated values: a plain text table, one row per line, that Excel and most systems can export."),
    ("List", "An ordered collection, written with square brackets: [7650101, 7650102]."),
    ("Dictionary", "Pairs of keys and values, written with braces: {\"General Fund\": 21986.15}. You look a value up by its key."),
    ("Set", "A collection with no repeats and no order. Good for comparing what you have with what you expected."),
    ("Decimal", "A number type that keeps peso amounts exact, so centavos never drift."),
    ("f-string", "Text that starts with f and fills in values inside braces: f\"Total: {total}\"."),
    ("DataFrame", "The table that the pandas library works with: rows and named columns, like a sheet in Excel."),
    ("Library", "A collection of modules someone else wrote, such as pandas. Some come with Python; others you install."),
    ("pip", "Python's installer for extra libraries: pip install pandas."),
    ("Hash", "A short fingerprint of some data. Change one character and the fingerprint changes completely."),
    ("HMAC", "A hash made with a secret key. Only someone with the key can make a matching one."),
]

LESSONS = [
    {
        "number": 0,
        "slug": "getting-started",
        "folder": "00-getting-started",
        "title": "Getting started: install Python and run your first script",
        "summary": "Install Python on Windows or Mac, open the command line, and run a script, with fixes for the usual first errors.",
        "level": "Beginner",
        "minutes": 20,
        "topics": ["history of Python", "installing Python", "Command Prompt", "Terminal", "pip"],
        "learn": [
            "Where Python came from and why its libraries make it so powerful",
            "Install Python 3 the right way on Windows or Mac",
            "Open Command Prompt or Terminal and move into a folder",
            "Run a Python script and read what it prints",
            "Install extra libraries with pip",
            "Fix the errors that almost everyone meets on day one",
        ],
        "body": [
            "Every lesson in this series is a small Python script that you run on your own computer. "
            "This lesson sets that up. It takes about twenty minutes, and you only do it once.",
            ("h", "Why Python? A short history"),
            "Before we install it, it helps to know where Python came from. It did not start in a big "
            "company. It started as one programmer's holiday project, and it grew into one of the most "
            "widely used programming languages in the world.",
            ("point", "1989",
             "Guido van Rossum, a Dutch programmer, began writing Python over the Christmas holidays as a "
             "hobby. He wanted a language that was easy to read and quick to write. He named it after the "
             "British comedy show Monty Python's Flying Circus, not after the snake."),
            ("point", "1991",
             "The first version was shared freely with the public. From the start, anyone could use it, "
             "read its code and help improve it, at no cost."),
            ("point", "2000",
             "Python 2 came out and the language spread to schools, offices and websites."),
            ("point", "2008",
             "Python 3 cleaned up old design mistakes, such as how text in other languages is handled. "
             "Python 2 was retired in 2020, so today everyone uses Python 3, and so do these lessons."),
            ("point", "Today",
             "Python sits at or near the top of the rankings of the most used programming languages. It runs "
             "inside banks, government agencies, universities, scientific labs and websites such as "
             "Instagram. It is also the main language for data analysis and artificial intelligence."),
            ("h", "Where its power comes from: the libraries"),
            "Python itself is simple. Its real strength is the huge collection of ready-made code, called "
            "libraries, that people around the world have written and shared for free. Python's public "
            "library index, PyPI, holds more than half a million of them. Instead of building everything "
            "from scratch, you bring in a library with one line and use what experts have already tested.",
            ("list", [
                "Built in, with nothing to install: csv reads spreadsheet exports, decimal keeps peso amounts "
                "exact to the centavo, datetime counts days and months for penalties, and sqlite3 stores "
                "records in a small database. These come with Python; people call it \"batteries included\".",
                "pandas works with tables of thousands of rows the way Excel does, but in seconds and without "
                "mistakes from dragging formulas. It was first written by Wes McKinney in 2008 at a financial "
                "firm, to analyse money data. That makes it a natural fit for treasury work.",
                "NumPy does fast calculations on large sets of numbers. pandas and many other libraries are "
                "built on top of it.",
                "openpyxl reads and writes real Excel files, so a script can fill in a report template for you.",
                "Flask turns Python code into a website or web system. This very site is written in Python, "
                "and ALTOS is built in Python too.",
            ]),
            "This is why one office worker with a laptop can do with a short script what used to need a "
            "team and expensive software. Collections can be added up, receipt series checked and penalties "
            "computed in seconds, the same way every time.",
            ("tip", "Python's guiding rules are built into it. After you install it, type py (Windows) or "
                    "python3 (Mac) to open Python, then type import this and press Enter. You will see "
                    "\"The Zen of Python\", which includes the line \"Readability counts.\" Type exit() to leave."),
            ("h", "1. Install Python"),
            ("steps", [
                "Go to python.org and open Downloads.",
                "Windows: download the Python install manager, double-click it and click Install. (You can also "
                "get the same \"Python Install Manager\" free from the Microsoft Store.) Then press the Windows "
                "key, type cmd, open Command Prompt, and type the command shown below the steps. It downloads "
                "the latest Python 3 for you. If it asks any setup questions, pressing Enter to accept the "
                "suggested answer is fine.",
                "Mac: download the latest Python 3 macOS installer, open the downloaded .pkg file and follow "
                "the steps.",
            ]),
            ("terminal", "py install default      (Windows only)"),
            ("tip", "On Windows you may also see the older installer (.exe) listed. It still works until "
                    "Python 3.16; if you use it, tick \"Add python.exe to PATH\" on its very first screen "
                    "before clicking Install Now."),
            ("h", "2. Open the command line"),
            "Python scripts are usually run by typing a short command. On Windows, press the Windows key, "
            "type cmd and open Command Prompt. On a Mac, press Cmd + Space, type Terminal and press Enter. "
            "Check that Python is there by typing the command below and pressing Enter. It should answer "
            "with a version number such as Python 3.15.2.",
            ("terminal", "py --version          (Windows)\npython3 --version     (Mac)"),
            ("h", "3. Make a folder and save the script"),
            "Make a folder for the lessons, for example python-lessons in your Documents. Open Notepad "
            "(Windows) or TextEdit (Mac, then choose Format, Make Plain Text), paste the code below, and save "
            "it in that folder as hello.py. You can also click Download on the code box. A code editor such "
            "as Visual Studio Code, which is free, makes this easier and colours the code like this page does.",
            ("code", "hello.py"),
            ("h", "4. Run it"),
            "In Command Prompt or Terminal, move into the folder with cd (change directory), then run the "
            "script:",
            ("terminal", "cd Documents\\python-lessons      (Windows)\npy hello.py\n\ncd Documents/python-lessons       (Mac)\npython3 hello.py"),
            "You should see exactly this:",
            ("output", "hello.py"),
            "Each print line in the code produced one line of output. Notice that 2 + 3 * 4 gives 14, not 20: "
            "Python multiplies before it adds, just like a calculator in scientific mode.",
            ("h", "5. Install extra libraries with pip"),
            "Python comes with many modules built in. Others, such as pandas for Lesson 4, are installed "
            "once with pip:",
            ("terminal", "py -m pip install pandas openpyxl          (Windows)\npython3 -m pip install pandas openpyxl     (Mac)"),
            ("h", "When something goes wrong"),
            ("point", "'python' is not recognized",
             "On Windows, close Command Prompt, open a new one and try again, or use py instead of python. "
             "If neither works, press the Windows key, type Manage app execution aliases, open it and make "
             "sure the Python entries are switched on. The same fix applies if typing python opens the "
             "Microsoft Store. If you used the older .exe installer, run it again, choose Modify, and tick "
             "Add Python to environment variables."),
            ("point", "No such file or directory",
             "Command Prompt is looking in a different folder. Use cd to move into the folder where you saved "
             "the file, and type dir (Windows) or ls (Mac) to see the files there."),
            ("point", "SyntaxError",
             "Something in the code was typed differently, often a missing quote, bracket or colon. Python "
             "shows the line number; compare that line with the lesson."),
            ("point", "IndentationError",
             "Python uses the spaces at the start of a line to group code. Lines inside a for or with block "
             "must be indented by the same amount, usually four spaces."),
            ("point", "ModuleNotFoundError: No module named 'pandas'",
             "The library is not installed yet. Run the pip command above."),
            ("tip", "Copying the code from this page with the Copy button is the safest way to start. Once a "
                    "script runs, change one thing at a time and run it again to see what happens."),
        ],
    },
    {
        "number": 1,
        "slug": "add-up-daily-collections",
        "folder": "01-daily-collections",
        "title": "Add up a day's collections from a CSV file",
        "summary": "Read the day's official receipts from a spreadsheet export and total them per fund, to the centavo.",
        "level": "Beginner",
        "minutes": 15,
        "topics": ["csv", "Decimal", "dictionaries", "f-strings"],
        "publish_on": "2026-11-07",
        "learn": [
            "Read a CSV file one row at a time with the csv module",
            "Keep peso amounts exact with Decimal",
            "Group totals by fund using a dictionary",
            "Print a neat, right-aligned summary with f-strings",
        ],
        "body": [
            "At the end of each day a collector has a stack of official receipts, and the cashier "
            "needs one figure per fund: how much went to the General Fund, how much to the Special "
            "Education Fund, how much is held in trust. Most collection systems and spreadsheets can "
            "export those receipts as a CSV file. A few lines of Python can turn that file into the "
            "totals, the same way every time, without retyping a single amount.",
            ("h", "The data"),
            "Save this as collections.csv. Each line is one official receipt. The first line holds the "
            "column names, which Python will use to find each value.",
            ("file", "collections.csv"),
            ("h", "The code"),
            "Save this as daily_total.py in the same folder.",
            ("code", "daily_total.py"),
            ("h", "Output"),
            ("output", "daily_total.py"),
            ("h", "Line by line"),
            "If this is your first Python script, here is what each part does, in plain words.",
            ("line", "\"\"\"Add up one day's collections...\"\"\"",
             "Text between triple quotes at the top is a note for people. Python ignores it. Lines that "
             "start with # are notes too."),
            ("line", "import csv",
             "brings in the csv module, Python's ready-made tool for reading CSV files. Without this line, "
             "Python would not know what csv.DictReader means."),
            ("line", "from decimal import Decimal",
             "brings in just one tool, Decimal, from the decimal module, so we can write Decimal(...) directly."),
            ("line", "totals = {}",
             "creates an empty dictionary named totals. A dictionary holds pairs, like a two-column table: "
             "the fund name on the left and its running total on the right."),
            ("line", "grand_total = Decimal(\"0\")",
             "creates a variable that starts at exactly zero pesos. receipts = 0 does the same for the count "
             "of receipts."),
            ("line", "with open(\"collections.csv\", ...) as f:",
             "opens the file and calls it f while we read it. The with keyword closes the file "
             "automatically when the indented block ends. The colon at the end means an indented block follows."),
            ("line", "for row in csv.DictReader(f):",
             "a loop. DictReader hands over the file one row at a time, skipping the header line, and the "
             "indented lines below run once for every row. With 10 receipts, they run 10 times."),
            ("line", "amount = Decimal(row[\"amount\"])",
             "row is a dictionary built from the header: row[\"amount\"] is the text in the amount column, "
             "such as \"4500.00\". Decimal turns that text into an exact number we can add."),
            ("line", "totals[fund] = totals.get(fund, Decimal(\"0\")) + amount",
             "read it from the right: take this fund's total so far (or zero if the fund has not appeared "
             "yet), add this receipt's amount, and store the result back under the fund's name."),
            ("line", "grand_total += amount",
             "a short way of writing grand_total = grand_total + amount. receipts += 1 adds one to the count."),
            ("line", "print(f\"... {receipts} official receipts\")",
             "prints a line of text. The f before the quote makes it an f-string: anything inside braces "
             "is replaced by its value, so {receipts} becomes 10."),
            ("line", "print(\"-\" * 44)",
             "repeating text: a dash times 44 prints a line of 44 dashes."),
            ("line", "for fund, total in sorted(totals.items()):",
             "goes through the dictionary in alphabetical order. Each pass gives two values at once: the "
             "fund name and its total."),
            ("line", "{fund:<28}  and  {total:>16,.2f}",
             "formatting codes inside the braces. <28 means left-aligned in 28 spaces. >16 means "
             "right-aligned in 16 spaces, the comma adds thousands separators, and .2f shows two decimal "
             "places. That is what makes the columns line up."),
            ("tip", "Open a CSV file with newline=\"\" and an explicit encoding, as Python's own "
                    "documentation advises. newline=\"\" lets the csv module handle line breaks itself "
                    "(and, when you write a CSV, it prevents blank rows on Windows); encoding=\"utf-8\" "
                    "keeps names with ñ readable on every computer."),
            ("h", "Try it yourself"),
            ("try", "Add a second total per nature of collection (Business tax, Real property tax, and so "
                    "on). Hint: make another dictionary and fill it inside the same loop."),
            ("answer", "answer_by_nature.py"),
        ],
    },
    {
        "number": 2,
        "slug": "check-or-series",
        "folder": "02-or-series-check",
        "title": "Check an official receipt series for gaps and duplicates",
        "summary": "Compare the receipts recorded today with the booklet issued, and flag missing, repeated or stray numbers.",
        "level": "Beginner",
        "minutes": 20,
        "topics": ["sets", "range", "Counter", "list comprehensions"],
        "publish_on": "2026-11-14",
        "learn": [
            "Use a set to compare what was expected with what was recorded",
            "Find repeated values with collections.Counter",
            "Write short filters with list and set comprehensions",
        ],
        "body": [
            "Official receipts are accountable forms. Every number in a booklet must be accounted "
            "for: used, cancelled, or still unused at the end. A skipped number or a number entered "
            "twice is the kind of thing an auditor will ask about, and it is much easier to explain "
            "on the same day than months later. This lesson checks a day's receipts against the "
            "booklet issued to the collector.",
            ("h", "The data"),
            "Save this as receipts.csv. The booklet issued runs from 7650101 to 7650150, and a few "
            "problems have been planted in the list on purpose.",
            ("file", "receipts.csv"),
            ("h", "The code"),
            ("code", "check_series.py"),
            ("h", "Output"),
            ("output", "check_series.py"),
            ("h", "How it works"),
            ("point", "Counter(numbers)",
             "counts how many times each receipt number appears. Any number with a count above one "
             "was recorded twice."),
            ("point", "BOOKLET_FIRST <= n <= BOOKLET_LAST",
             "Python lets you chain comparisons, so this reads just like the rule: the number must "
             "fall inside the booklet."),
            ("point", "expected - inside",
             "subtracting one set from another leaves the numbers that should be there but are not. "
             "That single line finds every gap."),
            ("point", "duplicates or 'none'",
             "an empty list counts as false in Python, so the report prints none instead of []."),
            ("tip", "A cancelled receipt is not a gap. It still uses up its number, so it stays in the "
                    "list and is reported on its own line."),
            ("h", "Try it yourself"),
            ("try", "Change the script so it also prints how many receipts remain unused in the booklet, "
                    "from the last number used up to 7650150."),
            ("answer", "answer_unused.py"),
        ],
    },
    {
        "number": 3,
        "slug": "rpt-penalty-with-decimal",
        "folder": "03-rpt-penalty",
        "title": "Compute real property tax penalties with Decimal",
        "summary": "See why floats are unsafe for money, then compute 2% monthly penalties with a 36-month cap, rounded correctly.",
        "level": "Beginner",
        "minutes": 20,
        "topics": ["Decimal", "functions", "rounding", "min()"],
        "publish_on": "2026-11-21",
        "learn": [
            "See the rounding errors that floats introduce",
            "Write a small, reusable function",
            "Round to the centavo with ROUND_HALF_UP",
            "Apply a ceiling with min()",
        ],
        "body": [
            "RA 7160 charges interest of 2% a month on delinquent real property tax, for at most 36 "
            "months; most offices simply call it the penalty. The computation looks simple until the "
            "centavos stop matching. Before writing the "
            "penalty function, it is worth seeing why money in Python should be handled with the "
            "Decimal type and not with ordinary float numbers.",
            ("h", "Why not float?"),
            ("code", "why_decimal.py"),
            ("output", "why_decimal.py"),
            "A float stores numbers in binary, and most decimal fractions like 0.10 cannot be stored "
            "exactly. The error is tiny at first, but it builds up over many additions. Decimal keeps "
            "the amount exactly as written, which is what a treasury report needs.",
            ("h", "The data"),
            "Save this as delinquent.csv. The months_late column is the number of months of "
            "delinquency, already counted for each tax declaration.",
            ("file", "delinquent.csv"),
            ("h", "The code"),
            ("code", "rpt_penalty.py"),
            ("h", "Output"),
            ("output", "rpt_penalty.py"),
            ("h", "How it works"),
            ("point", "def penalty(tax_due, months_late)",
             "puts the rule in one place. If the rule changes, you change one function and every "
             "report that uses it follows."),
            ("point", "min(months_late, MAX_MONTHS)",
             "applies the ceiling. A property delinquent for 58 months is charged for 36, the maximum."),
            ("point", "quantize(CENTAVO, rounding=ROUND_HALF_UP)",
             "rounds to two decimal places the way people round by hand: 916.066 becomes 916.07, and a "
             "half centavo always goes up."),
            ("tip", "This lesson keeps the month count as given. How months are counted (from which "
                    "date, and how partial months and installments are treated) follows your local "
                    "revenue code and the applicable rules, so check those before using a script like "
                    "this for real assessments."),
            ("h", "Try it yourself"),
            ("try", "Add a discount function for early payment: a percentage off the tax due when the "
                    "tax is paid in advance. Keep it in Decimal and round it the same way."),
            ("answer", "answer_discount.py"),
        ],
    },
    {
        "number": 4,
        "slug": "rcd-summary-with-pandas",
        "folder": "04-rcd-summary",
        "title": "Build a simple RCD summary with pandas",
        "summary": "Group collections by collector and fund, list the receipts used, and match collections against deposits.",
        "level": "Intermediate",
        "minutes": 25,
        "topics": ["pandas", "groupby", "pivot_table", "join"],
        "publish_on": "2026-11-28",
        "learn": [
            "Load CSV files into pandas DataFrames",
            "Summarize data with groupby and named aggregations",
            "Build a fund-by-collector table with pivot_table",
            "Join two tables and compute the difference",
        ],
        "body": [
            "The Report of Collections and Deposits brings three questions together: which receipts "
            "were used, how much was collected for each fund, and whether all of it reached the bank. "
            "The pandas library answers each question in a few lines. This lesson builds a simple "
            "summary of those three parts; it is a learning exercise, not the official report form.",
            ("tip", "pandas is not part of standard Python. If you skipped step 5 of Lesson 0, install it "
                    "once with: py -m pip install pandas (Windows) or python3 -m pip install pandas (Mac)."),
            ("h", "The data"),
            "Save the collections of two collectors as collections.csv:",
            ("file", "collections.csv"),
            "and the deposits made per fund as deposits.csv:",
            ("file", "deposits.csv"),
            ("h", "The code"),
            ("code", "rcd_summary.py"),
            ("h", "Output"),
            ("output", "rcd_summary.py"),
            ("h", "How it works"),
            ("point", "groupby(\"collector\").agg(...)",
             "splits the receipts by collector and computes several results at once: the first and "
             "last receipt number, how many were used, and the total amount."),
            ("point", "pivot_table(...)",
             "spreads the totals into a grid, one row per fund and one column per collector. "
             "margins=True adds the Total row and column, and fill_value=0 fills funds a collector "
             "did not collect."),
            ("point", "join(...)",
             "lines up deposits with collections by fund name, so the two amounts sit side by side "
             "and can be subtracted."),
            ("point", ".round(2)",
             "pandas works in floats, so the difference is rounded to the centavo before it is shown "
             "or compared."),
            "Section C shows 350.50 of Trust Fund collections not yet deposited. That is exactly the "
            "kind of line that should be explained, or deposited, before the report is signed.",
            ("h", "Try it yourself"),
            ("try", "Save the three tables to one Excel file with pandas: look up DataFrame.to_excel and "
                    "pd.ExcelWriter. This also needs openpyxl, which Lesson 0 installed with pandas."),
            ("answer", "answer_excel.py"),
        ],
    },
    {
        "number": 5,
        "slug": "tamper-evident-log-with-hmac",
        "folder": "05-tamper-evident-log",
        "title": "Make a tamper-evident log with HMAC",
        "summary": "Seal each log entry with a keyed hash chained to the one before it, so any later edit or deletion shows.",
        "level": "Intermediate",
        "minutes": 25,
        "topics": ["hmac", "hashlib", "json", "security"],
        "publish_on": "2026-12-05",
        "learn": [
            "What a hash and an HMAC are, in plain terms",
            "Chain records so that removing one breaks the next",
            "Compare secrets safely with hmac.compare_digest",
            "Keep keys out of the code",
        ],
        "body": [
            "A log of who did what, and when, is only useful if no one can quietly change it "
            "afterwards. Python's standard library has what you need to make a log that shows "
            "tampering: hashlib and hmac.",
            "A hash turns any text into a fixed-length fingerprint; change one character and the "
            "fingerprint changes completely. An HMAC is a hash mixed with a secret key, so only "
            "someone who holds the key can produce a valid fingerprint. Here each entry's fingerprint, "
            "its seal, also includes the seal of the entry before it. That chain is what makes a "
            "deleted entry visible too.",
            ("h", "The code"),
            ("code", "audit_log.py"),
            ("h", "Output"),
            ("output", "audit_log.py"),
            ("h", "How it works"),
            ("point", "json.dumps(entry, sort_keys=True)",
             "turns the entry into text in a fixed order, so the same entry always produces the same "
             "seal."),
            ("point", "previous_seal + ...",
             "each seal covers the one before it. Remove entry 3 and entry 4 no longer fits, which is "
             "why Check 3 points at position 3. The very last entry has nothing after it, so removing "
             "it would not show; that is one more reason to keep copies of the log elsewhere."),
            ("point", "hmac.compare_digest",
             "compares two seals in a way that does not leak timing clues to an attacker. Use it "
             "instead of == whenever secrets are compared."),
            ("point", "os.environ.get(\"AUDIT_KEY\", ...)",
             "reads the key from an environment variable. The practice key in the code is only for "
             "this lesson; a real key never goes into source code or a shared folder."),
            ("tip", "Tamper-evident is not tamper-proof. The log cannot stop someone from editing it, "
                    "but it shows that it happened. Keep the key with someone other than the people "
                    "who write the entries, and keep copies of the log elsewhere."),
            ("h", "Try it yourself"),
            ("try", "Save the log to a JSON file with json.dump, load it back with json.load, and run "
                    "verify() on the loaded copy. Then edit the file by hand and run it again."),
            ("answer", "answer_json.py"),
        ],
    },
]

# Month each lesson was last fully checked (code run, facts sourced, phone and computer view).
# Update a lesson's entry whenever it is re-checked. A lesson missing here shows no "Last checked" line.
LAST_CHECKED = {
    0: "November 2026",
    1: "November 2026",
    2: "November 2026",
    3: "November 2026",
    4: "November 2026",
    5: "November 2026",
}
