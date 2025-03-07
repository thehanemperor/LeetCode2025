# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque()
        queue.append(root)
        count = 0
        while queue:
            curr = queue.popleft()
            count += 1
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)


        return count
    