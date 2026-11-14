"""Answer: for each nature of collection, show the number of receipts and the total.

Run register.py first; this reads the database it made.
"""

import sqlite3
from decimal import Decimal

db = sqlite3.connect("register.db")
query = """
    SELECT nature, COUNT(*), SUM(centavos)
    FROM receipts
    GROUP BY nature
    ORDER BY SUM(centavos) DESC, nature
"""
print(f"{'Nature of collection':<28}{'ORs':>4}{'Amount':>12}")
for nature, receipts, centavos in db.execute(query):
    print(f"{nature:<28}{receipts:>4}{Decimal(centavos) / 100:>12,.2f}")
db.close()
