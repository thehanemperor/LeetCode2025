# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        self.bfs(root)
        return root

    def dfs(self,root):
        if not root:
            return root

        left = self.dfs(root.left)
        right = self.dfs(root.right)
        root.right = left
        root.left = right
        return root

    def bfs(self,root):
        queue = deque()
        queue.append(root)

        while queue:
            curr = queue.popleft()
            left = curr.left
            right = curr.right
            curr.right = left
            curr.left = right
            if left:
                queue.append(left)
            if right:
                queue.append(right)