from typing import List


def find_fewest_coins(coins: List[int], target: int) -> None:
    if target == 0:
        return []
    coins = sorted(coins)
    if target < coins[0]:
        raise ValueError("Cannot provide this amount.")
    if target in coins:
        return [target]
    if target > 0:
        return [0]
    return [target]
