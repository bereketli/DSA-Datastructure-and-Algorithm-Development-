class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(idx, role):
            if idx >= len(prices):
                return 0
            if (idx, role) in memo:
                return memo[(idx, role)]

            passing = dp(idx + 1, role)
            if role:
                buy = dp(idx + 1, not role) - prices[idx]
                memo[(idx, role)] =  max(buy, passing)

            else:
                sell = dp(idx + 2, not role) + prices[idx]
                memo[(idx, role)] = max(sell, passing)

            return memo[(idx, role)]
        return dp(0, True)

    
