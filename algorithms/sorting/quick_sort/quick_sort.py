"""Quicksort"""


def quick_sort(arr, start, end):
    """returns array ordered"""
    if end - start + 1 <= 1:
        return

    pivot = arr[end]
    left = start

    # Partition: elements smaller than privot on left side
    for i in range(start, end):
        if arr[i] < pivot:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1

    # Move pivot in-between left & right sides
    arr[end] = arr[left]
    arr[left] = pivot

    # Quicksort left side
    quick_sort(arr, start, left - 1)

    # Quicksort right side
    quick_sort(arr, start + 1, end)

    return arr


test = [6, 2, 4, 1, 3]
print(quick_sort(test, 0, len(test) - 1))
