"""Implementation of a double linked list."""


class Node(object):
    """A simple node."""

    def __init__(self, value, succeeding=None, previous=None):
        """Initilize."""
        self.value = value
        self.succeeding = succeeding
        self.previous = previous


class LinkedList(object):
    """A double linked list."""

    def __init__(self) -> None:
        """Initialize."""
        self.head = None
        self.tail = None
        self.node = None

    def push(self, value):
        """Add a node to the tail of the linked list."""
        node = Node(value, None, self.tail)
        if self.tail:
            self.tail.succeeding = node
        self.tail = node
        if not self.head:
            self.head = self.tail

    def unshift(self, value):
        """Add a node to the head of the linked list."""
        node = Node(value, self.head, None)
        if self.head:
            self.head.previous = node
        self.head = node
        if not self.tail:
            self.tail = self.head

    def pop(self):
        """Remove a node from the tail of the linked list."""
        value = self.tail.value
        self.tail = self.tail.previous
        if self.tail:
            self.tail.succeeding = None
        else:
            self.head = None
        return value

    def shift(self):
        """Remove a node from the head of the linked list."""
        value = self.head.value
        self.head = self.head.succeeding
        if self.head:
            self.head.previous = None
        else:
            self.tail = None
        return value

    def __len__(self):
        """Override len method."""
        node = self.head
        count = 0
        while node is not None:
            count = count + 1
            node = node.succeeding
        return count

    def __iter__(self):
        """Override iter method."""
        node = self.head
        while node:
            yield node.value
            node = node.succeeding
