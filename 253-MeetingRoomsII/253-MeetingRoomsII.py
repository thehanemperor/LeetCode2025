class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []
        res = 0
        for start,end in intervals:
            if not heap or start < heap[0]:
                heapq.heappush(heap,end)
            else:
                heapq.heappop(heap)
                heapq.heappush(heap,end)

            res = max(res,len(heap))

        return res

                