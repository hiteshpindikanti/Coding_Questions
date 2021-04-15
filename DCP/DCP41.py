from collections import defaultdict


def get_itinerary(flights: set, start: str) -> list:
    graph = defaultdict(list)
    locations = set()
    for source, target in flights:
        graph[source].append(target)
        locations.update({source, target})

    for key in graph.keys():
        graph[key].sort()

    # DFS
    stack = [start]
    visited = set()
    itinerary = []
    while stack:
        u = stack.pop(-1)
        itinerary.append(u)
        for v in graph[u]:
            if (u, v) not in visited:
                stack.append(v)
                visited.add((u, v))
                break
    if len(visited) == len(flights):
        return itinerary
    else:
        return [None]


print(get_itinerary(flights={('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')}, start='YUL'))
# ANSWER: ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']

print(get_itinerary(flights={('SFO', 'COM'), ('COM', 'YYZ')}, start='COM'))
# ANSWER: [None]

print(get_itinerary(flights={('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')}, start='A'))
# ANSWER: ['A', 'B', 'C', 'A', 'C']
