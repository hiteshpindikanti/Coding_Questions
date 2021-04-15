class Stack:
    def __init__(self):
        self.max_element = float('-inf')
        self.stack = []
        self.max_val_stack = []

    def push(self, val):
        self.stack.append(val)
        self.max_val_stack.append(max(self.max_element, val))

    def pop(self):
        if self.stack:
            self.max_val_stack.pop(-1)
            return self.stack.pop(-1)
        else:
            return None

    def max(self):
        if self.max_val_stack:
            return self.max_val_stack[-1]
        else:
            None


s = Stack()
s.push(10)
print("Max: {}".format(s.max()))
print("pop: {}".format(s.pop()))
print("Max: {}".format(s.max()))
print("Max: {}".format(s.max()))


s = Stack()
s.push(10)
print("Max: {}".format(s.max()))
s.push(11)
print("Max: {}".format(s.max()))
s.push(1)
print("Max: {}".format(s.max()))
print("pop: {}".format(s.pop()))
print("Max: {}".format(s.max()))
print("pop: {}".format(s.pop()))
print("Max: {}".format(s.max()))
print("pop: {}".format(s.pop()))
print("Max: {}".format(s.max()))
print(s.max_val_stack, s.stack)