"""Calculate the scrabble score of a word."""


from typing import Dict


def make_value_dict() -> Dict[str, int]:
    """Make a value dictionary for scrabble."""
    value_dict = {}

    def write_input(key, value):
        """Put the input to the dictionary."""
        for character in key:
            value_dict[character] = value

    values = [
        ("AEUIOULNRST", 1),
        ("DG", 2),
        ("BCMP", 3),
        ("FHVWY", 4),
        ("K", 5),
        ("JX", 8),
        ("QZ", 10),
    ]
    for value in values:
        write_input(value[0], value[1])
    return value_dict


def score(word: str) -> int:
    """Calculate the scrabble score of a word."""
    value_dict = make_value_dict()
    return sum(value_dict[character] for character in word.upper())
