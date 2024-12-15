"""Factorize a number."""

import math
from typing import List, Union


def factors(natural_number: int) -> Union[List[Union[int, float]], List[int]]:
    """Factorize a number."""
    i = 2
    prime_factors = []
    while natural_number % 2 == 0:
        prime_factors.append(2)
        natural_number = natural_number / 2
    for i in range(3, int(math.sqrt(natural_number)) + 1, 2):
        while natural_number % i == 0:
            prime_factors.append(i)
            natural_number = natural_number / i
    if natural_number > 2:
        prime_factors.append(natural_number)
    return prime_factors
