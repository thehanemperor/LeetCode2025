// Last updated: 3/21/2025, 1:23:20 AM
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    up= 0 if i == 0 else grid[i-1][j]
                    left = 0 if j == 0 else grid[i][j-1]
                    right = 0 if j == n-1 else grid[i][j+1]
                    bot = 0 if i == m-1 else grid[i+1][j]

                    res += 4 -(up+left+right+bot)

        return res