class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker.sort(key= lambda x:-x)
        heap = []
        for i in range(len(profit)):
            heapq.heappush(heap,(-profit[i],-difficulty[i]))

        res = 0
        for w in worker:
            while heap and -heap[0][1]> w:
                heapq.heappop(heap)
            if heap:
                res += -heap[0][0]

        return res