# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque()
        queue.append((root,0))
        res = []
        while queue:
            curr,level = queue.popleft()
            if len(res) == level:
                tmp = deque([curr.val])
                res.append(tmp)
            else:
                if level %2 == 0:
                    res[level].append(curr.val)
                else:
                    res[level].appendleft(curr.val)

            if curr.left:
                queue.append((curr.left,level+1))
            if curr.right:
                queue.append((curr.right,level+1))

        for i in range(len(res)):
            res[i] = list(res[i])

        return res