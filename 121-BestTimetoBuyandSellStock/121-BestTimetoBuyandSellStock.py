class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        high = [0]*n
        high[n-1] = prices[n-1]
        for i in range(n-2,-1,-1):
            high[i] = max(prices[i], high[i+1])

        res = 0
        for i in range(n):
            res = max(res, high[i] - prices[i])
        
        return res