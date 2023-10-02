class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n = len(dungeon)
        m = len(dungeon[0])
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        return self.getVal(dungeon, 0, 0, dp)

        
    def getVal(self, mat, i, j, dp):
        n = len(mat)
        m = len(mat[0])
        
        if i == n or j == m:
            return float('inf')

        if i == n - 1 and j == m - 1:
            return -mat[i][j] + 1 if mat[i][j] <= 0 else 1

        if dp[i][j] != -1:
            return dp[i][j]

        Right = self.getVal(mat, i, j + 1, dp)
        Down = self.getVal(mat, i + 1, j, dp)

        minHealthRequired = min(Right, Down) - mat[i][j]

        dp[i][j] = 1 if minHealthRequired <= 0 else minHealthRequired
        return dp[i][j]

    
        
