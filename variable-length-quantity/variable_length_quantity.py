from collections import deque
from typing import Deque

MASK_SEVEN_BITS = 0b01111111
MASK_SERIES_BIT = 0b10000000


def encode(numbers: list[int]) -> list[int]:
    result: list[int] = []
    encoded: Deque[int] = deque()
    for number in numbers:
        encoded.appendleft(number & MASK_SEVEN_BITS)
        number >>= 7
        while number:
            encoded.appendleft(number & MASK_SEVEN_BITS | MASK_SERIES_BIT)
            number >>= 7
        result.extend(encoded)
        encoded.clear()
    return result


def decode(encoded: list[int]) -> list[int]:
    if encoded[-1] & MASK_SERIES_BIT:
        raise ValueError("incomplete sequence")
    result: list[int] = []
    number = 0
    for byte in encoded:
        number <<= 7
        number += byte & MASK_SEVEN_BITS
        if not byte & MASK_SERIES_BIT:
            result.append(number)
            number = 0
    return result
