from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        x, y = entrance
        que = deque()
        maze[x][y] = "+"
        que.append(((x,y), 0))

        while que:
            node, distance =  que.popleft()
            x, y = node
            neghbours = [(x -1, y), (x + 1, y), (x, y-1), (x, y + 1)]
            
            for row, col in neghbours:

                if 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] == ".":
                    if (row == 0 or row == len(maze) -1 or col == 0 or col == len(maze[0]) - 1):
                        return distance + 1
                    maze[row][col] = "+"
                    que.append([(row, col), distance + 1])
        return -1
        
