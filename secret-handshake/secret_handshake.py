"""A secrete handshake decoder."""

from typing import List

ACTIONS = ["wink", "double blink", "close your eyes", "jump"]


def handshake(code: int) -> str:
    """Decode."""
    actions = [action for key, action in enumerate(ACTIONS) if code & 2 ** key > 0]
    if code >= 16:
        actions = actions[::-1]
    return actions


def secret_code(actions: List[str]) -> int:
    """Encode."""
    indices = [ACTIONS.index(action) for action in actions]
    if indices[0] <= indices[-1]:
        offset = 0
    else:
        offset = 16
    return offset + sum(2 ** index for index in indices)
