# Leecode question number 332

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize dp array, amount + 1 is like infinity (unreachable)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # Base case
        
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != amount + 1 else -1
