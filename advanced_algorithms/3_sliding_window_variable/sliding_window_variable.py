"""
Sliding window variable size

Q: Find the length of the longest subarray, with the same value in each
position
input: [4,2,2,3,3,3]
output: 3
"""


def longest_aubarray(nums):
    """O(n)"""
    length = 0
    L = 0

    for R in range(len(nums)):
        if nums[R] != nums[L]:
            L = R
        length = max(length, R - L + 1)
    return length


# 3
print(longest_aubarray([4, 2, 2, 3, 3, 3]))


"""
Q: find the minimum length subarray, where the sum is greater than or equal
to the target. Assume all values are positive.

input: [2,3,1,2,4,3] target = 6
output: 
"""


def shortest_subarray(nums, target):
    """O(n)"""
    L, total = 0, 0
    length = float("inf")

    for R in range(len(nums)):
        total += nums[R]
        while total >= target:
            length = min(R - L + 1, length)
            total -= nums[L]
            L += 1
    return 0 if length == float("inf") else length


# 2
print(shortest_subarray([2, 3, 1, 2, 4, 3], 6))
