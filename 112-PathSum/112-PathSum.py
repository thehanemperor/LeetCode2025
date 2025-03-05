# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.dfs(root,targetSum)

    def dfs(self,root,target):
        
        if not root:
            return False
        
        if not root.left and not root.right and root.val-target==0:
            return True
        
        
        
        left = self.dfs(root.left,target-root.val)
        right = self.dfs(root.right,target-root.val)

        return left or right