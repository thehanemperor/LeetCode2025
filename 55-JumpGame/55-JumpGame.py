class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[n-1] = True
        for i in range(n-2,-1,-1):
            for j in range(nums[i]+1):
                
                if dp[i+j] == True:
                    dp[i] = True
                    break
        
        return dp[0]

    def followUp(self, nums):
        n = len(nums)
        lastPos = n -1
        for i in range(n-2,-1,-1):
            if nums[i] + i>= lastPos:
                lastPos = i
        
        return lastPos == 0
