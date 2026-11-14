"""Answer: tests for missing_numbers() in series.py."""

from series import missing_numbers


def test_complete_series_has_no_gaps():
    assert missing_numbers([7650101, 7650102, 7650103]) == []


def test_finds_the_gaps():
    assert missing_numbers([7650101, 7650104, 7650102]) == [7650103]


def test_duplicates_do_not_hide_a_gap():
    assert missing_numbers([7650101, 7650101, 7650103]) == [7650102]


def test_empty_list():
    assert missing_numbers([]) == []
