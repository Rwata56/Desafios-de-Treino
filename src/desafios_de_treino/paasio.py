from typing import BinaryIO, Tuple


class IOStats:
    def __init__(self) -> None:
        self.read_count: int = 0
        self.write_count: int = 0
        self.read_bytes: int = 0
        self.write_bytes: int = 0

    def stats(self) -> Tuple[int, int, int, int]:
        """Retorna (read_count, write_count, read_bytes, write_bytes)."""
        return (
            self.read_count,
            self.write_count,
            self.read_bytes,
            self.write_bytes,
        )


class StatsIOWrapper:
    def __init__(self, inner: BinaryIO) -> None:
        self.inner = inner
        self.stats = IOStats()

    def read(self, size: int = -1) -> bytes:
        data = self.inner.read(size)
        self.stats.read_count += 1
        self.stats.read_bytes += len(data)
        return data

    def write(self, data: bytes) -> int:
        written = self.inner.write(data)
        self.stats.write_count += 1
        self.stats.write_bytes += written
        return written

    def __enter__(self) -> "StatsIOWrapper":
        self.inner.__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.inner.__exit__(exc_type, exc_val, exc_tb)
