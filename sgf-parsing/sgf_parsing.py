"""Build a class to parse SGF format."""
import re
import string
from typing import Dict, List, Optional


class SgfTree(object):
    """Build a class to parse SGF format."""

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


def parse(input_string: str) -> "SgfTree":
    """Build a function to parse SGF format."""
    input_string = input_string.replace("\\", "").replace("\t", " ")
    if input_string == "()":
        raise ValueError("tree missing")
    regex = r"\(?\;?(?P<keys>[A-Z]+)?(?:\[(?P<values>(.|\s)+?\]?)\])"
    matches = re.finditer(regex, input_string, re.MULTILINE)
    if input_string == "(;)":
        return SgfTree()
    if re.match(regex, input_string) is None:
        raise ValueError("tree missing")
    properties, children, last_key, level = {}, [], "", 0
    for _, match in enumerate(matches, start=1):
        full = match.group()
        key = match.group("keys")
        value = match.group("values")
        if "(;" in full or ";" in full:
            if not key and not last_key or not value:
                raise ValueError("tree missing")
            if key not in string.ascii_uppercase:
                raise ValueError("property must be in uppercase")
            level += 1
        if level == 1:
            if not key and last_key:
                properties[last_key].append(value)
            else:
                if key in properties:
                    properties[key].append(value)
                else:
                    properties[key] = [value]
        if level >= 2:
            children.append(SgfTree({key: [value]}))
        if key:
            last_key = key
    return SgfTree(properties, children)
