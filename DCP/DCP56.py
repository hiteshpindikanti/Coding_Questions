"""
This problem was asked by Google.

Given an undirected graph represented as an adjacency matrix and an integer k, write a function to determine whether each vertex in the graph can be colored such that no two adjacent vertices share the same color using at most k colors.
"""
from copy import deepcopy


def is_k_colorable(matrix, k: int) -> bool:
    domain = [{i for i in range(1, k + 1)} for _ in range(len(matrix))]

    # Satisfy Constraints
    for v in range(len(matrix)):
        if len(domain[v]) == 1:
            color_val = next(iter(domain[v]))
            for u, val in enumerate(matrix[v]):
                if val == 1 and color_val in domain[u]:
                    domain[u].remove(color_val)

    stack = [domain]
    while stack:
        domain = stack.pop(-1)

        # Check Status
        status = "SOLVED"
        for v, val in enumerate(domain):
            if len(val) == 0:
                status = "FAIL"
                break
            elif len(val) > 1:
                status = "CONTINUE"

        if status == "SOLVED":
            return True
        elif status == "FAIL":
            continue
        else:
            for v, color_set in enumerate(domain):
                if len(color_set) > 1:
                    for color_val in color_set:
                        domain_copy = deepcopy(domain)
                        domain_copy[v] = {color_val}

                        # Satisfy Constraints
                        for u, val in enumerate(matrix[v]):
                            if val == 1 and color_val in domain_copy[u]:
                                domain_copy[u].remove(color_val)

                        for vertex in range(len(matrix)):
                            if len(domain_copy[vertex]) == 1:
                                color_val = next(iter(domain_copy[vertex]))
                                for u, val in enumerate(matrix[vertex]):
                                    if val == 1 and color_val in domain_copy[u]:
                                        domain_copy[u].remove(color_val)

                        # Add to stack
                        stack.append(domain_copy)

    return False


if __name__ == "__main__":
    mat1 = [[0, 1],
            [1, 0]]
    mat2 = [[0, 1, 1],
            [1, 0, 0],
            [1, 0, 0]]
    mat3 = [[0, 1, 1],
            [1, 0, 1],
            [1, 1, 0]]
    print(is_k_colorable(mat1, 2))
