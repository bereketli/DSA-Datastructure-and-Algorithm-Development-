class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent, size, score = [], [], []

        for i in range(n + 1):
            parent.append(i)
            size.append(1)
            score.append(float("inf"))
        
        def find(node):
            while node != parent[node]:
                node = parent[node]
            return node
        def union(node1, node2, weight):
            root_node1 = find(node1)
            root_node2 = find(node2)
            if size[root_node1] > size[root_node2]:
                parent[root_node2] = parent[root_node1]
                size[root_node1]  += size[root_node2]
                score[root_node1] = min(score[root_node2], score[root_node1],weight)
            else:
                parent[root_node1] = parent[root_node2]
                size[root_node2] += size[root_node1]
                score[root_node2] = min(score[root_node2], score[root_node1], weight)


        for node1, node2, weight in roads:
          
            union(node1, node2, weight)

        return score[find(1)]


        
        

        


        
