from __future__ import annotations


class Node:
    def __init__(self, candy: int | None, left: Node | None, right: Node | None):
        self.candy = candy
        self.left = left
        self.right = right


def tree_candy(tree: Node) -> int:
    if tree.left is None and tree.right is None:
        return tree.candy  # type: ignore
    return tree_candy(tree.left) + tree_candy(tree.right)  # type: ignore


# Bonus: Calculates the number of nodes
def tree_nodes(tree: Node) -> int:
    if tree.left is None and tree.right is None:
        return 1
    return 1 + tree_nodes(tree.left) + tree_nodes(tree.right)  # type: ignore


# Bonus: Calculates the number of leaves
def tree_leaves(tree: Node) -> int:
    if tree.left is None and tree.right is None:
        return 1
    return tree_leaves(tree.left) + tree_leaves(tree.right)  # type: ignore


def tree_streets(tree: Node) -> int:
    if tree.left is None and tree.right is None:
        return 0
    return tree_streets(tree.left) + tree_streets(tree.right) + 4  # type: ignore


def tree_height(tree: Node) -> int:
    if tree.left is None and tree.right is None:
        return 0
    return 1 + max(tree_height(tree.left), tree_height(tree.right))  # type: ignore


def solve(tree: Node):
    num_streets = tree_streets(tree)
    height = tree_height(tree)
    min_num_streets = num_streets - height
    total_candy = tree_candy(tree)
    print(f"{min_num_streets} {total_candy}")
