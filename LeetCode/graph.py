from collections import defaultdict


class Graph:
    def __init__(self, n_vertices: int, is_directed: bool = False):
        self.n_vertices = n_vertices
        self.edges = defaultdict(list)
        self.is_directed = is_directed

    def add_edge(self, v: int, u: int):
        self.edges[v].append(u)
        if not self.is_directed:
            self.edges[u].append(v)

    def bfs(self, node: int) -> list:
        visited: list = [False for i in range(self.n_vertices)]
        queue: list = []
        traversal: list = []

        visited[node] = True
        queue.append(node)

        while len(queue) > 0:
            vertex = queue.pop(0)
            traversal.append(vertex)
            for v in self.edges[vertex]:
                if not visited[v]:
                    queue.append(v)
                    visited[v] = True

        return traversal

    def dfs(self, node: int) -> list:
        visited: list = [False for i in range(self.n_vertices)]
        stack: list = []
        traversal: list = []

        visited[node] = True
        stack.append(node)

        while len(stack) > 0:
            vertex = stack.pop(-1)
            traversal.append(vertex)
            for v in self.edges[vertex]:
                if not visited[v]:
                    stack.append(v)
                    visited[v] = True

        return traversal

    def get_strongly_connected_components(self) -> list:
        strongly_connected_components = []
        main_stack = []

        # First Pass
        visited_count = 0
        visited = [False] * self.n_vertices
        while visited_count < self.n_vertices:
            vertex = visited.index(False)
            visited[vertex] = True
            visited_count += 1
            stack = [vertex]
            pop_order = []
            while stack:
                vertex = stack.pop(-1)
                pop_order.append(vertex)
                for v in self.edges[vertex]:
                    if not visited[v]:
                        stack.append(v)
                        visited[v] = True
                        visited_count += 1
            main_stack.extend(pop_order[::-1])

        # Reverse the edges
        reverse_edges = defaultdict(list)
        for key, value in self.edges.items():
            for v in value:
                reverse_edges[v].append(key)

        # Second Pass
        visited_count = 0
        visited = [False] * self.n_vertices
        while visited_count < self.n_vertices:
            vertex = main_stack.pop(-1)
            while main_stack and visited[vertex]:
                vertex = main_stack.pop(-1)
            visited[vertex] = True
            visited_count += 1
            stack = [vertex]
            pop_order = []
            while stack:
                vertex = stack.pop(-1)
                pop_order.append(vertex)
                for v in reverse_edges[vertex]:
                    if not visited[v]:
                        stack.append(v)
                        visited[v] = True
                        visited_count += 1
            strongly_connected_components.append(pop_order[::-1])
        return strongly_connected_components
