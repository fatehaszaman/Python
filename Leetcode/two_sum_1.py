# LeetCode #1 — Two Sum
# Time: O(n)   — single pass through the array
# Space: O(n)  — hash map stores at most n elements

from typing import List

class Solution:
    # Time: O(n) | Space: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = {}
        for i, num in enumerate(nums):
            total = target - num
            if total in num_index:
                return [num_index[total], i]
            num_index[num] = i
