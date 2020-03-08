class ConnectGame:
    def __init__(self, board: str) -> None:
        self.board = [line.split() for line in board.split("\n")]
        self.board_length = len(self.board)

    def get_winner(self) -> None:
        if "0" not in self.board[0] and "X" not in [line[0] for line in self.board]:
            return ""
        return ""

    def check_if_0_win(self):
        # for i in range(self.board_length):
        #     pieces = [
        #         j
        #         for j, value in enumerate(self.board[i])
        #         if value == "O" and self.board
        #     ]
        return True
