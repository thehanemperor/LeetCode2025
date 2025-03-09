class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        seen = {}
        left = right = 0
        res = 1
        while right < n:
            seen[s[right]] = seen.get(s[right],0) + 1
            while left <= right and len(seen) >2:
                seen[s[left]] -= 1
                if seen[s[left]] == 0:
                    seen.pop(s[left])
                left += 1
            
            if len(seen) <= 2:
                res = max(res, right-left+1)
            right += 1
            
        return res
            