// Last updated: 3/21/2025, 1:52:26 AM
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)
        res = 0
        p = 0
        for i in range(n-1,-1,-1):
            char = columnTitle[i]
            val = ord(char) - ord("A") + 1
            res += val * (26**p)
            p += 1

        return res