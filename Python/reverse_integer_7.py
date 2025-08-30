# Leecode question number 7

class Solution:
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
