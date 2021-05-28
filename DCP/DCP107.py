"""
This problem was asked by Microsoft.

Print the nodes in a binary tree level-wise. For example, the following should print 1, 2, 3, 4, 5.

  1
 / \
2   3
   / \
  4   5
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_left_child_index(parent_index: int) -> int:
    return parent_index * 2 + 1


def get_right_child_index(parent_index: int) -> int:
    return parent_index * 2 + 2


def append_any_index(lst: list, element, index: int = None):
    if index is None:
        lst.append(element)
    else:
        if index >= len(lst):
            appending_list = [None] * (index - len(lst))
            appending_list.append(element)
            lst.extend(appending_list)
        else:
            if lst[index] is None:
                lst[index] = element
            else:
                raise Exception(f"Same index referenced multiple times: index={index}, \
                element={element}, existing_element={lst[index]}")


def get_elements(root: Node) -> list:
    stack = [(0, root)]
    elements = []
    while stack:
        index, node = stack.pop(-1)
        append_any_index(elements, node.val, index)
        if node.left is not None:
            stack.append((get_left_child_index(index), node.left))
        if node.right is not None:
            stack.append((get_right_child_index(index), node.right))
    return list(filter(lambda x: x is not None, elements))


if __name__ == "__main__":
    """
      1
     / \
    2   3
       / \
      4   5
    """
    tree = Node(1,
                left=Node(2),
                right=Node(3,
                           left=Node(4),
                           right=Node(5)))

    print(get_elements(tree))