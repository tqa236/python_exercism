"""A secret handshake decoder."""

ACTIONS = ["wink", "double blink", "close your eyes", "jump"]


def commands(code: str) -> str:
    """Decode."""
    actions = [
        action for key, action in enumerate(ACTIONS) if int(code, 2) & 2**key > 0
    ]
    if code >= "10000":
        actions = actions[::-1]
    return actions
