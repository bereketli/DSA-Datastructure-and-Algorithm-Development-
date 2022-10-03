class Solution(object):
    def totalSteps(self, nums):
        output =0
        stack =[]
        for i in range(len(nums)-1,-1,-1):
            count =0
            while stack and stack[-1][0] < nums[i]:
                popped_index  =stack.pop()[1]
                count = max(count + 1 , popped_index)  
               
            stack.append([nums[i], count])
            output = max(output, count)
           
        return output
        """
        :type nums: List[int]
        :rtype: int    
        """
        