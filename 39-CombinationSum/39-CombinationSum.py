class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(candidates, 0, target, [], res)
        return res
    def dfs(self, candidates, index, target, arr, res):
        if sum(arr) > target:
            return 
        if sum(arr) == target:
            res.append([x for x in arr])
            return
        
        for i in range(index, len(candidates)):
            arr.append(candidates[i])
            self.dfs(candidates, i, target, arr, res)
            arr.pop()