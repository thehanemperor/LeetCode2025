"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(-1)
        root = head
        prev = dummy
        seen = {}
        while root:
            if root not in seen:
                curr = Node(root.val)
                seen[root] = curr
            else:
                curr = seen.get(root)
            
            prev.next = curr
            if not root.random:
                curr.random = None
            else:
                if root.random in seen:
                    curr.random = seen.get(root.random)
                else:
                    random = Node(root.random.val)
                    seen[root.random] = random
                    curr.random = random

            
            root = root.next
            prev = prev.next

        return dummy.next