"""What a failing test looks like: this copy of penalty() forgot the 36-month cap."""

from decimal import Decimal


def penalty(tax_due: Decimal, months_late: int) -> Decimal:
    return (tax_due * Decimal("0.02") * months_late).quantize(Decimal("0.01"))


def test_penalty_stops_at_36_months():
    assert penalty(Decimal("1000.00"), 58) == Decimal("720.00")
