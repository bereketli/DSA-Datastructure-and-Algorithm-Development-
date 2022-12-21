class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        output=[]
       
        for i in range(len(nums)):
            wanted =-1 * nums[i]
            l =i +1 
            r = len(nums) - 1
            while l < r:
                
                while l < r and nums[l] + nums[r] < wanted:
                   l+=1
                if l < r and nums[l] + nums[r] == wanted:
                    if [-1 * wanted, nums[l], nums[r]] not in output:
                          output.append([-1 * wanted, nums[l], nums[r]])
                r -=1
        return output
            
            
            
            
            
        
        """
        wnated=17
        nums = [1,2,4,13]
        

        
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        