class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        res = []
        n = len(nums)
        k %= n
        if k == 0:
            return 
        index = n -k
        for i in range(index,n):
            res.append(nums[i])

        for i in range(index+1):
            res.append(nums[i])
        
        for i in range(n):
            nums[i] = res[i]