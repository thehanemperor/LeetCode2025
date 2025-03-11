class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        islandid = 2
        n = len(grid)
        islandCount = {}
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    size = self.bfs(deque([(i,j)]),islandid,grid)
                    islandCount[islandid] = size
                    islandid += 1
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        res = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    count = 1
                    seen = set()
                    for dx,dy in directions:
                        if 0<=i+dx<n and 0<=j+dy<n and grid[i+dx][j+dy]!=0 and grid[i+dx][j+dy] not in seen:
                            seen.add(grid[i+dx][j+dy])
                            count += islandCount[grid[i+dx][j+dy]]
                    res = max(res, count)
        return res if res!=0 else n*n


    def bfs(self,queue,mark,grid):
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        count = 0
        n = len(grid)
        while queue:
            x,y = queue.popleft()
            grid[x][y] = mark
            count += 1
            for dx,dy in directions:
                if 0<=dx+x<n and 0<=dy+y<n and grid[dx+x][dy+y] == 1:
                    
                    queue.append((dx+x,dy+y))
                    grid[dx+x][dy+y] = mark 
        
        return count