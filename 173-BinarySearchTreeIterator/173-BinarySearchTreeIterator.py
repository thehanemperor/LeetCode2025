# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        self.construct(root)
        self.index=0

    def next(self) -> int:
        curr = self.arr[self.index]
        self.index += 1
        return curr

    def hasNext(self) -> bool:
        return self.index < len(self.arr)

    def construct(self,root):
        if not root:
            return
        self.construct(root.left)
        self.arr.append(root.val)
        self.construct(root.right)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()