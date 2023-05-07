class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * n
        nums = nums + nums
        stack = []
       
        for i in range(n*2):
          
            while stack and nums[stack[-1]] < nums[i]:
                popped = stack.pop()
                output[popped] = nums[i]
            if i < n:
                stack.append(i)
        while stack:
            popped = stack.pop()
            output[popped] = -1
        return output
           
            
        
