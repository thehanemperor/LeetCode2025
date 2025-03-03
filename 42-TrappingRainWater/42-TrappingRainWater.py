class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        stack = []
        n = len(height)
        res = 0
        while i <n:
            while stack and height[i] > height[stack[-1]]:
                mid = stack.pop()
                if not stack:
                    continue # no left boundary

                distance = i - stack[-1] -1
                boundHeight = min(height[stack[-1]], height[i]) - height[mid]
                area = distance * boundHeight
                res += area

            stack.append(i)
            i += 1

        return res