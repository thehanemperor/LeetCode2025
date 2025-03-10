class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num,0) + 1

        heap = []
        for key,v in seen.items():
            heapq.heappush(heap,(-v,key))
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res