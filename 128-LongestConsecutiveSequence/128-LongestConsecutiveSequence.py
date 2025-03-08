class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seen = set(nums)
        res = 1

        for num in seen:
            if num -1 not in seen:
                step = 1
                curr = num
                while curr + 1 in seen:
                    step += 1
                    curr = curr + 1

                res = max(res,step)

        return res