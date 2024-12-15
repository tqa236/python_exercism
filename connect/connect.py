class ConnectGame:
    def __init__(self, board: str) -> None:
        self.board = [line.strip().split() for line in board.strip().splitlines()]
        self.rows = len(self.board)
        self.cols = len(self.board[0])

    def get_winner(self) -> str:
        def dfs(player, x, y, visited):
            if (player == "O" and x == self.rows - 1) or (
                player == "X" and y == self.cols - 1
            ):
                return True

            visited.add((x, y))

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, -1)]:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < self.rows
                    and 0 <= ny < self.cols
                    and (nx, ny) not in visited
                    and self.board[nx][ny] == player
                ):
                    if dfs(player, nx, ny, visited):
                        return True

            return False

        for x in range(self.rows):
            if self.board[x][0] == "X":
                if dfs("X", x, 0, set()):
                    return "X"

        for y in range(self.cols):
            if self.board[0][y] == "O":
                if dfs("O", 0, y, set()):
                    return "O"

        return ""
