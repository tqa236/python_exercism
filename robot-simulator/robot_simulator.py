"""Simulate the movements of a robot."""

EAST = (1, 0)
NORTH = (0, 1)
WEST = (-1, 0)
SOUTH = (0, -1)
DIRECTION = [NORTH, EAST, SOUTH, WEST]


class Robot(object):
    """Simulate the movements of a robot."""

    def __init__(self, bearing: None = NORTH, x: int = 0, y: int = 0) -> None:
        """Initialize position and orientation."""
        self.bearing = bearing
        self.coordinates = (x, y)

    def turn_left(self):
        """Turn left."""
        self.bearing = DIRECTION[DIRECTION.index(self.bearing) - 1]

    def turn_right(self):
        """Turn right."""
        self.bearing = DIRECTION[DIRECTION.index(self.bearing) - 3]

    def advance(self):
        """Advance."""
        self.coordinates = tuple(
            [item1 + item2 for item1, item2 in zip(self.coordinates, self.bearing)]
        )

    def simulate(self, instructions):
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
