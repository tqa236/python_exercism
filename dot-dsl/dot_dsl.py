from typing import Any

NODE, EDGE, ATTR = range(3)


class Node:
    def __init__(self, name: str, attrs: dict[str, str] = {}) -> None:
        self.name = name
        self.attrs = attrs

    def __eq__(self, other: "Node") -> bool:
        return self.name == other.name and self.attrs == other.attrs


class Edge:
    def __init__(self, src: str, dst: str, attrs: dict[str, str] = {}) -> None:
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other: "Edge") -> bool:
        return (
            self.src == other.src
            and self.dst == other.dst
            and self.attrs == other.attrs
        )


class Graph:
    def __init__(self, data: Any = []) -> None:
        self.nodes = []
        self.edges = []
        self.attrs = {}
        if not isinstance(data, list):
            raise TypeError("Graph data malformed")
        for datum in data:
            if len(datum) <= 1:
                raise TypeError("Graph item incomplete")
            if datum[0] == NODE:
                if len(datum) != 3:
                    raise ValueError("Node is malformed")
                self.nodes.append(Node(datum[1], datum[2]))
            elif datum[0] == EDGE:
                if len(datum) != 4:
                    raise ValueError("Edge is malformed")
                self.edges.append(Edge(datum[1], datum[2], datum[3]))
            elif datum[0] == ATTR:
                if len(datum) != 3:
                    raise ValueError("Attribute is malformed")
                self.attrs[datum[1]] = datum[2]
            else:
                raise ValueError("Unknown item")
