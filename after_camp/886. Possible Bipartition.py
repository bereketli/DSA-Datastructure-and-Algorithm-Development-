class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
            self.order = [0]  * (n + 1)
            self.hater = [[]for i in range(n + 1)]
            for a, b in dislikes:
                self.hater[a].append(b)
                self.hater[b].append(a)
            self.out = True
            
            def dfs(list, color, node):
                if self.order[node]:
                   
                    if self.order[node] != color:
                        
                        self.out = False
                    return
                
                self.order[node] = color
                for num in self.hater[node]:
                    next_col = 1 if color == -1 else -1
                    dfs(list, next_col, num )
                return
            for i in range(1, n+1):
                if not self.order[i]:
                    dfs(self.hater, -1, i)
            
            
            return self.out
            

        
