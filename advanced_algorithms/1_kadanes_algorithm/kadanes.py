"""
Kadanes algorithm

Q: find a non-empty subarray with the largest sum.
[4,-1,2,-7,3,4]
"""


def brute_force(nums):
    """Brute force: O(n^2)"""
    max_sums = nums[0]

    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i, len(nums)):
            curr_sum += nums[j]
            max_sums = max(max_sums, curr_sum)
    return max_sums


def kadanes(nums):
    """Kadanes algorithm: O(n)"""
    max_sum = 0
    curr_sum = 0

    for num in nums:
        curr_sum = max(max_sum, 0)
        curr_sum += num
        max_sum = max(max_sum, curr_sum)
    return max_sum
