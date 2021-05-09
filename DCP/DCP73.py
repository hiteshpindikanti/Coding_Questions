"""
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.
Given the head of a singly linked list, reverse it in-place.
"""


class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt


def create_linked_list(arr: list):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    node = head
    i = 1
    while i < len(arr):
        node.next = Node(arr[i])
        node = node.next
        i+=1
    return head


def reverse_linked_list(head: Node):
    if head is None or head.next is None:
        return head
    p2 = None
    p3 = head
    while p3 is not None:
        p1 = p2
        p2 = p3
        p3 = p3.next
        p2.next = p1
    return p2


def print_linked_list(node: Node):
    while node is not None:
        print("{} -> ".format(node.val), end="")
        node = node.next
    print("None")


ll = create_linked_list([1, 2, 3, 4, 5])
print_linked_list(ll)
r_ll = reverse_linked_list(ll)
print_linked_list(r_ll)
