"""A lazy custom set implementation."""
from typing import List, Optional


class CustomSet:
    """A lazy custom set implementation."""

    def __init__(self, elements: List[int] = []) -> None:
        self.elements = set(elements)
        print(self.elements)

    def isempty(self) -> None:
        return not self.elements

    def __contains__(self, element: int) -> None:
        return element in self.elements

    def issubset(self, other: "CustomSet") -> None:
        return self.elements.issubset(other.elements)

    def isdisjoint(self, other: "CustomSet") -> None:
        return self.elements.isdisjoint(other.elements)

    def __eq__(self, other: Optional["CustomSet"]) -> None:
        return self.elements == other.elements

    def add(self, element: int) -> None:
        self.elements.add(element)

    def intersection(self, other: "CustomSet") -> None:
        return CustomSet(self.elements.intersection(other.elements))

    def __sub__(self, other: "CustomSet") -> None:
        return CustomSet(self.elements.difference(other.elements))

    def __add__(self, other: "CustomSet") -> None:
        return CustomSet(self.elements | other.elements)
