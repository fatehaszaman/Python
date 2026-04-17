# LeetCode — Dynamic Programming Problems
# Each solution includes Time and Space complexity annotations.

import math
from collections import defaultdict, Counter, deque
from typing import List, Optional, Tuple, Dict, Set, Union
import heapq

# =============================================================================
# CLASS DEFINITIONS
# =============================================================================

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# =============================================================================
# DYNAMIC PROGRAMMING PROBLEMS
# =============================================================================

# PROBLEM: Maximum Product Subarray (LC 152)
# Time: O(n)   — single pass, tracking max and min products
# Space: O(1)  — only three variables
def maxProduct(nums):
    if not nums:
        return 0
    max_prod = min_prod = result = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_prod, min_prod = min_prod, max_prod   # swap: negative flips max/min
        max_prod = max(nums[i], max_prod * nums[i])
        min_prod = min(nums[i], min_prod * nums[i])
        result = max(result, max_prod)
    return result

# PROBLEM: Unique Paths (LC 62)
# Time: O(m * n)   — fill every cell of the DP table
# Space: O(m * n)  — 2D DP table
def uniquePaths(m, n):
    dp = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]

# PROBLEM: Unique Paths II (LC 63)
# Time: O(m * n)   — fill every cell once
# Space: O(1)      — modifies grid in-place
def uniquePathsWithObstacles(obstacleGrid):
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    if obstacleGrid[0][0] == 1:
        return 0
    obstacleGrid[0][0] = 1
    for j in range(1, n):
        obstacleGrid[0][j] = 0 if obstacleGrid[0][j] == 1 else obstacleGrid[0][j-1]
    for i in range(1, m):
        obstacleGrid[i][0] = 0 if obstacleGrid[i][0] == 1 else obstacleGrid[i-1][0]
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 1:
                obstacleGrid[i][j] = 0
            else:
                obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
    return obstacleGrid[m-1][n-1]

# PROBLEM: Minimum Path Sum (LC 64)
# Time: O(m * n)   — fill every cell once
# Space: O(1)      — modifies grid in-place
def minPathSum(grid):
    m, n = len(grid), len(grid[0])
    for j in range(1, n):
        grid[0][j] += grid[0][j-1]
    for i in range(1, m):
        grid[i][0] += grid[i-1][0]
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    return grid[m-1][n-1]

# PROBLEM: Decode Ways (LC 91)
# Time: O(n)   — single pass through string
# Space: O(n)  — DP array of length n+1
def numDecodings(s):
    if not s or s[0] == '0':
        return 0
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        if s[i-1] != '0':
            dp[i] += dp[i-1]
        two_digit = int(s[i-2:i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i-2]
    return dp[n]

# PROBLEM: Burst Balloons (LC 312)
# Time: O(n^3)  — three nested loops over interval endpoints
# Space: O(n^2) — 2D DP table
def maxCoins(nums):
    if not nums:
        return 0
    balloons = [1] + nums + [1]
    n = len(balloons)
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n):
        for left in range(n - length):
            right = left + length
            for k in range(left + 1, right):
                coins = balloons[left] * balloons[k] * balloons[right]
                dp[left][right] = max(dp[left][right], dp[left][k] + dp[k][right] + coins)
    return dp[0][n-1]

# PROBLEM: Word Break (LC 139) — v1
# Time: O(n^2 * m)  — n positions * n substrings * m dict lookup
# Space: O(n)       — DP boolean array
def wordBreak_v1(s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for word in wordDict:
            if i >= len(word) and dp[i - len(word)]:
                if s[i - len(word):i] == word:
                    dp[i] = True
                    break
    return dp[len(s)]

# PROBLEM 1: Climbing Stairs (LC 70)
# Time: O(n)   — iterate n times
# Space: O(1)  — two rolling variables
def climbStairs(n):
    if n <= 1:
        return 1
    prev2, prev1 = 1, 1
    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    return prev1

# PROBLEM 2: Fibonacci Number (LC 509)
# Time: O(n)   — iterate n times
# Space: O(1)  — two rolling variables
def fibonacci(n):
    if n <= 1:
        return n
    prev2, prev1 = 0, 1
    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    return prev1

# PROBLEM 3: Best Time to Buy and Sell Stock (LC 121)
# Time: O(n)   — single pass
# Space: O(1)  — two variables
def maxProfit(prices):
    if not prices:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)
    return max_profit

# PROBLEM 4: Word Break (LC 139) — v2 (set-based, faster lookup)
# Time: O(n^2)  — n positions, each checking up to n substrings; set lookup O(1)
# Space: O(n)   — DP array + word set
def wordBreak(s, wordDict):
    word_set = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[len(s)]

# PROBLEM 5: Longest Common Subsequence (LC 1143)
# Time: O(m * n)   — fill m*n DP table
# Space: O(m * n)  — 2D DP table
def longestCommonSubsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

# PROBLEM 6: House Robber (LC 198)
# Time: O(n)   — single pass
# Space: O(1)  — two rolling variables
def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    prev2, prev1 = nums[0], max(nums[0], nums[1])
    for i in range(2, len(nums)):
        current = max(prev1, prev2 + nums[i])
        prev2, prev1 = prev1, current
    return prev1

# PROBLEM 7: Coin Change (LC 322)
# Time: O(amount * len(coins))  — fill DP table
# Space: O(amount)              — 1D DP array
def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

# PROBLEM 8: Edit Distance (LC 72)
# Time: O(m * n)   — fill m*n DP table
# Space: O(m * n)  — 2D DP table
def minDistance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]

# PROBLEM 9: Unique Paths (LC 62) — space-optimized version
# Time: O(m * n)   — fill every cell
# Space: O(m * n)  — 2D DP table
def uniquePathsV2(m, n):
    dp = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]

# PROBLEM 10: Minimum Path Sum (LC 64) — separate DP table
# Time: O(m * n)   — fill every cell
# Space: O(m * n)  — separate DP table
def minPathSumV2(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
    return dp[m-1][n-1]
