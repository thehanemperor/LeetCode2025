class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        pre1 = [0,0]
        n = len(nums)
        odd = 0
        even = 0
        for i in range(n):
            if i%2==0:
                even += nums[i]
            else:
                odd += nums[i]

        pre2 = [even,odd]
        res = 0
        for i in range(n):
            pre2[i%2] -= nums[i]
            res += pre1[0] + pre2[1] == pre1[1] + pre2[0]
            pre1[i%2] += nums[i]

        return res