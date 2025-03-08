# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        self.leaf = []
        self.dfs(root,[])

        res = 0
        for i in range(len(self.leaf)):
            for j in range(i+1, len(self.leaf)):
                leaf1 = self.leaf[i]
                leaf2 = self.leaf[j]
                for k in range(min(len(leaf1), len(leaf2))):
                    if leaf1[k] != leaf2[k]:
                        curr = len(leaf1) - k + len(leaf2) -k 
                        if curr <= distance:
                            res += 1
                        break
        return res
        

    def dfs(self,root,step):
        if not root:
            return 
        
        if not root.left and not root.right:
            step.append(root)
            self.leaf.append([x for x in step])
            return 
        step.append(root)
        
        self.dfs(root.left,[x for x in step])
        self.dfs(root.right,[x for x in step])