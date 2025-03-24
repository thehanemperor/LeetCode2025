# Last updated: 3/24/2025, 3:54:12 PM
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        left = 0
        right = n -1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[right]:
                right -= 1
            elif nums[mid] < nums[right]:
                #  2,5,6,0,0,0,1,2  
                if target >= nums[mid] and target <= nums[right]:
                    #  target = 1 target has is between [mid, right]
                    left = mid + 1
                else:
                    right = mid - 1

            else:
                #  2,5,6,6,0,0,1,2 
                if target <= nums[right] or target >= nums[mid]:
                    left = mid + 1
                else:
                    right = mid -1

        return False