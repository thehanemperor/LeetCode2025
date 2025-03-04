class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0
        for n in seen:
            if n-1 not in seen:
                curr = n
                step = 0
                while curr in seen:
                    step += 1
                    curr += 1
                res = max(res,step)

        return res