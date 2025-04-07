# Last updated: 4/7/2025, 12:41:28 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.depth = float("inf")
        self.dfs(root,1)
        return self.depth

    def dfs(self,root,level):
        if not root:
            return 
        
        if not root.left and not root.right:
            self.depth = min(self.depth, level)
            return

        self.dfs(root.left,level+1)
        self.dfs(root.right,level+1)