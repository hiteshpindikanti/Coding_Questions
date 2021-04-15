"""
Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.
"""


def max_profit(stock_prices: list) -> int:
    current_val = stock_prices[0]
    for i in range(len(stock_prices)):
        current_val, stock_prices[i] = min(stock_prices[i], current_val), stock_prices[i]-current_val
    return max(stock_prices)


print(max_profit([9, 11, 8, 5, 7, 10]))