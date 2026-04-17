# LeetCode — Linked List & Misc Algorithms
# Time: varies per function — see inline # Time: | Space: annotations


# PROBLEM: plusOne (LEETCODE)
# Time: O(n) | Space: O(1)
def plusOne(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits

# =============================================================================

# QUESTION 90: Pow(x, n)
# Goal: Calculate x raised to the power n efficiently
# This uses the binary exponentiation technique - much faster than naive approach!
# Pseudocode:
#   1. Handle edge cases: n=0 returns 1, negative n means 1/x
#   2. Use binary representation of n to compute power
#   3. For each bit in n: if bit is 1, multiply result by current x
#   4. Square x for the next bit position
#   5. This reduces time complexity from O(n) to O(log n)!
# Time: O(log n), Space: O(log n)



# PROBLEM: __init__ (LEETCODE)
def __init__(self, val=0, next=None):
        self.val = val
        self.next = next




