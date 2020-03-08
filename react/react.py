"""Implement a basic reactive system."""


class InputCell(object):
    def __init__(self, initial_value: int) -> None:
        """Initialize."""
        self._value = initial_value
        self.observers = []
        self.updated = True

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        for observer in self.observers:
            observer.updated = False
        for observer in self.observers:
            observer.update_value()

    def register_observer(self, observer) -> None:
        """Bind to the callback to update automatically."""
        self.observers.append(observer)


class ComputeCell(InputCell):
    """Compute and update values for all cells."""

    def __init__(self, inputs, compute_function):
        """Initialize."""
        super().__init__(None)
        self.inputs = inputs
        self.compute_function = compute_function
        for cell in self.inputs:
            cell.register_observer(self)
        self.value = compute_function([input.value for input in self.inputs])
        self.callbacks = []

    def update_value(self) -> None:
        """Update new value when there's a change."""
        if all([input.updated for input in self.inputs]):
            self.updated = True
            old_value = self.value
            self.value = self.compute_function([input.value for input in self.inputs])
            for observer in self.observers:
                observer.update_value()
            if old_value != self.value:
                for callback in self.callbacks:
                    callback(self.value)

    def add_callback(self, callback) -> None:
        """Add new callback."""
        self.callbacks.append(callback)

    def remove_callback(self, callback) -> None:
        """Remove a callback."""
        if callback in self.callbacks:
            self.callbacks.remove(callback)
