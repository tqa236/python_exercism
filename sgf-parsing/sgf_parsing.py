"""Build a class to parse SGF format."""
from typing import Dict, List, Optional, Tuple


class SgfTree(object):
    """Build a class to parse SGF format."""

    __hash__ = None

    def __init__(
        self,
        properties: Optional[Dict[str, List[str]]] = None,
        children: Optional[List["SgfTree"]] = None,
    ) -> None:
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other: "SgfTree") -> bool:
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other: "SgfTree") -> bool:
        return not self == other


def _parse_value(raw_value: str) -> str:
    """Decode an SGF property value according to the SGF text rules."""
    chars: List[str] = []
    index = 0
    while index < len(raw_value):
        char = raw_value[index]
        if char == "\\":
            if index + 1 >= len(raw_value):
                break
            next_char = raw_value[index + 1]
            if next_char == "\n":
                index += 2
                continue
            if next_char in " \t\r":
                chars.append(" ")
                index += 2
                continue
            chars.append(next_char)
            index += 2
            continue
        if char == "\t":
            chars.append(" ")
        elif char == "\r":
            chars.append(" ")
        elif char == "\n":
            chars.append("\n")
        else:
            chars.append(char)
        index += 1
    return "".join(chars)


def _find_closing_bracket(text: str, start: int) -> Optional[int]:
    """Return the index of the closing ] for an SGF value."""
    index = start
    while index < len(text):
        char = text[index]
        if char == "\\":
            index += 2
            continue
        if char == "]":
            return index
        index += 1
    return None


def _parse_node(text: str, index: int) -> Tuple[SgfTree, int]:
    """Parse a single SGF node starting at the semicolon."""
    if index >= len(text) or text[index] != ";":
        raise ValueError("tree missing")

    index += 1
    properties: Dict[str, List[str]] = {}
    while index < len(text):
        char = text[index]
        if char in ");":
            break
        if char == "(":
            break

        if char.isalpha():
            if not char.isupper():
                raise ValueError("property must be in uppercase")
            key_start = index
            index += 1
            while index < len(text) and text[index].isalpha() and text[index].isupper():
                index += 1
            if index < len(text) and text[index].isalpha() and not text[index].isupper():
                raise ValueError("property must be in uppercase")
            key = text[key_start:index]

            values: List[str] = []
            while index < len(text) and text[index] == "[":
                closing = _find_closing_bracket(text, index + 1)
                if closing is None:
                    raise ValueError("properties without delimiter")
                value = _parse_value(text[index + 1 : closing])
                values.append(value)
                index = closing + 1
            if not values:
                raise ValueError("properties without delimiter")
            if key in properties:
                properties[key].extend(values)
            else:
                properties[key] = values
            continue

        if char in "[]":
            raise ValueError("properties without delimiter")

        raise ValueError("tree missing")

    return SgfTree(properties), index


def _parse_tree(text: str, index: int) -> Tuple[SgfTree, int]:
    if index >= len(text) or text[index] != "(":
        raise ValueError("tree missing")

    index += 1
    if index >= len(text):
        raise ValueError("tree with no nodes")
    if text[index] == ")":
        raise ValueError("tree with no nodes")

    if text[index] != ";":
        raise ValueError("tree missing")

    tree, index = _parse_node(text, index)
    while index < len(text):
        if text[index] == ")":
            return tree, index + 1
        if text[index] == ";":
            child, index = _parse_node(text, index)
            tree.children.append(child)
            continue
        if text[index] == "(":
            child, index = _parse_tree(text, index)
            tree.children.append(child)
            continue
        raise ValueError("tree missing")

    raise ValueError("tree missing")


def parse(input_string: str) -> "SgfTree":
    """Build a function to parse SGF format."""
    if input_string is None:
        raise ValueError("tree missing")

    text = input_string.strip()
    if not text:
        raise ValueError("tree missing")
    if text == ";":
        raise ValueError("tree missing")
    if not text.startswith("("):
        raise ValueError("tree missing")

    tree, index = _parse_tree(text, 0)
    if index != len(text):
        raise ValueError("tree missing")
    return tree
