"""
This problem was asked by Microsoft.

Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def evaluate_arithmetic_tree(root):
    operators = {'+', '−', '∗', '/'}
    stack = [root, root]
    print("START")
    while stack:
        node = stack.pop(-1)

        if node.right is not None and node.left is not None and \
                node.right.val not in operators and node.left.val not in operators:
            node.val = str(eval(node.left.val + node.val + node.right.val))

            node.left = None
            node.right = None
        if node.left is not None and node.left.val in operators:
            stack.append(node.left)
            stack.append(node.left)
        if node.right is not None and node.right.val in operators:
            stack.append(node.right)
            stack.append(node.right)


tree = Node(val='*',
            left=Node(val='+',
                      left=Node('3'),
                      right=Node('2')),
            right=Node(val='+',
                       left=Node('4'),
                       right=Node('5')))


evaluate_arithmetic_tree(tree)
print(tree.val)
