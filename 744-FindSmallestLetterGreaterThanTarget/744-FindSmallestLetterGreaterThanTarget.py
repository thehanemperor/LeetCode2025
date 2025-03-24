# Last updated: 3/24/2025, 2:32:43 AM
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n -1
        if nums[left] <= nums[right]:
            return nums[left]

        while left <= right:
            mid = left + (right-left) //2
            if nums[mid] > nums[n-1]:
                left = mid + 1
            else:
                right = mid - 1

        return nums[left]
        