# LeetCode #33 — Search in Rotated Sorted Array
# Time: O(log n)  — binary search, halving the search space each iteration
# Space: O(1)     — constant extra space

class Solution:
    # Time: O(log n) | Space: O(1)
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1   # target in sorted left half
                else:
                    left = mid + 1    # target in right half
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1    # target in sorted right half
                else:
                    right = mid - 1   # target in left half

        return -1
