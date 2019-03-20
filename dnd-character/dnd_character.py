"""Implement a simple DnD character."""
from secrets import randbelow


class Character:
    """Implement a simple DnD character."""

    def __init__(self):
        """Initialize."""
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        """Generate ability point."""
        choice = [randbelow(5) + 1 for i in range(4)]
        return sum(choice) - min(choice)


def modifier(point):
    """Modify point."""
    return (point - 10) // 2
