# Fibonacci — naive recursive implementation
# Time: O(2^n)  — exponential; each call branches into two recursive calls
# Space: O(n)   — call stack depth is n


# Time: O(2^n) | Space: O(n)
# Note: for large n use dynamic programming (O(n) time, O(1) space)
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
