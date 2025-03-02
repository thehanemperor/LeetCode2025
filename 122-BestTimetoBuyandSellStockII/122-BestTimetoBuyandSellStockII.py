class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.followUp(prices)
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

    def followUp(self,prices):
        high = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                high += prices[i]-prices[i-1]

        return high