class Solution(object):
    def maxOperations(self, nums, k):
        nums.sort()
        operation=0
        i=0
        j=len(nums)-1
        while i<j:
         
            while i<j and nums[i]+nums[j]>=k:
                
                if nums[i]+nums[j]==k:
                    operation+=1
                    j-=1
                    break
                j-=1
            i+=1
        return operation
            
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        