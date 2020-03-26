from functools import reduce
from operator import mul


def largest_product(series: str, size: int) -> int:
    if size == 0:
        return 1
    if size < 0:
        raise ValueError("Invalid inputs")
    return max(
        [
            reduce(mul, [int(x) for x in series[i : i + size]], 1)
            for i in range(len(series) - size + 1)
        ]
    )
