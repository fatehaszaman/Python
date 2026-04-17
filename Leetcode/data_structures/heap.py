# LeetCode — Heap / Priority Queue Problems
# Each solution includes Time and Space complexity annotations.

import math
from collections import defaultdict, Counter, deque
from typing import List, Optional, Tuple, Dict, Set, Union
import heapq

# =============================================================================
# HEAP PROBLEMS
# =============================================================================

# PROBLEM: Meeting Rooms II (LC 253)
# Time: O(n log n)  — sort O(n log n) + n heap operations O(log n) each
# Space: O(n)       — heap can hold up to n meeting end times
def minMeetingRooms(intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[0])
    heap = []
    heapq.heappush(heap, intervals[0][1])
    for i in range(1, len(intervals)):
        if intervals[i][0] >= heap[0]:
            heapq.heappop(heap)    # reuse a room
        heapq.heappush(heap, intervals[i][1])
    return len(heap)

# PROBLEM: Top K Frequent Elements (LC 347)
# Time: O(n)         — Counter O(n) + most_common O(n) using heapq.nlargest
# Space: O(n)        — frequency map stores all unique elements
def topKFrequent(nums, k):
    count = Counter(nums)
    return [num for num, _ in count.most_common(k)]

# PROBLEM: Kth Smallest Element in Sorted Matrix (LC 378)
# Time: O(k log n)   — k extractions from heap of size n (n = matrix side length)
# Space: O(n)        — heap stores one element per row
def kthSmallest(matrix, k):
    n = len(matrix)
    heap = []
    for i in range(n):
        heapq.heappush(heap, (matrix[i][0], i, 0))
    for _ in range(k - 1):
        val, row, col = heapq.heappop(heap)
        if col + 1 < n:
            heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))
    return heap[0][0]

# PROBLEM: Kth Largest Element in Array (LC 215)
# Time: O(n log k)   — push/pop on a heap of size k, done n times
# Space: O(k)        — min-heap stores at most k elements
def findKthLargest(nums, k):
    return heapq.nlargest(k, nums)[-1]

# PROBLEM: Find Median from Data Stream (LC 295)
# addNum:    Time O(log n) | Space O(1)
# findMedian: Time O(1)   | Space O(1)
# Overall Space: O(n)  — all numbers stored across two heaps
class MedianFinder:
    def __init__(self):
        self.small = []   # max-heap (negated values) — smaller half
        self.large = []   # min-heap — larger half

    # Time: O(log n) | Space: O(1)
    def addNum(self, num):
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)
        # Rebalance: size difference must be <= 1
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    # Time: O(1) | Space: O(1)
    def findMedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-self.small[0] + self.large[0]) / 2
