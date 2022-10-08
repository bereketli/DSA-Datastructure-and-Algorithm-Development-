class Solution(object):
    def subArrayRanges(self, nums):
        summed =0
        for i in range(len(nums)):
             maxi =-float("inf")
             mini =float("inf")
             for j in range(i, len(nums)):
                mini =min(mini, nums[j])
                maxi =max(maxi, nums[j])
                summed += (maxi - mini)
              
             
        return summed
        """
        :type nums: List[int]
        :rtype: int
        """
        