class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adj = [[] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if i!=j and isConnected[i][j] == 1:
                    adj[i].append(j)
        print(adj)
        seen = set()
        count = 0
        for i in range(n):
            if not adj[i]:
                count += 1
                continue

            if i in seen:
                continue

            seen.add(i)
            queue = deque([i])
            while queue:
                x = queue.popleft()
                for nei in adj[x]:
                    if nei not in seen:
                        seen.add(nei)
                        queue.append(nei)

            count += 1

        return count