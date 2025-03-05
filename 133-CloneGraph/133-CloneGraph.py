"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        res = Node(node.val)
        seen = {}
        queue = deque()
        queue.append((node,res))
        while queue:
            origin,copy = queue.popleft()
            seen[origin] = copy
            for nei in origin.neighbors:
                if nei in seen:
                    copy.neighbors.append(seen[nei])
                else:
                    tmp = Node(nei.val)
                    seen[nei] = tmp
                    copy.neighbors.append(tmp)
                    queue.append((nei,tmp))

        return res