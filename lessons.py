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
    ("tip", "text")             a highlighted note
    ("try", "text")             a practice exercise
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
        "To follow along, install Python 3 from python.org, save a lesson's files into one folder, "
        "and run the script from that folder, for example: python daily_total.py"
    ),
}

LESSONS = [
    {
        "number": 1,
        "slug": "add-up-daily-collections",
        "folder": "01-daily-collections",
        "title": "Add up a day's collections from a CSV file",
        "summary": "Read the day's official receipts from a spreadsheet export and total them per fund, to the centavo.",
        "level": "Beginner",
        "minutes": 15,
        "topics": ["csv", "Decimal", "dictionaries", "f-strings"],
        "publish_on": "2026-11-05",
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
            ("h", "How it works"),
            ("point", "csv.DictReader",
             "reads the file and gives each row as a dictionary, so you can write row[\"amount\"] "
             "instead of remembering that the amount is the sixth column."),
            ("point", "Decimal(row[\"amount\"])",
             "turns the text 4500.00 into an exact decimal number. Ordinary floating-point numbers "
             "store most centavo amounts with tiny errors; Lesson 3 shows why that matters."),
            ("point", "totals.get(fund, Decimal(\"0\"))",
             "looks up the running total for a fund, or starts it at zero the first time the fund "
             "appears. New funds are picked up automatically."),
            ("point", "f\"{total:>16,.2f}\"",
             "formats a number right-aligned in 16 spaces, with thousands separators and two decimal "
             "places, so the columns line up like a printed report."),
            ("tip", "Open the CSV with newline=\"\" and an explicit encoding. It prevents blank rows on "
                    "Windows and keeps names with ñ readable."),
            ("h", "Try it yourself"),
            ("try", "Add a second total per nature of collection (Business tax, Real property tax, and so "
                    "on). Hint: make another dictionary and fill it inside the same loop."),
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
        "publish_on": "2026-11-12",
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
        "publish_on": "2026-11-19",
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
        "publish_on": "2026-11-26",
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
            ("tip", "pandas is not part of standard Python. Install it once with: pip install pandas"),
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
                    "pd.ExcelWriter. (You may need: pip install openpyxl.)"),
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
        "publish_on": "2026-12-03",
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
             "why Check 3 points at position 3."),
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
        ],
    },
]
