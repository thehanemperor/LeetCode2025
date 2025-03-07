class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        n = len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue = deque([(i,j,0)])
                    while queue:
                        x,y,step = queue.popleft()
                        rooms[x][y] = step
                        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                            if 0<= dx+x < m and 0<=dy+y<n and rooms[dx+x][dy+y]!=-1 and rooms[dx+x][dy+y] > step + 1:
                                rooms[dx+x][dy+y] = step+1
                                queue.append((dx+x,dy+y,step+1))