"""
This problem was asked by Microsoft.

You have n fair coins and you flip them all at the same time. Any that come up tails you set aside. The ones that come up heads you flip again. How many rounds do you expect to play before only one coin remains?

Write a function that, given n, returns the number of rounds you'd expect to play until one coin remains.
"""
from random import random


def flip(num_coins: int) -> int:
    """
    :param num_coins: number of coins to flip
    :return: number of heads
    """
    return len(list(filter(lambda x: random() > 0.5, range(num_coins))))


def simulate_coin_flips(num_simulations: int, num_coins: int) -> int:
    """
    :param num_simulations:
    :param num_coins:
    :return: number of rounds
    """
    simulation_results = []
    for _ in range(num_simulations):
        remaining_coins = num_coins
        current_round = 0
        while remaining_coins > 1:
            current_round += 1
            remaining_coins = flip(remaining_coins)
        simulation_results.append(current_round)

    return sum(simulation_results) // num_simulations


if __name__ == "__main__":
    print(simulate_coin_flips(10 ** 4, 1000))
