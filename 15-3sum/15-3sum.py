class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        output =[]
       
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i - 1]:
                continue
            l , r = i + 1 , len(nums) - 1
            
                    
            while l < r:
               
                two_sum =  nums[l] + nums[r] 
                if two_sum == -1 * nums[i]:
                       output.append([nums[i],nums[l], nums[r]])
                       l +=1
                      
                       while l<len(nums) and nums[l]==nums[l-1]:
                          l +=1
                elif two_sum < -1 * nums[i]:
                    l +=1
                else: 
                    r -=1
        return output
                    
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        