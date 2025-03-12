class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        seen = set()
        m = len(mat)
        n = len(mat[0])
        res = [[0 for _ in range(n)] for _ in range(m)]
        queue = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i,j,0))
                    seen.add((i,j))
                    
        self.bfs(mat,queue,seen,res)
        return res

    def bfs(self,mat,queue,seen,res):
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        m = len(mat)
        n = len(mat[0])
        while queue:
            x,y,level= queue.popleft()
            seen.add((x,y))
            for i,j in directions:
                if 0<=x+i<m and 0<=j+y<n and (x+i,y+j) not in seen:
                    seen.add((x+i,y+j))
                    queue.append((x+i,y+j,level+1))
                    res[x+i][y+j] = level +1
        