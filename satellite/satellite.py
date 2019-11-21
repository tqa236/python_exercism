from typing import List


def tree_from_traversals(preorder: List[str], inorder: List[str]) -> None:
    if len(preorder) != len(inorder):
        raise ValueError("Wrong tree")
    return []
