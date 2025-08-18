from __future__ import annotations
from typing import Generator, Optional


class BinarySearchTree:
    def __init__(self, data: int) -> None:
        self._data: int = data
        self._left: Optional[BinarySearchTree] = None
        self._right: Optional[BinarySearchTree] = None

    @property
    def data(self) -> int:
        return self._data

    @property
    def left(self) -> Optional[BinarySearchTree]:
        return self._left

    @property
    def right(self) -> Optional[BinarySearchTree]:
        return self._right

    def insert(self, value: int) -> None:
        if value <= self._data:
            if self._left is None:
                self._left = BinarySearchTree(value)
            else:
                self._left.insert(value)
        else:
            if self._right is None:
                self._right = BinarySearchTree(value)
            else:
                self._right.insert(value)

    def each(self) -> Generator[int, None, None]:
        """Percorre a árvore em ordem crescente (in-order traversal)."""
        if self._left:
            yield from self._left.each()
        yield self._data
        if self._right:
            yield from self._right.each()
