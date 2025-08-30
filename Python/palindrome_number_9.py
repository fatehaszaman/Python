# Leet code number 9
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindrome
        # Numbers ending with 0 are not palindrome unless the number is 0
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # For even length numbers, x == reversed_half
        # For odd length numbers, ignore the middle digit by reversed_half // 10
        return x == reversed_half or x == reversed_half // 10
