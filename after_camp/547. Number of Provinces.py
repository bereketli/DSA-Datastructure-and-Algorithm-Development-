class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
       
        
        def connected_cities(visited, row, grid):
           
            for city in range(len(grid)):
                if grid[row][city] and city not in visited:
                    visited.add(row)
                    if row != city:
                       connected_cities(visited, city, grid)
            
            return
        visited = set()
        count_province = 0
        for city in range(len(isConnected)):
            if city not in visited:
                count_province += 1
                connected_cities(visited, city, isConnected)
        return count_province

