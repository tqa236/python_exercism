"""Implement a basic reactive system."""


class InputCell(object):
    def __init__(self, initial_value):
        """Initialize."""
        self.value = initial_value

    def __add__(self, number):
        """Overload + operator."""
        return self.value + number

    def __mul__(self, number):
        """Overload + operator."""
        return self.value * number


class ComputeCell(object):
    def __init__(self, inputs, compute_function):
        """Initialize."""
        self.value = compute_function(inputs)

    def add_callback(self, callback):
        pass

    def remove_callback(self, callback):
        pass
