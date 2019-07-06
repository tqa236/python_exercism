"""Return a unique robot name."""
from secrets import choice
from string import ascii_uppercase, digits


class Robot(object):
    """Return a unique robot name."""

    def __init__(self) -> None:
        self.name = self.generate_name()
        self.used_name = [self.name]

    def reset(self) -> None:
        while self.name in self.used_name:
            self.name = self.generate_name()
        self.used_name.append(self.name)

    def generate_name(self) -> str:
        return "".join(
            [choice(ascii_uppercase) for i in range(2)]
            + [choice(digits) for i in range(3)]
        )
