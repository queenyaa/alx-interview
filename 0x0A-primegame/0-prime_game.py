#!/usr/bin/python3
""" Prime Game between two players, given a set of
consecutive integers starting from 1 to n.
"""


def sieve_of_eratosthenes(max_num):
    """ Generate a list indicating prime status up to max_num. """
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers
    p = 2
    while p * p <= max_num:
        if sieve[p]:
            for i in range(p * p, max_num + 1, p):
                sieve[i] = False
        p += 1
    return sieve


def count_primes_up_to(sieve, max_num):
    """ Count the number of primes up to each number in the range. """
    prime_count = [0] * (max_num + 1)
    count = 0
    for i in range(max_num + 1):
        if sieve[i]:
            count += 1
        prime_count[i] = count
    return prime_count


def isWinner(x, nums):
    """ Determines the winner of the Prime Game. """
    if not nums or x < 1:
        return None

    max_num = max(nums)
    sieve = sieve_of_eratosthenes(max_num)
    prime_count = count_primes_up_to(sieve, max_num)

    maria_wins = 0
    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1

    if maria_wins * 2 == len(nums):
        return None
    elif maria_wins * 2 > len(nums):
        return "Maria"
    else:
        return "Ben"
