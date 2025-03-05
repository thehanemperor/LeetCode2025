class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i ==m-1 or j == n-1) and board[i][j] == "O":
                    queue = deque([(i,j)])
                    self.bfs(queue,"E",board)
                
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    queue = deque([(i,j)])
                    self.bfs(queue,"X",board)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "E":
                    board[i][j] = "O"

    def bfs(self,queue,mark,board):
        m = len(board)
        n = len(board[0])
        while queue:
            x,y = queue.popleft()
            board[x][y] = mark
            for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:
                if 0<= x+i <m and 0<=y+j <n and board[x+i][y+j] == "O":
                    board[x+i][y+j] = mark
                    queue.append((x+i,j+y)) 