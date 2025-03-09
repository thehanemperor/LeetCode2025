class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        minimum = [0] * n
        minimum[0] = nums[0]
        for i in range(1,n):
            minimum[i] = min(minimum[i-1], nums[i])
        stack = []
        for i in range(n-1,-1,-1):
            if nums[i] < minimum[i]:
                continue
            while stack and stack[-1] <= minimum[i]:
                stack.pop()
            if stack and stack[-1] < nums[i]:
                return True

            stack.append(nums[i])

        return False
