class Solution:
    def countArrangement(self, n: int) -> int:
        self.count = 0
        visited = set()
        def beautiful(visited, perm, idx):
            
            if len(perm) == n:
              self.count += 1
              return
            
            for i in range(1, n + 1):
                if i  not in  visited and (idx % i  == 0 or i % idx == 0):      
                    perm.append(i) 
                    visited.add(i)
                    beautiful(visited, [] + perm, idx + 1)
                    visited.remove(i)
                    perm.pop()
                    
            return 
        beautiful(visited, [], 1)
        return self.count
        


        
