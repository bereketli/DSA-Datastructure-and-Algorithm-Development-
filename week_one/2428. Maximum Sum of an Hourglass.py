class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
           
            prefi =[[0] * len(grid[0]) for g in grid]
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    
                        if i==0 and j ==0:
                            prefi[i][j] = grid[i][j]
                            continue
                        if j ==0:
                            prefi[i][j] = prefi[i -1][-1] + grid[i][j]
                        else:
                            prefi[i][j] = prefi[i][j -1] + grid[i][j]
        
            maxsum =0
            for i in range(len(prefi) - 2):
            
                for j in range(len(prefi[0]) -2):
                
                    previous1, previous2=0, 0
                    if i == 0 and j ==0:
                        previous1=0
                        previous2 = prefi[i + 1][-1]
                    elif j ==0:
                        previous2 = prefi[i + 1][-1]
                        previous1 = prefi[i -1][-1]
                    else:
                        previous1 =prefi[i][j -1]
                        previous2 =prefi[i +2][j -1]
                    maxsum = max(maxsum, (prefi[i][j +2] - previous1) + grid[i +1][j +1] +(prefi[i +2][j + 2] - previous2))
            
            return maxsum
                