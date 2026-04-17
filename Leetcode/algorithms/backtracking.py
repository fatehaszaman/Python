# LeetCode — Backtracking Problems
# Each solution includes Time and Space complexity annotations.

import math
from collections import defaultdict, Counter, deque
from typing import List, Optional, Tuple, Dict, Set, Union
import heapq

# =============================================================================
# BACKTRACKING PROBLEMS
# =============================================================================

# PROBLEM: Combination Sum (LC 39)
# Time: O(n^(t/m))  — n candidates, target t, smallest candidate m; branching factor pruned by target
# Space: O(t/m)     — max recursion depth is target / min_candidate
def combinationSum(candidates, target):
    candidates.sort()
    result = []
    def backtrack(start, current_sum, path):
        if current_sum == target:
            result.append(path[:])
            return
        if current_sum > target:
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, current_sum + candidates[i], path)
            path.pop()
    backtrack(0, 0, [])
    return result

# PROBLEM: Combination Sum II (LC 40)
# Time: O(2^n)  — at most 2^n subsets before pruning
# Space: O(n)   — recursion depth and path length at most n
def combinationSum2(candidates, target):
    candidates.sort()
    result = []
    def backtrack(start, current_sum, path):
        if current_sum == target:
            result.append(path[:])
            return
        if current_sum > target:
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue   # skip duplicates at same recursion level
            path.append(candidates[i])
            backtrack(i + 1, current_sum + candidates[i], path)
            path.pop()
    backtrack(0, 0, [])
    return result

# PROBLEM: Permutations (LC 46)
# Time: O(n * n!)  — n! permutations, each takes O(n) to copy
# Space: O(n)      — recursion depth n, path length n
def permute(nums):
    result = []
    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for num in nums:
            if num not in path:
                path.append(num)
                backtrack(path)
                path.pop()
    backtrack([])
    return result

# PROBLEM: Permutations II (LC 47)
# Time: O(n * n!)  — at most n! unique permutations, pruning reduces this
# Space: O(n)      — recursion depth n + used array
def permuteUnique(nums):
    nums.sort()
    result = []
    used = [False] * len(nums)
    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]):
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path)
            path.pop()
            used[i] = False
    backtrack([])
    return result

# PROBLEM: Subsets (LC 78)
# Time: O(n * 2^n)  — 2^n subsets, each copied in O(n)
# Space: O(n)       — recursion depth n
def subsets(nums):
    result = []
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    return result
