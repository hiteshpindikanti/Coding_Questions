"""
This problem was asked by Google.

Given the head of a singly linked list, swap every two nodes and return its head.

For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.
"""


class Node:
    def __init__(self, data, next_element=None):
        self.data = data
        self.next = next_element


def swap_pairs(head: Node) -> Node:
    p0 = None
    p1 = head
    p2 = head.next
    if p2 is None:
        return p1
    new_head = p2
    p3 = p2.next
    while p2 is not None:
        p2.next = p1
        p1.next = p3
        if p0 is not None:
            p0.next = p2
        p0 = p1
        p1 = p3
        p2 = p1.next if p1 is not None else None
        p3 = p2.next if p2 is not None else None
    return new_head


def get_ll(head: Node) -> list:
    ll = []
    while head is not None:
        ll.append(head.data)
        head = head.next
    return ll


if __name__ == "__main__":
    ll = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    ll = Node(1)
    print(f"BEFORE: {get_ll(ll)}")
    new_ll = swap_pairs(ll)
    print(f"AFTER: {get_ll(new_ll)}")
