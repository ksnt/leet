class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.calculate(prices, 0)
    
    def calculate(self,prices, s):
        if s >= len(prices):
            return 0
        m = 0
        for start in range(s,len(prices)):
            maxprofit = 0
            for i in range(start+1,len(prices)):
                if prices[start] < prices[i]:
                    profit = self.calculate(prices, i+1) + prices[i] - prices[start]
                    if profit > maxprofit:
                        maxprofit = profit
            if maxprofit > m:
                m = maxprofit
        return m