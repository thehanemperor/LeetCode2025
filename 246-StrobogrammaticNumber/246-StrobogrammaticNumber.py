// Last updated: 3/22/2025, 4:33:51 PM
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        after = list(reversed(num))
        
        rotate = ['0','1','','','','','9','','8','6']
        res = []
        for c in after:
            res.append(rotate[int(c)])

        return "".join(res) == num

        