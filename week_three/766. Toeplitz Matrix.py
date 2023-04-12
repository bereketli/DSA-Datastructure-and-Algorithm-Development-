class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for colu in range(n):
            i, j = 0, colu
            value = matrix[i][j]
            while i < m and j < n:
                if matrix[i][j] != value:
                    return False
                i += 1
                j += 1
        for row in range(m):
            i, j = row, 0
            value = matrix[i][j]
            while i < m and j < n:
                if matrix[i][j] != value:
                    return False
                i += 1
                j += 1
        return True
            
