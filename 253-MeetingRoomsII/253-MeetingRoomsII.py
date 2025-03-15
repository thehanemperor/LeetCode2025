class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        heap = []
        res = 1
        for start,end in intervals:
            if not heap or heap[0] > start:
                heapq.heappush(heap,end)
            else:
                heapq.heappop(heap)
                heapq.heappush(heap,end)
            res = max(res, len(heap))
        return res
