class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        prefix=[nums[0]]
        result=[]
        for i in range(1,len(nums)):
            
            prefix.append(prefix[i - 1] + nums[i])
        for i in range(len(nums)):
            
            sumgreater = (prefix[len(nums) - 1] - prefix[i]) - (nums[i] *(len(nums) - i -1))
            
            sumsmaller = (((i+1) * nums[i]) - prefix[i])  if i >0  else 0
            result.append(sumgreater + sumsmaller)
        return result
            
            
       