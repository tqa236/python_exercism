"""Convert numbers in 2 bases."""
from typing import List


def rebase(input_base: int, digits: List[int], output_base: int) -> None:
    """Convert numbers in 2 bases."""
    if input_base <= 1 or output_base <= 1:
        raise ValueError("Base must be a integer bigger than 1.")
    if digits:
        if min(digits) < 0:
            raise ValueError("Negative digit is not allowed.")
        if max(digits) >= input_base:
            raise ValueError("Digit exists in input_base.")
    return dec2base(base2dec(input_base, digits), output_base)[::-1] or [0]


def base2dec(input_base: int, digits: List[int]) -> int:
    """Convert numbers to base 10."""
    if not digits:
        return 0
    return input_base * base2dec(input_base, digits[:-1]) + digits[-1]


def dec2base(number: int, output_base: int) -> List[int]:
    """Convert numbers from base 10 (reversed order)."""
    if not number:
        return []
    return [number % output_base] + dec2base(number // output_base, output_base)
