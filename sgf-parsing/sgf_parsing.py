class SgfTree(object):
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
    if not input_string:
        raise ValueError("Empty input")
    if input_string in ['()', ';']:
        raise ValueError("Invalid input")
    if input_string == "(;)":
        return SgfTree()
    nodes = list(filter(None, input_string[1:-1].split(";")))
    print("nodes = ", nodes)
    tree = {}
    for i in nodes:
        if "[" not in i:
            raise ValueError("Node must have properties")
        key = i.split("[")[0]
        if key != key.upper():
            raise ValueError("Keys must be all capital")
        tree[key] = [i.split("[")[1][:-1]]
    print()
    print(tree)

    return SgfTree(properties=tree)
