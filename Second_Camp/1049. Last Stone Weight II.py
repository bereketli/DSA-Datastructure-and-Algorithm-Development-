class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        S = sum(stones)
        S2 = 0
        n = len(stones)

        # Maximizing S2
        dp = [[False] * (n + 1) for _ in range(S // 2 + 1)]

        for i in range(n + 1):
            dp[0][i] = True

        for i in range(1, n + 1):
            for s in range(1, S // 2 + 1):
                if dp[s][i - 1] or (s >= stones[i - 1] and dp[s - stones[i - 1]][i - 1]):
                    dp[s][i] = True
                    S2 = max(s, S2)

        return S - 2 * S2

        
