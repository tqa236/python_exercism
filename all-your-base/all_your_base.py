def rebase(input_base: int, digits: list[int], output_base: int) -> None:
    if input_base <= 1:
        raise ValueError("input base must be >= 2")
    if output_base <= 1:
        raise ValueError("output base must be >= 2")
    if digits:
        if min(digits) < 0 or max(digits) >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
    return dec2base(base2dec(input_base, digits), output_base)[::-1] or [0]


def base2dec(input_base: int, digits: list[int]) -> int:
    if not digits:
        return 0
    return input_base * base2dec(input_base, digits[:-1]) + digits[-1]


def dec2base(number: int, output_base: int) -> list[int]:
    if not number:
        return []
    return [number % output_base] + dec2base(number // output_base, output_base)
