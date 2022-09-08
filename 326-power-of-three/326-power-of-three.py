class Solution(object):
    def isPowerOfThree(self, n):
        if n<=0:
            return False
        def pow_three(num,divisor):
            if num==1:
                
                return True
            elif num%3==0:
                if num<divisor:
                    return pow_three(num,divisor/3)
                else: return pow_three(float(num/divisor),divisor*3)
            else:
                
                return False
        return pow_three(n,3)
        
        
        """
        :type n: int
        :rtype: bool
        """
        