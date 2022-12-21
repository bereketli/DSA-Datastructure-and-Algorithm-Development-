class Solution(object):
    def sortColors(self, nums):
       
          for color in range(len(nums)):
            j=color-1
            current=nums[color]
            while j>=0 and current<nums[j]:
                nums[j+1]=nums[j]
                j-=1
            nums[j+1]=current
          return nums            
      
        