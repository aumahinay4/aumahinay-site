"""The real property tax rules from Lesson 3, kept in one file so they can be tested."""

from decimal import Decimal, ROUND_HALF_UP

RATE_PER_MONTH = Decimal("0.02")
MAX_MONTHS = 36
CENTAVO = Decimal("0.01")


def penalty(tax_due: Decimal, months_late: int) -> Decimal:
    """2% of the unpaid tax for every month late, up to 36 months."""
    if tax_due < 0 or months_late < 0:
        raise ValueError("tax due and months late cannot be negative")
    months = min(months_late, MAX_MONTHS)
    return (tax_due * RATE_PER_MONTH * months).quantize(CENTAVO, rounding=ROUND_HALF_UP)


def discount(tax_due: Decimal, rate_percent: Decimal) -> Decimal:
    """A discount for paying early; the rate comes from the local ordinance."""
    if not 0 <= rate_percent <= 20:
        raise ValueError("the discount rate must be from 0 to 20 percent")
    return (tax_due * rate_percent / 100).quantize(CENTAVO, rounding=ROUND_HALF_UP)
