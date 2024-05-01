"""
Given an array of positive integers, nums, and a positive integer, 
target, find the minimum length of a contiguous subarray whose sum 
is greater than or equal to the target. If no such subarray is found, 
return 0.

Example #1
Input: [1,1,1,1,1,3], t = 11
Output: 0

Example #2
Input: [2,3,1,2,4,3], t = 7
Output: 2
"""


def min_sub_array_len(target, nums):
    """
    returns the min sub array of nums or 0
    """
    left, total = 0, 0
    res = float("inf")

    for right in range(len(nums)):
        total += nums[right]
        while total >= target:
            res = min(right - left + 1, res)
            total -= nums[left]
            left += 1
    return 0 if res == float("inf") else res
