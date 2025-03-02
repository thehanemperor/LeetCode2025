class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        seen = set()
        for i in range(1,len(nums)):
            if nums[i-1] != nums[i]:
                nums[left] = nums[i]
                left += 1

        return left