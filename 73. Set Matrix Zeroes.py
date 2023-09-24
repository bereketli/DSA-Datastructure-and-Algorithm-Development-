class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])
        
        arr_row = [False] * row
        arr_col = [False] * col
        
        # Finding the zeros in the Matrix
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    arr_row[i] = True
                    arr_col[j] = True
        
        # Updating the Row
        for i in range(row):
            if arr_row[i]:
                for j in range(col):
                    matrix[i][j] = 0
        
        for i in range(col):
            if arr_col[i]:
                for j in range(row):
                    matrix[j][i] = 0
        
