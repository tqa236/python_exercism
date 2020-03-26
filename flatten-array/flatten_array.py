"""Flatten nested array."""
from collections.abc import Iterable
from typing import Any, List, Union


def flatten(iterable: Any) -> Union[List[None], List[str], List[int]]:
    """Flatten nested array."""
    if isinstance(iterable, Iterable) and not isinstance(iterable, str):
        return [a for i in iterable for a in flatten(i) if a is not None]
    return [iterable]
