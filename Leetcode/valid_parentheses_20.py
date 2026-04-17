# LeetCode #20 — Valid Parentheses
# Time: O(n)   — single pass through string
# Space: O(n)  — stack holds at most n/2 opening brackets

class Solution:
    # Time: O(n) | Space: O(n)
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in mapping:
                top = stack.pop() if stack else '#'
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)

        return not stack
