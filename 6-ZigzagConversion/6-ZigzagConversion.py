class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        arr = [[] for _ in range(numRows)]
        n = len(s)
        row = 0
        down = True
        for i in range(n):
            arr[row].append(s[i])

            if row == numRows -1:
                down = False    
            if row == 0 and not down:
                down = True
            if down:
                row += 1
            else:
                row -= 1

        res = ""
        for part in arr:
            for c in part:
                res += c

        return res