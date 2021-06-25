"""
This question was asked by Apple.

Given a binary tree, find a minimum path sum from root to a leaf.

For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.

  10
 /  \
5    5
 \     \
   2    1
       /
     -1
"""


class Node:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


def get_minimum_path_sum(root: Node) -> float:
    minimum_path_sum = float('inf')
    stack = [(root, 0)]
    while stack:
        node, current_sum = stack.pop()
        current_sum += node.val
        stack_addition = []
        if node.right is not None:
            stack_addition.append((node.right, current_sum))
        if node.left is not None:
            stack_addition.append((node.left, current_sum))
        if not stack_addition:
            minimum_path_sum = min(minimum_path_sum, current_sum)
        else:
            stack.extend(stack_addition)
    return minimum_path_sum


if __name__ == "__main__":
    tree = Node(10,
                left=Node(5,
                          right=Node(2)),
                right=Node(5,
                           right=Node(1,
                                      left=Node(-1))))
    print(get_minimum_path_sum(tree))  # ANS = 15
