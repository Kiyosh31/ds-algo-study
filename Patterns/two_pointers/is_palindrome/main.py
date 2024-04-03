"""Two Pointers"""


def is_palindrome(s):
    """O(n)"""
    left = 0
    right = len(s) - 1

    while left <= right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Driver Code


def main():
    """Main"""
    test_cases = ["RACEACAR", "A", "ABCDEFGFEDCBA",
                  "ABC", "ABCBA", "ABBA", "RACEACAR"]
    for i, test in enumerate(test_cases):
        print()
        print("Test Case #", i + 1)
        print("-" * 100)
        print("The input string is '", test, "' and the length of the string is ", len(
            test), ".", sep='')
        print("Is it a palindrome?.....", is_palindrome(test))
        print("-" * 100)


if __name__ == '__main__':
    main()
