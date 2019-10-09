from typing import List


class Point(object):
    def __init__(self, x: int, y: int) -> None:
        self.x = None
        self.y = None

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WordSearch(object):
    def __init__(self, puzzle: List[str]) -> None:
        pass

    def search(self, word: str) -> None:
        pass
