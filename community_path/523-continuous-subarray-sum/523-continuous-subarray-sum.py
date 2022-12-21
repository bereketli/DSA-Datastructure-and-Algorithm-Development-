class Solution(object):
    def checkSubarraySum(self, nums, k):
          prefix_store = {0:-1}
          pre_sum =0
          for i,num in enumerate(nums):
                pre_sum +=num 
                if pre_sum % k not in prefix_store:
                    prefix_store[pre_sum % k] = i
                else:
                    if i-prefix_store[pre_sum % k] >1:
                        return True
          return False
                
          
                
  