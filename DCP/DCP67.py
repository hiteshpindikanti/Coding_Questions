"""
This problem was asked by Google.

Implement an LFU (Least Frequently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least frequently used item. If there is a tie, then the least recently used key should be removed.
get(key): gets the value at key. If no such key exists, return null.
Each operation should run in O(1) time.
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class LFU:
    def __init__(self, cache_limit: int):
        self.cache_limit = cache_limit
        self.current_cache = 0
        self.dictionary = {}
        self.frequency = {'value': 0, 'start': None, 'end': None}

    def set(self, key, value):
        if self.current_cache == self.cache_limit:

            # Remove the LFU + LRU
            self.dictionary.pop(self.frequency['start'].val['end'].val)
            if self.frequency['start'].val['start'] == self.frequency['start'].val['end']:
                self.frequency['start'] = self.frequency['start'].right
                self.frequency['start'].left = None
            else:
                if self.frequency['start'].val['end'].left is not None:
                    print("INSIDE")
                    self.frequency['start'].val['end'].left.right = None
                self.frequency['start'].val['end'] = self.frequency['start'].val['end'].left

                if self.frequency['start'].val['end'] is None:
                    self.frequency['start'] = self.frequency['start'].right
                    if self.frequency['start'] is not None:
                        self.frequency['start'].left = None

            self.current_cache -= 1

        ref = Node(key)
        if not self.frequency or self.frequency['start'] is None:
            self.frequency['start'] = Node(val={'freq': 0, 'start': ref, 'end': ref},
                                           left=None,
                                           right=self.frequency['start'] if self.frequency else None)
            if self.frequency['end'] is None:
                self.frequency['end'] = self.frequency['start']
            if self.frequency['start'].right is not None:
                self.frequency['start'].right.left = self.frequency['start']
        elif self.frequency['start'].val['freq'] != 0:
            self.frequency['start'] = Node(val={'freq': 0, 'start': ref, 'end': ref}, right=self.frequency['start'])
            self.frequency['start'].right.left = self.frequency['start']
        else:
            # Append node at last
            self.frequency['start'].val['end'].right = ref
            ref.left = self.frequency['start'].val['end']
            self.frequency['start'].val['end'] = self.frequency['start'].val['end'].right
        self.current_cache += 1

        self.dictionary[key] = {'value': value, 'freq_loc': self.frequency['start'], 'node_loc': ref}

    def get(self, key):
        if key in self.dictionary.keys():
            item = self.dictionary[key]

            # Disconnect the node from its freq list
            if item['node_loc'].right is not None:
                item['node_loc'].right.left = item['node_loc'].left
            if item['node_loc'].left is not None:
                item['node_loc'].left.right = item['node_loc'].right
            else:
                item['freq_loc'].val['start'] = item['node_loc'].right

            item['node_loc'].left = None
            item['node_loc'].right = None  # Redundant

            # Assign the node to the beginning of next freq node
            if item['freq_loc'].right is not None and \
                    item['freq_loc'].val['freq'] == item['freq_loc'].right.val['freq'] - 1:
                # Next freq node already exists
                freq_node = item['freq_loc'].right
            else:
                # Create new freq node
                freq_node = Node(val={'freq': item['freq_loc'].val['freq'] + 1, 'start': None, 'end': item['node_loc']},
                                 left=item['freq_loc'],
                                 right=item['freq_loc'].right)

                if item['freq_loc'].right is not None:
                    item['freq_loc'].right.left = freq_node
                item['freq_loc'].right = freq_node

            # Assign this node as the start of the next freq
            item['node_loc'].right = freq_node.val['start']
            freq_node.val['start'] = item['node_loc']
            if item['node_loc'].right is not None:
                item['node_loc'].right.left = item['node_loc']

            # Delete freq if it is empty
            if item['freq_loc'].val['start'] is None:
                if item['freq_loc'].right is not None:
                    item['freq_loc'].right.left = item['freq_loc'].left
                if item['freq_loc'].left is not None:
                    item['freq_loc'].left.right = item['freq_loc'].right
                if self.frequency['start'] == item['freq_loc']:
                    self.frequency['start'] = item['freq_loc'].right

            # Update dictionary
            self.dictionary[key]['freq_loc'] = freq_node

            # Return Value
            return item['value']
        else:
            return None

    def print_info(self):
        print('-----')
        print("DICTIONARY : {}".format({key: value['value'] for key, value in self.dictionary.items()}))
        freq_node = self.frequency['start']
        while freq_node is not None:
            print("FREQ: {}".format(freq_node.val['freq']))
            node = freq_node.val['start']
            print('FORWARD : ', end="")
            while node is not None:
                print("{} -> ".format(node.val), end="")
                node = node.right
            print("None")
            node = freq_node.val['end']
            print("BACKWARD: None", end="")
            while node is not None:
                print(" <- {}".format(node.val), end="")
                node = node.left
            print()
            freq_node = freq_node.right
        print('-----')


if __name__ == "__main__":
    cache = LFU(cache_limit=2)
    cache.set(1, "Hitesh")
    cache.set(2, "Vivek")
    #cache.print_info()
    print("ACCESS {}: {}".format(1, cache.get(1)))
    #cache.print_info()
    print("ACCESS {}: {}".format(1, cache.get(1)))
    #cache.print_info()
    print("ACCESS {}: {}".format(2, cache.get(2)))
    #cache.print_info()
    print("ACCESS {}: {}".format(2, cache.get(2)))
    cache.print_info()
    cache.set(3, "Vinay")
    print("ACCESS {}: {}".format(3, cache.get(3)))
    print("ACCESS {}: {}".format(3, cache.get(3)))
    print("ACCESS {}: {}".format(3, cache.get(3)))
    print("ACCESS {}: {}".format(3, cache.get(3)))
    cache.set(4, "Geetha")
    cache.print_info()

