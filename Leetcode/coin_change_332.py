# LeetCode #322 — Coin Change
# Time: O(amount * len(coins))  — fill DP table of size amount+1 with one pass per coin
# Space: O(amount)              — DP array of size amount+1

from typing import List

class Solution:
    # Time: O(amount * len(coins)) | Space: O(amount)
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize dp array; amount+1 acts as infinity (unreachable)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins needed to make amount 0

        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != amount + 1 else -1
