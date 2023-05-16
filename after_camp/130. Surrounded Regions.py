class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        def dfs(node, board):
            x, y = node 
            if board[x][y] != "O" :
                return 

            neghbours = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            board[x][y] = 0
            
            for row , col in neghbours:
                if 0 <= row < m and 0 <= col < n:
                    dfs((row, col), board)
       
        for i in range(m):
            for j in range(n):
                if (i == m -1 or i == 0 or j == n - 1 or j == 0) and board[i][j] == "O":
                    
                    dfs((i, j), board)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif not board[i][j]:
                    board[i][j] = "O"
        return board




        



        """
        Do not return anything, modify board in-place instead.
        """
