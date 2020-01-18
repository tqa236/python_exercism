# from bisect import bisect_right
from typing import List

MIN_LENGTH = None


def find_fewest_coins(coins: List[int], target: int) -> None:
    if target == 0:
        return []
    if target < min(coins):
        raise ValueError("Cannot provide this amount.")
    return find_fewest_coins_recursive(coins, target)


def find_fewest_coins_recursive(coins: List[int], target: int, coin_list=[]) -> None:
    if target == 0:
        return []
    if MIN_LENGTH and coin_list > MIN_LENGTH:
        return coin_list
    coins = [coin for coin in sorted(coins) if coin <= target]
    if not coins:
        raise ValueError("Cannot provide this amount.")
    # method1 = find_fewest_coins_recursive(
    #     coins, target - coins[-1], coin_list.append(coins[-1])
    # )
    return []


# def find_fewest_coins(coins: List[int], target: int) -> None:
#     flag1 = False
#     flag2 = False
#     if target < 0:
#         raise ValueError("Cannot provide this amount.")
#     if target == 0:
#         return
#     if not coins:
#         return []
#     if len(coins) == 1 and target % coins[0] != 0:
#         return []
#     coins = sorted(coins)
#     coins = coins[: bisect_right(coins, target)]
#     if not coins and target > 0:
#         raise ValueError("Cannot provide this amount.")
#     if target < 0:
#         return []
#     try:
#         method1 = find_fewest_coins(coins[:-1], target)
#     except ValueError:
#         flag1 = True
#     try:
#         method2 = find_fewest_coins(coins, target - coins[-1]) + [coins[-1]]
#     except ValueError:
#         flag2 = True
#     if flag1 and flag2:
#         raise ValueError("Cannot provide this amount.")
#     if ((not method1) or (-1) in method1) and ((not method2) or (-1) in method2):
#         raise ValueError("Cannot provide this amount.")
#     if not method1:
#         return method2
#     if not method2:
#         return method1
#     if len(method1) < len(method2):
#         return method1
#     return method2
