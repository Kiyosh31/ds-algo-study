"""
Given a string, s, that represents a DNA subsequence, and a number k, 
return all the contiguous subsequences (substrings) of length k that 
occur more than once in the string. The order of the returned 
subsequences does not matter. If no repeated substring is found, 
the function should return an empty set.

Example #1:
Input: s = "AAAAACCCCCAAAAACCCCCC", k = 8
output: ["AAAAACCC","AAAACCCC","AAACCCCC"]

Example #2:
Input: s = "GGGGGGGGGGGGGGGGGGGGGGGGG", k = 9
output: ["GGGGGGGGG"]

Example #3:
Input: s = "TTTTTCCCCCCCTTTTTTCCCCCCCTTTTTTT", k = 10
output: ["CCCCCCCTTT","CCCCCCTTTT","CCCCCTTTTT",
"CCCCTTTTTT","TCCCCCCCTT","TTCCCCCCCT",
"TTTCCCCCCC","TTTTCCCCCC","TTTTTCCCCC"]
"""


# 1. create 2 sets
#   - seen: to save all substrings seen
#   - res: to save all repeated substrings seened
# 2. iterate with sligind window
#   - Note: we could use 2 pointers but othe rway of using it is
#   to the len of subtrack k (s - k) this way we dont have to use 2 pointers
# 3. set a current (this is the content between the window)
#   - which is from left pointer to right pointer but since we dont
#    have a right pointer we need to iterate from left pointer to k
# 4. check if curr exist in seen
#   - add it to res
#   otherwise
#   - add it to seen
# 5. return res

def find_repeated_sequences(s, k):
    """
    :type s: str
    :rtype: List[str]
    """
    seen, res = set(), set()

    for left in range(len(s) - k):
        curr = s[left: left + k]
        if curr in seen:
            res.add(seen)
        else:
            seen.add(curr)
    return res
