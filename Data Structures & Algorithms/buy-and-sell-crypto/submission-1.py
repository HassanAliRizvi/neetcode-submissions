class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        max_diff = 0

        while j < len(prices):
            diff = prices[j] - prices[i]
            if diff > 0:
                max_diff = max(max_diff, diff)
            else:
                i = j
            j += 1
        
        return max_diff
