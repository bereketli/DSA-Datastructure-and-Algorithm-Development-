class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        output=[[0]*n for i in range(m)]
        print(output)
        for i in range(len(matrix)):
            for j in range( len(matrix[0])):
                print(i, j)
                output[j][i]= matrix[i][j]
        return output
        