class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        distance = [[float("inf") for _ in range(n)] for _ in range(m)]
        distance[start[0]][start[1]] = 0
        self.dfs(maze,start,distance)
        endx,endy = destination

        return distance[endx][endy] if distance[endx][endy] != float("inf") else -1

    def dfs(self,maze,curr,distance):
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        x,y = curr
        m = len(maze)
        n = len(maze[0])
        for dx,dy in directions:
            step = 0
            i = x # reset 
            j = y # reset
            while 0<= i+dx<m and 0<=j+dy<n and maze[i+dx][dy+j] == 0:
                
                i += dx
                j += dy
                step += 1
            
            if distance[x][y] + step < distance[i][j]:
                distance[i][j] = distance[x][y] + step
                self.dfs(maze,[i,j],distance)
        

        
