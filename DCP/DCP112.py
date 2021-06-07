"""
This problem was asked by Twitter.

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree. Assume that each node in the tree also has a pointer to its parent.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”
"""
import unittest


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(root.val, 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")


class Node:
    def __init__(self, val, parent=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


def get_lowest_common_ancestor(node1: Node, node2: Node):
    if node1 is None or node2 is None:
        return None
    path1_visited = {node1}
    path2_visited = {node2}
    while node1 not in path2_visited and node2 not in path1_visited and \
            (node1.parent is not None or node2.parent is not None):
        # Loop will run infinite if the binary tree does not have a single root
        if node1.parent is not None:
            node1 = node1.parent
            path1_visited.add(node1)
        if node2.parent is not None:
            node2 = node2.parent
            path2_visited.add(node2)
    if node1 in path2_visited:
        return node1
    elif node2 in path1_visited:
        return node2
    elif node1 == node2:
        return node1
    else:
        return None


if __name__ == "__main__":
    #        1
    #      /    \
    #    2       3
    #  /   \
    # 4     5
    #        \
    #         6

    # Building the tree down-up
    n1 = node = Node(6)
    node.parent = Node(5, right=node)
    node = node.parent

    node.parent = Node(2, right=node)
    node = node.parent

    n2 = node.left = Node(4, parent=node)
    node.parent = Node(1, left=node)
    node = node.parent
    node.right = Node(3, parent=node)
    root = node

    # Testing the tree
    assert root.parent is None
    assert root.val == 1
    assert root.left.val == 2
    assert root.left.parent.val == 1
    assert root.right.val == 3
    assert root.right.parent.val == 1
    assert root.left.left.val == 4
    assert root.left.left.parent.val == 2
    assert root.left.right.val == 5
    assert root.left.right.parent.val == 2
    assert root.left.right.right.val == 6
    assert root.left.right.right.parent.val == 5
    print("All Testcases passed")

    print(get_lowest_common_ancestor(n1, n2).val)  # Ans = 2
