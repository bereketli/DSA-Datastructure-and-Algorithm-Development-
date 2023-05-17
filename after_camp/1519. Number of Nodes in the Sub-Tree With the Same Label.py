from collections import defaultdict
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        count = [0] * n

        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
    
        def dfs(node, visited):
         
            if node == None:
                return {}
            visited.add(node)
            output = defaultdict(int)
            output[labels[node]] += 1

            for child in graph[node]:
                if child not in visited:
                    sub = dfs(child, visited)
                    for ky in sub:
                        output[ky] += sub[ky]
           
            count[node] = output[labels[node]]
            return output

        visited = set()
        dfs(0, visited)
        return count
