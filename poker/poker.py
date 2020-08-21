"""Find the best poker hands."""

from collections import Counter
from typing import List, Tuple

CARD_VALUE = {"J": 11, "Q": 12, "K": 13, "A": 1}
(
    HIGH_CARD,
    ONE_PAIR,
    TWO_PAIR,
    THREE_OF_A_KIND,
    STRAIGHT,
    FLUSH,
    FULL_HOUSE,
    FOUR_OF_A_KIND,
    STRAIGHT_FLUSH,
) = range(9)


def parse_hand(hand: str) -> Tuple[List[int], List[str]]:
    """Parse a hand into numbers and suits."""
    numbers = [
        int(card[:-1]) if card[:-1].isdigit() else CARD_VALUE[card[:-1]]
        for card in hand.split()
    ]
    suits = [card[-1] for card in hand.split()]
    return numbers, suits


def find_best_type(hand: str) -> int:
    """Find the best type of a hand."""
    numbers, suits = parse_hand(hand)
    numbers = sorted(numbers, reverse=True)
    counter = Counter(numbers)
    if len(counter) <= 4:
        most_common_cards = counter.most_common(4)
        numbers = [[card[0] for _ in range(card[1])] for card in most_common_cards]
        numbers = [card if card > 1 else 14 for sublist in numbers for card in sublist]
        most_common_quantities = [i[1] for i in most_common_cards]
        if most_common_quantities == [4, 1]:
            return (FOUR_OF_A_KIND, numbers)
        if most_common_quantities == [3, 2]:
            return (FULL_HOUSE, numbers)
        elif most_common_quantities == [3, 1, 1]:
            return (THREE_OF_A_KIND, numbers)
        elif most_common_quantities == [2, 2, 1]:
            return (TWO_PAIR, numbers)
        elif most_common_quantities == [2, 1, 1, 1]:
            return (ONE_PAIR, numbers)
    straight = numbers == list(range(numbers[0], numbers[0] - 5, -1))
    if 1 in numbers and not straight:
        numbers = [14] + numbers[:-1]
        straight = numbers == list(range(numbers[0], numbers[0] - 5, -1))
    flush = len(set(suits)) == 1
    if straight and flush:
        return (STRAIGHT_FLUSH, numbers)
    if straight:
        return (STRAIGHT, numbers)
    if flush:
        return (FLUSH, numbers)
    return (HIGH_CARD, numbers)


def best_hands(hands: List[str]) -> None:
    """Find all the best hands."""
    best_hand_types = [find_best_type(hand) for hand in hands]
    best_hand = [
        hand
        for index, hand in enumerate(hands)
        if best_hand_types[index]
        == max(enumerate(best_hand_types), key=lambda x: x[1])[1]
    ]
    return best_hand
