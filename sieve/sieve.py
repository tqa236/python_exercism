"""Generate a list of primes based on the Sieve algorithm."""


def sieve(limit):
    """Generate a list of primes based on the Sieve algorithm."""
    primes = []
    numbers = range(2, limit + 1)
    while numbers:
        prime = numbers[0]
        primes.append(prime)
        numbers = [number for number in numbers if number % prime != 0]
    return primes
