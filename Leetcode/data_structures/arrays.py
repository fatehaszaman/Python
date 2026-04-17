# LeetCode - Array Problems
# Collection of array manipulation problems from LeetCode

import math
from collections import defaultdict, Counter, deque
from typing import List, Optional, Tuple, Dict, Set, Union
import heapq

# =============================================================================
# ARRAY PROBLEMS
# =============================================================================

# PROBLEM: 4Sum (LC 18)
# Goal: Find all unique quadruplets that sum to a target value
# This extends 3Sum to four numbers using nested loops and two pointers
# Pseudocode:
#   1. Sort the array to enable two-pointer technique
#   2. Fix first two numbers with nested loops
#   3. Use two pointers for the remaining two numbers
#   4. Skip duplicates at each level to avoid duplicate quadruplets
#   5. Adjust pointers based on current sum vs target
# Time: O(n^3) | Space: O(1)
def fourSum(nums, target):
   nums.sort()  # Sort to enable two-pointer technique
   result = []  # Store all unique quadruplets
   n = len(nums)
   for i in range(n - 3):  # Fix first number, need at least 3 more
       if i > 0 and nums[i] == nums[i-1]:  # Skip duplicates for first number
           continue
       for j in range(i + 1, n - 2):  # Fix second number, need at least 2 more
           if j > i + 1 and nums[j] == nums[j-1]:  # Skip duplicates for second number
               continue
           left, right = j + 1, n - 1  # Two pointers for remaining numbers
           while left < right:  # Use two-pointer technique
               current_sum = nums[i] + nums[j] + nums[left] + nums[right]  # Calculate current sum
               if current_sum == target:  # Found a valid quadruplet
                   result.append([nums[i], nums[j], nums[left], nums[right]])  # Add to result
                   # Skip duplicates for left pointer
                   while left < right and nums[left] == nums[left + 1]:
                       left += 1
                   # Skip duplicates for right pointer
                   while left < right and nums[right] == nums[right - 1]:
                       right -= 1
                   left += 1  # Move both pointers
                   right -= 1
               elif current_sum < target:  # Sum too small, need larger numbers
                   left += 1  # Move left pointer right
               else:  # Sum too large, need smaller numbers
                   right -= 1  # Move right pointer left
   return result

# PROBLEM: Trapping Rain Water (LC 42)
# Goal: Calculate how much rainwater can be trapped between bars
# This is a classic two-pointer problem with a clever insight about water trapping
# Pseudocode:
#   1. Use two pointers from both ends
#   2. Track the maximum height seen from each side
#   3. Water trapped at current position = min(left_max, right_max) - current_height
#   4. Move the pointer with smaller max height (greedy approach)
# Time: O(n) | Space: O(1)
def trap(height):
   if not height:  # Edge case: empty array
       return 0
   left, right = 0, len(height) - 1  # Start with pointers at both ends
   left_max = right_max = 0  # Track maximum heights seen from each side
   water = 0  # Total water trapped
   while left < right:  # Continue until pointers meet
       if height[left] < height[right]:  # Process left side
           if height[left] >= left_max:  # Update left maximum
               left_max = height[left]
           else:  # Water can be trapped here
               water += left_max - height[left]  # Add trapped water
           left += 1  # Move left pointer right
       else:  # Process right side
           if height[right] >= right_max:  # Update right maximum
               right_max = height[right]
           else:  # Water can be trapped here
               water += right_max - height[right]  # Add trapped water
           right -= 1  # Move right pointer left
   return water

# PROBLEM: Remove Duplicates from Sorted Array (LC 26)
# Goal: Remove duplicates from a sorted array in-place and return new length
# This uses the two-pointer technique with read and write pointers
# Pseudocode:
#   1. Use two pointers: read_idx (scans array) and write_idx (writes unique elements)
#   2. Start write_idx at 1 (first element is always unique)
#   3. For each element, if it's different from previous, write it at write_idx
#   4. Return write_idx as the new length
# Time: O(n) | Space: O(1)
def removeDuplicates(nums):
   if not nums:  # Edge case: empty array
       return 0
   write_idx = 1  # Position to write next unique element (first element is always unique)
   for read_idx in range(1, len(nums)):  # Start from second element
       if nums[read_idx] != nums[read_idx - 1]:  # If current element is different from previous
           nums[write_idx] = nums[read_idx]  # Write unique element at write position
           write_idx += 1  # Move write pointer forward
   return write_idx  # Return new length

# PROBLEM: Remove Duplicates from Sorted Array II (LC 80)
# Goal: Remove duplicates from sorted array, allowing at most 2 occurrences of each element
# This extends the previous problem to allow up to 2 duplicates
# Pseudocode:
#   1. Handle edge case: empty array
#   2. Use a write pointer to track where to place unique elements
#   3. Go through array with read pointer
#   4. If current element is different from previous, write it
#   5. Return the new length
def remove_duplicates(nums):
    if not nums:  # Edge case: empty array
        return 0
    write_idx = 1  # Pointer for where to write next unique element
    for i in range(1, len(nums)):  # Start from second element
        if nums[i] != nums[i-1]:  # If current element is different from previous
            nums[write_idx] = nums[i]  # Write it to the write position
            write_idx += 1  # Move write pointer forward
    return write_idx  # Return the new length

# PROBLEM: Square of a Sorted Array (LC 977)
# Goal: Return squares of numbers in sorted order
# Since input is sorted, largest squares come from either end (most negative or most positive)
# Pseudocode:
#   1. Use two pointers from both ends of the array
#   2. Compare absolute values to find larger square
#   3. Place larger square at the end of result array
#   4. Move pointers inward and repeat
def sortedSquares(nums):
   n = len(nums)
   result = [0] * n  # Create result array
   left, right = 0, n - 1  # Two pointers from both ends
   for i in range(n - 1, -1, -1):  # Fill result array from right to left
       if abs(nums[left]) > abs(nums[right]):  # Left element has larger absolute value
           result[i] = nums[left] * nums[left]  # Square left element
           left += 1  # Move left pointer right
       else:  # Right element has larger or equal absolute value
           result[i] = nums[right] * nums[right]  # Square right element
           right -= 1  # Move right pointer left
   return result

# PROBLEM: Merge Sorted Array (LC 88)
# Goal: Merge two sorted arrays into the first array in-place
# This uses a clever approach: work backwards to avoid overwriting unprocessed elements
# Pseudocode:
#   1. Start from the end of both arrays (largest elements)
#   2. Compare elements and place larger one at the end of result
#   3. Move pointers backwards as we fill the result
#   4. Copy any remaining elements from nums2
def merge(nums1, m, nums2, n):
   # Start from the end of both arrays to avoid overwriting
   i, j, k = m - 1, n - 1, m + n - 1  # i: nums1, j: nums2, k: result position
   while i >= 0 and j >= 0:  # Continue while both arrays have elements
       if nums1[i] > nums2[j]:  # nums1 element is larger
           nums1[k] = nums1[i]  # Place nums1 element
           i -= 1  # Move nums1 pointer left
       else:  # nums2 element is larger or equal
           nums1[k] = nums2[j]  # Place nums2 element
           j -= 1  # Move nums2 pointer left
       k -= 1  # Move result pointer left
   # Copy remaining elements from nums2 (nums1 elements are already in place)
   while j >= 0:
       nums1[k] = nums2[j]  # Copy remaining nums2 element
       j -= 1  # Move nums2 pointer left
       k -= 1  # Move result pointer left

# PROBLEM: Contains Duplicate (LC 217)
# Goal: Check if array contains any duplicate values
# This uses a set to track seen numbers for O(1) lookup
# Pseudocode:
#   1. Use set to track numbers we've seen
#   2. For each number, check if already in set
#   3. If found, return True; otherwise add to set
#   4. If no duplicates found, return False
# Time: O(n) | Space: O(n)
def containsDuplicate(nums):
   seen = set()  # Track numbers we've seen
   for num in nums:  # Check each number
       if num in seen:  # If we've seen this number before
           return True  # Duplicate found
       seen.add(num)  # Add to seen set
   return False  # No duplicates found

# PROBLEM: Intersection of Two Arrays (LC 349)
# Goal: Find intersection of two arrays (unique elements common to both)
# This uses set intersection to find common elements
# Pseudocode:
#   1. Convert both arrays to sets
#   2. Find intersection using set operation
#   3. Convert result back to list
def intersection(nums1, nums2):
   set1 = set(nums1)  # Convert first array to set
   set2 = set(nums2)  # Convert second array to set
   return list(set1 & set2)  # Return intersection as list

# PROBLEM: Rotate Array (LC 189)
# Goal: Rotate array to the right by k steps
# This uses reverse technique for O(1) space solution
# Pseudocode:
#   1. Reverse entire array
#   2. Reverse first k elements
#   3. Reverse remaining elements
# Time: O(n) | Space: O(1)
def rotate(nums, k):
   n = len(nums)
   k = k % n  # Handle k > n
   
   def reverse(start, end):
       while start < end:
           nums[start], nums[end] = nums[end], nums[start]
           start += 1
           end -= 1
   reverse(0, n - 1)  # Reverse entire array
   reverse(0, k - 1)  # Reverse first k elements
   reverse(k, n - 1)  # Reverse remaining elements

# PROBLEM: 3Sum (LC 15)
# Goal: Find all unique triplets that sum to zero
# This extends the two-sum problem to three numbers using sorting and two pointers
# Pseudocode:
#   1. Sort the array to enable two-pointer technique
#   2. Fix the first number and use two pointers for the remaining two
#   3. Skip duplicates to avoid duplicate triplets
#   4. If sum is zero, add to result and move both pointers
#   5. If sum is too small, move left pointer right
#   6. If sum is too large, move right pointer left
# Time: O(n^2) | Space: O(1)
def threeSum(nums):  
   nums.sort()  # Sort to enable two-pointer technique
   result = []  # Store all unique triplets
   for i in range(len(nums) - 2):  # Fix first number, need at least 2 more
       if i > 0 and nums[i] == nums[i-1]:  # Skip duplicates for first number
           continue
       left, right = i + 1, len(nums) - 1  # Two pointers for remaining numbers
       while left < right:  # Use two-pointer technique
           current_sum = nums[i] + nums[left] + nums[right]  # Calculate current sum
           if current_sum == 0:  # Found a valid triplet
               result.append([nums[i], nums[left], nums[right]])  # Add to result
               # Skip duplicates for left pointer
               while left < right and nums[left] == nums[left + 1]:
                   left += 1
               # Skip duplicates for right pointer
               while left < right and nums[right] == nums[right - 1]:
                   right -= 1           
               left += 1  # Move both pointers
               right -= 1
           elif current_sum < 0:  # Sum too small, need larger numbers
               left += 1  # Move left pointer right
           else:  # Sum too large, need smaller numbers
               right -= 1  # Move right pointer left
   return result

# PROBLEM: Median of Two Sorted Arrays (LC 4)
# Goal: Find median using merge technique (simpler but less efficient)
# This is an alternative approach that's easier to understand!
# Pseudocode:
#   1. Merge the two arrays until we reach the middle elements
#   2. Keep track of previous and current elements
#   3. For even total length, return average of two middle elements
#   4. For odd total length, return the middle element
# Time Complexity: O(m + n), Space Complexity: O(1)
def findMedianSortedArrays(nums1, nums2):
    m, n = len(nums1), len(nums2)  # Get array lengths
    total = m + n  # Total number of elements
    is_even = total % 2 == 0  # Check if total length is even
    i = j = 0  # Pointers for both arrays
    prev = curr = 0  # Track previous and current elements
    for _ in range(total // 2 + 1):  # Merge until we reach middle
        prev = curr  # Update previous element
        if i < m and (j >= n or nums1[i] <= nums2[j]):  # Choose from nums1
            curr = nums1[i]  # Current element from nums1
            i += 1  # Advance nums1 pointer
        else:  # Choose from nums2
            curr = nums2[j]  # Current element from nums2
            j += 1  # Advance nums2 pointer
    return (prev + curr) / 2 if is_even else curr  # Return median

# PROBLEM: Merge Intervals (LC 56)
# Goal: Merge all overlapping intervals
# This is a classic interval problem using sorting!
# Pseudocode:
#   1. Sort intervals by start time
#   2. Initialize result with first interval
#   3. For each interval, check if it overlaps with last merged interval
#   4. If overlap: extend the last interval's end
#   5. If no overlap: add as new interval
# Time: O(n log n), Space: O(1)
def merge(intervals):
    if not intervals:  # Edge case: empty list
        return []
    intervals.sort(key=lambda x: x[0])  # Sort by start time
    merged = [intervals[0]]  # Initialize with first interval
    for current in intervals[1:]:  # Go through remaining intervals
        last = merged[-1]  # Get last merged interval
        if current[0] <= last[1]:  # If current overlaps with last
            last[1] = max(last[1], current[1])  # Extend end time
        else:  # No overlap
            merged.append(current)  # Add as new interval
    return merged

# PROBLEM: Sliding Window Maximum (LC 239)
# Goal: Find maximum element in each sliding window of size k
# Time: O(n), Space: O(k)
# Pseudocode:
#   1. Use deque to maintain indices in decreasing order of values
#   2. Remove indices outside current window
#   3. Remove smaller elements from back
#   4. Front of deque has index of max in current window
def maxSlidingWindow(nums, k):
    if not nums or k == 0:
        return []
    
    dq = deque()
    result = []
    
    for i in range(len(nums)):
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        
        dq.append(i)
        
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result

# PROBLEM: Build Array from Permutation (LC 1920)
# Goal: Transform array using permutation
# Pseudocode:
#   1. For each index i, result[i] = nums[nums[i]]
#   2. This creates a new array where each element is the value at the index specified by the original array
def buildArray(nums):
    return [nums[nums[i]] for i in range(len(nums))]  # Transform array using permutation

# PROBLEM 1: Two Sum (LC 1)
# Goal: Find two numbers that add up to target and return their indices
# Time: O(n), Space: O(n)
# Pseudocode:
#   1. Use hashmap to store number -> index
#   2. For each number, check if (target - number) exists in hashmap
#   3. If found, return both indices
#   4. Otherwise, add current number and index to hashmap
# Time: O(n) | Space: O(n)
def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# PROBLEM 2: Container With Most Water (LC 11)
# Goal: Find two lines that together with x-axis forms a container with most water
# Time: O(n), Space: O(1)
# Pseudocode:
#   1. Use two pointers at start and end
#   2. Calculate area = min(height[left], height[right]) * (right - left)
#   3. Move pointer with smaller height
#   4. Track maximum area
# Time: O(n) | Space: O(1)
def maxArea(height):
    left, right = 0, len(height) - 1
    max_area = 0
    
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, area)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

# PROBLEM 3: Product of Array Except Self (LC 238)
# Goal: Return array where each element is product of all other elements
# Time: O(n), Space: O(1) excluding output
# Pseudocode:
#   1. Create result array with all 1s
#   2. First pass: calculate left products
#   3. Second pass: calculate right products and multiply
#   4. Return result array
# Time: O(n) | Space: O(1)
def productExceptSelf(nums):
    n = len(nums)
    result = [1] * n
    
    # Calculate left products
    for i in range(1, n):
        result[i] = result[i-1] * nums[i-1]
    
    # Calculate right products and multiply
    right_product = 1
    for i in range(n-1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]
    
    return result

# PROBLEM 4: Maximum Subarray (LC 53) - Kadane's Algorithm
# Goal: Find maximum sum of any contiguous subarray
# Time: O(n), Space: O(1)
# Pseudocode:
#   1. Track max_ending_here and max_so_far
#   2. For each element, decide: add to current sum or start new
#   3. Update max_so_far if current sum is larger
#   4. Return max_so_far
# Time: O(n) | Space: O(1)
def maxSubArray(nums):
    if not nums:
        return 0
    
    max_ending_here = max_so_far = nums[0]
    
    for i in range(1, len(nums)):
        max_ending_here = max(nums[i], max_ending_here + nums[i])
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far

# PROBLEM 5: Contains Duplicate (LC 217)
# Goal: Check if array contains any duplicates
# Time: O(n), Space: O(n)
# Pseudocode:
#   1. Use set to track seen numbers
#   2. If number already in set, return True
#   3. Otherwise, add to set
#   4. Return False if no duplicates found
# Time: O(n) | Space: O(n)
def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# PROBLEM 6: Missing Number (LC 268)
# Goal: Find missing number in array containing n distinct numbers from 0 to n
# Time: O(n), Space: O(1)
# Pseudocode:
#   1. Calculate expected sum = n * (n + 1) / 2
#   2. Calculate actual sum of array
#   3. Return expected - actual
# Time: O(n) | Space: O(1)
def missingNumber(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# PROBLEM 7: Single Number (LC 136)
# Goal: Find element that appears once while others appear twice
# Time: O(n), Space: O(1)
# Pseudocode:
#   1. Use XOR property: a ^ a = 0, a ^ 0 = a
#   2. XOR all numbers together
#   3. Result is the single number
# Time: O(n) | Space: O(1)
def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# PROBLEM 8: Rotate Array (LC 189)
# Goal: Rotate array to the right by k steps
# Time: O(n), Space: O(1)
# Pseudocode:
#   1. Reverse entire array
#   2. Reverse first k elements
#   3. Reverse remaining elements
# Time: O(n) | Space: O(1)
def rotate(nums, k):
    n = len(nums)
    k = k % n
    
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)

# PROBLEM 9: Merge Sorted Array (LC 88)
# Goal: Merge two sorted arrays in-place
# Time: O(m + n), Space: O(1)
# Pseudocode:
#   1. Start from the end of both arrays
#   2. Compare elements and place larger one at end of result
#   3. Move pointers accordingly
def merge(nums1, m, nums2, n):
    i, j, k = m - 1, n - 1, m + n - 1
    
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    
    # Copy remaining elements from nums2
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

# PROBLEM 10: Remove Duplicates from Sorted Array (LC 26)
# Goal: Remove duplicates in-place and return new length
# Time: O(n), Space: O(1)
# Pseudocode:
#   1. Use two pointers: slow and fast
#   2. If elements are different, move slow pointer and copy element
#   3. Always move fast pointer
#   4. Return slow + 1 as new length
# Time: O(n) | Space: O(1)
def removeDuplicates(nums):
    if not nums:
        return 0
    
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    
    return slow + 1

# =============================================================================
# CODESIGNAL ARRAY PROBLEMS
# =============================================================================

# PROBLEM 11: Adjacent Elements Product (CodeSignal)
# Goal: Find the largest product of two adjacent elements in an array
# Time: O(n), Space: O(1)
# Pseudocode:
#   1. Start with the smallest possible product value
#   2. For each pair of adjacent elements, calculate their product
#   3. Keep track of the maximum product found so far
#   4. Return the maximum product
def adjacentElementsProduct(inputArray):
    max_product = float('-inf')
    for i in range(len(inputArray) - 1):
        product = inputArray[i] * inputArray[i + 1]
        max_product = max(max_product, product)
    return max_product

# PROBLEM 12: Make Array Consecutive 2 (CodeSignal)
# Goal: Count how many additional statues are needed to make the array consecutive
# Time: O(n), Space: O(1)
# Pseudocode:
#   1. Find the range from minimum to maximum value
#   2. Calculate how many numbers should be in this range
#   3. Subtract the current count to find missing numbers
def makeArrayConsecutive2(statues):
    return max(statues) - min(statues) - len(statues) + 1

# PROBLEM 13: Array Maximal Adjacent Difference (CodeSignal)
# Goal: Find the maximal absolute difference between any two adjacent elements
# Time: O(n), Space: O(1)
# Pseudocode:
#   1. Initialize max difference to 0
#   2. For each adjacent pair, calculate absolute difference
#   3. Update max difference if current is larger
def arrayMaximalAdjacentDifference(inputArray):
    max_diff = 0
    for i in range(len(inputArray) - 1):
        diff = abs(inputArray[i] - inputArray[i + 1])
        max_diff = max(max_diff, diff)
    return max_diff

# PROBLEM 14: First Duplicate (CodeSignal)
# Goal: Find the first duplicate number in the array
# Time: O(n), Space: O(n)
# Pseudocode:
#   1. Use set to keep track of numbers we've seen
#   2. For each number, check if we've seen it before
#   3. If yes, return it (first duplicate)
#   4. Otherwise, add to set
def firstDuplicate(a):
    seen = set()
    for num in a:
        if num in seen:
            return num
        seen.add(num)
    return -1

# PROBLEM 15: Array Replace (CodeSignal)
# Goal: Replace all occurrences of elemToReplace with substitutionElem
# Time: O(n), Space: O(1)
# Pseudocode:
#   1. Iterate through the array
#   2. If element equals elemToReplace, replace with substitutionElem
#   3. Return the modified array
def arrayReplace(inputArray, elemToReplace, substitutionElem):
    for i in range(len(inputArray)):
        if inputArray[i] == elemToReplace:
            inputArray[i] = substitutionElem
    return inputArray
