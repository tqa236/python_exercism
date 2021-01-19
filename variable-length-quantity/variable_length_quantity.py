"""
Variable Length Quantity encoder and decoder.

Source: https://exercism.io/tracks/python/exercises/variable-length-quantity/solutions/2b148713ca514f599cc43ef8ed32fc6f

"""
from collections import deque
from typing import Deque, List

MASK_SEVEN_BITS = 0b01111111
MASK_SERIES_BIT = 0b10000000


def encode(numbers: List[int]) -> List[int]:
    """Encode the list of numbers with VLQ."""
    result: List[int] = []
    encoded: Deque[int] = deque()
    for number in numbers:
        # get the rightmost 7 bits, unsetting the series bit
        encoded.appendleft(number & MASK_SEVEN_BITS)
        # shift right 7  bits
        number >>= 7
        # while anything remains, keep processing in 7 bit chunks
        while number:
            # get the first seven bits and set the series bit
            encoded.appendleft(number & MASK_SEVEN_BITS | MASK_SERIES_BIT)
            number >>= 7
        # add the bytes to the result
        result.extend(encoded)
        encoded.clear()
    return result


def decode(encoded: List[int]) -> List[int]:
    """Decode a list of VLQ-encoded numbers."""
    if encoded[-1] & MASK_SERIES_BIT:
        raise ValueError("Byte sequence terminator missing!")
    result: List[int] = []
    number = 0  # running total for an individual number
    for byte in encoded:
        # add the significant bits to the running total
        number <<= 7
        number += byte & MASK_SEVEN_BITS
        # if the series bit is 0, we've reached the end of the series
        if not byte & MASK_SERIES_BIT:
            result.append(number)
            number = 0
    return result
