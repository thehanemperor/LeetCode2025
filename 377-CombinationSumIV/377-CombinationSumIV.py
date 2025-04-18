# Last updated: 4/18/2025, 11:57:06 AM
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = [0] *(target + 1)
        dp[0] = 1
        for combSum in range(target+1):
            for num in nums:
                if combSum - num >= 0:
                    # dp[1] = dp[1] + dp[0]
                    dp[combSum] = dp[combSum] + dp[combSum - num]

        return dp[-1]