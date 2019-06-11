"""Check if a number is an armstrong number."""


def is_armstrong(number: int) -> bool:
    """Check if a number is an armstrong number."""
    return sum([int(d)**len(str(number)) for d in str(number)]) == number
