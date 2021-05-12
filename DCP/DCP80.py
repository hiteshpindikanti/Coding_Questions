"""
This problem was asked by Google.

Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.

    a
   / \
  b   c
 /
d
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_deepest_node(root: Node) -> Node:
    node = root
    level = 0

    # Run DFS
    queue = [(node, level)]
    while queue:
        node, level = queue.pop(0)
        if node.left is not None:
            queue.append((node.left, level + 1))
        if node.right is not None:
            queue.append((node.right, level + 1))
    return node


tree = Node('a',
            left=Node('b',
                      left=Node('d')),
            right=Node('c'))

print(get_deepest_node(tree).val)
