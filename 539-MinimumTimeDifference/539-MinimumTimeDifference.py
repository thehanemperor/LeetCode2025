class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        arr = []
        for time in timePoints:
            hr,m = time.split(":")
            arr.append(int(hr)*60 + int(m))

        arr.sort()
        res = float("inf")
        for i in range(1,len(arr)):
            res = min(res, arr[i]- arr[i-1])
        
        res = min(24*60 - arr[-1] + arr[0], res)

        return res