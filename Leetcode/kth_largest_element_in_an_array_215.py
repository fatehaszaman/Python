# LeetCode #215 — Kth Largest Element in an Array
# Time: O(n log k)  — push/pop on a heap of size k, done n times
# Space: O(k)       — min-heap stores at most k elements

import heapq

# Time: O(n log k) | Space: O(k)
def findKthLargest(nums, k):
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)   # evict smallest; heap keeps top-k largest

    return min_heap[0]   # smallest of the top-k is the kth largest
