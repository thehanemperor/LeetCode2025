class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        seen = {}
        left = 0
        n = len(s)
        right = 0
        while right < n:
            if s[right] in seen:
                while left<=right:
                    if s[left] == s[right]:
                        seen.pop(s[left])
                        left += 1
                        break
                    seen.pop(s[left])
                    left += 1
                    
            # print(left,right,s[left:right+1],seen)
            res = max(res, right -left + 1)
            seen[s[right]] = seen.get(s[right],0)+1
            right += 1

        return res
