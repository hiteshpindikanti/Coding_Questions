"""
This problem was asked by Google.

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.
"""
from queue import Queue


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs(root: Node, value) -> list:
    queue = Queue()
    queue.put(root)
    matching_nodes = []
    while not queue.empty():
        node = queue.get()
        if node.val == value:
            matching_nodes.append(node)
        if node.left is not None:
            queue.put(node.left)
        if node.right is not None:
            queue.put(node.right)
    return matching_nodes


def get_inorder_traversal(root) -> list:
    if root is None:
        return []
    inorder_path = []
    stack = [(root, True)]
    while stack:
        node, is_node = stack.pop()
        if not is_node:
            inorder_path.append(node)
        else:
            if node.right is not None:
                stack.append((node.right, True))
            stack.append((node.val, False))
            if node.left is not None:
                stack.append((node.left, True))
    return inorder_path


def is_subtree_of(subtree_root: Node, original_tree_root: Node) -> bool:
    matching_nodes = bfs(original_tree_root, subtree_root.val)
    subtree_inorder_traversal = get_inorder_traversal(subtree_root)
    for node in matching_nodes:
        inorder_traversal = get_inorder_traversal(node)
        if inorder_traversal == subtree_inorder_traversal:
            return True
    return False


if __name__ == "__main__":
    #        1
    #      /    \
    #    2       3
    #  /   \
    # 4     5
    #        \
    #         6

    tree = Node(1,
                left=Node(2,
                          left=Node(4),
                          right=Node(5,
                                     right=Node(6))),
                right=Node(3))

    subtree = Node(2,
                   left=Node(4),
                   right=Node(5,
                              right=Node(6)))
    print(is_subtree_of(subtree, tree))  # ANS = True
