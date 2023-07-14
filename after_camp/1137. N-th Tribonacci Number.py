class Solution:
    def tribonacci(self, n: int) -> int:
        def tri_bo(num):
            if num == 0:
                return 0
            elif num <= 2:
                return 1
            
            dp = [0] * (num + 1)
            dp[1] = 1
            dp[2] = 1
            
            for i in range(3, num + 1):
                dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
            
            return dp[num]
        return tri_bo(n)
