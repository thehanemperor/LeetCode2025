class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        seen = set()
        left = 0
        n = len(s)
        right = 0
        while right < n:
            if s[right] in seen:
                while left<=right:
                    if s[left] == s[right]:
                        seen.remove(s[left])
                        left += 1
                        break
                    seen.remove(s[left])
                    left += 1
                    
            res = max(res, right -left + 1)
            seen.add(s[right])
            right += 1

        return res
