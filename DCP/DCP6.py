"""
An XOR linked list is a more memory efficient doubly linked list.
Instead of each node holding next and prev fields, it holds a field named both,
which is an XOR of the next node and the previous node. Implement an XOR linked list;
it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python),
you can assume you have access to get_pointer and dereference_pointer functions
that converts between nodes and memory addresses.
"""
import ctypes


class Node:
    def __init__(self, val, both=None):
        self.val = val
        self.both = id(None) ^ id(None) if both is None else both

    def next(self, prev_node):
        next_node_id = id(prev_node) ^ self.both
        return ctypes.cast(next_node_id, ctypes.py_object).value

    def prev(self, next_node):
        prev_node_id = self.both ^ id(next_node)
        return ctypes.cast(prev_node_id, ctypes.py_object).value


def insert_node(head, val):
    prev_node = None
    while head.next(prev_node) is not None:
        temp = head
        head = head.next(prev_node)
        prev_node = temp
    node = head
    next_node = Node(val, id(node) ^ id(None))
    node.both = id(prev_node) ^ id(next_node)


def traverse(head) -> list:
    result = []
    prev_node = None
    while head.next(prev_node) is not None:
        result.append(head.val)
        temp = head
        head = head.next(prev_node)
        prev_node = temp
    return result


if __name__ == "__main__":
    root = Node(1)
    insert_node(root, 2)
    insert_node(root, 3)
    insert_node(root, 4)
    insert_node(root, 5)
    insert_node(root, 6)
    traverse(root)