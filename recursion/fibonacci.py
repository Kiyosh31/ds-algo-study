"""
Fibonacci

Calculate the fibonacci sequence from n
"""


def fibonacci(n):
    """returns the nth fibonacci number"""
    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(12))
