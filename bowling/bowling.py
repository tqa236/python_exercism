class BowlingGame(object):
    def __init__(self) -> None:
        self.score_ = 0
        self.last_score = 0
        self.frame_score = 0
        self.first_throw = True
        self.bonus_rate = 1
        self.bonus_countdown = 0
        self.frame = 0

    def roll(self, pins: int) -> None:
        if pins < 0:
            raise ValueError("Cannot score negative point.")
        if pins > 10:
            raise ValueError("Cannot score more than 10 points in a throw.")
        if self.first_throw:
            self.frame = self.frame + 1
        if self.frame > 10:
            if self.bonus_countdown == 0:
                raise IndexError("Game already finished.")
            self.bonus_rate = max(self.bonus_rate - 1, 1)
        self.frame_score = self.frame_score + pins
        if self.frame_score > 10:
            raise ValueError("Cannot score more than 10 points in a frame.")
        self.score_ = self.score_ + pins * self.bonus_rate
        self.bonus_countdown = max(self.bonus_countdown - 1, 0)
        if self.bonus_countdown == 0:
            self.bonus_rate = 1
        elif self.frame_score != 10:
            self.bonus_rate = 2
        if self.frame_score == 10:
            if self.frame <= 10:
                self.bonus_rate = 2 + self.bonus_countdown
                if not self.first_throw:
                    self.bonus_countdown = 1
                else:
                    self.bonus_countdown = 2
            self.first_throw = True
        else:
            self.first_throw = not self.first_throw
        if self.first_throw:
            self.frame_score = 0

    def score(self) -> None:
        if self.frame < 10 or self.bonus_countdown > 0:
            raise IndexError("Unfinished game.")
        return self.score_
