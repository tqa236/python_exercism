from json import dumps
from typing import List


class Tree(object):
    def __init__(self, label: str, children: List["Tree"] = []) -> None:
        self.label = label
        self.children = children

    def __dict__(self):
        return {self.label: [c.__dict__() for c in sorted(self.children)]}

    def __str__(self, indent: None = None) -> str:
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other: "Tree") -> bool:
        return self.label < other.label

    def __eq__(self, other: None):
        return self.__dict__() == other.__dict__()

    def from_pov(self, from_node: str) -> None:
        pass

    def path_to(self, from_node: str, to_node: str) -> None:
        pass
