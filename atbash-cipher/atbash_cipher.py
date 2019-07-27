"""Encode and decode text with atbash cipher."""
from typing import Optional
import re
import string


def encode(plain_text: str) -> None:
    """Encode."""
    pattern = re.compile(r"[\W_]+", re.UNICODE)
    clean_text = pattern.sub("", plain_text).lower()
    ciphered_text = decode(clean_text)
    ciphered_text = " ".join(
        [ciphered_text[i : i + 5] for i in range(0, len(ciphered_text), 5)]
    )
    return ciphered_text


def decode(ciphered_text: Optional[str]) -> None:
    """Decode."""
    reversed_alphabet = string.ascii_lowercase[::-1]
    return "".join(
        reversed_alphabet[string.ascii_lowercase.index(char)]
        if char.isalpha()
        else char
        for char in ciphered_text.replace(" ", "")
    )
