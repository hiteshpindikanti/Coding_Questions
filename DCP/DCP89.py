"""
This problem was asked by LinkedIn.

Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right, and satisfies the constraint that the key in the left child must be less than or equal to the root and the key in the right child must be greater than or equal to the root.
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# RUN INORDER TRAVERSAL
def is_valid(root: Node) -> bool:
    # stack = [root]
    # while stack:
    #     # node = stack.pop(-1)
    #     # if node.left is not None:
    #     #     if node.left.val > node.val:
    #     #         return False
    #     #     else:
    #     #         stack.append(node.left)
    #     # if node.right is not None:
    #     #     if node.right.val < node.val:
    #     #         return False
    #     #     else:
    #     #         stack.append(node.right)
    #
    # return True
    pass


tree1 = Node(val=5,
             left=Node(val=3,
                       left=Node(val=1)),
             right=Node(val=8,
                        left=Node(val=7,
                                  left=Node(6))))

tree2 = Node(val=6,
             left=Node(10))

print(is_valid(tree1))
print(is_valid(tree2))
