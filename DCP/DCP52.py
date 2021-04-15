"""
This problem was asked by Google.

Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item.
get(key): gets the value at key. If no such key exists, return null.
Each operation should run in O(1) time.

"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Cache:
    def __init__(self, cache_size: int):
        self.dict = {}
        self.rev_dict = {}
        self.linked_list_front = None
        self.linked_list_end = None
        self.cache_limit = cache_size
        self.linked_list_length = 0
        pass

    def __append_front(self, key, value):
        if self.linked_list_length == 0:
            self.linked_list_front = Node(value)
            self.linked_list_end = self.linked_list_front
        else:
            self.linked_list_front.left = Node(value, right=self.linked_list_front)
            self.linked_list_front = self.linked_list_front.left
        self.dict[key] = self.linked_list_front
        self.rev_dict[self.linked_list_front] = key
        self.linked_list_length += 1

    def __remove_last(self):
        temp = self.linked_list_end
        self.linked_list_end = self.linked_list_end.left
        self.linked_list_end.right = None
        key = self.rev_dict.pop(temp)
        self.dict.pop(key)

        self.linked_list_length -= 1

    def __move_to_front(self, key):
        node = self.dict[key]
        if node == self.linked_list_front:
            return
        node.left.right, node.right.left = node.right, node.left
        node.right = self.linked_list_front
        self.linked_list_front.left = node
        self.linked_list_front = self.linked_list_front.left

    def set(self, key, value):
        print("length = {}, limit = {}".format(self.linked_list_length, self.cache_limit))
        if self.linked_list_length == self.cache_limit:
            self.__remove_last()
        self.__append_front(key, value)

    def get(self, key):
        if key in self.dict.keys():
            self.__move_to_front(key)
            return self.dict[key].val
        else:
            return None


def print_ll(root: Node):
    result = []
    while root is not None:
        result.append(root.val)
        root = root.right
    print(' -> '.join(result))


if __name__ == "__main__":
    lru = Cache(cache_size=5)
    lru.set(1, "Hitesh")
    lru.set(2, "Vivek")
    lru.set(3, "Vinay")
    print_ll(lru.linked_list_front)
    print("Get 2: {}".format(lru.get(2)))
    print_ll(lru.linked_list_front)
    print("Get 3: {}".format(lru.get(3)))
    print_ll(lru.linked_list_front)
    print("Get 3: {}".format(lru.get(3)))
    print_ll(lru.linked_list_front)
    print("Get 2: {}".format(lru.get(2)))
    print_ll(lru.linked_list_front)
    lru.set(4, "Geetha")
    lru.set(5, "Manish")
    print_ll(lru.linked_list_front)
    lru.set(6, "Hemant")
    print_ll(lru.linked_list_front)


