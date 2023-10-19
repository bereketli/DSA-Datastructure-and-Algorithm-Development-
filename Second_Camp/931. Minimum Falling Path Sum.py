class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        min_sum = {}
        def dp(row, col):
            if not 0<= row < len(matrix):
                return 0 

            if (row, col) in min_sum:
                return min_sum[(row, col)]
            
            next_element = [(row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]
            
            min_path = float(inf)
            
            for new_row, new_col in next_element:
                if 0<= new_col < len(matrix):
                    min_path = min(dp(new_row, new_col) + matrix[row][col], min_path)
                    
                
            min_sum[(row, col)] = min_path
            return min_sum[(row,col)]
        
        min_allsum = float("inf")
        for i in range(len(matrix)):
            min_allsum = min(dp(0, i), min_allsum)
            
        return min_allsum
    
        
