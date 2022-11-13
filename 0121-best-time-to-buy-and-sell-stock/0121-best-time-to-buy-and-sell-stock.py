class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        sell = prices[-1]
        
        for i in range(len(prices)-2, -1, -1):
            curr = prices[i]
            max_profit = max(max_profit, sell - curr)
            sell = max(sell, curr)
        
        return max_profit