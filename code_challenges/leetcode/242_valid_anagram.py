"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of 
a different word or phrase, typically using all the original letters 
exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""

# Two possible solutions here
# 1. Hash table
# 2. Sort the strings


def is_anagram_ht(s, t):
    """hash table solution"""
    if len(s) != len(t):
        return False

    dict1 = {}
    dict2 = {}

    for letter in enumerate(s):
        if letter in dict1:
            dict1[letter] += 1
        else:
            dict1[letter] = 1

    for letter in enumerate(t):
        if letter in dict2:
            dict2[letter] += 1
        else:
            dict2[letter] = 1

    return dict1 == dict2


def is_anagram_sr(s, t):
    """Sorting solution"""
    return sorted(s) == sorted(t)
