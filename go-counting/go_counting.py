from collections import deque
from typing import Deque, Dict, List, Set, Tuple

WHITE = "W"
BLACK = "B"
NONE = ""


class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board: List[str]) -> None:
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0]) if self.rows else 0

    def _is_valid_coordinate(self, x: int, y: int) -> bool:
        return 0 <= x < self.cols and 0 <= y < self.rows

    def _neighbor_positions(self, x: int, y: int):
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if self._is_valid_coordinate(nx, ny):
                yield nx, ny

    def _component(self, start_x: int, start_y: int) -> Set[Tuple[int, int]]:
        queue: Deque[Tuple[int, int]] = deque([(start_x, start_y)])
        seen = {(start_x, start_y)}
        while queue:
            x, y = queue.popleft()
            for nx, ny in self._neighbor_positions(x, y):
                if (nx, ny) not in seen and self.board[ny][nx] == " ":
                    seen.add((nx, ny))
                    queue.append((nx, ny))
        return seen

    def _owner_of_component(self, component: Set[Tuple[int, int]]) -> str:
        touches_black = False
        touches_white = False
        for x, y in component:
            for nx, ny in self._neighbor_positions(x, y):
                stone = self.board[ny][nx]
                if stone == BLACK:
                    touches_black = True
                elif stone == WHITE:
                    touches_white = True
        if touches_black and not touches_white:
            return BLACK
        if touches_white and not touches_black:
            return WHITE
        return NONE

    def territory(self, x: int, y: int) -> Tuple[str, Set[Tuple[int, int]]]:
        """Find the owner and the territories given a coordinate on
           the board

        Args:
            x (int): Column on the board
            y (int): Row on the board

        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.
        """
        if not self._is_valid_coordinate(x, y):
            raise ValueError("Invalid coordinate")

        if self.board[y][x] in (BLACK, WHITE):
            return NONE, set()

        component = self._component(x, y)
        return self._owner_of_component(component), component

    def territories(self) -> Dict[str, Set[Tuple[int, int]]]:
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        territories: Dict[str, Set[Tuple[int, int]]] = {
            BLACK: set(),
            WHITE: set(),
            NONE: set(),
        }
        visited: Set[Tuple[int, int]] = set()

        for y in range(self.rows):
            for x in range(self.cols):
                if self.board[y][x] == " " and (x, y) not in visited:
                    component = self._component(x, y)
                    owner = self._owner_of_component(component)
                    territories[owner].update(component)
                    visited.update(component)

        return territories
