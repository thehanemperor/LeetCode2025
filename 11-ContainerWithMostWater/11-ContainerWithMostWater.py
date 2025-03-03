class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        n = len(height)
        left,right = 0,n-1
        while left <right:
            curr = (right-left) * min(height[left], height[right])
            res = max(res, curr)
            if height[left] < height[right]:
                left += 1
            else:
                right -=1 

        return res

        