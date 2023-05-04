import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify (self.heap )
        self.kthlargest = self.find_kth(self.heap,self.k) if len(self.heap) >= k else -(10**5)
    def find_kth(self, heap, k) -> int:
        while len(heap) > k:
            heapq.heappop(heap)
        return heap[0]

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if val > self.kthlargest:
           self.kthlargest = self.find_kth(self.heap,self.k)
        return self.kthlargest 
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
