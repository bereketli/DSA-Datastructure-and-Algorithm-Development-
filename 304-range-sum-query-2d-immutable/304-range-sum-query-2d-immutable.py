class NumMatrix(object):

    def __init__(self, matrix):
        self.matrix=matrix
        self.prefix_sum=matrix
        sum=0
        for i in range(len(self.matrix)):
            for j in range(1,len(self.matrix[0])):
                sum+=self.matrix[i][j]
                self.prefix_sum[i][j]+=self.prefix_sum[i][j-1]

    def sumRegion(self, row1, col1, row2, col2):
           i=row1
           sum=0
           while i<=row2:
                if col1>0:
                    sum+=(self.prefix_sum[i][col2]-self.prefix_sum[i][col1-1])
                else:
                    sum+=self.prefix_sum[i][col2]
                i+=1
           return sum

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)