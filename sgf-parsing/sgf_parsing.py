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
    if input_string in ['()', ';', '(;)']:
        raise ValueError("Invalid input")
    nodes = list(filter(None, input_string[1:-1].split(";")))
    print(nodes)
    for i in nodes:
        if i[0].islower():
            raise ValueError("Invalid key")
        key = i.split("[")[0]
        print(key[0])
        return SgfTree(properties={key: i.split("[")[1][:-1]})
