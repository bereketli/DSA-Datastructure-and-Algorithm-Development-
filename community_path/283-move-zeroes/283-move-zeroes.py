class Solution(object):
    def moveZeroes(self, nums):
        left=-1
        right=0
        for right in range(len(nums)):
            if left==-1 and nums[right]==0:
                left=right
                continue
            if left>-1 and nums[left]==0 and nums[right]!=0:
               
                nums[left]=nums[right]
                nums[right]=0
                left+=1
              
            
            
        return nums
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        