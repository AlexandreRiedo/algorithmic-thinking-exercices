from __future__ import annotations

TEST_CASES = 5


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


def tree_solve(tree: Node):
    num_streets = tree_streets(tree)
    height = tree_height(tree)
    min_num_streets = num_streets - height
    total_candy = tree_candy(tree)
    print(f"{min_num_streets} {total_candy}")


# NB: The Book's 1st attempt
# def read_tree(str_input: str) -> Node:
#     if str_input.startswith("("):
#         tree = Node(None, read_tree(str_input[1:]), read_tree(str_input[999]))
#         return tree


# My attempts at translating
def read_tree(str_input: str) -> Node:
    pos = [0]
    return read_tree_helper(str_input, pos)


def read_tree_helper(str_input: str, pos: list[int]) -> Node:  # type: ignore
    tree = Node(None, None, None)
    if str_input[pos[0]] == "(":
        pos[0] += 1
        tree.left = read_tree_helper(str_input, pos)
        pos[0] += 1
        tree.right = read_tree_helper(str_input, pos)
        pos[0] += 1
        return tree
    else:
        tree.left = None
        tree.right = None
        tree.candy = int(str_input[pos[0]])
        pos[0] += 1
        if (digit_char := str_input[pos[0]]).isdigit():
            tree.candy = tree.candy * 10 + int(digit_char)
            pos[0] += 1
        return tree


def main():
    for _ in range(TEST_CASES):
        str_input = input()
        tree = read_tree(str_input)
        tree_solve(tree)


if __name__ == "__main__":
    main()
