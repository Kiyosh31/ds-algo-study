"""
Given an integer array nums, return true if any value appears 
at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""


def contains_duplicate(nums):
    """Returns True/False if array contains duplicates"""
    seen = set()

    for _, num in enumerate(nums):
        if num in seen:
            return True
        else:
            seen.add(num)
    return False
