def triplets_with_sum(sum_of_triplet):
    triplet = []
    for a in range(1, sum_of_triplet // 3 + 1):
        b = (sum_of_triplet**2 - 2 * sum_of_triplet *
             a) // (2 * (sum_of_triplet - a))
        c = sum_of_triplet - a - b
        if a**2 + b**2 == c**2:
            triplet.append((a, b, c))
    return set(triplet)


def triplets_in_range(range_start, range_end):
    pass


def is_triplet(triplet):
    return triplet[0] ** 2 + triplet[1] ** 2 == triplet[2] ** 2
