class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row = len(matrix)
        col = len(matrix[0])
        self.prefix = [[0]*col for i in range(row) ]

        for i in range(row):
            sum = 0
            for j in range(col):
                sum += matrix[i][j]
                self.prefix[i][j] = sum
        
        for i in range(col):
            sum = 0
           
            for j in range(row):
                
                sum += self.prefix[j][i]
                temp = sum
                self.prefix[j][i] = temp
       
        
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        upper = self.prefix[row1 - 1][col2] if row1 != 0 else 0
        side = self.prefix[row2][col1 - 1] if col1 != 0 else 0
        reduced = upper + side - self.prefix[row1 - 1][col1 -1] if upper != 0 and side != 0 else upper + side
        summed = self.prefix[row2][col2] - reduced
        return summed
        
       


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)