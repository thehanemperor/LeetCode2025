class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        room = []
        heap = []
        for start,end in intervals:
            heapq.heappush(heap,(start,end))

        while heap:
            fit = False
            for i in range(len(room)):
                start,end = room[i][-1]
                if end <= heap[0][0]:
                    room[i].append(heapq.heappop(heap))
                    fit = True
                    break

            if not fit:
                room.append([heapq.heappop(heap)])

        return len(room)