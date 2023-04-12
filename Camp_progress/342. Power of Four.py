class Solution(object):
    def isPowerOfFour(self, n):
        if n<=0:
            return False
        else:
            def pow_four(num):
                if num==1:
                    return True
                if num%4==0:
                    return pow_four(num/4)
                else:
                    return False
        return pow_four(n)
        """
        :type n: int
        :rtype: bool
        """
        
