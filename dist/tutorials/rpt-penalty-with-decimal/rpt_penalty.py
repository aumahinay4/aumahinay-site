"""Compute the penalty on delinquent real property tax with exact decimals.

The rule used here: 2% of the unpaid tax for every month of delinquency,
counted up to a ceiling of 36 months (72%), as provided in Section 255 of RA 7160.
"""

import csv
from decimal import Decimal, ROUND_HALF_UP

RATE_PER_MONTH = Decimal("0.02")
MAX_MONTHS = 36
CENTAVO = Decimal("0.01")


def penalty(tax_due: Decimal, months_late: int) -> Decimal:
    months = min(months_late, MAX_MONTHS)
    amount = tax_due * RATE_PER_MONTH * months
    return amount.quantize(CENTAVO, rounding=ROUND_HALF_UP)


print(f"{'TD number':<15}{'Year':>5}{'Tax due':>11}{'Months':>8}{'Penalty':>11}{'Total':>11}")
with open("delinquent.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        tax = Decimal(row["tax_due"])
        months = int(row["months_late"])
        pen = penalty(tax, months)
        shown = f"{min(months, MAX_MONTHS)}" + ("*" if months > MAX_MONTHS else "")
        print(f"{row['td_number']:<15}{row['year']:>5}{tax:>11,.2f}{shown:>8}{pen:>11,.2f}{tax + pen:>11,.2f}")

print("* capped at 36 months")
