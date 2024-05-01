"""
Given an array where the element at the index i represents 
the price of a stock on day i, find the maximum profit that 
you can gain by buying the stock once and then selling it.

Example #1
Input: [7,1,5,3,6,4]
Output: 5

Example #2
Input: [10,8,6,4,2]
Output: 0
"""


def max_profit(prices):
    """
    Return profit or 0
    """
    buy, sell = 0, 1
    max_p = 0

    while sell < len(prices):
        if prices[buy] < prices[sell]:
            profit = prices[sell] - prices[buy]
            max_p = max(max_p, profit)
        else:
            buy = sell
        sell += 1
    return max_p
