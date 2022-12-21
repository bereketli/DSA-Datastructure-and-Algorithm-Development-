class Solution(object):
    def minSwaps(self, s):
        count =[0,0]
        output, l, r =0, 0, len(s) - 1
        while l < r:
           
            if s[l] =="]":
                count[1] +=1
            else:
                count[0] +=1
            
            while s[r] != "[":
                r -= 1
            if count[1] > count[0]:
                output +=1
                count[0] +=1
                count[1] -=1
                r -=1
            l +=1
        return output
                
        
        
        """
        :type s: str
        :rtype: int
        """
        