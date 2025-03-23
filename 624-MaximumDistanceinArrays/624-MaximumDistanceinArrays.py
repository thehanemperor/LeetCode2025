# Last updated: 3/23/2025, 2:08:10 AM
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        n = len(arrays)
        res = 0
        minNum = arrays[0][0]
        maxNum = arrays[0][-1]

        for i in range(1,n):
            res = max(res, abs(maxNum - arrays[i][0]), abs(minNum - arrays[i][-1]))
            maxNum = max(maxNum,arrays[i][-1])
            minNum = min(minNum, arrays[i][0])

        return res