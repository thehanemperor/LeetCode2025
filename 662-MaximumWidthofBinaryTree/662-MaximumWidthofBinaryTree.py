# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        queue = deque()
        queue.append((root,0,0))
        level = []
        while queue:
            curr,h,index = queue.popleft()
            if h == len(level):
                level.append([index])
            else:
                level[h].append(index)

            if curr.left:
                queue.append((curr.left,h+1,2*index))

            if curr.right:
                queue.append((curr.right,h+1, 2*index+1))

        for l in level:
            diff = l[-1] - l[0] +1
            res = max(res,diff)

        return res