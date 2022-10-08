class Solution(object):
    def mostCompetitive(self, nums, k):
        stack =[]
        for i in range(len(nums)):
            while stack and len(stack) > k - (len(nums) - i) and stack[-1] > nums[i]:
                stack.pop()
            stack.append(nums[i])
        return stack[:k]
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
                                       
            
            














            
            
            
            
            




            
            
            
          