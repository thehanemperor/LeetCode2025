# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = -float("inf")
        self.resPath = None
        self.followUp(root)
        return sum(self.resPath)

    def dfs(self,root):
        if not root:
            return 0

        left = max(0,self.dfs(root.left))
        right = max(0, self.dfs(root.right))
        curr = root.val + left + right
        self.res = max(self.res, curr)

        return max(root.val + left, root.val+right)

    def followUp(self,root):
        if not root:
            return 0,[]

        leftMax,leftPath = self.followUp(root.left)
        rightMax,rightPath = self.followUp(root.right)

        if leftMax<0:
            leftMax = 0
            leftPath = []

        if rightMax<0:
            rightMax = 0
            rightPath = []

        currentMax = root.val + leftMax + rightMax
        if leftMax >0 and rightMax>0:
            currentPath = leftPath+ [root.val]+ rightPath
        elif leftMax >0:
            currentPath = leftPath + [root.val]
        elif rightMax >0:
            currentPath = [root.val] + rightPath
        else:
            currentPath = [root.val]

        if currentMax > self.res:
            self.res = currentMax
            self.resPath = currentPath

        if leftMax > rightMax:
            return root.val + leftMax, leftPath +[root.val]
        else:
            return root.val + rightMax, [root.val] + rightPath



