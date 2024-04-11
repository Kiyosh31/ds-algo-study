"""
Given an array, colors, which contains a combination 
of the following three elements:

0 (representing red)
1 (representing white)
2 (representing blue)

Sort the array in place so that the elements of the same color are adjacent, 
with the colors in the order of red, white, and blue. 
To improve your problem-solving skills, 
do not utilize the built-in sort function.
"""


def sort_colors(colors):
    """Return an array of sorted numbers"""
    start = 0
    current = 0
    end = len(colors) - 1

    if colors[current] == 0:
        aux = colors[current]
        colors[current] = colors[start]
        colors[start] = aux
    elif colors[current] == 1:
        current += 1
    else:
        aux = colors[current]
        colors[current] = colors[end]
        colors[end] = aux
