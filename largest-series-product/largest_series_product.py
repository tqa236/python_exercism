from functools import reduce
from operator import mul


def largest_product(series: str, size: int) -> int:
    # if size == 0:
    #     return 1
    if size < 0:
        raise ValueError("span must not be negative")
    if size > len(series):
        raise ValueError("span must be smaller than string length")
    clean_series = [int(i) for i in series if i.isdigit()]
    if len(series) > len(clean_series):
        raise ValueError("digits input must only contain digits")
    return max(
        [
            reduce(mul, [int(x) for x in series[i : i + size]], 1)
            for i in range(len(series) - size + 1)
        ],
    )
