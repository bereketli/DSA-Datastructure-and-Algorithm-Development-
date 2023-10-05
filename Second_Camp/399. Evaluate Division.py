from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        gr = defaultdict(dict)

        for (dividend, divisor), value in zip(equations, values):
            gr[dividend][divisor] = value
            gr[divisor][dividend] = 1.0 / value

        def dfs(node, dest, vis, temp):
            if node == dest:
                return temp
            vis.add(node)
            for ne, val in gr[node].items():
                if ne not in vis:
                    result = dfs(ne, dest, vis, temp * val)
                    if result != -1.0:
                        return result
            return -1.0

        ans = [dfs(dividend, divisor, set(), 1.0) if dividend in gr and divisor in gr else -1.0 for dividend, divisor in queries]

        return ans
