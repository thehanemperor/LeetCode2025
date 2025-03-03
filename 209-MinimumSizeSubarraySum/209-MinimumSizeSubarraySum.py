class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("inf")
        n = len(nums)
        curr = 0
        left = 0
        for i in range(n):
            curr += nums[i]
            while curr >= target:
                res = min(res, i-left+1)
                curr -= nums[left]
                left += 1

        return res if res != float("inf") else 0