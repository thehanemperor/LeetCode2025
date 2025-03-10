class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left <= right:
            mid = (left +right) //2

            time = 0
            for p in piles:
                time += p//mid
                if p%mid !=0:
                    time += 1

            if time <=h:
                right = mid -1
            else:
                left = mid + 1

        return left