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
        root = res
        queue = deque()
        queue.append((node,root))
        seen = {}
        visited = set()
        while queue:
            curr, copy = queue.popleft()
            seen[curr] = copy
            visited.add(curr)
            for nei in curr.neighbors:
                if nei not in seen:
                    seen[nei] = Node(nei.val)
                copy.neighbors.append(seen[nei])
                if nei not in visited:
                    queue.append((nei,seen[nei]))
                    visited.add(nei)

        return res
                