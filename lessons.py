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
    ("Workbook", "An Excel file. It holds one or more sheets, which openpyxl calls worksheets."),
    ("Formula", "A calculation stored in a cell, such as =SUM(E2:E11). Excel or another spreadsheet app works out its value when the file is opened."),
    ("Database", "An organised store of records that a program can search, add to and total quickly. SQLite keeps a whole database in one file."),
    ("SQL", "Structured Query Language: short commands such as SELECT, INSERT and GROUP BY that ask a database for data or change it."),
    ("Placeholder", "A ? in an SQL command that the database fills in with a value you pass separately. It keeps typed-in text from being run as a command."),
    ("Exception", "Python's way of reporting an error while a script runs. try and except let the script catch it and carry on."),
    ("Validation", "Checking that data follows the rules (right format, allowed values, sensible amounts) before using it."),
    ("Test", "A small function that runs your code with a known input and checks the answer. pytest runs all of them at once."),
    ("assert", "A Python statement that stops with an error if something is not true: assert total == 100."),
    ("Web app", "A program that answers a browser's requests with web pages. Flask is a library for writing one in Python."),
    ("Route", "In Flask, the link between an address such as /receipt/7650101 and the function that makes that page."),
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
        "publish_on": "2026-11-10",  # published early in a batch for AdSense readiness (Butch, 2026-11-10)
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
        "publish_on": "2026-11-10",  # published early in a batch for AdSense readiness (Butch, 2026-11-10)
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
        "publish_on": "2026-11-10",  # published early in a batch for AdSense readiness (Butch, 2026-11-10)
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
        "publish_on": "2026-11-10",  # published early in a batch for AdSense readiness (Butch, 2026-11-10)
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
    {
        "number": 6,
        "slug": "excel-report-with-openpyxl",
        "folder": "06-excel-report",
        "title": "Make a formatted Excel report with openpyxl",
        "summary": "Turn the day's receipts into a real Excel file with a bold header, peso formatting, a SUM formula and a frozen top row.",
        "level": "Beginner",
        "minutes": 20,
        "topics": ["openpyxl", "Excel", "formulas", "number formats"],
        "publish_on": "2026-11-12",  # published at once after re-check (Butch, 2026-11-12)
        "learn": [
            "Create an Excel workbook and fill it row by row",
            "Make the header bold, set column widths and freeze the top row",
            "Show amounts with a thousands separator and two decimals",
            "Write Excel formulas such as SUM and SUMIF from Python",
            "Open a saved Excel file again and read what is inside",
        ],
        "body": [
            "Most treasury reports end up in Excel. Someone exports the receipts, pastes them into a "
            "template, fixes the column widths, formats the amounts and types the total formula, every "
            "single day. The openpyxl library lets a script do all of that in a second, and the file it "
            "makes is an ordinary Excel file that anyone can open, print or forward.",
            ("tip", "openpyxl is not part of standard Python. If you skipped step 5 of Lesson 0, install it "
                    "once with: py -m pip install openpyxl (Windows) or python3 -m pip install openpyxl (Mac). "
                    "It works with the modern .xlsx format, not the old .xls files."),
            ("h", "The data"),
            "This is the same collections.csv from Lesson 1. Save it in a new folder for this lesson.",
            ("file", "collections.csv"),
            ("h", "The code"),
            "Save this as make_report.py in the same folder and run it. It saves daily_report.xlsx next to "
            "the script, then opens that file again to show what was saved.",
            ("code", "make_report.py"),
            ("h", "Output"),
            ("output", "make_report.py"),
            "Now open daily_report.xlsx in Excel. The header is bold, the amounts read 4,500.00 and "
            "1,250.75, the columns are wide enough to read, and the TOTAL cell shows 26,567.80, the same "
            "figure Lesson 1 printed (21,986.15 + 2,231.15 + 2,350.50).",
            ("h", "How it works"),
            ("point", "Workbook() and wb.active",
             "a new workbook starts with one empty sheet. wb.active is that sheet, and ws.title renames it."),
            ("point", "ws.append([...])",
             "adds one row at the bottom of the sheet. Each item in the list goes into the next column, A, B, "
             "C and so on."),
            ("point", "Font(bold=True)",
             "ws[1] is the whole first row, so the loop makes every header cell bold."),
            ("point", "f\"=SUM(E2:E{last})\"",
             "any text that starts with = is saved as a formula. With 10 receipts, last is 11, so the cell "
             "holds =SUM(E2:E11). If someone corrects an amount later, Excel updates the total by itself."),
            ("point", "number_format = \"#,##0.00\"",
             "the same format code you would pick in Excel's Format Cells: a comma for thousands and "
             "always two decimal places. It changes how the number looks, not the number itself."),
            ("point", "freeze_panes = \"A2\"",
             "freezes everything above cell A2, so the header row stays in view while you scroll down a "
             "long list."),
            ("point", "load_workbook(...)",
             "opens an existing Excel file. values_only=True gives plain values instead of cell objects, "
             "which is handy for reading."),
            "Look at the last line of the output: the TOTAL cell comes back as the formula text, not as "
            "26,567.80. openpyxl writes formulas but never calculates them; Excel calculates when the file "
            "is opened. Notice also that 4500.00 came back as 4500: Excel stores numbers, and the two "
            "decimal places are only part of the display format.",
            ("tip", "Excel stores amounts as ordinary floating-point numbers, the kind Lesson 3 warned about. "
                    "That is fine for showing and printing figures. When the total itself matters, compute it "
                    "in Python with Decimal, as in Lesson 1, and compare it with the Excel total."),
            ("h", "Try it yourself"),
            ("try", "Open daily_report.xlsx with load_workbook and add a second sheet named \"By fund\" with one "
                    "row per fund. Instead of typing the amounts, give each row a SUMIF formula that adds up "
                    "that fund's receipts from the Collections sheet, then a TOTAL row. Hint: "
                    "wb.create_sheet(\"By fund\"), and a formula can point at another sheet as "
                    "Collections!E2:E11."),
            ("answer", "answer_by_fund.py"),
            "Open the file in Excel and the By fund sheet shows General Fund 21,986.15, Special Education "
            "Fund 2,231.15 and Trust Fund 2,350.50, the same totals as Lesson 1.",
        ],
    },
    {
        "number": 7,
        "slug": "receipts-register-with-sqlite",
        "folder": "07-sqlite-register",
        "title": "Keep a receipts register in SQLite",
        "summary": "Save official receipts in a small database file, total them with SQL, and let the database itself refuse a duplicate OR number.",
        "level": "Intermediate",
        "minutes": 25,
        "topics": ["sqlite3", "SQL", "placeholders", "IntegrityError"],
        "publish_on": "2026-11-14",
        "learn": [
            "Create a database table with sqlite3, which comes with Python",
            "Store peso amounts safely as whole centavos",
            "Add many rows at once with executemany and ? placeholders",
            "Ask questions with SELECT, SUM and GROUP BY",
            "Let a PRIMARY KEY stop the same receipt number from being saved twice",
        ],
        "body": [
            "A CSV file is fine for one day's receipts. After a year there are thousands of them, spread "
            "over many files, and questions like \"how much did this taxpayer pay this year?\" mean opening "
            "file after file. A database keeps every record in one place and answers such questions in "
            "a moment. SQLite is a small database that lives in a single file on your computer, needs no "
            "server and no password, and is built into Python.",
            ("h", "The data"),
            "The same collections.csv as Lessons 1 and 6. Save it in a new folder for this lesson.",
            ("file", "collections.csv"),
            ("h", "The code"),
            "Save this as register.py and run it. It creates register.db in the same folder.",
            ("code", "register.py"),
            ("h", "Output"),
            ("output", "register.py"),
            "Run it a second time and the count stays at 10. The receipts are not saved twice.",
            ("h", "How it works"),
            ("point", "sqlite3.connect(\"register.db\")",
             "opens the database file, and creates it if it does not exist yet. Everything is kept in that "
             "one file, so you can back it up like any document."),
            ("point", "CREATE TABLE IF NOT EXISTS",
             "describes the table once: its columns and what each one holds. IF NOT EXISTS means running "
             "the script again does not cause an error."),
            ("point", "or_number INTEGER PRIMARY KEY",
             "makes the receipt number the key of each record. A key must be unique, so the database "
             "itself refuses a second receipt with the same number, the problem Lesson 2 looked for."),
            ("point", "centavos INTEGER",
             "SQLite has no exact decimal type; a REAL column is a float, with the rounding problems from "
             "Lesson 3. So each amount is stored as whole centavos: 1,250.75 pesos is saved as 125075, and "
             "divided by 100 again only when it is shown."),
            ("point", "VALUES (?, ?, ?, ?, ?, ?)",
             "each ? is a placeholder. sqlite3 fills them in from the values you pass, in order. Never build "
             "an SQL command by pasting text into it with an f-string: a payor name with a quote mark in it "
             "would break the command, and someone could slip in a command of their own (this is called "
             "SQL injection)."),
            ("point", "INSERT OR IGNORE",
             "adds each receipt unless its number is already in the table, in which case it skips it quietly."),
            ("point", "GROUP BY fund",
             "SUM(centavos) with GROUP BY fund gives one total per fund, the same totals Lesson 1 worked out "
             "with a dictionary."),
            ("point", "db.commit() and db.close()",
             "commit saves the changes for good; without it, the new rows are lost when the script ends. "
             "close lets go of the file."),
            ("point", "except sqlite3.IntegrityError",
             "the last INSERT tries to save OR 7650104 again. The database refuses, Python raises an "
             "IntegrityError, and the script catches it and prints the reason instead of stopping."),
            ("tip", "The database is a file like any other. Keep backup copies, and remember it holds "
                    "taxpayers' names and payments: under the Data Privacy Act, keep it where only the people "
                    "who need it can open it."),
            ("h", "Try it yourself"),
            ("try", "Write a query that lists each nature of collection with the number of receipts and the "
                    "total, biggest total first. Hint: COUNT(*), SUM(centavos), GROUP BY nature and "
                    "ORDER BY ... DESC."),
            ("answer", "answer_by_nature.py"),
        ],
    },
    {
        "number": 8,
        "slug": "check-data-before-you-trust-it",
        "folder": "08-check-data",
        "title": "Check a collections file before you trust it",
        "summary": "Catch blank payors, impossible dates, mistyped funds, commas in amounts and extra decimals, and list every problem by line.",
        "level": "Beginner",
        "minutes": 20,
        "topics": ["validation", "try and except", "datetime", "functions"],
        "publish_on": "2026-11-21",
        "learn": [
            "Write a function that checks one row and returns its problems",
            "Catch errors with try and except instead of letting the script stop",
            "Check dates, amounts, receipt numbers and allowed values",
            "Report each problem with its line number so it is easy to fix",
        ],
        "body": [
            "The scripts in the earlier lessons trusted their data. Real files are not so kind: a cashier "
            "types 1,050.00 with a comma, a letter O slips into a receipt number, a date reads November 31, "
            "or a fund is spelled Trust Fnd. Some of these stop a script with an error. Worse, some do not: "
            "the misspelled fund simply becomes a fourth fund in the totals and nobody notices. Checking the "
            "data first, and listing every problem at once, saves a lot of trouble later.",
            ("h", "The data"),
            "Save this as collections.csv. Seven of its ten rows have one problem each, planted on purpose.",
            ("file", "collections.csv"),
            ("h", "The code"),
            ("code", "check_rows.py"),
            ("h", "Output"),
            ("output", "check_rows.py"),
            "Every problem is listed with the line it is on, so the person who prepared the file can fix "
            "them all in one go. Line 5 is the comma: Python's Decimal reads 1050.00, but not 1,050.00.",
            ("h", "How it works"),
            ("point", "def check(row) -> list",
             "keeps all the rules in one function. It returns a list of problems, and an empty list means "
             "the row passed. Adding a rule later means adding a few lines here and nowhere else."),
            ("point", "number.isdigit() and len(number) == 7",
             "the receipt number must be seven digits. 76502O5 has the letter O instead of a zero, so "
             "isdigit() is false. (Use the length your own receipts have.)"),
            ("point", "try: ... except ValueError:",
             "date.fromisoformat(\"2026-11-31\") raises a ValueError, because November has 30 days. Instead "
             "of stopping, the except part runs and the problem is written down."),
            ("point", "row[\"fund\"] not in FUNDS",
             "FUNDS is a set of the allowed names. Anything else, such as Trust Fnd, is reported instead of "
             "becoming a new fund."),
            ("point", "except InvalidOperation: ... else:",
             "Decimal raises InvalidOperation for text that is not a number. The else part runs only when "
             "there was no error, so the amount is checked for zero, negative values and extra decimals "
             "only when it was read correctly."),
            ("point", "amount != amount.quantize(Decimal(\"0.01\"))",
             "980.405 changes when it is rounded to the centavo, so it has more than two decimal places."),
            ("point", "enumerate(..., start=2)",
             "counts the rows as it reads them. It starts at 2 because line 1 of the file is the header, so "
             "the numbers match what you see when you open the file."),
            ("tip", "The script lists the problems and leaves the file alone. It does not guess that Trust Fnd "
                    "means Trust Fund or remove the comma by itself. In treasury records it is safer for a "
                    "person to correct the source and run the check again than for a script to change "
                    "figures quietly."),
            ("h", "Try it yourself"),
            ("try", "Add a check that every date is the date of the report being prepared, 2026-11-03. Hint: "
                    "compare the date you read with date(2026, 11, 3), and remember that line 7 has a date "
                    "that cannot be read at all."),
            ("answer", "answer_date.py"),
        ],
    },
    {
        "number": 9,
        "slug": "test-your-code-with-pytest",
        "folder": "09-test-with-pytest",
        "title": "Test your treasury code with pytest",
        "summary": "Write short tests for the penalty and discount rules, run them all with one command, and see how a failing test points to the bug.",
        "level": "Intermediate",
        "minutes": 25,
        "topics": ["pytest", "assert", "parametrize", "testing"],
        "publish_on": "2026-11-28",
        "learn": [
            "Keep the rules in their own file so they can be tested",
            "Write a test as a function with assert",
            "Run many cases at once with pytest.mark.parametrize",
            "Check that bad input is refused with pytest.raises",
            "Read a failing test and find the mistake",
        ],
        "body": [
            "When you change a script, how do you know you did not break something that used to work? "
            "Checking by hand every time is slow and easy to skip. A test is a small function that runs your "
            "code with an input whose answer you already know, and complains if the answer is different. "
            "Once written, hundreds of tests run in a second, every time you change the code. pytest is "
            "the most widely used tool for this in Python.",
            ("tip", "Install pytest once with: py -m pip install pytest (Windows) or python3 -m pip install "
                    "pytest (Mac)."),
            ("h", "The code to test"),
            "These are the penalty rule from Lesson 3 and the discount from its practice answer, moved into a "
            "file of their own. Two checks were added: a negative amount or month count, and a discount rate "
            "above 20%, are refused. (RA 7160 allows a discount of up to 20% for paying in advance; the "
            "actual rate is set by each local ordinance.) Save this as rpt.py. It prints nothing by itself.",
            ("code", "rpt.py"),
            ("h", "The tests"),
            "Save this as test_rpt.py in the same folder. pytest looks for files whose names start with "
            "test_, and runs every function in them whose name starts with test_.",
            ("code", "test_rpt.py"),
            ("h", "Run the tests"),
            ("terminal", "py -m pytest -v test_rpt.py          (Windows)\npython3 -m pytest -v test_rpt.py     (Mac)"),
            ("output", "test_rpt.py"),
            ("tip", "On your computer, pytest also prints a line or two at the top with your Python and pytest "
                    "versions, and the time at the end will differ. -v (verbose) lists each test by name."),
            ("h", "How it works"),
            ("point", "from rpt import discount, penalty",
             "the tests use the real functions from rpt.py. That is why the rules were moved out of the report "
             "script: a test can use them without running the whole report."),
            ("point", "assert penalty(...) == Decimal(\"916.07\")",
             "assert means \"this must be true\". 2% of 4,580.33 for 10 months is 916.066, which rounds to "
             "916.07, the same figure Lesson 3 printed for TD-2024-01130."),
            ("point", "@pytest.mark.parametrize",
             "runs one test with several inputs. Here the same check, that the penalty stops at 72% of the "
             "tax, runs for 36, 37, 58 and 120 months. That is why 7 test functions became 10 tests."),
            ("point", "test_half_centavo_rounds_up",
             "2% of 0.25 is exactly 0.005. With ROUND_HALF_UP it must become 0.01. Small edge cases like "
             "this are where money code usually goes wrong."),
            ("point", "with pytest.raises(ValueError):",
             "this test passes only if the code inside raises a ValueError. It proves that bad input is "
             "refused instead of quietly producing a wrong penalty."),
            ("h", "What a failing test looks like"),
            "Tests are most useful when something breaks. This file has a copy of the penalty function that "
            "forgot the 36-month cap, and the same kind of test. Save it as test_forgot_cap.py and run it.",
            ("code", "test_forgot_cap.py"),
            ("terminal", "py -m pytest -v --tb=short test_forgot_cap.py          (Windows)\npython3 -m pytest -v --tb=short test_forgot_cap.py     (Mac)"),
            ("output", "test_forgot_cap.py"),
            "pytest shows the line that failed and both values: the function returned 1,160.00 (58 months at "
            "2%) where 720.00 was expected. That points straight at the missing cap. --tb=short keeps the "
            "report brief.",
            ("tip", "A good habit: when you find a bug, first write a test that fails because of it, then fix "
                    "the code until the test passes. The test stays, so the same bug cannot come back unnoticed."),
            ("h", "Try it yourself"),
            ("try", "Save the missing_numbers() function below as series.py, then write tests for it in "
                    "test_series.py: a complete series, a series with a gap, a duplicate that hides a gap, "
                    "and an empty list."),
            ("code", "series.py"),
            ("answer", "test_answer_series.py"),
        ],
    },
    {
        "number": 10,
        "slug": "web-page-with-flask",
        "folder": "10-flask-web-page",
        "title": "Show the day's collections on a web page with Flask",
        "summary": "Turn the collections script into a small web app with a totals page, a page per receipt and a JSON address, all in one Python file.",
        "level": "Intermediate",
        "minutes": 30,
        "topics": ["Flask", "routes", "templates", "JSON"],
        "publish_on": "2026-12-05",
        "learn": [
            "Write a Flask app with two routes",
            "Fill an HTML page with values using a template",
            "Take a receipt number from the address and answer 404 when it does not exist",
            "Run the app on your own computer and open it in a browser",
            "Check every page from a script with Flask's test client",
        ],
        "body": [
            "So far every script has printed its results in Command Prompt. A web app shows them in a "
            "browser instead, so a cashier or a supervisor can look at the day's totals without running "
            "anything. Flask is a small Python library for making web apps; this website and ALTOS are "
            "written in Python too. In this lesson the whole app is one file.",
            ("tip", "Install Flask once with: py -m pip install flask (Windows) or python3 -m pip install flask "
                    "(Mac)."),
            ("h", "The data"),
            "The same collections.csv as Lessons 1, 6 and 7, in a new folder.",
            ("file", "collections.csv"),
            ("h", "The app"),
            "Save this as app.py in the same folder.",
            ("code", "app.py"),
            ("h", "Run it"),
            ("terminal", "py app.py          (Windows)\npython3 app.py     (Mac)"),
            "Flask answers that it is running on http://127.0.0.1:5000. Open that address in your browser and "
            "you will see a table of the three fund totals. Add /receipt/7650106 to the address to see one "
            "receipt. Flask also prints a warning that this is a development server; that is expected, "
            "and the note on safety below explains it. Press Ctrl + C in Command Prompt or Terminal to stop "
            "the app.",
            ("h", "Check every page from a script"),
            "Clicking through pages by hand is slow. Flask has a test client that visits the pages from "
            "Python, without a browser or a running server. Save this as try_app.py and run it.",
            ("code", "try_app.py"),
            ("output", "try_app.py"),
            "The totals page shows the same figures as Lesson 1, the receipt page finds OR 7650106, and a "
            "receipt number that does not exist gets 404 Not Found, just as on any website.",
            ("h", "How it works"),
            ("point", "app = Flask(__name__)",
             "creates the web app. __name__ tells Flask where the app's file is."),
            ("point", "@app.route(\"/\")",
             "the line above a function says which address it answers. When a browser asks for /, Flask runs "
             "totals_page() and sends back what it returns."),
            ("point", "/receipt/<int:or_number>",
             "the part in angle brackets is taken from the address. For /receipt/7650106, Flask calls "
             "receipt_page(7650106). int: means only whole numbers are accepted."),
            ("point", "render_template_string(PAGE, ...)",
             "fills the HTML in PAGE with values. {{ fund }} is replaced by the fund name, and the {% for %} "
             "line repeats the table row for each fund. Flask escapes these values, so a payor name with < or "
             "& in it is shown as text and cannot break the page."),
            ("point", "abort(404)",
             "stops and answers \"404 Not Found\" when no receipt has that number."),
            ("point", "if __name__ == \"__main__\":",
             "app.run() starts the server only when you run app.py yourself, not when another script, such "
             "as try_app.py, imports it."),
            ("tip", "Safety: app.run() starts Flask's development server, meant only for trying things on your "
                    "own computer. It listens on 127.0.0.1, which only your computer can reach. Do not put it "
                    "on the office network or the internet as it is, never switch on debug mode on a shared "
                    "network, and add a login before any real taxpayer data goes into a web app."),
            ("h", "Try it yourself"),
            ("try", "Add an address /api/totals that returns the fund totals as JSON, so that another program "
                    "can read them. Hint: in Flask, a route that returns a Python dictionary is sent as JSON. "
                    "JSON has no Decimal type, so send each amount as text with two decimals."),
            ("answer", "answer_json.py"),
            "That is the end of this series for now. With these ten lessons you can read files, keep amounts "
            "exact, check and test your work, save it to Excel or a database, and show it on a web page: the "
            "same building blocks that larger treasury systems are made of.",
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
    6: "November 2026",
    7: "November 2026",
    8: "November 2026",
    9: "November 2026",
    10: "November 2026",
}
