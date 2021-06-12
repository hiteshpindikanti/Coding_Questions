"""
This problem was asked by Google.

Given a set of closed intervals, find the smallest set of numbers that covers all the intervals. If there are multiple smallest sets, return any of them.

For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set of numbers that covers all these intervals is {3, 6}.
"""


def get_smallest_set(intervals: list) -> set:
    smallest_set = set()
    intervals = list(map(lambda x: x[::-1], intervals))
    intervals.sort(reverse=True)
    intervals = list(map(lambda x: x[::-1], intervals[::-1]))
    i = len(intervals) - 1
    next_number_range = intervals[i][:]
    i -= 1
    while i >= 0:
        if intervals[i][1] < next_number_range[0]:
            smallest_set.add(next_number_range[0])
            next_number_range = intervals[i][:]
        elif intervals[i][0] < next_number_range[0]:
            next_number_range[1] = intervals[i][1]
        elif intervals[i][0] >= next_number_range[0]:
            next_number_range = intervals[i][:]
        i -= 1

    smallest_set.add(next_number_range[0])
    return smallest_set


if __name__ == "__main__":
    print(get_smallest_set([[0, 3], [2, 6], [3, 4], [6, 9]]))  # ANS = {3, 6}
