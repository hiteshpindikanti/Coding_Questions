"""
Find the minimum number of coins required to make n cents.

You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.

For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.
"""
from collections import defaultdict

DENOMINATIONS = [1, 5, 10, 25]
memo = defaultdict(lambda: -1)
memo[0] = 0


def get_min_req_coins(amount: int) -> int:
    if amount in memo:
        return memo[amount]
    min_req_coins = float('inf')
    for coin in DENOMINATIONS:
        if amount >= coin:
            num_coins = 1 + get_min_req_coins(amount - coin)
            min_req_coins = min(min_req_coins, num_coins)
    memo[amount] = min_req_coins
    return memo[amount]


if __name__ == "__main__":
    print(get_min_req_coins(16))
