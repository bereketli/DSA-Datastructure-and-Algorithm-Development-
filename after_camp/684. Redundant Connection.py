class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.output = [0, 0]
        graph = {i :[i , 1] for i in range(1, len(edges) + 1)}
        def find(node):
            while node != graph[node][0]:
                node = graph[node][0]
            return node
        def union (node1, node2):
            rootnode1 = find(node1)
            rootnode2 = find(node2)
           
            if rootnode1 != rootnode2:
                if graph[rootnode1][1] > graph[rootnode2][1]:
                    graph[rootnode2][0] = graph[rootnode1][0]
                    graph[rootnode1][1] += graph[rootnode2][1]
                    
                else:
                    graph[rootnode1][0] = rootnode2
                    graph[rootnode2][1] += graph[rootnode1][1]
            else:
                self.output = [node1, node2]

        for node1, node2 in edges:
            union(node1, node2)
         
        return self.output

        
            
         
