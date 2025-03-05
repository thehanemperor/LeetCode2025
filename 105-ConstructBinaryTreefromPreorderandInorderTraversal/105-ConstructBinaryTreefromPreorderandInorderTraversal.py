# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.inorderMap = {}
        # must be global to track the preorder progress
        self.index = 0
        for i in range(len(inorder)):
            self.inorderMap[inorder[i]] = i

        return self.dfs(0,len(preorder)-1,preorder)

    
    def dfs(self,left,right,preorder):
        if left> right:
            return None

        rootVal = preorder[self.index]
        root = TreeNode(rootVal)
        self.index += 1

        root.left = self.dfs(left, self.inorderMap[rootVal]-1,preorder)
        root.right = self.dfs(self.inorderMap[rootVal]+1, right, preorder)
        
        return root