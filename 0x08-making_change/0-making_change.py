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

    # Initialize the dp array with a large number representing infinity
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Populate the dp array
    for coin in coins:
        for x in range(coin, total + 1):
            if dp[x - coin] != float('inf'):
                dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
