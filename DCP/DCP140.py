"""
This problem was asked by Facebook.

Given an array of integers in which two elements appear exactly once and all other elements appear exactly twice, find the two elements that appear only once.

For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8. The order does not matter.

Follow-up: Can you do this in linear time and constant space?
"""


def get_odd_elements(array: list) -> tuple:
    xor = 0
    for element in array:
        xor = xor ^ element

    set_bit_index = 0
    while not xor & (1 << set_bit_index):
        set_bit_index += 1

    group1_xor = 0
    group2_xor = 0
    for element in array:
        if element & (1 << set_bit_index):
            # Group 1
            group1_xor = group1_xor ^ element
        else:
            # Group 2
            group2_xor = group2_xor ^ element

    return group1_xor, group2_xor


if __name__ == "__main__":
    print(get_odd_elements([2, 4, 6, 8, 10, 2, 6, 10]))
