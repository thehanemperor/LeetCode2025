class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        pairs = [(efficiency[i],speed[i]) for i in range(n)]
        pairs.sort(key = lambda x:-x[0])
        heap = []
        speedSum = 0
        res = 0

        for eff, currSpeed in pairs:
            if len(heap) >= k:
                speedSum -= heapq.heappop(heap)
            heapq.heappush(heap,currSpeed)
            speedSum += currSpeed

            res = max(res,speedSum * eff)

        return res % (10**9 + 7)