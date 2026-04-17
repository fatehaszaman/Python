# LeetCode #9 — Palindrome Number
# Time: O(log10(n))  — we process half the digits of x
# Space: O(1)        — no extra data structures

class Solution:
    # Time: O(log10(n)) | Space: O(1)
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and non-zero multiples of 10 can't be palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # Even length: x == reversed_half
        # Odd length: ignore middle digit via reversed_half // 10
        return x == reversed_half or x == reversed_half // 10
