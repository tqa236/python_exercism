"""A simple Clock class."""


class Clock(object):
    """A simple Clock class."""

    def __init__(self, hour: int, minute: int) -> None:
        """Initialize a Clock object with the correct hour and minute."""
        self.hour = (hour + minute // 60) % 24
        self.minute = minute % 60

    def __repr__(self) -> str:
        """Display time with format hh:mm."""
        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other: Clock) -> bool:
        """Compare time of two clocks."""
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes: int) -> Clock:
        """Add time of a clock."""
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes: int) -> Clock:
        """Substract time from a clock."""
        return Clock(self.hour, self.minute - minutes)
