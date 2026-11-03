"""Answer: a discount for paying real property tax in advance.

The rate here (10%) is only an example. RA 7160 lets the sanggunian set a
discount of up to 20%, so use the rate in your own ordinance.
"""

from decimal import Decimal, ROUND_HALF_UP

CENTAVO = Decimal("0.01")


def discount(tax_due: Decimal, rate_percent: Decimal) -> Decimal:
    amount = tax_due * rate_percent / 100
    return amount.quantize(CENTAVO, rounding=ROUND_HALF_UP)


for tax in (Decimal("1250.75"), Decimal("980.40"), Decimal("4580.33")):
    off = discount(tax, Decimal("10"))
    print(f"Tax {tax:>9,.2f}   discount {off:>7,.2f}   to pay {tax - off:>9,.2f}")
