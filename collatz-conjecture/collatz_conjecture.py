"""Return the number of steps in a collatz conjecture."""


def collatz_steps(number: int) -> int:
    """Return the number of steps in a collatz conjecture."""
    if number < 1:
        raise ValueError("Number must be a positive integer")
    count = 0
    while number > 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
        count = count + 1
    return count
