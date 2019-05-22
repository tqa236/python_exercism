"""Flatten nested array."""
from collections import Iterable


def flatten(iterable):
    """Flatten nested array."""
    if isinstance(iterable, Iterable) and not isinstance(iterable, str):
        return [a for i in iterable for a in flatten(i) if a is not None]
    return [iterable]
