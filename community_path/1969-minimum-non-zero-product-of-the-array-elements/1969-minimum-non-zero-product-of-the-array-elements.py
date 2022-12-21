class Solution(object):
    def minNonZeroProduct(self, p):
        if p<=1:
            return 1
        mod=1000000007
        last_value=pow(2,p)-1
        value=last_value-1
        n=value/2
        
            
        def pow_value(value_iterate,n):
            if n==0:
                return 1
            memo=pow_value(value,n/2)%mod
            if n%2==0:
                return (memo**2)%mod
            else:
                return ((memo**2)%mod*value)%mod
        result=pow_value(value,n)
        return (result*last_value)%mod
            
        
        """
        :type p: int
        :rtype: int
        """
        