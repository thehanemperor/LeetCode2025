# Last updated: 4/1/2025, 8:37:34 PM
class Solution:
    def compress(self, chars: List[str]) -> int:
        left = right = 0
        n = len(chars)
        while right <n :
            start = right
            while right + 1 < n and chars[right+1] == chars[right]:
                right += 1
            
            interval = right - start + 1
            chars[left] = chars[right]
            left += 1
            if interval > 1:
                tmp = str(interval)
                for t in tmp:
                    chars[left] = t
                    left += 1
            
            right += 1
            
        return left