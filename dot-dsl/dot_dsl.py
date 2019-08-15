"""A simple Domain Specific Language."""
from typing import Any

NODE, EDGE, ATTR = range(3)


class Node(object):
    def __init__(self, name, attrs={}):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge(object):
    def __init__(self, src, dst, attrs={}):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (
            self.src == other.src
            and self.dst == other.dst
            and self.attrs == other.attrs
        )


class Graph(object):
    def __init__(self, data: Any = []) -> None:
        self.nodes = []
        self.edges = []
        self.attrs = {}
        if not isinstance(data, list):
            raise TypeError("Type not known.")
        for datum in data:
            if len(datum) <= 1:
                raise TypeError("Malformed graph item.")
            if datum[0] == NODE:
                if len(datum) != 3:
                    raise ValueError("Value not good.")
                self.nodes.append(Node(datum[1], datum[2]))
            elif datum[0] == EDGE:
                if len(datum) != 4:
                    raise ValueError("Value not good.")
                self.edges.append(Edge(datum[1], datum[2], datum[3]))
            elif datum[0] == ATTR:
                if len(datum) != 3:
                    raise ValueError("Value not good.")
                self.attrs[datum[1]] = datum[2]
            else:
                raise ValueError("Value not good.")
