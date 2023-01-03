class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:       
        rows={}
        for i in range(len(grid)):
            count0 =0
            count1 =0
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count1 += 1
                else:
                    count0 += 1
            rows[i] = [count0, count1]
        columns = {}
        for i in range(len(grid[0])):
            count0 =0
            count1 =0
            for j in range(len(grid)):
                if grid[j][i] == 1:
                    count1 += 1
                else:
                    count0 += 1
            columns[i] = [count0, count1]
        output = [["m"] * len(grid[0]) for i in range(len(grid)) ]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                output[i][j] = rows[i][1] + columns[j][1] - rows[i][0] - columns[j][0]
        return output

