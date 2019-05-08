"""Test if a number is valid or not."""
from itertools import islice


class Luhn(object):
    """A simple Luhn object."""

    def __init__(self, card_num):
        """Initialize."""
        card_num = card_num.replace(" ", "")
        self.card_num = [int(digit)
                         for digit in card_num[::-1]]\
            if card_num.isdigit() else [0]

    def is_valid(self):
        """Test if the number is valid."""
        if self.card_num == [0]:
            return False
        return (sum(self.card_num) + sum(i - 9 * (i // 5)
                                         for i in islice(self.card_num, 1,
                                                         None, 2))) % 10 == 0
