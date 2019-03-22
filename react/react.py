"""Implement a basic reactive system."""


class InputCell(object):
    def __init__(self, initial_value):
        """Initialize."""
        self._value = initial_value
        self.observers = []
        # print(f"cell value is {self._value}")

    def __add__(self, number):
        """Overload + operator."""
        return self.value + number

    def __sub__(self, number):
        """Overload - operator."""
        return self.value - number

    def __mul__(self, number):
        """Overload + operator."""
        return self.value * number

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        for observer in self.observers:
            observer.update_value()

    def register_observer(self, observer):
        """Bind to the callback to update automatically."""
        self.observers.append(observer)

    # def notify_observers(self):
    #     for observer in self.observers:
    #         observer.notify(self)


class ComputeCell(object):
    """Compute and update values for all cells."""

    def __init__(self, inputs, compute_function):
        """Initialize."""
        self.inputs = inputs
        self.compute_function = compute_function
        for i in self.inputs:
            i.register_observer(self)
        self.value = compute_function(inputs)
        # print(self.inputs[0].observers[0].value)
        self.callbacks = []

    def update_value(self):
        """Update new value when there's a change."""
        self.value = self.compute_function(self.inputs)

    def add_callback(self, callback):
        """Add new callback."""
        self.callbacks.append(callback)

    def remove_callback(self, callback):
        """Remove a callback."""
        if callback in self.callbacks:
            self.callbacks.remove(callback)
