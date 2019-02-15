"""Manage high scores of a game."""


class HighScores(object):
    """Manage high scores of a game."""

    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        """Return the latest score."""
        return self.scores[-1]

    def personal_best(self):
        """Return the best score."""
        return max(self.scores)

    def personal_top(self):
        """Return three best scores."""
        return sorted(self.scores, reverse=True)[:3]

    def report(self):
        """Auto-generate a report."""
        best_score = self.personal_best()
        latest_score = self.latest()
        if best_score == latest_score:
            return f"Your latest score was {latest_score}."\
                f" That's your personal best!"
        return f"Your latest score was {self.latest()}."\
            f" That's {best_score - latest_score} short of your personal best!"
