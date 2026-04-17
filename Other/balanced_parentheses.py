# Balanced Parentheses — check if a string of brackets is balanced
# Time: O(n)   — single pass through the string
# Space: O(n)  — stack holds at most n/2 opening brackets


# Time: O(n) | Space: O(n)
def is_balanced(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack
