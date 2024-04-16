"""
Given an array, colors, which contains a combination of the following 
three elements:

- 0 (representing red)
- 1(representing white)
- 2 (representing blue)

Sort the array in place so that the elements of the same color are adjacent, w
ith the colors in the order of red, white, and blue. 
To improve your problem-solving skills, do not utilize the built-in 
sort function.
"""


def sort_colors(colors):
    """Return colors in asc order"""
    start = 0
    end = len(colors) - 1
    current = 0

    while current <= end:
        if colors[current] == 0:
            if colors[start] != 0:
                colors[start], colors[current] = colors[current], colors[start]
            current += 1
            start += 1
        if colors[current] == 1:
            current += 1
        else:
            if colors[end] != 2:
                colors[current], colors[end] = colors[end], colors[current]
            end -= 1
    return colors
