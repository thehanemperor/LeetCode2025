class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        n = len(heights)
        res = [0] * n
        for i in range(n-1,-1,-1):
            count = 0
            while stack and heights[stack[-1]] <= heights[i]:
                stack.pop()
                count += 1
            if not stack:
                res[i] = count
            else:
                res[i] = count + 1

            stack.append(i)

        return res
