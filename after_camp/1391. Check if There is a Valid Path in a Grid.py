class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        def possiblePath(node, child):
            x, y, value = node
            r, c = child
            node_val = value
            child_val = grid[r][c]

            if node_val == 1:
                if y - 1 == c and grid[r][c] in set([1, 4, 6]):
                    return True
                elif y + 1 == c and grid[r][c] in set([1, 3, 5]):
                    return True

            elif node_val == 2:
                if x - 1 == r and grid[r][c] in set([2, 3, 4]):
                    return True

                elif x + 1 == r and grid[r][c] in set([2, 5, 6]):
                    return True

            elif node_val == 3:
                if y - 1 == c and grid[r][c] in set([1,4, 6]):
                    return True
                elif x + 1 == r and grid[r][c] in set([2, 5, 6]):
                    return True
            elif node_val == 4:
                if y + 1 == c and grid[r][c] in set([1, 3, 5]):
                    return True
                elif x + 1 == r and grid[r][c] in set([2, 5, 6]):
                    return True
            elif node_val == 5:
                if y - 1 == c and grid[r][c] in set([1, 4, 6]):
                    return True
                elif x - 1 == r and grid[r][c] in set([2, 3, 4]):
                    return True
            elif node_val == 6:
                if y + 1 == c and grid[r][c] in set([1, 3, 5]):
                    return True
                elif x - 1 == r and grid[r][c] in set([2, 3, 4]):
                    return True
            return False

            
        
        self.output = False
        def dfs(node, grid):
            x, y = node
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                self.output = True
                return

            neighbours = [(x - 1, y),(x + 1, y), (x, y - 1), (x, y+1 ) ]
            value = grid[x][y]
            grid[x][y] = 0
            
            for child in neighbours:
                r, c = child
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c]:
                    if possiblePath((x, y, value), child):
                        dfs(child, grid)
            
            return

        dfs((0,0), grid)
        return self.output
