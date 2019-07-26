"""Decide if 2 queens can attack each other."""


class Queen(object):
    """A simple queen object."""

    def __init__(self, row: int, column: int) -> None:
        """Initialize the position of the queen."""
        if min(row, column) >= 0 and max(row, column) < 8:
            self.row = row
            self.column = column
        else:
            raise ValueError("Unexpected Exception")

    def can_attack(self, another_queen: Queen) -> bool:
        """Decide if this queen can attack another queen."""
        if (self.row, self.column) == (another_queen.row, another_queen.column):
            raise ValueError("Unexpected Exception")
        if self.row == another_queen.row or self.column == another_queen.column:
            return True
        if self.row + self.column == another_queen.row + another_queen.column:
            return True
        if abs(self.row - self.column) == abs(another_queen.row - another_queen.column):
            return True
        return False
