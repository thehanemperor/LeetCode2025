// Last updated: 3/22/2025, 12:42:21 AM
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
                if num not in row[i]:
                    row[i].append(num)
                else:
                    return False

                if num not in col[j]:
                    col[j].append(num)
                else:
                    return False

                gdex = 3 * (i//3) + j//3
                if num not in grid[gdex]:
                    grid[gdex].append(num)
                else:
                    return False

        return True