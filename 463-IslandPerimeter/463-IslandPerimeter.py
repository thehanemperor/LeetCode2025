// Last updated: 3/21/2025, 1:17:24 AM
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        edge = [[0 for _ in range(n)] for _ in range(m)]
        seen = set()
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i,j))
                    break
            if queue:
                break
        
        while queue:
            
            x,y = queue.popleft()
            seen.add((x,y))

            for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
                if 0<= x+dx <m and 0<=y+dy<n and grid[x+dx][y+dy] == 1:
                    edge[x][y] += 1
                    if (x+dx,y+dy) not in seen:
                        seen.add((x+dx,y+dy))
                        queue.append((x+dx,y+dy))

        res = 0
        for i,j in seen:
            res += 4 - edge[i][j]

        return res