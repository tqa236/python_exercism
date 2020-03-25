"""Test if a number is valid or not."""


class Luhn(object):
    """A simple Luhn object."""

    def __init__(self, card_num):
        """Initialize."""
        self.card_num = card_num.replace(" ", "")

    def valid(self):
        """Test if the number is valid."""
        if not self.card_num.isdigit() or self.card_num == "0":
            return False

        card_num_rev = list(map(int, self.card_num))[::-1]
        points = sum(card_num_rev[::2]) + sum(
            2 * i - 9 * (i // 5) for i in card_num_rev[1::2]
        )
        return points % 10 == 0
