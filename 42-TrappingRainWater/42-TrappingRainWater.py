class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                mid = stack.pop()
                if not stack:
                    break
                
                boundHeight = min(height[i], height[stack[-1]]) - height[mid]
                length = i - stack[-1] -1
                area = boundHeight * length
                res += area

            stack.append(i)

        return res