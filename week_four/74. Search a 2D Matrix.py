class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if target == matrix[row][col]:
                     return True
        return False
            