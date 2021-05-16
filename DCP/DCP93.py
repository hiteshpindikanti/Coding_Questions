"""
This problem was asked by Apple.

Given a tree, find the largest tree/subtree that is a BST.

Given a tree, return the size of the largest tree/subtree that is a BST.
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# TODO: Memoization
def get_bst_size(node: Node):
    if node is None:
        return 0
    size = 1
    if node.left is not None and node.val > node.left.val:
        size += get_bst_size(node.left)
    if node.right is not None and node.val < node.right.val:
        size += get_bst_size(node.right)
    return size


# TODO: Memoization
def get_largest_bst_size(node: Node) -> int:
    if node is None:
        return 0
    options = [get_bst_size(node),
               get_largest_bst_size(node.left),
               get_largest_bst_size(node.right)]
    return max(options)


#                 20
#         10              18
#     5       15      17      19
# 2       7
# ANSWER = 6
tree = Node(val=20,
            left=Node(val=10,
                      left=Node(val=5,
                                left=Node(2),
                                right=Node(7)),
                      right=Node(val=15)),
            right=Node(val=18,
                       left=Node(17),
                       right=Node(19)))

print(get_largest_bst_size(tree))

#                 9
#         10              18
#     5       15      17      19
# 2       7
# ANSWER = 5
tree = Node(val=9,
            left=Node(val=10,
                      left=Node(val=5,
                                left=Node(2),
                                right=Node(7)),
                      right=Node(val=15)),
            right=Node(val=18,
                       left=Node(17),
                       right=Node(19)))

print(get_largest_bst_size(tree))

#                 9
#         10              18
#     5       15      17      19
# 20      7
# ANSWER = 4
tree = Node(val=9,
            left=Node(val=10,
                      left=Node(val=5,
                                left=Node(20),
                                right=Node(7)),
                      right=Node(val=15)),
            right=Node(val=18,
                       left=Node(17),
                       right=Node(19)))

print(get_largest_bst_size(tree))
