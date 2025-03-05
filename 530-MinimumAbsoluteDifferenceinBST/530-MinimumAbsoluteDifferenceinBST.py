# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.arr = []
        self.dfs(root)
        res = float("inf")
        for i in range(1,len(self.arr)):
            res = min(res, self.arr[i]-self.arr[i-1])

        return res

    def dfs(self,root):
        if not root:
            return 
        self.dfs(root.left)
        self.arr.append(root.val)
        self.dfs(root.right)

        