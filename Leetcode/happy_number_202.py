# LeetCode #202 — Happy Number
# Time: O(log n)   — number of digits shrinks quickly; cycle detected by Floyd's algorithm
# Space: O(1)      — only two integer pointers (slow/fast)

class Solution:
    # Time: O(log n) | Space: O(1)
    def isHappy(self, n: int) -> bool:
        def getNext(num):
            # Time: O(log num) to process each digit
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total

        # Floyd's cycle detection (tortoise & hare)
        slow = n
        fast = getNext(n)
        while fast != 1 and slow != fast:
            slow = getNext(slow)
            fast = getNext(getNext(fast))

        return fast == 1
