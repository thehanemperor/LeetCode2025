class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        isCol = False
        for i in range(m):
            if matrix[i][0] ==0:
                    isCol = True
            for j in range(1, n):
                
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
       
        for i in range(1,m):
            for j in range(1,n):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0

        if isCol:
            for i in range(m):
                matrix[i][0] = 0