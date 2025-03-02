class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = i = 0
        while i<len(nums):
            curr = nums[i]
            nums[left] = nums[i]
            left += 1
            i += 1
            if i < len(nums) and nums[i] == nums[i-1]:
                nums[left] = nums[i]
                left += 1
                i += 1
                while i <len(nums) and nums[i] == nums[i-1]:
                    i += 1

        return left

                