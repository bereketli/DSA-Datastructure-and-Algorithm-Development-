import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        pq = []
        N = len(matrix)
        for i in range(min(N, k)):
            heapq.heappush(pq, [matrix[i][0], i, 0])
        
        while k > 0:
            element = heapq.heappop(pq)
            k -= 1
            if k == 0:
                return element[0]
   
            if element[2] + 1 < len(matrix[0]):
                heapq.heappush(pq, [matrix[element[1]][element[2] + 1], element[1], element[2] + 1])
        
        return -1
