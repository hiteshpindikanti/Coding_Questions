"""
This question was asked by Snapchat.

Given the head to a singly linked list, where each node also has a “random” pointer that points to anywhere in the linked list, deep clone the list.
"""


class Node:
    def __init__(self, val, next_node=None, random_node=None):
        self.val = val
        self.next = next_node
        self.random = random_node


def deep_clone(head: Node) -> Node:
    clone_head = None
    node = head
    if node is not None:
        clone_map = {}
        clone_head = Node(node.val)
        clone_map[head] = clone_head
        node = node.next
        prev_clone_node = clone_head

        # 1st Pass: Initial cloning without the random pointer
        while node is not None:
            prev_clone_node.next = Node(node.val)
            prev_clone_node = prev_clone_node.next
            clone_map[node] = prev_clone_node
            node = node.next

        # 2nd Pass: Clone the random pointer
        node = head
        clone_node = clone_head
        while node is not None:
            clone_node.random = clone_map[node.random]
            node = node.next
            clone_node = clone_node.next

    return clone_head


def get_linked_list(head: Node) -> list[dict]:
    linked_list = []
    node = head
    while node is not None:
        linked_list.append({'val': node.val, 'next': node.next.val if node.next is not None else None,
                            'random': node.random.val if node.random is not None else None})
        node = node.next
    return linked_list


if __name__ == "__main__":
    original_linked_list = Node(1, Node(2, Node(3, Node(4))))
    # random pointers
    original_linked_list.random = original_linked_list.next.next
    original_linked_list.next.random = original_linked_list.next.next.next
    original_linked_list.next.next.random = original_linked_list
    original_linked_list.next.next.next.random = original_linked_list.next

    print(f"Original Linked List: {get_linked_list(original_linked_list)}")
    new_linked_list = deep_clone(original_linked_list)
    print(f"Cloned Linked List: {get_linked_list(new_linked_list)}")
