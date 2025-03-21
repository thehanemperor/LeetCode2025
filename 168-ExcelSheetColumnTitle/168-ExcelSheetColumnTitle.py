// Last updated: 3/21/2025, 2:10:58 AM
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n = columnNumber
        res = ""
        A = ord("A")
        while n >0:
            n-= 1
            curr = n %26
            res = chr(curr + A) + res
            n = n // 26

        return res
         