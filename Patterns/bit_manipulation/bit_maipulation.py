"""
Bit Manipulation
"""
# AND
N = 1 & 1

# OR
N = 1 | 0

# XOR
N = 0 ^ 1

# Not (negation)
N = ~N

# Bit Shifting
N = 1
N = N << 1
N = N >> 1


def count_bits(n):
    """Counting Bits"""
    count = 0
    while n > 0:
        if n & 1 == 1:
            count += 1
        n = n >> 1  # same as n // 2
    return count


print(count_bits(10))
print(count_bits(10_000_000))
