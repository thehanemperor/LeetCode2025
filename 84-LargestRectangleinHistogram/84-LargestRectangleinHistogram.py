class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        res = min(heights) * n
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                right = i
                mid = stack.pop()
                left = stack[-1] if stack else -1
                high = heights[mid]
                area = high * (right-left - 1)
                res = max(res,area)

            stack.append(i)
        if not stack:
            return res
        right = stack[-1]
        while stack:
            
            mid = stack.pop()
            print(heights[mid])
            left = stack[-1] if stack else mid-1
            high = heights[mid]
            area = high * (right-left)
            res = max(res,area)

        return res
