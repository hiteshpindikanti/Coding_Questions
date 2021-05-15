"""
This problem was asked by Jane Street.

Suppose you are given a table of currency exchange rates, represented as a 2D array. Determine whether there is a possible arbitrage: that is, whether there is some sequence of trades you can make, starting with some amount A of any currency, so that you can end up with some amount greater than A of that currency.

There are no transaction costs and you can trade fractional quantities.
"""
from collections import defaultdict


def has_arbitrage(exchange_rates: list) -> bool:
    # Run DFS
    visited = defaultdict(int)
    stack = [(0, 1)]
    while stack:
        node, value = stack.pop(-1)
        visited[node] = value
        for adjacent_node in range(len(exchange_rates)):

            if adjacent_node != node:
                new_value = value * exchange_rates[node][adjacent_node]
                if visited[adjacent_node]:

                    if abs(visited[adjacent_node] - new_value) > 0.0001:
                        return True
                else:
                    stack.append((adjacent_node, new_value))
    return False


# import heapq
#
#
# def check_arbitrage(exchange_rates: list) -> bool:
#     # Modified Dijkstra
#     max_distance = {i: float('-inf') for i in range(len(exchange_rates))}
#     source = 0
#     target = 0
#     visited = [False] * len(exchange_rates)
#     max_distance[source] = 1
#     pq = []
#     heapq.heapify(pq)
#     heapq.heappush(pq, (-max_distance[source], source))
#
#     while pq:
#         print("pq: {}".format(pq))
#         distance, v = heapq.heappop(pq)
#         max_distance[v] = max(-distance, max_distance[v])
#         for adj_v in range(len(exchange_rates)):
#             if adj_v != v and max_distance[adj_v] < abs(distance * exchange_rates[v][adj_v]):
#                 heapq.heappush(pq, (-abs(distance * exchange_rates[v][adj_v]), adj_v))
#
#     print(max_distance)
#     if max_distance[source] > 1:
#         return True
#     return False
#
#
currency_rates = [[1, 1.5, 0.4],
                  [2, 1, 1.4],
                  [2, 0.7, 1]]

currency_rates = [[1, 1.5, 0.4],
                  [1 / 1.5, 1, 1.4],
                  [1 / 0.4, 1 / 1.4, 1]]
print(has_arbitrage(currency_rates))
