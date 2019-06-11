"""Find a largest products of continuous elements of a series."""
from operator import mul
from functools import reduce


def largest_product(series: str, size: int) -> int:
    """Find a largest products of continuous elements of a series."""
    if size == 0:
        return 1
    if size < 0:
        raise ValueError("Invalid inputs")
    return max([reduce(mul, [int(x) for x in series[i:i+size]], 1)
                for i in range(len(series) - size + 1)])
