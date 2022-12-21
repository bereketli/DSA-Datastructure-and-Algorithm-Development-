class Solution(object):
    def maxSumMinProduct(self, nums):
        modulo = pow(10,9) + 7
        prefix =[nums[0]]
        inc_mono =[]
        max_pro =0
        for i in range(1,len(nums)):
            prefix.append(prefix[i -1] + nums[i])
       
        for i in range(len(nums)):
            while inc_mono and nums[inc_mono[-1]] > nums[i]:
                popped = inc_mono.pop()
                previous = prefix[inc_mono[-1] ] if inc_mono else 0
                max_pro = max(max_pro,nums[popped] * (prefix[i - 1] - previous)) 
            inc_mono.append(i) 
      
        while inc_mono: 
            popped = inc_mono.pop()
            previous = prefix[inc_mono[-1]] if inc_mono else 0
            max_pro = max(max_pro, nums[popped] * (prefix[len(nums) - 1] - previous) )  
       
        return max_pro  % modulo
            

                
                
            
        """
        nums = [1,2,3,2]
        1 * 8
        2*7=14
        3 * 3
        2
        :type nums: List[int]
        :rtype: int
        """
        