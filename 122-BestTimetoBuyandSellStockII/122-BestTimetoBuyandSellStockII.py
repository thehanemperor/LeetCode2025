class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        res = 0
        n = len(prices)
        for i in range(n):
            if stack and prices[i] < prices[stack[-1]]:
                high = prices[stack[-1]]
                low = prices[stack[0]]
                res += high - low
                stack = []
            stack.append(i) 

        if stack:
            res += prices[stack[-1]]-prices[stack[0]]

        return res