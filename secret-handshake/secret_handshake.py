"""A secrete handshake decoder."""

ACTIONS = ['wink', 'double blink', 'close your eyes', 'jump']


def handshake(code: int) -> str:
    """Decode."""
    return ACTIONS[code & 31]


def secret_code(actions):
    """Encode."""
    return 0
