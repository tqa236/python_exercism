"""Produce a greeting with an ordinal numeral for a customer in line."""


def line_up(name: str, number: int) -> str:
    """Produce a greeting with an ordinal numeral for a customer in line."""
    return f"{name}, you are the {number}{_suffix(number)} customer we serve today. Thank you!"


def _suffix(number: int) -> str:
    """Return the ordinal suffix for a given number."""
    if number % 100 in {11, 12, 13}:
        return "th"
    return {1: "st", 2: "nd", 3: "rd"}.get(number % 10, "th")
