class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        res = 0
        heap = [(grid[0][0],(0,0))]
        n = len(grid)
        seen = set()
        while heap:
            level, (x,y) = heapq.heappop(heap)
            seen.add((x,y))
            res = max(res, level)
            if x == n-1 and y == n-1:
                return res
            for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                if 0<=x+dx<n and 0<=y+dy<n and (x+dx,y+dy) not in seen:
                    seen.add((x+dx,y+dy))
                    heapq.heappush(heap,(grid[x+dx][y+dy],(x+dx,y+dy)))

        return res