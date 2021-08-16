class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class LRU:
    def __init__(self, max_capacity: int):
        self.max_capacity = max_capacity
        self.current_capacity = 0
        self.lru_dict = {}  # [key, lru_ll_ptr]
        self.lru_head = None
        self.lru_tail = None

    def put(self, key, value):

        if key in self.lru_dict:
            self.lru_dict[key].data = value
        else:
            if self.current_capacity >= self.max_capacity:
                self.remove_lru()
            self.lru_dict[key] = Node(value)
            self.lru_dict[key].next = self.lru_head
            if self.lru_head is not None:
                self.lru_head.prev = self.lru_dict[key]
            self.lru_head = self.lru_dict[key]
            if self.lru_tail is None:
                self.lru_tail = self.lru_head
            self.current_capacity += 1

    def get(self, key):
        if key not in self.lru_dict:
            return None
        else:
            self.move_to_head(self.lru_dict[key])
            return self.lru_dict[key].data

    def move_to_head(self, node: Node):
        if node is self.lru_tail:
            self.lru_tail = self.lru_tail.prev
        if node.prev is not None:
            node.prev.next = node.next
        node.next = self.lru_head
        self.lru_head = node

    def remove_lru(self):
        self.lru_tail = self.lru_tail.prev
        if self.lru_tail is not None:
            self.lru_tail.next = None


def print_ll(node):
    while node is not None:
        print(f"{node.data}->", end="")
        node = node.next
    print("None")


if __name__ == "__main__":
    lru = LRU(3)
    lru.put(1, 10)
    lru.put(2, 20)
    print_ll(lru.lru_head)
    print(lru.get(1))
    print_ll(lru.lru_head)
    lru.put(3, 30)
    print_ll(lru.lru_head)
    lru.put(4, 40)
    print_ll(lru.lru_head)
