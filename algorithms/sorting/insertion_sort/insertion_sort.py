"""
Insertion Sort

not the best, used in arryas and linked lists

to solve this proble we need to break the problem into
smaller problems
"""


def insertion_sort(nums):
    """this funcion sorts the array"""
    for i in range(1, len(nums)):
        j = i - 1
        while j >= 0 and nums[j + 1] < nums[j]:
            tmp = nums[j+1]
            nums[j+1] = nums[j]
            nums[j] = tmp
            j -= 1
    return nums


print(insertion_sort([2, 3, 4, 1, 6]))
print(insertion_sort([7, 9, 1, 0, 4, 7, 6, 44]))
