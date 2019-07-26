"""A simple rotational cipher."""
from string import ascii_lowercase, ascii_uppercase
from typing import Optional


def rotate(text: str, key: int) -> Optional[str]:
    """Encode and decode text."""
    double_alphabet = ascii_lowercase * 2 + ascii_uppercase * 2
    return "".join(
        [
            double_alphabet[double_alphabet.index(ch) + key] if ch.isalpha() else ch
            for ch in text
        ]
    )
