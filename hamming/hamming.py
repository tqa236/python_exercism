"""Find the Hamming distance of two ADN strands."""


def distance(strand_a: str, strand_b: str) -> int:
    """Find the Hamming distance of two ADN strands."""
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    return sum(i != j for i, j in zip(strand_a, strand_b))
