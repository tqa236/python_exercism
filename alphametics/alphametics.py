"""Solve alphametics puzzles."""
import string
from itertools import permutations


def parse_number(number, value_dict):
    """Convert letters to number."""
    return int("".join([value_dict[letter] for letter in number]))


def solve(puzzle: str) -> None:
    """Solve alphametics puzzles."""
    letters = list(
        set([letter for letter in puzzle if letter in string.ascii_uppercase])
    )
    left_side, right_side = puzzle.replace(" ", "").split("==")
    left_side = left_side.split("+")
    non_zeros = set([letter[0] for letter in left_side])
    non_zeros.add(right_side[0])
    all_permutations = permutations(range(10), len(letters))
    for permutation in all_permutations:
        value_dict = {k: str(v) for k, v in zip(letters, permutation)}
        if "0" not in [value_dict[i] for i in non_zeros]:
            left_value = sum(parse_number(number, value_dict) for number in left_side)
            right_value = parse_number(right_side, value_dict)
            if left_value == right_value:
                return {k: int(v) for k, v in value_dict.items()}
    return None
