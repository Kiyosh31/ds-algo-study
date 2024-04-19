"""
Given an integer list, nums, find the maximum values in all 
the contiguous subarrays (windows) of size w.

Example #1:
Input: nums = [1,2,3,4,5,6,7,8,9,10], w = 3
Output: 

Example #2:
Input: nums = [3,3,3,3,3,3,3,3,3,3], w = 4
Output: 

Example #3:
Input: nums = [10,6,9,-3,23,-1,34,56,67,-1,-4,-8,-2,9,10,34,67], w = 3
Output: 
"""


def find_max_sliding_window(nums, w):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    if len(nums) == 1:
        return nums

    res = []

    for left in range(len(nums) - w + 1):
        window = nums[left: left + w]
        max_num = max(window)
        res.append(max_num)

    return res
