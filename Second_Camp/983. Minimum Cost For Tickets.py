class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        maxDay = days[-1]
        travelDay = [False] * (maxDay + 1)

        for day in days:
            travelDay[day] = True

        dp = [0] * (maxDay + 1)
        dp[0] = 0

        for i in range(1, maxDay + 1):
            if not travelDay[i]:
                dp[i] = dp[i - 1]
                continue

            dp[i] = costs[0] + dp[i - 1]
            dp[i] = min(dp[max(0, i - 7)] + costs[1], dp[i])
            dp[i] = min(dp[max(0, i - 30)] + costs[2], dp[i])

        return dp[maxDay]
  
