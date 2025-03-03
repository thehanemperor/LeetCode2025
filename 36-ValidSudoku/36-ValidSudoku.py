class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[] for _ in range(9)]
        col = [[] for _ in range(9)]
        grid = [[] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if not board[i][j].isdigit():
                    continue
                num = int(board[i][j])
                if not 0<=num<=9:
                    return False
                if num not in row[i]:
                    row[i].append(num)
                else:
                    return False
                if num not in col[j]:
                    col[j].append(num)
                else:
                    return False

                gr = i //3 *3
                gc = j //3
                if num not in grid[gr+gc]:
                    grid[gr+gc].append(num)
                else:
                    return False

        return True