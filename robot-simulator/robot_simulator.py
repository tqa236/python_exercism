"""Simulate the movements of a robot."""

EAST = (1, 0)
NORTH = (0, 1)
WEST = (-1, 0)
SOUTH = (0, -1)
DIRECTION = [NORTH, EAST, SOUTH, WEST]


class Robot(object):
    """Simulate the movements of a robot."""

    def __init__(self, direction: None = NORTH, x: int = 0, y: int = 0) -> None:
        """Initialize position and orientation."""
        self.direction = direction
        self.coordinates = (x, y)

    def turn_left(self) -> None:
        """Turn left."""
        self.direction = DIRECTION[DIRECTION.index(self.direction) - 1]

    def turn_right(self) -> None:
        """Turn right."""
        self.direction = DIRECTION[DIRECTION.index(self.direction) - 3]

    def advance(self) -> None:
        """Advance."""
        self.coordinates = tuple(
            [item1 + item2 for item1, item2 in zip(self.coordinates, self.direction)]
        )

    def move(self, instructions: str) -> None:
        """Simulate a chain of command."""
        for instruction in instructions:
            if instruction == "L":
                self.turn_left()
            elif instruction == "R":
                self.turn_right()
            elif instruction == "A":
                self.advance()
            else:
                raise ValueError("Unknown command.")
