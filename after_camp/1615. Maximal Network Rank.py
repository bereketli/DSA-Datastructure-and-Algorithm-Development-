class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        maxrank = 0
        adjecency = [] 
        for i in range(n):
            adjecency.append(set())
        for edge in roads:
            adjecency[edge[0]].add(edge[1])
            adjecency[edge[1]].add(edge[0])
            
        for i in range(n):
            for j in range(i + 1,n):
                rank = len(adjecency[i]) + len(adjecency[j])
            
                if j in adjecency[i] and i in adjecency[j]:
                    rank -= 1
                maxrank = max(maxrank, rank)
        return maxrank

        
