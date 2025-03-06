class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.dfs(n,[],0,0)
        return self.res
    def dfs(self, n, arr, left, right):
        if len(arr) == 2 *n:
            self.res.append("".join(arr))
            return 

        if left < n:
            arr.append("(")
            self.dfs(n, arr, left + 1, right)
            arr.pop()
        if left > right:
            arr.append(")")
            self.dfs(n, arr, left, right + 1)
            arr.pop()