NUM_TEST = 2


class Tree:
    def __init__(self, left, right) -> None:
        self.left: int | Tree | None = left
        self.right: int | Tree | None = right


def find_left_tree_end(str_tree):
    left_tree_end_index = 1
    parenthese_count = 1
    while parenthese_count != 0:
        left_tree_end_index += 1
        if str_tree[left_tree_end_index] == "(":
            parenthese_count += 1
        elif str_tree[left_tree_end_index] == ")":
            parenthese_count -= 1
    return left_tree_end_index


def find_right_tree_start(str_tree):
    right_tree_start_index = len(str_tree) - 2
    parenthese_count = 1
    while parenthese_count != 0:
        right_tree_start_index -= 1
        if str_tree[right_tree_start_index] == "(":
            parenthese_count -= 1
        elif str_tree[right_tree_start_index] == ")":
            parenthese_count += 1
    return right_tree_start_index


def parse_tree(parent_tree: Tree, str_tree: str):
    if str_tree[1] != "(":
        parent_tree.left = int(str_tree[1:3])
    else:
        parent_tree.left = Tree(None, None)
        parse_tree(parent_tree.left, str_tree[1 : find_left_tree_end(str_tree) + 1])

    if str_tree[-2] != ")":
        parent_tree.right = int(str_tree[-3:-1])
    else:
        parent_tree.right = Tree(None, None)
        parse_tree(parent_tree.right, str_tree[find_right_tree_start(str_tree) : - 1])


for _ in range(NUM_TEST):
    str_input = input()
    sum_candy = sum(
        int(digit)
        for digit in str_input.replace("(", "").replace(")", "").replace(" ", "")
    )


"""
((1 (2 3)) (10 12))
(2 ((4 6) (7 8)))

(1 (2 3))
"""
