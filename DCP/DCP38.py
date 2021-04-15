from copy import deepcopy


def n_qeens(n: int, row: int = 0, restriction: list = None) -> set:
    if row == n:
        return set()
    if restriction is None:
        restriction = [set() for _ in range(n)]
    for col in range(n):

        if col not in restriction[row]:
            restriction_copy = deepcopy(restriction)
            for i in range(row + 1, n):
                restriction_copy[i].add(col)
                if col + (i-row) < n:
                    restriction_copy[i].add(col + i-row)
                if col - (i-row) > 0:
                    restriction_copy[i].add(col - (i-row))

            arrangement = n_qeens(n, row + 1, restriction_copy)
            if None not in arrangement:
                arrangement.add((row, col))
                return arrangement

    return {None}


print(n_qeens(15))
