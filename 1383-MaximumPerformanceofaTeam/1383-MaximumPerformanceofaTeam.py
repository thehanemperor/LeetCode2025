# Last updated: 3/30/2025, 1:20:25 AM
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        # performance = sum(speeds) * min(efficiency)
        # go from high efficiency and maintain a high speed as well
        workers = [(efficiency[i],speed[i]) for i in range(n)]
        workers.sort(key= lambda x:-x[0])
        
        speedHeap = []
        res = 0 
        speedSum = 0
        for currEff, currSpeed in workers:
            # efficiency is decreasing, everytime we get a lower eff
            if len(speedHeap) >= k:
                lowspeed = heappop(speedHeap)
                speedSum -= lowspeed
            heappush(speedHeap, currSpeed)
            speedSum += currSpeed
            res = max(res, speedSum * currEff)

        return res % (10**9 +7)
            