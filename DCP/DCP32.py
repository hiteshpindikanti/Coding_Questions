import heapq


def check_arbitrage(exchange_rates: list) -> bool:
    # Modified Dijkstra
    max_distance = {i: float('-inf') for i in range(len(exchange_rates))}
    source = 0
    target = 0
    visited = [False] * len(exchange_rates)
    max_distance[source] = 1
    pq = []
    heapq.heapify(pq)
    heapq.heappush(pq, (-max_distance[source], source))

    while pq:
        print("pq: {}".format(pq))
        distance, v = heapq.heappop(pq)
        max_distance[v] = max(-distance, max_distance[v])
        for adj_v in range(len(exchange_rates)):
            if adj_v != v and max_distance[adj_v] < abs(distance * exchange_rates[v][adj_v]):
                heapq.heappush(pq, (-abs(distance * exchange_rates[v][adj_v]), adj_v))

    print(max_distance)
    if max_distance[source] > 1:
        return True
    return False


currency_rates = [[1, 1.5, 0.4],
                  [2, 1, 1.4],
                  [2, 0.7, 1]]

print(check_arbitrage(currency_rates))
