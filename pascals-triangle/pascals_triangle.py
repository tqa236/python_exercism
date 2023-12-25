from functools import cache
from copy import deepcopy


@cache
def rows(row_count):
    if row_count < 0:
        raise ValueError("number of rows is negative")
    if row_count == 0:
        return []
    if row_count == 1:
        return [[1]]
    base_triangle = deepcopy(rows(row_count - 1))
    last_line = [
        i + j for i, j in zip([0] + base_triangle[-1], base_triangle[-1] + [0])
    ]
    base_triangle.append(last_line)
    return base_triangle
