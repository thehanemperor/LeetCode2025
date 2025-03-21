// Last updated: 3/21/2025, 1:46:47 AM
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower,upper]]
        left = lower
        n = len(nums)
        i = 0
        res = []
        while i < n:
            if left < nums[i]:
                res.append([left,nums[i]-1])
            while i+1 <n and nums[i]+1 == nums[i+1]:
                i += 1

            left = nums[i]+1
            i += 1

        if upper > nums[n-1]:
            res.append([nums[n-1]+1,upper])

        return res