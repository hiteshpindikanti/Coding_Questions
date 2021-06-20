"""
This problem was asked by Facebook.

Given an array of numbers representing the stock prices of a company in chronological order and an integer k, return the maximum profit you can make from k buys and sells. You must buy the stock before you can sell it, and you must sell the stock before you can buy it again.

For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.
"""
import heapq


def get_max_profit(stock_prices: list[float], num_transactions: int) -> float:
    i = 0
    profit_transactions = set()
    while i < len(stock_prices) - 1:  # O(n)
        buy_index = i
        while i < len(stock_prices) - 1 and stock_prices[i] < stock_prices[i + 1]:
            i += 1
        sell_index = i

        profit_transactions.add(stock_prices[sell_index] - stock_prices[buy_index])
        i += 1

    profit_transactions_list = list(profit_transactions)  # O(n)
    heapq.heapify(profit_transactions_list)  # O(n)
    max_profit = sum(heapq.nlargest(num_transactions, profit_transactions_list))  # O(k.log(n))
    return max_profit


if __name__ == "__main__":
    print(get_max_profit([5, 2, 4, 0, 1], 2))
