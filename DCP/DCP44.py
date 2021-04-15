"""
This problem was asked by Google.

We can determine how "out of order" an array A is by counting the number of inversions it has. Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.
"""
from math import ceil


def count_inversions(arr: list) -> int:
    if len(arr) % 2 == 1:
        arr.append(float('inf'))
    num_inversions = 0
    for k in range(1, len(arr) // 2 + 1):
        for start in range(0, len(arr), 2 * k):
            end = min(start + 2 * k, len(arr))
            mid = (start + end - 1) // 2
            if end - start == 1:
                continue
            i = start
            j = mid + 1
            sorted_arr = []
            while i <= mid or j < end:
                while i <= mid and (j == end or arr[i] < arr[j]):
                    sorted_arr.append(arr[i])
                    i += 1
                    if j == end:
                        num_inversions += 1

                while j < end and (i == mid + 1 or arr[i] > arr[j]):
                    sorted_arr.append(arr[j])
                    j += 1
                    if i <= mid:
                        num_inversions += 1

            for index, val in enumerate(sorted_arr):
                arr[start + index] = val
    print(arr)
    return num_inversions


#print(count_inversions([2, 4, 1, 3, 5]))
print(count_inversions([5, 4, 3, 2, 1]))
