# Last updated: 3/26/2025, 11:32:32 PM
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.res = []    
        self.dfs(0,s,wordDict,[])

        return self.res

    def dfs(self, index, s,wordDict,arr):
        if index == len(s):
            self.res.append(" ".join(arr))
            return 
        
        for i in range(index,len(s)):
            if s[index:i+1] in wordDict:
                arr.append(s[index:i+1])
                self.dfs(i+1, s,wordDict,arr)
                arr.pop()
    