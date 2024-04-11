"""
Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, 
"pwke" is a subsequence and not a substring. 
"""


def length_of_longest_substring(s):
    """return length of longest substring"""
    seen = set()
    left = 0
    longest_substring = 0

    for right, letter in enumerate(s):
        while letter in seen:
            seen.remove(s[left])
            left += 1
        seen.add(letter)
        longest_substring = max(longest_substring, right - left + 1)
    return longest_substring


def main():
    """main"""
    test_cases = [
        {
            "input": "abcabcbb",
            "output": 3
        },
        {
            "input": "bbbbb",
            "output": 1
        },
        {
            "input": "pwwkew",
            "output": 3
        }
    ]

    for i, test in enumerate(test_cases):
        print()
        print("Test case #", i)
        print("Input: ", test['input'])
        print("Expected: ", test["output"])
        print("result: ", length_of_longest_substring(test["input"]))


if __name__ == '__main__':
    main()
