class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for i in range(len(equations)):
            (x,y),val = equations[i],values[i]
            if x not in graph:
                graph[x] = {y:val}
            else:
                graph[x][y] = val

            if y not in graph:
                graph[y] = {x:1/val}
            else:
                graph[y][x] = 1/val

        res = []
        for x,y in queries:
            if not x in graph or not y in graph:
                res.append(-1.0)
                continue
            queue = deque()
            queue.append((x, 1.0))
            seen = set()
            found = False
            while queue:
                node,value = queue.popleft()
                seen.add(node)
                if node == y:
                    res.append(value)
                    found = True
                    break
                for i in graph[node]:
                    if i not in seen:
                        queue.append((i, value*graph[node][i]))
            if not found:
                res.append(-1.0)

        return res