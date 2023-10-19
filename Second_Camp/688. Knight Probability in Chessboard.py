class Solution:
    def __init__(self):
        self.moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[0.0 for _ in range(n)] for _ in range(n)]
        dp[row][column] = 1.0

        for move in range(1, k + 1):
            ndp = [[0.0 for _ in range(n)] for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    for m in self.moves:
                        nr, nc = r + m[0], c + m[1]
                        if self.isValid(nr, nc, n):
                            ndp[r][c] += dp[nr][nc] / 8.0
            dp = ndp

        prob = 0.0
        for r in range(n):
            for c in range(n):
                prob += dp[r][c]

        return prob

    def isValid(self, r: int, c: int, n: int) -> bool:
        return 0 <= r < n and 0 <= c < n

        
