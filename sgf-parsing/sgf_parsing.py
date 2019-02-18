"""Build a class to parse SGF format."""
import re


class SgfTree(object):
    """Build a class to parse SGF format."""

    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def parse(input_string):
    """Build a function to parse SGF format."""
    if input_string in ['()', ';', ""]:
        raise ValueError("Invalid input")
    if input_string == "(;)":
        return SgfTree()
    nodes = list(filter(None, input_string[1:-1].split(";")))
    print("nodes = ", nodes)
    whole_tree = []
    for node in nodes:
        tree = {}
        if "[" not in node:
            raise ValueError("Node must have properties")
        key = node.split("[")[0]
        if key != key.upper():
            raise ValueError("Keys must be all capital")
        print(node.split("["))
        value = [x.split("]")[0] for x in node.split("[") if "]" in x]
        tree[key] = value
        whole_tree.append(tree)
    print("whole tree = ", whole_tree)
    children = [SgfTree(properties=x) for x in whole_tree[1:]]
    return SgfTree(properties=whole_tree[0], children=children)
