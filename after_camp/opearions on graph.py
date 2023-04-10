from collections import defaultdict
class Operation:
    def __init__(self) -> None:
        self.graph = defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
       
    def vertex(self,u):
        
        if self.graph[u]:
            print(*self.graph[u])
        else:
            print()
gra = Operation()
vertices = int(input())
operation = int(input())
for _ in range(operation):
    op = list(map(int, input().split()))
    if op[0] == 1:
        gra.addEdge(op[1],op[2])
    else:
        gra.vertex(op[1])

