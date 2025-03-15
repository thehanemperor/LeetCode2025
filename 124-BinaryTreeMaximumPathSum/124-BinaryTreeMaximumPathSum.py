# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float('-inf')
        
        def dfs(node):
            if not node:
                return 0
            
            # Recursively get gains from left and right subtrees
            left_gain = max(0, dfs(node.left))
            right_gain = max(0, dfs(node.right))
            
            # Current path sum passing through this node (taking both children)
            current_path_sum = node.val + left_gain + right_gain
            
            # Update global maximum path sum
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # Return the maximum path sum going down from this node 
            # (either to the left or right, or none if negative)
            return node.val + max(left_gain, right_gain)
        
        dfs(root)
        return self.max_sum