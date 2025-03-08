class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        return self.followUp(nums)
        n = len(nums)
        seen = [False] * (n+1)

        for num in nums:
            if 0< num <=n:
                seen[num] = True

        for i in range(1,n+1):
            if not seen[i]:
                return i

        return n+1

    def followUp(self,nums): # O(1) Space
        n = len(nums)
        i = 0
        while i < n:
            indexGoTo = nums[i]-1
            while 0<nums[i]<=n and nums[i] != nums[indexGoTo]:
                nums[i], nums[indexGoTo] = nums[indexGoTo], nums[i]
                indexGoTo = nums[i]-1
            
            i += 1    

        for i in range(n):
            if nums[i] != i+1:
                return i+1

        return n+1

        return n+1
