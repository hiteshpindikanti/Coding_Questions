import heapq


def running_median(l: list) -> list:
    maxheap = []
    minheap = []
    heapq.heapify(maxheap)
    heapq.heapify(minheap)
    median_list = []
    median = 0
    for val in l:
        if val < median:
            if len(maxheap) > len(minheap):
                heapq.heappush(minheap, -heapq.heappop(maxheap))
            heapq.heappush(maxheap, -val)
        elif val > median:
            if len(minheap) > len(maxheap):
                heapq.heappush(maxheap, -heapq.heappop(minheap))
            heapq.heappush(minheap, val)
        else:
            heapq.heappush(maxheap, -val) if len(maxheap) < len(minheap) else heapq.heappush(minheap, val)

        if len(maxheap) > len(minheap):
            median = -maxheap[0]
        elif len(maxheap) < len(minheap):
            median = minheap[0]
        else:
            median = (-maxheap[0] + minheap[0]) / 2
        median_list.append(median)
        # print("maxheap = {}\nminheap = {}\nmedian = {}".format(maxheap, minheap, median), end="\n\n")

    return median_list


print(running_median([2, 1, 5, 7, 2, 0, 5]))
