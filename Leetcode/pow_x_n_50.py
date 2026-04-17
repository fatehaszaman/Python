# LeetCode #50 — Pow(x, n)  (Fast Power / Binary Exponentiation)
# Time: O(log n)  — halve the exponent each iteration
# Space: O(1)     — iterative, no call stack

class Solution:
    # Time: O(log n) | Space: O(1)
    def myPow(self, x: float, n: int) -> float:
        N = n
        if N < 0:
            x, N = 1 / x, -N
        res = 1
        while N > 0:
            if N & 1:          # if lowest bit is set, multiply in current x
                res *= x
            x *= x             # square x for next bit position
            N >>= 1            # shift exponent right
        return res
