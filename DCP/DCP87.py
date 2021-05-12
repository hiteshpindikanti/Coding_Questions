"""
This problem was asked by Uber.

A rule looks like this:

A NE B

This means this means point A is located northeast of point B.

A SW C

means that point A is southwest of C.

Given a list of rules, check if the sum of the rules validate. For example:

A N B
B NE C
C N A
does not validate, since A cannot be both north and south of C.

A NW B
A N B
is considered valid.
"""
from collections import defaultdict


def get_opposite_direction(direction: str) -> str:
    opposite_direction = []
    for ch in direction:
        if ch == "N":
            opposite_direction.append("S")
        elif ch == "S":
            opposite_direction.append("N")
        elif ch == "E":
            opposite_direction.append("W")
        elif ch == "W":
            opposite_direction.append("E")
    return ''.join(opposite_direction)


def add_to_area_map(area_map: defaultdict, source: str, destination: str, direction: str):
    area_map[source][direction].add(destination)
    opposite_direction = get_opposite_direction(direction)
    location_set = set()
    if direction == "NE":
        location_set.update(area_map[destination]["N"]
                            .union(area_map[destination]["NE"])
                            .union(area_map[destination]["E"]))
    elif direction == "N":
        location_set.update(area_map[destination]["N"])
    elif direction == "NW":
        location_set.update(area_map[destination]["N"]
                            .union(area_map[destination]["NW"])
                            .union(area_map[destination]["W"]))
    elif direction == "W":
        location_set.update(area_map[destination]["W"])
    elif direction == "SW":
        location_set.update(area_map[destination]["S"]
                            .union(area_map[destination]["SW"])
                            .union(area_map[destination]["W"]))
    elif direction == "S":
        location_set.update(area_map[destination]["S"])
    elif direction == "SE":
        location_set.update(area_map[destination]["S"]
                            .union(area_map[destination]["SE"])
                            .union(area_map[destination]["E"]))
    elif direction == "E":
        location_set.update(area_map[destination]["E"])

    area_map[source][direction].update(location_set)
    for location in location_set:
        area_map[location][opposite_direction].add(source)


def validate(rules: list) -> bool:
    area_map = defaultdict(lambda: {"N": set(), "S": set(), "E": set(), "W": set(),
                                    "NW": set(), "NE": set(), "SE": set(), "SW": set()})
    for rule in rules:
        destination, direction, source = rule.split(' ')
        print("RULE: {}".format(rule))

        for key, value in area_map[source].items():
            if destination in value:
                if key != direction:
                    return False
                else:
                    break
        else:
            opposite_direction = get_opposite_direction(direction)
            for key, value in area_map[destination].items():
                if source in value:
                    if key != opposite_direction:
                        return False
                    else:
                        break
            else:
                add_to_area_map(area_map, source, destination, direction)
                add_to_area_map(area_map, destination, source, opposite_direction)

        for key, value in dict(area_map).items():
            print("{}: {}".format(key, value))
        print()
    return True


print(validate(['A N B', 'B NE C', 'C N A']))
