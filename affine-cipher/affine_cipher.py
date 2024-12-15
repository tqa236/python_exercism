"""Affine Cipher."""

from math import gcd
from string import ascii_lowercase

ALPHABET_LENGTH = 26


def convert(text: str, a: int, b: int) -> str:
    """Convert the main part of encoding and decoding."""
    if gcd(a, ALPHABET_LENGTH) != 1:
        raise ValueError("a and m must be coprime.")
    text = "".join([char for char in text.lower() if char.isalnum()])
    plain_numbers = [
        ascii_lowercase.index(char) if char in ascii_lowercase else -1 for char in text
    ]
    encoded_numbers = [
        (a * item + b) % ALPHABET_LENGTH if item >= 0 else item
        for item in plain_numbers
    ]
    encoded_text = "".join(
        ascii_lowercase[value] if value >= 0 else text[index]
        for index, value in enumerate(encoded_numbers)
    )
    return encoded_text


def encode(plain_text: str, a: int, b: int) -> None:
    """Encode."""
    encoded_text = convert(plain_text, a, b)
    return " ".join([encoded_text[i : i + 5] for i in range(0, len(encoded_text), 5)])


def decode(ciphered_text: str, a: int, b: int) -> None:
    """Decode."""
    if gcd(a, ALPHABET_LENGTH) != 1:
        raise ValueError("a and m must be coprime.")
    mmi = [(a * n) % ALPHABET_LENGTH for n in range(ALPHABET_LENGTH)].index(1)
    return convert(ciphered_text, mmi, -mmi * b)
