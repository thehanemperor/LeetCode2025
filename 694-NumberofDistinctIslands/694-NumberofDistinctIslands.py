class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        self.seen = set()
        m = len(grid)
        n = len(grid[0])
        uniqueIslands = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in self.seen:
                    island = self.findIsland(grid,i,j)
                    col = n
                    for row in range(len(island)):
                        col = min(col,island[row][1])
                    for row in range(len(island)):
                        island[row][0] -=i
                        island[row][1] -= col
                    print(island)
                    self.addToUnique(uniqueIslands,island)

        return len(uniqueIslands)
    
    def addToUnique(self,uniqueIslands,island):
        
        for unique in uniqueIslands:
            found = True
            if len(unique) != len(island):
                continue
            for i in range(len(unique)):
                if unique[i] != island[i]:
                    found = False
                    break

            if found:
                return 
        uniqueIslands.append([x for x in island])

        

            
        


    def findIsland(self,grid,x,y):
        m = len(grid)
        n = len(grid[0])
        queue = deque()
        queue.append((x,y))
        island = []
        while queue:
            i,j = queue.popleft()
            self.seen.add((i,j))
            island.append([i,j])
            for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                if 0<=i+di<m and 0<=j+dj<n and grid[di+i][dj+j] == 1 and (di+i,dj+j) not in self.seen:
                    queue.append((di+i,dj+j))
                    self.seen.add((di+i,dj+j))
        
        return island