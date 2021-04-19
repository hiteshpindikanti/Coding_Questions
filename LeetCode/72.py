"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
"""
import heapq


def edit_distance(word1: str, word2: str) -> int:
    if len(word1) < len(word2):
        word1, word2 = word2, word1
    pq = [(0, -0, -0, len(word1) - len(word2))]
    heapq.heapify(pq)
    while pq:
        # print(pq)
        distance, i, j, diff = heapq.heappop(pq)
        i = abs(i)
        j = abs(j)
        # print("HEAP MIN: {}".format((distance, i, j, diff)))

        if i == len(word1) and j == len(word2) and diff == 0:
            return distance

        elif (i == len(word1) or j == len(word2)) and diff == 0:
            continue

        heapq.heappush(pq, (distance + 1, (-(i + 1) if i < len(word1) else -i),
                            (-(j + 1) if j < len(word2) else -j), diff))
        heapq.heappush(pq, (distance + 1, (-(i + 1) if i < len(word1) else -i), -j, diff - 1))
        # print("Pushed: {}".format(((distance + 1,(-(i + 1) if i<len(word1) else -i), -j, diff - 1))))
        if i < len(word1) and j < len(word2) and word1[i] == word2[j]:
            heapq.heappush(pq, (distance, -(i + 1), -(j + 1), diff))
        if diff < len(word1):
            heapq.heappush(pq, ((distance + 1), -i, -(j + 1), diff + 1))


print(edit_distance("horse", "ros"))
print(edit_distance("execution", "intention"))
print(edit_distance("trinitrophenylmethylnitramine", "dinitrophenylhydrazine"))
