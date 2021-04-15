"""
This problem was asked by Airbnb.
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
Numbers can be 0 or negative.
For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10,
since we pick 5 and 5.
Follow-up: Can you do this in O(N) time and constant space?
"""


def largest_sum(arr):
    odd_max = float('-inf')
    even_max = float('-inf')
    if len(arr) <= 2:
        return max(arr)
    else:
        even_max = arr[0]
        odd_max = arr[1]
    index = 2
    while index < len(arr):
        if index % 2 == 0:
            odd_max = max(odd_max, even_max)
            if odd_max < 0:
                odd_max = 0
            even_max = max(even_max, even_max + arr[index])
            if even_max < 0:
                even_max = 0
        else:
            even_max = max(odd_max, even_max)
            if even_max < 0:
                even_max = 0
            odd_max = max(odd_max, odd_max + arr[index])
            if odd_max < 0:
                odd_max = 0
        index += 1

    if max(odd_max, even_max) <= 0:
        return max(arr)
    else:
        return max(odd_max, even_max)


print(largest_sum([5, 1, 1, 5]))
print(largest_sum([2, 4, 6, 2, 5]))
print(largest_sum([0, 0, 9, 10, 8, 0, 0]))
print(largest_sum([-1, -10, -1, -5, 10]))
