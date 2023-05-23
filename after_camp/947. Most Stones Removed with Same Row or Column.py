class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {(x, y) : (x, y) for x, y in stones}
        self.countset = len(stones)

        def find(node):
            while node != parent[node]:
                node = parent[node]
            return node

        def union(node1, node2):
            rootnode1 = find(node1)
            rootnode2 = find(node2)
           
            if rootnode1 != rootnode2:
                self.countset -= 1
                parent[rootnode2] = parent[rootnode1]
                
             
        for idx, stone in enumerate(stones):
            x, y = stone
            for a, b in stones[idx + 1: ]:
                if x == a or y == b :
                    union((x, y), (a, b))
                 
       
        return len(stones) - self.countset 
