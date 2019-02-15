"""Find the difference of square of natural numbers."""


def square_of_sum(count):
    """Calculate the square of sum of natural numbers."""
    return sum(range(count + 1))**2


def sum_of_squares(count):
    """Calculate the sum of squares of natural numbers."""
    return sum([i * i for i in range(count + 1)])


def difference(count):
    """Find the difference of square of natural numbers."""
    return square_of_sum(count) - sum_of_squares(count)
