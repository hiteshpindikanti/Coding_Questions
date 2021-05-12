"""
This problem was asked by Snapchat.

Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].
"""


def merged_intervals(intervals) -> list:
    intervals.sort()
    merged_intervals = []
    i = -1
    while i >= -len(intervals):
        start, end = intervals[i]
        i -= 1
        while i >= -len(intervals) and intervals[i][1] > start:
            start = intervals[i][0]
            end = max(end, intervals[i][1])
            i -= 1
        merged_intervals.append((start, end))

    return merged_intervals


intervals1 = [(1, 3), (5, 8), (4, 10), (20, 25)]
intervals2 = [(1, 5), (2, 4)]
intervals3 = [(1, 5), (2, 10)]
intervals4 = [(6, 10), (1, 7)]
intervals5 = [(1, 5), (6, 10)]
intervals6 = [(1, 5), (2, 6), (3, 7), (4, 8)]

print(merged_intervals(intervals1))
print(merged_intervals(intervals2))
print(merged_intervals(intervals3))
print(merged_intervals(intervals4))
print(merged_intervals(intervals5))
print(merged_intervals(intervals6))
