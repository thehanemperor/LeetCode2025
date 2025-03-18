class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]

        for after,prev in prerequisites:
            graph[prev].append(after)

        indegree = [0] * numCourses
        for i in range(len(graph)):
            for cour in graph[i]:
                indegree[cour] += 1

        queue = deque()
        seen = set()
        res = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            prevCour = queue.popleft()
            seen.add(prevCour)
            res.append(prevCour)
            for afterCour in graph[prevCour]:
                indegree[afterCour] -= 1
                if indegree[afterCour] == 0 and afterCour not in seen:
                    seen.add(afterCour)
                    queue.append(afterCour)
        if len(seen) == numCourses:
            return res
        else:
            return []