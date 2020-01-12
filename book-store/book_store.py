"""Find the optimal price given a list of books."""
from collections import Counter
from typing import List

BOOK_COST = 800
DISCOUNT_RATE = [0, 0.05, 0.1, 0.2, 0.25]


def total(basket: List[int]) -> float:
    """Find the optimal price given a list of books."""
    book_quantities = [value for _, value in Counter(basket).most_common()]
    return optimal_cost(book_quantities)


def optimal_cost(book_quantities: List[int]) -> float:
    """Find the optimal price given a list of quantities of books."""
    book_quantities = [
        book for book in sorted(book_quantities, reverse=True) if book > 0
    ]
    if not book_quantities:
        return 0
    cases = []
    for i in range(len(book_quantities)):
        cost = (i + 1) * BOOK_COST * (1 - DISCOUNT_RATE[i])
        new_basket = [
            book if index > i else book - 1
            for index, book in enumerate(book_quantities)
        ]
        cost = cost + optimal_cost(new_basket)
        cases.append(cost)
    return min(cases)
