"""
Binary Search (Dvide and conquer)

This requires the array to be sorted

"""


def binary_search(arr, target):
    """
    returns index if target was found
    return -1 if no found
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if target > mid:
            left = mid + 1
        elif target < mid:
            right = mid - 1
        else:
            return mid
    return -1


print(binary_search([1, 3, 3, 4, 5, 6, 7, 8, 9], 8))
