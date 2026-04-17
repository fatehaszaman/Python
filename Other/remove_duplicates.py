# Remove All Adjacent Duplicates (like LC 1047)
# Time: O(n)   — single pass through the string
# Space: O(n)  — stack can hold up to n characters in worst case


# Time: O(n) | Space: O(n)
def removeDuplicates(s):
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()   # cancel adjacent duplicate pair
        else:
            stack.append(c)
    return ''.join(stack)
