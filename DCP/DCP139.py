"""
This problem was asked by Google.

Given an iterator with methods next() and hasNext(), create a wrapper iterator, PeekableInterface, which also implements peek(). peek shows the next element that would be returned on next().

Here is the interface:

class PeekableInterface(object):
    def __init__(self, iterator):
        pass

    def peek(self):
        pass

    def next(self):
        pass

    def hasNext(self):
        pass
"""
from copy import deepcopy


class PeekableInterface(object):
    def __init__(self, iterator):
        self.iterator = iterator

    def peek(self):
        try:
            return next(deepcopy(self.iterator))
        except StopIteration:
            return None

    def next(self):
        return next(self.iterator)

    def has_next(self):
        try:
            next(deepcopy(self.iterator))
            return True
        except StopIteration:
            return False


if __name__ == "__main__":
    obj = PeekableInterface(iter([1, 2, 3, 4, 5]))
    print(f"{obj.next()} {obj.next()} {obj.next()} {obj.next()} {obj.peek()} {obj.next()}")

