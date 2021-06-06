"""
This problem was asked by Facebook.

Given a binary tree, return all paths from the root to leaves.

For example, given the tree:

   1
  / \
 2   3
    / \
   4   5
Return [[1, 2], [1, 3, 4], [1, 3, 5]].
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_all_paths(root) -> list:
    if root is None:
        return []

    all_paths = []
    stack = [[root, []]]
    while stack:
        node, path = stack.pop(-1)
        appended_path = path + [node.val]
        if node.left is None and node.right is None:
            # it is a leaf node, append the path to all_paths
            all_paths.append(appended_path)
        else:
            if node.left is not None:
                stack.append([node.left, appended_path])
            if node.right is not None:
                stack.append([node.right, appended_path])
    return all_paths


if __name__ == "__main__":
    tree = Node(1,
                left=Node(2),
                right=Node(3,
                           left=Node(4),
                           right=Node(5)))
    print(get_all_paths(tree))

