"""Check if a string has correct bracket order or not."""

import re


def is_paired(input_string: str) -> bool:
    """Check if a string has correct bracket order or not."""
    stack = []
    brackets = re.sub(r"[^\(\)\[\]\{\}]", "", input_string)
    bracket_pairs = {"{": "}", "(": ")", "[": "]"}
    for i in brackets:
        if i in bracket_pairs:
            stack.append(bracket_pairs[i])
        elif not stack:
            return False
        elif i == stack[-1]:
            stack.pop()
        else:
            return False
    return not stack
