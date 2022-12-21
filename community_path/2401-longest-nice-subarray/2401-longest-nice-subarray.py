class Solution(object):
    def longestNiceSubarray(self, nums):
        l, maxlen, nice =0, 1, nums[0]
        for r in range(1, len(nums)):
            
            while l < r and nums[r] & nice != 0:
                nice ^= nums[l]
                l +=1
            nice ^= nums[r]
            maxlen =max(maxlen, r -l +1)
        return maxlen
                  
        
        """
        :type nums: List[int]
        :rtype: int
        """
        