"""
Dynamic Programming

get the Fibonacci number
"""


def brute_force(n):
    """
    Calculates the n fibonacci number
    brute force
    """
    if n <= 1:
        return n

    return brute_force(n-1) + brute_force(n-2)


print("Brute force: ", brute_force(10))


def memoization(n, cache):
    """
    Calculates the n fibonacci number with memoization
    top to bottom
    """
    if n <= 1:
        return n
    if n in cache:
        return cache[n]

    cache[n] = memoization(n - 1, cache) + memoization(n - 2, cache)
    print(cache)
    return cache[n]


print("Memoization: ", memoization(10, {}))


def dynamic_programming(n):
    """
    Calculates the n fibonacci number
    bottom to top
    """
    if n <= 2:
        return n

    dp = [0, 1]
    i = 2
    while i <= n:
        tmp = dp[1]
        dp[1] = dp[0] + dp[1]
        dp[0] = tmp
        i += 1
    return dp[1]


print("Dynamic programming: ", dynamic_programming(10))
