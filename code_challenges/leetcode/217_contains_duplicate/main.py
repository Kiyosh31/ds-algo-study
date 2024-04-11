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


def main():
    """Main func"""
    test_cases = [
        {
            "input": [1, 2, 3, 1],
            "output": True
        },
        {
            "input": [1, 2, 3, 4],
            "output": False
        },
        {
            "input": [1, 1, 1, 3, 3, 4, 3, 2, 4, 2],
            "output": True
        },
    ]

    for i, test in enumerate(test_cases):
        print()
        print("Test case #", i)
        print("Input: ", test["input"])
        print("Expected: ", test["output"])
        print("Output: ", contains_duplicate(test["input"]))


if __name__ == '__main__':
    main()
