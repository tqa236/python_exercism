from typing import List, Optional, Tuple


def can_chain(dominoes: List[Tuple[int, int]]) -> Optional[List[Tuple[int, int]]]:
    if not dominoes:
        return []

    dominoes = [tuple(sorted(d)) for d in dominoes]

    # A valid closed chain must use every domino exactly once.
    def backtrack(
        path: List[Tuple[int, int]], remaining: List[Tuple[int, int]]
    ) -> Optional[List[Tuple[int, int]]]:
        if not remaining:
            return path if path[0][0] == path[-1][1] else None

        current_end = path[-1][1]
        for i, domino in enumerate(remaining):
            left, right = domino
            if left == current_end:
                next_path = path + [domino]
                result = backtrack(next_path, remaining[:i] + remaining[i + 1 :])
                if result is not None:
                    return result
            elif right == current_end:
                next_path = path + [(right, left)]
                result = backtrack(next_path, remaining[:i] + remaining[i + 1 :])
                if result is not None:
                    return result
        return None

    for i, domino in enumerate(dominoes):
        left, right = domino
        for orientation in [(left, right), (right, left)]:
            result = backtrack([orientation], dominoes[:i] + dominoes[i + 1 :])
            if result is not None:
                return result

    return None
