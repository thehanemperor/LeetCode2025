class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        return self.followUp(timePoints)
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

    def followUp(self, timePoints):
        clock = [False] * (24*60)
        for time in timePoints:
            hr, m = time.split(":")
            curr = int(hr)*60+int(m)
            if clock[curr]:
                return 0
            clock[curr] = True

        first = None
        prev = None
        curr = None
        res = float("inf")
        for i in range(24*60):
            if clock[i]:
                if first == None:
                    first = i
                curr = i

                if prev:
                    res = min(res, curr - prev)

                prev = curr
        res = min(res, 24*60 - curr + first)

        return res