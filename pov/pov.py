from json import dumps
from typing import Dict, List, Optional


class Tree(object):
    def __init__(self, label: str, children: Optional[List["Tree"]] = None) -> None:
        self.label = label
        self.children = children if children is not None else []

    def __dict__(self):
        return {self.label: [c.__dict__() for c in sorted(self.children)]}

    def __str__(self, indent: None = None) -> str:
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other: "Tree") -> bool:
        return self.label < other.label

    def __eq__(self, other):
        if other is None:
            return False
        return self.__dict__() == other.__dict__()

    def from_pov(self, from_node: str) -> "Tree":
        target = self._find_node(from_node)
        if target is None:
            raise ValueError("Tree could not be reoriented")

        path = self._root_path(from_node)
        if path is None:
            raise ValueError("Tree could not be reoriented")
        if len(path) == 1:
            return Tree(
                self.label,
                [Tree(child.label, child.children) for child in self.children],
            )

        parent_map = self._build_parent_map()
        new_parent = dict(parent_map)
        for index, node_label in enumerate(path[:-1]):
            new_parent[node_label] = path[index + 1]
        new_parent[path[-1]] = None

        return self._rebuild_from_parent_map(path[-1], new_parent)

    def path_to(self, from_node: str, to_node: str) -> List[str]:
        source_path = self._root_path(from_node)
        if source_path is None:
            raise ValueError("Tree could not be reoriented")

        target_path = self._root_path(to_node)
        if target_path is None:
            raise ValueError("No path found")

        if source_path == target_path:
            return source_path

        common_len = 0
        while (
            common_len < min(len(source_path), len(target_path))
            and source_path[common_len] == target_path[common_len]
        ):
            common_len += 1

        common_ancestor = source_path[common_len - 1] if common_len > 0 else None
        upward = []
        if common_ancestor is not None:
            source_index = source_path.index(common_ancestor)
            upward = source_path[source_index + 1 :][::-1]
            downward = target_path[target_path.index(common_ancestor) + 1 :]
            return upward + [common_ancestor] + downward
        return source_path[::-1] + target_path

    def _root_path(
        self,
        target: str,
        current: Optional["Tree"] = None,
        path: Optional[List[str]] = None,
    ) -> Optional[List[str]]:
        if current is None:
            current = self
        if path is None:
            path = []
        if current.label == target:
            return path + [current.label]
        for child in current.children:
            result = self._root_path(target, child, path + [current.label])
            if result is not None:
                return result
        return None

    def _find_node(
        self, target: str, current: Optional["Tree"] = None
    ) -> Optional["Tree"]:
        if current is None:
            current = self
        if current.label == target:
            return current
        for child in current.children:
            found = self._find_node(target, child)
            if found is not None:
                return found
        return None

    def _build_parent_map(
        self, current: Optional["Tree"] = None, parent: Optional[str] = None
    ) -> Dict[str, Optional[str]]:
        if current is None:
            current = self
        parent_map = {}
        if parent is not None:
            parent_map[current.label] = parent
        for child in current.children:
            parent_map.update(self._build_parent_map(child, current.label))
        return parent_map

    def _rebuild_from_parent_map(
        self, root_label: str, parent_map: Dict[str, Optional[str]]
    ) -> "Tree":
        root = Tree(root_label)
        for label, parent in parent_map.items():
            if label == root_label:
                continue
            if parent == root_label:
                root.children.append(self._rebuild_from_parent_map(label, parent_map))
        root.children.sort()
        return root
