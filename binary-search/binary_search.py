"""Binary search."""
from typing import List


def find(search_list: List[int], value: int) -> None:
    """Binary search."""
    start = 0
    end = len(search_list)
    while start < end:
        index = (start + end) // 2
        if search_list[index] == value:
            return index
        elif search_list[index] > value:
            end = index
        else:
            start = index + 1
    raise ValueError("Value doesn't exist in the list.")
