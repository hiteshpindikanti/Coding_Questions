"""
This problem was asked by Google.

Given the root of a binary search tree, and a target K, return two nodes in the tree whose sum equals K.

For example, given the following tree and K of 20

    10
   /   \
 5      15
       /  \
     11    15
Return the nodes 5 and 15.
"""
from collections import defaultdict


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_pair(root: Node, k):
    tree_dict = defaultdict(list)

    # Traverse
    stack = [root]
    while stack:
        node = stack.pop()
        tree_dict[node.val].append(node)
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)

    for node_value in tree_dict.keys():
        if k - node_value in tree_dict.keys():
            if node_value != k / 2:
                return tree_dict[node_value][0], tree_dict[k - node_value][0]
            elif len(tree_dict[node_value]) > 1:
                return tuple(tree_dict[node_value][:2])

    return None, None


if __name__ == "__main__":
    #     10
    #    /   \
    #  5      15
    #        /  \
    #      11    15

    tree = Node(10,
                Node(5),
                Node(15,
                     Node(11),
                     Node(15)))
    node1, node2 = get_pair(tree, 20)
    print(f'{node1.val}, {node2.val}')
