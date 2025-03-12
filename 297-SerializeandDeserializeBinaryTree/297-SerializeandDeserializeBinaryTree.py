# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        arr = []
        def dfs(root):
            if not root:
                arr.append("None")
                return 
            arr.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return ",".join(arr)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        arr = data.split(",")
        self.index = 0
        def dfs():
            if self.index <len(arr) and arr[self.index] == "None":
                self.index += 1
                return None
            
            root = TreeNode(int(arr[self.index]))
            self.index+= 1
            root.left = dfs()
            root.right = dfs()
            return root
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))