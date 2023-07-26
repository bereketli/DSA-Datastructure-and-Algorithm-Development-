class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = [[] for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        return self.dfs(-1, 0, graph, hasApple)
    
    def dfs(self, prev, curr, graph, hasApple):
        ans = 0
        for x in graph[curr]:
            if x != prev:
                res = self.dfs(curr, x, graph, hasApple)
                if res > 0 or hasApple[x]:
                    ans += (res + 2)
        return ans
