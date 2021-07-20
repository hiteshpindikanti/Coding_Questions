"""
This problem was asked by Microsoft.

Implement 3 stacks using a single list:

"""


class Stack:
    def __init__(self):
        self.list_size = 6
        self.list = [None] * self.list_size
        self.stack_top_index = [-1, (self.list_size // 2) - 1, self.list_size]

    def pop(self, stack_number):
        element = self.list[self.stack_top_index[stack_number]]
        if element is None:
            raise IndexError
        self.list[self.stack_top_index[stack_number]] = None
        self.stack_top_index[stack_number] = self.stack_top_index[stack_number] + (1 if stack_number == 2 else -1)
        return element

    def push(self, item, stack_number):
        self.list[self.stack_top_index[stack_number] + (-1 if stack_number == 2 else 1)] = item
        self.stack_top_index[stack_number] = self.stack_top_index[stack_number] + (-1 if stack_number == 2 else 1)
        self.increase_stack_size_if_full()

        pass

    def increase_stack_size_if_full(self):
        if self.stack_top_index[0] == self.list_size // 2 - 1 or self.stack_top_index[1] == self.stack_top_index[2] - 1:
            self.list = self.list[:self.stack_top_index[0] + 1] + [None] * (
                        self.list_size - (self.stack_top_index[0] + 1)) + \
                        self.list[self.list_size // 2:self.stack_top_index[1]] + \
                        [None] * (self.list_size - (self.list_size - self.stack_top_index[2] +
                                                    self.stack_top_index[1] - self.list_size // 2) - 1) \
                        + self.list[self.stack_top_index[2]:]
            self.stack_top_index[1] = self.list_size + (self.stack_top_index[1] - self.list_size//2 - 1)
            self.stack_top_index[2] = self.list_size*2 -(self.list_size - self.stack_top_index[2])
            self.list_size *= 2




if __name__ == "__main__":
    s = Stack()
    s.push('Hitesh1', 0)
    print(f"{s.list_size}, {len(s.list)}")
    s.push('Hitesh2', 0)
    print(f"{s.list_size}, {len(s.list)}, {s.list}")
    s.push('Hitesh3', 0)
    print(f"{s.list_size}, {len(s.list)}, {s.list}")
    s.push('Vivek1', 1)
    print(f"{s.list_size}, {len(s.list)}, {s.list}")
    s.push('Vinay1', 2)
    print(f"{s.list_size}, {len(s.list)}, {s.list}")

