class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def scores(self):
        return self.scores

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        return max(self.scores)

    def personal_top(self):
        return sorted(self.scores, reverse=True)[:3]

    def report(self):
        best_score = self.personal_best()
        latest_score = self.latest()
        if best_score == latest_score:
            return f"Your latest score was {latest_score}."\
                f" That's your personal best!"
        return f"Your latest score was {self.latest()}."\
            f" That's {best_score - latest_score} short of your personal best!"
