"""Detect palindrome products in a given range."""


def check_palindrom(number):
    """Check if a number is a palindrome or not."""
    return number == int(str(number)[::-1])


def find_factors(number, min_factor, max_factor):
    """Return a set of factors in a given range for a given number."""
    return set([(i, number//i) for i in range(min_factor, max_factor+1)
                if number % i == 0 and min_factor <= number//i <= max_factor
                and i <= number//i])


def check_valid(max_factor, min_factor):
    """Check the validity of the factor range."""
    if max_factor < min_factor:
        raise ValueError("Min factor must be smaller than max factor")


def find_palindrome(max_factor, min_factor, palindrome_type):
    """Find all palindromes."""
    check_valid(max_factor, min_factor)
    palindromes = [i*j for i in range(min_factor, max_factor + 1)
                   for j in range(i, max_factor + 1) if check_palindrom(i*j)]
    if palindrome_type == "min":
        number = min(palindromes)
    if palindrome_type == "max":
        number = max(palindromes)
    return [number, find_factors(number, min_factor, max_factor)]


def largest_palindrome(max_factor, min_factor):
    """Find the largest palindrome and its factors."""
    return find_palindrome(max_factor, min_factor, "max")


def smallest_palindrome(max_factor, min_factor):
    """Find the smallest palindrome and its factors."""
    return find_palindrome(max_factor, min_factor, "min")
