"""
This problem was asked by Google.

Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.
"""
import heapq


class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt


def merge_all_linked_lists(ll_arr: list) -> Node:
    current_elements = [(node.val, index) for index, node in enumerate(ll_arr)]
    heapq.heapify(current_elements)
    value, index = heapq.heappop(current_elements)
    ll_arr[index] = ll_arr[index].next
    if ll_arr[index] is not None:
        heapq.heappush(current_elements, (ll_arr[index].val, index))

    merged_head = Node(value)
    node = merged_head
    while current_elements:
        value, index = heapq.heappop(current_elements)
        ll_arr[index] = ll_arr[index].next
        if ll_arr[index] is not None:
            heapq.heappush(current_elements, (ll_arr[index].val, index))
        node.next = Node(value)
        node = node.next
    return merged_head


def get_ll(node: Node) -> list:
    lst = []
    while node is not None:
        lst.append(node.val)
        node = node.next
    return lst


array = [
    Node(0, Node(10, Node(20, Node(30, Node(40))))),
    Node(1, Node(11, Node(21, Node(31)))),
    Node(2, Node(22, Node(23))),
    Node(5, Node(50))
]

print(get_ll(merge_all_linked_lists(array)))