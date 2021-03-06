class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        if len(prices) == 0: return 0
        valley = prices[0]
        peak = prices[0]
        maxprofit = 0
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i+1]:
                i = i + 1
            valley = prices[i]
            while i < len(prices) - 1 and prices[i] <= prices[i+1]:
                i = i + 1
            peak = prices[i]
            maxprofit = maxprofit + (peak - valley)
        return maxprofit