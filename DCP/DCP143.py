"""
This problem was asked by Amazon.

Given a pivot x, and a list lst, partition the list into three parts.

The first part contains all elements in lst that are less than x
The second part contains all elements in lst that are equal to x
The third part contains all elements in lst that are larger than x
Ordering within a part can be arbitrary.

For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one partition may be [9, 3, 5, 10, 10, 12, 14]
"""


def partition(lst: list, x: int):
    """
    In-place operation. O(n)
    :param lst:
    :param x:
    :return:
    """
    i = 0
    j = len(lst) - 1

    while i < j:
        while lst[i] <= x:
            if lst[i] == x:
                t = i
                while lst[t] == x:
                    if t==j:
                        return
                    t += 1
                lst[t], lst[i] = lst[i], lst[t]
                continue
            i += 1

        while lst[j] >= x:
            if lst[j] == x:
                t = j
                while lst[t] == x:
                    if t==i:
                        return
                    t -= 1
                lst[t], lst[j] = lst[j], lst[t]
                continue
            j -= 1

        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1


if __name__ == "__main__":
    lst = [9, 12, 3, 5, 14, 10, 10]
    partition(lst, 10)
    print(lst)
