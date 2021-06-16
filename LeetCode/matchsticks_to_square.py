from collections import Counter
from copy import deepcopy


def can_make_square(matchsticks: list[int]) -> bool:
    square_side_length = sum(matchsticks) / 4
    if len(matchsticks) < 4 or max(matchsticks) > square_side_length:
        return False
    matchsticks = Counter(matchsticks)
    stack = [(0, matchsticks)]
    while stack:
        current_sum, remaining_matchsticks = stack.pop()
        print(f'current_sum = {current_sum}, remaining_matchsticks = {remaining_matchsticks}')
        if current_sum == square_side_length:
            if not remaining_matchsticks:
                return True
            else:
                stack.append((0, remaining_matchsticks))
        else:
            for matchsticks_length in remaining_matchsticks.keys():
                new_remaining_matchsticks = deepcopy(remaining_matchsticks)
                if new_remaining_matchsticks[matchsticks_length] == 1:
                    new_remaining_matchsticks.pop(matchsticks_length)
                else:
                    new_remaining_matchsticks[matchsticks_length] -= 1
                stack.append((current_sum + matchsticks_length, new_remaining_matchsticks))

    return False


memo = {}


def check_sum(matchsticks: dict, side_length, current_sum=0) -> bool:
    if (str(matchsticks), current_sum) in memo.keys():
        return memo[(str(matchsticks), current_sum)]
    else:
        memo[(str(matchsticks), current_sum)] = False
        if current_sum == side_length:
            if not matchsticks:
                memo[(str(matchsticks), current_sum)] = True
            else:
                if check_sum(matchsticks, side_length):
                    memo[(str(matchsticks), current_sum)] = True
        for matchstick_length in matchsticks.keys():
            remaining_matchsticks = deepcopy(matchsticks)
            if remaining_matchsticks[matchstick_length] == 1:
                remaining_matchsticks.pop(matchstick_length)
            else:
                remaining_matchsticks[matchstick_length] -= 1
            if check_sum(remaining_matchsticks, side_length, current_sum + matchstick_length):
                memo[(str(matchsticks), current_sum)] = True
    return memo[(str(matchsticks), current_sum)]


def can_make_square2(matchsticks: list[int]) -> bool:
    square_side_length = sum(matchsticks) / 4
    if len(matchsticks) < 4 or max(matchsticks) > square_side_length:
        return False
    matchsticks = Counter(matchsticks)
    return check_sum(matchsticks, square_side_length)


def get_remaining_combinations(matchsticks: dict, remaining_sum) -> list[dict]:
    remaining_combinations = []
    for matchstick_length in matchsticks.keys():
        remaining_matchsticks = deepcopy(matchsticks)
        if remaining_matchsticks[matchstick_length] == 1:
            remaining_matchsticks.pop(matchstick_length)
        else:
            remaining_matchsticks[matchstick_length] -= 1
        sub_remaining_combinations = get_remaining_combinations(remaining_matchsticks, remaining_sum - matchstick_length)



if __name__ == "__main__":
    print(can_make_square2([1, 1, 2, 2, 2]))  # True
    print(can_make_square2([3, 3, 3, 3, 4]))  # False
    print(can_make_square2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
