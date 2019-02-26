"""Factorize a number."""
import math


def prime_factors(natural_number):
    """Factorize a number."""
    i = 2
    factors = []
    while natural_number % 2 == 0:
        factors.append(2)
        natural_number = natural_number / 2
    for i in range(3, int(math.sqrt(natural_number)) + 1, 2):
        while natural_number % i == 0:
            factors.append(i)
            natural_number = natural_number / i
    if natural_number > 2:
        factors.append(natural_number)
    return factors
