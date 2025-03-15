class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        decreasingQ = deque()
        
        for i in range(k):
            while decreasingQ and nums[decreasingQ[-1]] <= nums[i]:
                decreasingQ.pop()
            decreasingQ.append(i)
        res = []
        res.append(nums[decreasingQ[0]])

        for i in range(k,len(nums)):
            if decreasingQ and i - decreasingQ[0] == k:
                decreasingQ.popleft()
            while decreasingQ and nums[decreasingQ[-1]] <= nums[i]:
                decreasingQ.pop()
            
            decreasingQ.append(i)
            res.append(nums[decreasingQ[0]])

        return res
