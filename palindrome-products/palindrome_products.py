from typing import Union


def check_palindrom(number: int) -> bool:
    return number == int(str(number)[::-1])


def find_factors(number: int, min_factor: int, max_factor: int) -> set[tuple[int, int]]:
    return set(
        [
            (i, number // i)
            for i in range(min_factor, max_factor + 1)
            if number % i == 0
            and min_factor <= number // i <= max_factor
            and i <= number // i
        ],
    )


def check_valid(max_factor: int, min_factor: int) -> None:
    if max_factor < min_factor:
        raise ValueError("min must be <= max")


def find_palindrome(
    max_factor: int,
    min_factor: int,
    palindrome_type: str,
) -> list[Union[int, set[tuple[int, int]]]]:
    check_valid(max_factor, min_factor)
    palindromes = [
        i * j
        for i in range(min_factor, max_factor + 1)
        for j in range(i, max_factor + 1)
        if check_palindrom(i * j)
    ]
    if not palindromes:
        return None, []
    if palindrome_type == "min":
        number = min(palindromes)
    if palindrome_type == "max":
        number = max(palindromes)
    return [number, find_factors(number, min_factor, max_factor)]


def largest(max_factor: int, min_factor: int) -> list[Union[int, set[tuple[int, int]]]]:
    return find_palindrome(max_factor, min_factor, "max")


def smallest(
    max_factor: int,
    min_factor: int,
) -> list[Union[int, set[tuple[int, int]]]]:
    return find_palindrome(max_factor, min_factor, "min")
