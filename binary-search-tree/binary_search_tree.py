"""Binary search tree."""

from typing import List, Optional


class TreeNode(object):
    """Simple tree node."""

    def __init__(
        self, data: str, left: Optional["TreeNode"], right: Optional["TreeNode"]
    ) -> None:
        """Initialize."""
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        """Override the string method."""
        fmt = "TreeNode(data={}, left={}, right={})"
        return fmt.format(self.data, self.left, self.right)

    def add(self, value: str) -> None:
        """Add new value to a node."""
        if value <= self.data:
            if not self.left:
                self.left = TreeNode(value, None, None)
            else:
                self.left.add(value)
        else:
            if not self.right:
                self.right = TreeNode(value, None, None)
            else:
                self.right.add(value)


class BinarySearchTree(object):
    """A simple binary tree."""

    def __init__(self, tree_data: List[str]) -> None:
        """Initialize."""
        self.tree_data = TreeNode(tree_data[0], None, None)
        for node in tree_data[1:]:
            self.tree_data.add(node)

    def data(self) -> None:
        """Return the whole tree."""
        return self.tree_data

    def sorted_data(self) -> None:
        """Return a list of sorted data."""
        go_left = True
        result = []
        nodes = []
        node = self.tree_data
        while node:
            if node.left and go_left:
                nodes.append(node)
                node = node.left
            else:
                go_left = False
                result.append(node.data)
                if node.right:
                    node = node.right
                    go_left = True
                else:
                    if nodes:
                        node = nodes.pop()
                    else:
                        break
        return result

    def add(self, value):
        """Add new value to the tree."""
        self.tree_data.add(value)
