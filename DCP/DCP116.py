"""
This problem was asked by Jane Street.

Generate a finite, but an arbitrarily large binary tree quickly in O(1).

That is, generate() should return a tree whose size is unbounded but finite.
"""


class Node:
    node_count = 0
    max_nodes_limit = 10

    def __init__(self, val='default', left=None, right=None, max_nodes_limit: int = 10):
        self.val = val
        self.__left = left
        self.__right = right
        Node.max_nodes_limit = max_nodes_limit

    @property
    def left(self):
        if self.__left is None and Node.node_count < Node.max_nodes_limit:
            self.__left = Node()
            Node.node_count += 1
        return self.__left

    @left.setter
    def left(self, node):
        self.__left = node

    @property
    def right(self):
        if self.__right is None and Node.node_count < Node.max_nodes_limit:
            self.__right = Node()
            Node.node_count += 1
        return self.__right

    @right.setter
    def right(self, node):
        self.__right = node


if __name__ == "__main__":
    tree = Node()
    tree_nodes_values = [
        tree.val,
        tree.left.val,
        tree.right.val,
        tree.left.left.val,
        tree.left.right.val,
        tree.right.left.val,
        tree.right.right.val,
        ]
    for value in tree_nodes_values:
        print(value)
