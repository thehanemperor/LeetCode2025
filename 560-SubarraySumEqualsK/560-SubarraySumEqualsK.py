class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        seen = {0:1} # any num minus itself get 0
        currentSum = 0
        for num in nums:
            currentSum += num
            if currentSum - k in seen:
                res += seen[currentSum-k]
            seen[currentSum] = seen.get(currentSum,0) + 1

        return res