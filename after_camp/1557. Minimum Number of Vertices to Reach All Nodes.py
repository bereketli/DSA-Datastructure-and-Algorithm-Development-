class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:  
        reachable = set()
        vertices = set()
        for edge in edges:
                if edge[0] not in reachable:
                    reachable.add(edge[0])
                    reachable.add(edge[1])
                    vertices.add(edge[0])
                else:
                    reachable.add(edge[1])
                if edge[1] in vertices:
                    vertices.remove(edge[1])
        return list(vertices)
                



