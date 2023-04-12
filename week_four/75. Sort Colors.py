class Solution(object):
    def sortColors(self, nums):
      count = [0] * 3
      
      for num in nums:
          count[num] +=1
      output =0
      for i, value in enumerate(count):
          output += value
        
          for j in range(output - value, output):
              nums[j] =i
      
      return output
       

              
       
          
