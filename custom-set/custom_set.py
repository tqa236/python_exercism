from typing import List, Optional


class CustomSet:
    def __init__(self, elements: List[int] = []) -> None:
        pass

    def isempty(self) -> None:
        pass

    def __contains__(self, element: int) -> None:
        pass

    def issubset(self, other: "CustomSet") -> None:
        pass

    def isdisjoint(self, other: "CustomSet") -> None:
        pass

    def __eq__(self, other: Optional["CustomSet"]) -> None:
        pass

    def add(self, element: int) -> None:
        pass

    def intersection(self, other: "CustomSet") -> None:
        pass

    def __sub__(self, other: "CustomSet") -> None:
        pass

    def __add__(self, other: "CustomSet") -> None:
        pass
