"""A secret handshake decoder."""

ACTIONS = ["wink", "double blink", "close your eyes", "jump"]


def commands(code: int) -> str:
    """Decode."""
    actions = [action for key, action in enumerate(ACTIONS) if code & 2 ** key > 0]
    if code >= 16:
        actions = actions[::-1]
    return actions
