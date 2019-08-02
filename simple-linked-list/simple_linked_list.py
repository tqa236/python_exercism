from typing import Any, Iterator, List, Optional, Union


class Node(object):
    def __init__(self, value: int) -> None:
        self.node_value = value
        self.next_node = None

    def value(self) -> int:
        return self.node_value

    def next(self) -> Optional[Node]:
        return self.next_node


class LinkedList(object):
    def __init__(self, values: Union[range, List[int]] = []) -> None:
        self.head_node = None
        self.length = 0
        for value in values:
            self.push(value)
        self.length = len(values)
        self.index = self.length

    def __len__(self) -> int:
        return self.length

    def __iter__(self) -> Iterator[Any]:
        return (self.pop() for i in range(self.length))

    def head(self) -> Node:
        if self.__len__() == 0:
            raise EmptyListException("Empty linked list.")
        return self.head_node

    def push(self, value: int) -> None:
        node = Node(value)
        node.next_node = self.head_node
        self.head_node = node
        self.length = self.length + 1

    def pop(self) -> int:
        if self.__len__() == 0:
            raise EmptyListException("Empty linked list.")
        self.length = self.length - 1
        value = self.head().value()
        self.head_node = self.head_node.next()
        return value

    def reversed(self) -> LinkedList:
        if self.head_node is None:
            return self
        return self


class EmptyListException(Exception):
    pass
