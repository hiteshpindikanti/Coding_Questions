"""
This problem was asked by Pinterest.

Given an integer list where each number represents the number of hops you can make, determine whether you can reach to the last index starting at index 0.

For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.
"""


def can_reach_end(hops: list) -> bool:
    index = 0
    prev_index = -1
    while len(hops)-1 > index > prev_index:
        prev_index = index
        index += hops[index]
    if index == len(hops)-1:
        return True
    else:
        return False


if __name__ == "__main__":
    print(can_reach_end([2, 0, 1, 0]))
    print(can_reach_end([1, 1, 0, 1]))
