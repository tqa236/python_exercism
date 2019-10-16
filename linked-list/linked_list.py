class Node(object):
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.succeeding = succeeding
        self.previous = previous


class LinkedList(object):
    def __init__(self) -> None:
        pass
