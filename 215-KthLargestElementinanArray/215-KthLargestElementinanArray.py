class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap,-num)

        res = -1
        for _ in range(k):
            res = -heapq.heappop(heap)

        return res