"""Implement a simple Ceasar cipher."""
import secrets
from string import ascii_lowercase
from typing import Optional


class Cipher(object):
    """Implement a simple Ceasar cipher."""

    def __init__(self, key: Optional[str] = None) -> None:
        """Initialize key or create a random key if it is not provided."""
        self.key = (
            key if key else "".join(secrets.choice(ascii_lowercase) for _ in range(100))
        )

    def encode(self, text: str) -> str:
        """Encode text."""
        if not self.key:
            return text
        return "".join(
            [
                chr(
                    (ord(char) + ord(self.key[index % len(self.key)]) - 97 * 2) % 26
                    + 97
                )
                for index, char in enumerate(text)
            ]
        )

    def decode(self, text: str) -> str:
        """Decode text."""
        if not self.key:
            return text
        return "".join(
            [
                chr((ord(char) - ord(self.key[index % len(self.key)])) % 26 + 97)
                for index, char in enumerate(text)
            ]
        )
