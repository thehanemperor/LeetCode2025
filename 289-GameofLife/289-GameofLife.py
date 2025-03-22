// Last updated: 3/22/2025, 1:45:38 AM
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        zero = []
        one = []
        m = len(board)
        n = len(board[0])
        neighbors = [(0,1),(1,0),(0,-1),(-1,0),(-1,1),(1,-1),(-1,-1),(1,1)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == 0:
                    liveCount = 0
                    for x,y in neighbors:
                        if 0<=x+i<m and 0<=y+j<n and board[i+x][j+y] == 1:
                            liveCount += 1

                    if liveCount == 3:
                        one.append((i,j))
                else:
                    liveCount = 0
                    deadCount = 0
                    for x,y in neighbors:
                        if 0<=x+i<m and 0<=y+j<n:
                            if board[x+i][y+j] == 0:
                                deadCount += 1
                            else:
                                liveCount += 1
                    if liveCount < 2 or liveCount>3:
                        zero.append((i,j))

        for i,j in zero:
            board[i][j] = 0

        for i,j in one:
            board[i][j] = 1