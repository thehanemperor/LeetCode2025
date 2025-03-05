# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        return self.dfs(root,0)

    def dfs(self,root, parent):
        if not root:
            return 0
        curr = parent*10 + root.val
        
        if not root.left and not root.right:
            return curr
        left = self.dfs(root.left, curr)
        right = self.dfs(root.right, curr)
        
        return left + right