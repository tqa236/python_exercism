"""Find the optimal price given a list of books."""
import math
import sys
from functools import reduce
from typing import List

sys.setrecursionlimit(10 ** 6)

BOOK_COST = 1


def optimal_cost(book_quantities: List[int], discount_rate) -> float:
    """Find the optimal price given a list of quantities of books."""
    book_quantities = tuple(
        [book for book in sorted(book_quantities, reverse=True) if book > 0]
    )
    if not book_quantities:
        return 0
    largest_gcd = reduce(math.gcd, book_quantities)
    core_quantities = tuple([quantity // largest_gcd for quantity in book_quantities])

    min_cost = None
    for i in range(len(core_quantities)):
        cost = (i + 1) * BOOK_COST * (10 - discount_rate[i])
        new_basket = [
            book if index > i else book - 1
            for index, book in enumerate(core_quantities)
        ]
        cost = cost + optimal_cost(new_basket, discount_rate)
        min_cost = min(min_cost, cost) if min_cost else cost
    return min_cost * largest_gcd


def optimal_cost1(book_quantities: List[int], discount_rate) -> float:
    """Find the optimal price given a list of quantities of books."""
    book_quantities = tuple(
        [book for book in sorted(book_quantities, reverse=True) if book > 0]
    )
    if not book_quantities:
        return 0
    min_cost = None
    for i in range(len(book_quantities)):
        cost = (i + 1) * BOOK_COST * (10 - discount_rate[i])
        new_basket = [
            book if index > i else book - 1
            for index, book in enumerate(book_quantities)
        ]
        cost = cost + optimal_cost1(new_basket, discount_rate)
        min_cost = min(min_cost, cost) if min_cost else cost
    return min_cost
