class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {chr(i) : chr(i) for i in range(97, 97 + 26) }
        output = []
        def find(node):
          
            while node != parent[node]:
                node = parent[node]
            return node
        
        def union(node1, node2):
            rootnode1 = find(node1)
            rootnode2 = find(node2)

            if rootnode1 != rootnode2:
                if rootnode1 < rootnode2:
                    parent[rootnode2] = rootnode1
                else:
                    parent[rootnode1] = rootnode2
        
        for node1, node2 in zip(s1, s2):
            union(node1, node2)

        for node in baseStr:
            smallest = find(node)
            output.append(smallest)
        output = "".join(output)

        return output


