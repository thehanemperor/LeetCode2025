class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        startBad = []
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    startBad.append((i,j,0))

        res = 0
        queue = deque(startBad)
        while queue:
            x,y,step = queue.popleft()
            res = max(res,step)

            for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                if 0<=x+dx<m and 0<=dy+y<n and grid[dx+x][dy+y] == 1:
                    queue.append((x+dx,y+dy,step+1))
                    grid[dx+x][dy+y] = 2
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return res