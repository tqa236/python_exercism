import re
from typing import List, Optional


class Point(object):
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WordSearch(object):
    def __init__(self, puzzle: List[str]) -> None:
        self.puzzle = puzzle

    def search(self, word: str) -> Optional[List[Point]]:
        result = [
            (position.start(), index)
            for index, row in enumerate(self.puzzle)
            for position in re.finditer(word, row)
        ]
        if not result:
            return None
        print(result)
        print([Point(point[0], point[1]) for point in result])
        return [Point(x, y) for x, y in result]
