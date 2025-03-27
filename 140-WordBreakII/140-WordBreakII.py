# Last updated: 3/26/2025, 11:19:33 PM
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] *(n+1)
        dp[0] = True
        for i in range(n):
            for j in range(i,n):
                if s[i:j+1] in wordDict and dp[i]:
                    dp[j+1] = True
                    
        print(dp)
        return dp[-1]
