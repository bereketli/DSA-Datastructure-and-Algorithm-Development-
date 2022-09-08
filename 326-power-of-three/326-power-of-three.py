class Solution(object):
    def isPowerOfThree(self, n):
        if n<=0:
            return False
        def pow_three(n):
            if n==1:
                
                return True
            elif n%3==0:
                return pow_three(n/3)
            else:
                
                return False
        return pow_three(n)
        
        
        """
        :type n: int
        :rtype: bool
        """
        