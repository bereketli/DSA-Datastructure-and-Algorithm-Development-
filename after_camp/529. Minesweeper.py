class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x, y = click
        if board[x][y] == "M":
            board[x][y]  = "X"
            return board
        def dfs(node, visited, board):
            
            x, y = node
            adjecents = [(x -1, y), (x + 1, y), (x, y - 1), (x, y + 1),
             (x + 1, y + 1), (x + 1, y- 1), (x -1, y + 1), (x -1, y -1)]
            count_mines = 0
            for row, col in adjecents:
                
                if 0 <= row < len(board) and 0 <= col < len(board[0]):
                    
                    if board[row][col] == "M":
                        
                        count_mines += 1
            if count_mines:
                board[x][y] = str(count_mines)
                return
            visited.add((x, y))
            for row, col in adjecents:
                if 0 <= row < len(board) and 0 <= col < len(board[0]) and (row, col) not in visited:

                    dfs((row, col), visited, board)
            board[x][y] = "B"
            return
        dfs((x, y), set(), board)
        return board

                        

