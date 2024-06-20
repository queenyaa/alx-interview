#!/usr/bin/python3

"""
Prime Game between two players, given a set of
consecutive integers starting from 1 to n.
"""


def sieve_of_eratosthenes(max_num):
    """Eratosthenes sieve.

    Args:
        max_num (int): maximum number

    Returns:
        list: list of prime numbers
    """
    is_prime = [True] * (max_num + 1)
    is_prime[0], is_prime[1] = False, False  # 0 and 1 are not prime numbers
    p = 2
    while p * p <= max_num:
        if is_prime[p]:
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p, prime in enumerate(is_prime) if prime]

def isWinner(x, nums):
    """
    Determines if the second player will win.

    Args:
        x (int): number of rounds
        nums (list): list of consecutive integers
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)
    memo = {}

    def game_winner(n):
        """
        Determines if the second player will win.

        Args:
            n (int): number

        Returns:
            str: Maria or Ben
        """
        if n == 1:
            return "Ben"
        if n in memo:
            return memo[n]

        remaining_numbers = set(range(1, n + 1))
        available_primes = [p for p in primes if p <= n]
        turns = 0

        while available_primes:
            turns += 1
            current_prime = available_primes.pop(0)
            multiples = set(range(current_prime, n + 1, current_prime))
            remaining_numbers -= multiples
            available_primes = [p for p in available_primes if p in remaining_numbers]

        winner = "Maria" if turns % 2 == 1 else "Ben"
        memo[n] = winner
        return winner

    maria_wins, ben_wins = 0, 0

    for n in nums:
        winner = game_winner(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
