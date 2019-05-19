"""Extract relevant scores by some criterio."""


def latest(scores):
    """Extract the latest score."""
    return scores[-1]


def personal_best(scores):
    """Extract the best score."""
    return max(scores)


def personal_top_three(scores):
    """Extract the top three best scores."""
    return sorted(scores, reverse=True)[:3]
