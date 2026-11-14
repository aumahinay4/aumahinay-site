"""Keep official receipts in a small SQLite database and ask it questions with SQL.

sqlite3 comes with Python; there is nothing to install.
"""

import csv
import sqlite3
from decimal import Decimal

db = sqlite3.connect("register.db")      # creates the file the first time

db.execute("""
    CREATE TABLE IF NOT EXISTS receipts (
        or_number INTEGER PRIMARY KEY,   -- each receipt number only once
        date      TEXT    NOT NULL,
        payor     TEXT    NOT NULL,
        nature    TEXT    NOT NULL,
        fund      TEXT    NOT NULL,
        centavos  INTEGER NOT NULL       -- 1250.75 pesos is stored as 125075
    )
""")

with open("collections.csv", newline="", encoding="utf-8") as f:
    rows = [(int(r["or_number"]), r["date"], r["payor"], r["nature"], r["fund"],
             int(Decimal(r["amount"]) * 100)) for r in csv.DictReader(f)]

# INSERT OR IGNORE skips receipts already saved, so running the script twice adds nothing twice
db.executemany("INSERT OR IGNORE INTO receipts VALUES (?, ?, ?, ?, ?, ?)", rows)
db.commit()

count = db.execute("SELECT COUNT(*) FROM receipts").fetchone()[0]
print(f"Receipts in the register: {count}\n")

print("Total per fund")
for fund, centavos in db.execute(
        "SELECT fund, SUM(centavos) FROM receipts GROUP BY fund ORDER BY fund"):
    print(f"  {fund:<26}{Decimal(centavos) / 100:>12,.2f}")

payor = "Rosa Mendoza"
print(f"\nReceipts of {payor}")
for number, nature, centavos in db.execute(
        "SELECT or_number, nature, centavos FROM receipts WHERE payor = ? ORDER BY or_number", (payor,)):
    print(f"  {number}  {nature:<28}{Decimal(centavos) / 100:>10,.2f}")

# The database itself refuses a receipt number that is already used
try:
    db.execute("INSERT INTO receipts VALUES (7650104, '2026-11-02', 'Someone Else', "
               "'Community tax', 'General Fund', 10500)")
except sqlite3.IntegrityError as error:
    print(f"\nRefused OR 7650104 again: {error}")

db.close()
