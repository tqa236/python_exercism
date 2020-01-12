"""Fill the knapsack with the highest values item."""

from typing import Dict, List


def maximum_value(
    maximum_weight: int, items: List[Dict[str, int]], current_value: int = 0
) -> None:
    """Fill the knapsack with the highest values item."""
    if maximum_weight < 0:
        return -current_value
    if not items or maximum_weight == 0:
        return 0
    return max(
        maximum_value(maximum_weight, items[1:]),
        maximum_value(maximum_weight - items[0]["weight"], items[1:], items[0]["value"])
        + items[0]["value"],
    )
