# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = -float("inf")
        self.dfs(root)
        return self.res

    def dfs(self,root):
        if not root:
            return 0

        left = max(0,self.dfs(root.left))
        right = max(0, self.dfs(root.right))
        curr = root.val + left + right
        self.res = max(self.res, curr)

        return max(root.val + left, root.val+right)