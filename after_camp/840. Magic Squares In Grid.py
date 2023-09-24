class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        
        magic_box_count = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                if self.is_a_magic_box(grid, i, j):
                    magic_box_count += 1
        
        return magic_box_count
    
    def is_a_magic_box(self, grid, x, y):
        if grid[x + 1][y + 1] != 5:
            return False
         
        if any(grid[i][j] % 2 != 0 for i, j in [(x, y), (x + 2, y), (x, y + 2), (x + 2, y + 2)]):
              return False
        
     
        if any(grid[i][j] % 2 == 0 for i, j in [(x + 1, y), (x, y + 1), (x + 1, y + 2), (x + 2, y + 1)]):
            return False
        
        if (grid[x][y] + grid[x][y + 1] + grid[x][y + 2] != 15 or
            grid[x + 2][y] + grid[x + 2][y + 1] + grid[x + 2][y + 2] != 15 or
            grid[x][y] + grid[x + 1][y] + grid[x + 2][y] != 15):
            return False
        
        return True
        
