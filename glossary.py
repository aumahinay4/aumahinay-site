"""Words to know: the glossary at the bottom of the Tutorials page (Python for Treasury Work).

Each word has:
  term     the word itself
  lesson   the lesson where it is first used (a link is shown only once that lesson is live)
  means    what it is, in plain words
  why      why it matters in treasury work
  code     a short example (Python unless "label" says otherwise)
  label    caption of the example box (default "Example")
  output   what the example really prints; check_glossary.py runs every example and compares
  after    one sentence under the example (optional)

Butch asked for fuller, more meaningful entries on 2026-11-24 PH. All names and amounts are made up.
"""

GLOSSARY_INTRO = (
    "These are the words that come up again and again in the lessons. Each one says what the word means, "
    "why it matters in treasury work, and gives a short example. Every Python example below was run, and the "
    "result shown under it is what it really prints."
)

GLOSSARY = [
    {
        "term": "Script",
        "lesson": 0,
        "means": "A plain text file of Python instructions, saved with a name that ends in .py. When you run it, "
                 "Python reads it from the top line to the bottom and does each step in order.",
        "why": "A script does the same job the same way every time. Write the steps for the day's total once, "
               "and tomorrow you only run the file again instead of redoing the work by hand.",
        "code": '# daily_note.py\nprint("Collections report for November 2, 2026")\nprint("Prepared by the collecting officer")',
        "output": "Collections report for November 2, 2026\nPrepared by the collecting officer",
        "after": "Run it with py daily_note.py on Windows or python3 daily_note.py on Mac.",
    },
    {
        "term": "Library",
        "lesson": 0,
        "means": "A collection of ready-made code that someone else wrote and tested. Some libraries come with "
                 "Python (the standard library, such as csv, decimal and sqlite3). Others, such as pandas, "
                 "openpyxl, pytest and Flask, are installed separately with pip.",
        "why": "You do not have to write your own Excel writer or CSV reader. A library gives you a tool that "
               "thousands of people already use, so you can spend your time on the treasury rules instead.",
        "code": "import pandas",
        "label": "If a library is not installed yet",
        "output": "ModuleNotFoundError: No module named 'pandas'",
        "after": "This error only means the library is missing. Install it once with pip (next word) and the "
                 "import works.",
    },
    {
        "term": "pip",
        "lesson": 0,
        "means": "Python's installer for extra libraries. It downloads them from the Python Package Index "
                 "(PyPI), the public store of free Python libraries, and sets them up on your computer.",
        "why": "You install a library once per computer, and then every script on that computer can use it. "
               "If a new office computer is set up, run the same pip command there too.",
        "code": "py -m pip install pandas openpyxl          (Windows)\npython3 -m pip install pandas openpyxl     (Mac)",
        "label": "Type this in Command Prompt or Terminal, not inside a script",
        "after": "Writing py -m pip (or python3 -m pip) makes sure the library goes to the same Python that "
                 "runs your scripts.",
    },
    {
        "term": "Variable",
        "lesson": 1,
        "means": "A name that holds a value, such as receipts = 10. The = sign means \"store this value under "
                 "this name\", not \"is equal to\". You can store a new value under the same name later.",
        "why": "Good names make a script read like a report: grand_total, receipts, fund. When a value changes, "
               "such as the booklet's first receipt number, you change it in one place.",
        "code": "receipts = 10\nreceipts = receipts + 1    # one more official receipt issued\nprint(receipts)",
        "output": "11",
    },
    {
        "term": "Loop",
        "lesson": 1,
        "means": "Code that repeats once for each item in a group. In Python it is written with for, and the "
                 "indented lines under it are the steps that repeat.",
        "why": "The same few lines handle 5 receipts or 5,000. A loop is how a script goes through every row "
               "of a collections file without you touching each row.",
        "code": "amounts = [4500, 1250, 105]\ntotal = 0\nfor amount in amounts:\n    total = total + amount\nprint(total)",
        "output": "5855",
    },
    {
        "term": "Module",
        "lesson": 1,
        "means": "One file of ready-made code that you bring into your script with import. A library is "
                 "usually made of one or more modules.",
        "why": "Modules that come with Python cover most everyday office work: csv reads files, decimal keeps "
               "peso amounts exact, datetime works with dates, and sqlite3 keeps a database.",
        "code": "from datetime import date\n\ncollected = date(2026, 11, 2)\ndeposited = date(2026, 11, 3)\n"
                "print((deposited - collected).days, \"day(s) from collection to deposit\")",
        "output": "1 day(s) from collection to deposit",
    },
    {
        "term": "CSV",
        "lesson": 1,
        "means": "Comma-separated values: a table saved as plain text, one row per line, with commas between "
                 "the columns. The first line usually holds the column names. A value that has a comma "
                 "inside it is wrapped in double quotes.",
        "why": "Excel, Google Sheets and most office systems can save or export a CSV, and Python reads it "
               "without installing anything. That makes it the easiest way to move collections data from "
               "one system into a script.",
        "code": "or_number,date,payor,fund,amount\n7650101,2026-11-02,\"Santos Bakery, Inc.\",General Fund,4500.00\n"
                "7650102,2026-11-02,Juan Dela Cruz,General Fund,1250.75",
        "label": "collections.csv",
        "after": "Python's csv module reads every value as text, so \"4500.00\" must be turned into a number "
                 "with Decimal before it can be added.",
    },
    {
        "term": "Dictionary",
        "lesson": 1,
        "means": "A set of pairs, each a key and a value, written with braces: {\"General Fund\": 4500}. You "
                 "look a value up by its key. Each key appears only once.",
        "why": "A dictionary is a ready lookup table, such as which fund each kind of collection goes to, or a "
               "running total for each fund while a script reads the day's receipts.",
        "code": "fund_of = {\n    \"Business tax\": \"General Fund\",\n"
                "    \"Real property tax (SEF)\": \"Special Education Fund\",\n}\n"
                "print(fund_of[\"Real property tax (SEF)\"])\nprint(fund_of.get(\"Fishery rental\", \"not listed\"))",
        "output": "Special Education Fund\nnot listed",
        "after": "fund_of[\"Fishery rental\"] would stop the script with a KeyError, because that key is not in "
                 "the dictionary. .get() gives a fallback value instead.",
    },
    {
        "term": "Decimal",
        "lesson": 1,
        "means": "A number type from Python's decimal module that stores amounts exactly as written, centavo "
                 "for centavo. Ordinary decimal numbers in Python (called float) are stored in binary and "
                 "cannot hold most centavo amounts exactly.",
        "why": "Totals, penalties and reports must agree to the centavo. With float, tiny errors build up as "
               "amounts are added and can show up as a centavo difference. Decimal avoids that.",
        "code": "from decimal import Decimal\n\nprint(0.10 + 0.20)\nprint(Decimal(\"0.10\") + Decimal(\"0.20\"))",
        "output": "0.30000000000000004\n0.30",
        "after": "Always make a Decimal from text, Decimal(\"0.10\"), not from a float, Decimal(0.10), or the "
                 "float's tiny error comes along with it.",
    },
    {
        "term": "f-string",
        "lesson": 1,
        "means": "Text that starts with the letter f and fills in values written inside braces. After a colon "
                 "you can say how the value should look: ,.2f means thousands separators and two decimal "
                 "places.",
        "why": "It is how a script prints amounts the way a report shows them, such as 21,986.15, and lines "
               "up columns so a printed summary is easy to check.",
        "code": "from decimal import Decimal\n\ntotal = Decimal(\"21986.15\")\nprint(f\"Total collections: {total:,.2f}\")",
        "output": "Total collections: 21,986.15",
    },
    {
        "term": "List",
        "lesson": 2,
        "means": "An ordered collection written with square brackets: [7650101, 7650102]. It keeps items in "
                 "the order you add them, allows repeats, and numbers its places from 0.",
        "why": "A list keeps official receipt numbers in the order they were recorded, and because it allows "
               "repeats, it lets a script find a number that was entered twice.",
        "code": "used = [7650101, 7650102, 7650104]\nused.append(7650105)\nprint(used[0])\nprint(len(used), \"receipts\")",
        "output": "7650101\n4 receipts",
    },
    {
        "term": "Set",
        "lesson": 2,
        "means": "A collection with no repeats and no fixed order, written with braces: {7650101, 7650102}. "
                 "Two sets can be compared: one minus the other gives what is in the first but not the "
                 "second.",
        "why": "Put every number in a receipt booklet in one set and every number actually used in another. "
               "Subtract them and the missing receipt numbers appear in a second.",
        "code": "booklet = set(range(7650101, 7650106))       # 7650101 to 7650105\n"
                "used = {7650101, 7650102, 7650104, 7650105}\nprint(sorted(booklet - used))",
        "output": "[7650103]",
    },
    {
        "term": "Function",
        "lesson": 3,
        "means": "A named set of steps that you can use again and again, written with def. You give it inputs "
                 "(parameters), and it hands back a result with return.",
        "why": "A rule written once in a function is used the same way everywhere. If the rule changes, you "
               "fix one function instead of every place that does the computation, and you can test it on "
               "its own.",
        "code": "from decimal import Decimal\n\ndef peso(amount):\n    return f\"PHP {amount:,.2f}\"\n\n"
                "print(peso(Decimal(\"1250.75\")))\nprint(peso(Decimal(\"21986.15\")))",
        "output": "PHP 1,250.75\nPHP 21,986.15",
    },
    {
        "term": "DataFrame",
        "lesson": 4,
        "means": "The table that the pandas library works with: rows, plus columns with names, much like a "
                 "sheet in Excel. pandas can read a whole CSV into a DataFrame in one line.",
        "why": "Summaries that take many steps by hand, such as totals per fund or per collector, take one "
               "line on a DataFrame. That makes it a quick way to prepare and cross-check report figures.",
        "code": "import pandas as pd\n\ndf = pd.DataFrame({\n"
                "    \"fund\": [\"General Fund\", \"Special Education Fund\", \"General Fund\"],\n"
                "    \"amount\": [4500.00, 1250.75, 105.00],\n})\n"
                "print(df.groupby(\"fund\")[\"amount\"].sum().to_string())",
        "output": "fund\nGeneral Fund              4605.00\nSpecial Education Fund    1250.75",
        "after": "pandas uses float for amounts, so round its results to two decimals before you put them in a "
                 "report.",
    },
    {
        "term": "Hash",
        "lesson": 5,
        "means": "A short fingerprint worked out from some data. The same data always gives the same "
                 "fingerprint, but change even one character and the fingerprint changes completely. "
                 "SHA-256, used in Lesson 5, gives a fingerprint 64 characters long.",
        "why": "Keep the hash of a file when you submit it. Later, hash the file again: if the two do not "
               "match, the file was changed after it was submitted.",
        "code": "import hashlib\n\nfor text in [\"OR 7650101 4500.00\", \"OR 7650101 4600.00\"]:\n"
                "    print(hashlib.sha256(text.encode()).hexdigest()[:16])",
        "output": "31ea3865d3707925\ndedceb079797ca66",
        "after": "Only the first 16 characters are shown. One changed digit gives a completely different "
                 "fingerprint.",
    },
    {
        "term": "HMAC",
        "lesson": 5,
        "means": "A hash made with a secret key (hash-based message authentication code). Only someone who "
                 "has the key can make a matching HMAC.",
        "why": "Anyone who edits a record can also make a new plain hash for it. With an HMAC they cannot, "
               "unless they have the key. That is what makes a log of collections tamper-evident.",
        "code": "import hashlib, hmac\n\nkey = b\"practice-key-only\"\n"
                "seal = hmac.new(key, b\"OR 7650101 4500.00\", hashlib.sha256).hexdigest()\n\n"
                "for text in [b\"OR 7650101 4500.00\", b\"OR 7650101 4600.00\"]:\n"
                "    check = hmac.new(key, text, hashlib.sha256).hexdigest()\n"
                "    print(text.decode(), hmac.compare_digest(seal, check))",
        "output": "OR 7650101 4500.00 True\nOR 7650101 4600.00 False",
        "after": "In real use, keep the key out of the script, for example in an environment variable.",
    },
    {
        "term": "Workbook",
        "lesson": 6,
        "means": "An Excel file (.xlsx). It holds one or more sheets, which the openpyxl library calls "
                 "worksheets. A new workbook starts with one sheet named Sheet.",
        "why": "Most offices still pass reports around in Excel. A script that writes a workbook gives the "
               "same tidy report every day, with no copying and pasting.",
        "code": "from openpyxl import Workbook\n\nwb = Workbook()\nws = wb.active\nws.title = \"Collections\"\n"
                "ws.append([\"OR number\", \"Payor\", \"Amount\"])\nws.append([7650101, \"Santos Bakery\", 4500.00])\n"
                "print(wb.sheetnames, ws.max_row, \"rows\")",
        "output": "['Collections'] 2 rows",
        "after": "wb.save(\"report.xlsx\") would then write the file.",
    },
    {
        "term": "Formula",
        "lesson": 6,
        "means": "A calculation stored in a cell, such as =SUM(C2:C11). openpyxl saves the formula as text; "
                 "Excel or another spreadsheet app works out its value when the file is opened.",
        "why": "A reviewer can click the total and see exactly how it was made, and the total updates by "
               "itself if a row is corrected later. A typed number gives neither.",
        "code": "from openpyxl import Workbook\n\nws = Workbook().active\nws[\"C12\"] = \"=SUM(C2:C11)\"\n"
                "print(ws[\"C12\"].value)",
        "output": "=SUM(C2:C11)",
        "after": "Python shows the formula, not the answer, because openpyxl never computes formulas.",
    },
    {
        "term": "Database",
        "lesson": 7,
        "means": "An organised store of records that a program can search, add to and total quickly. SQLite, "
                 "which comes with Python, keeps a whole database in one file.",
        "why": "A database can enforce rules by itself. Mark the official receipt number as the primary key "
               "and the database refuses the same number twice, even if a person or a script tries.",
        "code": "import sqlite3\n\ndb = sqlite3.connect(\":memory:\")     # a practice database in memory\n"
                "db.execute(\"CREATE TABLE receipts (or_number INTEGER PRIMARY KEY, centavos INTEGER)\")\n"
                "db.execute(\"INSERT INTO receipts VALUES (7650101, 450000)\")\ntry:\n"
                "    db.execute(\"INSERT INTO receipts VALUES (7650101, 10500)\")\n"
                "except sqlite3.IntegrityError as error:\n    print(\"Refused:\", error)",
        "output": "Refused: UNIQUE constraint failed: receipts.or_number",
    },
    {
        "term": "SQL",
        "lesson": 7,
        "means": "Structured Query Language: short commands that ask a database for data or change it. "
                 "SELECT reads, INSERT adds, WHERE picks rows, and GROUP BY totals by a column.",
        "why": "One SQL line answers the questions a treasury asks every day, such as the total per fund or "
               "every receipt of one payor, no matter how many records there are.",
        "code": "import sqlite3\n\ndb = sqlite3.connect(\":memory:\")\n"
                "db.execute(\"CREATE TABLE receipts (fund TEXT, centavos INTEGER)\")\n"
                "db.executemany(\"INSERT INTO receipts VALUES (?, ?)\",\n"
                "               [(\"General Fund\", 450000), (\"General Fund\", 10500), (\"Trust Fund\", 20000)])\n"
                "for fund, centavos in db.execute(\"SELECT fund, SUM(centavos) FROM receipts GROUP BY fund\"):\n"
                "    print(fund, centavos / 100)",
        "output": "General Fund 4605.0\nTrust Fund 200.0",
    },
    {
        "term": "Placeholder",
        "lesson": 7,
        "means": "A ? in an SQL command that the database fills in with a value you pass separately. The value "
                 "is treated only as data, never as part of the command.",
        "why": "Names typed into a system can contain any character, such as an apostrophe. Gluing them into "
               "the SQL text can break the command or, worse, let someone change what it does (SQL "
               "injection). Placeholders prevent both.",
        "code": "import sqlite3\n\ndb = sqlite3.connect(\":memory:\")\n"
                "db.execute(\"CREATE TABLE receipts (payor TEXT)\")\n"
                "payor = \"Lola's Kakanin\"                      # the apostrophe would break glued-in SQL\n"
                "db.execute(\"INSERT INTO receipts VALUES (?)\", (payor,))\n"
                "print(db.execute(\"SELECT COUNT(*) FROM receipts WHERE payor = ?\", (payor,)).fetchone()[0])",
        "output": "1",
    },
    {
        "term": "Exception",
        "lesson": 8,
        "means": "Python's way of reporting an error while a script runs. If nothing catches it, the script "
                 "stops. A try block with an except part catches it, so the script can note the problem and "
                 "carry on.",
        "why": "Real files have bad rows, such as an amount typed with a comma. Catching the error lets a "
               "script list every bad row for correction instead of stopping at the first one.",
        "code": "from decimal import Decimal, InvalidOperation\n\nfor text in [\"1250.75\", \"1,250.75\"]:\n"
                "    try:\n        print(Decimal(text))\n    except InvalidOperation:\n"
                "        print(\"Not a valid amount:\", text)",
        "output": "1250.75\nNot a valid amount: 1,250.75",
    },
    {
        "term": "Validation",
        "lesson": 8,
        "means": "Checking that data follows the rules, such as the right format, an allowed value or a "
                 "sensible amount, before you use it.",
        "why": "A total is only as good as the rows behind it. Checking first means a wrong fund name or a "
               "zero amount is caught before it reaches a report, not after the report is submitted.",
        "code": "FUNDS = {\"General Fund\", \"Special Education Fund\", \"Trust Fund\"}\n\n"
                "def problems(fund, amount):\n    found = []\n    if fund not in FUNDS:\n"
                "        found.append(f\"unknown fund {fund!r}\")\n    if amount <= 0:\n"
                "        found.append(\"amount must be more than zero\")\n    return found\n\n"
                "print(problems(\"General Fund\", 4500))\nprint(problems(\"Genral Fund\", 0))",
        "output": "[]\n[\"unknown fund 'Genral Fund'\", 'amount must be more than zero']",
    },
    {
        "term": "Test",
        "lesson": 9,
        "means": "A small function that runs your code with an input whose answer you already know, and "
                 "checks that the code gives that answer. pytest finds every function whose name starts "
                 "with test_ and runs them all at once.",
        "why": "Treasury rules have edge cases, such as a cap on months or a rounding rule. Tests check those "
               "cases every time you change the code, so a mistake is caught on your computer, not in an "
               "official computation.",
        "code": "from decimal import Decimal\n\ndef peso(amount):\n    return f\"PHP {amount:,.2f}\"\n\n"
                "def test_peso_adds_comma_and_centavos():\n    assert peso(Decimal(\"1250.5\")) == \"PHP 1,250.50\"",
        "label": "test_peso.py",
        "output": "1 passed",
        "after": "Run it with py -m pytest test_peso.py (Windows) or python3 -m pytest test_peso.py (Mac). "
                 "The last line of the report says 1 passed.",
    },
    {
        "term": "assert",
        "lesson": 9,
        "means": "A Python statement that checks something is true. If it is not, the script stops with an "
                 "AssertionError and the message you wrote after the comma.",
        "why": "It is the check inside every test, and a quick way to stop a script when two figures that "
               "must agree, such as collections and deposits, do not.",
        "code": "from decimal import Decimal\n\ncollected = Decimal(\"5750.75\")\ndeposited = Decimal(\"5750.00\")\n"
                "assert deposited == collected, \"Deposit does not match collections\"",
        "output": "AssertionError: Deposit does not match collections",
        "after": "Python skips assert statements when run with the -O option, so for checks that must always "
                 "run in a finished script, use if and print or raise instead.",
    },
    {
        "term": "Web app",
        "lesson": 10,
        "means": "A program that answers requests from a web browser with web pages. Flask is a small library "
                 "for writing one in Python. While you practise, it runs only on your own computer.",
        "why": "A web page lets others in the office see the day's collections in their browser, without "
               "running a script or opening a file themselves.",
        "code": "from flask import Flask\n\napp = Flask(__name__)\n\n@app.route(\"/\")\ndef home():\n"
                "    return \"<h1>Collections today</h1>\"\n\n"
                "print(app.test_client().get(\"/\").get_data(as_text=True))",
        "output": "<h1>Collections today</h1>",
        "after": "test_client() asks for the page without opening a browser. In Lesson 10, app.run() serves "
                 "the page at http://127.0.0.1:5000.",
    },
    {
        "term": "Route",
        "lesson": 10,
        "means": "In Flask, the link between a web address, such as /receipt/7650101, and the Python function "
                 "that makes that page. A part in angle brackets, such as <int:number>, is read from the "
                 "address and handed to the function.",
        "why": "Routes give every record its own address. Anyone in the office can open the page for one official "
               "receipt by its number instead of searching a long list.",
        "code": "from flask import Flask\n\napp = Flask(__name__)\n\n@app.route(\"/receipt/<int:number>\")\n"
                "def receipt(number):\n    return f\"Official receipt {number}\"\n\n"
                "print(app.test_client().get(\"/receipt/7650101\").get_data(as_text=True))",
        "output": "Official receipt 7650101",
    },
]
