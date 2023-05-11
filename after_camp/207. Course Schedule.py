from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        que = deque()
        taken_courses = []

        #build the graph and count indegree of each node
        for node, prerequisitie in prerequisites:
            graph[prerequisitie].append(node)
            indegree[node] += 1
        
        #finding nodes with not prerequisties to start
        for idx in range(numCourses):
            if not indegree[idx]:
                que.append(idx)

        while que:
            node = que.popleft()
            taken_courses.append(node)
            for child in graph[node]:
                indegree[child] -= 1
                if not indegree[child]:
                    que.append(child)
        
        return True if len(taken_courses) == numCourses else False

        
        

        

