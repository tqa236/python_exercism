"""Build a tree of records."""


from typing import List, Optional


class Record():
    """Simple record class."""

    def __init__(self, record_id: int, parent_id: int) -> None:
        """Initialize."""
        self.record_id = record_id
        self.parent_id = parent_id


class Node():
    """Simple node class."""

    def __init__(self, node_id: int) -> None:
        """Initialize."""
        self.node_id = node_id
        self.children = []


def check_valid_record(record: Record) -> None:
    """Check valid record."""
    if record.record_id == 0 and record.parent_id != 0:
        raise ValueError('Root node cannot have a parent')
    elif record.record_id < record.parent_id:
        raise ValueError('Parent id must be lower than child id')
    elif record.record_id == record.parent_id and record.record_id != 0:
        raise ValueError('Tree is a cycle')


def BuildTree(records: List[Record]) -> Optional[Node]:
    """Build a tree of records."""
    records.sort(key=lambda x: x.record_id)
    if not records:
        return None
    if records[-1].record_id != len(records) - 1:
        raise ValueError('Tree must be continuous')
    if records[0].record_id != 0:
        raise ValueError('Tree must start with id 0')
    trees = []
    for record in records:
        check_valid_record(record)
        trees.append(Node(record.record_id))
        if record.record_id > 0:
            trees[record.parent_id].children.append(trees[record.record_id])
    return trees[0]
