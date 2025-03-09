class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(1,len(heights)):
            climb = heights[i] - heights[i-1]
            if climb <=0:
                continue
            
            heapq.heappush(heap,climb)
            if len(heap) <= ladders:
                continue # don't worry now
            
            bricks -= heapq.heappop(heap)
            if bricks < 0:
                return i -1

        
        return len(heights)-1