"""
Prefix Sum

Q: Given an array of values, design a data structure that can query the sum of
subarray of the values
"""


class PrefixSum:
    """Prefix Sum"""

    def __init__(self, nums) -> None:
        """O(n) prework"""
        self.prefix = []
        total = 0
        for n in nums:
            total += n
            self.prefix.append(total)

    def range_sum(self, left, right):
        """O(1)"""
        pre_right = self.prefix[right]
        pre_left = self.prefix[left - 1] if left > 0 else 0
        return pre_right - pre_left


p = PrefixSum([2, -1, 3, -3, 4])

# 5
print(p.range_sum(2, 3))
