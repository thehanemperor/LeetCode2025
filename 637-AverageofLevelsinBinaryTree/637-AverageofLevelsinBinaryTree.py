# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque()
        res = []
        arr = []

        queue.append((root,0))

        while queue:
            curr,level = queue.popleft()
            if len(arr) == level:
                arr.append([curr.val])
            else:
                arr[level].append(curr.val)

            if curr.left:
                queue.append((curr.left,level+1))
            if curr.right:
                queue.append((curr.right,level+1))

        for level in arr:
            res.append(sum(level)/len(level))

        return res 