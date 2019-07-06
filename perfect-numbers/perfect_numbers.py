"""Classify numbers into the perfect number types."""
from functools import reduce


def classify(number: int) -> str:
    """Classify numbers into the perfect number types."""
    if number < 1:
        raise ValueError("Invalid number.")
    factors_sum = (
        sum(
            set(
                reduce(
                    list.__add__,
                    (
                        [s, number // s]
                        for s in range(1, int(number ** 0.5) + 1)
                        if not number % s
                    ),
                )
            )
        )
        / 2
    )
    if factors_sum == number:
        return "perfect"
    if factors_sum > number:
        return "abundant"
    return "deficient"
