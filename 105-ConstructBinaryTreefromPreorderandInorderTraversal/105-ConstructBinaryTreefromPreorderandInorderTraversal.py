# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.check = {inorder[i]:i for i in range(len(inorder))}
        self.index = 0
        return self.dfs(preorder,0,len(preorder)-1)

    def dfs(self,preorder,left,right):
        if left > right:
            return None

        root = TreeNode(preorder[self.index])
        inorderIndex = self.check[preorder[self.index]]
        self.index += 1
        root.left = self.dfs(preorder,left,inorderIndex-1)
        root.right = self.dfs(preorder,inorderIndex+1, right)

        return root

    