"""
This problem was asked by Yelp.

Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the number could represent. You can assume each valid number in the mapping is a single digit.

For example if {“2": [“a", “b", “c"], 3: [“d", “e", “f"], …} then “23" should return [“ad", “ae", “af", “bd", “be", “bf", “cd", “ce", “cf"].
"""


def get_all_possibilities(mapping: dict, msg: str) -> list:
    msgs_list = []
    stack = [(mapping[msg[0]], msg[1:])]
    while stack:
        current_list, msg = stack.pop(-1)
        if msg:
            new_list = []
            for val in mapping[msg[0]]:
                new_list.extend(map(lambda x: x + val, current_list))
            stack.append((new_list, msg[1:]))
        else:
            msgs_list.extend(current_list)

    return msgs_list


print(get_all_possibilities({"2": ["a", "b", "c"], "3": ["d", "e", "f"]}, "23"))
