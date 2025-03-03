class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        n = len(s)
        res = 0
        seen = {}
        while right < n:
            if s[right] in seen:
                if seen[s[right]] >= left:    
                    left = seen[s[right]] + 1
                
            res = max(res, right-left + 1)
            seen[s[right]] = right
            right += 1

        return res