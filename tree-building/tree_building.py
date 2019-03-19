"""Build a tree of records."""


class Record():
    """Simple record class."""

    def __init__(self, record_id, parent_id):
        """Initialize."""
        self.record_id = record_id
        self.parent_id = parent_id


class Node():
    """Simple node class."""

    def __init__(self, node_id):
        """Initialize."""
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    """Build a tree of records."""
    records.sort(key=lambda x: x.record_id)
    ordered_id = [i.record_id for i in records]
    if not records:
        return None
    if ordered_id[-1] != len(ordered_id) - 1:
        raise ValueError('Tree must be continuous')
    if ordered_id[0] != 0:
        raise ValueError('Tree must start with id 0')
    trees = []
    parent = {}
    for i in range(len(ordered_id)):
        for j in records:
            if ordered_id[i] == j.record_id:
                if j.record_id == 0 and j.parent_id != 0:
                    raise ValueError('Root node cannot have a parent')
                elif j.record_id < j.parent_id:
                    raise ValueError('Parent id must be lower than child id')
                elif j.record_id == j.parent_id and j.record_id != 0:
                    raise ValueError('Tree is a cycle')
                trees.append(Node(ordered_id[i]))
    for i in range(len(ordered_id)):
        for j in trees:
            if i == j.node_id:
                parent = j
        for j in records:
            if j.parent_id == i:
                for k in trees:
                    if k.node_id == 0:
                        continue
                    if j.record_id == k.node_id:
                        child = k
                        parent.children.append(child)
    return trees[0]
