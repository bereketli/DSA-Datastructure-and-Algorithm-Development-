class Solution(object):
    def checkSubarraySum(self, nums, k):
        prefix ={0:-1}
        summed =0
        for i in range(len(nums)):
            summed += nums[i]
            if summed % k in prefix:
                if i - prefix[summed % k] > 1:
                    return True
                
            else:
                prefix[summed % k] = i
        return False
        
        
         
          
                
  