class Record:
    def __init__(self, record_id: int, parent_id: int) -> None:
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id: int) -> None:
        self.node_id = node_id
        self.children = []


def check_valid_record(record: Record) -> None:
    if (
        record.record_id == 0
        and record.parent_id != 0
        or record.record_id < record.parent_id
    ):
        raise ValueError("Node parent_id should be smaller than it's record_id.")
    elif record.record_id == record.parent_id and record.record_id != 0:
        raise ValueError("Only root should have equal record and parent id.")


def BuildTree(records: list[Record]) -> Node | None:
    records.sort(key=lambda x: x.record_id)
    if not records:
        return None
    if records[-1].record_id != len(records) - 1:
        raise ValueError("Record id is invalid or out of order.")
    trees = []
    for record in records:
        check_valid_record(record)
        trees.append(Node(record.record_id))
        if record.record_id > 0:
            trees[record.parent_id].children.append(trees[record.record_id])
    return trees[0]
