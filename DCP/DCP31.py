def edit_distance(s1, s2) -> int:
    distance = len(s1) - len(s2)
    if len(s2) == 0:
        return distance

    possible_distances = []
    if s1[0] == s2[0]:
        possible_distances.append(edit_distance(s1[1:], s2[1:]))
    else:
        possible_distances.append(1 + edit_distance(s1[1:], s2[1:]))
        if len(s1) > len(s2):
            possible_distances.append(1 + edit_distance(s1[1:], s2))

    return min(possible_distances)


print(edit_distance("sitting", "kitten"))
