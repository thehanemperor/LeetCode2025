class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        res = ""
        high = 0
        
        for i in range(len(s)):
            left, right = self.expand(s, i, i + 1)
            evenLength = right - left - 1
            if evenLength > high:
                high = evenLength
                res = s[left + 1: right]
            left, right = self.expand(s, i, i)
            oddLength = right - left - 1
            if oddLength > high:
                high = oddLength
                res = s[left + 1: right]
        
        return res

    def expand(self, s, left, right):
        while left > -1 and right < len(s):
            if s[left] != s[right]:
                break
            left -= 1
            right += 1
        return (left, right)