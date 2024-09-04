"""
Sliding window fixed

Q: Given an array, return true if there are two elements within a window 
of size k that are equal

[1,2,3,2,3,3]
"""


def close_duplicates_brute_force(nums, k):
    """O(n * k)"""
    for L in range(len(nums)):
        for R in range(L+1, min(len(nums), L + k)):
            if nums[L] == nums[R]:
                return True
    return False


def close_duplicates(nums, k):
    """O(n)"""
    window = set()
    L = 0

    for R in range(len(nums)):
        if R - L + 1 > k:
            window.remove(nums[L])
            L += 1
        if nums[R] in window:
            return True
        window.add(nums[R])

    return False


# True
print(close_duplicates([1, 2, 3, 2, 3, 3], 2))

# False
print(close_duplicates([1, 2, 3, 2, 3, 2], 2))
