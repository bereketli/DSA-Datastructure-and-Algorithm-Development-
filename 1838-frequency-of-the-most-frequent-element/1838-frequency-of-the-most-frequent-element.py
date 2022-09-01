class Solution(object):
    def maxFrequency(self, nums, k):
        nums.sort()
        maxFrequency=l=r=0
        tempoK=k
        while r<len(nums):
            if len(nums)==1:
                return 1
            if l==r:
                r=l+1
           
            while (nums[r]-nums[r-1])*(r-l)>tempoK:
              
                
               
                if tempoK<k:
                   
                   tempoK+=(nums[r-1]-nums[l])
                l+=1
                
            maxFrequency=max(maxFrequency,(r-l+1))
            
            tempoK-=(nums[r]-nums[r-1])*(r-l)
            r+=1
           
        return maxFrequency
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        