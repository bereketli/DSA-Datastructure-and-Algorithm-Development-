import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []
        if not nums1 or not nums2 or k <= 0:
            return result

        minHeap = []
        for i in range(min(k, len(nums1))):
            heapq.heappush(minHeap, (nums1[i] + nums2[0], nums1[i], nums2[0], 0))

        while k > 0 and minHeap:
            sum_val, num1, num2, idx = heapq.heappop(minHeap)
            result.append([num1, num2])
            k -= 1

            if idx + 1 < len(nums2):
                heapq.heappush(minHeap, (num1 + nums2[idx + 1], num1, nums2[idx + 1], idx + 1))

        return result
