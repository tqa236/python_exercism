"""Convert resistor colors to value."""

from typing import List

CODES = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}


def color_code(color: str) -> int:
    """Convert resistor colors to value."""
    return CODES[color]


def colors() -> List[str]:
    """Return the full list of colors."""
    return [color for color in CODES]
