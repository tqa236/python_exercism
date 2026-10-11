"""Provide metered file and socket wrappers to report I/O statistics."""

import io
from typing import Any, Iterator


class MeteredFile(io.BufferedRandom):
    """Implement a metered file wrapper using a subclassing model."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize MeteredFile and its I/O counters."""
        super().__init__(*args, **kwargs)
        self._read_bytes = 0
        self._read_ops = 0
        self._write_bytes = 0
        self._write_ops = 0

    def __enter__(self) -> "MeteredFile":
        """Enter the runtime context for the file."""
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """Exit the runtime context and close the file."""
        return super().__exit__(exc_type, exc_val, exc_tb)

    def __iter__(self) -> Iterator[bytes]:
        """Return self as an iterator."""
        return self

    def __next__(self) -> bytes:
        """Read and return the next line, updating read statistics."""
        line = super().readline()
        if not line:
            raise StopIteration
        self._read_bytes += len(line)
        self._read_ops += 1
        return line

    def read(self, size: int | None = -1) -> bytes:
        """Read and return up to size bytes, updating read statistics."""
        data = super().read(size)
        self._read_bytes += len(data)
        self._read_ops += 1
        return data

    @property
    def read_bytes(self) -> int:
        """Total number of bytes read."""
        return self._read_bytes

    @property
    def read_ops(self) -> int:
        """Total number of read operations."""
        return self._read_ops

    def write(self, b: bytes | bytearray) -> int:
        """Write the given bytes-like object and update write statistics."""
        n = super().write(b)
        self._write_bytes += n
        self._write_ops += 1
        return n

    @property
    def write_bytes(self) -> int:
        """Total number of bytes written."""
        return self._write_bytes

    @property
    def write_ops(self) -> int:
        """Total number of write operations."""
        return self._write_ops


class MeteredSocket:
    """Implement a metered socket wrapper using a delegation model."""

    def __init__(self, socket: Any) -> None:
        """Initialize MeteredSocket with the underlying socket and I/O counters."""
        self._socket = socket
        self._recv_bytes = 0
        self._recv_ops = 0
        self._send_bytes = 0
        self._send_ops = 0

    def __enter__(self) -> "MeteredSocket":
        """Enter the runtime context for the socket."""
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """Exit the runtime context and close the underlying socket."""
        return self._socket.__exit__(exc_type, exc_val, exc_tb)

    def recv(self, bufsize: int, flags: int = 0) -> bytes:
        """Receive up to bufsize bytes from the socket, updating receive statistics."""
        data = self._socket.recv(bufsize, flags)
        self._recv_bytes += len(data)
        self._recv_ops += 1
        return data

    @property
    def recv_bytes(self) -> int:
        """Total number of bytes received."""
        return self._recv_bytes

    @property
    def recv_ops(self) -> int:
        """Total number of receive operations."""
        return self._recv_ops

    def send(self, data: bytes, flags: int = 0) -> int:
        """Send data to the socket, updating send statistics."""
        n = self._socket.send(data, flags)
        self._send_bytes += n
        self._send_ops += 1
        return n

    @property
    def send_bytes(self) -> int:
        """Total number of bytes sent."""
        return self._send_bytes

    @property
    def send_ops(self) -> int:
        """Total number of send operations."""
        return self._send_ops
