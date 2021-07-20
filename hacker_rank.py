from collections import defaultdict


def getUnallottedUsers(bids: list[list], totalShares: int) -> list[int]:
    notAllottedSet = set(map(lambda x: x[0], bids))
    # Reorder
    bidsReordered = list(map(lambda x: [x[2], -x[3], x[1], x[0]], bids))
    bidsReordered.sort(reverse=True)
    start = 0
    while start < len(bidsReordered) and totalShares > 0:
        end = start
        fulfilledBidderIndex = set()
        while end + 1 < len(bidsReordered) and bidsReordered[end][0] == bidsReordered[end + 1][0]:
            if bidsReordered[end][2] == float('inf'):
                fulfilledBidderIndex.add(end)
            end += 1
        minShares = min(map(lambda x: x[2], bidsReordered[start: end + 1]))

        if minShares * (end + 1 - start - len(fulfilledBidderIndex)) < totalShares:
            for i in range(start, end + 1):
                if bidsReordered[i][2] != float('inf'):
                    bidsReordered[i][2] -= minShares
                    totalShares -= minShares
                    if bidsReordered[i][-1] in notAllottedSet:
                        notAllottedSet.remove(bidsReordered[i][-1])
                    if bidsReordered[i][2] == 0:
                        bidsReordered[i][2] = float('inf')
                        fulfilledBidderIndex.add(i)
        else:
            givenShares = totalShares // (end + 1 - start)
            if givenShares:
                for i in range(start, end + 1):
                    bidsReordered[i][2] -= givenShares
                    if bidsReordered[i][-1] in notAllottedSet:
                        notAllottedSet.remove(bidsReordered[i][-1])
                totalShares -= givenShares
            for i in range(start, start + totalShares + 1):
                if totalShares == 0:
                    break
                bidsReordered[i][2] -= 1
                totalShares -= 1
                if bidsReordered[i][-1] in notAllottedSet:
                    notAllottedSet.remove(bidsReordered[i][-1])
        while bidsReordered[start][2] == float('inf'):
            start += 1

    return sorted(notAllottedSet)


if __name__ == "__main__":
    print(getUnallottedUsers([[1, 5, 5, 0], [2, 7, 8, 1], [3, 7, 5, 1], [4, 10, 3, 3]], 18))  # [4]
    print(getUnallottedUsers([[1, 5, 5, 0], [2, 7, 8, 1], [3, 7, 5, 1], [4, 10, 3, 3]], 20))  # []
    print(getUnallottedUsers([[1, 2, 5, 0], [2, 1, 4, 2], [3, 5, 4, 6]], 3)) # [3]
