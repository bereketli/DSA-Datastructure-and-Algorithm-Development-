class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        def max_generated(num):
            if num == 0:
                return 0
            
            dp = [0] * (n + 1)
            dp[1] = 1
            for i in range(2, num + 1):
                if i % 2 == 0:
                    dp[i] = dp[i // 2]
                else:
                    dp[i] = dp[i // 2] + dp[i // 2 + 1]
            
            return max(dp)
        
        return max_generated(n)
