class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        sum_T =sum(nums)
        prefix =0
        result =[]
        for i in range(len(nums)):
            prefix += nums[i]
            
            sumgreater = (sum_T - prefix) - (nums[i] *(len(nums) - 1 -i))
            
            sumsmaller = (((i+1) * nums[i]) - prefix)  
            result.append(sumgreater + sumsmaller)
        return result
            
            
       