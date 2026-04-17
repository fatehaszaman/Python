# Reverse String — using Python slice notation
# Time: O(n)   — creates a reversed copy of length n
# Space: O(n)  — new string of length n


# Time: O(n) | Space: O(n)
def reverse_string(s):
    return s[::-1]   # slice [start:end:step=-1] reverses in one pass
