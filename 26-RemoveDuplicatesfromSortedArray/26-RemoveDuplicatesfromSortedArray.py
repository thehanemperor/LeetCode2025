class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        seen = set()
        for i in range(len(nums)):
            if nums[i] not in seen:
                nums[left] = nums[i]
                left += 1
            seen.add(nums[i])

        return left