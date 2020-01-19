class Zipper(object):
    def __init__(self, value, left, right):
        self._value = value
        if left is None:
            self._left = left
        else:
            print("left", left)
            self._left = Zipper(left["value"], left["left"], left["right"])
        if right is None:
            self._right = right
        else:
            print("right", right)
            self._right = Zipper(right["value"], right["left"], right["right"])
        print("tree", self.to_tree())

    @staticmethod
    def from_tree(tree):
        print(tree)
        print(tree["value"])
        return Zipper(tree["value"], tree["left"], tree["right"])

    def value(self):
        return self._value

    def set_value(self):
        pass

    def left(self):
        return self._left

    def set_left(self):
        pass

    def right(self):
        return self._right

    def set_right(self):
        pass

    def up(self):
        pass

    def to_tree(self):
        left = None
        right = None
        if self._left is not None:
            left = self._left.to_tree()
        if self._right is not None:
            right = self._right.to_tree()
        return {"value": self._value, "left": left, "right": right}
