"""
Factorial

Calculate the factorial of a num n
"""

# One-Branch
# n! = n * (n - 1)


def factorial(n):
    """it returns the factorial of n"""

    # This if is important since this is the stop condition,
    # without this the code would run infinitely
    # s when n = 1 the calculation wont be executed since
    # is not needed anymore
    if n <= 1:
        return n

    return n * factorial(n-1)


print(factorial(5))
