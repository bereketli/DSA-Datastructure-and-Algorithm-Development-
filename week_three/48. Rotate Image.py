class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reverse(matrix)
        return matrix
        
    def transpose(self, matrix):
        for i in range(0, len(matrix)):
            for j in range(0, i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    def reverse(self, matrix):
        for column in range(0, int(len(matrix) / 2)):
            for row in range(0, len(matrix)):
                matrix[row][column], matrix[row][len(matrix)-1-column] = matrix[row][len(matrix)-1-column], matrix[row][column]
