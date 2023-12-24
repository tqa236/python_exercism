"""Check a valid ISBN number."""
import re


def is_valid(isbn: str) -> bool:
    """Check a valid ISBN number."""
    isbn = isbn.replace("-", "")
    if not isbn:
        return False
    valid_characters = set([str(i) for i in range(10)])
    valid_characters.add("X")
    isbn_characters = set(c for c in isbn)
    if not isbn_characters.issubset(valid_characters):
        return False
    isbn_number = [int(digit) for digit in re.sub(r"\D", "", isbn)]
    if isbn[-1] == "X":
        isbn_number.append(10)
    return (
        sum([a * b for a, b in zip(isbn_number, range(10, 0, -1))]) % 11 == 0
        if len(isbn_number) == 10
        else False
    )
