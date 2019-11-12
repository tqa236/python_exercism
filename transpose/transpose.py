"""Transpose a matrix."""
import itertools


def transpose(lines: str) -> None:
    """Transpose a matrix."""
    transpose_matrix = itertools.zip_longest(*lines.splitlines(), fillvalue="\n")
    return "\n".join(
        ["".join(line).rstrip("\n").replace("\n", " ") for line in transpose_matrix]
    )
