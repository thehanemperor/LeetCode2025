class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        res = 0
        seen = {}
        for i in range(m):
            for j in range(n):
                curr = self.dfs(matrix,i,j,seen)
                
        # print(seen)
        res = max(seen.values())
        return res

    def dfs(self,matrix,x,y,seen):
        if (x,y) in seen:
            return seen[(x,y)]
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        m = len(matrix)
        n = len(matrix[0])
        step = 0
        for dx,dy in directions:
            count = 0
            if 0<= x+dx<m and 0<=y+dy<n and matrix[dx+x][dy+y] > matrix[x][y]:
                count = self.dfs(matrix,dx+x,dy+y,seen)
            step = max(step, count)

        seen[(x,y)] = step+1
        return step+1