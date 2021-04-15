"""
This problem was asked by Google.

Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

For example, given the following preorder traversal:

[a, b, d, e, c, f, g]

And the following inorder traversal:

[d, b, e, a, f, c, g]

You should return the following tree:

    a
   / \
  b   c
 / \ / \
d  e f  g
"""


class Node:
    def __init__(self, val: int = None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def generate_tree(preorder: list = None, inorder: list = None, postorder: list = None) -> Node:
    if len(list(filter(lambda x: x is not None, [preorder, inorder, postorder]))) > 1:
        raise Exception("Insufficient Data. At least 2 traversal orders required.")

    root_node = Node()

    if preorder is not None and inorder is not None:
        stack = [(root_node, preorder, inorder)]
        while stack:
            root, preorder, inorder = stack.pop(-1)
            root.val = preorder[0]
            index = inorder.index(preorder[0])
            if index > 0:
                root.left = Node()
                stack.append((root.left, preorder[1:index+1], inorder[:index]))
            if index < len(preorder)-1:
                root.right = Node()
                stack.append((root.right, preorder[index+1:], inorder[index+1:]))
    
    elif preorder is not None and postorder is not None:
        pass

    elif inorder is not None and postorder is not None:
        pass

    return root_node
