# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.index = len(inorder)-1
        self.check = {inorder[i]:i for i in range(len(inorder))}
        return self.dfs(postorder,0,len(postorder)-1)

    def dfs(self,postorder,left,right):
        if left>right:
            return None

        curr = postorder[self.index]
        root = TreeNode(curr)
        self.index -= 1
        root.right = self.dfs(postorder,self.check[curr]+1,right)
        root.left = self.dfs(postorder,left, self.check[curr]-1)

        return root
