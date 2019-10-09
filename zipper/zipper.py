from typing import Dict, Union


class Zipper(object):
    @staticmethod
    def from_tree(
        tree: Dict[
            str,
            Union[
                int,
                Dict[str, Union[int, None, Dict[str, Union[int, None]]]],
                Dict[str, Union[int, None]],
            ],
        ]
    ) -> None:
        pass

    def value(self):
        pass

    def set_value(self):
        pass

    def left(self):
        pass

    def set_left(self):
        pass

    def right(self):
        pass

    def set_right(self):
        pass

    def up(self):
        pass

    def to_tree(self):
        pass
