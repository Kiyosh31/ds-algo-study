"""
Two Pointers

Q: Check if an array is a palindrome.
Input: [1,2,7,7,2,1]
Output: True
"""


def is_palindrome(word):
    """O(n)"""
    left = 0
    right = len(word) - 1

    while left < right:
        if word[left] != word[right]:
            return False

        right -= 1
        left += 1

    return True


# True
print(is_palindrome("anitalavalatina"))


# True
print(is_palindrome([1, 2, 7, 7, 2, 1]))


"""
Q: Given a sorted input array, return, the two indices of the two elements
which sum up to the target value. Assume there's exactly one solution.

Input: [-1,2,3,4,8,9] target = 7
Output: 
"""


def target_sum(nums, target):
    """O(n)"""
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] + nums[right] > target:
            right -= 1
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            return [left, right]


# [0,4]
print(target_sum([-1, 2, 3, 4, 8, 9], 7))
