"""
This problem was asked by Apple.

Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it.
"""


class Stack:
    def __init__(self):
        self.__stack = []

    def push(self, val):
        self.__stack.append(val)

    def pop(self):
        if len(self.__stack) == 0:
            return None
        else:
            return self.__stack.pop(-1)


class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def __transfer_items(self):
        while True:
            val = self.stack1.pop()
            if val is not None:
                self.stack2.push(val)
            else:
                break

    def enqueue(self, val):
        self.stack1.push(val)

    def dequeue(self):
        self.__transfer_items()
        return self.stack2.pop()


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
