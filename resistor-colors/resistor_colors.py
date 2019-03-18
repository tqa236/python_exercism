"""Convert resistor colors to value."""

CODES = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
         "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}


def value(colors):
    """Convert resistor colors to value."""
    return int("".join(str(CODES[color]) for color in colors))
