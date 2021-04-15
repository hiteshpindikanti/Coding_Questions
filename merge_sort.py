import time
from random import randint


def recursive_merge_sort(array: list, start: int = 0, end: int = None) -> list:

    if end is None:
        end = len(array) - 1
    mid = (start + end)//2
    if start == end:
        return [array[start]]

    array1 = recursive_merge_sort(array, start, mid)
    array2 = recursive_merge_sort(array, mid+1, end)

    # Merge
    i = 0
    j = 0
    result = []
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            result.append(array1[i])
            i += 1
        else:
            result.append(array2[j])
            j += 1
    result.extend(array1[i:])
    result.extend(array2[j:])
    return result


def iterative_merge_sort(array) -> list:
    array = array[:]

    list_size = 1
    while list_size < len(array):
        i = 0
        while i < len(array):
            start = i
            end = min(i + (2*list_size)-1, len(array)-1)
            mid = (start + end)//2

            result = []

            # Merge
            a1 = start
            a2 = mid+1
            while a1 < mid+1 and a2 < end+1:
                if array[a1] < array[a2]:
                    result.append(array[a1])
                    a1 += 1
                else:
                    result.append(array[a2])
                    a2 += 1
            result.extend(array[a1:mid+1])
            result.extend(array[a2:end+1])

            for index, val in enumerate(result):
                array[start+index] = val

            i += 2*list_size
        list_size *= 2
    return array


if __name__ == "__main__":
    arr = [randint(1, 10**4) for _ in range(10**5)]

    start_time = time.time()
    sorted_arr = recursive_merge_sort(arr, 0, len(arr)-1)
    end_time = time.time()
    print("Time taken to sort {} elements recursively: {} secs".format(len(arr), end_time-start_time))

    start_time = time.time()
    sorted_arr = iterative_merge_sort(arr)
    end_time = time.time()
    print("Time taken to sort {} elements iteratively: {} secs".format(len(arr), end_time-start_time))

