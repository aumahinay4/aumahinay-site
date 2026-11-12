"""Tests for rpt.py. Run them with:  py -m pytest -v   (Mac: python3 -m pytest -v)"""

from decimal import Decimal

import pytest

from rpt import discount, penalty


def test_ten_months_late():
    assert penalty(Decimal("4580.33"), 10) == Decimal("916.07")


def test_no_penalty_when_paid_on_time():
    assert penalty(Decimal("1250.75"), 0) == Decimal("0.00")


@pytest.mark.parametrize("months", [36, 37, 58, 120])
def test_penalty_stops_at_36_months(months):
    assert penalty(Decimal("1000.00"), months) == Decimal("720.00")


def test_half_centavo_rounds_up():
    assert penalty(Decimal("0.25"), 1) == Decimal("0.01")   # 0.005 becomes 0.01


def test_negative_months_are_refused():
    with pytest.raises(ValueError):
        penalty(Decimal("1000.00"), -1)


def test_discount_of_ten_percent():
    assert discount(Decimal("980.40"), Decimal("10")) == Decimal("98.04")


def test_discount_above_twenty_percent_is_refused():
    with pytest.raises(ValueError):
        discount(Decimal("980.40"), Decimal("25"))
