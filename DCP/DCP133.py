"""
This problem was asked by Amazon.

Given a node in a binary search tree, return the next bigger element, also known as the inorder successor.

For example, the inorder successor of 22 is 30.

   10
  /  \
 5    30
     /  \
   22    35
You can assume each node has a parent pointer.
"""


class Node:
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


def get_inorder_successor(node: Node) -> Node:
    inorder_successor = node.parent
    if node.right is not None:
        node = node.right
        while node.left is not None:
            node = node.left
        inorder_successor = node
    return inorder_successor


if __name__ == "__main__":
    tree = Node(10,
                left=Node(5),
                right=Node(30,
                           left=Node(22),
                           right=Node(35)))
    tree.left.parent = tree.right.parent = tree
    tree.right.left.parent = tree.right.right.parent = tree.right

    n = get_inorder_successor(tree.right.left)
    print(f"{tree.right.left.val} => {n.val if n is not None else None}")

