class BufferFullException(BufferError):
    def __init__(self, message):
        self.message = message


class BufferEmptyException(BufferError):
    def __init__(self, message):
        self.message = message


class CircularBuffer:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.content = []

    def read(self) -> str:
        if not self.content:
            raise BufferEmptyException("Circular buffer is empty")
        return self.content.pop(0)

    def write(self, data: str) -> None:
        if len(self.content) == self.capacity:
            raise BufferFullException("Circular buffer is full")
        self.content.append(data)

    def overwrite(self, data: str) -> None:
        if len(self.content) == self.capacity:
            self.content.pop(0)
        self.write(data)

    def clear(self) -> None:
        self.content = []
