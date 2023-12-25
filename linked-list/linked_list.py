from __future__ import annotations


class Node(object):
    def __init__(
        self,
        value: int,
        succeeding: Node | None,
        previous: Node | None,
    ) -> None:
        self.value = value
        self.succeeding = succeeding
        self.previous = previous


class LinkedList(object):
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.node = None

    def push(self, value: int) -> None:
        node = Node(value, None, self.tail)
        if self.tail:
            self.tail.succeeding = node
        self.tail = node
        if not self.head:
            self.head = self.tail

    def unshift(self, value: int) -> None:
        node = Node(value, self.head, None)
        if self.head:
            self.head.previous = node
        self.head = node
        if not self.tail:
            self.tail = self.head

    def pop(self) -> int:
        if self.tail is None:
            raise IndexError("List is empty")
        value = self.tail.value
        self.tail = self.tail.previous
        if self.tail:
            self.tail.succeeding = None
        else:
            self.head = None
        return value

    def shift(self) -> int:
        if self.head is None:
            raise IndexError("List is empty")
        value = self.head.value
        self.head = self.head.succeeding
        if self.head:
            self.head.previous = None
        else:
            self.tail = None
        return value

    def delete(self, value) -> int:
        node = self.head
        while node:
            if node.value == value:
                if node.previous is None and node.succeeding is None:
                    self.head = None
                    self.tail = None
                    return
                if node.succeeding is not None:
                    node.succeeding.previous = node.previous
                else:
                    self.tail = node.previous
                if node.previous is not None:
                    node.previous.succeeding = node.succeeding
                else:
                    self.head = node.succeeding
                return
            node = node.succeeding
        raise ValueError("Value not found")

    def __len__(self) -> int:
        node = self.head
        count = 0
        while node is not None:
            count = count + 1
            node = node.succeeding
        return count
