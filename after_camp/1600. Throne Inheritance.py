from collections import defaultdict
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.successors = defaultdict(list) 
        self.successors[kingName] = []
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.successors[parentName].append(childName)    

    def death(self, name: str) -> None:
        self.dead.add(name)
    def getInheritanceOrder(self) -> List[str]:
        def dfs(node, order):
            if node not in self.dead:
                order.append(node)
            if node not in self.successors:
                return

            for child in self.successors[node]:
                dfs(child,order)
            return order
       
        return dfs(self.kingName,[])
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
