"""
Given an array of integers, nums, and an integer value, target, 
determine if there are any three integers in nums whose sum is equal
to the target, that is, nums[i] + nums[j] + nums[k] == target. 

Return TRUE if three such integers exist in the array. 
Otherwise, return FALSE.
"""


def find_sum_of_three(nums, target):
    """Return true/false if the sum of three numbers match target"""
    nums.sort()
    print(nums)

    for i in range(0, len(nums)-2):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            triplet = nums[i] + nums[left] + nums[right]

            if triplet == target:
                return True
            elif triplet < target:
                left += 1
            else:
                right -= 1
    return False


print(find_sum_of_three([3, 7, 1, 2, 8, 4, 5], 10))
