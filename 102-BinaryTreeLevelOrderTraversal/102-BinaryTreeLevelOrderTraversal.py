# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append((root,0))
        res = []

        while queue:
            curr,level = queue.popleft()
            if level == len(res):
                res.append([curr.val])
            else:
                res[level].append(curr.val)

            if curr.left:
                queue.append((curr.left, level+1))
            
            if curr.right:
                queue.append((curr.right, level+1))

        return res