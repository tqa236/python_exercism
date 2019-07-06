"""Check a valid ISBN number."""
import re


def verify(isbn: str) -> bool:
    """Check a valid ISBN number."""
    if not isbn:
        return False
    isbn_number = [int(digit) for digit in re.sub(r"\D", "", isbn)]
    if isbn[-1] == "X":
        isbn_number.append(10)
    return (
        sum([a * b for a, b in zip(isbn_number, range(10, 0, -1))]) % 11 == 0
        if len(isbn_number) == 10
        else False
    )
