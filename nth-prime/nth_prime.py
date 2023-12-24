"""Find the nth prime."""
from math import log


def prime(number: int) -> int:
    """Find the nth prime."""
    if number == 0:
        raise ValueError("there is no zeroth prime")
    upper_bound = 10 + (number + 1) * int(log(number + 1) + log(log(number + 1)))
    prime_list = range(2, upper_bound)
    for i in range(int(number**0.5) + 1):
        prime_list = list(
            filter(lambda x: x % prime_list[i] != 0 or x == prime_list[i], prime_list)
        )
    return prime_list[number - 1]
