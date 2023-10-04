class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        if len(triangle) == 1:
            return triangle[0][0]

        dp = [0] * len(triangle)
        dp[0] = triangle[0][0]
        return self.minimumTotalHelper(triangle, dp, 1)

    def minimumTotalHelper(self, triangle, dp, lvlidx):
        row = triangle[lvlidx]
        pre = dp[0]
        dp[0] += row[0]
        for i in range(1, lvlidx):
            temp = dp[i]
            dp[i] = row[i] + min(pre, dp[i])
            pre = temp

        dp[lvlidx] = pre + row[lvlidx]

        if lvlidx + 1 == len(triangle):
            res = dp[0]
            for i in range(1, lvlidx + 1):
                res = min(res, dp[i])
            return res

        return self.minimumTotalHelper(triangle, dp, lvlidx + 1)
        
