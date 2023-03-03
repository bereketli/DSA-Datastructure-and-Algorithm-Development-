class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left= 0
        maxsum = -float("inf")
        windowsum = 0
        for right in range(len(nums)):
            if right - left + 1 < k:
                windowsum += nums[right]
                
            else:
                windowsum += nums[right]
                maxsum = max(maxsum,windowsum)
                windowsum -= nums[left]
                left += 1
        return maxsum/k



            
