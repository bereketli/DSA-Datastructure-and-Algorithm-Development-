class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        self.inrange = [[] for i in range(len(bombs))]
        for i, circle_i in enumerate(bombs):
            xi, yi, ri = circle_i
            for j in range(i + 1, len(bombs)):
                xj, yj, rj = bombs[j]
                distance = sqrt(((xi - xj) ** 2) + ((yi - yj) ** 2))
                if distance <= ri:
                    self.inrange[i].append(j)
                if distance <= rj:
                    self.inrange[j].append(i)
        
        
        maxbomb = 0
        def dfs(list,node, bombs):
            self.visited[node] = 1

            for num in self.inrange[node]:
                if not self.visited[num]:
                    bombs = dfs(list, num, bombs) + 1
                
            return bombs
        for i in range(len(bombs)):
                self.visited = [0] * len(bombs)
                maxbomb = max(maxbomb, dfs(self.inrange,i, 0))
      
        return maxbomb + 1
