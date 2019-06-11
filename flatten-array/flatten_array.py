"""Flatten nested array."""
from collections import Iterable
from typing import Any, List, Union


def flatten(iterable: Any) -> Union[List[str], List[int], List[None]]:
    """Flatten nested array."""
    if isinstance(iterable, Iterable) and not isinstance(iterable, str):
        return [a for i in iterable for a in flatten(i) if a is not None]
    return [iterable]
