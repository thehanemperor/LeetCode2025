class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        left = right = 0
        intervals.sort(key= lambda x:x[0])
        n = len(intervals)
        res = []

        for start,end in intervals:
            if not res or res[-1][1] < start:
                res.append([start,end])

            else:
                res[-1][1] = max(res[-1][1], end)

        return res