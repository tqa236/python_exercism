from typing import Optional

# import random


def all_primes(start, end):
    return list(
        sorted(
            set(range(start, end + 1)).difference(
                set(
                    (p * f)
                    for p in range(2, int(end ** 0.5) + 2)
                    for f in range(2, (end // p) + 1)
                )
            )
        )
    )


def private_key(p: int) -> None:
    return 2
    # prime_list = all_primes(2, p - 1)
    # return random.choice(prime_list)


def public_key(p: int, g: int, private: Optional[int]) -> None:
    pass


def secret(p: int, public: Optional[int], private: Optional[int]) -> None:
    pass
