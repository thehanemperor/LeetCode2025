class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.dfs(nums, [])
        return self.res

    def dfs(self, nums, arr):
        if len(arr) == len(nums):
            self.res.append([x for x in arr])
            return 
        
        for num in nums:
            if num not in arr:
                arr.append(num)
                self.dfs(nums,arr)
                arr.pop()