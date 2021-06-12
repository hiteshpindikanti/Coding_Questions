from collections import defaultdict
from collections import Counter
from copy import deepcopy


def get_type_count(obj, count: dict = None) -> dict:
    if count is None:
        count = defaultdict(int)
    count[str(type(obj))] += 1
    if type(obj) != str:
        try:
            for obj_element in obj:
                get_type_count(obj_element, count)
        except TypeError:
            pass
    return count


def get_permutations(string: dict) -> set:
    permutations = set()
    if not string:
        return {''}
    for ch in string.keys():
        new_string = deepcopy(string)
        if new_string[ch] == 1:
            new_string.pop(ch)
        else:
            new_string[ch] -= 1
        permutations.update(set(map(lambda x: ch+x, get_permutations(new_string))))
    return permutations


if __name__ == "__main__":
    custom_object = [1, 1.5, [2, 'hitesh', 2 / 3, (4.0, 5.0, '7'), {(1, 2), (3, 4), 'someStr'}], 5.67, (3,)]
    print(dict(get_type_count(custom_object)))

    print(get_permutations(Counter("aab")))