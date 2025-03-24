# Last updated: 3/24/2025, 2:58:48 AM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n -1
        while left <= right:
            mid = left +(right-left)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[n-1]:
                left = mid + 1
            else:
                right = mid -1

        if nums[left] <= target <= nums[n-1]:
            right = n-1
        else:
            right = left
            left = 0
        print(left,right)
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid +1
            else:
                right = mid -1

        return -1