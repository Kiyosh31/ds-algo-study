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

    for i in range(len(s)):
        dict1[s[i]] = 1 + dict1.get(s[i], 0)
        dict2[t[i]] = 1 + dict2.get(t[i], 0)

    for c in dict2:
        if dict1[c] != dict2.get(c, 0):
            return False

    return True


def is_anagram_sr(s, t):
    """Sorting solution"""
    return sorted(s) == sorted(t)


# True
print(is_anagram_ht("racecar", "carrace"))
print(is_anagram_sr("racecar", "carrace"))
