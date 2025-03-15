class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        seen = set()
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and (i,j) not in seen:
                    if not self.bfs(i,j,grid,seen):
                        print(i,j)
                        count += 1

        return count
    def bfs(self,i,j,grid,seen):
        
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        queue.append((i,j))
        isEdge = False
        while queue:
            x,y = queue.popleft()

            seen.add((x,y))
            if x in [0,m-1] or y in [0,n-1]:
                isEdge = True
                
            for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                if 0<=dx+x<m and 0<=dy+y<n and (dx+x,dy+y) not in seen and grid[dx+x][y+dy] == 0:
                    seen.add((dx+x,dy+y))
                    queue.append((dx+x,dy+y))

        return isEdge