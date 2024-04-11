# Sliding Window

The sliding window pattern is used to process `sequential data`, `arrays`, and `strings`, for example, to efficiently solve `subarray` or `substring` problems. It involves maintaining a dynamic window that slides through the array or string, adjusting its boundaries as needed to track relevant elements or characters. The window is used to slide over the data in chunks corresponding to the window size, and this can be set according to the problem’s requirements. It may be viewed as a variation of the two pointers pattern, with the pointers being used to set the window bounds.

Imagine you’re in a long hallway lined with paintings, and you’re looking through a narrow frame that only reveals a portion of this hallway at any time. As you move the frame along the hallway, new paintings come into view while others leave the frame. This process of moving and adjusting what’s visible through the frame is akin to how the sliding window technique operates over data.

# Does your problem match this pattern?

Yes, if all of these conditions are fulfilled:

- `Contiguous data`: The input data is stored in a contiguous manner, such as an array or string.

- `Processing subsets of elements`: The problem requires repeated computations on a contiguous subset of data elements (a subarray or a substring), such that the window moves across the input array from one end to the other. The size of the window may be fixed or variable, depending on the requirements of the problem.

- `Efficient computation time complexity`: The computations performed every time the window moves take constant or very small time.

Yes, if all of these conditions are fulfilled:

`Contiguous data`: The input data is stored in a contiguous manner, such as an array or string.

`Processing subsets of elements`: The problem requires repeated computations on a contiguous subset of data elements (a subarray or a substring), such that the window moves across the input array from one end to the other. The size of the window may be fixed or variable, depending on the requirements of the problem.

Efficient computation time complexity: The computations performed every time the window moves take constant or very small time.

# Real-world problems

Many problems in the real world use the sliding window pattern. Let’s look at some examples.

`Telecommunications`: Find the maximum number of users connected to a cellular network’s base station in every k-millisecond sliding window.

`Video streaming`: Given a stream of numbers representing the number of buffering events in a given user session, calculate the median number of buffering events in each one-minute interval.

`Social media content mining`: Given the lists of topics that two users have posted about, find the shortest sequence of posts by one user that includes all the topics that the other user has posted about.
