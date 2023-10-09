import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = [[] for _ in range(n)]

        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        prob = self.dijkstra(graph, start, n)
        return prob[end]

    def dijkstra(self, graph, src, n):
        prob = [0.0] * n
        prob[src] = 1.0
        pq = [(-1.0, src)]

        while pq:
            cur_prob, u = heapq.heappop(pq)
            cur_prob = -cur_prob

            if cur_prob < prob[u]:
                continue

            for v, edge_prob in graph[u]:
                new_prob = cur_prob * edge_prob
                if new_prob > prob[v]:
                    prob[v] = new_prob
                    heapq.heappush(pq, (-new_prob, v))

        return prob

    

        
