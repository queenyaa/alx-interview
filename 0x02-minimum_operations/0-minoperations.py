#!/usr/bin/python3
"""
Function to calculate the fewest number of operations
needed to result inexactly n H characters by
utilizing prime factorization.
"""


def minOperations(n):
    """
    Returns the fewest number of operations needed to achieve
    n H characters. If it's impossible to achieve n H characters,
    returns 0.

    Args:
        n (int): number of characters required
    """
    # Initialize the total number of operations
    operations = 0
    # Start with the smallest prime factor
    smallest_prime = 2

    # Continue the loop until n becomes 1
    while n > 1:
        # Check if n is divisible by the smallest prime factor
        while n % smallest_prime == 0:
            # Increment operations by the smallest prime factor
            operations += smallest_prime
            # Divide n by the smallest prime factor
            n //= smallest_prime
        # Move to the next prime factor
        smallest_prime += 1

    return operations
