from __future__ import annotations

from typing import Generic, TypeVar

T = TypeVar("T")


class Node:
    def __init__(self, candy: int | None, left: Node | None, right: Node | None):
        self.candy = candy
        self.left = left
        self.right = right


# Claude's Stack Implementation for Python
class Stack(Generic[T]):
    def __init__(self):
        self._values: list = []

    def push(self, item: T) -> None:
        self._values.append(item)

    def pop(self) -> T:
        if not self._values:
            raise IndexError("pop from empty stack")
        return self._values.pop()

    def peek(self) -> T:
        if not self._values:
            raise IndexError("peek at empty stack")
        return self._values[-1]

    def is_empty(self):
        return not self._values

    def __len__(self):
        return len(self._values)


def tree_candy(tree: Node | None) -> int:
    total: int = 0
    s: Stack[Node] = Stack()
    while tree:
        if tree.left and tree.right:
            s.push(tree.left)
            tree = tree.right
        else:
            total += tree.candy  # type: ignore[operator]
            tree = None if s.is_empty() else s.pop()
    return total
