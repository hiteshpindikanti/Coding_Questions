"""
This problem was asked by Google.

Invert a binary tree.

For example, given the following tree:

    a
   / \
  b   c
 / \  /
d   e f
should become:

  a
 / \Invert a binary tree.

For example, given the following tree:

    a
   / \
  b   c
 / \  /
d   e f
should become:

  a
 / \
 c  b
 \  / \
  f e  d
 c  b
 \  / \
  f e  d
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_binary_tree(root):
    stack = [root]
    while stack:
        node = stack.pop(-1)
        node.left, node.right = node.right, node.left
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)


tree = Node('a',
            left=Node('b',
                      left=Node('d'),
                      right=Node('e')),
            right=Node('c',
                       left=Node('f')))

invert_binary_tree(tree)

print("{}".format(tree.val))
print("{} {}".format(tree.left.val, tree.right.val))
print(" {} {} {}". format(tree.left.right.val, tree.right.left.val, tree.right.right.val))
