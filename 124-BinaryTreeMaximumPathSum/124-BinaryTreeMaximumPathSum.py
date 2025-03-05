# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -float("inf")
        self.dfs(root)
        return self.res
    def dfs(self, root):
        if not root:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        self.res = max(self.res, root.val, root.val+left+right, root.val+left, root.val +right)
        return max(root.val+left, root.val +right, root.val) 

        