class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0
        dp = [[0] * 1001 for _ in range(n)]

        for i in range(1, n):
            for j in range(i):
                diff = nums[j] - nums[i] + 500
                dp[i][diff] = dp[j][diff] + 1
                max_len = max(max_len, dp[i][diff])

        return max_len + 1







        
