class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {chr(i) : chr(i) for i in range(97, 97 + 26) }
        size = [1] * (26)
        def find(node):
          
            while node != parent[node]:
                node = parent[node]
            return node
        
        def union(node1, node2):
            rootnode1 = find(node1)
            rootnode2 = find(node2)

            if rootnode1 != rootnode2:
                if size[ord(rootnode1) - 97 ] > size[ord(rootnode2) - 97]:
                    parent[rootnode2] = parent[rootnode1]
                    size[ord(rootnode1) - 97] += size[ord(rootnode2) - 97]
                else:
                    parent[rootnode1] = rootnode2
                    size[ord(rootnode2) - 97] += size[ord(rootnode1) - 97]
        
        for relation in equations:
           if relation[1:3] == "==":
                union(relation[0], relation[3])
        
        for relation in equations:
           if relation[1:3] == "!=":
               if find(relation[0]) == find(relation[3]):
                   return False
        
        return True


        

