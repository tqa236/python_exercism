from typing import List, Optional


class TreeNode(object):
    def __init__(
        self, data: str, left: Optional["TreeNode"], right: Optional["TreeNode"]
    ) -> None:
        self.data = None
        self.left = None
        self.right = None

    def __str__(self):
        fmt = "TreeNode(data={}, left={}, right={})"
        return fmt.format(self.data, self.left, self.right)


class BinarySearchTree(object):
    def __init__(self, tree_data: List[str]) -> None:
        pass

    def data(self) -> None:
        pass

    def sorted_data(self) -> None:
        pass
