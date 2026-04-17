# LeetCode #1328 — Break a Palindrome
# Time: O(n)   — single pass through first half of string
# Space: O(n)  — list conversion of the string

class Solution:
    # Time: O(n) | Space: O(n)
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""   # single char can't be broken into non-palindrome
        chars = list(palindrome)

        # Replace first non-'a' character in the first half with 'a'
        for i in range(len(palindrome) // 2):
            if chars[i] != 'a':
                chars[i] = 'a'
                return ''.join(chars)

        # All characters are 'a' — change last character to 'b'
        chars[-1] = 'b'
        return ''.join(chars)
