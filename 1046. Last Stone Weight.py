import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            heavy_1 = heapq.heappop(stones)
            heavy_2 = heapq.heappop(stones)
            if heavy_1 - heavy_2:
                heapq.heappush(stones, heavy_1 - heavy_2)
        return -stones[0] if stones else 0
