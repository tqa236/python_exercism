"""Implement a simple class to detect allergens."""


class Allergies(object):
    """Implement a simple class to detect allergens."""

    def __init__(self, score):
        """Initialize variables."""
        self.score = score
        self.allergies = ['eggs', 'peanuts', 'shellfish', 'strawberries',
                          'tomatoes', 'chocolate', 'pollen', 'cats']

    def is_allergic_to(self, item):
        """Check if allergic to an allergen."""
        return item in self.lst

    @property
    def lst(self):
        """Return all allegens."""
        return [item for index, item in enumerate(self.allergies)
                if 2 ** index & self.score != 0]
