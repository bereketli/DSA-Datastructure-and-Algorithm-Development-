class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        if not matrix:
            return ans
        
        row, col = len(matrix), len(matrix[0])
        startR, startCol = 0, 0
        
        while startR < row and startCol < col:
            for i in range(startCol, col):
                ans.append(matrix[startR][i])
            startR += 1
            
            for i in range(startR, row):
                ans.append(matrix[i][col - 1])
            col -= 1
            
            if startR < row:
                for i in range(col - 1, startCol - 1, -1):
                    ans.append(matrix[row - 1][i])
                row -= 1
                
            if startCol < col:
                for i in range(row - 1, startR - 1, -1):
                    ans.append(matrix[i][startCol])
                startCol += 1
        
        return ans


        
