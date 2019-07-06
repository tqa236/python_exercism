"""Make a diamond with letters."""
from string import ascii_uppercase


def make_space_pad(length: int) -> str:
    """Make a space string with a given length."""
    return "".join(" " for _ in range(length))


def make_row(letter: str, center_letter: str) -> str:
    """Make one row a diamond with letters."""
    center_pad_length = 2 * (ord(letter) - 65) - 1
    side_pad_length = ord(center_letter) - ord(letter)
    center = "A"
    if letter != "A":
        center = letter + make_space_pad(center_pad_length) + letter
    side_pad = make_space_pad(side_pad_length)
    return side_pad + center + side_pad


def make_diamond(letter: str) -> str:
    """Make a diamond with letters."""
    upper_part = [
        make_row(l, letter)
        for l in ascii_uppercase[: ascii_uppercase.index(letter) + 1]
    ]
    return "\n".join(upper_part + upper_part[::-1][1:]) + "\n"
