class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        left,right = 0,len(nums)-1
        while left <= right:
            mid = (left + right) //2
            if mid +1 <len(nums) and nums[mid]> nums[mid + 1]:
                right = mid - 1
            else:
                left = mid + 1

        return left if left < len(nums) else left -1