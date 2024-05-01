"""
Given two strings, str1 and str2, find the shortest substring in 
str1 such that str2 is a subsequence of that substring.
A substring is defined as a contiguous sequence of characters
within a string. A subsequence is a sequence that can be derived 
from another sequence by deleting zero or more elements without 
changing the order of the remaining elements.

Lets say you have the following two strings:
str1 = "abbcb"
str2 = "ac"

In this example, "abbc" is a substring of str1, from which we 
can derive str2 simply by deleting both the nstances of the character  b.
Therefore, str2 is a subsequence of this substring. Since this 
substring is the shortest among all the substrings in which str2 is 
present as a subsequence, the function should return this substring, 
that is, "abbc".
"""


def min_window(str1, str2):
    """

    """
