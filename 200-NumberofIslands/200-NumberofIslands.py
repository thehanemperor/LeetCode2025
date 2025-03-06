from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        length, height = len(grid), len(grid[0])
        seen = set()
        res = 0
        for i in range(length):
            for j in range(height):
                if (i,j) in seen:
                    continue
                if grid[i][j] == "1":
                    # count here
                    queue = deque([(i,j)])
                    while queue:
                        x,y = queue.popleft()
                        seen.add((x, y))
                        for di, dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                            if 0 <= (di + x) < length and 0<= (dj +y)< height and grid[di+x][dj+y] == '1' and (di+x, dj+y) not in seen:
                                queue.append((di+x, dj+y))
                                seen.add((di+x, dj+y))
                    res += 1
        
        return res