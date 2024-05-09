# Overview

This algorithm is effective to found elements in and already `ordered array` why is it better than linear search? because this algorithm use `divide and conquer` this means we're searching in ranges, let's say we have an array like [1,3,3,4,5,6,7,8] and a target of 5, we will create `2 pointers` left and right one to the beginning of the array and another at the end, in base of that we calculate the `mid` element and compare if mid is equal to the target we found it! but if its `greater` we know the next search is on the right side of the array, and if its `lower` is on the left side of the array
move pointers and compare again, until you found your target

# Big(O)

| Time Complexity | Space Complexity |
| --------------- | ---------------- |
| O(logn)         | O(1)             |
