class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        seen = {}
        res = 0
        candidate = None
        self.path=[]
        for i in range(m):
            for j in range(n):
                curr = self.dfs(matrix,i,j,seen)
                if curr > res:
                    res = curr
                    candidate = (i,j)
        
        ci,cj = candidate
        self.printPath(matrix,ci,cj,1,res,[matrix[ci][cj]],seen)

        return len(self.path[0])

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

    def printPath(self,matrix,i,j,step,longest,arr,seen):
        if step == longest:
            self.path.append([x for x in arr])
        
        m = len(matrix)
        n = len(matrix[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        res = 1
        for x,y in directions:
            if 0<=i+x<m and 0<=j+y<n and matrix[i+x][j+y] > matrix[i][j] and longest-step ==seen[(i+x,j+y)] :
                arr.append(matrix[i+x][j+y])
                self.printPath(matrix, i+x,j+y,step+1,longest,arr,seen)
                arr.pop()

        return res