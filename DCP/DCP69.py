"""
This problem was asked by Facebook.

Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
"""


def max_triple_product(arr: list) -> int:
    max1 = max2 = max3 = float('-inf')
    min1 = min2 = float('inf')

    for val in arr:
        if val > max3:
            max3 = val
            if max3 > max2:
                max2, max3 = max3, max2
                if max2 > max1:
                    max1, max2 = max2, max1

        if val < min2:
            min2 = val
            if min2 < min1:
                min1, min2 = min2, min1

    return max(min1 * min2 * max1, max1 * max2 * max3)


print(max_triple_product([-10, -10, 5, 2]))
