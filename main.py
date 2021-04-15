from graph import Graph

if __name__ == "__main__":
    g = Graph(n_vertices=6, is_directed=False)
    edges_list = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 2]]

    g = Graph(n_vertices=4, is_directed=True)
    edges_list = [[0, 1], [1, 2], [2, 0], [1, 3]]
    for v, u in edges_list:
        g.add_edge(v, u)

    print(g.get_strongly_connected_components())