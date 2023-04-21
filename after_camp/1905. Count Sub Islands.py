class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(row, col):
            if not (0<= row < len(grid2)) or not (0<= col < len(grid2[0])) or not grid2[row][col] or (row, col) in self.visited:
                return
            self.visited.add((row, col))
         
            if not grid1[row][col]:
                self.sum = False
            dfs(row -1, col) 
            dfs(row + 1, col) 
            dfs(row, col - 1) 
            dfs(row, col + 1)
        
        self.visited = set()
        count_iland = 0
        for row in range(len(grid2)):
            for col in range(len(grid2[0])):
                self.sum = True
                if grid2[row][col] and (row, col) not in self.visited:
                    dfs(row, col)
                    if self.sum:
                        count_iland += 1

        return count_iland
