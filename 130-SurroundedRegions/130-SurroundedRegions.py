class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        edges = []
        for i in range(m):
            for j in range(n):
                if (i in [0,m-1] or j in [0,n-1]) and board[i][j] == "O":
                    edges.append((i,j))

        self.bfs(deque(edges),board,"E")

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    self.bfs(deque([(i,j)]), board, "X")

        for i in range(m):
            for j in range(n):
                if board[i][j] == "E":
                    board[i][j] = "O"

        
    def bfs(self,queue,board,mark):
        m = len(board)
        n = len(board[0])
        while queue:
            x,y = queue.popleft()
            board[x][y] = mark
            for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                if 0<=x+dx<m and 0<=y+dy<n and board[dx+x][dy+y] == "O":
                    queue.append((dx+x,dy+y))
                    board[dx+x][y+dy] = mark