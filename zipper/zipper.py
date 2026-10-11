from typing import Any, Dict, Optional


class Zipper(object):
    def __init__(
        self,
        value: int,
        left: Optional["Zipper"] = None,
        right: Optional["Zipper"] = None,
        parent: Optional["Zipper"] = None,
    ) -> None:
        self._value = value
        self._left = left
        self._right = right
        self._parent = parent

        if self._left is not None:
            self._left._parent = self
        if self._right is not None:
            self._right._parent = self

    @staticmethod
    def from_tree(
        tree: Optional[Dict[str, Any]], parent: Optional["Zipper"] = None
    ) -> Optional["Zipper"]:
        if tree is None:
            return None

        zipper = Zipper(tree["value"], parent=parent)
        zipper._left = Zipper.from_tree(tree.get("left"), parent=zipper)
        zipper._right = Zipper.from_tree(tree.get("right"), parent=zipper)
        return zipper

    def value(self) -> int:
        return self._value

    def set_value(self, value: int) -> "Zipper":
        self._value = value
        return self

    def left(self) -> Optional["Zipper"]:
        return self._left

    def set_left(self, tree: Optional[Dict[str, Any]]) -> "Zipper":
        self._left = Zipper.from_tree(tree, parent=self)
        return self

    def right(self) -> Optional["Zipper"]:
        return self._right

    def set_right(self, tree: Optional[Dict[str, Any]]) -> "Zipper":
        self._right = Zipper.from_tree(tree, parent=self)
        return self

    def up(self) -> Optional["Zipper"]:
        return self._parent

    def to_tree(self) -> Dict[str, Any]:
        root = self
        while root._parent is not None:
            root = root._parent

        def build(node: Optional["Zipper"]) -> Optional[Dict[str, Any]]:
            if node is None:
                return None
            return {
                "value": node._value,
                "left": build(node._left),
                "right": build(node._right),
            }

        return build(root)
