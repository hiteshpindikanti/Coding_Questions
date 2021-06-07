"""
This problem was asked by Facebook.

Given a binary tree, return the level of the tree with minimum sum.
"""
from queue import Queue


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_min_sum_tree_level(root: Node) -> int:
    queue = Queue()
    queue.put([root])
    level_sum_list = []
    current_level = -1
    while not queue.empty():
        current_level += 1
        nodes_list = queue.get()
        current_level_sum = 0
        next_level_nodes_list = []
        for node in nodes_list:
            current_level_sum += node.val
            if node.left is not None:
                next_level_nodes_list.append(node.left)
            if node.right is not None:
                next_level_nodes_list.append(node.right)
        level_sum_list.append((current_level_sum, current_level))
        if next_level_nodes_list:
            queue.put(next_level_nodes_list)

    return min(level_sum_list)[1]


if __name__ == "__main__":
    #        10
    #      /    \
    #    2       3
    #  /   \
    # 4     5
    #        \
    #         4

    tree = Node(10,
                left=Node(2,
                          left=Node(4),
                          right=Node(5,
                                     right=Node(4))),
                right=Node(3))

    print(get_min_sum_tree_level(tree))  # ANS = 3
