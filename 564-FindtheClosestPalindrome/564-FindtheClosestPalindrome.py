// Last updated: 3/22/2025, 3:01:02 AM

class Solution:
    def nearestPalindromic(self, n: str) -> str:
        size = len(n)
        if size %2 == 0:
            leftLen = size // 2 # 1234 -> 3
        else:
            leftLen = size //2 +1 # 123 -> 2

        firstHalf = int(n[:leftLen])
        candidates = []
        for offset in range(-1,2):
            # -1, 0, 1
            candidates.append(self.getPali(firstHalf+offset,size%2==0))
        candidates.append(10**(size)+1)
        candidates.append(10**(size-1)-1)
        print(candidates)
        res = 0
        origin = int(n)
        minDiff = float("inf")
        for candi in candidates:
            if candi == origin:
                continue
            if abs(origin - candi) < minDiff:
                minDiff = abs(origin-candi)
                res = candi
            elif abs(origin -candi) == minDiff:
                res = min(res, candi)

        return str(res)



    def getPali(self,leftHalf,isEven):
        res = leftHalf
        if not isEven:
            leftHalf //= 10

        
        while leftHalf>0:
            res = res*10 + leftHalf%10
            leftHalf //= 10

        return res
