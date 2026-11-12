"""A small function from Lesson 2: which receipt numbers are missing from a series."""


def missing_numbers(used: list) -> list:
    """Numbers between the lowest and highest used that do not appear."""
    if not used:
        return []
    return sorted(set(range(min(used), max(used) + 1)) - set(used))
