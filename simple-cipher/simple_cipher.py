"""Implement a simple Ceasar cipher."""
import random
from string import ascii_lowercase


class Cipher(object):
    """Implement a simple Ceasar cipher."""

    def __init__(self, key=None):
        """Initialize key or create a random key if it is not provided."""
        self.key = key if key else "".join(
            random.choice(ascii_lowercase)
            for _ in range(100))

    def encode(self, text):
        """Encode text."""
        if not self.key:
            return text
        return "".join([chr((ord(char) + ord(self.key[index % len(self.key)])
                             - 97 * 2) % 26 + 97)
                        for index, char in enumerate(text)])

    def decode(self, text):
        """Decode text."""
        if not self.key:
            return text
        return "".join([chr((ord(char) - ord(self.key[index % len(self.key)]))
                            % 26 + 97)
                        for index, char in enumerate(text)])
