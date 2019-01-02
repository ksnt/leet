import sys
class Solution:
    def maxProfit(self,prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0: return 0
        min_price = sys.maxsize
        max_profit = 0
        length = len(prices)
        for i in range(length):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit