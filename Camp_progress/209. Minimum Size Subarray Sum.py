class Solution(object):
    def minSubArrayLen(self, target, nums):
        minlen = float("inf")
        prefi,l = 0, 0
        for i, value in enumerate(nums):
             prefi +=value
             
             while prefi >= target:
                if prefi >= target:
                    minlen = min(minlen, i - l + 1)
                prefi -= nums[l]
                l +=1
                
                
        return minlen if minlen != float("inf") else 0
                  


                
            
                
            
        
        """
        minlen =1
        sum =6
        target = 7, nums = [2,3,1,2,4,3]
        l =1  r =3

        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        