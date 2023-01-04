class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rowstore = {}
        columnstore ={}
        for i in range(len(grid)):
            col = []
            for j in range(len(grid[0])):
                col.append(str(grid[i][j]))
            col = " ".join(col)
            if col not in columnstore:
                columnstore[col] = 1
            else:
                columnstore[col] += 1
        for i in range(len(grid[0])):
            row = []
            for j in range(len(grid)):
                row.append(str(grid[j][i]))
            row = " ".join(row)
            if row not in rowstore:
                rowstore[row] = 1
            else:
                rowstore[row] += 1
        
        count = 0
        for row in rowstore:
            if row in columnstore:
                count += (rowstore[row] * columnstore[row] )
      
        return count
               
