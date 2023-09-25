class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        al = [[] for _ in range(n)]
        con = [0] * n

        for edge in edges:
            al[edge[0]].append(edge[1])
            al[edge[1]].append(edge[0])

        dp = [[-1 for _ in range(2)] for _ in range(n)]

        def solve(node, par, use):
            u = con[node] * price[node] // 2
            uu = con[node] * price[node]
            if dp[node][use] != -1:
                return dp[node][use]
            for v in al[node]:
                if v != par:
                    uu += solve(v, node, 0)
            if use == 1:
                dp[node][use] = uu
                return uu

            for v in al[node]:
                if v != par:
                    u += solve(v, node, 1)
            dp[node][use] = min(u, uu)
            return dp[node][use]

        def dfs(s, d, al, par):
            if s == d:
                return True
            for v in al[s]:
                if v != par:
                    if dfs(v, d, al, s):
                        con[v] += 1
                        return True
            return False

        for trip in trips:
            aa, bb = trip[0], trip[1]
            con[aa] += 1
            dfs(aa, bb, al, -1)

        return solve(0, -1, 0)


        
