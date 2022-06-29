class Solution(object):
    def twoSum(self, nums, target):
        output=[]
        
        for i in range(len(nums)):
            find=target-nums[i]
            if (find in nums[i+1:] and nums.index(find) not in output):
                nums[i]="a"
                       
                next= nums.index(find)
                output.extend((i,next))
        return output
        
            
  
        