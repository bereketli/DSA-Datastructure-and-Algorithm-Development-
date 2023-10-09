class Solution:
    def __init__(self):
        self.mod = 1000000007
        self.dx = [-2, -1, 1, 2, 2, 1, -1, -2]
        self.dy = [1, 2, 2, 1, -1, -2, -2, -1]
        self.dp = [[[ -1 for _ in range(5002)] for _ in range(4)] for _ in range(5)]

    def knightDialer(self, n: int) -> int:
        nums = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [-1, 9, -1]]
        ans = 0

        for i in range(4):
            for j in range(3):
                if nums[i][j] != -1:
                    ans = (ans + self.solve(nums, i, j, n - 1)) % self.mod

        return ans

    def solve(self, nums, i, j, n):
        if i < 0 or j < 0 or i >= 4 or j >= 3 or nums[i][j] == -1:
            return 0

        if n == 0:
            return 1

        if self.dp[i][j][n] != -1:
            return self.dp[i][j][n]

        t = 0
        for k in range(8):
            x = i + self.dx[k]
            y = j + self.dy[k]
            t = (t + self.solve(nums, x, y, n - 1)) % self.mod

        self.dp[i][j][n] = t % self.mod
        return self.dp[i][j][n]

