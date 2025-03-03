class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        print(nums)
        for i in range(len(nums)):
            if i == 0 or nums[i-1] != nums[i]:
                target = 0 - nums[i]
                self.twoSum(nums,i,target,res)

        return res

    def twoSum(self,nums,index,target,res):
        seen = set()
        i = index+1
        while i < len(nums):
            
            
            if target - nums[i] in seen:
                # must add the fist non duplicate then skip
                res.append([nums[index], target-nums[i], nums[i]])
                while i+1 < len(nums) and nums[i+1] == nums[i]:
                    i += 1

            seen.add(nums[i])
            i += 1