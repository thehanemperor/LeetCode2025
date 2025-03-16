# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pathsum=float("-inf")
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.pathsum
    def helper(self,root):
        if not root:
            return 0
        left = max(0, self.helper(root.left))
        right = max(0, self.helper(root.right))
        self.pathsum=max(self.pathsum,left+right+root.val)
        return max(left,right)+root.val

        