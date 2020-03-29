"""Verify if a string is an isogram or not."""


def is_isogram(string: str) -> bool:
    """Verify if a string is an isogram or not."""
    letters = [c for c in string.lower() if c.isalpha()]
    return len(set(letters)) == len(letters)
