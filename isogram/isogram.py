"""Verify if a string is an isogram or not."""


def is_isogram(string: str) -> bool:
    """Verify if a string is an isogram or not."""
    letters = "".join(c for c in string if c.isalpha()).lower()
    return len(set(letters)) == len(letters)
