"""
Given an array of integers, nums, and an integer value, target, 
determine if there are any three integers in nums whose sum 
is equal to the target, that is, nums[i] + nums[j] + nums[k] == target. 
Return TRUE if three such integers exist in the array. Otherwise, return FALSE.
"""

"""
- sort array in asc order
- iterate over the entire array
- in each iteration make a triplet by storing the current 
array element and the other two elements using two pointer
and calculate their sum
- adjust the cal sum value, until it becomes equal to the target
by conditionally moving pointers
- return true if required sum is found otherwise return false
"""


def find_sum_of_three(nums, target):
    """O(n^2)"""
    nums.sort()

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


def main():
    """Main"""
    test_cases = [
        {
            "nums": [1, -1, 0],
            "target": -1
        },
        {
            "nums": [3, 7, 1, 2, 8, 4, 5],
            "target": 21
        },
        {
            "nums": [-1, 2, 1, -4, 5, -3],
            "target": -8
        },
        {
            "nums": [-1, 2, 1, -4, 5, -3],
            "target": 0
        },
        {
            "nums": [3, 7, 1, 2, 8, 4, 5],
            "target": 21
        }
    ]

    for i, test in enumerate(test_cases):
        print()
        print("Test Case #", i + 1)
        print("-" * 100)
        print("Nums is '", test["nums"], "' and the target is ",
              test["target"], ".", sep='')
        print("Is it a three sum?.....",
              find_sum_of_three(test["nums"], test["target"]))
        print("-" * 100)


if __name__ == '__main__':
    main()
