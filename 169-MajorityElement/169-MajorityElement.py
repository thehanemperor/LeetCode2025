class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return self.followUp(nums)
        seen = {}
        for n in nums:
            seen[n] = seen.get(n,0) + 1
        maxKey = None
        maxVal = -float("inf")
        for k,v in seen.items():
            if v > maxVal:
                maxVal = v
                maxKey = k
        return maxKey

    def followUp(self,nums):
        # because the most frequent is over a half
        # we can store only one candidate count
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            if num != candidate:
                count -=1
            else:
                count += 1

        return candidate