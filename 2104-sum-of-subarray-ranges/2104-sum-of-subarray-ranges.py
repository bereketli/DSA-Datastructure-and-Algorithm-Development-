class Solution(object):
    def subArrayRanges(self, nums):
        inc_mono =[]
        dec_mono =[]
        def inc (num):
            while inc_mono and inc_mono[-1] > num:
                inc_mono.pop()
            inc_mono.append(num)
        def dec (num):
          
            while dec_mono and dec_mono[-1] < num:
                dec_mono.pop()
            dec_mono.append(num)
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
        