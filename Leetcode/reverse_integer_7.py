# LeetCode #7 — Reverse Integer
# Time: O(log10(n))  — number of digits in x
# Space: O(1)        — only a few integer variables

class Solution:
    # Time: O(log10(n)) | Space: O(1)
    def reverse(self, x: int) -> int:
        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10
            # Check overflow before it happens
            if res > (2**31 - 1) // 10:
                return 0
            res = res * 10 + digit

        return res * sign
