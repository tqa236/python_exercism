"""Return the number of grains for each square and for all squares."""


def is_valid_square(integer_number):
    """Check if the number represent a valid square."""
    if integer_number not in range(1, 65):
        raise ValueError("Wrong square")


def on_square(integer_number):
    """Return the number of grains for each square."""
    is_valid_square(integer_number)
    return 2 ** (integer_number - 1)


def total_after(integer_number):
    """Return the number of grains for all squares."""
    is_valid_square(integer_number)
    return 2 ** integer_number - 1
