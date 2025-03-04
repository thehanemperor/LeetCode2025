class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        return self.followUp(board)
        m = len(board)
        n = len(board[0])
        copy = [[board[i][j] for j in range(n)] for i in range(m)]
        neighbor= [(0,1),(1,0),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        for i in range(m):
            for j in range(n):
                live = 0
                for x,y in neighbor:
                    if 0<=i+x<m and 0<=j+y<n and board[i+x][j+y] == 1:
                        live += 1

                if live < 2:
                    copy[i][j] = 0

                if live >3:
                    copy[i][j] = 0

                if board[i][j] == 0 and live == 3:
                    copy[i][j] = 1

        for i in range(m):
            for j in range(n):
                board[i][j] = copy[i][j]

    def followUp(self,board):
        m = len(board)
        n = len(board[0])
        neighbor= [(0,1),(1,0),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        for i in range(m):
            for j in range(n):
                live = 0
                for x,y in neighbor:
                    if 0<=i+x<m and 0<=j+y<n and abs(board[i+x][j+y]) == 1:
                        live += 1

                if live < 2 and board[i][j] == 1:
                    board[i][j] = -1

                if live >3 and board[i][j] == 1:
                    board[i][j] = -1

                if board[i][j] == 0 and live == 3:
                    board[i][j] = 2

        for i in range(m):
            for j in range(n):
                if board[i][j] >0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0