from collections import defaultdict, deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        reverse = [[] for i in range(len(graph))]
        indegree = [0] * len(graph)
        safenodes = []
        que = deque()
        # reconstruct the graph in reverse and count indegree
        for i, childs in enumerate(graph):
            indegree[i] = len(childs)
            for child in childs:
                reverse[child].append(i)
        
        #find all the terminal nodes
        for i in range(len(graph)):
            if not indegree[i]:
                que.append(i)

        while que:
            node = que.popleft()
            safenodes.append(node)
            for child in reverse[node]:
                indegree[child] -= 1
                if not indegree[child]:
                    que.append(child)
        safenodes.sort()
        return safenodes

