"""Recognize a number."""

from typing import List

NUMBERS = {
    "0": [" _ ", "| |", "|_|", "   "],
    "1": ["   ", "  |", "  |", "   "],
    "2": [" _ ", " _|", "|_ ", "   "],
    "3": [" _ ", " _|", " _|", "   "],
    "4": ["   ", "|_|", "  |", "   "],
    "5": [" _ ", "|_ ", " _|", "   "],
    "6": [" _ ", "|_ ", "|_|", "   "],
    "7": [" _ ", "  |", "  |", "   "],
    "8": [" _ ", "|_|", "|_|", "   "],
    "9": [" _ ", "|_|", " _|", "   "],
}


def convert_one_number(number: List[str]) -> str:
    """Recognize a single number."""
    for key in NUMBERS:
        if "\n".join(number) == "\n".join(NUMBERS[key]):
            return key
    return "?"


def convert(input_grid: List[str]) -> None:
    """Recognize a list of numbers."""
    length = len(input_grid[0])
    width = len(input_grid)
    if width % 4 != 0 or length % 3 != 0:
        raise ValueError("Wrong input size.")
    numbers = [
        [
            [line[j : j + 3] for line in input_grid[i : i + 4]]
            for j in range(0, length, 3)
        ]
        for i in range(0, width, 4)
    ]
    return ",".join(
        ["".join([convert_one_number(number) for number in line]) for line in numbers]
    )
