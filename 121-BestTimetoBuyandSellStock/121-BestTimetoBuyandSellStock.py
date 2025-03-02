class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        high = 0
        low = float("inf")
        for p in prices:
            if p< low:
                low = p
            elif p - low > high:
                high = p-low

        return high