"""Find the optimal price given a list of books."""
import math
import sys
from collections import Counter
from functools import reduce
from typing import List

sys.setrecursionlimit(10 ** 6)

BOOK_COST = 800
DISCOUNT_RATE = [0, 0.05, 0.1, 0.2, 0.25]

BOOK_PRICE = {(): 0}
BOOK_PRICE1 = {(): 0}


def total(basket: List[int]) -> float:
    """Find the optimal price given a list of books."""
    book_quantities = [value for _, value in Counter(basket).most_common()]
    return optimal_cost(book_quantities)


def optimal_cost(book_quantities: List[int]) -> float:
    """Find the optimal price given a list of quantities of books."""
    book_quantities = tuple(
        [book for book in sorted(book_quantities, reverse=True) if book > 0]
    )
    if not book_quantities:
        return 0
    largest_gcd = reduce(math.gcd, book_quantities)
    core_quantities = tuple([quantity // largest_gcd for quantity in book_quantities])
    if core_quantities in BOOK_PRICE:
        return BOOK_PRICE[core_quantities] * largest_gcd
    min_cost = None
    for i in range(len(core_quantities)):
        cost = (i + 1) * BOOK_COST * (1 - DISCOUNT_RATE[i])
        new_basket = [
            book if index > i else book - 1
            for index, book in enumerate(core_quantities)
        ]
        cost = cost + optimal_cost(new_basket)
        min_cost = min(min_cost, cost) if min_cost else cost
        BOOK_PRICE[core_quantities] = min_cost
    return min_cost * largest_gcd


def optimal_cost1(book_quantities: List[int]) -> float:
    """Find the optimal price given a list of quantities of books."""
    book_quantities = tuple(
        [book for book in sorted(book_quantities, reverse=True) if book > 0]
    )
    if not book_quantities:
        return 0
    largest_gcd = 1
    core_quantities = tuple([quantity // largest_gcd for quantity in book_quantities])
    # if core_quantities in BOOK_PRICE1:
    #     return BOOK_PRICE1[core_quantities] * largest_gcd
    min_cost = None
    for i in range(len(core_quantities)):
        cost = (i + 1) * BOOK_COST * (1 - DISCOUNT_RATE[i])
        new_basket = [
            book if index > i else book - 1
            for index, book in enumerate(core_quantities)
        ]
        cost = cost + optimal_cost1(new_basket)
        min_cost = min(min_cost, cost) if min_cost else cost
        BOOK_PRICE1[core_quantities] = min_cost
    return min_cost * largest_gcd


# Additional test case (Exercism doesn't preserve changed test files.)
# from hypothesis import given, settings
# from hypothesis.strategies import lists, integers
# from book_store import total, optimal_cost
#     @given(
#         list1=lists(integers(min_value=0, max_value=30), min_size=5, max_size=5),
#         list2=lists(integers(min_value=0, max_value=30), min_size=5, max_size=5),
#     )
#     @settings(deadline=None)
#     def test_combine_of_two_book_sets_is_always_cheaper(self, list1, list2):
#         self.assertEqual(
#             optimal_cost(list1) + optimal_cost(list2)
#             >= optimal_cost([i + j for i, j in zip(list1, list2)]),
#             True,
#         )
