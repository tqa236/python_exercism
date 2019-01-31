# Score categories
# Change the values as you see fit


def YACHT(dice): return 50 if len(set(dice)) == 1 else 0


def ONES(dice): return dice.count(1) * 1


def TWOS(dice): return dice.count(2) * 2


def THREES(dice): return dice.count(3) * 3


def FOURS(dice): return dice.count(4) * 4


def FIVES(dice): return dice.count(5) * 5


def SIXES(dice): return dice.count(6) * 6


def FULL_HOUSE(dice): return sum(dice) if all([len(set(dice)) == 2, any(
    [dice.count(x) == 2 for x in dice]), any([dice.count(x) == 3
                                              for x in dice])]) else 0


def FOUR_OF_A_KIND(dice): return sum([x * 4 for x in set(dice)
                                      if dice.count(x) >= 4])


def LITTLE_STRAIGHT(dice): return 30\
    if set([1, 2, 3, 4, 5]) == set(sorted(dice)) else 0


def BIG_STRAIGHT(dice): return 30\
    if set([2, 3, 4, 5, 6]) == set(sorted(dice)) else 0


def CHOICE(dice): return sum(dice)


def score(dice, category):
    return category(dice)
