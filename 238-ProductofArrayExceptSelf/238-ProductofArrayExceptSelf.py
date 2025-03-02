class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n
        for i in range(1,n):
            left[i] = left[i-1] * nums[i-1]

        for i in range(n-2,-1,-1):
            right[i] = right[i+1] * nums[i+1]

        res = []

        for i in range(n):
            res.append(left[i]* right[i])

        return res

    def followUp(self,nums):
        n = len(nums)
        res = [1] * n

        for i in range(1,n):
            res[i] = nums[i-1] * res[i-1]

        mul = 1
        for i in range(n-1,-1,-1):
            
            res[i] *= mul
            mul *= nums[i]

        return res