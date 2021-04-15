class Node:
    def __init__(self, val: int, left: object = None, right: object = None):
        self.val = val
        self.left = left
        self.right = right


def second_largest_node(root: Node) -> Node:
    parent_node, node = largest_node(root)
    _, node = largest_node(node.left)
    if node is None:
        return parent_node
    else:
        return node


def largest_node(root: Node) -> tuple:
    """
    :param root: root of the tree
    :return: (Parent Node, Largest Node)
    """
    if root is None:
        return None, None
    node = root
    parent_node = None
    while node.right is not None:
        parent_node = node
        node = node.right
    return parent_node, node


if __name__ == "__main__":
    root = Node(val=10,
                left=Node(val=5),
                right=Node(val=15,
                           left=Node(val=13,
                                     right=Node(val=14))))
    node = second_largest_node(root)
    print(node.val)