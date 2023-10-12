import collections

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        q = collections.deque()
        distance = [float('inf')] * n
        
        adj = [[] for _ in range(n)]
        for arr in flights:
            source, destination, price = arr
            adj[source].append((destination, price))
        
        q.append((src, 0, 0))
        distance[src] = 0
        
        while q:
            node, prevPrice, oldK = q.popleft()
            if oldK > k:
                continue
            for dest, newdistance in adj[node]:
                if oldK <= k and prevPrice + newdistance < distance[dest]:
                    distance[dest] = prevPrice + newdistance
                    q.append((dest, distance[dest], oldK + 1))
        
        return -1 if distance[dst] == float('inf') else distance[dst]
