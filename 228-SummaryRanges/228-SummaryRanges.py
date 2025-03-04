class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        left = right = 0
        n = len(nums)
        res = []
        while right < n:
            while right +1 <n and nums[right+1] - nums[right] == 1:
                right += 1
            if left == right:
                res.append(str(nums[right]))
            else:
                res.append("{}->{}".format(str(nums[left]), str(nums[right])))
            
            right += 1
            left = right

        return res