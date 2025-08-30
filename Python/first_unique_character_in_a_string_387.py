# Leetcode question number 387
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = [0] * 26  # For lowercase a-z

        for ch in s:
            count[ord(ch) - ord('a')] += 1  # Count each character

        for i, ch in enumerate(s):
            if count[ord(ch) - ord('a')] == 1:
                return i

        return -1
