from collections import deque, defaultdict
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = [0] * n
        que = deque()
        output = [set() for i in range(n)]

        for node1, node2 in edges:
            graph[node1].append(node2)
            indegree[node2] += 1

        for i in range(n):
            if not indegree[i]:
                que.append(i)
            
        while que:
            node = que.pop()
            for child in graph[node]:
                indegree[child] -= 1
                if not indegree[child]:
                    que.append(child)
                output[child].add(node)
                
                output[child] = output[child].union(output[node]) 
               
        
        
        for i in range(n):
            output[i] = list(output[i])
            output[i].sort()

            
        
        return output
