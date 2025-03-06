class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) //2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1
        
        res = self.binSearch(0, left -1, nums, target)
        if res != -1:
            return res
        res = self.binSearch(left, len(nums)-1, nums, target)
        return res

    def binSearch(self, leftBound, rightBound, nums, target):
        left = leftBound
        right = rightBound
        while left <= right:
            mid = (left + right) //2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid -1
            else:
                left = mid + 1

        return -1  