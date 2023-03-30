class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        offset = 10 ** 4
        counter = [0] * ((2 * (10 ** 4)) + 1)
        for num in nums:
            counter [num + offset] += 1
        count = 0
        for i in range(len(counter) - 1, -1,  -1):
            if counter[i] > 0:
                count += counter[i]
               
            if count >= k:
                return (i - offset)

