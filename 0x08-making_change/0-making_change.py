#!/usr/bin/python3

"""
function to calculate the fewest number of coins
needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    function to calculate the fewest number of coins
    needed to meet a given amount total
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1
    if total > 0:
        return -1
    return count
