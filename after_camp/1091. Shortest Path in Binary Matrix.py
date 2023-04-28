class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1
        if len(grid) == 1 and grid[0][0] == 0:
            return 1
            
        else:
            n = len(grid)
            visited = set([(0,0)])
            que = deque([[(0,0), 1]])
            visited = set([(0,0)])
          
            while que:
                node = que.popleft()
                
                i, j = node[0]
                neighbors =  [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), (i + 1, j + 1), (i + 1, j - 1), (i - 1, j - 1), (i - 1, j + 1)]
               
                for adj in neighbors:
                    row, col = adj
                    if  ((0 <= row < n and  0 <= col < n) and not grid[row][col]) and (row, col) not in visited:
                        if (row, col) == (n -1, n-1):
                            return node[1] + 1
                        que.append([(row, col), node[1] + 1])
                        visited.add((row, col))
                
            return -1
                      



        
