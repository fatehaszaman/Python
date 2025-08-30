class Solution:
    def myPow(self, x: float, n: int) -> float:
        N = n
        if N < 0:
            x, N = 1 / x, -N
        res = 1
        while N > 0:
            if N & 1: res *= x
            x *= x
            N >>= 1
        return res
