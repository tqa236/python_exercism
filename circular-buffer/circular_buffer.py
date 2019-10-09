"""A simple circular buffer."""


class CircularBuffer(object):
    """A simple circular buffer."""

    def __init__(self, capacity):
        """Initialize."""
        self.capacity = capacity
        self.content = []

    def read(self):
        """Return the oldest element of the circular buffer and remove it."""
        if not self.content:
            raise ValueError("The buffer is empty.")
        return self.content.pop(0)

    def write(self, data):
        """Add to the circular buffer."""
        if len(self.content) == self.capacity:
            raise BaseException("The buffer is full.")
        self.content.append(data)

    def overwrite(self, data):
        """Overwrite the oldest element if the buffer is full."""
        if len(self.content) == self.capacity:
            self.content.pop(0)
        self.write(data)

    def clear(self):
        """Clear the circular buffer."""
        self.content = []
