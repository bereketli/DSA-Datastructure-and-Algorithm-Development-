class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0
        self.area = 0
        def area(row, col, grid, visited):
            if not(0 <= row < len(grid)) or not(0 <= col < len(grid[0])) or not grid[row][col] or (row, col) in visited:
                return
            
            
            self.area += 1
            visited.add((row, col))
            area(row -1, col, grid, visited) # top
            area(row + 1, col, grid, visited) # bottom
            area(row, col - 1, grid, visited) # left
            area(row, col + 1, grid, visited) # right
            return
        
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                    if (row, col) not in visited and grid[row][col]:
                        area(row, col, grid, visited)
                    maxarea = max(maxarea, self.area)
                    self.area = 0
        return maxarea
