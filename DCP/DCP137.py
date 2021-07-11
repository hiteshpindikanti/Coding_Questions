"""
This problem was asked by Amazon.

Implement a bit array.

A bit array is a space efficient array that holds a value of 1 or 0 at each index.

init(size): initialize the array with size
set(i, val): updates index at i with val where val is either 1 or 0.
get(i): gets the value at index i.
"""


class BitArray:
    def __init__(self, size):
        self.size = size
        self.bit_array = 0

    def set_val_at_index(self, index: int, value: int):
        if value not in {0, 1}:
            raise Exception("value is not a binary number")
        if self.bit_array & (1 << index) and value == 0:
            self.bit_array = self.bit_array & ~(1 << index)
        elif not self.bit_array & (1 << index) and value == 1:
            self.bit_array = self.bit_array | (1 << index)

    def get_val_at_index(self, index: int):
        if index >= self.size:
            raise IndexError("index out of range")
        if self.bit_array & (1 << index):
            return 1
        else:
            return 0


if __name__ == "__main__":
    arr = BitArray(10)
    print(arr.get_val_at_index(2))
    arr.set_val_at_index(2, 1)
    print(arr.get_val_at_index(2))
    arr.set_val_at_index(2, 1)
    print(arr.get_val_at_index(2))
    arr.set_val_at_index(2, 0)
    print(arr.get_val_at_index(2))
