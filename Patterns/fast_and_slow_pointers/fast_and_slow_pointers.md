# Fast and slow pointers

Similar to the two pointers pattern, the fast and slow pointers pattern uses two pointers to traverse an iterable data structure, but at different speeds, often to identify patterns, detect cycles, or find specific elements. The speeds of the two pointers can be adjusted according to the problem statement. Unlike the two pointers approach, which is concerned with data values, the fast and slow pointers approach is often used to determine specific pattern or structure in the data.

The key idea is that `the pointers start at the same location` and then start moving at `different speeds`. Generally, the `slow pointer moves` forward by a `factor of one`, and the `fast pointer moves` by a `factor of two`. This approach enables the algorithm to detect patterns or properties within the data structure, such as cycles or intersections. If there is a cycle, the two are bound to meet at some point during the traversal. To understand the concept, think of two runners on a track. While they start from the same point, they have different running speeds. If the track is circular, the faster runner will overtake the slower one after completing a lap.

# Does your problem match this pattern?

Yes, if the following condition is fulfilled:

- `Linear data structure`: The input data can be traversed in a linear fashion, such as an array, linked list, or string.

In addition, if either of these conditions is fulfilled:

- `Cycle or intersection detection`: The problem involves detecting a loop within a linked list or an array or involves finding an intersection between two linked lists or arrays.

- `Find the starting element at the second quantile`: The problem involves finding the starting element of the second quantile, i.e., second half, second tertile, second quartile, etc. For example, the problem asks to find the middle element of an array or a linked list.
