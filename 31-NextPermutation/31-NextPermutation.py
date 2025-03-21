// Last updated: 3/21/2025, 2:26:44 PM
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        right = n-1
        while right >=0:
            if right -1>=0 and nums[right-1]<nums[right]:
                break

            right -= 1

        
        if right == -1:
            nums.reverse()
            return 

        left = right -1
        right = n-1
        while right > left:
            if nums[right] > nums[left]:
                break
            right -= 1

        nums[left],nums[right] = nums[right],nums[left]
        i = left + 1
        j = n -1
        while i<j:
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
            j -= 1

        