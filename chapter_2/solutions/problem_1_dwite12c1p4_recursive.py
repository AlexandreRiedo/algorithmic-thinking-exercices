from __future__ import annotations


class Node:
    def __init__(self, candy: int | None, left: Node | None, right: Node | None):
        self.candy = candy
        self.left = left
        self.right = right


def tree_nodes(tree: Node) -> int:
    if tree.left is None and tree.right is None:
        return 1
    return 1 + tree_nodes(tree.left) + tree_nodes(tree.right)  # type: ignore


def tree_leaves(tree: Node) -> int:
    if tree.left is None and tree.right is None:
        return 1
    return tree_leaves(tree.left) + tree_leaves(tree.right)  # type: ignore
