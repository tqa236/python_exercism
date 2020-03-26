"""Find the fewest number of coins for a given price."""
from typing import List, Optional


def find_fewest_coins(coins: List[int], target: int) -> None:
    """Find the fewest number of coins for a given price."""
    if target == 0:
        return []
    target_coin_list = find_fewest_coins_recursive(sorted(coins, reverse=True), target)
    if not target_coin_list:
        raise ValueError("Cannot provide this amount.")
    return sorted(target_coin_list)


def find_fewest_coins_recursive(
    coins: List[int], target: int, coin_list: Optional[List[int]] = None
) -> None:
    """Find the fewest number of coins for a given price recursively."""
    coins = [coin for coin in coins if coin <= target]
    if not coins:
        return []
    if coin_list is None:
        coin_list = []
    if target % coins[0] == 0:
        return coin_list + [coins[0]] * (target // coins[0])
    best_coin_list = []
    min_length = target // min(coins) + len(coin_list) + 1
    for coin in coins:
        if len(coin_list) + target // coin < min_length:
            target_coin_list = find_fewest_coins_recursive(
                coins, target - coin, coin_list + [coin]
            )
            if target_coin_list and len(target_coin_list) < min_length:
                min_length = len(target_coin_list)
                best_coin_list = target_coin_list
    return best_coin_list
