"""Generate public and private keys."""

import secrets


def private_key(p: int) -> int:
    return secrets.randbelow(p - 3) + 2


def public_key(p: int, g: int, private: int) -> int:
    return (g**private) % p


def secret(p: int, public: int, private: int) -> int:
    return (public**private) % p
