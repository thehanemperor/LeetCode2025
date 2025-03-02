class Solution:
    def majorityElement(self, nums: List[int]) -> int:
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