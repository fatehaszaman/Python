# Find Missing Number — given n distinct numbers from 0..n, find the missing one
# Time: O(n)   — sum() iterates over array once
# Space: O(1)  — arithmetic only, no extra data structures


# Time: O(n) | Space: O(1)
def find_missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2   # Gauss formula: 0+1+...+n
    actual_sum = sum(nums)
    return expected_sum - actual_sum
