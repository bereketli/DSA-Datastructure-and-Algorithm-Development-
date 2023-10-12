from collections import defaultdict
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:

        graph = defaultdict(list)
        visited = set()
        self.count = 0
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        def dfs(node):
            visited.add(node)
            previous = values[node]

            for child in graph[node]:
                 if child not in visited:
                    val_child = dfs(child)

                    if val_child % k == 0:
                        self.count += 1
                    
                    else:
                        previous += val_child
                    
            
            return previous
        
        dfs(0)
        return self.count + 1
                

            
        
