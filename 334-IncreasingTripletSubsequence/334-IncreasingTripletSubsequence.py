class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        minimum = [0] * n
        minimum[0] = nums[0]
        for i in range(1,n):
            minimum[i] = min(minimum[i-1], nums[i])

        stack = []
        for i in range(n-1,-1,-1):
            
            if not stack:
                stack.append(nums[i])
                continue

            if minimum[i]< nums[i]< stack[-1]:
                return True

            stack.append(max(nums[i],stack[-1]))

        return False