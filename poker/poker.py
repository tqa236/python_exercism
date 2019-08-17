from typing import List, Tuple

CARD_VALUE = {"J": 11, "Q": 12, "K": 13, "A": 1}

HIGH_CARD, ONE_PAIR, TWO_PAIR, THREE_OF_A_KIND, STRAIGHT, FLUSH, FULL_HOUSE, FOUR_OF_A_KIND, STRAIGHT_FLUSH = range(
    9
)


def parse_hand(hand: str) -> Tuple[List[int], List[str]]:
    numbers = [
        int(card[0]) if card[0].isdigit() else CARD_VALUE[card[0]]
        for card in hand.split()
    ]
    suits = [card[1] for card in hand.split()]
    return numbers, suits


def find_best_type(hand: str) -> int:
    """Find the best type of a hand."""
    numbers, suits = parse_hand(hand)
    numbers = sorted(numbers)
    if len(set(suits)) == 1:
        return FLUSH
    return HIGH_CARD


def best_hands(hands: List[str]) -> None:
    best_hand_types = [find_best_type(hand) for hand in hands]
    best_hand = hands[max(enumerate(best_hand_types), key=lambda x: x[1])[0]]
    return [best_hand]
