# Last updated: 3/24/2025, 2:16:59 AM
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left = 0
        right = n-1
        res = []

        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] >= target:
                right = mid -1

            else:
                left = mid + 1

        if left == n or nums[left]!= target:
            return [-1,-1]
        
        res.append(left)

        left = 0
        right = n -1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid -1

        res.append(right)
        return res        