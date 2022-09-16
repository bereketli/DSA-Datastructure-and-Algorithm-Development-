class Solution(object):
    def checkSubarraySum(self, nums, k):
          remin_index={0:0}
          summed=0
          for index,num in enumerate(nums):
                
                summed+=num
               
                if summed%k not in remin_index:
                    remin_index[summed%k]=index+1
                else:
                    if index-remin_index[summed%k]+1>1:
                        return True
          return False
                
                
  