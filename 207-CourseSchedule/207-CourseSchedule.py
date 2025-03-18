class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for after,prev in prerequisites:
            graph[prev].append(after)

        indegree = [0] * numCourses

        for i in range(len(graph)):
            for curr in graph[i]:
                indegree[curr] += 1
        
        seen = set()
        queue = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            prevCourse = queue.popleft()
            seen.add(prevCourse)
            for nextCourse in graph[prevCourse]:
                indegree[nextCourse] -= 1
                if indegree[nextCourse] == 0 and nextCourse not in seen:
                    seen.add(nextCourse)
                    queue.append(nextCourse)

        if sum(indegree):
            return False
        
        return True
