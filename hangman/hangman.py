STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word: str) -> None:
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.masked_word = "".join("_" for c in word)
        self.correct_guess = []

    def guess(self, char: str) -> None:
        if self.status != STATUS_ONGOING:
            raise ValueError("The game has already ended.")

        if char not in self.word or char in self.correct_guess:
            self.remaining_guesses = self.remaining_guesses - 1
            if self.remaining_guesses < 0:
                self.status = STATUS_LOSE
        else:
            self.correct_guess.append(char)
            self.masked_word = "".join(
                c if c in self.correct_guess else "_" for c in self.word
            )
            if "_" not in self.masked_word:
                self.status = STATUS_WIN

    def get_masked_word(self) -> str:
        return self.masked_word

    def get_status(self) -> str:
        return self.status
