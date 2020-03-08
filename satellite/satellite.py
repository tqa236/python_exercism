"""Construct a tree from the preoder and inorder traversals."""
from typing import List


def tree_from_traversals(preorder: List[str], inorder: List[str]) -> None:
    """Construct a tree from the preoder and inorder traversals."""
    if len(preorder) != len(inorder):
        raise ValueError("Wrong tree")
    if len(preorder) != len(set(preorder)):
        raise ValueError("Repeated item")
    if not preorder:
        return {}
    root = preorder[0]
    root_index = inorder.index(root)

    left_inorder = inorder[:root_index]
    right_inorder = inorder[root_index + 1 :]

    left_preoder = preorder[1 : len(left_inorder) + 1]
    right_preoder = preorder[len(left_inorder) + 1 :]

    left_tree = tree_from_traversals(left_preoder, left_inorder)
    right_tree = tree_from_traversals(right_preoder, right_inorder)

    return {"v": root, "l": left_tree, "r": right_tree}
