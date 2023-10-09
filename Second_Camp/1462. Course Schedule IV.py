class Solution:
    def checkIfPrerequisite(self, n, prerequisites, queries):
        dp = [[float('inf')] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 0
        
        for edge in prerequisites:
            dp[edge[0]][edge[1]] = 1
        
        for mid in range(n):
            for source in range(n):
                for destiny in range(n):
                    if dp[source][destiny] > dp[source][mid] + dp[mid][destiny]:
                        dp[source][destiny] = dp[source][mid] + dp[mid][destiny]

        
        answer = []
        for query in queries:
            answer.append(dp[query[0]][query[1]] < float('inf'))
        
        return answer
