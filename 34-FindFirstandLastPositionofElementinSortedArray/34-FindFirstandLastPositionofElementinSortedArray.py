class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.binary(nums,target,True), self.binary(nums,target,False)]
    def binary(self, nums,target, isSmall):
        begin, end = 0, len(nums)-1

        while begin <= end:
            mid = (begin + end)//2
            if nums[mid] == target:
                if isSmall:
                    if mid == begin or nums[mid-1] < target:
                        return mid
                    end = mid -1

                else:
                    if mid == end or nums[mid+1] > target:
                        return mid
                    
                    begin = mid +1
            elif nums[mid] < target:
                begin = mid + 1
            else:
                end = mid - 1

        return -1