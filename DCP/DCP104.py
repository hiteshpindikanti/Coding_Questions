"""
This problem was asked by Google.

Determine whether a doubly linked list is a palindrome. What if it’s singly linked?

For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False.
"""


class DNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SNode:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt


def is_palindrome_doubly(node: DNode) -> bool:
    head = node
    tail = head
    length = 1
    while tail.right is not None:
        length += 1
        tail = tail.right
    for _ in range(length // 2):
        if head.val != tail.val:
            return False
        head = head.right
        tail = tail.left
    return True


def is_palindrome_singly(node: SNode) -> bool:
    stack = []
    head = node
    length = 1
    while node.next is not None:
        length += 1
        node = node.next
    node = head
    for _ in range(length // 2):
        stack.append(node.val)
        node = node.next

    if length & 1:
        node = node.next
    for _ in range(length // 2):
        if stack.pop(-1) != node.val:
            return False
        node = node.next

    return True


if __name__ == "__main__":
    dll = DNode(1)
    dll.right = DNode(2, dll)
    dll.right.right = DNode(1, dll.right)
    print(is_palindrome_doubly(dll))

    sll = SNode(1, SNode(2, SNode(1)))
    print(is_palindrome_singly(sll))