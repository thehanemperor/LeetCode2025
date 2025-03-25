# Last updated: 3/25/2025, 1:10:33 AM
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = {}
        n = len(bombs)
        for i in range(n):
            if i not in graph:
                    graph[i] = []
            for j in range(n):
                if i == j:
                    continue 
                
                
                if j not in graph:
                    graph[j] = []
                xi,yi,ri = bombs[i]
                xj,yj,rj = bombs[j]
                distance = sqrt((xi -xj)**2 + (yi -yj)**2)
                if ri >= distance:
                    graph[i].append(j)

        res = 0
        for i in range(n):
            seen = set()
            seen.add(i)
            res = max(res,self.dfs(graph,seen,i))

        return res

    def dfs(self,graph,seen,index):
        for nei in graph[index]:
            if nei not in seen:
                seen.add(nei)
                self.dfs(graph,seen,nei)
        return len(seen)
        