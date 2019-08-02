"""Implement a basic reactive system."""


from functools import partial
from typing import Callable, List, Union


class InputCell(object):
    def __init__(self, initial_value: int) -> None:
        """Initialize."""
        self._value = initial_value
        self.observers = []
        # print(f"cell value is {self._value}")

    def __add__(self, number: int) -> int:
        """Overload + operator."""
        return self.value + number

    def __sub__(self, number: int) -> int:
        """Overload - operator."""
        return self.value - number

    def __mul__(self, number: int) -> int:
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

    def register_observer(self, observer: "ComputeCell") -> None:
        """Bind to the callback to update automatically."""
        self.observers.append(observer)

    # def notify_observers(self):
    #     for observer in self.observers:
    #         observer.notify(self)


class ComputeCell(object):
    """Compute and update values for all cells."""

    def __init__(
        self,
        inputs: Union[List[InputCell], List["ComputeCell"]],
        compute_function: Callable,
    ) -> None:
        """Initialize."""
        self.inputs = inputs
        self.compute_function = compute_function
        for i in self.inputs:
            i.register_observer(self)
        self.value = compute_function(inputs)
        # print(self.inputs[0].observers[0].value)
        self.callbacks = []

    def update_value(self) -> None:
        """Update new value when there's a change."""
        self.value = self.compute_function(self.inputs)

    def add_callback(self, callback: partial) -> None:
        """Add new callback."""
        self.callbacks.append(callback)

    def remove_callback(self, callback: partial) -> None:
        """Remove a callback."""
        if callback in self.callbacks:
            self.callbacks.remove(callback)
