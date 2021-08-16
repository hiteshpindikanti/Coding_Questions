"""
This question was asked by BufferBox.

Given a binary tree where all nodes are either 0 or 1, prune the tree so that subtrees containing all 0s are removed.

For example, given the following tree:

   0
  / \
 1   0
    / \
   1   0
  / \
 0   0
should be pruned to:

   0
  / \
 1   0
    /
   1
We do not remove the tree at the root or its left child because it still has a 1 as a descendant.
"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def prune_zero_subtrees(root: Node):
    if root is None:
        return None
    prune_zero_subtrees(root.left)
    prune_zero_subtrees(root.right)
    if root.left == 0 and root.left.left is root.left.right is None:
        root.left = None
    if root.right == 0 and root.right.left is root.right.right is None:
        root.right = None
    if root.left is None and root.right is None and root.data == 0:
        return None
    else:
        return root


if __name__ == "__main__":
    tree = Node(0,
                left=Node(1),
                right=Node(0,
                           left=Node(1,
                                     left=Node(0),
                                     right=Node(0)),
                           right=Node(0)))
    new_tree = prune_zero_subtrees(tree)

    print(f"{new_tree.data}, {new_tree.left.data}, {new_tree.right.data}, {new_tree.right.left.data}")