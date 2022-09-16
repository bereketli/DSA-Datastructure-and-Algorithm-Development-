class Solution(object):
    def minSubArrayLen(self, target, nums):
        length=float("inf")
        prefix_sum=0
        left=0
        for i in range(len(nums)):
            prefix_sum+=nums[i]
            while left<=i and prefix_sum>=target:
               
                length=min(i-left+1,length)
                prefix_sum-=nums[left]    
                left+=1
        return length  if length!=float("inf") else 0
                
            
                
            
        
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        