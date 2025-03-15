class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        seen = {}
        res = 0
        for i in range(m):
            for j in range(n):
                seen[(i,j)] = self.dfs(matrix,i,j,seen)
                res = max(res,seen[(i,j)])

        return res

    def dfs(self,matrix,i,j,seen):
        if (i,j) in seen:
            return seen[(i,j)]

        m = len(matrix)
        n = len(matrix[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        res = 1
        for x,y in directions:
            if 0<=i+x<m and 0<=j+y<n and matrix[i+x][j+y] > matrix[i][j]:
                res = max(res,self.dfs(matrix,i+x,j+y,seen)+1)
        seen[(i,j)] = res
        return res