class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

        stor = [[0.0] * 101 for _ in range(101)]
        stor[0][0] = poured
        
        for i in range(query_row):
            for j in range(query_glass + 1):
                res = max(stor[i][j] - 1, 0)
                stor[i + 1][j] += res / 2
                stor[i + 1][j + 1] += res / 2
        
        return min(stor[query_row][query_glass], 1.0)

        
