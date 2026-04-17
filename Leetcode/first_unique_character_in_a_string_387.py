# LeetCode #387 — First Unique Character in a String
# Time: O(n)   — two passes through string of length n
# Space: O(1)  — fixed-size array of 26 for lowercase letters

class Solution:
    # Time: O(n) | Space: O(1)
    def firstUniqChar(self, s: str) -> int:
        count = [0] * 26   # frequency table for a-z

        for ch in s:
            count[ord(ch) - ord('a')] += 1   # first pass: count frequencies

        for i, ch in enumerate(s):
            if count[ord(ch) - ord('a')] == 1:
                return i   # second pass: first index with frequency 1

        return -1
