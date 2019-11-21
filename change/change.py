from bisect import bisect_right
from typing import List

# import pdb

# pdb.set_trace()


def find_fewest_coins(coins: List[int], target: int) -> None:
    flag1 = False
    flag2 = False
    print(coins, target)
    if target < 0:
        raise ValueError("Cannot provide this amount.")
    if not coins:
        return []
    if target == 0:
        return []
    if target and not coins:
        return []
    if len(coins) == 1 and target % coins[0] != 0:
        return []
    coins = sorted(coins)
    coins = coins[: bisect_right(coins, target)]
    print("After:", coins, target)
    if not coins and target > 0:
        print("Huh")
        raise ValueError("Cannot provide this amount.")
    if target < 0:
        return []
    print("Why")
    try:
        method1 = find_fewest_coins(coins[:-1], target)
    except ValueError:
        flag1 = True
    print("Because")
    try:
        method2 = find_fewest_coins(coins, target - coins[-1]) + [coins[-1]]
    except ValueError:
        flag2 = True
    # print(method1, method2)
    if flag1 and flag2:
        raise ValueError("Cannot provide this amount.")
    if ((not method1) or (-1) in method1) and ((not method2) or (-1) in method2):
        raise ValueError("Cannot provide this amount.")
    if not method1:
        return method2
    if not method2:
        return method1
    if len(method1) < len(method2):
        return method1
    return method2
