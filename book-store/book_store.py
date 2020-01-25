"""Find the optimal price given a list of books."""
import math
from collections import Counter
from functools import reduce
from typing import List

BOOK_COST = 800
DISCOUNT_RATE = [0, 0.05, 0.1, 0.2, 0.25]
BOOK_PRICE = {(): 0}


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
    # The price to buy a book basket nth times will be equal to the price of a
    # big book basket with nth times the quantities of each book. So if the gcd
    # of the book quantities in a basket is bigger than 1, we divide the quantities
    # of all books to this gcd and later multiply the cost of this new book basket
    # with gcd to receive the price of the original book basket.
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
