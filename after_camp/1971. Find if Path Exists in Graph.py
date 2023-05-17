class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {i : i for i in range(n)}
        
        def find_parent(node):
            while graph[node] != node:
                node = graph[node]
            return node

        for node1, node2 in edges:
            graph[find_parent(node1)] = graph[find_parent(node2)]
        def union(source, destination):
            return find_parent(source) == find_parent(destination)
            
           
        return union(source, destination)
            
            
