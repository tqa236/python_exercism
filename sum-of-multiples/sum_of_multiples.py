"""Find the sum of all the unique multiples of some numbers up to a limit."""


def sum_of_multiples(limit, multiples):
    """Find the sum of all unique multiples of some numbers up to a limit."""
    if 0 in multiples:
        multiples.remove(0)
    return sum([i for i in range(limit) if any(i % j == 0 for j in multiples)])
