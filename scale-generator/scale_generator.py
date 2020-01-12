from typing import List


class Scale(object):
    def __init__(self, tonic: str) -> None:
        self.tonic = tonic
        self.chromatic_ = self.make_chromatic()

    def chromatic(self) -> None:
        return self.chromatic_

    def interval(self, intervals: str) -> None:
        pass

    def make_chromatic(self) -> List[str]:
        base_chromatic = [
            "A",
            "A#",
            "B",
            "C",
            "C#",
            "D",
            "D#",
            "E",
            "F",
            "F#",
            "G",
            "G#",
        ]
        index = base_chromatic.index(self.tonic)
        return base_chromatic[index:] + base_chromatic[:index]
