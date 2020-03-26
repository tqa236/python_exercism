"""Generate a list of primes based on the Sieve algorithm."""


from typing import List


def primes(limit: int) -> List[int]:
    """Generate a list of primes based on the Sieve algorithm."""
    all_primes = []
    numbers = range(2, limit + 1)
    while numbers:
        prime = numbers[0]
        all_primes.append(prime)
        numbers = [number for number in numbers if number % prime != 0]
    return all_primes
