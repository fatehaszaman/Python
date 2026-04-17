# LeetCode #121 — Best Time to Buy and Sell Stock
# Time: O(n)   — single pass through prices array
# Space: O(1)  — only two variables tracked

class Solution:
    # Time: O(n) | Space: O(1)
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price          # update minimum buying price
            elif price - min_price > max_profit:
                max_profit = price - min_price   # update max profit

        return max_profit
