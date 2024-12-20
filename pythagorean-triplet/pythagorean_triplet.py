"""Find all pythagorean triplets of a given sum."""

from typing import Set, Tuple


def triplets_with_sum(sum_of_triplet: int) -> Set[Tuple[int, int, int]]:
    """Find all pythagorean triplets of a given sum."""
    triplet = []
    for a in range(1, sum_of_triplet // 3):
        b = (sum_of_triplet**2 - 2 * sum_of_triplet * a) // (2 * (sum_of_triplet - a))
        c = sum_of_triplet - a - b
        if a**2 + b**2 == c**2:
            triplet.append((min(a, b), max(a, b), c))
    return [list(unique_triplet) for unique_triplet in set(triplet)]


def is_triplet(triplet):
    """Verify if a triplet is a pythagorean triplet."""
    return triplet[0] ** 2 + triplet[1] ** 2 == triplet[2] ** 2
