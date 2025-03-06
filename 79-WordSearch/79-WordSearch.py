class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.res = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    tmp = board[i][j]
                    board[i][j] = "#"
                    found = self.backtrack(board, i, j, 1, word)
                    board[i][j] = tmp
                    if self.res == True:
                        return True

        return False
    def backtrack(self, board, i, j, index, word):
        
        if index == len(word):
            self.res = True
            return
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        for x,y in direction: 
                          
            if 0<= i+x < len(board) and 0<= j+y <len(board[0]) and board[i+x][j+y] == word[index] and board[i+x][j+y] !="#":
                before = board[i+x][j+y]
                board[i+x][j+y] = "#"
                self.backtrack(board,i+x, j+y, index+1, word)
                board[i+x][j+y] = before
        