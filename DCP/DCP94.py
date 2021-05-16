"""
This problem was asked by Google.

Given a binary tree of integers, find the maximum path sum between two nodes. The path must go through at least one node, and does not need to go through the root.
"""


class Node:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#     10
# 5       15

tree1 = Node(val=10,
             left=Node(val=5),
             right=Node(val=15))
tree2 = Node(10)
tree2.left = Node(5)
tree2.right = Node(15)

max_path_sum_memo = {}


def max_path_sum(node: Node) -> int:
    if node is None:
        return 0
    if node not in max_path_sum_memo.keys():
        max_path_sum_memo[node] = max(max_path_sum(node.left),
                                      max_path_sum(node.right),
                                      0) + node.val
    return max_path_sum_memo[node]


#                 2
#         15              18
#    -5       5      7      1
# 2       17
# ANSWER = 29

tree = Node(val=2,
            left=Node(val=15,
                      left=Node(val=-5,
                                left=Node(2),
                                right=Node(17)),
                      right=Node(val=5)),
            right=Node(val=18,
                       left=Node(7),
                       right=Node(1)))

max_path_sum(tree)
print(max(max_path_sum_memo.values()))
