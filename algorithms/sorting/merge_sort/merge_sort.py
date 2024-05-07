"""Merge sort"""


def merge_sort(arr, start, end):
    """returns an ordered array"""
    if end - start + 1 <= 1:
        return arr

    # The middle index of array
    middle = (start + end)//2

    # Sort the left half
    merge_sort(arr, start, end)

    # Sort the right half
    merge_sort(arr, middle + 1, end)

    # Merge sorted halfs
    merge(arr, start, middle, end)

    return arr


def merge(arr, start, middle, end):
    """merge left and right"""
    left = arr[start: middle + 1]
    right = arr[middle + 1: end + 1]

    i = 0     # index of left
    j = 0     # index for right
    k = start  # index of arr

    # Merge the two sorted halfs into the original array
    while i < len(arr) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # One of the halfs will have elements remaining
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


example = [3, 2, 4, 1, 6]
print(merge_sort(example, example[0], len(example)))
