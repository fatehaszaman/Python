# LeetCode — Sorting Problems
# Each solution includes Time and Space complexity annotations.

import math
from collections import defaultdict, Counter, deque
from typing import List, Optional, Tuple, Dict, Set, Union
import heapq

# =============================================================================
# SORTING PROBLEMS
# =============================================================================

# PROBLEM: Sort Colors (LC 75)  — Dutch National Flag algorithm
# Time: O(n)   — single pass with three pointers
# Space: O(1)  — in-place, no extra data structures
def sortColors(nums):
    low = mid = 0
    high = len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:                                   # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1                            # don't advance mid; check swapped element
