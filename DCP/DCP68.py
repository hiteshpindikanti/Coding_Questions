"""
This problem was asked by Google.

On our special chessboard, two bishops attack each other if they share the same diagonal. This includes bishops that have another bishop located between them, i.e. bishops can attack through pieces.

You are given N bishops, represented as (row, column) tuples on a M by M chessboard. Write a function to count the number of pairs of bishops that attack each other. The ordering of the pair doesn't matter: (1, 2) is considered the same as (2, 1).

For example, given M = 5 and the list of bishops:

(0, 0)
(1, 2)
(2, 2)
(4, 0)
The board would look like this:

[b 0 0 0 0]
[0 0 b 0 0]
[0 0 b 0 0]
[0 0 0 0 0]
[b 0 0 0 0]
You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.
"""


def is_diagonal(coordinate1, coordinate2) -> bool:
    x1, y1 = coordinate1
    x2, y2 = coordinate2
    return abs(x1 - x2) == abs(y1 - y2)


def count_attacks(bishops: list, m: int) -> int:
    visited = set()
    count = 0
    for bishop1 in bishops:
        for bishop2 in bishops:
            attack = frozenset([bishop2, bishop1])
            if bishop1 != bishop2 and attack not in visited and \
                    abs(bishop2[0] - bishop1[0]) == abs(bishop2[1] - bishop1[1]):
                visited.add(attack)
                count += 1
    return count


l = [(0, 0), (1, 2), (2, 2), (4, 0)]
print(count_attacks(l, 5))
