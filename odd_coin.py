"""
Q1)
You have n coins with identical weight, except one which weighs a little less.
You are given a weighing scale, which can compare two sets of coins:

def scale(coin_set1: list, coin_set2: list) -> int:
     # returns 0 if both sets are equal
     # returns -1 if coin_set1 is less
     # returns 1 if coin_set1 is more

Write a program to determine the index of odd coin.

Follow-up question,
What if the odd coin can weigh more or less than the other coins, how can this coin be determined?
"""


def scale(coin_set1: list, coin_set2: list) -> int:
    coin_set1_weight = sum(coin_set1)
    coin_set2_weight = sum(coin_set2)
    if coin_set1_weight < coin_set2_weight:
        return -1
    elif coin_set1_weight > coin_set2_weight:
        return 1
    else:
        return 0


def get_odd_coin_index(coins: list) -> int:
    if len(coins) & 1:
        coins.pop(-1)
    mid_index = len(coins) // 2
    scale_reading = scale(coins[:mid_index], coins[mid_index:])
    if scale_reading == -1:
        odd_coin_index = get_odd_coin_index(coins[:mid_index])
    elif scale_reading == 1:
        odd_coin_index = mid_index + get_odd_coin_index(coins[mid_index:])
    else:
        odd_coin_index = len(coins)
    return odd_coin_index


if __name__ == "__main__":
    print(get_odd_coin_index([2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2]))
