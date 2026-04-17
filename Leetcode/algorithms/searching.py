# LeetCode — Searching & Bit Problems
# Time / Space: see inline annotations


# PROBLEM: isPowerOfTwo (LEETCODE)
# Time: O(1) | Space: O(1)
def isPowerOfTwo(n):
    return n > 0 and n & (n - 1) == 0

# Add Binary



# PROBLEM: addBinary (LEETCODE)
# Time: O(max(a,b)) | Space: O(max(a,b))
def addBinary(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]

# Sqrt(x)


