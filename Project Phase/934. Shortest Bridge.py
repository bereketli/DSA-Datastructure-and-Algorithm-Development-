from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        islandOne, queue, visited = deque(), deque(), set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    islandOne.append([r, c])
                    queue.append([r, c])
                    visited.add((r, c))
                    break
            if len(islandOne) == 1:
                break
        
        def is_valid(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        while queue:
            size = len(queue)
            for _ in range(size):
                row, col = queue.popleft()
                for r, c in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    new_row, new_col = row + r, col + c
                    if (new_row, new_col) not in visited and is_valid(new_row, new_col) and grid[new_row][new_col] == 1:
                        queue.append([new_row, new_col])
                        islandOne.append([new_row, new_col])
                        visited.add((new_row, new_col))
        
        number_of_moves = 0
        while islandOne:
            size = len(islandOne)
            for _ in range(size):
                row, col = islandOne.popleft()
                for r, c in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    new_row, new_col = row + r, col + c

                    if (new_row, new_col) not in visited and is_valid(new_row, new_col):
                        if grid[new_row][new_col] == 1:
                            return number_of_moves

                        islandOne.append([new_row, new_col])
                        visited.add((new_row, new_col))
            number_of_moves += 1
